SPEC = {
    "tenure_months": {"type": "number", "min": 0, "max": 120},
    "contract": {
        "type": "str",
        "values": ["month-to-month", "one-year", "two-year"],
    },
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
    return True


assert check_row({"tenure_months": 12, "contract": "one-year"})
try:
    check_row({"tenure_months": 12, "contract": "weekly"})
    raise SystemExit("should have failed")
except ValueError as e:
    print("caught", e)
print("schema ok")
