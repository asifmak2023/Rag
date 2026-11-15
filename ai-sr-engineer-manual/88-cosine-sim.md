# 88. Cosine similarity (search, duplicates, RAG retrieval)

```
cos(a,b) = (a·b) / (||a|| ||b||)
```

Scale-invariant. 1 = same direction, 0 = orthogonal, -1 = opposite.
For bag-of-words and embeddings, this is the default "are these two
texts related" score.

Nearest neighbor in embedding space = retrieval. That is the R in RAG
(chapter 60). Garbage corpus => garbage answers.

## Lab 88. File: `labs/88_cosine.py`

TF-IDF vectors, cosine of a query to three docs. Argmax is the hit.

## Pass / fail

Write the formula. Say why Euclidean on raw counts is worse (length).
