# 63. Data contracts (schema as a test)

Serving dies when someone renames `MonthlyCharges`.

## Contract

A JSON or YAML list: name, dtype, allowed cats, min/max, null ok.

Lab 63. File: `labs/63_schema.py`

```python
SPEC = {
    "tenure_months": {"type": "number", "min": 0, "max": 120},
    "contract": {"type": "str", "values": ["month-to-month", "one-year", "two-year"]},
}

def check_row(row):
    for k, spec in SPEC.items():
        if k not in row:
            raise ValueError(f"missing {k}")
        v = row[k]
        if spec["type"] == "number":
            if not (spec["min"] <= float(v) <= spec["max"]):
                raise ValueError(f"range {k}")
        elif v not in spec["values"]:
            raise ValueError(f"cat {k}")
```

Call this in the API before `predict`. Pydantic already does some of
it in capstone A. This is the same idea for batch CSV files.

## Pass / fail

A renamed column fails loud, not with a silent 0.5 probability.
