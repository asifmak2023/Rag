# 101. Numeric hygiene (MATLAB/C++ instincts)

- `log(0)` and `1/0` produce -inf/inf, then NaN. Clip probabilities.
- Subtract max before softmax (lab 02_softmax).
- `float32` vs `float64`: nets often float32; money totals may need 64
  or decimal in finance, float32 in the model.
- Condition number of X.T X: large => linear model jitter.
- Do not compare floats with `==`. Use `allclose`.
- Integer overflow is rarer in Python ints, still real in numpy int32.

## Lab 101. File: `labs/101_softmax_stable.py`

Softmax of `[1000, 1001, 1002]` without subtract-max is inf. With
subtract-max it is fine. You already have the stable version; this lab
shows the unstable one failing.

## Pass / fail

You mention subtract-max if they ask you to write softmax.
