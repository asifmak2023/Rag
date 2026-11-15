# 66. Probability, odds, and log loss (speak precisely)

Sigmoid output is not "confidence" in English. It is a model
probability. Calibration (chapter 34) decides if you can treat it as
a frequency.

## Log loss / cross entropy

Punishes confident wrong answers hard. If you predict 0.99 and it was
0, you pay a lot. Accuracy does not. For ranking risk, log loss is a
better training objective than 0-1 error.

Binary: `-(y log p + (1-y) log(1-p))`. Clip p to [1e-7, 1-1e-7].

## Lab 66. File: `labs/66_logloss.py`

Implement binary log loss. Match `sklearn.metrics.log_loss`.

## Odds

p / (1-p). Logistic regression is linear in log-odds. Coefficients
are additive in log-odds, not in probability. Do not say "this feature
adds 10% probability" for a logistic coef unless you compute at a
point.

## Pass / fail

Explain log loss vs accuracy in 40 seconds. Mention clipping.
