# 26. MATLAB to Python cookbook (your existing brain)

You already think in arrays. This chapter is a dictionary, then three
ports you must type.

## Dictionary

| MATLAB | NumPy / pandas |
|---|---|
| `zeros(m,n)` | `np.zeros((m, n))` |
| `ones(m,n)` | `np.ones((m, n))` |
| `eye(n)` | `np.eye(n)` |
| `rand(m,n)` | `rng.random((m, n))` |
| `randn(m,n)` | `rng.normal(size=(m, n))` |
| `size(A)` | `A.shape` |
| `length(v)` | `len(v)` or `v.shape[0]` |
| `A'` | `A.T` |
| `A * B` (matrix) | `A @ B` |
| `A .* B` | `A * B` |
| `A ./ B` | `A / B` |
| `inv(A)` | `np.linalg.inv(A)` |
| `pinv(A)` | `np.linalg.pinv(A)` |
| `A \ b` | `np.linalg.solve(A, b)` |
| `eig(A)` | `np.linalg.eig(A)` |
| `svd(A)` | `np.linalg.svd(A, full_matrices=False)` |
| `fft(x)` | `np.fft.fft(x)` |
| `mean(A,1)` (columns) | `A.mean(axis=0)` |
| `sum(A,2)` (rows) | `A.sum(axis=1)` |
| `find(x>0)` | `np.where(x>0)[0]` |
| `A(1,:)` 1-based | `A[0, :]` |
| `A(:,end)` | `A[:, -1]` |
| `cat(1,A,B)` | `np.vstack([A, B])` |
| `cat(2,A,B)` | `np.hstack([A, B])` |
| `NaN` | `np.nan` |
| `isnan` | `np.isnan` / `df.isna()` |
| `logical indexing` | boolean mask, same idea |
| `struct` | `dict` or `dataclass` |
| `cell` | `list` |
| `plot(x,y)` | `plt.plot(x, y)` |
| `hold on` | just call plot again |
| `save -mat` | `np.savez` or parquet |
| `load` | `np.load` / `pd.read_csv` |
| scripts + cwd | packages + `pathlib` |
| 1-based, column-major | 0-based, row-major C order |

Broadcasting in NumPy is MATLAB `bsxfun` that is always on. If a
`(n,1)` and `(n,)` surprise you, print `.shape` before you debug math.

## Lab 26A. Port a linear system

MATLAB in your head: `x = A \ b`

```python
import numpy as np
A = np.array([[3., 1.], [1., 2.]])
b = np.array([9., 8.])
x = np.linalg.solve(A, b)
print(x, A @ x)
```

If `A` is rectangular, `np.linalg.lstsq(A, b, rcond=None).solution`
(or `[0]` on older numpy). Never `inv(A) @ b` in production.

## Lab 26B. Port a filter / moving average

```python
def moving_mean(x, k=5):
    x = np.asarray(x, dtype=float)
    k = min(k, len(x))
    c = np.cumsum(x)
    out = np.empty_like(c)
    out[:k] = c[:k] / np.arange(1, k + 1)
    out[k:] = (c[k:] - c[:-k]) / k
    return out
```

This is the C++/MATLAB instinct: O(n), no pandas until you need dates.

## Lab 26C. Plot like MATLAB

```python
import matplotlib.pyplot as plt
t = np.linspace(0, 2 * np.pi, 256)
plt.plot(t, np.sin(t), label="sin")
plt.plot(t, np.cos(t), label="cos")
plt.xlabel("t")
plt.ylabel("x")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("labs/matlab_port_plot.png")
```

## Memory talk (use in interview)

"MATLAB hid the copies. In NumPy I watch views vs copies: a slice is
often a view, `X.T` is a view, `np.array(X)` may copy. I profile before
I rewrite a hot loop in C++. For ML, vectorized NumPy plus a GBDT is
faster than a clever Python `for`."

## Pass / fail

Take one real MATLAB script of yours. Port it. Put both in
`labs/01_matlab_port.md`. If you have no script, port least-squares +
FFT of a sine + a plot in 30 minutes.
