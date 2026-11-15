import numpy as np


def dcg(rels):
    rels = np.asarray(rels, dtype=float)
    denom = np.log2(np.arange(2, len(rels) + 2))
    return float((rels / denom).sum())


def ndcg(rels, k=5):
    rels = np.asarray(rels)[:k]
    ideal = np.sort(rels)[::-1]
    i = dcg(ideal)
    return 0.0 if i == 0 else dcg(rels) / i


good = ndcg([3, 2, 0, 1, 0])
bad = ndcg([0, 0, 0, 0, 3])
print("ndcg good", round(good, 4), "bad", round(bad, 4))
assert good > bad
