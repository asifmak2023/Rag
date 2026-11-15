# 13. Sixteen-week schedule

Assume 25 to 30 focused hours per week. Labs first, reading second.

## Phase A. Convert the programmer (weeks 1-4)

| Week | Chapter | Outcome |
|---|---|---|
| 1 | 01 Python for AI | Write pandas/NumPy without thinking. No row loops. |
| 2 | 02 Math for ML | Whiteboard: gradient, Bayes, bias-variance, SVD sketch. |
| 3 | 03 sklearn part 1 | Classification pipeline, CV, leakage hunt on a CSV. |
| 4 | 03 sklearn part 2 + 33 | Regression, trees, HistGB/LightGBM, imbalance. |

Gate: complete `labs/01` through `labs/03`. If a self-check fails, repeat
the week. Do not start PyTorch weak on sklearn. Most business AI is tabular.

## Phase B. Deep learning (weeks 5-8)

| Week | Chapter | Outcome |
|---|---|---|
| 5 | 04 PyTorch tensors and autograd | Manual linear regression in torch. |
| 6 | 04 + 74 + 75 | CNN, Adam vs SGD talk, early stopping. |
| 7 | 04 transfer + 16 NLP + 17 CV | TF-IDF baseline, CNN loop, freeze-head talk. |
| 8 | 05 TensorFlow/Keras | Same CNN in Keras, SavedModel export. |

Gate: you can train, overfit on purpose, then regularize, in both frameworks.

## Phase C. Production (weeks 9-12)

| Week | Chapter | Outcome |
|---|---|---|
| 9 | 06 + 32 + 41 + 43 | Chunked ETL, SQL features, time split, batch scores. |
| 10 | 07 Evaluation and testing | Metrics, pytest on a model, security basics. |
| 11 | 08 Deploy | FastAPI + Docker + /predict + /health. |
| 12 | 09 + 10 | Logging, a drift alarm sketch, experiment writeup. |

Gate: one container that serves a real sklearn or torch model.

## Phase D. Look senior (weeks 13-16)

| Week | Chapter | Outcome |
|---|---|---|
| 13-14 | 11 + capstone-a-churn | Tabular product model, full pipeline, API, report. |
| 15 | 11 + capstone-b-images | Image model loop, then optional FastAPI wrap. |
| 16 | 12 + 18 + 19 | Salary, commute, 20 answers, 3 design talks. |

## Daily pattern (90 minutes minimum)

1. 10 min: recap yesterday's failure.
2. 60 min: lab, not tutorial watching.
3. 20 min: write 5 lines in `labs/notes.md`: what broke, what you changed.

## Weekend pattern

Saturday: finish the week's lab and self-check.
Sunday: one extra: either a Kaggle-scale CSV or a paper summary (chapter 10).

## If you only have 8 weeks

Do weeks 1-4, 5-6, 11, 13, 16. Skip TensorFlow until after an offer, but
read chapter 05 once so you can name Keras layers in an interview.

## Tracking

Copy this into `labs/progress.md` and tick it.

```
[ ] Week 1 Python
[ ] Week 2 Math
[ ] Week 3 sklearn class
[ ] Week 4 sklearn trees
[ ] Week 5 torch core
[ ] Week 6 CNN
[ ] Week 7 transfer
[ ] Week 8 TF
[ ] Week 9 data
[ ] Week 10 eval
[ ] Week 11 deploy
[ ] Week 12 mlops + research
[ ] Week 13-14 capstone A
[ ] Week 15 capstone B
[ ] Week 16 interview drills
```
