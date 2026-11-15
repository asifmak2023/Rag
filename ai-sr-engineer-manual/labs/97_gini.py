import numpy as np


def entropy(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(-p * np.log2(p) - (1 - p) * np.log2(1 - p))


def gini(p):
    return float(1 - p * p - (1 - p) * (1 - p))


for p in (0.0, 0.5, 1.0):
    print("p", p, "gini", round(gini(p), 4), "entropy", round(entropy(p) if 0 < p < 1 else 0.0, 4))
assert gini(0.5) > gini(0.1)
assert abs(gini(0.0)) < 1e-12
