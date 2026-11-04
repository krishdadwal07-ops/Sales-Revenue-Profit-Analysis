
# Sales Revenue, Profit Margin & Monthly Growth Analysis
# Week 6 - Exploratory Data Analysis (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Load Dataset
file_path = "../Dataset/week6_extended_sales_dataset.csv"
df = pd.read_csv(file_path)

# 2. Basic Dataset Information
print("\n========== DATASET OVERVIEW ==========")
print("First 5 Records:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

# 3. Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate Records
print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate Rows:", df.duplicated().sum())

# 5. Statistical Summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 6. Total Business Performance
print("\n========== BUSINESS PERFORMANCE ==========")
print("Total Revenue:", df["Revenue"].sum())
print("Total Profit:", df["Estimated_Profit"].sum())
print("Average Profit Margin:",
      df["Profit_Margin_Pct"].mean())

# 7. Product-wise Analysis
print("\n========== PRODUCT-WISE ANALYSIS ==========")
product_analysis = df.groupby("Product").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Estimated_Profit", "sum"),
    Average_Margin=("Profit_Margin_Pct", "mean"),
    Total_Units=("Units_Sold", "sum")
)
print(product_analysis)

# 8. Region-wise Analysis
print("\n========== REGION-WISE ANALYSIS ==========")
print(df.groupby("Region")["Revenue"].sum())

# 9. Category-wise Analysis
print("\n========== CATEGORY-WISE ANALYSIS ==========")
print(df.groupby("Category")["Revenue"].sum())

# 10. Monthly Revenue and Growth
monthly = df.groupby("Year_Month")["Revenue"].sum().reset_index()
monthly["Monthly_Growth_Pct"] = (
    monthly["Revenue"].pct_change() * 100
)
print("\n========== MONTHLY GROWTH ==========")
print(monthly)

# 11. Create Visualization Folder
os.makedirs("../Visualizations", exist_ok=True)

# Visualization 1: Product-wise Revenue
plt.figure(figsize=(9, 5))
plt.bar(product_analysis.index, product_analysis["Total_Revenue"])
plt.title("Product-wise Total Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("../Visualizations/01_product_revenue.png")
plt.show()

# Visualization 2: Region-wise Revenue
region_revenue = df.groupby("Region")["Revenue"].sum()
plt.figure(figsize=(8, 5))
plt.bar(region_revenue.index, region_revenue.values)
plt.title("Region-wise Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../Visualizations/02_region_revenue.png")
plt.show()

# Visualization 3: Category-wise Revenue
category_revenue = df.groupby("Category")["Revenue"].sum()
plt.figure(figsize=(7, 7))
plt.pie(category_revenue.values,
        labels=category_revenue.index,
        autopct="%1.1f%%")
plt.title("Category-wise Revenue Distribution")
plt.tight_layout()
plt.savefig("../Visualizations/03_category_revenue.png")
plt.show()

# Visualization 4: Monthly Revenue Trend
plt.figure(figsize=(10, 5))
plt.plot(monthly["Year_Month"], monthly["Revenue"],
         marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../Visualizations/04_monthly_revenue.png")
plt.show()

# Visualization 5: Profit Margin by Product
plt.figure(figsize=(9, 5))
plt.bar(product_analysis.index,
        product_analysis["Average_Margin"])
plt.title("Average Profit Margin by Product")
plt.xlabel("Product")
plt.ylabel("Profit Margin (%)")
plt.tight_layout()
plt.savefig("../Visualizations/05_profit_margin.png")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")
print("Five visualizations saved in the Visualizations folder.")
