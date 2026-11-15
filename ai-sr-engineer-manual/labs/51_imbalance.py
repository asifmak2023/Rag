from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=5000,
    n_features=16,
    weights=[0.95, 0.05],
    random_state=0,
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
maj = (yte * 0)
print("majority acc", float(accuracy_score(yte, maj)), "f1", float(f1_score(yte, maj, zero_division=0)))

def fit(cw):
    pipe = Pipeline(
        [
            ("sc", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, class_weight=cw)),
        ]
    )
    pipe.fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    return (
        float(accuracy_score(yte, pred)),
        float(f1_score(yte, pred, zero_division=0)),
        float(recall_score(yte, pred, zero_division=0)),
    )

print("unweighted acc f1 rec", fit(None))
print("balanced  acc f1 rec", fit("balanced"))
