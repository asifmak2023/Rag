import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

rng = np.random.default_rng(0)
y = rng.integers(0, 2, size=2000)
X_ok = rng.normal(size=(2000, 5))
X_leak = np.column_stack([X_ok, y.astype(float)])

for name, X in [("ok", X_ok), ("leak", X_leak)]:
    model = LogisticRegression(max_iter=1000).fit(X, y)
    auc = roc_auc_score(y, model.predict_proba(X)[:, 1])
    print(name, float(auc))
