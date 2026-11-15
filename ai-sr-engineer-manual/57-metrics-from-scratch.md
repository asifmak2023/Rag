# 57. Metrics from scratch (whiteboard insurance)

sklearn is allowed at work. Onsite they may say "no libraries".

## Definitions

```
tp = predicted 1 and true 1
fp = predicted 1 and true 0
tn = predicted 0 and true 0
fn = predicted 0 and true 1

accuracy  = (tp+tn) / n
precision = tp / (tp+fp)
recall    = tp / (tp+fn)
f1        = 2 * p * r / (p+r)
```

Zero division: if tp+fp == 0, precision = 0 (or undefined; pick 0 and
say so).

## Lab 57. File: `labs/57_metrics_scratch.py`

Implement confusion + f1. Assert against sklearn on a tiny array.

ROC-AUC intuition: probability a random positive scores higher than a
random negative. You do not need to code AUC in the interview. You
need that sentence.

## Pass / fail

Write f1 from tp,fp,fn on a whiteboard in 3 minutes.
