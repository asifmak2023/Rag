# 105. Temperature scaling (last-minute calibration)

For a trained classifier, divide logits by T > 0, then softmax.
T>1 softens (less confident). T<1 sharpens. Fit T on a validation
set by minimizing NLL. One parameter. Does not change ranking of
classes much if T is shared. Changes probabilities.

Nets are often overconfident. This is cheaper than retraining.

## Lab 105. File: `labs/105_temperature.py`

Two-class logits. T=1 vs T=2. Show max probability drop.

## Interview

"If the net is overconfident, I try temperature scaling on val before
I rebuild the architecture."

## Pass / fail

T>1 softens. Fit on val, not test.
