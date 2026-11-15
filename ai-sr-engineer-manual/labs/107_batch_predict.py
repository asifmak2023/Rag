import time

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=1000, n_features=20, random_state=0)
m = LogisticRegression(max_iter=1000).fit(X, y)
Xq = X[:500]
t0 = time.perf_counter()
for row in Xq:
    m.predict(row.reshape(1, -1))
t_loop = time.perf_counter() - t0
t0 = time.perf_counter()
m.predict(Xq)
t_mat = time.perf_counter() - t0
print("loop_s", round(t_loop, 4), "matrix_s", round(t_mat, 4))
assert t_mat < t_loop
