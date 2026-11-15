# 68. Outliers: winsorize, log, do not worship z=3

A 1e9 amount will dominate MSE and some linear models. Trees care
less. Deleting every z>3 can delete the fraud you wanted.

## Tactics

- Plot: histogram, then log-histogram
- Clip at p1/p99 on TRAIN, apply same bounds on serve
- `log1p` for money and counts
- Robust scaler (median/IQR) for linear models
- Keep a `amount_is_huge` flag

## Lab 68. File: `labs/68_clip.py`

Clip a fat-tail column at p99. Print max before/after. Fit ridge on
raw vs clipped vs log1p, compare MAE. Narrate, do not hunt a winner.

## Pass / fail

You can explain why you clip using train quantiles only.
