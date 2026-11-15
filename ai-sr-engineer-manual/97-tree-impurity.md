# 97. Gini and entropy (why trees split)

A split is good if child nodes are purer than the parent.

Entropy: `-sum p log2 p`. 0 if all one class. 1 bit if 50/50 binary.
Information gain: entropy(parent) - weighted entropy(children).

Gini: `1 - sum p^2`. Same job, slightly different curve. sklearn
trees default Gini.

## Lab 97. File: `labs/97_gini.py`

Compute gini and entropy for p=0, 0.5, 1. Assert max at 0.5.

## Interview

"Trees greedily pick the split with the best impurity drop. That is
why a leak column gets used first."

## Pass / fail

Gini formula and "pure = 0" without notes.
