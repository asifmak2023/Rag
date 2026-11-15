import pandas as pd

from src.features import add_ratio_features, drop_leaks


def test_ratio():
    df = pd.DataFrame(
        {
            "tenure_months": [10, 0],
            "total_charges": [100.0, 50.0],
            "monthly_charges": [10.0, 10.0],
        }
    )
    out = add_ratio_features(df)
    assert out["avg_charge_per_month"].iloc[0] == 10.0
    assert out["avg_charge_per_month"].iloc[1] == 50.0


def test_drops_leak():
    df = pd.DataFrame({"future_collection_flag": [1], "churn": [1]})
    out = drop_leaks(df)
    assert "future_collection_flag" not in out.columns
