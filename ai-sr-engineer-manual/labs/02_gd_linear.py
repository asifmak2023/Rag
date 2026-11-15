import numpy as np

rng = np.random.default_rng(1)
x = rng.normal(size=200)
y = 3 * x + 2 + 0.2 * rng.normal(size=200)
w, b = 0.0, 0.0
lr = 0.1
for _ in range(200):
    pred = w * x + b
    err = pred - y
    w -= lr * (2 * err * x).mean()
    b -= lr * (2 * err).mean()
print("w", w, "b", b)
assert abs(w - 3) < 0.15 and abs(b - 2) < 0.15
