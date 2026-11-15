# 21. Whiteboard / laptop katas they actually give

Each kata: 25-40 minutes. No internet first pass.

## Kata 1. Fit a line

Given `xs`, `ys`, implement GD in Python lists or NumPy.
They want to see the update rule, not sklearn.

## Kata 2. Confusion from scratch

Given `y_true`, `y_pred`, return tp, fp, tn, fn, then precision,
recall, f1. No sklearn. Off-by-one on zero division is the trap.

## Kata 3. Softmax and cross entropy

Write softmax numerically stable (`x - max(x)`).
Write mean cross entropy for one-hot or class indices.

## Kata 4. Train/val/test split without sklearn

Shuffle with a seed. Proportions 70/15/15. Stratify optional extra.

## Kata 5. Parse messy CSV mentally

They paste 8 rows: mixed dates, "N/A", duplicate ids.
You list: grain, target, leaks, imputes. No code required. This is
senior.

## Kata 6. Shape debugging

`RuntimeError: mat1 and mat2 shapes cannot be multiplied (32x512 and 256x10)`
You say: last linear expected 512, got 256, flatten or conv out_channels
wrong. Walk a CNN shape table.

## Kata 7. SQL window

`LAG(amount) OVER (PARTITION BY user_id ORDER BY ts)`
Explain why that is a feature and why you must still cut at as_of.

## Kata 8. API contract

Write JSON in and JSON out for a credit score. Include model_version,
request_id, error object. They are testing product thinking.

## Kata 9. Complexity

kNN predict is O(n d) per query. Why it dies. What ANN / IVF / HNSW
is in one sentence. You do not implement HNSW.

## Kata 10. Debugging a dead training run

Loss constant. Checklist you recite:

1. lr
2. labels dtype / range
3. forgot softmax vs CrossEntropy (double softmax)
4. not shuffling
5. still in eval()
6. gradients None (forgot requires_grad or detached too early)
7. data all zeros after a bad normalize

## After each kata

Write the time and the one thing you had to look up. That thing is
tomorrow's first 10 minutes.
