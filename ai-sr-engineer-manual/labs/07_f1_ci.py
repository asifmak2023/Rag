import numpy as np
from sklearn.metrics import f1_score


def f1_ci(y, pred, n=200, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    pred = np.asarray(pred)
    stats = []
    for _ in range(n):
        idx = rng.integers(0, len(y), len(y))
        stats.append(f1_score(y[idx], pred[idx], zero_division=0))
    lo, hi = np.percentile(stats, [2.5, 97.5])
    return float(np.mean(stats)), float(lo), float(hi)


rng = np.random.default_rng(0)
y = rng.integers(0, 2, size=800)
pred = y.copy()
pred[:80] = 1 - pred[:80]
print("f1 mean lo hi", f1_ci(y, pred))
