import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "ts": pd.date_range("2024-01-01", periods=100, freq="D"),
        "y": range(100),
    }
)
cut = df["ts"].quantile(0.8)
train, test = df[df["ts"] < cut], df[df["ts"] >= cut]
assert train["ts"].max() < test["ts"].min()
print("time split ok", len(train), len(test), train["ts"].max(), test["ts"].min())

tr, te = train_test_split(df, test_size=0.2, random_state=0)
overlap = not (tr["ts"].max() < te["ts"].min() or te["ts"].max() < tr["ts"].min())
print("shuffled ranges overlap?", overlap)
assert overlap
