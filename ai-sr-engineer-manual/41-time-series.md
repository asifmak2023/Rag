# 41. Time series (forecasting without the cult)

Consulting "AI" often means: next week's demand, next month's cash,
next day's load. Deep seq2seq is rarely v1.

## First questions

1. Grain: daily SKU, hourly meter, weekly branch.
2. Horizon: 1 day, 7 days, 28 days.
3. Cadence: when the forecast is consumed.
4. What they did last year: last-week copy is the baseline.

If last-week copy is within 5% of a fancy model, ship the copy plus
a dashboard.

## Leakage (again)

You cannot use today's sales to predict today's sales. Features at
time t use only data < t. Rolling origin backtest, not a random split.

## Lab 41A. Naive baselines

File: `labs/41_naive_forecast.py`

```python
import numpy as np
import pandas as pd

idx = pd.date_range("2023-01-01", periods=400, freq="D")
y = 50 + 8 * np.sin(np.arange(400) * 2 * np.pi / 7) + np.random.default_rng(0).normal(0, 2, 400)
s = pd.Series(y, index=idx)

def mape(a, p):
    a, p = np.asarray(a), np.asarray(p)
    return float(np.mean(np.abs(a - p) / np.clip(np.abs(a), 1e-6, None)))

h = 14
actual = s.iloc[-h:]
naive = pd.Series(s.iloc[-h - 1], index=actual.index)  # last value
seasonal = s.shift(7).iloc[-h:]  # last week
print("naive mape", mape(actual, naive))
print("seasonal7 mape", mape(actual, seasonal))
```

Always print these two before Prophet, LSTM, or "AI demand planning".

## Lab 41B. Time split for a classifier

Events with a date: train on months 1-10, validate 11, test 12.
Never `train_test_split(shuffle=True)` on that table.

```python
cut = df["ts"].quantile(0.8)
train = df[df["ts"] < cut]
test = df[df["ts"] >= cut]
```

## Models in order

1. Seasonal naive
2. Exponential smoothing / Holt-Winters (`statsmodels`)
3. Ridge on lags + calendar (month, dow, holiday)
4. LightGBM on lags if many series (SKU-level)
5. Deep models last, and only if 1-4 lose on a locked backtest

## Interview

"I backtest with a rolling origin. I refuse a random split. I will
not put an LSTM in production until seasonal naive is beaten on MAPE
or money, not on a blog metric."

## Pass / fail

On a sine+noise daily series, implement seasonal naive and beat it
with a lag regression. If you cannot beat it, say so. That is senior.
