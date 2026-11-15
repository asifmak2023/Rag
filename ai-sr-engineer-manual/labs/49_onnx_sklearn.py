from pathlib import Path

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=200, n_features=8, random_state=0)
pipe = Pipeline(
    [("sc", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))]
)
pipe.fit(X, y)
print("trained", pipe.n_features_in_)

try:
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType

    onx = convert_sklearn(
        pipe, initial_types=[("input", FloatTensorType([None, 8]))]
    )
    out = Path(__file__).resolve().parent / "data"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "logreg.onnx"
    path.write_bytes(onx.SerializeToString())
    print("wrote", path, "bytes", path.stat().st_size)
except Exception as exc:
    print("onnx skipped:", type(exc).__name__, exc)
