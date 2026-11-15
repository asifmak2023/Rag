from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=3000,
    n_features=16,
    weights=[0.9, 0.1],
    random_state=0,
)

print("--- honest ---")
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
sc = StandardScaler().fit(Xtr)
clf = LogisticRegression(max_iter=1000, class_weight="balanced").fit(sc.transform(Xtr), ytr)
proba = clf.predict_proba(sc.transform(Xte))[:, 1]
pred = (proba >= 0.5).astype(int)
print("counts train", int(ytr.sum()), "test", int(yte.sum()))
print("f1", float(f1_score(yte, pred)), "recall", float(recall_score(yte, pred)))

print("--- no stratify ---")
Xtr2, Xte2, ytr2, yte2 = train_test_split(X, y, test_size=0.2, random_state=1)
print("counts train", int(ytr2.sum()), "test", int(yte2.sum()))

print("--- no class_weight ---")
clf2 = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
pred2 = clf2.predict(sc.transform(Xte))
print("recall", float(recall_score(yte, pred2)))

print("--- scaler leak ---")
sc_bad = StandardScaler().fit(X)
clf3 = LogisticRegression(max_iter=1000, class_weight="balanced").fit(sc_bad.transform(Xtr), ytr)
auc_bad = roc_auc_score(yte, clf3.predict_proba(sc_bad.transform(Xte))[:, 1])
auc_ok = roc_auc_score(yte, proba)
print("auc honest", float(auc_ok), "auc leaked scaler", float(auc_bad))
