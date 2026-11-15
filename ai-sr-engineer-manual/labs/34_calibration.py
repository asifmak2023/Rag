from sklearn.calibration import calibration_curve
from sklearn.datasets import make_classification
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=4000, n_features=16, weights=[0.8, 0.2], random_state=0
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
for name, m in [
    ("logreg", LogisticRegression(max_iter=1000)),
    ("hgb", HistGradientBoostingClassifier(max_depth=3, random_state=0)),
]:
    m.fit(Xtr, ytr)
    p = m.predict_proba(Xte)[:, 1]
    frac, meanp = calibration_curve(yte, p, n_bins=8, strategy="quantile")
    pairs = list(zip(meanp.round(3).tolist(), frac.round(3).tolist()))
    print(name, pairs)
