# 108. n_jobs and cores (do not melt the office laptop)

`n_jobs=-1` in GridSearchCV uses all cores. Fine at home. Rude on a
shared VM. Prefer `n_jobs=2` or 4 unless you own the box.

BLAS already parallelizes some numpy. Nested parallelism (sklearn
n_jobs and MKL) can be slower. If a job hangs the machine, set
`OMP_NUM_THREADS=1` and sklearn `n_jobs=1` to debug.

## Pass / fail

You do not ship `n_jobs=-1` in a production web worker (it fights
the request threads).
