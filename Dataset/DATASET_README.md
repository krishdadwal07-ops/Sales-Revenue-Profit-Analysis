# Week 6 Capstone Dataset Notes

This dataset extends the Week 5 sales dataset with fields needed for profit and monthly analysis.

## Original fields
Order_ID, Product, Category, Region, Units_Sold, Unit_Price, Customer_Rating, Revenue

## Added fields
- Order_Date: illustrative dates assigned for training analysis.
- Estimated_Cost_Rate: assumed product-level cost percentage.
- Estimated_Cost: Revenue multiplied by the assumed cost rate.
- Estimated_Profit: Revenue minus Estimated_Cost.
- Profit_Margin_Pct: Estimated_Profit / Revenue * 100.
- Year_Month, Month, Year: date dimensions for monthly summaries.

## Important data limitation
Week 5 data did not contain actual order dates, cost, or profit. These added values are simulated assumptions for the Week 6 learning project. They are not actual Prime Corporate Gifting financial records and must not be represented as company-reported figures.

Cost-rate assumptions used:
- Laptop: 82%
- Mobile: 75%
- Tablet: 78%
- Headphones: 60%

For an authentic business analysis, replace these assumptions with verified transaction dates and costs if they become available.
