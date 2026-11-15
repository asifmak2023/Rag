# 89. Cost-sensitive threshold (the business knob)

Predicted probability is not the decision. The threshold is.

Cost example: FN = 20, FP = 1. Expected cost at threshold t:

```
cost = fp(t)*1 + fn(t)*20
```

Pick t that minimizes cost on validation. Lock it. Do not retune on
test.

## Lab 89. File: `labs/89_cost.py`

Sweep thresholds 0.1..0.9. Print cost. Show 0.5 is not the minimum.

## Pass / fail

"I pick t from a cost matrix on val, then freeze it."
