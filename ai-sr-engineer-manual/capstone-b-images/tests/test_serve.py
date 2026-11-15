from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "cnn.pt"


def test_health_ready_predict():
    if not ART.exists():
        from train import main

        main()
    from serve import app

    with TestClient(app) as c:
        assert c.get("/health").json()["status"] == "ok"
        ready = c.get("/ready").json()
        assert ready["ready"] is True
        r = c.post(
            "/predict",
            json={"pixels": [0.0] * 256, "request_id": "demo"},
        )
        assert r.status_code == 200
        out = r.json()
        assert 0.0 <= out["prob_class1"] <= 1.0
        assert out["label"] in (0, 1)
        assert out["model_version"]
        assert out["request_id"] == "demo"
