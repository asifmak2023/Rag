# 08. Deploy: containers, microservices, cloud

If it is not an API, it is a demo. This chapter is the difference between
a student and a Sr. AI Engineer on this posting.

## Architecture you will actually ship

```
client -> FastAPI (uvicorn) -> load model once -> predict
                |
                +-- /health  (liveness)
                +-- /ready   (model loaded)
                +-- /predict (POST JSON)
```

One process, one model, one container. That is a microservice.

## Lab 08A. FastAPI model service

File: `labs/serve/app.py`

```python
from pathlib import Path
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL_PATH = Path("model.joblib")
app = FastAPI(title="churn-score")
model = None

class PredictIn(BaseModel):
    features: list[float] = Field(min_length=1, max_length=128)

class PredictOut(BaseModel):
    prob: float
    label: int

@app.on_event("startup")
def load_model():
    global model
    if not MODEL_PATH.exists():
        raise RuntimeError("model.joblib missing")
    model = joblib.load(MODEL_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"ready": model is not None}

@app.post("/predict", response_model=PredictOut)
def predict(body: PredictIn):
    if model is None:
        raise HTTPException(503, "model not loaded")
    try:
        import numpy as np
        x = np.asarray(body.features, dtype=float).reshape(1, -1)
        prob = float(model.predict_proba(x)[0, 1])
    except Exception:
        raise HTTPException(400, "bad features")
    return PredictOut(prob=prob, label=int(prob >= 0.5))
```

Run:

```bash
# train a tiny model first, write model.joblib next to app.py
uvicorn labs.serve.app:app --host 0.0.0.0 --port 8000
```

Call:

```bash
curl -s http://127.0.0.1:8000/health
curl -s http://127.0.0.1:8000/predict \
  -H 'content-type: application/json' \
  -d '{"features":[0,1,0,0,1]}'
```

Fix the feature length to match your model. Document it in `README`.

## Lab 08B. Docker

File: `labs/serve/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements-serve.txt .
RUN pip install --no-cache-dir -r requirements-serve.txt
COPY app.py model.joblib ./
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

`requirements-serve.txt` should be small: `fastapi uvicorn joblib scikit-learn numpy`.
Do not copy torch into an sklearn service.

```bash
docker build -t churn-score:v1 labs/serve
docker run --rm -p 8000:8000 churn-score:v1
```

Interview sentences:

- Image is immutable. Version it `v1`, `v2`.
- Model weights live in the image for v1. Later, mount a volume or pull
  from object storage.
- Health checks belong in the orchestrator (compose, k8s, systemd).

## Cloud, without fake expertise

You do not need AWS certification. You need a true story:

1. Container runs the same locally and in the cloud.
2. Put it on one VM (IaaS) or Cloud Run / App Service / ECS.
3. Object storage for datasets and model artifacts.
4. Secrets in env vars, not in git.
5. HTTPS at the load balancer, not inside your Python if you can avoid it.

If asked "AWS or GCP?": "The model does not care. I containerize first."

## Integrate with a product (their first responsibility)

Pretend a billing app needs a churn score.

- Product calls `POST /predict` with a customer feature vector.
- You do not put SQL inside the model service if you can help it.
- A batch job can score everyone nightly and write to a table the
  product already reads.

That is integration. Draw it on paper before the interview.

## PyTorch serving extras

- `model.eval()` and `torch.no_grad()` on the request path
- Warmup one dummy tensor at startup so first real request is not slow
- Pin CPU threads if you co-locate with other services

## Pass / fail

A stranger can:

```bash
docker run -p 8000:8000 your-image
curl /health
curl /predict
```

and get a JSON probability. If they need your laptop, you failed.
