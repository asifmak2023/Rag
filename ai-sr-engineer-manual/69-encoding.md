# 69. Categorical encoding (the silent leak machine)

| Method | Use | Leak risk |
|---|---|---|
| One-hot | low cardinality | low if fit on train |
| Ordinal / integer codes | trees | low |
| Hashing | huge cardinality | low |
| Frequency encode | medium card | fit on train only |
| Target encode | high card | HIGH if fit on full data |

Target encode: replace city with mean(y | city). If you compute that
on all rows, you leaked y. Use CV target encoding or smoothing + train
only.

IDs: 50k customer_ids one-hot will explode. Hash or embeddings or do
not use.

## Lab 69. File: `labs/69_onehot_unknown.py`

`OneHotEncoder(handle_unknown="ignore")` on a category that appears
only in test. Without ignore, it crashes. With ignore, zeros.

## Pass / fail

You never `get_dummies` on the concatenated train+test frame.
