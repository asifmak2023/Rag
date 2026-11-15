from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=2500, n_features=10, weights=[0.8, 0.2], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
base = float(ytr.mean())
dummy = [base] * len(yte)
p = LogisticRegression(max_iter=1000).fit(Xtr, ytr).predict_proba(Xte)[:, 1]
print("dummy brier", float(brier_score_loss(yte, dummy)))
print("model brier", float(brier_score_loss(yte, p)))
assert brier_score_loss(yte, p) < brier_score_loss(yte, dummy)
