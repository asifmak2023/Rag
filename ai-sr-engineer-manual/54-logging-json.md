# 54. JSON logs (so you can grep production later)

`print` is for labs. Services log one JSON object per request.

```python
import json, time, logging
log = logging.getLogger("infer")

def log_infer(request_id, ms, n, version, status):
    log.info(json.dumps({
        "request_id": request_id,
        "latency_ms": round(ms, 2),
        "n_features": n,
        "model_version": version,
        "status": status,
    }))
```

Do not log CNIC, phone, raw tokens. Hash if you must join later.

Interview: "I can tell you p95 from logs without a vendor APM on day
one. Then we add Prometheus if the service matters."

Pass / fail: one request produces one line you could ship to grep.
