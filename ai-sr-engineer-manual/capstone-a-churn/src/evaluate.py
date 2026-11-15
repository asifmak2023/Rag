import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split

from .data import load_or_build
from .features import split_xy

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts"


def f1_ci(y, pred, n=200, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    pred = np.asarray(pred)
    stats = []
    for _ in range(n):
        idx = rng.integers(0, len(y), len(y))
        stats.append(f1_score(y[idx], pred[idx], zero_division=0))
    lo, hi = np.percentile(stats, [2.5, 97.5])
    return float(np.mean(stats)), float(lo), float(hi)


def main():
    bundle = joblib.load(ART / "model.joblib")
    model, threshold = bundle["model"], bundle["threshold"]
    df = load_or_build()
    X, y, _ = split_xy(df)
    _, Xte, _, yte = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=0
    )
    proba = model.predict_proba(Xte)[:, 1]
    pred = (proba >= threshold).astype(int)
    mean, lo, hi = f1_ci(yte, pred)
    print(classification_report(yte, pred))
    print("f1 ci", mean, lo, hi)
    extra = {"f1_mean": mean, "f1_ci_lo": lo, "f1_ci_hi": hi}
    metrics_path = ART / "metrics.json"
    metrics = json.loads(metrics_path.read_text())
    metrics.update(extra)
    metrics_path.write_text(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
