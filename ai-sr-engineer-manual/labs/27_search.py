from scipy.stats import loguniform
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score

X, y = make_classification(
    n_samples=2000, n_features=20, weights=[0.85, 0.15], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
pipe = Pipeline(
    [
        ("sc", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)
search = RandomizedSearchCV(
    pipe,
    {"clf__C": loguniform(1e-3, 1e2)},
    n_iter=12,
    scoring="f1",
    cv=StratifiedKFold(5, shuffle=True, random_state=0),
    random_state=0,
    n_jobs=1,
)
search.fit(Xtr, ytr)
pred = search.predict(Xte)
print("best", search.best_params_, "cv_f1", float(search.best_score_))
print("test_f1", float(f1_score(yte, pred)))
