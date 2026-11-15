import numpy as np


def softmax(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


logits = np.array([[4.0, 0.2], [2.0, 0.1]], dtype=float)
p1 = softmax(logits)
p2 = softmax(logits / 2.0)
print("T=1", p1[:, 0].round(3))
print("T=2", p2[:, 0].round(3))
assert p2[0, 0] < p1[0, 0]
