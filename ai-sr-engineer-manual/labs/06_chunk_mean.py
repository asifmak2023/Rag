from pathlib import Path

import numpy as np
import pandas as pd

path = Path(__file__).resolve().parent / "data" / "big.csv"
path.parent.mkdir(parents=True, exist_ok=True)
n = 50_000
rng = np.random.default_rng(0)
pd.DataFrame(
    {
        "id": np.arange(n),
        "x": rng.normal(size=n),
        "y": rng.integers(0, 2, size=n),
    }
).to_csv(path, index=False)

n_rows = 0
sx = 0.0
for chunk in pd.read_csv(path, chunksize=10_000):
    n_rows += len(chunk)
    sx += chunk["x"].sum()
print("mean x", sx / n_rows)
