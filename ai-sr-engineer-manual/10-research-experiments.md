# 10. Research and experiments without becoming a PhD student

The posting wants research, experiments, and staying current. In a
consulting shop that means: beat a baseline, write what you tried, read
one paper a week, do not chase every new model.

## Experiment protocol (use this forever)

1. Write the question in one sentence. "Does class_weight='balanced'
   raise recall on churn without killing precision below 0.4?"
2. Freeze data and split.
3. Baseline first. Always.
4. Change one thing.
5. Record: git hash, seed, params, metrics, notes.
6. Decide: ship, iterate, or stop.

File: `labs/experiments/exp_001.md`

```
question:
baseline:
change:
data:
metrics:
decision:
```

If you cannot fill that, you did not run an experiment. You played.

## Lab 10A. Ablation table

Train four models on the same split:

| id | model | extra | val F1 | test F1 | p95 ms |
|---|---|---|---|---|---|
| b0 | logistic | none | | | |
| b1 | logistic | class_weight | | | |
| t0 | hist GBDT | depth 3 | | | |
| t1 | hist GBDT | depth 6 | | | |

Only t1 ships if it wins on test and stays under the latency budget.

## How to read a paper in 30 minutes

Source: arXiv cs.LG, PyTorch blog, sklearn release notes, not Twitter.

Template (`labs/papers/YYYY-MM-DD.md`):

```
title:
year:
problem in one line:
method in three lines:
why it might matter for our stack:
what I will try:
what I will ignore:
```

Read 16 papers in 16 weeks. That is "stay up to date".

Start list (read in this order):

1. A Gentle Introduction to Gradient Boosting (any solid blog + Friedman)
2. ImageNet classification with deep CNNs (AlexNet) — history
3. Attention Is All You Need — enough to explain self-attention
4. BERT — pretrained transformers
5. Adam optimizer paper abstract + the bias-correction idea
6. Batch Normalization
7. Dropout
8. A survey of ML system production failures (Google/hidden technical debt)

You do not implement transformers from scratch for this job. You explain
them and call a library.

## When research is the wrong move

- n = 800 rows: do not fine-tune an LLM
- The product needs a rule + a linear model on Friday
- You cannot get labels

A senior says no. Practice saying no in writing.

## Lab 10B. Reproduce a number

Pick your chapter 03 model. Retrain with a different seed five times.
Report mean and std of F1. If std is 0.04, a 0.01 "improvement" is noise.

## Pass / fail

You have a folder of experiment notes and one paper note per week.
Empty notebooks do not count.
