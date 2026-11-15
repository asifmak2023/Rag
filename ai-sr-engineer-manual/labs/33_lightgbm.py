from sklearn.datasets import make_classification
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=4000,
    n_features=24,
    n_informative=8,
    weights=[0.9, 0.1],
    random_state=0,
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)

logreg = Pipeline(
    [
        ("sc", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)
hgb = HistGradientBoostingClassifier(
    max_depth=4, learning_rate=0.08, max_iter=120, random_state=0
)
logreg.fit(Xtr, ytr)
hgb.fit(Xtr, ytr)
print("logreg auc", float(roc_auc_score(yte, logreg.predict_proba(Xte)[:, 1])))
print("hgb auc", float(roc_auc_score(yte, hgb.predict_proba(Xte)[:, 1])))

try:
    from lightgbm import LGBMClassifier

    lgbm = LGBMClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        class_weight="balanced",
        verbose=-1,
    )
    lgbm.fit(Xtr, ytr)
    print("lgbm auc", float(roc_auc_score(yte, lgbm.predict_proba(Xte)[:, 1])))
except Exception as exc:
    print("lightgbm skipped:", type(exc).__name__, exc)
