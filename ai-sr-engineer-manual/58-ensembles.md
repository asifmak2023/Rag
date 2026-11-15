# 58. Ensembles: bagging, boosting, stacking (short)

You already use boosting (chapter 33). Know the family so you do not
mix words.

## Bagging (random forest)

Train trees on bootstrap samples. Average votes. Reduces variance.
Parallel.

## Boosting (GBDT)

Trees in sequence, each fixes residuals. Reduces bias. Sequential.
Usually stronger on tabular.

## Stacking

Level-0 models (logistic, GBDT, linear SVM). Level-1 learns to blend
their scores. Easy to leak if the blender sees the same rows the
base models trained on. Use out-of-fold predictions.

## Voting

Hard (labels) or soft (probabilities). Cheap. Try after two strong
singles. Diminishing returns.

## Interview

"I ensemble when a single GBDT plateaus and the extra latency is free.
I do not stack five deep nets on 3k rows."

## Pass / fail

Define bagging vs boosting in two sentences. Mention out-of-fold for
stacking.
