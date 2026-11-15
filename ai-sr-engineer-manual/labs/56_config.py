import json
from dataclasses import asdict, dataclass


@dataclass
class TrainConfig:
    seed: int = 0
    test_size: float = 0.2
    C: float = 1.0
    class_weight: str | None = "balanced"
    max_iter: int = 1000


cfg = TrainConfig(C=0.5)
print(json.dumps(asdict(cfg), indent=2))
assert cfg.C == 0.5
