from sklearn.datasets import make_regression
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

X, y = make_regression(n_samples=800, n_features=6, noise=15, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)
dummy = DummyRegressor(strategy="mean").fit(Xtr, ytr)
ridge = Ridge(alpha=1.0).fit(Xtr, ytr)


def report(name, pred):
    mae = mean_absolute_error(yte, pred)
    rmse = mean_squared_error(yte, pred) ** 0.5
    r2 = r2_score(yte, pred)
    print(name, "mae", round(mae, 3), "rmse", round(rmse, 3), "r2", round(r2, 3))


report("dummy", dummy.predict(Xte))
report("ridge", ridge.predict(Xte))
assert r2_score(yte, ridge.predict(Xte)) > r2_score(yte, dummy.predict(Xte))
