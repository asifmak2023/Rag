import time
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 8))
w = rng.normal(size=(8, 1))
y = X @ w + 0.1 * rng.normal(size=(1000, 1))

mu = X.mean(axis=0, keepdims=True)
sd = X.std(axis=0, keepdims=True) + 1e-8
Xn = (X - mu) / sd

w_hat = np.linalg.solve(Xn.T @ Xn, Xn.T @ y)
w_lstsq = np.linalg.lstsq(Xn, y, rcond=None)[0]
mse = np.mean((Xn @ w_hat - y) ** 2)
print("mse", float(mse))
print("solve vs lstsq max abs", float(np.max(np.abs(w_hat - w_lstsq))))

n = 400
A = rng.normal(size=(n, n))
B = rng.normal(size=(n, n))
t0 = time.perf_counter()
_ = A @ B
t_vec = time.perf_counter() - t0

t0 = time.perf_counter()
C = np.zeros((n, n))
for i in range(n):
    for k in range(n):
        aik = A[i, k]
        C[i] += aik * B[k]
t_loop = time.perf_counter() - t0
print("matmul sec", round(t_vec, 4), "loop-ish sec", round(t_loop, 4))
