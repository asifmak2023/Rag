# 95. CSV vs Parquet (large data, small disk)

CSV: universal, slow, no types, huge.
Parquet: columnar, compressed, typed, pandas/Spark/SQL engines like it.

For the posting's "large data streams": store extracts as Parquet,
not 8 GB CSVs on a laptop.

## Lab 95. File: `labs/95_parquet.py`

Write a DataFrame to parquet and csv if pyarrow/fastparquet exists,
else skip. Print file sizes when both work.

```bash
pip install pyarrow
```

Interview: "I will not email a 2 GB CSV. I will write partitioned
Parquet by date."

## Pass / fail

You know CSV has no schema and Parquet does.
