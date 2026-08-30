Stock & Inventory Management Analytics Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI">
  <img src="https://img.shields.io/badge/Python-Data%20Pipeline-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/DAX-Measures-512BD4?style=for-the-badge" alt="DAX">
  <img src="https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=for-the-badge&logo=pandas" alt="Pandas">
</p>

> An end-to-end Business Intelligence project that generates, cleans, models, and analyzes retail inventory data using Python and Power BI.

## Project overview

This project simulates a real-world Stock & Inventory Management System. A realistic retail dataset is generated with Python, cleaned and validated through a dedicated quality process, and then analyzed in Power BI through five interactive dashboards.

The solution covers sales, inventory, customers, purchase orders, returns, promotions, warehouses, and supplier performance. Clean CSV files are modeled in a star schema and enhanced with DAX measures to turn operational data into actionable business insights.

## Project workflow

```text
Python data generation
        |
        v
Data cleaning & quality validation
        |
        v
Clean CSV datasets
        |
        v
Power BI data model (star schema)
        |
        v
DAX measures & KPIs
        |
        v
Five interactive dashboards
        |
        v
Business insights
```

## Technology stack

- Power BI
- Python
- Pandas and NumPy
- DAX
- CSV
- Star schema data modeling

## Key features

- Synthetic retail data generation with seasonal demand, promotions, returns, and inventory movements.
- Data cleaning and quality validation before reporting.
- Clean CSV datasets prepared for analysis.
- Star schema model in Power BI.
- Interactive slicers, cross-filtering, KPI cards, trend analysis, and time intelligence.
- Five focused dashboards for executive, inventory, sales, customer, and operations analysis.

## Repository structure

```text
Stock-and-Inventory-Management-Dashboard/
|
|-- PowerBI/
|   `-- StockAndInventoryManagement_new.pbix
|
|-- Python/
|   |-- data_generation.py
|   `-- data_cleaning.py
|
|-- Data/
|   |-- data_sales.csv
|   |-- data_returns.csv
|   |-- data_purchase_orders.csv
|   |-- data_promotions.csv
|   |-- data_products.csv
|   |-- data_customers.csv
|   `-- data_current_inventory.csv
|
|-- Screenshots/
|   |-- generate_data outcome.png
|   |-- cleaned_data 1.png
|   |-- cleaned_data 2.png
|   |-- Executive Dashboard.png
|   |-- inventory analysis dashboard.png
|   |-- sales dashboard.png
|   |-- Customer analytics dashboard.png
|   `-- operations & performance dashboard.png
|
`-- README.md
```

## 1. Synthetic data generation

Python is used to generate realistic retail data instead of relying on a public dataset. The generated data includes products, customers, sales transactions, purchase orders, current inventory, inventory movements, returns, promotions, and supplier-related operational activity.

Retail events such as Black Friday, Diwali, Christmas, New Year, and seasonal sales are represented to create realistic changes in demand.

<p align="center">
  <img src="Screenshots/generate_data%20outcome.png" alt="Python data generation output" width="100%">
</p>

## 2. Data cleaning & quality validation

Before loading the data into Power BI, the Python cleaning pipeline validates and prepares each dataset. The process includes:

- Missing-value and duplicate checks
- Duplicate transaction validation
- Orphan-record detection
- Negative-value and date validation
- Outlier detection using the IQR method
- Warehouse and category validation
- Data-quality scoring and reporting

<p align="center">
  <img src="Screenshots/cleaned_data%201.png" alt="Data cleaning output 1" width="100%">
</p>

<p align="center">
  <img src="Screenshots/cleaned_data%202.png" alt="Data cleaning output 2" width="100%">
</p>

## 3. Power BI model and dashboards

The cleaned CSV datasets are imported into Power BI and organized into a star schema. DAX measures, dynamic KPIs, interactive slicers, and visualizations are used to explore performance across sales, inventory, customers, and operations.

## Dashboard previews

### Executive Dashboard

Provides a high-level view of business performance through KPIs, revenue and profit trends, sales volume, returns, and warehouse insights.

<p align="center">
  <img src="Screenshots/Executive%20Dashboard.png" alt="Executive Dashboard" width="100%">
</p>

### Inventory Analysis Dashboard

Tracks inventory value, current stock, availability, warehouse distribution, and products that may require replenishment.

<p align="center">
  <img src="Screenshots/inventory%20analysis%20dashboard.png" alt="Inventory Analysis Dashboard" width="100%">
</p>

### Sales Dashboard

Analyzes sales and revenue trends, product and category performance, warehouse contribution, and top-performing products.

<p align="center">
  <img src="Screenshots/sales%20dashboard.png" alt="Sales Dashboard" width="100%">
</p>

### Customer Analytics Dashboard

Explores customer demographics, customer segments, regional performance, purchasing behaviour, and revenue contribution.

<p align="center">
  <img src="Screenshots/Customer%20analytics%20dashboard.png" alt="Customer Analytics Dashboard" width="100%">
</p>

### Operations & Performance Dashboard

Monitors inventory movements, purchase orders, supplier quality, warehouse inventory, and operational KPIs.

<p align="center">
  <img src="Screenshots/operations%20%26%20performance%20dashboard.png" alt="Operations and Performance Dashboard" width="100%">
</p>

## Key performance indicators

The dashboards include KPIs such as:

- Total revenue, total profit, and profit margin
- Sales volume and revenue growth
- Return rate
- Inventory value, current stock, and stock availability
- Customer count and customer contribution
- Supplier quality score and purchase orders
- Inventory movement and low-stock products

## Business questions answered

- Which products and categories generate the highest revenue?
- Which warehouses hold the highest inventory value?
- Which products need replenishment?
- How do sales and inventory movements change over time?
- Which customer segments contribute most to revenue?
- Which suppliers maintain the strongest quality scores?
- How are purchase orders and operational performance trending?

## Skills demonstrated

- Business Intelligence and dashboard design
- Data generation, cleaning, and validation
- ETL-style data preparation
- Power BI data modeling and star schema design
- DAX measures and KPI development
- Retail, sales, inventory, customer, and operations analytics

## Getting started

1. Clone this repository.
2. Open `PowerBI/StockAndInventoryManagement_new.pbix` in Power BI Desktop.
3. If Power BI asks for a data source, reconnect it to the files in the `Data` folder.
4. Refresh the report.
5. Use the slicers and visuals to explore the dashboards.

## Future improvements

- SQL database integration
- Automated ETL scheduling
- Real-time dashboard refresh
- Demand forecasting and inventory optimization
- Supplier performance forecasting

## Author

**Sufiyan Nadaf**  
Aspiring Data Analyst | Power BI | Python | SQL | Business Intelligence

If you find this project useful, consider giving the repository a star.
