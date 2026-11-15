from pathlib import Path

import numpy as np
import pandas as pd

path = Path(__file__).resolve().parent / "data"
path.mkdir(parents=True, exist_ok=True)
df = pd.DataFrame(
    {
        "id": np.arange(20_000),
        "x": np.random.default_rng(0).normal(size=20_000),
        "city": np.random.default_rng(1).choice(["KHI", "LHE", "ISB"], size=20_000),
    }
)
csv_p = path / "toy.csv"
df.to_csv(csv_p, index=False)
print("csv_bytes", csv_p.stat().st_size)
try:
    parq = path / "toy.parquet"
    df.to_parquet(parq, index=False)
    print("parquet_bytes", parq.stat().st_size)
    back = pd.read_parquet(parq)
    assert len(back) == len(df)
except Exception as exc:
    print("parquet skipped:", type(exc).__name__, exc)
