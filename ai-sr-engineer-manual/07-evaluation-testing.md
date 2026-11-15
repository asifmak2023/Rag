# 07. Testing and evaluation (performance, reliability, security)

The posting asks you to test AI systems against performance, reliability,
and security. Notebooks that print accuracy are not that.

## Performance (model quality)

Pick the metric from the business cost.

| Situation | Metric |
|---|---|
| Balanced 2-class | ROC-AUC, F1, log loss |
| Rare fraud / churn | PR-AUC, recall at precision P |
| Multiclass | macro-F1 if classes equal, weighted if not |
| Regression | MAE (money), RMSE (large errors matter), MAPE if scale-free |
| Ranking | NDCG, recall@k |

Always report:

- Point estimate on a held-out set that was not used to tune
- A simple baseline (mean, last week, majority class, linear model)
- Slice metrics: by city, by month, by customer tenure

Lab 07A. Bootstrap a confidence interval on F1:

```python
import numpy as np
from sklearn.metrics import f1_score

def f1_ci(y, pred, n=200, seed=0):
    rng = np.random.default_rng(seed)
    y, pred = np.asarray(y), np.asarray(pred)
    stats = []
    for _ in range(n):
        idx = rng.integers(0, len(y), len(y))
        stats.append(f1_score(y[idx], pred[idx], zero_division=0))
    lo, hi = np.percentile(stats, [2.5, 97.5])
    return float(np.mean(stats)), float(lo), float(hi)
```

If two models overlap in CI, you do not get to claim a winner.

## Reliability (the system, not the AUC)

A model that is 0.02 F1 better and times out is a worse product.

Check:

- Latency p50 / p95 of `/predict`
- Throughput at a fixed batch size
- Behavior on empty input, NaN, extra columns, missing columns
- Determinism: same input, same output (watch dropout at train vs eval)
- Rollback: previous `model.joblib` still loadable

Lab 07B. Contract tests with pytest:

File: `labs/tests/test_predict_contract.py`

```python
import numpy as np
import pytest

def predict(model, x):
    if x.ndim != 2:
        raise ValueError("x must be 2d")
    if np.isnan(x).any():
        raise ValueError("nan")
    return model.predict(x)

def test_rejects_nan(fitted_model):
    x = np.zeros((1, fitted_model.n_features_in_))
    x[0, 0] = np.nan
    with pytest.raises(ValueError):
        predict(fitted_model, x)
```

## Security (enough to not be naive)

You are not a pentester. You are an engineer who does not ship an open
model API that executes strings.

Rules:

- Never `eval` user input. Never `pickle.loads` from the network.
- Authenticate `/predict` if it is not public. API key header is enough
  for internal services.
- Validate schema with Pydantic. Reject extra fields or huge payloads.
- Do not return raw training data or other users' records.
- Rate limit. A model endpoint is a CPU/GPU budget.
- PII: do not log raw CNICs, phone numbers, full names in plaintext.
- Model files are code. Treat `joblib` / pickle as untrusted unless you
  produced them.

Lab 07C. Pydantic schema:

```python
from pydantic import BaseModel, Field, conlist

class PredictIn(BaseModel):
    features: conlist(float, min_length=16, max_length=16)
    request_id: str = Field(min_length=1, max_length=64)
```

## Experiment hygiene

- Seed everything you can (`numpy`, `torch`, `random`)
- Log git commit + data hash + hyperparameters
- One change per experiment when you are debugging

## Pass / fail

You have a script that:

1. Trains
2. Writes metrics.json with baseline + model + CI
3. Runs pytest on input validation
4. Fails CI if F1 drops more than 5% vs last artifact

That is "thorough testing" in the language of this job.
