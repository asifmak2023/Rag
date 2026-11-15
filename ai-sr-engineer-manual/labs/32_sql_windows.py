import sqlite3
from pathlib import Path

import pandas as pd

path = Path("labs/data/toy_windows.db")
path.parent.mkdir(parents=True, exist_ok=True)
con = sqlite3.connect(path)

spine = pd.DataFrame(
    {
        "customer_id": [1, 1],
        "as_of": pd.to_datetime(["2024-02-01", "2024-03-01"]),
    }
)
events = pd.DataFrame(
    {
        "customer_id": [1, 1, 1, 1],
        "ts": pd.to_datetime(
            ["2024-01-20", "2024-01-28", "2024-02-10", "2024-02-25"]
        ),
        "amount": [10.0, 4.0, 50.0, 7.0],
    }
)
spine.to_sql("spine", con, if_exists="replace", index=False)
events.to_sql("events", con, if_exists="replace", index=False)

sql = """
SELECT
  s.customer_id,
  s.as_of,
  COUNT(e.amount) AS n_30d,
  COALESCE(SUM(e.amount), 0) AS sum_30d
FROM spine s
LEFT JOIN events e
  ON e.customer_id = s.customer_id
 AND e.ts < s.as_of
 AND e.ts >= datetime(s.as_of, '-30 day')
GROUP BY s.customer_id, s.as_of
ORDER BY s.as_of
"""
feat = pd.read_sql(sql, con)
print(feat)
feb = feat.iloc[0]
mar = feat.iloc[1]
assert int(feb["n_30d"]) == 2
assert float(feb["sum_30d"]) == 14.0
assert int(mar["n_30d"]) == 2
assert float(mar["sum_30d"]) == 57.0
con.close()
