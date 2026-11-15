import sqlite3
from pathlib import Path

import pandas as pd

path = Path(__file__).resolve().parent / "data" / "toy.db"
path.parent.mkdir(parents=True, exist_ok=True)
con = sqlite3.connect(path)
customers = pd.DataFrame(
    {
        "customer_id": [1, 2, 3],
        "as_of": pd.to_datetime(["2024-02-01", "2024-02-01", "2024-02-01"]),
    }
)
events = pd.DataFrame(
    {
        "customer_id": [1, 1, 1, 2, 2, 3],
        "ts": pd.to_datetime(
            [
                "2024-01-10",
                "2024-01-20",
                "2024-02-10",
                "2024-01-05",
                "2024-01-25",
                "2023-12-01",
            ]
        ),
        "amount": [10.0, 15.0, 999.0, 5.0, 7.0, 40.0],
    }
)
customers.to_sql("customers", con, if_exists="replace", index=False)
events.to_sql("events", con, if_exists="replace", index=False)

sql = """
SELECT
  c.customer_id,
  COUNT(e.amount) AS n_events,
  AVG(e.amount) AS avg_amount_hist
FROM customers c
LEFT JOIN events e
  ON e.customer_id = c.customer_id
 AND e.ts < c.as_of
GROUP BY c.customer_id
ORDER BY c.customer_id
"""
feat = pd.read_sql(sql, con)
print(feat)
assert feat.loc[feat.customer_id == 1, "n_events"].iloc[0] == 2
assert feat.loc[feat.customer_id == 1, "avg_amount_hist"].iloc[0] == 12.5
con.close()
