# 24. Algorithm cards (one minute each)

If you cannot fill the blanks from memory, you do not know the algorithm.

## Logistic regression

Predicts P(y=1|x) with sigmoid(w·x+b). Loss: log loss. Linear decision
boundary. Fast, calibrated-ish, great baseline. Fails on XOR-style
interactions unless you add features.

## Linear / ridge / lasso regression

Predict a number. MSE. Ridge = L2 on w. Lasso = L1. Use when the
product wants an interpretable dollars-ish score.

## SVM

Max-margin classifier. Kernel SVM (RBF) only for small n. Linear SVM
on TF-IDF is a classic text model. Slow to train at huge n. Does not
give probabilities unless you calibrate.

## Decision tree

Recursive splits. Interpretable. Overfits if deep. The atom of GBDT
and random forest.

## Random forest

Bagged trees, random feature subset per split. Strong, fewer knobs
than boosting. Slower to score than a shallow GBDT.

## Gradient boosting / HistGB / LightGBM / XGBoost

Trees added to fix residuals. Default king of tabular. Tune depth,
learning rate, leaves, min child. Watch leakage; trees will exploit it.

## kNN

Predict from k nearest train rows. No training. Predict is O(n d).
Dies at scale. Good teaching model, rare in production.

## Naive Bayes

Features independent given y. Fast, surprisingly good for text counts.
The independence assumption is false and often good enough.

## k-means

Cluster by nearest centroid, iterate. You pick k. Scale features
first. Not a classifier. Use to explore, then look at the clusters.

## PCA / SVD

Linear compression. Variance directions. Visualize, denoise, sometimes
speed up. Not magic feature engineering.

## MLP (feedforward net)

Linear, activation, repeat. Universal approximator, data hungry,
needs scaling, easy to overfit.

## CNN

Shared local filters. Images, some 1D signals. Pool to shrink.

## RNN / LSTM

Sequence in a loop. Mostly replaced by transformers for language.
Still a valid answer for short sensor sequences.

## Transformer

Attention instead of a loop. Pretrained (BERT, GPT). You fine-tune or
embed. You do not train from scratch on a consulting timeline.

## How to choose in 20 seconds

```
tabular, n < 10M          -> GBDT, logistic baseline first
text, labeled, n < 100k   -> TF-IDF + linear, then embeddings
images                    -> pretrained CNN head
sequences / language      -> pretrained transformer
need explanations Friday  -> linear or shallow tree
n = 500                   -> not a deep net
```
