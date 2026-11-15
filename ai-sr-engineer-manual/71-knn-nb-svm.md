# 71. kNN, Naive Bayes, SVM (the rest of "classical ML")

The posting said algorithms. You already have linear and trees. These
three still appear in interviews.

## kNN

Store the data. Predict by vote of k nearest. Scale features. Dies at
large n. Curse of dimensionality. Good for a "lazy learner" question.

## Naive Bayes

Assume features independent given class. Fast, surprisingly strong on
word counts. GaussianNB on numeric, MultinomialNB on counts.

## SVM

Max-margin. LinearSVC on high-d text. RBF SVC only for small n.
`C` = penalty for violating the margin. No native probabilities
without calibration.

## Lab 71. File: `labs/71_nb_svm.py`

Compare Logistic, GaussianNB, LinearSVC on the same synthetic data.
Print F1. Talk, do not crown a universal winner.

## Pass / fail

Complexity of kNN predict: O(n d) naive. Why ANN exists (chapter 21).
