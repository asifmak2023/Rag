# 09. Monitor, then recommend improvements

Shipping is day 1. The posting asks you to watch performance and suggest
changes. That is MLOps at the scale of a consulting team: not a 50-person
platform, a disciplined service.

## What to log on every request

- request_id
- model_version
- latency_ms
- n_features / payload size
- predicted label and probability
- hashed input (not raw PII)
- error class if any

Lab 09A. Middleware timer (FastAPI):

```python
import time, logging
from fastapi import Request

log = logging.getLogger("infer")

@app.middleware("http")
async def timed(request: Request, call_next):
    t0 = time.perf_counter()
    resp = await call_next(request)
    dt = (time.perf_counter() - t0) * 1000
    log.info("path=%s status=%s ms=%.1f", request.url.path, resp.status_code, dt)
    return resp
```

## Metrics that matter after go-live

Live metrics (always):

- QPS, p95 latency, error rate
- Output distribution: mean probability per hour
- Fraction of requests rejected by schema

Delayed metrics (when labels arrive):

- Daily F1 / MAE vs last week
- Calibration: among scores 0.8-0.9, did ~85% convert?

## Drift (the improvement engine)

Data drift: input stats moved (income mean jumped).
Concept drift: same inputs, different labels (new competitor).

Lab 09B. Cheap drift alarm:

```python
import numpy as np

def psi(expected, actual, bins=10):
    e_perc = np.histogram(expected, bins=bins)[0] + 1e-6
    a_perc = np.histogram(actual, bins=bins, range=(expected.min(), expected.max()))[0] + 1e-6
    e_perc, a_perc = e_perc / e_perc.sum(), a_perc / a_perc.sum()
    return float(np.sum((a_perc - e_perc) * np.log(a_perc / e_perc)))
```

PSI above ~0.2 on a key feature: investigate. Do not auto-retrain blindly.

## Retraining policy you can defend

1. Labels accumulate for N days.
2. Retrain on a schedule (weekly) or on a drift alarm, not both at random.
3. Champion / challenger: new model must beat old on a locked test window
   and pass latency budget.
4. Canary 10% traffic, then 100%.
5. Keep previous image to roll back in one command.

## Recommendations (practice writing them)

Each week write a 6-line note:

```
What we saw:
What it might mean:
What I propose:
Cost of doing it:
Cost of ignoring it:
How we will know it worked:
```

That is the communication skill on the posting.

## Optional tools (names only, then one lab)

- MLflow or just folders + json for experiment tracking
- Prometheus + a `/metrics` gauge for latency
- Great Expectations or a SQL check for data quality

Lab 09C. Add `prometheus_client` histogram of `/predict` latency.
You do not need a full Grafana stack. Knowing the metric exists is enough.

## Pass / fail

You can talk for 5 minutes: "Here is how I know the model is healthy,
here is how I know the data moved, here is how I ship a better version
without taking the product down."
