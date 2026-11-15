import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame(
    {
        "age": [21, 35, None, 40, 29, 51, 33, 44, 26, 38],
        "city": ["KHI", "LHE", "KHI", None, "ISB", "KHI", "LHE", "KHI", "ISB", "LHE"],
        "income": [50, 80, 40, 120, 70, 90, 55, 110, 48, 88],
        "churn": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    }
)
num = ["age", "income"]
cat = ["city"]
pre = ColumnTransformer(
    [
        (
            "num",
            Pipeline(
                [
                    ("imp", SimpleImputer(strategy="median")),
                    ("sc", StandardScaler()),
                ]
            ),
            num,
        ),
        (
            "cat",
            Pipeline(
                [
                    ("imp", SimpleImputer(strategy="most_frequent")),
                    ("oh", OneHotEncoder(handle_unknown="ignore")),
                ]
            ),
            cat,
        ),
    ]
)
model = Pipeline(
    [
        ("pre", pre),
        ("clf", HistGradientBoostingClassifier(max_depth=3, random_state=0)),
    ]
)
model.fit(df[num + cat], df["churn"])
print("pred", model.predict(df[num + cat][:3]))
