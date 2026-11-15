import math

val = [1.0, 0.7, 0.5, 0.42, 0.40, 0.41, 0.43, 0.48, 0.55]
best, best_ep, wait, patience = math.inf, 0, 0, 3
stopped = None
for ep, v in enumerate(val):
    if v < best - 1e-6:
        best, best_ep, wait = v, ep, 0
    else:
        wait += 1
        if wait >= patience:
            stopped = ep
            break
print("best_epoch", best_ep, "best_val", best, "stopped_at", stopped)
assert best_ep == 4
assert stopped == 7
