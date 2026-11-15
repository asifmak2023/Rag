import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(2000, 6))
w = rng.normal(size=6)
y = (X @ w + 0.3 * rng.normal(size=2000) > 0).astype(int)
mask = rng.random(len(X)) < 0.2
X[mask, 0] = np.nan
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)

def complete(a, b):
    keep = ~np.isnan(a).any(axis=1)
    return a[keep], b[keep]

Xtr_d, ytr_d = complete(Xtr, ytr)
Xte_d, yte_d = complete(Xte, yte)
clf = Pipeline(
    [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
)
clf.fit(Xtr_d, ytr_d)
print("dropna n_test", len(yte_d), "f1", float(f1_score(yte_d, clf.predict(Xte_d))))

pipe = Pipeline(
    [
        ("imp", SimpleImputer(strategy="median")),
        ("sc", StandardScaler()),
        ("m", LogisticRegression(max_iter=1000)),
    ]
)
pipe.fit(Xtr, ytr)
print("impute n_test", len(yte), "f1", float(f1_score(yte, pipe.predict(Xte))))
