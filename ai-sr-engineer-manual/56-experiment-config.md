# 56. Config files, not mystery kwargs

Seniors do not hide hyperparameters in a cell. They live in YAML or a
dataclass that is logged with the run.

## Lab 56. File: `labs/56_config.py`

```python
from dataclasses import asdict, dataclass
import json

@dataclass
class TrainConfig:
    seed: int = 0
    test_size: float = 0.2
    C: float = 1.0
    class_weight: str | None = "balanced"
    max_iter: int = 1000

cfg = TrainConfig(C=0.5)
print(json.dumps(asdict(cfg), indent=2))
```

Train reads `cfg`. `metrics.json` stores `asdict(cfg)` plus git hash.
That is MLflow without MLflow.

YAML optional:

```yaml
seed: 0
C: 0.5
class_weight: balanced
```

`yaml.safe_load`, never `load`. Interview: "I do not execute config."

## Pass / fail

You can point at one object that fully specifies a run. If reproducing
requires remembering a UI click, fail.
