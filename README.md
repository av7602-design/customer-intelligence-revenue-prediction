
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
- Power BI analytics

The goal is to help businesses understand **customer value, purchasing behavior, repurchase likelihood, and revenue patterns**.

---

## 🎯 Business Problem

Businesses generate large amounts of customer and transaction data but often struggle to convert this data into actionable insights.

This project addresses questions such as:

- Which customers have the highest value?
- How can customers be grouped based on purchasing behavior?
- Which customers are likely to make another purchase?
- What revenue can be expected from customers?
- Which product categories contribute most to revenue?
- How do customer segments and purchasing patterns vary?

---

## 🚀 Key Features

### 1. Customer Data Analysis

Customer and transaction-level data are analyzed using Python to identify:

- Purchasing patterns
- Order frequency
- Customer spending behavior
- Revenue trends
- Customer activity

### 2. RFM Customer Segmentation

Customer behavior is analyzed using **RFM analysis**:

- **Recency** – How recently a customer purchased
- **Frequency** – How frequently a customer purchases
- **Monetary** – How much a customer spends

**K-Means clustering** is then applied to group customers according to their purchasing behavior.

### 3. Repurchase Prediction

A Machine Learning classification pipeline is used to predict whether a customer is likely to make another purchase.

This type of prediction can support customer retention and targeted marketing analysis.

### 4. Revenue Prediction

A Machine Learning regression pipeline is used to estimate future customer revenue based on customer-level behavioral features.

### 5. SQL Analytics

SQL queries are included for analyzing:

- Customer purchasing behavior
- Revenue
- Order activity
- Product categories
- Customer segments

### 6. Power BI Analytics

Power BI-ready datasets are provided for creating interactive dashboards covering:

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
          ├─────────────────┐
          ▼                 ▼
     RFM Analysis      Customer Features
          │                 │
          ▼                 ├───────────────┐
   K-Means              Repurchase      Revenue
  Segmentation          Prediction     Prediction
          │                 │               │
          └─────────────────┴───────────────┘
                          │
                          ▼
                   Business Insights
                          │
                          ▼
                   Power BI Analytics
````

---

## 🛠️ Technology Stack

### Programming & Data Science

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

### Machine Learning

* K-Means Clustering
* Classification
* Regression
* Feature Engineering
* Model Evaluation

### Data & Database

* SQL
* Data Cleaning
* Exploratory Data Analysis
* RFM Analysis

### Business Intelligence

* Microsoft Power BI

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

## 📂 Project Structure

```text
customer-intelligence-revenue-prediction/
│
├── analysis_queries.sql
│
├── customers.csv
├── orders.csv
├── customer_features.csv
│
├── powerbi_monthly_revenue.csv
├── powerbi_category_performance.csv
├── powerbi_customer_segments.csv
│
├── project_metrics.csv
│
├── pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 📊 Dataset

The project uses a **synthetic e-commerce dataset** containing customer and transaction information.

### Customer Data

Customer-level information is used for:

* Behavioral analysis
* Feature engineering
* Customer segmentation
* Predictive modeling

### Order Data

Transaction-level information is used to calculate:

* Order frequency
* Customer spending
* Revenue
* Category performance
* Customer activity

> **Note:** The dataset is synthetic and is intended for demonstration and portfolio purposes.

---

## 🔍 Exploratory Data Analysis

The project performs exploratory analysis to identify patterns in:

* Customer purchasing behavior
* Order frequency
* Customer spending
* Revenue trends
* Product categories
* Customer activity
* RFM metrics

The analysis provides the foundation for customer segmentation and predictive modeling.

---

## 👥 Customer Segmentation

RFM metrics are used to understand customer value and purchasing behavior.

### Segmentation Process

```text
Transaction Data
      ↓
Calculate RFM Metrics
      ↓
Prepare Customer Features
      ↓
Apply K-Means Clustering
      ↓
Generate Customer Segments
```

The resulting customer segments can be used for analytical use cases such as:

* Customer profiling
* Retention analysis
* Targeted marketing
* Customer value analysis

---

## 🤖 Predictive Modeling

### Repurchase Prediction

A classification model is used to estimate whether a customer is likely to make another purchase.

**Evaluation Metric:**

* ROC-AUC

**Demo Result:**

```text
ROC-AUC: 0.901
```

### Revenue Prediction

A regression model is used to estimate customer-level future revenue.

**Evaluation Metrics:**

* Mean Absolute Error (MAE)
* R² Score

**Demo Results:**

```text
MAE: 34.17
R²: 0.994
```

> **Important:** These results were obtained using the synthetic demonstration dataset included in this repository. They should not be interpreted as production or real-world model performance.

---

## 📈 Power BI Analytics

The project provides Power BI-ready datasets for creating interactive business intelligence dashboards.

### Dashboard Areas

#### Customer Intelligence

* Customer segments
* RFM analysis
* Customer behavior
* Customer value

#### Revenue Analytics

* Monthly revenue
* Revenue trends
* Category performance
* Customer contribution

#### Predictive Insights

* Repurchase prediction
* Revenue prediction
* Customer-level predictive features

### Power BI Files

```text
powerbi_monthly_revenue.csv
powerbi_category_performance.csv
powerbi_customer_segments.csv
```

These files can be imported into Power BI to create interactive visualizations and dashboards.

---

## 🧮 SQL Analysis

The project includes SQL queries for customer and sales analytics.

The SQL analysis covers areas such as:

* Customer-level aggregation
* Purchase frequency
* Customer spending
* Revenue analysis
* Category performance
* Customer segmentation

SQL queries are available in:

```text
analysis_queries.sql
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/av7602-design/customer-intelligence-revenue-prediction.git
```

### 2. Navigate to the Project

```bash
cd customer-intelligence-revenue-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the Python pipeline:

```bash
python pipeline.py
```

The project data and generated analytical datasets can then be used for further analysis and Power BI visualization.

For SQL analysis, open:

```text
analysis_queries.sql
```

For Power BI analysis, import the Power BI-ready CSV files into Microsoft Power BI.

---

## 📌 Project Workflow

```text
1. Customer & Transaction Data
             ↓
2. Data Cleaning & Preprocessing
             ↓
3. Exploratory Data Analysis
             ↓
4. Feature Engineering
             ↓
5. RFM Analysis
             ↓
6. K-Means Customer Segmentation
             ↓
7. Repurchase Prediction
             ↓
8. Revenue Prediction
             ↓
9. SQL Business Analysis
             ↓
10. Power BI Analytics
             ↓
11. Business Insights
```

---

## 💡 Business Applications

The analytical framework can support use cases such as:

* Customer segmentation
* Customer retention analysis
* Personalized marketing
* Revenue analysis
* Customer value analysis
* Sales analytics
* Business intelligence
* Predictive analytics
* Data-driven decision making

---

## 📈 Future Enhancements

Potential improvements include:

* Customer Lifetime Value (CLV) prediction
* Advanced churn prediction
* Real-time prediction API using Flask or FastAPI
* Model deployment on AWS
* Automated Power BI data refresh
* Advanced ensemble Machine Learning models
* Model monitoring and performance tracking
* Interactive web-based analytics dashboard

---

## 📚 Skills Demonstrated

This project demonstrates practical application of:

* Python
* Pandas
* NumPy
* Scikit-learn
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* RFM Analysis
* K-Means Clustering
* Classification
* Regression
* Model Evaluation
* SQL
* Power BI
* Data Visualization
* Business Intelligence
* Predictive Analytics
* Git & GitHub

---

## 👩‍💻 Author

**Abikka Vincy J**

B.Tech Computer Science & Engineering (Data Science)
SRM Institute of Science and Technology

### Areas of Interest

* Data Science
* Data Analytics
* Machine Learning
* Business Intelligence
* Predictive Analytics

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

````

