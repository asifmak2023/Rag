import numpy as np
import pandas as pd

df = pd.DataFrame({
    "user_id": [1, 1, 2, 2, 3, None],
    "ts": pd.to_datetime([
        "2024-01-01", "2024-01-03", "2024-01-01",
        "2024-01-02", "2024-01-05", "2024-01-06",
    ]),
    "amount": [10, 40, 5, np.nan, 100, 20],
    "city": ["KHI", "khi", "LHE", "LHE", None, "ISB"],
})

df = df.copy()
df["city"] = df["city"].str.upper().fillna("UNKNOWN")
df["user_id"] = df["user_id"].astype("Int64")
df["amount"] = df["amount"].fillna(df.groupby("city")["amount"].transform("median"))

feat = (
    df.sort_values("ts")
    .groupby("user_id", dropna=False)
    .agg(
        n=("amount", "size"),
        sum_amount=("amount", "sum"),
        last_ts=("ts", "max"),
    )
    .reset_index()
)
print(feat)
