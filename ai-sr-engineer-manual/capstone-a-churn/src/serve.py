from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import MODEL_VERSION
from .features import add_ratio_features

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "model.joblib"

app = FastAPI(title="churn-capstone")
bundle = None


class PredictIn(BaseModel):
    tenure_months: float = Field(ge=0, le=120)
    monthly_charges: float = Field(ge=0, le=500)
    total_charges: float = Field(ge=0, le=20000)
    contract: str
    internet: str
    senior: int = Field(ge=0, le=1)
    request_id: str = Field(default="local", min_length=1, max_length=64)


class PredictOut(BaseModel):
    prob: float
    label: int
    threshold: float
    model_version: str
    request_id: str


@app.on_event("startup")
def load_model():
    global bundle
    if not ART.exists():
        raise RuntimeError("artifacts/model.joblib missing; run python -m src.train")
    bundle = joblib.load(ART)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": bundle is not None, "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictOut)
def predict(body: PredictIn):
    if bundle is None:
        raise HTTPException(status_code=503, detail="model not loaded")
    row = pd.DataFrame(
        [
            {
                "tenure_months": body.tenure_months,
                "monthly_charges": body.monthly_charges,
                "total_charges": body.total_charges,
                "contract": body.contract,
                "internet": body.internet,
                "senior": body.senior,
            }
        ]
    )
    row = add_ratio_features(row)
    feats = bundle["features"]
    try:
        proba = float(bundle["model"].predict_proba(row[feats])[0, 1])
    except Exception as exc:
        raise HTTPException(status_code=400, detail="bad features") from exc
    thr = float(bundle["threshold"])
    return PredictOut(
        prob=proba,
        label=int(proba >= thr),
        threshold=thr,
        model_version=MODEL_VERSION,
        request_id=body.request_id,
    )
