# Customer Intelligence & Revenue Prediction Platform
# Re-run the notebook/script with the supplied CSV files to reproduce the analysis.
# Main workflow:
# 1. Load customers.csv and orders.csv
# 2. Clean and validate data
# 3. Build RFM features
# 4. Apply K-Means customer segmentation
# 5. Train repurchase classifier
# 6. Train 90-day revenue regressor
# 7. Export Power BI-ready tables

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_absolute_error, r2_score

orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
customers = pd.read_csv("customers.csv")

orders["revenue"] = orders["quantity"] * orders["unit_price"] * (1 - orders["discount"])
analysis_date = orders["order_date"].max() + pd.Timedelta(days=1)

rfm = orders.groupby("customer_id").agg(
    last_order=("order_date","max"),
    frequency=("order_id","count"),
    monetary=("revenue","sum"),
    avg_order_value=("revenue","mean"),
    avg_delivery_days=("delivery_days","mean")
).reset_index()

rfm["recency"] = (analysis_date - rfm["last_order"]).dt.days

X_rfm = rfm[["recency","frequency","monetary"]]
scaled = StandardScaler().fit_transform(X_rfm)
rfm["cluster"] = KMeans(n_clusters=4, random_state=42, n_init=20).fit_predict(scaled)

print(rfm.head())
