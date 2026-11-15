# Feature dictionary

Grain: one customer at scoring time. Target: churn (1/0).

| name | dtype | source | leak risk |
|---|---|---|---|
| tenure_months | int | account | low |
| monthly_charges | float | billing | low |
| total_charges | float | billing | medium if it includes last unbilled cycle |
| senior | 0/1 | profile | low |
| contract | cat | account | low |
| internet | cat | account | low |
| avg_charge_per_month | float | total/tenure | low |
| customer_id | id | key | do not use as feature |
| future_collection_flag | int | planted leak | refused |

Owner: you, until a real team assigns one.
