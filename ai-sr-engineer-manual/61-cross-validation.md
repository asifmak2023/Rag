# 61. Cross-validation, nested, grouped, time

`cross_val_score` is not a personality. Wrong CV is leakage with extra
steps.

## Standard k-fold

Shuffle, k=5, stratified if classification. OK when rows are i.i.d.

## Grouped

Many rows per customer. Split by `customer_id`, not by row.
`GroupKFold`. Otherwise the same user is in train and test.

## Time

Chapter 41. Expanding window or cutoff. No shuffle.

## Nested

Outer loop: estimate generalization. Inner loop: tune C / depth.
If you tune on the same CV you report, the number is optimistic.
For consulting v1: hold out a test set, CV only on train. Nested if
someone will audit the paper.

## Leak through preprocessing

Any fit that sees the test fold (scaler, target encode, feature
select) must live inside the Pipeline so CV refits it.

## Pass / fail

You name the CV that matches the grain of the data, unprompted.
