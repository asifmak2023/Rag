from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=800, n_features=30, n_informative=5, random_state=0
)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
pipe = Pipeline(
    [
        ("sel", SelectKBest(f_classif, k=8)),
        ("sc", StandardScaler()),
        ("m", LogisticRegression(max_iter=1000)),
    ]
)
scores = cross_val_score(pipe, X, y, cv=cv, scoring="f1")
print("cv f1", float(scores.mean()), float(scores.std()))
pipe.fit(X, y)
print("chosen idx", pipe.named_steps["sel"].get_support(indices=True).tolist())
