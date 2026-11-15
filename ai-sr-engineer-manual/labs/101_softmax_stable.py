import numpy as np


def softmax_unstable(x):
    e = np.exp(x)
    return e / e.sum()


def softmax_stable(x):
    z = x - np.max(x)
    e = np.exp(z)
    return e / e.sum()


x = np.array([1000.0, 1001.0, 1002.0])
u = softmax_unstable(x)
s = softmax_stable(x)
print("unstable", u)
print("stable", s)
assert np.isnan(u).any()
assert np.allclose(s.sum(), 1.0)
assert np.all(np.isfinite(s))
