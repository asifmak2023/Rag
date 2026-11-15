import numpy as np

rng = np.random.default_rng(0)
x = rng.lognormal(mean=3, sigma=1.0, size=5000)
x[0:20] = x[0:20] * 40
print(
    "mean",
    round(float(x.mean()), 2),
    "median",
    round(float(np.median(x)), 2),
    "p90",
    round(float(np.quantile(x, 0.9)), 2),
)
assert np.median(x) < x.mean()
