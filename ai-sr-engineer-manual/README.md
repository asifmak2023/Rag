# Senior AI Engineer Hands-On Manual

Training path from MCS + MATLAB/C/C++/SQL to a production Sr. AI Engineer
who can pass an onsite interview at Pivotize Consulting and jobs like it.

## Who this is for

You already know:

- Programming (C, C++, MATLAB)
- Databases and SQL
- Computer science fundamentals

You do not yet have daily, muscle-memory practice in:

- Python data stack (NumPy, pandas, scikit-learn)
- PyTorch and TensorFlow as working tools, not slogans
- Training, evaluating, and shipping models
- Docker, APIs, and production monitoring

This manual closes that gap with labs you run, not notes you read.

## How to use this

1. Read `00-job-skill-map.md` once. It is the contract with the job posting.
2. Follow `13-16-week-schedule.md` in order. Do not skip labs.
3. Every chapter ends with a pass/fail self-check. Fail means repeat the lab.
4. After week 12, treat the two capstones as fake production tickets.
5. Use `12-interview-onsite.md` in the last 10 days before any interview.
6. If you are starting today, ignore the 16-week chart and do `23-first-seven-days.md`.

Work 3 to 4 hours a day on weekdays, 5 to 6 on weekends. That is a 16-week
full conversion. Compress to 8 weeks only if you can do 6+ hours daily.

## Folder map

```
ai-sr-engineer-manual/
  README.md
  00-job-skill-map.md
  01-python-for-ai.md
  02-math-for-ml.md
  03-sklearn-classical-ml.md
  04-pytorch-deep-learning.md
  05-tensorflow-keras.md
  06-data-engineering.md
  07-evaluation-testing.md
  08-deploy-docker-api.md
  09-mlops-monitoring.md
  10-research-experiments.md
  11-capstone-projects.md
  12-interview-onsite.md
  13-16-week-schedule.md
  14-onsite-cheatsheet.md
  15-adjacent-skills.md
  16-nlp-text.md
  17-computer-vision.md
  18-ml-system-design.md
  19-interview-answers.md
  20-daily-drills.md
  21-code-katas.md
  22-glossary.md
  23-first-seven-days.md
  24-algorithm-cards.md
  25-resume-and-talk.md
  26-matlab-to-python.md
  27-hyperparameter-tuning.md
  28-debugging-playbook.md
  29-fairness-and-product.md
  30-week16-mock-day.md
  31-first-90-days-onsite.md
  32-sql-feature-patterns.md
  33-gbdt-lightgbm.md
  34-calibration-explain.md
  35-git-for-ml.md
  36-linux-cli.md
  37-resources.md
  38-self-audit.md
  39-office-hours-script.md
  40-lab-checklist.md
  41-time-series.md
  42-ranking.md
  43-batch-scoring.md
  44-stats-for-engineers.md
  45-feature-store-lite.md
  46-errors-you-will-see.md
  47-karachi-onsite-logistics.md
  48-reproducibility.md
  49-onnx-export.md
  50-api-auth.md
  51-imbalanced-learning.md
  52-eda-plots.md
  53-unit-test-models.md
  54-logging-json.md
  55-model-card.md
  56-experiment-config.md
  57-metrics-from-scratch.md
  58-ensembles.md
  59-labeling.md
  60-transformers-honest.md
  61-cross-validation.md
  62-regularization-picture.md
  63-data-contracts.md
  64-profiling.md
  65-week-by-week-outcomes.md
  66-probability-calibration-talk.md
  67-missing-data.md
  68-outliers.md
  69-encoding.md
  70-scaling.md
  71-knn-nb-svm.md
  72-pca.md
  73-clustering.md
  74-optimizers.md
  75-schedules-earlystop.md
  76-vanishing-exploding.md
  77-init-seed-repro-torch.md
  78-class-weights-torch.md
  79-transfer-learning-talk.md
  80-ab-test-ml.md
  INDEX.md
  requirements.txt
  requirements-light.txt
  labs/
  capstone-a-churn/
  capstone-b-images/
```

## Setup (do this today)

```bash
python3 -m venv ~/ai-env
source ~/ai-env/bin/activate

pip install --upgrade pip
pip install -r ai-sr-engineer-manual/requirements.txt
```

Confirm:

```bash
python -c "import numpy, pandas, sklearn, torch, fastapi; print('ok')"
```

If `torch` install is slow, CPU is enough for every lab except the optional GPU notes.

## Rule of this manual

You are not done with a topic when you understand it.
You are done when you can do the self-check with the docs closed.
