import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
inliers = rng.normal(size=(400, 2))
outliers = rng.normal(loc=6.0, scale=0.4, size=(12, 2))
X = np.vstack([inliers, outliers])
clf = IsolationForest(contamination=0.03, random_state=0).fit(X)
pred = clf.predict(X)
caught = int((pred[-12:] == -1).sum())
print("caught outliers", caught, "of 12", "flagged total", int((pred == -1).sum()))
assert caught >= 8
