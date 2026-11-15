from pathlib import Path

from fastapi.testclient import TestClient

SERVE = Path(__file__).resolve().parents[1] / "serve"


def test_health_ready_predict():
    import runpy
    import sys

    sys.path.insert(0, str(SERVE))
    runpy.run_path(str(SERVE / "train_tiny.py"), run_name="__not_main__")
    from app import app

    with TestClient(app) as c:
        assert c.get("/health").json()["status"] == "ok"
        assert c.get("/ready").json()["ready"] is True
        r = c.post(
            "/predict",
            json={"features": [0, 0, 0, 0, 0, 0, 0, 0], "request_id": "demo"},
        )
        assert r.status_code == 200
        body = r.json()
        assert 0.0 <= body["prob"] <= 1.0
        assert body["label"] in (0, 1)
        assert body["request_id"] == "demo"
