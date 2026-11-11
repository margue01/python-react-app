from unittest import TestCase

from app_people.app import setup_app


class TestMetrics(TestCase):

    def setUp(self):
        self.client = setup_app().test_client()

    def test_metrics_endpoint_exposes_prometheus_format(self):
        response = self.client.get('/app/metrics')

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.content_type.startswith('text/plain'))
        body = response.get_data(as_text=True)
        self.assertIn('http_requests_total', body)
        self.assertIn('http_request_duration_seconds', body)
        self.assertIn('http_requests_in_progress', body)

    def test_request_is_counted_with_route_template_and_status(self):
        self.client.get('/app/healthcheck')

        body = self.client.get('/app/metrics').get_data(as_text=True)
        self.assertIn('http_requests_total{method="GET",route="/app/healthcheck",status="200"}', body)

    def test_person_id_is_not_used_as_label(self):
        self.client.delete('/app/people/cardinality-check-id')

        body = self.client.get('/app/metrics').get_data(as_text=True)
        self.assertIn('route="/app/people/<person_id>"', body)
        self.assertNotIn('cardinality-check-id', body)
