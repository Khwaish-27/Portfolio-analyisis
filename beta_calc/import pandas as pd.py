import pandas as pd
import numpy as np

# Load CSVs with day-first date format
a = pd.read_csv("index_a.csv", parse_dates=["Date"], dayfirst=True)
b = pd.read_csv("index_b.csv", parse_dates=["Date"], dayfirst=True)
c = pd.read_csv("index_c.csv", parse_dates=["Date"], dayfirst=True)

# Rename 'Price' column to make them unique
a = a.rename(columns={"Price": "A_Close"})
b = b.rename(columns={"Price": "B_Close"})
c = c.rename(columns={"Price": "C_Close"})

# Merge data on Date
data = a.merge(b, on="Date").merge(c, on="Date")

# Calculate daily returns
data["A_Return"] = data["A_Close"].pct_change()
data["B_Return"] = data["B_Close"].pct_change()
data["C_Return"] = data["C_Close"].pct_change()

# Drop rows with missing data (from pct_change)
data = data.dropna()

# Calculate beta of B and C w.r.t A
beta_b = data["B_Return"].cov(data["A_Return"]) / data["A_Return"].var()
beta_c = data["C_Return"].cov(data["A_Return"]) / data["A_Return"].var()

# Print the results
print("Beta of Index B with respect to Index A:", beta_b)
print("Beta of Index C with respect to Index A:", beta_c)
