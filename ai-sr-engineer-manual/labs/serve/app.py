from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).with_name("model.joblib")
model = None
N_FEATURES = 8


@asynccontextmanager
async def lifespan(_app: FastAPI):
    global model
    if not MODEL_PATH.exists():
        raise RuntimeError("model.joblib missing; run train_tiny.py")
    model = joblib.load(MODEL_PATH)
    yield
    model = None


app = FastAPI(title="churn-score", lifespan=lifespan)


class PredictIn(BaseModel):
    features: list[float] = Field(min_length=N_FEATURES, max_length=N_FEATURES)
    request_id: str = Field(default="local", min_length=1, max_length=64)


class PredictOut(BaseModel):
    prob: float
    label: int
    request_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": model is not None}


@app.post("/predict", response_model=PredictOut)
def predict(body: PredictIn):
    if model is None:
        raise HTTPException(status_code=503, detail="model not loaded")
    x = np.asarray(body.features, dtype=float).reshape(1, -1)
    try:
        prob = float(model.predict_proba(x)[0, 1])
    except Exception as exc:
        raise HTTPException(status_code=400, detail="bad features") from exc
    return PredictOut(prob=prob, label=int(prob >= 0.5), request_id=body.request_id)
