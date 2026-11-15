# 106. Mixup (simple augmentation)

Take two train examples, mix x and y:

```
x = lam * x_i + (1-lam) * x_j
y = lam * y_i + (1-lam) * y_j
```

lam ~ Beta(alpha, alpha). Teaches smoother decision boundaries.
Used in vision. Know the name. Do not mixup tabular IDs or one-hots
without thinking.

## Pass / fail

You can write the two lines. You do not mixup the test set.
