import numpy as np


def psi(expected, actual, bins=10):
    expected = np.asarray(expected, dtype=float)
    actual = np.asarray(actual, dtype=float)
    lo, hi = np.min(expected), np.max(expected)
    e_cnt, edges = np.histogram(expected, bins=bins, range=(lo, hi))
    a_cnt, _ = np.histogram(actual, bins=edges)
    e_perc = e_cnt.astype(float) + 1e-6
    a_perc = a_cnt.astype(float) + 1e-6
    e_perc /= e_perc.sum()
    a_perc /= a_perc.sum()
    return float(np.sum((a_perc - e_perc) * np.log(a_perc / e_perc)))


rng = np.random.default_rng(0)
base = rng.normal(0, 1, size=5000)
same = rng.normal(0, 1, size=5000)
shifted = rng.normal(1.0, 1, size=5000)
print("psi same", round(psi(base, same), 4))
print("psi shifted", round(psi(base, shifted), 4))
