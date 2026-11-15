# 49. ONNX (when Java or a non-Python service must score)

The posting lists Java. You will not rewrite GBDT in Java. You export.

## Idea

Train in sklearn or PyTorch. Export ONNX. Score with ONNX Runtime in
Python, C++, or Java. Same math, no pickle, no Python on the hot path
if they refuse Python.

## Lab 49. sklearn to ONNX

File: `labs/49_onnx_sklearn.py`

Needs `onnx` and `skl2onnx` (in the full `requirements.txt`).

If import fails, print skipped. Still explain the interview sentence.

```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=200, n_features=8, random_state=0)
pipe = Pipeline([("sc", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))])
pipe.fit(X, y)
```

Export sketch:

```python
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
onx = convert_sklearn(pipe, initial_types=[("input", FloatTensorType([None, 8]))])
open("labs/data/logreg.onnx", "wb").write(onx.SerializeToString())
```

PyTorch: `torch.onnx.export(model, dummy, "m.onnx", ...)` with a frozen
`eval()` model and a dummy batch of the right shape.

## When not to use ONNX

- Tiny internal FastAPI in Python: joblib is fine
- Custom Python ops that will not convert
- You have not trained a model yet

## Interview

"If the core is Java, I export ONNX and keep training in Python. I do
not pickle across languages. I still version the file and schema."

## Pass / fail

Say pickle vs state_dict vs ONNX without mixing them up (chapter 19 Q13).
