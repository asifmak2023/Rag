import numpy as np


def softmax(x):
    z = x - np.max(x, axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def cross_entropy(logits, y_index):
    p = softmax(logits)
    return float(-np.log(p[y_index] + 1e-12))


logits = np.array([2.0, 1.0, 0.1])
p = softmax(logits)
assert abs(p.sum() - 1) < 1e-8
print("softmax", p)
print("ce class0", cross_entropy(logits, 0))
