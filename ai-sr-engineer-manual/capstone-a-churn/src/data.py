from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "churn.csv"


def synthesize(n=4000, seed=0):
    rng = np.random.default_rng(seed)
    tenure = rng.integers(1, 73, size=n)
    monthly = rng.normal(70, 25, size=n).clip(20, 140)
    contract = rng.choice(
        ["month-to-month", "one-year", "two-year"],
        size=n,
        p=[0.55, 0.25, 0.20],
    )
    internet = rng.choice(["fiber", "dsl", "none"], size=n, p=[0.45, 0.35, 0.20])
    senior = rng.integers(0, 2, size=n)
    total = monthly * tenure * rng.uniform(0.7, 1.1, size=n)

    logit = (
        -1.6
        + 0.035 * (monthly - 70)
        - 0.04 * tenure
        + 0.9 * (contract == "month-to-month")
        + 0.45 * (internet == "fiber")
        + 0.35 * senior
        + rng.normal(0, 0.4, size=n)
    )
    p = 1 / (1 + np.exp(-logit))
    churn = (rng.uniform(size=n) < p).astype(int)

    df = pd.DataFrame(
        {
            "customer_id": np.arange(n),
            "tenure_months": tenure,
            "monthly_charges": monthly.round(2),
            "total_charges": total.round(2),
            "contract": contract,
            "internet": internet,
            "senior": senior,
            "churn": churn,
        }
    )
    leak = rng.normal(size=n)
    df["future_collection_flag"] = (churn + (leak > 1.8).astype(int)).clip(0, 1)
    return df


def load_or_build():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)
    df = synthesize()
    df.to_csv(DATA_PATH, index=False)
    return df
