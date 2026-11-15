# 46. Errors you will see, and the one-line fix

Memorize the left column. The interview may paste a traceback.

| Error | Likely cause | Fix |
|---|---|---|
| `ValueError: Found input variables with inconsistent numbers of samples` | X and y length differ after dropna | Drop on a combined frame or reindex |
| `could not convert string to float` | City column in a numeric scaler | ColumnTransformer |
| `Expected 2D array, got 1D` | `predict([1,2,3])` | `reshape(1, -1)` |
| `X has 10 features, but model expects 12` | OneHot extra cats or missing col | Save whole Pipeline, schema check |
| `LinAlgError: Singular matrix` | collinear / rank deficient | drop cols, ridge, pinv |
| `loss is nan` | lr too big, log(0), overflow | lower lr, clip, check labels |
| `mat1 and mat2 shapes cannot be multiplied` | linear in_features wrong | print shape after flatten |
| `CUDA out of memory` | batch too big | smaller batch, CPU for this lab |
| `RuntimeError: ... requires_grad` | inplace ops on graph | remove `x +=`, use `x = x +` |
| `You must call model.eval()` symptoms | dropout on in serve | `eval()` + `no_grad()` |
| `pickle UnpicklingError` | sklearn version skew | pin versions, or ONNX |
| `pydantic ValidationError` | extra/missing JSON field | match schema, version API |
| `Address already in use` | port 8000 taken | other port |
| `SQL GROUP BY` row explosion | join before aggregate | aggregate events first |
| AUC = 1.0 | leak | hunt IDs, dates, target copies |

Lab: pick three, reproduce one of them on purpose in a scratch file,
then fix it. Write the traceback headline in `labs/notes.md`.
