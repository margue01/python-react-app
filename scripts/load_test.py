"""Generate traffic against the app so the observability dashboard has data.

Usage:
    python scripts/load_test.py --duration 60 --workers 8 --error-ratio 0.05

--error-ratio sets the share of requests that are deliberately bad (a PUT
without a JSON body, which the API answers with 400). Raise it to demonstrate
an error spike on the dashboard.
"""
import argparse
import random
import threading
import time
import urllib.error
import urllib.request

GOOD_PATHS = ['/app/people', '/app/healthcheck', '/app/version']


def send(base_url, method, path, body=None, headers=None):
    request = urllib.request.Request(base_url + path, data=body, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except urllib.error.URLError:
        return 0


def worker(base_url, deadline, error_ratio, counts, lock):
    while time.time() < deadline:
        if random.random() < error_ratio:
            # PUT without JSON content type -> 400 Bad Request
            status = send(base_url, 'PUT', '/app/people/load-test-id')
        else:
            status = send(base_url, 'GET', random.choice(GOOD_PATHS))
        with lock:
            counts[status] = counts.get(status, 0) + 1


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--url', default='http://127.0.0.1:8003')
    parser.add_argument('--duration', type=int, default=60, help='seconds to run')
    parser.add_argument('--workers', type=int, default=8, help='concurrent clients')
    parser.add_argument('--error-ratio', type=float, default=0.05, help='share of deliberately bad requests')
    args = parser.parse_args()

    counts, lock = {}, threading.Lock()
    deadline = time.time() + args.duration
    threads = [
        threading.Thread(target=worker, args=(args.url, deadline, args.error_ratio, counts, lock))
        for _ in range(args.workers)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    total = sum(counts.values())
    print(f'sent {total} requests in {args.duration}s')
    for status in sorted(counts):
        print(f'  status {status}: {counts[status]}')


if __name__ == '__main__':
    main()
