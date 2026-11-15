# 23. First seven days (do this even if you skip ahead later)

## Day 0 (today, 90 minutes)

1. Create the venv, install `requirements.txt` (torch/tf can wait until
   week 5 if the install is heavy; install numpy pandas sklearn fastapi
   first).
2. Read `00-job-skill-map.md` and `14-onsite-cheatsheet.md`.
3. Write salary, notice, onsite sentence in `12-interview-onsite.md`
   on paper.
4. Run `labs/01_numpy_warmup.py`.
5. If MATLAB is still faster than Python in your head, skim
   `26-matlab-to-python.md` the same day.

## Day 1

`labs/01_pandas_etl.py` then rewrite it from memory.
Read chapter 01. Tick week 1 in `labs/progress.md` only if the
self-check passes.

## Day 2

Chapter 02. Run `labs/02_gd_linear.py`. Derive MSE gradient on paper.

## Day 3

`labs/03_churn_baseline.py` and `labs/03_leakage.py`.
Say out loud why accuracy is a trap on 10% churn.

## Day 4

`labs/03_column_transformer.py`. Start `labs/churn_proto` tests.

## Day 5

`labs/06_sql_features.py`. Point-in-time: the 999 amount after as_of
must not appear. Confirm the assert.

## Day 6

`python labs/serve/train_tiny.py` then uvicorn the tiny API.
curl /health and /predict. This is your first "deployed model".

## Day 7

Rest the fingers. Recite the five "seasoned" checks from chapter 00.
If you cannot, days 1-6 were reading, not training. Repeat the failed
lab only.

Do not open PyTorch until day 7 is honest.
