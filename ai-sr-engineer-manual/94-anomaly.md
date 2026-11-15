# 94. Anomaly detection (when there is no label)

Fraud/ops sometimes has almost no confirmed positives. Then you are
not doing classification. You are ranking weirdness.

Tools:

- IsolationForest: random splits, anomalies are easy to isolate
- One-class SVM: name it
- Autoencoder reconstruction error: if you already have nets
- Simple: z-score, IQR, "amount vs city median"

v1 is often a rule plus IsolationForest on a few numeric columns,
reviewed by a human. Do not advertise "AI fraud engine" for that.

## Lab 94. File: `labs/94_iforest.py`

Inliers from a blob, a few far points. IsolationForest `contamination`.
Print how many far points got score below 0.

## Interview

"Unsupervised anomaly is a triage list, not a guilty verdict."

## Pass / fail

You refuse to report accuracy when there are no labels.
