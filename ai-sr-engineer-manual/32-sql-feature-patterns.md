# 32. SQL feature patterns (you already know SQL; make it ML)

Point-in-time is the whole game. If the feature query can see the
future, the model is a liar.

## Pattern 1. Snapshot grain

One row per (customer_id, as_of_date). Everything else joins to that.

```sql
WITH spine AS (
  SELECT customer_id, as_of_date
  FROM scoring_calendar
)
SELECT
  s.customer_id,
  s.as_of_date,
  c.city,
  c.plan_type
FROM spine s
JOIN customers c
  ON c.customer_id = s.customer_id
 AND c.valid_from <= s.as_of_date
 AND (c.valid_to IS NULL OR c.valid_to > s.as_of_date);
```

Slowly changing dimensions: the join must be valid at as_of, not "the
latest row in the table today".

## Pattern 2. Rolling windows

```sql
SELECT
  s.customer_id,
  s.as_of_date,
  COUNT(*) FILTER (
    WHERE e.ts >= s.as_of_date - INTERVAL '30 day'
      AND e.ts < s.as_of_date
  ) AS n_events_30d,
  SUM(e.amount) FILTER (
    WHERE e.ts >= s.as_of_date - INTERVAL '30 day'
      AND e.ts < s.as_of_date
  ) AS sum_amount_30d
FROM spine s
LEFT JOIN events e ON e.customer_id = s.customer_id
GROUP BY 1, 2;
```

The upper bound is always `< as_of_date`, never `<=` if as_of is "now"
and events can share the timestamp of the label.

## Pattern 3. Recency

```sql
s.as_of_date - MAX(e.ts) FILTER (WHERE e.ts < s.as_of_date) AS days_since_last
```

Null recency means "never". Keep a boolean `has_ever_event`.

## Pattern 4. Label with delay

Churn in the next 30 days:

```sql
CASE WHEN EXISTS (
  SELECT 1 FROM cancellations k
  WHERE k.customer_id = s.customer_id
    AND k.ts > s.as_of_date
    AND k.ts <= s.as_of_date + INTERVAL '30 day'
) THEN 1 ELSE 0 END AS churn_30d
```

You cannot score today with labels that need 30 days unless you train
on as_of dates at least 30 days ago.

## Pattern 5. Leakage you will actually see

- `cancelled_at` used as a feature for "will cancel"
- `amount_due_after_collection`
- Joining the current customer status that was updated by the event
  you are predicting
- Using `NOW()` in a backtest query

## Lab 32

Extend `labs/06_sql_features.py` with a 7-day window count. Assert the
post-as_of event is excluded. That assert is the seniority.

## Pass / fail

On a whiteboard, write a 30-day count that cannot leak. If you write
`WHERE customer_id = ?` without a time filter, you fail.
