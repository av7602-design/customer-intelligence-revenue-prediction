# Customer Intelligence & Revenue Prediction Platform

> An end-to-end Data Science and Business Intelligence project for customer segmentation, repurchase prediction, revenue prediction, and interactive Power BI analytics.

---

## 📌 Project Overview

The **Customer Intelligence & Revenue Prediction Platform** is an end-to-end Data Science and Business Intelligence solution designed to analyze customer purchasing behavior and generate actionable business insights.

The project combines:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- RFM (Recency, Frequency, Monetary) analysis
- K-Means customer segmentation
- Machine Learning for repurchase prediction
- Machine Learning for revenue prediction
- SQL-based customer and sales analysis
- Interactive Power BI analytics

The goal is to help businesses understand **who their valuable customers are, which customers are likely to repurchase, and how customer behavior influences future revenue**.

---

## 🎯 Business Problem

Businesses generate large amounts of customer and transaction data but often struggle to convert this data into actionable decisions.

This project addresses key business questions such as:

- Which customers are the most valuable?
- How can customers be grouped based on purchasing behavior?
- Which customers are likely to make another purchase?
- What revenue can be expected from customers?
- Which product categories generate the most revenue?
- How do customer segments and purchasing patterns change over time?

---

## 🚀 Key Features

### 1. Customer Data Analysis

Processed customer and transaction-level data using Python to identify:

- Customer purchasing patterns
- Order frequency
- Spending behavior
- Revenue trends
- Customer activity

### 2. RFM Customer Segmentation

Performed **RFM analysis** using:

- **Recency** – How recently a customer purchased
- **Frequency** – How frequently a customer purchases
- **Monetary** – How much a customer spends

K-Means clustering was then applied to group customers according to their purchasing behavior.

### 3. Repurchase Prediction

Built a Machine Learning classification pipeline to predict whether a customer is likely to make another purchase.

The model can support customer retention and targeted marketing strategies.

### 4. Revenue Prediction

Developed a Machine Learning regression pipeline to estimate future customer revenue based on customer-level behavioral features.

### 5. SQL Analytics

Created SQL queries to analyze:

- Customer purchasing behavior
- Revenue
- Order activity
- Product categories
- Customer segments

### 6. Power BI Analytics

Prepared Power BI-ready datasets for interactive business intelligence dashboards covering:

- Monthly revenue
- Category performance
- Customer segments
- Customer behavior
- Revenue trends

---

## 🧠 Machine Learning Workflow

```text
Raw Customer & Order Data
          │
          ▼
Data Cleaning & Preprocessing
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Feature Engineering
          │
          ├───────────────┐
          ▼               ▼
    RFM Analysis     Customer Features
          │               │
          ▼               ├───────────────┐
    K-Means            Repurchase       Revenue
   Segmentation        Prediction      Prediction
          │               │               │
          └───────────────┴───────────────┘
                          │
                          ▼
                   Business Insights
                          │
                          ▼
                    Power BI Dashboardpatterns, customer behavior, and revenue trends.
- Applied RFM + K-Means segmentation, built ML models for repurchase and revenue prediction, and developed a Power BI dashboard for business insights.
