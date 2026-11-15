from pathlib import Path

import joblib
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1000, n_features=8, n_informative=4, random_state=0
)
pipe = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000)),
    ]
)
pipe.fit(X, y)
out = Path(__file__).with_name("model.joblib")
joblib.dump(pipe, out)
print("wrote", out, "n_features", pipe.n_features_in_)
