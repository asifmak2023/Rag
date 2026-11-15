from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "model.joblib"


def test_health_ready_predict():
    if not ART.exists():
        from src.train import main

        main()
    from src.serve import app

    body = {
        "tenure_months": 12,
        "monthly_charges": 85.0,
        "total_charges": 1020.0,
        "contract": "month-to-month",
        "internet": "fiber",
        "senior": 0,
        "request_id": "demo",
    }
    with TestClient(app) as c:
        assert c.get("/health").json()["status"] == "ok"
        ready = c.get("/ready").json()
        assert ready["ready"] is True
        r = c.post("/predict", json=body)
        assert r.status_code == 200
        out = r.json()
        assert 0.0 <= out["prob"] <= 1.0
        assert out["label"] in (0, 1)
        assert out["model_version"]
        assert out["request_id"] == "demo"
