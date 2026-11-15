# 87. Feature hashing (huge categoricals)

One-hot on 2 million SKUs will not fit. Hash the token into a fixed
number of buckets. Collisions exist. That is the trade.

sklearn: `FeatureHasher`, `HashingVectorizer` for text (stateless,
good for streaming, chapter 06).

Pros: constant memory, no vocabulary file, train/serve match if the
hash function and n_features match.

Cons: collisions, cannot easily invert to feature names, interpretability
dies.

## Lab 87. File: `labs/87_hashing.py`

HashingVectorizer vs TfidfVectorizer on tiny tickets. Print shapes.
Hashing is fixed-width.

## Interview

"I hash high-cardinality IDs into 2^18 buckets for a linear model. I
do not one-hot user_id."

## Pass / fail

You name collisions and the missing inverse mapping.
