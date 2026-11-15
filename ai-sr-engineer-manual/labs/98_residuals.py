import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

rng = np.random.default_rng(0)
x = rng.uniform(-2, 2, size=400)
y = x ** 2 + rng.normal(0, 0.15, size=400)
X = x.reshape(-1, 1)
lin = LinearRegression().fit(X, y)
resid_lin = y - lin.predict(X)
poly = PolynomialFeatures(2, include_bias=True)
Xp = poly.fit_transform(X)
quad = LinearRegression().fit(Xp, y)
resid_q = y - quad.predict(Xp)
print("lin resid mean abs", float(np.mean(np.abs(resid_lin))))
print("quad resid mean abs", float(np.mean(np.abs(resid_q))))
assert np.mean(np.abs(resid_q)) < np.mean(np.abs(resid_lin))
