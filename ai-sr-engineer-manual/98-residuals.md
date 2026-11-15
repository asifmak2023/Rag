# 98. Residual plots (regression sanity)

Residual = y - pred. Plot vs pred and vs time.

- Fan shape: variance grows with y (heteroscedasticity). Log y or
  quantile regression. Linear MAE may be more honest than MSE.
- Curve left in residuals: model too simple, add terms or a tree.
- Blob around 0: good enough for v1.

## Lab 98. File: `labs/98_residuals.py`

Fit a line to y = x^2 + noise. Residuals vs x should show a U.
Then fit a polynomial degree 2 and show the U flatten.

## Pass / fail

You look at residuals before you celebrate R^2.
