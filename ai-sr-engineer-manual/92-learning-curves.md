# 92. Learning curves (do I need more data?)

Plot train vs val score against training set size.

- Both low: underfit. More data will not save a linear model on XOR.
- Train high, val low, gap shrinking with n: more data may help.
- Gap stuck: need regularization or simpler model, not another million
  rows of the same mess.

## Lab 92. File: `labs/92_learning_curve.py`

`sklearn.model_selection.learning_curve` on logistic. Print mean train
and val F1 at a few sizes.

## Interview

"I look at the learning curve before I ask the business for more
history. Sometimes I need better labels, not more of the same."

## Pass / fail

You can sketch the two regimes and say which way more data helps.
