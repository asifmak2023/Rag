# 80. Online evaluation: A/B, canary, interleaving

Offline AUC is a hypothesis. Users are the exam.

## A/B

Randomize users. Control = champion. Treatment = challenger. Primary
metric plus guardrails (latency, complaints, revenue). Precompute
sample size. Do not peek every hour and stop when you like it.

## Canary

Send 5-10% to the new model. Watch error rate and score distribution.
Ramp or roll back.

## Interleaving (ranking)

Show a mixed list from two rankers. More sample-efficient for search.
Name it if they do recsys.

## Pass / fail

You refuse to declare a winner from one weekend of cherry-picked AUC.
