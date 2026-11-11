import time

from flask import Response, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest

METRICS_PATH = '/app/metrics'
UNMATCHED_ROUTE = 'unmatched'

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'route', 'status'],
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'route', 'status'],
)
REQUESTS_IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'HTTP requests currently being handled',
)


def route_template():
    # Use the route pattern (e.g. /app/people/<person_id>), never the raw path,
    # so each person ID doesn't create a new time series.
    if request.url_rule is None:
        return UNMATCHED_ROUTE
    return request.url_rule.rule


def init_metrics(app):
    @app.before_request
    def start_request_metrics():
        request.metrics_start = time.perf_counter()
        REQUESTS_IN_PROGRESS.inc()

    @app.after_request
    def record_request_metrics(response):
        if request.path != METRICS_PATH:
            elapsed = time.perf_counter() - request.metrics_start
            labels = {
                'method': request.method,
                'route': route_template(),
                'status': str(response.status_code),
            }
            REQUEST_COUNT.labels(**labels).inc()
            REQUEST_LATENCY.labels(**labels).observe(elapsed)
        return response

    @app.teardown_request
    def finish_request_metrics(_exc):
        REQUESTS_IN_PROGRESS.dec()

    @app.route(METRICS_PATH)
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
