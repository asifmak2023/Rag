# 53. Tests that are not a joke

Chapter 07 had contract tests. Capstone A has two. This is the rest of
the suite a senior actually writes.

## What to test

- Feature function: known input, known output (golden)
- Leak columns absent from the matrix
- Schema: required columns present
- `predict` rejects NaN and wrong length
- Threshold in (0,1)
- Metrics.json has winner and version
- Invariant: probability in [0,1]

## What not to test

- "AUC > 0.99" on random data
- Bit-identical GBDT across OS
- Pixel-perfect plots

## Lab

Run:

```bash
pytest labs/tests labs/churn_proto/tests capstone-a-churn/tests
```

If pytest is missing, `pip install pytest` in the venv.

Add one test whenever a production bug bites. That is the real policy.

## Pass / fail

`pytest` green on those three folders. A red test you skip is a lie.
