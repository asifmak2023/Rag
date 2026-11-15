# Tiny model service

```bash
python labs/serve/train_tiny.py
uvicorn labs.serve.app:app --host 0.0.0.0 --port 8000
```

From `labs/serve` after `model.joblib` exists:

```bash
docker build -t churn-score:v1 .
docker run --rm -p 8000:8000 churn-score:v1
```

```bash
curl -s http://127.0.0.1:8000/health
curl -s http://127.0.0.1:8000/predict \
  -H 'content-type: application/json' \
  -d '{"features":[0,0,0,0,0,0,0,0],"request_id":"demo"}'
```
