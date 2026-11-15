# 42. Ranking and retrieval (search, recs, "similar")

If they say "recommendation engine", they often mean: sort 50 items
for a user. Not a foundation model.

## Three layers

1. Candidate generation: 1M items -> 200. SQL filters, popularity,
   ANN on embeddings.
2. Ranking: 200 -> 10. GBDT on features (user, item, context).
3. Business rules: in stock, already bought, compliance.

v1 is often popularity in that city plus a few rules. Say that.

## Metric

Not accuracy. `recall@k`, `ndcg@k`, `precision@k`. If the user only
sees 5 slots, k=5.

Lab 42. File: `labs/42_ndcg.py`

```python
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

print(ndcg([3, 2, 0, 1, 0]))
print(ndcg([0, 0, 0, 0, 3]))
```

Explain: putting the relevant item first beats putting it last.

## Two-tower (know the picture)

User encoder -> vector. Item encoder -> vector. Score = dot product.
Train with in-batch negatives. Serve: precompute item vectors, ANN
search, then maybe a reranker.

You do not need to implement FAISS for this job. Draw the picture.

## Interview trap

"We will fine-tune an LLM to recommend." For a catalog of 8k SKUs and
a sales table, LightGBM ranker on "bought together" + price + city
ships this quarter. LLM later if queries are free text.

## Pass / fail

Compute NDCG by hand on a 5-item list. Draw candidate -> rank -> rules.
