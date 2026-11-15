from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1500, n_features=16, weights=[0.8, 0.2], random_state=0
)
pipe = Pipeline(
    [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
)
sizes, tr, va = learning_curve(
    pipe, X, y, cv=5, scoring="f1", train_sizes=[0.2, 0.4, 0.6, 0.8, 1.0]
)
for n, t, v in zip(sizes, tr.mean(axis=1), va.mean(axis=1)):
    print("n", int(n), "train_f1", round(float(t), 3), "val_f1", round(float(v), 3))
