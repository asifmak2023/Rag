import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import f1_score, precision_recall_curve, roc_auc_score
from sklearn.model_selection import train_test_split

from . import MODEL_VERSION
from .data import load_or_build
from .features import split_xy
from .model import make_gbdt, make_logistic

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts"


def pick_threshold(y_true, proba, min_recall=0.70):
    p, r, t = precision_recall_curve(y_true, proba)
    t = np.append(t, 1.0)
    ok = np.where(r >= min_recall)[0]
    if len(ok) == 0:
        return 0.5
    i = ok[np.argmax(p[ok])]
    return float(t[i])


def main():
    ART.mkdir(parents=True, exist_ok=True)
    df = load_or_build()
    X, y, feats = split_xy(df)
    num_cols = [c for c in feats if c not in ("contract", "internet")]
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=0
    )

    models = {
        "logistic": make_logistic(num_cols),
        "gbdt": make_gbdt(num_cols),
    }
    rows = []
    for name, est in models.items():
        est.fit(Xtr, ytr)
        proba = est.predict_proba(Xte)[:, 1]
        rows.append(
            {
                "name": name,
                "roc_auc": float(roc_auc_score(yte, proba)),
                "f1_at_05": float(f1_score(yte, (proba >= 0.5).astype(int))),
            }
        )

    winner_name = max(rows, key=lambda r: r["roc_auc"])["name"]
    winner = models[winner_name]
    proba = winner.predict_proba(Xte)[:, 1]
    threshold = pick_threshold(yte.to_numpy(), proba)
    pred = (proba >= threshold).astype(int)
    metrics = {
        "model_version": MODEL_VERSION,
        "winner": winner_name,
        "threshold": threshold,
        "test_roc_auc": float(roc_auc_score(yte, proba)),
        "test_f1": float(f1_score(yte, pred)),
        "candidates": rows,
        "features": feats,
        "n_train": int(len(Xtr)),
        "n_test": int(len(Xte)),
        "churn_rate": float(y.mean()),
        "leaks_refused": ["customer_id", "future_collection_flag"],
    }
    joblib.dump(
        {"model": winner, "threshold": threshold, "features": feats},
        ART / "model.joblib",
    )
    (ART / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
