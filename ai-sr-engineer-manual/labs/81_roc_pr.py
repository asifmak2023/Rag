from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=4000, n_features=12, weights=[0.95, 0.05], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
base_rate = float(yte.mean())
dummy = yte * 0.0 + base_rate
print("base_rate", base_rate)
print("dummy roc", float(roc_auc_score(yte, dummy)), "ap", float(average_precision_score(yte, dummy)))
clf = LogisticRegression(max_iter=1000, class_weight="balanced").fit(Xtr, ytr)
p = clf.predict_proba(Xte)[:, 1]
print("model roc", float(roc_auc_score(yte, p)), "ap", float(average_precision_score(yte, p)))
