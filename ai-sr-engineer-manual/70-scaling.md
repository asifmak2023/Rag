# 70. Feature scaling (when it matters)

Trees: mostly optional. Distances, linear models, nets, kNN, SVM, PCA:
required or they lie.

StandardScaler: mean 0, var 1. Sensitive to outliers (chapter 68).
MinMax: to [0,1]. RobustScaler: median and IQR.

Fit on train. Apply on val/test/serve. Inside Pipeline.

## Lab 70. File: `labs/70_scale.py`

kNN accuracy with and without scaling on two features of different
magnitude. Unscaled should be worse.

## Pass / fail

You never scale before split. You never scale the target for
classification.
