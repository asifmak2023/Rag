# 06. Data: collect, clean, feature, scale

The posting spends as many words on data as on models. Treat data work
as the job, models as a function you call.

## Principles

1. The unit of work is a table with a documented grain (one row = one
   customer on one day, not "whatever").
2. Time is a first-class column. Random splits on time-ordered events
   leak the future.
3. IDs are not features unless you have a reason.
4. Missing is information. "Unknown city" is not the same as Karachi.
5. You never need the whole file in RAM if you can stream.

## Lab 06A. Chunked CSV (large data, small machine)

File: `labs/06_chunk_mean.py`

```python
import pandas as pd
import numpy as np

path = "labs/data/big.csv"
# create a stand-in if needed
n = 200_000
pd.DataFrame({
    "id": np.arange(n),
    "x": np.random.default_rng(0).normal(size=n),
    "y": np.random.default_rng(1).integers(0, 2, size=n),
}).to_csv(path, index=False)

n_rows = 0
sx = 0.0
for chunk in pd.read_csv(path, chunksize=20_000):
    n_rows += len(chunk)
    sx += chunk["x"].sum()
print("mean x", sx / n_rows)
```

Upgrade: compute mean and variance in one pass (Welford). Seniors know
one-pass stats.

## Lab 06B. SQL as a feature store

You already know SQL. Use it.

```sql
-- features at prediction time T must only use events < T
SELECT
  c.customer_id,
  COUNT(*) FILTER (WHERE e.ts < c.as_of) AS n_events,
  AVG(e.amount) FILTER (WHERE e.ts < c.as_of) AS avg_amount_hist
FROM customers c
LEFT JOIN events e ON e.customer_id = c.customer_id
GROUP BY 1, c.as_of;
```

If you do not have a database, SQLite is enough:

```python
import sqlite3, pandas as pd
con = sqlite3.connect("labs/data/toy.db")
# pd.read_sql("SELECT ...", con)
```

Self-check: explain point-in-time correctness in two minutes. If labels
come from next month's churn, features must be computed from this month
and earlier only.

## Lab 06C. Cleaning checklist (run on every new table)

Write a function `profile(df)` that prints:

- shape, dtypes, memory
- null counts
- numeric describe
- categorical value_counts head
- duplicate key count
- date min/max

Then fix, in this order:

1. Wrong grain / duplicate keys
2. Target definition (who is positive, when)
3. Leak columns
4. Null strategy per column
5. Outliers: winsorize or log, do not delete blindly
6. Categorical cardinality (one-hot 10k cities is a footgun; use target
   encode with CV or hashing)

## Lab 06D. Generators for "streams"

The posting says "large data streams at speed". You do not need Kafka
on day one. You need to not load everything.

```python
def iter_jsonl(path, batch=1024):
    batch_rows = []
    with open(path) as f:
        for line in f:
            batch_rows.append(line)
            if len(batch_rows) >= batch:
                yield batch_rows
                batch_rows = []
    if batch_rows:
        yield batch_rows
```

Then vectorize inside the batch. This is how you talk about streaming
without lying that you ran a 100-node cluster.

## Feature engineering that actually works

Tabular:

- Ratios, diffs, rolling windows (time-aware)
- Counts of events in last 1/7/30 days
- Missing indicators
- Cross features only if trees cannot find them cheaply (trees can)

Text:

- Start with TF-IDF + linear model
- Then embeddings if the linear model plateaus

Images:

- Resize, normalize with dataset mean/std
- Light augmentation: flip, small crop. Do not augment the test set.

## Efficiency (C++ brain, Python body)

- Vectorize (NumPy/pandas)
- Prefer `HistGradientBoosting` / LightGBM on 10M rows over deep nets
- `dtype` downcast: `float64` -> `float32`, categoricals
- Avoid copies: `copy=False` when safe
- Profile before rewriting in C++. `cProfile` / `line_profiler`

## Pass / fail

Given a dirty CSV with dates, nulls, and a target, produce a leak-free
feature table and a written data dictionary. No model required for pass.
