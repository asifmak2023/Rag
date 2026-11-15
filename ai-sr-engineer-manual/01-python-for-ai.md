# 01. Python for AI (from C/C++/MATLAB)

You already think in arrays and pointers. Python hides memory. For AI you
must put the memory model back in your head, then never write a Python
loop over rows.

## Mental translation

| MATLAB / C++ | Python AI |
|---|---|
| `A * B` matrix multiply | `A @ B` |
| `A .* B` elementwise | `A * B` |
| 1-based index | 0-based |
| column-major MATLAB | row-major NumPy (C order) |
| `NaN` | `np.nan` and pandas `NA` |
| `for i` over matrix | vectorize or it is wrong |
| `std::vector` | `list` (slow) or `np.ndarray` (fast) |
| classes / RAII | classes + context managers |

## Lab 01A. NumPy until it is boring

File: `labs/01_numpy_warmup.py`

Do this by typing, not copy-paste.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 8))
w = rng.normal(size=(8, 1))
y = X @ w + 0.1 * rng.normal(size=(1000, 1))

# Standardize columns without a loop
mu = X.mean(axis=0, keepdims=True)
sd = X.std(axis=0, keepdims=True) + 1e-8
Xn = (X - mu) / sd

# Closed-form linear regression
XtX = Xn.T @ Xn
w_hat = np.linalg.solve(XtX, Xn.T @ y)
mse = np.mean((Xn @ w_hat - y) ** 2)
print(mse)
```

Self-check:

- Explain why `keepdims=True` matters.
- Replace `solve` with `lstsq` and get the same answer.
- Time a Python nested loop vs `@` on 5000x5000. Write the two numbers.

## Lab 01B. pandas the way production uses it

File: `labs/01_pandas_etl.py`

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "user_id": [1, 1, 2, 2, 3, None],
    "ts": pd.to_datetime([
        "2024-01-01", "2024-01-03", "2024-01-01",
        "2024-01-02", "2024-01-05", "2024-01-06",
    ]),
    "amount": [10, 40, 5, np.nan, 100, 20],
    "city": ["KHI", "khi", "LHE", "LHE", None, "ISB"],
})

df["city"] = df["city"].str.upper().fillna("UNKNOWN")
df["user_id"] = df["user_id"].astype("Int64")
df["amount"] = df["amount"].fillna(df.groupby("city")["amount"].transform("median"))

feat = (
    df.sort_values("ts")
      .groupby("user_id", dropna=False)
      .agg(
          n=("amount", "size"),
          sum_amount=("amount", "sum"),
          last_ts=("ts", "max"),
      )
      .reset_index()
)
print(feat)
```

Self-check:

- What does `transform` do that `agg` does not?
- Why is `astype("Int64")` used instead of `int`?
- Write a version that never uses `inplace=True`.

Forbidden: `iterrows`, `itertuples` for feature math, chained indexing
like `df[df.a > 1]["b"] = 0`.

## Lab 01C. Project layout of an AI service

Create this and keep it for later chapters:

```
labs/churn_proto/
  data/
  src/
    __init__.py
    features.py
    model.py
    serve.py
  tests/
    test_features.py
  README.md
```

`features.py` must contain one pure function:

```python
def add_amount_z(df):
    mu = df["amount"].mean()
    sd = df["amount"].std(ddof=0) or 1.0
    out = df.copy()
    out["amount_z"] = (out["amount"] - mu) / sd
    return out
```

Test it with pytest. Models without tests are homework, not engineering.

## Python skills that show up in interviews

1. List vs generator vs numpy array. Memory.
2. Mutable default arguments. Never `def f(xs=[])`.
3. `*args`, `**kwargs`, dataclasses, type hints.
4. Virtualenv, `requirements.txt`, pin versions.
5. Exceptions: catch specific ones, log, re-raise if you cannot handle.

## MATLAB exercise (do once)

Take a MATLAB script you still remember (FFT, linear system, plot).
Rewrite it in NumPy + matplotlib in under 30 minutes. Put both side by
side in `labs/01_matlab_port.md`. This is how you talk about your past.

## Pass / fail

Pass if you can, from memory:

- Standardize a matrix
- Group-by aggregate in pandas
- Write a pytest for a feature function
- Explain broadcasting in two sentences
