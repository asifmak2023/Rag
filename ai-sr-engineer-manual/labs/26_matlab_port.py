import numpy as np

A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])
x = np.linalg.solve(A, b)
print("x", x, "Ax", A @ x)
assert np.allclose(A @ x, b)


def moving_mean(x, k=5):
    x = np.asarray(x, dtype=float)
    k = min(k, len(x))
    c = np.cumsum(x)
    out = np.empty_like(c)
    out[:k] = c[:k] / np.arange(1, k + 1)
    out[k:] = (c[k:] - c[:-k]) / k
    return out


x = np.arange(10.0)
print("moving_mean", moving_mean(x, 3))

t = np.linspace(0, 2 * np.pi, 256)
y = np.sin(t)
spec = np.fft.fft(y)
print("fft peak bin", int(np.argmax(np.abs(spec[:128]))))
