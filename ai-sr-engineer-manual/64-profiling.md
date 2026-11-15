# 64. Profile before you rewrite in C++

Your C++ years are a weapon only after you measure.

## Python

```python
import cProfile, pstats
cProfile.run("train()", sort="cumtime")
```

Or `python -m cProfile -s cumtime labs/03_churn_baseline.py`.

Look at: pandas `apply` on rows, Python loops, giant copies.

## Serving

time `curl` 100 times. p95. If 3 ms, stop. If 300 ms, check:

- model loaded every request (bug)
- DataFrame constructed from one row in a slow way
- logging too much
- cold start

## Interview

"I profile. I vectorize. I only drop to C++/pybind11 for a proven hot
loop. Logistic on 40 floats is not that loop."

## Pass / fail

You have one sentence with a measured millisecond number from your
own API, even if it is localhost.
