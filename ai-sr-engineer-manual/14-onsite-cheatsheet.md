# 14. One-page onsite cheatsheet (print this)

## Role

Sr. AI Engineer, Pivotize Consulting, Karachi, onsite only.
Bahria Complex 1, Lalazar, M.T. Khan Road.
Pay from Rs 250,000. Full-time. No remote.

## Your story (30 seconds)

MCS. Years of C/C++, MATLAB, SQL. Converted that numerical and database
discipline into Python ML: sklearn pipelines, PyTorch training loops,
FastAPI + Docker, tests, monitoring. Two shipped-style capstones. I work
in the office.

## Default technical answers

- Tabular first: logistic baseline, then GBDT. Neural nets if images/text
  or huge nonlinear structure.
- Split by time if events have time. Else stratified.
- Metric from cost, not accuracy. Imbalance: PR-AUC, class_weight,
  threshold from precision/recall, not SMOTE first.
- Leakage: IDs, future dates, target in features, preprocess before split.
- Production: one Pipeline artifact, /health /ready /predict, versioned
  image, p95 latency, schema validation, no pickle from the network.
- Drift: watch input PSI and score distribution. Retrain on a schedule
  with champion/challenger.
- PyTorch loop: train(), zero_grad, backward, step; eval() + no_grad.
- Keras: Sequential or functional, callbacks, SavedModel.
- L1 sparse, L2 small weights. Dropout train only.
- Attention: queries, keys, values; weighted sum of values.

## Numbers to fill before you leave home

Current salary:
Expected salary:
Notice:
Join date:
Commute: yes, onsite, not remote.

## Demo order if they open a laptop

1. `docker run` capstone A
2. `curl /predict`
3. Open `report.md` plots
4. Show the training script, not a notebook

## Do not say

- "I would just use GPT" as the first design
- "Accuracy was 99%" on an imbalanced problem
- "I cannot work onsite"
- Fake years of PyTorch
