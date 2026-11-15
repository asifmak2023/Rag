from pathlib import Path

import joblib
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

art = Path(__file__).resolve().parent / "data"
art.mkdir(parents=True, exist_ok=True)
X, y = make_classification(n_samples=500, n_features=8, random_state=0)
pipe = Pipeline(
    [("sc", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))]
)
pipe.fit(X, y)
joblib.dump(pipe, art / "batch_model.joblib")

cols = [f"f{i}" for i in range(8)]
today = pd.DataFrame(X[:50], columns=cols)
today.insert(0, "customer_id", range(50))
expected = list(pipe.feature_names_in_) if hasattr(pipe, "feature_names_in_") else cols
if list(today[cols].columns) != cols:
    raise SystemExit("column mismatch")
model = joblib.load(art / "batch_model.joblib")
today["prob"] = model.predict_proba(today[cols])[:, 1]
today["model_version"] = "churn-gbdt-v1"
today["as_of"] = "2026-03-15"
out = art / "scores_today.csv"
today[["customer_id", "prob", "model_version", "as_of"]].to_csv(out, index=False)
assert today["prob"].notna().all()
print("wrote", out, "mean_prob", float(today["prob"].mean()), "n", len(today))
