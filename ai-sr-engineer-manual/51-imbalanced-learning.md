# 51. Imbalance without folklore

The posting's real-world problems are often 5% default, 8% churn, 1%
fraud. Accuracy is a trap. Chapter 03 started this. Finish it.

## Order of operations (memorize)

1. Get the metric right (PR-AUC, recall at precision P, cost).
2. `class_weight="balanced"` or scale_pos_weight in LightGBM.
3. Threshold on validation, not 0.5.
4. Better features / more real minority rows.
5. Only then undersample majority or augment minority.
6. SMOTE last, and never on the test fold, never before the split.

SMOTE on mixed categoricals invents fake people. Say no unless you
can defend it.

## Lab 51. File: `labs/51_imbalance.py`

Compare majority baseline vs logistic vs weighted logistic on 5%
positives. Print accuracy (misleading) and F1/recall (honest).

## Cost matrix

False negative costs Rs 50,000 (lost loan). False positive costs
Rs 500 (analyst time). Threshold moves toward catching more defaults.
Write the costs. Do not guess 0.5.

## Pass / fail

You refuse accuracy as the headline on an imbalanced table, twice, in
one interview, without sounding sarcastic.
