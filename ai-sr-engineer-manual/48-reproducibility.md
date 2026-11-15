# 48. Reproducibility (same script, same number)

If you cannot rerun last week's score, you do not have a system. You
have a moment.

## Seed everything

```python
import os, random
import numpy as np

def seed_all(s=0):
    random.seed(s)
    np.random.seed(s)
    os.environ["PYTHONHASHSEED"] = str(s)
    try:
        import torch
        torch.manual_seed(s)
        torch.use_deterministic_algorithms(False)
    except Exception:
        pass
```

Deterministic CUDA is a bonus, not required for this job. CPU sklearn
plus a seed is enough to look adult.

## What to record in metrics.json

- git commit hash
- data file name + row count + `y.mean()`
- package versions (`sklearn.__version__`)
- seed
- command that trained

Lab 48. File: `labs/48_versions.py`

```python
import sklearn, numpy, pandas
print("sklearn", sklearn.__version__)
print("numpy", numpy.__version__)
print("pandas", pandas.__version__)
```

Capstone A already writes metrics. Add versions there when you touch it.

## Pin installs

`requirements.txt` with lower bounds is a start. For a real service,
pin `==` after it works. Do not upgrade sklearn on the server the same
day you pickle a Pipeline.

## Pass / fail

Train twice with the same seed. Coefficients or val AUC match. If they
do not, you have shuffle or data-order bugs.
