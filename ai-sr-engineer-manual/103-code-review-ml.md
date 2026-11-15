# 103. Reviewing an ML PR (what you look for)

Checklist when a teammate (or you) opens a PR:

- [ ] Target definition in the README
- [ ] Split is time or grouped if needed
- [ ] Pipeline, not ad hoc scaler
- [ ] Dummy baseline numbers
- [ ] Metric matches the decision
- [ ] Threshold not silently 0.5
- [ ] No ID / future columns
- [ ] Versions pinned
- [ ] Test for NaN / schema
- [ ] metrics.json / model version
- [ ] Rollback sentence
- [ ] No PII in the diff

If three boxes are empty, request changes. That is communication
(the posting asked for it) without being theatrical.

## Pass / fail

You can review a notebook-as-PR and reject it for leakage in 5 minutes.
