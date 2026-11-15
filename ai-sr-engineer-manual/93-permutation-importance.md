# 93. Permutation importance (less lying than raw tree gain)

Shuffle one column on validation, measure the drop in the metric.
Large drop => the model used that column. Does not prove causality.

Better than "gain" when correlated features split credit arbitrarily.

Still leaks if you permute a leak column: it will look "important".
Importance does not certify a feature is legal.

## Lab 93. File: `labs/93_perm.py`

`sklearn.inspection.permutation_importance` on a fitted pipeline.
Print top 3 feature indices.

## Pass / fail

"Importance is not why, and it is not permission to use a leak."
