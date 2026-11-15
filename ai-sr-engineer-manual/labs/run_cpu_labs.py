"""Run CPU labs that do not start a server.

From repo root or this folder:

    python labs/run_cpu_labs.py
"""

from __future__ import annotations

import runpy
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {
    "run_cpu_labs.py",
}
ORDER = [
    "01_numpy_warmup.py",
    "01_pandas_etl.py",
    "02_gd_linear.py",
    "02_softmax.py",
    "03_churn_baseline.py",
    "03_leakage.py",
    "03_column_transformer.py",
    "04_linear_torch.py",
    "04_mlp_tabular.py",
    "04_cnn.py",
    "06_chunk_mean.py",
    "06_sql_features.py",
    "07_f1_ci.py",
    "09_psi.py",
    "16_tfidf_tickets.py",
    "17_cnn_synthetic.py",
    "26_matlab_port.py",
    "27_search.py",
    "28_break_fix.py",
    "32_sql_windows.py",
    "33_lightgbm.py",
    "34_calibration.py",
    "41_naive_forecast.py",
    "42_ndcg.py",
    "43_batch_score.py",
    "44_mean_median.py",
    "48_versions.py",
    "49_onnx_sklearn.py",
    "51_imbalance.py",
    "52_eda.py",
    "56_config.py",
    "57_metrics_scratch.py",
    "61_group_split.py",
    "63_schema.py",
    "66_logloss.py",
    "67_missing.py",
    "68_clip.py",
    "69_onehot_unknown.py",
    "70_scale.py",
    "71_nb_svm.py",
    "72_pca.py",
    "73_kmeans.py",
    "74_sgd_vs_adam.py",
    "75_early_stop.py",
    "78_ce_weight.py",
    "81_roc_pr.py",
    "82_regression.py",
    "83_multiclass.py",
    "84_select.py",
    "86_shapes.py",
    "87_hashing.py",
    "88_cosine.py",
    "89_cost.py",
    "90_time_split.py",
    "91_dummy.py",
]


def main():
    failed = []
    for name in ORDER:
        path = ROOT / name
        if name in SKIP or not path.exists():
            print("SKIP", name)
            continue
        print("===", name, "===")
        try:
            runpy.run_path(str(path), run_name="__main__")
        except Exception:
            traceback.print_exc()
            failed.append(name)
    if failed:
        print("FAILED", failed)
        raise SystemExit(1)
    print("ALL OK", len(ORDER))


if __name__ == "__main__":
    main()
