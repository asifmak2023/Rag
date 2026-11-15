# 28. Debugging playbook (when the model is "not working")

Juniors retrain. Seniors isolate.

## 1. The data is wrong (most common)

Checklist:

- Row count vs expected grain
- Target rate vs business knowledge (3% churn suddenly 40%?)
- Nulls in a column that was never null
- Train/test from different months without noticing
- Duplicate keys
- Label definition changed in the SQL

Fix: `profile(df)` from chapter 06. Print `y.mean()` always.

## 2. The split is wrong

Random split on a user who appears twice. Time leak. Stratify forgot
on a 2% class so the test set has 0 positives.

Fix: print class counts in every split. For users, split by user_id.

## 3. The pipeline is wrong

Scaler fit on all data. OneHot on test-only categories exploding.
`predict` instead of `predict_proba` then threshold.

Fix: one Pipeline, fit on train only.

## 4. The metric is wrong

Accuracy on 99% negative. R-squared when the business uses MAE in
rupees. AUC 0.99 because of a leak.

Fix: metric from cost. Always print a baseline.

## 5. Training is dead (deep learning)

Recite kata 10. Add:

- Overfit one batch: 8 samples, 200 steps, loss must go to ~0.
  If it cannot, the graph or labels are broken. Do not tune lr yet.
- Print a batch of labels. Are they all 0?
- Print `next(model.parameters()).grad` after backward. None = bug.

## 6. Serving is wrong

Train with 21 features, API sends 20. Different category spelling
(`Month-to-Month` vs `month-to-month`). Dropout left on.
Image RGB vs gray. Keras NHWC vs torch NCHW.

Fix: contract tests + a saved example payload in the repo.

## 7. It worked yesterday

Code changed, data changed, or dependency changed.
`metrics.json` plus git hash plus data file hash.

## Lab 28. Break then fix

Take `labs/03_churn_baseline.py`.

1. Drop `stratify=`. See class counts.
2. Drop `class_weight`. See recall.
3. Fit scaler on X_train+X_test. Note the dishonest AUC.
4. Put it back. Write the four numbers in `labs/notes.md`.

## Pass / fail

Given a broken notebook (you can break your own), you find the bug
in 15 minutes using this list, not by adding layers.
