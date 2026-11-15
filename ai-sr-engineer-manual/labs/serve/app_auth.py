import os

from fastapi import Depends, FastAPI, Header, HTTPException

API_KEY = os.getenv("USER_MODEL_API_KEY", "dev-only-change-me")
app = FastAPI(title="auth-sketch")


def require_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="unauthorized")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(_auth: None = Depends(require_key)):
    return {"prob": 0.0, "note": "sketch only; wire to model in app.py"}
