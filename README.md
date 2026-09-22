# Customer Intelligence & Revenue Prediction Platform

An end-to-end Data Science and BI project for analyzing e-commerce customer behavior,
segmenting customers, predicting repurchase behavior and estimating 90-day customer revenue.

## Tech Stack
Python, Pandas, NumPy, SQL, Scikit-learn, Matplotlib/Power BI

## Workflow
1. Data preparation and validation
2. Exploratory data analysis
3. RFM feature engineering
4. K-Means customer segmentation
5. Repurchase prediction using Random Forest
6. 90-day revenue prediction using Random Forest Regression
7. Power BI-ready business dashboards

## Dataset
This project package includes a **synthetically generated e-commerce dataset** for reproducible demonstration.
It contains 1,500 customers and 7,500 orders. Because the data is synthetic,
do not describe it on your resume as real company/customer data.

## Current model results on the included synthetic data
- Repurchase model ROC-AUC: 0.901
- Revenue model MAE: 34.17
- Revenue model R²: 0.994

These metrics are demonstration results from the included synthetic dataset. If you replace the data,
retrain the models and update the resume metrics with your actual results.

## Power BI
Import:
- powerbi_monthly_revenue.csv
- powerbi_category_performance.csv
- powerbi_customer_segments.csv
- customer_features.csv

Recommended visuals:
- KPI cards: Revenue, Orders, Customers, AOV
- Line chart: Monthly revenue
- Bar chart: Category revenue
- Donut/bar chart: Customer segments
- Scatter: Recency vs Monetary
- Table: Repurchase probability and predicted revenue

## Resume version
**Customer Intelligence & Revenue Prediction Platform | 2026**
- Analyzed customer data using Python, SQL, and EDA, identifying purchasing patterns, customer behavior, and revenue trends.
- Applied RFM + K-Means segmentation, built ML models for repurchase and revenue prediction, and developed a Power BI dashboard for business insights.
