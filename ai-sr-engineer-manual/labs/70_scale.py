import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
n = 800
x1 = rng.normal(size=n)
x2 = rng.normal(loc=0, scale=1000, size=n)
X = np.column_stack([x1, x2])
y = (x1 + 0.001 * x2 > 0).astype(int)
Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)
knn = KNeighborsClassifier(n_neighbors=15)
print("unscaled acc", float(knn.fit(Xtr, ytr).score(Xte, yte)))
sc = StandardScaler().fit(Xtr)
print("scaled acc", float(knn.fit(sc.transform(Xtr), ytr).score(sc.transform(Xte), yte)))
