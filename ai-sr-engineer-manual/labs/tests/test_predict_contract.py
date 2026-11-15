import numpy as np
import pytest
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression


@pytest.fixture
def fitted_model():
    X, y = make_classification(n_samples=200, n_features=8, random_state=0)
    return LogisticRegression(max_iter=1000).fit(X, y)


def predict(model, x):
    if x.ndim != 2:
        raise ValueError("x must be 2d")
    if np.isnan(x).any():
        raise ValueError("nan")
    return model.predict(x)


def test_rejects_nan(fitted_model):
    x = np.zeros((1, fitted_model.n_features_in_))
    x[0, 0] = np.nan
    with pytest.raises(ValueError):
        predict(fitted_model, x)


def test_accepts_row(fitted_model):
    x = np.zeros((1, fitted_model.n_features_in_))
    out = predict(fitted_model, x)
    assert out.shape == (1,)
