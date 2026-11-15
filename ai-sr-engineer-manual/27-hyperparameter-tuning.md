# 27. Hyperparameters: search like an engineer

Random search beats fancy folklore on small budgets. Nested CV is
correct and often too slow. This is the consulting compromise.

## What you tune, what you do not

Do not tune everything. Tune the knobs that move the metric.

Logistic / linear:

- `C` or `alpha` (log grid: 1e-3 ... 1e3)
- `class_weight`

Trees / HistGB / LightGBM:

- `max_depth` or `num_leaves`
- `learning_rate` with `n_estimators` / `max_iter`
- `min_samples_leaf` / `min_child_samples`
- `l2_regularization`

Neural nets:

- learning rate first
- then batch size, weight decay, dropout
- architecture last, and only after the loop is known-good

## Lab 27A. sklearn search, small and honest

File: `labs/27_search.py`

```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import loguniform

X, y = make_classification(
    n_samples=2000, n_features=20, weights=[0.85, 0.15], random_state=0
)
pipe = Pipeline([
    ("sc", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
])
search = RandomizedSearchCV(
    pipe,
    {"clf__C": loguniform(1e-3, 1e2)},
    n_iter=12,
    scoring="f1",
    cv=StratifiedKFold(5, shuffle=True, random_state=0),
    random_state=0,
    n_jobs=1,
)
search.fit(X, y)
print(search.best_params_, search.best_score_)
```

Rules:

- Search on train folds only. The real test set stays in a vault.
- `n_jobs=-1` is fine on your laptop. Do not melt a shared server.
- Report best CV score AND the untouched test score. The gap is
  overfitting to the search.

## Lab 27B. Manual LR finder for torch (no library)

Train 30 steps at 1e-4, 1e-3, 1e-2. Plot loss. Pick the largest rate
where loss still drops smoothly. That is enough for this job.

## Optuna (optional, week 12)

Know the name: define a `objective(trial)` that returns val metric,
`trial.suggest_float("lr", 1e-4, 1e-2, log=True)`. If you use it, cap
trials (20-40). Unbounded search is not research, it is stalling.

## Early stopping

Trees: `n_iter_no_change` / `early_stopping`.
Keras: `EarlyStopping(restore_best_weights=True)`.
PyTorch: if val loss does not improve for p epochs, break and load
best `state_dict` you cached.

Early stopping is a regularizer. Say that.

## Pass / fail

You can explain why you did not grid-search 10,000 combinations, and
you have one RandomizedSearchCV run in `labs/`.
