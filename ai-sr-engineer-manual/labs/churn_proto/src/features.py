def add_amount_z(df):
    mu = df["amount"].mean()
    sd = df["amount"].std(ddof=0) or 1.0
    out = df.copy()
    out["amount_z"] = (out["amount"] - mu) / sd
    return out
