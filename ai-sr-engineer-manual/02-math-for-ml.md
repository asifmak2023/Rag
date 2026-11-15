# 02. Math you must speak, not just have passed

The posting asks for linear algebra, algorithms, statistics. Onsite they
will not ask you to invert a 4x4 by hand. They will ask you why a model
diverged, why accuracy is a bad metric, and what a gradient is.

Write every derivation in `labs/02_math.md` in your own words.

## 1. Linear algebra (one weekend)

Objects: vector, matrix, rank, inverse vs pseudoinverse, eigenvalues.

You must compute by hand for 2x2:

- Dot product, matrix-vector product
- Determinant, inverse if it exists
- Eigenvalues of `[[2, 1], [1, 2]]`

Meaning in ML:

- A dataset is `X` shape `(n, d)`. A linear model is `Xw`.
- Collinear features => rank-deficient `X.T @ X` => unstable `w`.
- PCA is eigendecomposition of the covariance (or SVD of X).
- Attention and embeddings are matrix multiplies. Nothing mystical.

Lab 02A:

```python
import numpy as np
X = np.array([[1., 2.], [2., 4.], [3., 6.]])  # rank 1
print(np.linalg.matrix_rank(X))
try:
    np.linalg.inv(X.T @ X)
except np.linalg.LinAlgError as e:
    print("expected", e)
print(np.linalg.pinv(X.T @ X))
```

Say out loud: "I cannot invert this. I can still project with pinv, but
coefficients are not unique."

## 2. Calculus and optimization

A loss `L(w)`. Gradient `dL/dw` points uphill. We go the other way.

Gradient descent:

```
w <- w - lr * grad
```

You must:

- Derive the gradient of MSE for linear regression.
- Explain learning rate too big (diverges) vs too small (crawls).
- Name local minima, saddle points, and why SGD helps.

Lab 02B. Fit `y = 3x + 2` with plain GD in NumPy. No sklearn.

```python
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
print(w, b)
```

Stop when `|w-3| < 0.1` and `|b-2| < 0.1`.

## 3. Probability and statistics

Memorize these as working tools:

- Expectation, variance, covariance
- Bayes: `P(H|D) = P(D|H)P(H) / P(D)`
- Gaussian, Bernoulli, categorical
- MLE vs MAP (L2 regularization is a Gaussian prior on weights)
- Train / val / test. Why you never tune on test.
- Bias-variance. Underfit vs overfit.
- p-values: you do not need to worship them. You do need to know a
  confidence interval on a metric.

Classification metrics (write definitions from memory):

- Accuracy, precision, recall, F1
- ROC-AUC vs PR-AUC (imbalance: use PR-AUC)
- Confusion matrix, cost-sensitive threshold

Lab 02C. You have 1000 negatives and 10 positives. A model that always
predicts negative has 99% accuracy. Compute precision, recall, F1 of that
model. Then explain why the business cannot use accuracy.

## 4. Algorithms they expect

- Time/space of training linear models, trees, kNN, naive Bayes
- Why kNN is lazy and dies at scale
- Mini-batch SGD as streaming: you do not need all data in RAM
- Hashing trick / feature hashing for high-cardinality IDs
- Approximate nearest neighbors if they ask about search

## Whiteboard scripts (practice standing up)

Do each in 8 minutes on paper:

1. Derive logistic regression gradient.
2. Draw train and val loss for overfit, underfit, good fit.
3. Explain k-fold vs time-series split. When k-fold leaks.
4. SVD in one picture: X = U S V.T, keep top k.
5. Regularization: L1 sparse, L2 small weights, elastic net both.

## Pass / fail

Pass if you can teach logistic regression to a junior in 15 minutes
with equations and a drawing, no slides.
