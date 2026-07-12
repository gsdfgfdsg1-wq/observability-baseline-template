import unittest
from baseline import generate


class BaselineTests(unittest.TestCase):
    def service(self): return {"name": "api", "owner": "platform", "environment": "prod"}
    def test_generates_red_metrics(self): self.assertIn("api_errors_total", generate(self.service())["metrics"])
    def test_adds_trace_resource_attributes(self): self.assertEqual(generate(self.service())["resource"]["service.name"], "api")
    def test_reports_missing_required_service_metadata(self):
        report = generate({"name": "api"})
        self.assertIn("owner", report["missing"])
        self.assertFalse(report["valid"])


if __name__ == "__main__": unittest.main()
