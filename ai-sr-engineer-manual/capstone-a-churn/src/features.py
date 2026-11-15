NUM_COLS = ["tenure_months", "monthly_charges", "total_charges", "senior"]
CAT_COLS = ["contract", "internet"]
TARGET = "churn"
ID_COL = "customer_id"
LEAK_COLS = ["future_collection_flag"]
FEATURE_COLS = NUM_COLS + CAT_COLS


def add_ratio_features(df):
    out = df.copy()
    tenure = out["tenure_months"].replace(0, 1)
    out["avg_charge_per_month"] = out["total_charges"] / tenure
    return out


def drop_leaks(df):
    cols = [c for c in LEAK_COLS if c in df.columns]
    return df.drop(columns=cols)


def split_xy(df):
    work = drop_leaks(add_ratio_features(df))
    extra = ["avg_charge_per_month"]
    feats = FEATURE_COLS + extra
    return work[feats], work[TARGET], feats
