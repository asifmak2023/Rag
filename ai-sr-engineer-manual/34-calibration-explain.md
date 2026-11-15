# 34. Calibration and explanation

A score of 0.8 that is not ~80% true is a lying probability. Ops
teams notice. Also: "why did this customer get 0.8?"

## Calibration

Lab 34A. File: `labs/34_calibration.py`

```python
from sklearn.calibration import calibration_curve
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier

X, y = make_classification(n_samples=4000, weights=[0.8, 0.2], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
for name, m in [
    ("logreg", LogisticRegression(max_iter=1000)),
    ("hgb", HistGradientBoostingClassifier(max_depth=3, random_state=0)),
]:
    m.fit(Xtr, ytr)
    p = m.predict_proba(Xte)[:, 1]
    frac, meanp = calibration_curve(yte, p, n_bins=8, strategy="quantile")
    print(name, list(zip(meanp.round(3), frac.round(3))))
```

If trees are over-confident, wrap with `CalibratedClassifierCV`
(isotonic or sigmoid) on a validation fold. Recalibrate when you
retrain. Do not calibrate on the test set.

Interview: "I will not tell the call center that 0.9 means 90% unless
I have a reliability plot."

## Explanation without a 200-page SHAP thesis

1. Linear: coefficients after scaling. Sign and magnitude.
2. Trees: gain importance + a few `plot_tree` / leaf rules.
3. Partial dependence on 1-2 key features.
4. For one row: "tenure low, month-to-month, fiber" is better than
   a SHAP screenshot nobody can audit.

SHAP: know the name. Use it if the bank requires per-loan reasons.
Install later. Do not lead with it.

Lab 34B. Print logistic coefficients with feature names from a
Pipeline. Map one-hot names back. Write three English sentences.

## Counterfactuals (product language)

"If they switched to a one-year contract, the score would drop."
That is a partial dependence / what-if on one row. Useful. Dangerous
if you imply causation. Say "associated with", not "causes".

## Pass / fail

Show a reliability list of bins and explain one customer's score
without opening SHAP.
