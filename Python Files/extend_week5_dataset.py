import pandas as pd
from pathlib import Path

# Read the Week 5 dataset. Change this path if your CSV is stored elsewhere.
input_file = Path(r"C:\Users\krish\OneDrive\Desktop\Week 5 Power BI Business Intelligence Assignment\Dataset\sales_dataset.csv")
output_file = Path("week6_extended_sales_dataset.csv")

df = pd.read_csv(input_file)

# Add 20 illustrative dates across 10 months.
df["Order_Date"] = pd.date_range("2025-01-08", periods=len(df), freq="15D")

# Week 5 did not contain actual cost or profit fields.
# These product-level cost rates are assumptions for practice, not company records.
cost_rates = {
    "Laptop": 0.82,
    "Mobile": 0.75,
    "Tablet": 0.78,
    "Headphones": 0.60
}
df["Estimated_Cost_Rate"] = df["Product"].map(cost_rates)
df["Estimated_Cost"] = (df["Revenue"] * df["Estimated_Cost_Rate"]).round(0)
df["Estimated_Profit"] = df["Revenue"] - df["Estimated_Cost"]
df["Profit_Margin_Pct"] = (
    df["Estimated_Profit"] / df["Revenue"] * 100
).round(2)

df["Year_Month"] = df["Order_Date"].dt.strftime("%Y-%m")
df["Month"] = df["Order_Date"].dt.strftime("%b")
df["Year"] = df["Order_Date"].dt.year

df.to_csv(output_file, index=False)
print("Extended dataset created:", output_file.resolve())
print("Rows and columns:", df.shape)
print(df.head())
