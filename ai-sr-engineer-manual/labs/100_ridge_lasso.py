import numpy as np
from sklearn.linear_model import Lasso, LinearRegression, Ridge

rng = np.random.default_rng(0)
n = 400
x1 = rng.normal(size=n)
x2 = x1 + 0.01 * rng.normal(size=n)
X = np.column_stack([x1, x2])
y = 3 * x1 + rng.normal(scale=0.2, size=n)
for name, m in [
    ("ols", LinearRegression()),
    ("ridge", Ridge(alpha=1.0)),
    ("lasso", Lasso(alpha=0.05, max_iter=5000)),
]:
    m.fit(X, y)
    print(name, np.round(m.coef_, 3).tolist())
