# 43. Batch scoring (most production ML)

Online `/predict` is the demo. Nightly tables are the business.

## Pattern

```
SQL extract as_of = today
  -> Python job loads model.joblib
  -> writes warehouse.scores_churn_2026_03_15
  -> product reads top 500
```

No Kubernetes required. cron, Airflow, or a scheduled GitHub Action
at toy scale. In office: whatever they already use to run SQL.

## Lab 43. File: `labs/43_batch_score.py`

```python
from pathlib import Path
import json
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

art = Path("labs/data")
art.mkdir(parents=True, exist_ok=True)
X, y = make_classification(n_samples=500, n_features=8, random_state=0)
pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))])
pipe.fit(X, y)
joblib.dump(pipe, art / "batch_model.joblib")

# "today's" file
cols = [f"f{i}" for i in range(8)]
today = pd.DataFrame(X[:50], columns=cols)
today.insert(0, "customer_id", range(50))
model = joblib.load(art / "batch_model.joblib")
today["prob"] = model.predict_proba(today[cols])[:, 1]
today["model_version"] = "churn-gbdt-v1"
out = art / "scores_today.csv"
today[["customer_id", "prob", "model_version"]].to_csv(out, index=False)
print("wrote", out, "mean_prob", float(today["prob"].mean()))
```

Add a row count assert and a null check. That is a data quality gate.

## Failure modes

- Scoring a file with shuffled columns
- Yesterday's model on today's schema
- Writing scores with no `as_of` column so nobody can audit
- Replacing the table instead of partitioning by date (cannot rollback)

## Interview

"If the call list is used at 9am, I batch at 2am. I only build an
API if a screen needs a score during a click."

## Pass / fail

A script that reads a CSV, writes scores with version and date, and
refuses to run if columns mismatch.
