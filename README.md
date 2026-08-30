# 📦 Stock & Inventory Management Analytics Dashboard

<p align="center">

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-ETL-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Measures-512BD4?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=for-the-badge&logo=pandas)

</p>

---

# 📖 About The Project

This project demonstrates an **end-to-end Business Intelligence workflow** for a Stock & Inventory Management system.

Instead of relying on publicly available datasets, the complete retail dataset was generated using Python to simulate realistic business scenarios including customer purchases, inventory movements, supplier performance, warehouse operations, seasonal sales, promotions, and returns.

After generating the data, a dedicated data cleaning pipeline was implemented to validate and prepare the datasets before importing them into Power BI.

The cleaned data was modeled using a **Star Schema**, followed by the development of interactive dashboards and business KPIs using DAX.

The final result is a complete Business Intelligence solution that transforms raw operational data into actionable insights.

---

# 🚀 Project Workflow

```
Synthetic Data Generation (Python)
                │
                ▼
Data Cleaning & Quality Validation
                │
                ▼
Clean CSV Dataset
                │
                ▼
Power BI Data Model (Star Schema)
                │
                ▼
DAX Measures & KPIs
                │
                ▼
Interactive Dashboard Development
                │
                ▼
Business Insights
```

---

# 🛠 Tech Stack

- Power BI
- Python
- Pandas
- NumPy
- DAX
- CSV
- Star Schema Data Modeling

---

# 📂 Repository Structure

```
Stock-and-Inventory-Management-Dashboard
│
├── 📁 PowerBI
│   └── StockAndInventoryManagement.pbix
│
├── 📁 Python
│   ├── data_generation.py
│   └── data_cleaning.py
│
├── 📁 Data
│   ├── clean_sales.csv
│   ├── clean_customers.csv
│   ├── clean_products.csv
│   ├── clean_inventory.csv
│   ├── clean_inventory_movements.csv
│   ├── clean_purchase_orders.csv
│   ├── clean_returns.csv
│   ├── clean_suppliers.csv
│   ├── clean_promotions.csv
│   └── clean_date.csv
│
├── 📁 Screenshots
│   ├── data_generation.png
│   ├── data_cleaning.png
│   ├── Executive Dashboard.png
│   ├── Inventory Dashboard.png
│   ├── Sales Dashboard.png
│   ├── Customer Dashboard.png
│   └── Operations Dashboard.png
│
├── data_quality_log.json
└── README.md
```

---

# 🐍 Step 1 — Synthetic Data Generation

The project begins by generating a realistic retail dataset using Python.

The generated data includes:

- Products
- Customers
- Sales Transactions
- Purchase Orders
- Inventory
- Inventory Movements
- Returns
- Promotions
- Supplier Performance

The dataset also simulates real retail events including:

- Black Friday
- Diwali
- Christmas
- New Year
- Summer Sale

to produce realistic demand fluctuations.

## Preview

![Data Generation](Screenshots/data_generation.png)

---

# 🧹 Step 2 — Data Cleaning & Quality Validation

Before importing the data into Power BI, a dedicated cleaning pipeline validates and prepares every dataset.

The cleaning process includes:

- Missing Value Detection
- Duplicate Detection
- Duplicate Transaction Validation
- Orphan Record Detection
- Negative Value Validation
- Outlier Detection (IQR Method)
- Date Validation
- Warehouse Validation
- Category Validation
- Data Quality Scoring

A complete **Data Quality Report** is also generated.

## Preview

![Data Cleaning](Screenshots/data_cleaning.png)

---

# 📊 Step 3 — Power BI Dashboard Development

The cleaned datasets are imported into Power BI where a **Star Schema** data model is built.

Custom DAX measures, KPIs, slicers, and interactive charts are then developed to provide business insights across inventory, sales, customers, and operations.

---

# ⭐ Dashboard Features

✔ Dynamic KPI Cards

✔ Interactive Slicers

✔ Star Schema Data Model

✔ Custom DAX Measures

✔ Time Intelligence

✔ Business KPIs

✔ Interactive Visualizations

✔ Cross Filtering

✔ Trend Analysis

✔ Responsive Dashboard Layout

---

# 📷 Dashboard Preview

## 📊 Executive Dashboard

Provides an overview of overall business performance.

![Executive Dashboard](Screenshots/Executive%20Dashboard.png)

---

## 📦 Inventory Analysis Dashboard

Tracks inventory levels, warehouse performance, stock availability, and inventory value.

![Inventory Dashboard](Screenshots/Inventory%20Analysis%20Dashboard.png)

---

## 💰 Sales Dashboard

Analyzes sales trends, product performance, warehouse revenue, and customer contribution.

![Sales Dashboard](Screenshots/Sales%20Dashboard.png)

---

## 👥 Customer Analytics Dashboard

Analyzes customer demographics, purchasing behavior, revenue contribution, and regional distribution.

![Customer Dashboard](Screenshots/Customer%20Analytics%20Dashboard.png)

---

## ⚙️ Operations & Performance Dashboard

Monitors inventory movement, purchase orders, supplier quality, and operational efficiency.

![Operations Dashboard](Screenshots/Operations%20Dashboard.png)

---

# 📈 Key Performance Indicators

The dashboards include multiple business KPIs including:

- Total Revenue
- Total Profit
- Profit Margin
- Sales Volume
- Return Rate
- Inventory Value
- Current Stock
- Stock Availability
- Revenue Growth
- Customer Count
- Supplier Quality Score
- Purchase Orders
- Inventory Movement
- Low Stock Products

---

# 💡 Business Questions Answered

The dashboards help answer questions such as:

- Which product categories generate the highest revenue?
- Which warehouses contribute the highest inventory value?
- Which products require immediate replenishment?
- How does inventory movement change over time?
- Which customer segment contributes the most revenue?
- Which age group generates the highest sales?
- Which suppliers maintain the highest quality scores?
- How are purchase orders trending over time?

---

# 🧠 Skills Demonstrated

This project demonstrates practical experience in:

- Business Intelligence
- Data Analytics
- Dashboard Design
- Data Cleaning
- ETL
- Python Automation
- Pandas
- DAX
- KPI Development
- Star Schema Design
- Data Modeling
- Retail Analytics
- Data Visualization

---

# ▶️ Getting Started

1. Clone this repository.

2. Open:

```
PowerBI/StockAndInventoryManagement.pbix
```

3. If prompted, reconnect the CSV files located inside the **Data** folder.

4. Refresh the report.

5. Explore the interactive dashboards.

---

# 📌 Future Improvements

Possible future enhancements include:

- SQL Database Integration
- Automated ETL Pipeline
- Real-Time Dashboard Refresh
- Forecasting using Power BI
- Demand Prediction
- Inventory Optimization
- Supplier Performance Forecasting

---

# ⭐ If You Like This Project

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

It helps support the project and encourages future improvements.

---

# 👨‍💻 Author

**Sufiyan Nadaf**

Aspiring Data Analyst | Power BI | Python | SQL | Business Intelligence

Feel free to connect and share your feedback!
