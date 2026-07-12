# observability-baseline-template

A dependency-free generator for a service observability baseline: structured logs, RED metrics, trace resource attributes, and a simple availability SLO.

## Quick start

```bash
python baseline.py service.json
```

Service metadata supplies name, owner, environment, and an optional availability target. The generator reports missing metadata and emits baseline instrumentation and SLO configuration fields.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
