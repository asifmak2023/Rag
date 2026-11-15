import numpy as np
from sklearn.model_selection import GroupKFold, train_test_split

rng = np.random.default_rng(0)
user = np.repeat(np.arange(100), 5)
X = rng.normal(size=(500, 4))
y = rng.integers(0, 2, size=500)

Xtr, Xte, ytr, yte, utr, ute = train_test_split(
    X, y, user, test_size=0.2, random_state=0
)
overlap = set(utr) & set(ute)
print("random split user overlap", len(overlap))

gkf = GroupKFold(n_splits=5)
n_overlap = []
for tr, te in gkf.split(X, y, groups=user):
    n_overlap.append(len(set(user[tr]) & set(user[te])))
print("groupkfold overlaps", n_overlap)
assert max(n_overlap) == 0
