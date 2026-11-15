from src.data import synthesize
from src.features import split_xy
from src.model import make_logistic


def test_logistic_fits_and_predicts():
    df = synthesize(n=400, seed=1)
    X, y, feats = split_xy(df)
    num_cols = [c for c in feats if c not in ("contract", "internet")]
    model = make_logistic(num_cols)
    model.fit(X, y)
    proba = model.predict_proba(X[:3])[:, 1]
    assert proba.shape == (3,)
    assert (proba >= 0).all() and (proba <= 1).all()
