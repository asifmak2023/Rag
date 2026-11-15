# 03. scikit-learn: the default tool for tabular AI

Most "AI solutions" in consulting are classification or regression on
tables. If you reach for a neural net first, you look junior.

## The only pattern you need

```
raw -> split -> Pipeline(preprocess, model) -> CV on train -> test once
```

Never preprocess before splitting. That is leakage.

## Lab 03A. End-to-end classification

File: `labs/03_churn_baseline.py`

Use any binary table. If you have no data, synthesize:

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score

X, y = make_classification(
    n_samples=4000, n_features=20, n_informative=6,
    weights=[0.9, 0.1], random_state=0,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0,
)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1")
print("cv f1", scores.mean(), scores.std())

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print(classification_report(y_test, pred))
print("test f1", f1_score(y_test, pred))
```

Self-check: change `class_weight` off and watch recall on the rare class
die. Write that number in your notes.

## Lab 03B. Mixed types, real preprocess

File: `labs/03_column_transformer.py`

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingClassifier

df = pd.DataFrame({
    "age": [21, 35, None, 40, 29, 51],
    "city": ["KHI", "LHE", "KHI", None, "ISB", "KHI"],
    "income": [50, 80, 40, 120, 70, 90],
    "churn": [0, 0, 1, 0, 1, 0],
})
num = ["age", "income"]
cat = ["city"]
pre = ColumnTransformer([
    ("num", Pipeline([
        ("imp", SimpleImputer(strategy="median")),
        ("sc", StandardScaler()),
    ]), num),
    ("cat", Pipeline([
        ("imp", SimpleImputer(strategy="most_frequent")),
        ("oh", OneHotEncoder(handle_unknown="ignore")),
    ]), cat),
])
model = Pipeline([
    ("pre", pre),
    ("clf", HistGradientBoostingClassifier(max_depth=3)),
])
# too few rows to be serious; the API is the lesson
model.fit(df[num + cat], df["churn"])
```

This object is what you pickle and put in Docker. Not a notebook.

## Models you must be able to choose

| Problem | First model | When to upgrade |
|---|---|---|
| Linear-ish tabular | Logistic / Ridge | After a strong baseline |
| Mixed tabular | HistGradientBoosting or LightGBM | Always try trees |
| High dimension text counts | Linear SVM / logistic on TF-IDF | Then deep models |
| Clusters, no labels | k-means, then look at PCA plot | GMM / HDBSCAN if needed |
| Ranking / search | GBDT on features | Two-tower later |

Know the hyperparameters that matter:

- Trees: `max_depth`, `learning_rate`, `min_samples_leaf`, `n_estimators`
- Linear: `C` or `alpha`, `class_weight`
- SVM: `C`, kernel (RBF only if d is small)

## Lab 03C. Leakage hunt (this is how seniors think)

Create a feature that is the target in disguise, watch AUC become 1.0,
then remove it.

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

rng = np.random.default_rng(0)
y = rng.integers(0, 2, size=2000)
X_ok = rng.normal(size=(2000, 5))
X_leak = np.column_stack([X_ok, y.astype(float)])  # last col is target

for name, X in [("ok", X_ok), ("leak", X_leak)]:
    m = LogisticRegression().fit(X, y)
    print(name, roc_auc_score(y, m.predict_proba(X)[:, 1]))
```

Other leaks: customer_id as a feature, future timestamps, row index,
target encoding fitted on the full data.

## Lab 03D. Imbalance and threshold

`predict` uses 0.5. Business rarely wants 0.5.

```python
from sklearn.metrics import precision_recall_curve
proba = pipe.predict_proba(X_test)[:, 1]
p, r, t = precision_recall_curve(y_test, proba)
# pick threshold with recall >= 0.8 and best precision
```

Practice saying: "I will not ship the default threshold. I will pick it
from the cost of false positives vs false negatives."

## Persistence

```python
import joblib
joblib.dump(pipe, "model.joblib")
pipe2 = joblib.load("model.joblib")
```

Save the whole Pipeline. Saving only the classifier without the scaler
is a production incident.

## Pass / fail

Pass if you can, from a raw CSV in 45 minutes:

1. Identify target, IDs, dates
2. Time-aware or stratified split
3. ColumnTransformer + model
4. CV F1 and a test report
5. Name two likely leaks
