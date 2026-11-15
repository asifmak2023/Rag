from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .features import CAT_COLS


def _preprocess(num_cols):
    return ColumnTransformer(
        [
            (
                "num",
                Pipeline(
                    [
                        ("imp", SimpleImputer(strategy="median")),
                        ("sc", StandardScaler()),
                    ]
                ),
                num_cols,
            ),
            (
                "cat",
                Pipeline(
                    [
                        ("imp", SimpleImputer(strategy="most_frequent")),
                        ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                    ]
                ),
                CAT_COLS,
            ),
        ]
    )


def make_logistic(num_cols):
    return Pipeline(
        [
            ("pre", _preprocess(num_cols)),
            (
                "clf",
                LogisticRegression(max_iter=1000, class_weight="balanced"),
            ),
        ]
    )


def make_gbdt(num_cols):
    return Pipeline(
        [
            ("pre", _preprocess(num_cols)),
            (
                "clf",
                HistGradientBoostingClassifier(
                    max_depth=4,
                    learning_rate=0.08,
                    max_iter=120,
                    random_state=0,
                ),
            ),
        ]
    )
