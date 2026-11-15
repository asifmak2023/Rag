# 100. Ridge vs Lasso vs OLS (collinear features)

OLS: minimize MSE. Unstable when columns are copies of each other
(chapter 02 rank).

Ridge (L2): shrink all coefs, keep them. Good default linear model.

Lasso (L1): some coefs hit exactly 0. Feature selection.

Elastic net: mix.

Scale features first or the penalty is meaningless (units).

## Lab 100. File: `labs/100_ridge_lasso.py`

Two collinear features. OLS coefs large opposite signs. Ridge smaller.
Lasso may zero one.

## Pass / fail

"I do not invert X.T X if it is ill-conditioned. I use ridge."
