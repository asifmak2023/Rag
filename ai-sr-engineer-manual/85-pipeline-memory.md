# 85. Memorize a Pipeline (closed-book exam)

Write this from nothing. 12 minutes.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import HistGradientBoostingClassifier

pre = ColumnTransformer([
    ("num", Pipeline([
        ("imp", SimpleImputer(strategy="median")),
        ("sc", StandardScaler()),
    ]), num_cols),
    ("cat", Pipeline([
        ("imp", SimpleImputer(strategy="most_frequent")),
        ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]), cat_cols),
])
model = Pipeline([
    ("pre", pre),
    ("clf", HistGradientBoostingClassifier(max_depth=3, random_state=0)),
])
```

Then: split, fit on train, `predict_proba` on test, F1 at a chosen
threshold.

If you cannot, you are not week-4 done. Repeat chapter 03.

## Pass / fail

Blank laptop, this object, plus a split. Timer.
