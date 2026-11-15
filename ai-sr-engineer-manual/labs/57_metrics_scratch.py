import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score


def confusion(y, p):
    y = np.asarray(y).astype(int)
    p = np.asarray(p).astype(int)
    tp = int(((p == 1) & (y == 1)).sum())
    fp = int(((p == 1) & (y == 0)).sum())
    tn = int(((p == 0) & (y == 0)).sum())
    fn = int(((p == 0) & (y == 1)).sum())
    return tp, fp, tn, fn


def prec_rec_f1(y, p):
    tp, fp, tn, fn = confusion(y, p)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0.0
    )
    return precision, recall, f1


y = np.array([0, 0, 1, 1, 1, 0, 1, 0])
p = np.array([0, 1, 1, 1, 0, 0, 1, 0])
pr, rc, f1 = prec_rec_f1(y, p)
print("tp fp tn fn", confusion(y, p))
print("p r f1", pr, rc, f1)
assert abs(pr - precision_score(y, p)) < 1e-12
assert abs(rc - recall_score(y, p)) < 1e-12
assert abs(f1 - f1_score(y, p)) < 1e-12
