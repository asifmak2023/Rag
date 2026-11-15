# Capstone A report

## Problem

Score a customer for churn before an outreach team calls. A false
positive costs a call. A false negative costs a lost subscriber.
Recall floor 0.70, then maximize precision via the threshold search.

## Data

Synthetic 4000 rows with tenure, charges, contract, internet, senior.
`customer_id` is not a feature. `future_collection_flag` is a planted
leak and is dropped. If you put it back, test AUC will jump; that is
the lesson, not a win.

## Method

1. Stratified 80/20 split (no dates in the toy set; on real data, split
   by signup or last-bill month instead).
2. ColumnTransformer: median impute + scale numerics, most-frequent +
   one-hot categoricals.
3. Baseline: logistic with class_weight=balanced.
4. Challenger: HistGradientBoosting, max_depth 4.
5. Winner by ROC-AUC on the held-out test set.
6. Threshold from precision-recall curve with recall >= 0.70.

## What I would do next on real data

- Time split and monthly backtest
- Slice F1 by contract type and city
- PSI on monthly_charges
- Cost matrix from the business, not a guessed 0.70 recall

## Spoken walkthrough (5 minutes)

Data grain, leaks refused, two models, threshold, API fields,
how I roll back (previous image + previous joblib).
