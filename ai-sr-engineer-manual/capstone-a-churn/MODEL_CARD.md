# Model card (fill after you train)

Name: churn-gbdt-v1
Version: churn-gbdt-v1
Owner: you
Problem / decision it changes: who the retention team calls
Target definition: binary churn on synthetic accounts
Training window: synthetic, no dates; on real data list months
Data grain: one customer
Features: tenure, charges, contract, internet, senior, avg_charge_per_month
Leaks refused: customer_id, future_collection_flag
Model type: logistic vs HistGB, winner in metrics.json
Baseline it beat: majority class and unthresholded 0.5 logistic
Metric + value + CI: run `python -m src.evaluate` and paste
Operating threshold: recall floor 0.70 (see train.py)
Latency budget / measured: CPU tabular, well under 200 ms for one row
How to roll back: previous joblib + previous image
Known failure slices: synthetic; on real data slice by contract
What it must not be used for: automated account closure without appeal
