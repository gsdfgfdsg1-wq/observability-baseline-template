#!/usr/bin/env python3
"""Generate a minimal logs, metrics, traces, and SLO observability baseline."""
import argparse
import json
from pathlib import Path


def generate(service):
    name = service.get("name")
    required = ["name", "owner", "environment"]
    missing = [key for key in required if not service.get(key)]
    return {"valid": not missing, "missing": missing, "resource": {"service.name": name, "deployment.environment": service.get("environment")}, "logs": ["timestamp", "level", "message", "trace_id", "service"], "metrics": [f"{name}_requests_total", f"{name}_request_duration_ms", f"{name}_errors_total"], "slo": {"availability": service.get("availability_target", 0.99), "window_days": 30}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("service")
    args = parser.parse_args()
    print(json.dumps(generate(json.loads(Path(args.service).read_text())), indent=2))


if __name__ == "__main__": main()
