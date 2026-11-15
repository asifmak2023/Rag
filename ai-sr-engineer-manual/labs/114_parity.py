import sys
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "capstone-a-churn"))
from src.features import add_ratio_features

row = pd.DataFrame(
    [
        {
            "tenure_months": 12,
            "monthly_charges": 80.0,
            "total_charges": 960.0,
            "senior": 0,
        }
    ]
)
with_ratio = add_ratio_features(row)
X = with_ratio[
    ["tenure_months", "monthly_charges", "total_charges", "senior", "avg_charge_per_month"]
]
y = [0]
pipe = Pipeline(
    [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
)
# tiny fit on copies so the object is real
pipe.fit(pd.concat([X, X]), [0, 1])
p_train = float(pipe.predict_proba(X)[0, 1])
p_serve = float(pipe.predict_proba(add_ratio_features(row)[X.columns])[0, 1])
print("p", p_train, p_serve)
assert abs(p_train - p_serve) < 1e-12
