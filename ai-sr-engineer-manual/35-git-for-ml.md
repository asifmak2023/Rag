# 35. Git and repo hygiene for models

Models are software. A pile of notebooks is not a portfolio.

## Layout they can clone

```
project/
  README.md
  requirements.txt
  src/
  tests/
  artifacts/     # gitignored weights, tracked .gitkeep
  data/          # gitignored raw dumps, tracked sample schema
  notebooks/     # optional, not the source of truth
```

Never commit:

- `.env` with keys
- customer CSV
- 500 MB `model.pt` unless they asked for Git LFS
- `__pycache__`

This manual's `.gitignore` already covers the lab artifacts.

## Commands you actually use

```bash
git status
git diff
git add -p
git commit -m "feat: add recall floor threshold search"
git log --oneline -8
```

Message style: `feat:`, `fix:`, `docs:`, `chore:`. Say why if the diff
is not obvious.

## What a PR looks like for ML

- Metric table: baseline vs this branch vs last release
- Data hash or query name
- How to roll back
- Screenshots of plots optional; `metrics.json` required

## DVC / LFS (names)

If artifacts grow, DVC or Git LFS. For this job, `artifacts/` on disk
plus a version string in the API is enough. Do not start a platform
migration in week 1.

## Pass / fail

Your capstone clone has a README that runs, tests that pass, and no
PII. If git status is 40 untracked CSVs, you fail software engineering.
