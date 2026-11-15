# 99. Brier score (one number for calibration + accuracy)

Brier = mean (p - y)^2 for binary y. 0 is perfect. Always predicting
the base rate is the dummy. Lower is better.

It punishes both "wrong" and "overconfident". Complements log loss
(chapter 66) and reliability diagrams (chapter 34).

## Lab 99. File: `labs/99_brier.py`

Dummy constant base-rate vs logistic. Print Brier both. Model should
win if it learned anything.

## Interview

"If the call center treats 0.8 as 80%, I report Brier and a reliability
table, not only AUC."

## Pass / fail

Brier formula from memory. Dummy baseline named.
