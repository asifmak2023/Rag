# 20. Daily 45-minute drills (muscle memory)

Do one drill a day after week 4. Timer on. Docs closed unless stuck
for 10 minutes.

## Drill set A. Python / data (10 days)

A1. Standardize a matrix with broadcasting. No loops.
A2. pandas groupby + rolling 7-day sum. Time index required.
A3. Join two tables without duplicating grain. Assert row count.
A4. Fill nulls by group median. Keep a missing flag column.
A5. Downcast dtypes, print memory before/after.
A6. Chunk a CSV, compute mean and variance one pass.
A7. Detect duplicate IDs. Keep latest by timestamp.
A8. Target-encode a category with CV (or skip and use OneHot).
A9. Write `profile(df)` from chapter 06 from memory.
A10. SQL in SQLite: 30-day aggregates point-in-time.

## Drill set B. sklearn (10 days)

B1. Pipeline + ColumnTransformer on mixed types.
B2. Stratified split + F1 vs accuracy on 10% positives.
B3. HistGradientBoosting vs logistic, same split, table of two metrics.
B4. Calibration curve sketch (plot or print buckets).
B5. Leakage: add y to X, watch AUC, remove it.
B6. Threshold sweep for recall >= 0.8.
B7. joblib dump/load, predict one row.
B8. Time split on a date column.
B9. Feature importance from a tree, 5-line story.
B10. Cross_val_score with a scorer you name, not default accuracy.

## Drill set C. PyTorch (10 days)

C1. Tensor 2x2, `requires_grad`, backward, print grad.
C2. Linear regression loop, 50 lines max.
C3. `nn.Module` MLP, DataLoader, 5 epochs.
C4. Forget `zero_grad` on purpose, write what you saw.
C5. CNN forward on `(8,1,28,28)`, print shapes after each layer.
C6. Save/load state_dict in a new process.
C7. `train()` vs `eval()` with Dropout, two mean outputs.
C8. Class-weighted CrossEntropyLoss.
C9. Clip grad norm, explain exploding grads.
C10. Freeze all but last layer (`requires_grad=False`).

## Drill set D. Production (10 days)

D1. FastAPI /predict with Pydantic, 15 minutes.
D2. Reject NaN and wrong length with 400.
D3. /health and /ready.
D4. Dockerfile for the sklearn service.
D5. Log latency_ms.
D6. pytest on the feature function.
D7. Champion vs challenger: two joblib files, pick by metrics.json.
D8. PSI on one feature.
D9. Draw the bank design skeleton on paper, 8 minutes.
D10. Explain pickle risk and ONNX in 90 seconds.

## Scoring

0: looked at notes the whole time.
1: finished with notes.
2: finished closed-book.
A week of 2s on a set means that set is done.

Track in `labs/drill-log.md`.
