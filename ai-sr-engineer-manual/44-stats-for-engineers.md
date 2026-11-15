# 44. Statistics you will actually use at a whiteboard

Not a full stats course. These five tools cover 90% of arguments.

## 1. Mean vs median

Outliers: salary, ticket time, claim size. Report median + p90, not
only the mean. Lab: print both on a lognormal sample.

## 2. Standard error and "is this lift real"

A/B: two conversion rates. You need n and a sense of noise.
Rule of thumb: difference much smaller than `sqrt(p(1-p)/n)` is noise.
Do not ship a model because one weekend looked good.

## 3. Confusion of correlation

Ice cream and drownings. In ML: a feature correlated with the target
that is not available at decision time, or is a proxy for a leak.

## 4. Power / sample size (qualitative)

Rare fraud at 0.3%: you will not estimate a 0.01 AUC lift on 2,000
rows. Ask for more history or a coarser target.

## 5. Multiple testing

You tried 40 features and 12 models. One "wins" at p < 0.05 by chance.
Pre-register the metric. Use a locked test set. Chapter 10 protocol.

## Lab 44. File: `labs/44_mean_median.py`

```python
import numpy as np
rng = np.random.default_rng(0)
x = rng.lognormal(mean=3, sigma=1.0, size=5000)
x[0:20] = x[0:20] * 40
print("mean", float(x.mean()), "median", float(np.median(x)), "p90", float(np.quantile(x, 0.9)))
```

Say: "I would not tell finance the mean claim is the typical claim."

## Bayes one-liner

Prior belief, data, posterior. MAP vs MLE. L2 as Gaussian prior.
Enough unless they are a research lab.

## Pass / fail

Given two F1s 0.61 vs 0.63 on n=400, you refuse to declare a winner
without a CI (chapter 07).
