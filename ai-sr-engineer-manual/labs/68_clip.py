import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
x = rng.lognormal(2, 1.0, size=3000)
x[:15] *= 80
y = 0.4 * np.log1p(x) + rng.normal(0, 0.3, size=3000)
X = x.reshape(-1, 1)
Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)
p99 = np.quantile(Xtr, 0.99)
print("max train", float(Xtr.max()), "p99", float(p99))


def mae(transform):
    m = Ridge().fit(transform(Xtr), ytr)
    return float(mean_absolute_error(yte, m.predict(transform(Xte))))


print("raw", mae(lambda a: a))
print("clip", mae(lambda a: np.clip(a, None, p99)))
print("log1p", mae(np.log1p))
