import pandas as pd

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "capstone-a-churn"))
from src.data import synthesize
from src.features import TARGET, drop_leaks

df = drop_leaks(synthesize(n=2000, seed=0))
print("shape", df.shape)
print("dtypes")
print(df.dtypes)
print("target rate", float(df[TARGET].mean()))
print("nulls")
print(df.isna().sum())
print("duplicate customer_id", int(df["customer_id"].duplicated().sum()))
print(df.describe(include="all").transpose().head(12))
print("churn by contract")
print(df.groupby("contract")[TARGET].mean())
print("churn by internet")
print(df.groupby("internet")[TARGET].mean())
print("will not use customer_id as a feature")
