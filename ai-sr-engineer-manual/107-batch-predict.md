# 107. Batch vs one-row predict (latency)

One HTTP call per customer at 1 ms is fine at 50 QPS. At 20k QPS you
batch.

- API: accept a list of rows, cap length (e.g. 256)
- Internal: score a numpy matrix once
- GPU: batch is how you get utilization

Do not build a queue system in week 1. Do not loop `predict` on rows
in pandas.

## Lab 107. File: `labs/107_batch_predict.py`

Time `predict` on 1 row x 500 vs 500 rows once. Matrix should win.

## Pass / fail

You never `iterrows` into sklearn.
