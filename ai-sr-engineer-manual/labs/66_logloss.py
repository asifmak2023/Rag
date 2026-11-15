import numpy as np
from sklearn.metrics import log_loss


def binary_logloss(y, p, eps=1e-7):
    y = np.asarray(y, dtype=float)
    p = np.clip(np.asarray(p, dtype=float), eps, 1 - eps)
    return float(-(y * np.log(p) + (1 - y) * np.log(1 - p)).mean())


y = np.array([0, 0, 1, 1, 1])
p = np.array([0.1, 0.4, 0.6, 0.9, 0.99])
a, b = binary_logloss(y, p), log_loss(y, p)
print("scratch", a, "sklearn", b)
assert abs(a - b) < 1e-12
print("confident-wrong", binary_logloss(np.array([1]), np.array([0.01])))
