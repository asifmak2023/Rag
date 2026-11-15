# 45. Feature store lite (without buying a platform)

A feature store is: the same feature function in training and serving,
with point-in-time correctness, documented grain, and an owner.

You can fake 80% of Feast with a Python module and SQL.

## Rules

1. One function `features_for(as_of, ids) -> DataFrame`
2. Train calls it for historical as_of dates
3. Serve calls it for as_of=now (or reads a nightly snapshot)
4. Tests lock a golden row
5. A yaml or markdown dict: name, dtype, owner, leak risk

## Anti-pattern

Notebook cell 17 computes `days_since_last` differently from the API.
That is training-serving skew. Fire the notebook, keep the function.

## Lab

You already have `capstone-a-churn/src/features.py` and
`labs/06_sql_features.py`. Add a `FEATURE.md` in capstone A that lists
each column in one line. That document is the store.

## When to buy a real store

Many teams, many models, same features, online serving with millisecond
lookups. Not your first month. Chapter 31.

## Pass / fail

Point at one function used by train and serve. If they are two copies,
you fail this chapter.
