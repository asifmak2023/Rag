# 81. ROC and PR curves (draw them)

ROC: TPR (recall) vs FPR as you move the threshold.
AUC-ROC: chance a random positive ranks above a random negative.
Pretty even when negatives dominate. Can look "good" while PR is dead.

PR: precision vs recall. Better headline for rare positives.
PR-AUC / average precision: area under that curve.

At threshold 1: no positives predicted, recall 0, precision undefined
or 1 by convention. At 0: everything positive, recall 1, precision =
base rate.

## Lab 81. File: `labs/81_roc_pr.py`

Print `roc_auc_score` and `average_precision_score` on imbalanced data
for majority scores vs a real model. Majority can have ROC not terrible
and PR near the base rate.

## Interview

"I will show the PR curve for fraud, not only ROC."

## Pass / fail

Sketch both axes from memory. Mark the base-rate line on PR.
