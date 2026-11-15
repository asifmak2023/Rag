# Capstone A. Telco-style churn scorer

This is the tabular production system from chapter 11, fully runnable
on synthetic data so you can practice the loop before swapping in a
real CSV.

## What it proves

- Point-in-time-ish features (no raw customer_id as a feature)
- sklearn Pipeline + ColumnTransformer
- Logistic baseline vs HistGradientBoosting
- Threshold chosen for recall floor, not 0.5
- metrics.json + reports
- FastAPI + Docker
- pytest on features and predict contract

## Run

```bash
python3 -m venv ~/ai-env
source ~/ai-env/bin/activate
pip install -r requirements.txt

python -m src.train
python -m src.evaluate
pytest tests
uvicorn src.serve:app --host 0.0.0.0 --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health
curl -s http://127.0.0.1:8000/predict \
  -H 'content-type: application/json' \
  -d '{"tenure_months":12,"monthly_charges":85.0,"total_charges":1020.0,"contract":"month-to-month","internet":"fiber","senior":0,"request_id":"demo"}'
```

Docker (after `python -m src.train` so `artifacts/model.joblib` exists):

```bash
docker build -t churn-capstone:v1 .
docker run --rm -p 8000:8000 churn-capstone:v1
```

## Swap real data

Replace `src/data.py` with a CSV loader. Keep the same column names or
update `FEATURE_SPEC` in `src/features.py`. Retrain. Do not change the
API JSON without bumping `MODEL_VERSION`.
