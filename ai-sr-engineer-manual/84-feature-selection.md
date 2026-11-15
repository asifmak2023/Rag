# 84. Feature selection (after a baseline, not instead)

Reasons: speed, simpler serving, less leakage surface, interpretability.
Not: "we selected 8 features so the model is intelligent."

Order:

1. Drop IDs, leaks, constants, duplicate columns
2. Domain keep-list
3. Univariate (mutual info, ANOVA) as EDA, not gospel
4. Regularized linear (L1) or tree importances
5. Recursive elimination only if n_features is painful

Do selection inside CV. Selecting on the full data then CV is leak.

## Lab 84. File: `labs/84_select.py`

`SelectKBest` inside a Pipeline vs outside. Outside on all X is the
wrong pattern; show both APIs, use inside.

## Pass / fail

Selection is a Pipeline step, not a pre-CSV you forgot to version.
