from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get("your_server_ip:8000")
        self.assertEqual(response.status_code, 404)
