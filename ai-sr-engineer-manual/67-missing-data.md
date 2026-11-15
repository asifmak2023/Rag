# 67. Missing data without deleting the universe

`dropna()` on 40 columns can delete the whole table. That is not
cleaning. That is surrender.

## Types

- MCAR: missing by accident, independent of values
- MAR: missing depends on observed columns
- MNAR: missing depends on the missing value itself (income not
  reported because it is high)

You usually cannot prove which. You can still be careful.

## Tactics

1. Missing indicator column (`age_missing`)
2. Median / most_frequent inside a Pipeline (chapter 03)
3. Trees: HistGB / LightGBM handle NaN natively
4. Do not fill with 0 unless 0 is a real category (amount)
5. Do not fill test with train-unseen statistics computed on test

## Lab 67. File: `labs/67_missing.py`

Compare dropna vs impute on a table with 20% nulls in one column.
Print remaining n and F1. Dropna should look "cleaner" and worse on
n.

## Interview

"I impute inside the Pipeline and I keep a missing flag when absence
is a signal (no credit file)."

## Pass / fail

You never lead with dropna as the whole strategy.
