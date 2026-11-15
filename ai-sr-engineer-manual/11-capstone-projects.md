# 11. Capstone projects (this is your 4+ years story)

You cannot manufacture years. You can manufacture proof. Two complete
systems plus your MCS and MATLAB/C++/SQL background is how you walk into
Bahria Complex 1 without looking like a course graduate.

Each capstone must have:

- `README.md` (problem, data, metric, how to run)
- `src/` train, evaluate, serve
- `tests/` at least contract tests
- `Dockerfile`
- `report.md` (2 pages: method, plots, what you would do next)
- A 5-minute spoken walkthrough you rehearse standing up

Do not use a famous Kaggle notebook as-is. Use public data, your code.

## Capstone A. Tabular product model (weeks 13-14)

Business story (pick one and stick to it):

- Telco churn
- Credit default
- Hospital no-show
- Lead conversion

Requirements:

1. SQL or pandas feature table with point-in-time features
2. sklearn Pipeline, ColumnTransformer
3. Baseline logistic vs HistGradientBoosting or LightGBM
4. Imbalance handled on purpose
5. Threshold chosen from cost, not 0.5
6. FastAPI + Docker
7. metrics.json and two plots: PR curve, feature importance
8. A leakage section in the report: what you refused to use

Stretch: PSI drift script on a later time window.

This capstone maps to 80% of consulting AI work.

A complete runnable version lives in `capstone-a-churn/`. Run it, then
delete the parts you did not type yourself and rebuild them from
`report.md`. Shipping a folder you never understood is not a portfolio.

## Capstone B. Unstructured model (week 15)

Pick one:

- Image: defect vs ok, or digit-like toy if no GPU
- Text: ticket classification or spam/ham

Requirements:

1. PyTorch training loop you wrote
2. Train/val curves saved
3. Regularization you can explain
4. Export `state_dict` + a FastAPI that tokenizes or resizes
5. Compare against a dumb baseline (TF-IDF+linear for text, mean pixel
   logistic for images). If deep learning does not win, say so.

Stretch: one Keras clone of the same model (chapter 05).

Starter training loop: `capstone-b-images/`. Replace synthetic tensors
with real `ok/` and `defect/` folders before you claim CV experience.

## How to talk about "4+ years"

Never lie about dates. Say:

"I have a Master's in Computer Science and several years building
numerical and database software in C/C++ and MATLAB. I then completed a
production AI conversion: sklearn and PyTorch systems with APIs,
containers, tests, and monitoring. These two repositories are the
evidence. I can walk through the code."

If they need a calendar number you cannot honestly give, do not invent
it. Strength of proof beats a fake year count.

## Portfolio hygiene

- Public GitHub, English README, no notebooks as the only artifact
- Pin dependencies
- Sample `.env.example` with `USER_` placeholders, never real keys
- One screenshot of `/docs` from FastAPI

## Pass / fail

A competent engineer clones Capstone A, runs Docker, hits `/predict`,
and understands the report in 15 minutes. If they need you on a call to
run it, rewrite the README.
