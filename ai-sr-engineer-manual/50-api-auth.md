# 50. API keys, rate limits, and not being naive

Chapter 07 said do not open a model to the internet. This is the
minimum lock.

## Lab 50. Header key

File: `labs/serve/app_auth.py` is a sketch. Pattern:

```python
import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("USER_MODEL_API_KEY", "dev-only-change-me")

def require_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="unauthorized")
```

Put `Depends(require_key)` on `/predict`, not on `/health` (load
balancers need health without secrets).

Use `USER_MODEL_API_KEY` in the project. Do not read agent/platform
key names. Do not commit real keys. `.env.example`:

```
USER_MODEL_API_KEY=replace-me
```

## Other basics

- Reject bodies over a small byte size
- One request, one row unless you designed batch
- HTTPS at the reverse proxy
- Do not log the API key or the full feature vector if it is PII

## Rate limit (concept)

Token bucket per key. For v1, nginx `limit_req` or a slow Python
counter is enough to talk about. A public GPU endpoint without a cap
is a bill.

## Pass / fail

You can add a header check and explain why `/health` stays open.
