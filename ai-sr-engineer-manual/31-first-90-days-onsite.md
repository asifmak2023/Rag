# 31. First 90 days if they hire you

Looking seasoned after the offer is how you keep the job. This is not
theory. It is calendar behavior at Bahria Complex 1.

## Week 1. Do not train a model

- Get laptop, git, VPN, data access, Slack/Teams, who owns production.
- Ask: what is already in production, what failed last time, where
  notebooks live.
- Pair with a software engineer on how services are deployed. Copy
  their repo layout.
- Read one real table. Write a one-page data dictionary. Show it.

Deliverable: a note "what I think the first model problem is" with
grain, target, leaks, metric. No code required.

## Weeks 2-3. Baseline in their stack

- Reproduce a number they already believe (a SQL KPI).
- Logistic or GBDT baseline on a frozen extract.
- Same metric they use in the business, even if it is ugly.
- Code in a PR, not a private notebook.

Deliverable: CV table, baseline vs "always predict majority".

## Weeks 4-6. Ship v1 behind a flag

- Batch job if the product can wait overnight. API only if someone
  calls it.
- Tests, `/health`, model version in logs.
- Rollback documented in the README of the service.

Deliverable: a score table or endpoint the product can ignore safely.

## Weeks 7-12. Monitor and one improvement

- Slice metrics, one drift plot, one on-call note template.
- One ablation that is not "try a transformer".
- Talk in standup in product language: "recall at the ops precision
  floor moved from 0.61 to 0.70. False calls up 8%."

## How you use MATLAB/C++/SQL there

- SQL: you volunteer for the feature query. You will be useful on day 2.
- C++: you profile, you do not rewrite the company in C++.
- MATLAB: you port a colleague's prototype without mocking it.

## Things that get you fired from an AI role

- Silent leakage that makes a demo look magic
- Training on production PII in a laptop CSV
- Changing the API contract without telling anyone
- Blocking a release for a 0.004 AUC that does not change a decision

## Pass / fail

You can describe this 90-day plan in the interview when they ask
"what would you do in the first month?" That answer hires seniors.
