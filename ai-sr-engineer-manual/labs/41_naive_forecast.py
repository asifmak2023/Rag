import numpy as np
import pandas as pd

idx = pd.date_range("2023-01-01", periods=400, freq="D")
y = (
    50
    + 8 * np.sin(np.arange(400) * 2 * np.pi / 7)
    + np.random.default_rng(0).normal(0, 2, 400)
)
s = pd.Series(y, index=idx)


def mape(a, p):
    a, p = np.asarray(a), np.asarray(p)
    return float(np.mean(np.abs(a - p) / np.clip(np.abs(a), 1e-6, None)))


h = 14
actual = s.iloc[-h:]
naive = pd.Series(float(s.iloc[-h - 1]), index=actual.index)
seasonal = s.shift(7).iloc[-h:]
print("naive mape", round(mape(actual, naive), 4))
print("seasonal7 mape", round(mape(actual, seasonal), 4))
assert mape(actual, seasonal) < mape(actual, naive)
