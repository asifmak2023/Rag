# 96. SLOs and a one-page runbook

The posting says monitor and recommend improvements. Ops language:

- SLI: the number (p95 latency, error rate, daily F1 when labels land)
- SLO: the promise (p95 < 200 ms, 99% non-5xx)
- Error budget: how much you may miss the SLO this month
- Runbook: what a human does at 2am

## Runbook template (paste into the service README)

```
Symptom: /predict 5xx
1. curl /health and /ready
2. Check last deploy / model_version
3. Roll back to previous image if started after deploy
4. If schema errors, inspect payload samples (no PII in Slack)
5. If latency, check CPU and batch size; shed load

Symptom: scores all ~0.5 suddenly
1. Compare input means vs training (PSI)
2. Did upstream send empty strings as 0?
3. Do not retrain at 2am. Revert features or model first
```

## Pass / fail

You can recite rollback before retrain.
