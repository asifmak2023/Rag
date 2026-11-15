# 114. Train/serve parity test (the skew killer)

Take one row from the training frame. Score it with the training
Pipeline. Score the same row through the API feature function.
Assert probabilities match within 1e-6.

If they differ, you have two feature paths. That is chapter 14
"training-serving skew". Fix before any AUC argument.

## Lab 114. File: `labs/114_parity.py`

Capstone A `add_ratio_features` then model vs raw columns without
the ratio: numbers differ. Then both with the ratio: match.

This is the test you add when a product says "the batch job and the
API disagree".

## Pass / fail

One pytest that locks train path == serve path on a golden row.
