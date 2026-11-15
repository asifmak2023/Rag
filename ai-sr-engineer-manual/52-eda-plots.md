# 52. EDA you can defend in 20 minutes

Exploratory data analysis is not 40 seaborn themes. It is a hunt for
grain, leaks, and whether a model is even possible.

## Fixed tour (do this on every new table)

1. Shape, dtypes, memory
2. Target rate
3. Nulls
4. Duplicate keys
5. Date min/max, gaps
6. Numeric describe, a few histograms
7. Categorical cardinalities (top 10 + "other")
8. Target vs 3-5 features (rate by bin or by city)
9. One correlation note: collinear pairs
10. Write "I will not use X because ..."

## Lab 52. File: `labs/52_eda.py`

Print the tour on the synthetic churn from capstone A without plotting
if matplotlib is annoying in CI. Optional: save one png of churn rate
by contract.

## Interview

They may hand you a CSV and watch. Talk while you profile. Silence
while you click is junior. Narrate: "churn is 18%, month-to-month is
half the rows, I smell a leak if cancelled_at is here."

## Pass / fail

On a new 12-column CSV, you produce the tour and two leak suspects
before you train.
