import json
import sys

DS = {"type": "prometheus", "uid": "prometheus"}


def panel(pid, title, x, y, w, h, targets, unit=None, panel_type="timeseries", extra=None):
    p = {
        "id": pid,
        "title": title,
        "type": panel_type,
        "datasource": DS,
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "targets": [
            {"refId": chr(ord("A") + i), "datasource": DS, "expr": t[0], "legendFormat": t[1], "range": True}
            for i, t in enumerate(targets)
        ],
        "fieldConfig": {"defaults": {"unit": unit or "short"}, "overrides": []},
        "options": {},
    }
    if extra:
        p.update(extra)
    return p


up_mappings = [{
    "type": "value",
    "options": {
        "1": {"text": "UP", "color": "green", "index": 0},
        "0": {"text": "DOWN", "color": "red", "index": 1},
    },
}]

dashboard = {
    "uid": "app-people",
    "title": "App People",
    "tags": ["app-people"],
    "timezone": "browser",
    "schemaVersion": 39,
    "version": 1,
    "refresh": "10s",
    "time": {"from": "now-15m", "to": "now"},
    "panels": [
        panel(1, "Service up", 0, 0, 4, 4,
              [('up{job="app-people"}', "up")], panel_type="stat",
              extra={"fieldConfig": {"defaults": {"mappings": up_mappings, "unit": "short"}, "overrides": []}}),
        panel(2, "Requests in flight", 4, 0, 4, 4,
              [("http_requests_in_progress", "in flight")], panel_type="stat"),
        panel(3, "Error rate (5xx share)", 8, 0, 4, 4,
              [('sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))', "5xx share")],
              unit="percentunit", panel_type="stat"),
        panel(4, "Request rate by route", 12, 0, 12, 8,
              [("sum by (route) (rate(http_requests_total[5m]))", "{{route}}")], unit="reqps"),
        panel(5, "Latency p50 / p95 / p99", 0, 8, 12, 8,
              [("histogram_quantile(0.50, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))", "p50"),
               ("histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))", "p95"),
               ("histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))", "p99")],
              unit="s"),
        panel(6, "Error responses by route and status", 0, 16, 24, 8,
              [('sum by (route, status) (rate(http_requests_total{status=~"[45].."}[5m]))', "{{route}} {{status}}")],
              unit="reqps"),
    ],
}

json.dump(dashboard, sys.stdout, indent=2)
sys.stdout.write("\n")
