import numpy as np


def welford(xs):
    mean = 0.0
    m2 = 0.0
    n = 0
    for x in xs:
        n += 1
        delta = x - mean
        mean += delta / n
        delta2 = x - mean
        m2 += delta * delta2
    var = m2 / n if n else 0.0
    return mean, var, n


rng = np.random.default_rng(0)
xs = rng.normal(loc=3.0, scale=2.0, size=5000)
mean, var, n = welford(xs)
print("welford", mean, var, "numpy", float(xs.mean()), float(xs.var(ddof=0)))
assert n == len(xs)
assert abs(mean - xs.mean()) < 1e-10
assert abs(var - xs.var(ddof=0)) < 1e-10
