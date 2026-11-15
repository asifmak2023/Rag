# 91. Dummy baselines (always first)

If you cannot beat:

- classification: most_frequent or stratified dummy
- regression: mean or median dummy
- forecast: seasonal naive (chapter 41)

you do not have a model. You have a ritual.

## Lab 91. File: `labs/91_dummy.py`

DummyClassifier most_frequent vs logistic on 10% positives. Dummy
accuracy looks high. Dummy F1 is ~0. Logistic F1 should be better.

## Pass / fail

Every capstone README lists the dummy number next to the model number.
