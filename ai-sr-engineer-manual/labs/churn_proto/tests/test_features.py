import pandas as pd

from src.features import add_amount_z


def test_amount_z_zero_mean():
    df = pd.DataFrame({"amount": [1.0, 2.0, 3.0]})
    out = add_amount_z(df)
    assert abs(out["amount_z"].mean()) < 1e-12
    assert abs(out["amount_z"].std(ddof=0) - 1.0) < 1e-12
