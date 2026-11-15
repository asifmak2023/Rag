from sklearn.datasets import make_classification
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1200, n_features=10, n_informative=3, random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)
pipe = Pipeline(
    [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
)
pipe.fit(Xtr, ytr)
r = permutation_importance(
    pipe, Xte, yte, n_repeats=8, random_state=0, scoring="f1"
)
order = r.importances_mean.argsort()[::-1][:3]
print("top idx", order.tolist(), "mean", r.importances_mean[order].round(4).tolist())
