# 18. ML system design (the onsite whiteboard)

Seniors are hired for this more than for knowing optimizer names.
Use the same skeleton every time. Eight minutes. Then stop.

## Skeleton

1. Goal and user. Who calls this, how often, what they do with the score.
2. Target definition. Positive class, time, exclusions.
3. Data. Sources, grain, labels, delay until label exists.
4. Split. Time vs random. Leakage list.
5. Metric and constraint. Quality + latency + cost + fairness.
6. Baseline. Rule or logistic. Then the upgrade.
7. Training. Pipeline, schedule, owners.
8. Serving. Batch vs online. API contract. SLA.
9. Monitor. Drift, slices, incidents.
10. Risks and "I would not".

## Pattern: online scoring (loan, churn at click)

- Features computed from a store keyed by customer_id
- Model service is stateless
- p95 latency budget from the product, not from you
- Cache features, not just model weights

## Pattern: batch scoring (nightly churn list)

- Spark/SQL/pandas job writes a table `scores_date`
- Product reads the table. No 5ms API needed
- Easier rollback: yesterday's table is still there

Say which one you would pick and why. Many "AI products" are batch.

## Three designs to rehearse

### A. Loan default (from chapter 12)

Already specified. Time split, GBDT, 200 ms, human review band.

### B. Factory camera defect

- Classification if cropped; detection if not
- Pretrained CNN, few hundred labeled images
- Edge vs server: if the line cannot go down, run on a small CPU/GPU
  box next to the camera; batch is useless here
- False negative cost (bad part ships) vs false positive (stops line)

### C. Support ticket router

- TF-IDF baseline, then embeddings if needed
- Human override on low confidence
- Languages: Karachi tickets may be mixed English / Urdu
- Latency 1s is fine; correctness and audit trail matter more

## Training-serving skew (say this unprompted)

"The code that builds features in training must be the same function
the API calls. I put that function in a shared module and unit test it.
I do not reimplement features in SQL for train and Python for serve
unless I have tests that lock them together."

## Capacity back-of-envelope

100 requests/sec * 5 ms CPU = 0.5 core. Logistic regression on 40
features does not need Kubernetes theater. A CNN on HD frames might.

Always do this arithmetic. It signals seniority.

## Pass / fail

Give talks A, B, C without notes. Record yourself. If you ramble past
10 minutes, cut the story, not the skeleton.
