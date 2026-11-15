# 83. Multiclass: OVR, softmax, macro vs micro

Binary tools extend.

- Logistic / softmax: one linear score per class, softmax, cross entropy
- Trees: native multiclass
- OVR: one binary model per class vs rest
- OVO: one per pair, rare now

Metrics:

- micro-F1: pool tp/fp/fn globally (dominated by frequent classes)
- macro-F1: unweighted mean of per-class F1 (cares about rare classes)
- weighted-F1: support-weighted

Confusion matrix is the slide. Read off which pair confuses.

## Lab 83. File: `labs/83_multiclass.py`

3-class `make_classification`. Print classification_report. Note
macro vs weighted.

## Pass / fail

You ask "do rare classes matter equally?" before you pick macro vs
micro.
