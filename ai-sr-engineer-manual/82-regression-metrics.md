# 82. Regression metrics (money vs squares)

MAE: mean |error|. Robust, same units as y.
MSE / RMSE: penalizes large misses. RMSE same units as y.
MAPE: percent. Dies when y ~ 0. Avoid for sparse counts.
R^2: 1 - SS_res/SS_tot. 0 means "no better than predicting the mean".
Negative R^2: worse than the mean. Possible.

Pinball / quantile loss if they want P90 demand, not the mean.

## Lab 82. File: `labs/82_regression.py`

Ridge on noisy y. Print MAE, RMSE, R^2. Compare to DummyRegressor mean.

## Interview

"If finance feels rupees, I optimize and report MAE. If a huge miss
is a disaster, RMSE."

## Pass / fail

You do not call R^2 "accuracy".
