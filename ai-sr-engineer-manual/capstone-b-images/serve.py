from contextlib import asynccontextmanager
from pathlib import Path

import numpy as np
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from model import TinyCNN

ART = Path(__file__).resolve().parent / "artifacts" / "cnn.pt"
model = None
MODEL_VERSION = "tiny-cnn-v1"


@asynccontextmanager
async def lifespan(_app: FastAPI):
    global model
    if not ART.exists():
        raise RuntimeError("artifacts/cnn.pt missing; run python train.py")
    bundle = torch.load(ART, map_location="cpu", weights_only=False)
    m = TinyCNN()
    m.load_state_dict(bundle["state_dict"])
    m.eval()
    with torch.no_grad():
        m(torch.zeros(1, 1, 16, 16))
    model = m
    yield
    model = None


app = FastAPI(title="cnn-capstone", lifespan=lifespan)


class PredictIn(BaseModel):
    pixels: list[float] = Field(min_length=256, max_length=256)
    request_id: str = Field(default="local", min_length=1, max_length=64)


class PredictOut(BaseModel):
    prob_class1: float
    label: int
    model_version: str
    request_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": model is not None, "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictOut)
def predict(body: PredictIn):
    if model is None:
        raise HTTPException(status_code=503, detail="model not loaded")
    x = torch.tensor(body.pixels, dtype=torch.float32).view(1, 1, 16, 16)
    if not torch.isfinite(x).all():
        raise HTTPException(status_code=400, detail="non-finite pixels")
    with torch.no_grad():
        prob = torch.softmax(model(x), dim=1)[0]
    p1 = float(prob[1])
    return PredictOut(
        prob_class1=p1,
        label=int(p1 >= 0.5),
        model_version=MODEL_VERSION,
        request_id=body.request_id,
    )


def demo_payload():
    rng = np.random.default_rng(0)
    return rng.normal(size=256).tolist()
