from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=2000, n_features=10, weights=[0.9, 0.1], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
d = DummyClassifier(strategy="most_frequent").fit(Xtr, ytr)
m = LogisticRegression(max_iter=1000, class_weight="balanced").fit(Xtr, ytr)
for name, pred in ("dummy", d.predict(Xte)), ("logreg", m.predict(Xte)):
    print(
        name,
        "acc",
        round(accuracy_score(yte, pred), 3),
        "f1",
        round(f1_score(yte, pred, zero_division=0), 3),
    )
