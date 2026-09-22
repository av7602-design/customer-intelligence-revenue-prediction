-- Customer Intelligence & Revenue Prediction Platform
-- PostgreSQL/MySQL-compatible analytical examples

-- 1. Monthly revenue
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       SUM(revenue) AS revenue,
       COUNT(order_id) AS orders,
       COUNT(DISTINCT customer_id) AS customers
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

-- 2. Customer-level revenue
SELECT customer_id,
       COUNT(order_id) AS order_count,
       SUM(revenue) AS total_revenue,
       AVG(revenue) AS avg_order_value
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC;

-- 3. Category performance
SELECT category,
       SUM(revenue) AS revenue,
       COUNT(order_id) AS orders,
       AVG(revenue) AS avg_order_value
FROM orders
GROUP BY category
ORDER BY revenue DESC;

-- 4. Regional performance
SELECT region,
       SUM(revenue) AS revenue,
       COUNT(DISTINCT customer_id) AS customers
FROM orders
GROUP BY region
ORDER BY revenue DESC;
