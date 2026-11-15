import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=3000, n_features=10, weights=[0.85, 0.15], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
p = LogisticRegression(max_iter=1000).fit(Xtr, ytr).predict_proba(Xte)[:, 1]
c_fp, c_fn = 1.0, 20.0
best_t, best_c = 0.5, 1e18
for t in np.linspace(0.1, 0.9, 17):
    pred = (p >= t).astype(int)
    fp = int(((pred == 1) & (yte == 0)).sum())
    fn = int(((pred == 0) & (yte == 1)).sum())
    cost = fp * c_fp + fn * c_fn
    print(f"t={t:.2f} fp={fp} fn={fn} cost={cost}")
    if cost < best_c:
        best_t, best_c = t, cost
print("best_t", best_t, "best_cost", best_c)
