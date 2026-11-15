# 73. Clustering (unsupervised, not a classifier)

k-means: pick k, assign nearest centroid, update means, repeat. Scale
first. Sensitive to k and init. Elbow / silhouette are heuristics, not
truth.

Use: segment customers for a marketing talk, find weird groups in EDA.
Do not report "accuracy" unless you have labels, in which case you
probably wanted classification.

Lab 73. File: `labs/73_kmeans.py`

k=3 on blobs, print inertia and a crosstab vs true blob id if you used
`make_blobs`.

Pass / fail: "unsupervised" and "you pick k" said out loud.
