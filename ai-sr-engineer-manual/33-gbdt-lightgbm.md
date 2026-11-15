# 33. GBDT in practice: HistGB, LightGBM, XGBoost

The posting says "popular AI/ML framework". For tabular consulting
work, boosting is that framework more often than PyTorch.

sklearn `HistGradientBoosting*` is enough to start. LightGBM is what
many teams actually run. XGBoost is the name managers know.

## Same idea

Fit a small tree to the residual of the previous trees. Shrink each
tree by a learning rate. Stop when val loss stalls.

## When to pick which

| Tool | Use |
|---|---|
| HistGradientBoosting | No extra pip politics, missing values native, good default |
| LightGBM | Large tables, categoricals, speed |
| XGBoost | Existing team standard, GPU optional |
| CatBoost | Lots of categoricals, if the team already has it |

Do not install all three on day one. HistGB, then LightGBM.

## Lab 33A. HistGB vs logistic (you already have this)

Capstone A. Recite the table: AUC, F1, p95 if you timed it.

## Lab 33B. LightGBM API

File: `labs/33_lightgbm.py`

If `lightgbm` is not installed: `pip install --break-system-packages lightgbm`
or install inside `~/ai-env`.

```python
import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=5000, n_features=30, n_informative=8,
    weights=[0.9, 0.1], random_state=0,
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
train = lgb.Dataset(Xtr, ytr)
valid = lgb.Dataset(Xte, yte, reference=train)
params = {
    "objective": "binary",
    "metric": "auc",
    "learning_rate": 0.05,
    "num_leaves": 31,
    "max_depth": 5,
    "min_child_samples": 40,
    "verbose": -1,
    "is_unbalance": True,
}
model = lgb.train(
    params,
    train,
    num_boost_round=200,
    valid_sets=[valid],
    callbacks=[lgb.early_stopping(20), lgb.log_evaluation(50)],
)
pred = model.predict(Xte, num_iteration=model.best_iteration)
print("auc", roc_auc_score(yte, pred))
```

sklearn wrapper if you want a Pipeline:

```python
from lightgbm import LGBMClassifier
clf = LGBMClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    class_weight="balanced",
)
```

Put `ColumnTransformer` in front. Same rule as chapter 03.

## Categoricals

LightGBM can take integer codes and `categorical_feature`. sklearn
OneHot also works. Do not one-hot 100k IDs.

## Importances

```python
# gain vs split count
model.feature_importance(importance_type="gain")
```

Importance is not causality. "This feature is used a lot" is not
"raise this slider in the product".

## Interview

"I baseline with logistic in a Pipeline, then HistGB or LightGBM. I
do not start with a net on 40 numeric columns."

## Pass / fail

Train LightGBM or HistGB, print best iteration, AUC, and three top
features. Explain early stopping in one sentence.
