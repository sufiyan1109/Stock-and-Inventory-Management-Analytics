import pandas as pd
import numpy as np
import json
from datetime import datetime

# ============================================================
# LOAD RAW DATA
# ============================================================
df_sales = pd.read_csv('data_sales.csv')
df_returns = pd.read_csv('data_returns.csv')
df_po = pd.read_csv('data_purchase_orders.csv')
df_inv = pd.read_csv('data_current_inventory.csv')
df_inv_mov = pd.read_csv('data_inventory_movements.csv')
df_sup = pd.read_csv('data_suppliers.csv')
df_prod = pd.read_csv('data_products.csv')
df_cust = pd.read_csv('data_customers.csv')
df_promo = pd.read_csv('data_promotions.csv')

# Convert dates
for df, date_cols in [
    (df_sales, ['Date']),
    (df_returns, ['Date']),
    (df_po, ['PO_Date', 'Expected_Delivery', 'Actual_Delivery']),
    (df_inv, ['Last_Stock_Count']),
    (df_inv_mov, ['Date']),
    (df_cust, ['Registration_Date']),
    (df_promo, ['Start_Date', 'End_Date'])
]:
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])

print("=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

quality_scores = {}

# ============================================================
# 1. MISSING VALUES
# ============================================================
print("\n1. MISSING VALUES")
for name, df in [
    ("Sales", df_sales), ("Returns", df_returns), ("PO", df_po),
    ("Inventory", df_inv), ("Movements", df_inv_mov), ("Suppliers", df_sup),
    ("Products", df_prod), ("Customers", df_cust), ("Promotions", df_promo)
]:
    missing = int(df.isnull().sum().sum())
    total = int(df.size)
    score = float(max(0, 100 - (missing / total * 100)))
    quality_scores[name] = score
    print(f"  {name}: {missing} missing values (Score: {score:.1f}%)")

# ============================================================
# 2. DUPLICATE KEYS
# ============================================================
print("\n2. DUPLICATE KEYS")
dup_sku = int(df_prod[['SKU', 'Warehouse']].duplicated().sum())
print(f"  Duplicate SKU-Warehouse in products: {dup_sku}")

# ============================================================
# 3. ORPHANED RECORDS
# ============================================================
print("\n3. ORPHANED RECORDS")
sales_orphans = int(df_sales[~df_sales['SKU'].isin(df_prod['SKU'])].shape[0])
po_orphans = int(df_po[~df_po['SKU'].isin(df_prod['SKU'])].shape[0])
return_orphans = int(df_returns[~df_returns['SKU'].isin(df_prod['SKU'])].shape[0])
print(f"  Orphaned sales SKUs: {sales_orphans}")
print(f"  Orphaned PO SKUs: {po_orphans}")
print(f"  Orphaned return SKUs: {return_orphans}")

# ============================================================
# 4. NEGATIVE/ZERO VALUES
# ============================================================
print("\n4. NEGATIVE/ZERO VALUES")
neg_revenue = int((df_sales['Revenue'] < 0).sum())
neg_cogs = int((df_sales['COGS'] < 0).sum())
neg_qty = int((df_sales['Quantity_Sold'] <= 0).sum())
neg_po_qty = int((df_po['Order_Qty'] <= 0).sum())
print(f"  Negative revenue: {neg_revenue}")
print(f"  Negative COGS: {neg_cogs}")
print(f"  Zero/negative quantity sold: {neg_qty}")
print(f"  Zero/negative PO quantity: {neg_po_qty}")

# ============================================================
# 5. OUTLIER DETECTION (IQR Method)
# ============================================================
print("\n5. OUTLIER DETECTION")

def detect_outliers(series, name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = float(Q1 - 1.5 * IQR)
    upper = float(Q3 + 1.5 * IQR)
    outliers = int(((series < lower) | (series > upper)).sum())
    print(f"  {name}: {outliers} outliers (range: {lower:.2f} - {upper:.2f})")
    return outliers

detect_outliers(df_sales['Revenue'], "Revenue")
detect_outliers(df_sales['Quantity_Sold'], "Quantity Sold")
detect_outliers(df_prod['Unit_Cost'], "Unit Cost")
detect_outliers(df_prod['Selling_Price'], "Selling Price")

# ============================================================
# 6. DATE VALIDATION
# ============================================================
print("\n6. DATE VALIDATION")
future_sales = int((df_sales['Date'] > pd.Timestamp('2026-07-10')).sum())
impossible_po = int((df_po['Expected_Delivery'] < df_po['PO_Date']).sum())
print(f"  Future sales dates: {future_sales}")
print(f"  PO delivery before order: {impossible_po}")

# ============================================================
# 7. DUPLICATE TRANSACTIONS
# ============================================================
print("\n7. DUPLICATE TRANSACTIONS")
dup_sales = int(df_sales[['Transaction_ID']].duplicated().sum())
dup_po = int(df_po[['PO_ID']].duplicated().sum())
print(f"  Duplicate transaction IDs: {dup_sales}")
print(f"  Duplicate PO IDs: {dup_po}")

# ============================================================
# 8. CATEGORY & WAREHOUSE VALIDATION
# ============================================================
print("\n8. VALID CATEGORY/WAREHOUSE")
valid_cats = ["Electronics", "Apparel", "Home", "Sports", "Food"]
valid_wh = ["WH-East", "WH-West", "WH-Central"]
invalid_cat = int((~df_prod['Category'].isin(valid_cats)).sum())
invalid_wh = int((~df_prod['Warehouse'].isin(valid_wh)).sum())
print(f"  Invalid categories: {invalid_cat}")
print(f"  Invalid warehouses: {invalid_wh}")

# ============================================================
# 9. OVERALL QUALITY SCORE
# ============================================================
print("\n" + "=" * 60)
overall = float(np.mean(list(quality_scores.values())))
print(f"OVERALL DATA QUALITY SCORE: {overall:.1f}/100")
print("=" * 60)

# ============================================================
# 10. FIXES
# ============================================================
print("\n🔧 APPLYING FIXES...")

zero_stock = int((df_inv['Current_Stock'] <= 0).sum())
df_inv.loc[df_inv['Current_Stock'] <= 0, 'Stock_Status'] = 'OUT'
df_inv['Current_Stock'] = df_inv['Current_Stock'].clip(lower=0)
print(f"  Fixed {zero_stock} SKUs with zero/negative stock")

# Standardize column names
for df in [df_sales, df_returns, df_po, df_inv, df_inv_mov, df_sup, df_prod, df_cust, df_promo]:
    df.columns = df.columns.str.lower().str.replace(' ', '_')

# Create date dimension
date_range = pd.date_range(start=df_sales['date'].min(), end=df_sales['date'].max(), freq='D')
df_date = pd.DataFrame({
    'date': date_range,
    'year': date_range.year,
    'month': date_range.month,
    'month_name': date_range.month_name(),
    'quarter': date_range.quarter,
    'day_of_week': date_range.day_name(),
    'is_weekend': date_range.dayofweek.isin([5, 6]),
    'fiscal_quarter': ((date_range.month - 1) // 3 + 1)
})

# ============================================================
# SAVE QUALITY LOG (ALL VALUES CONVERTED TO PYTHON TYPES)
# ============================================================
log = {
    'timestamp': datetime.now().isoformat(),
    'quality_scores': {k: float(round(v, 1)) for k, v in quality_scores.items()},
    'overall_score': float(round(overall, 1)),
    'issues_found': {
        'missing_values': int(sum(1 for v in quality_scores.values() if v < 100)),
        'zero_stock': zero_stock,
        'orphaned_records': int(sales_orphans + po_orphans + return_orphans),
        'negative_values': int(neg_revenue + neg_cogs + neg_qty + neg_po_qty),
        'duplicate_keys': dup_sku,
        'invalid_categories': invalid_cat,
        'invalid_warehouses': invalid_wh
    }
}

with open('data_quality_log.json', 'w') as f:
    json.dump(log, f, indent=2)

# ============================================================
# SAVE CLEAN FILES
# ============================================================
df_sales.to_csv('clean_sales.csv', index=False)
df_returns.to_csv('clean_returns.csv', index=False)
df_po.to_csv('clean_purchase_orders.csv', index=False)
df_inv.to_csv('clean_inventory.csv', index=False)
df_inv_mov.to_csv('clean_inventory_movements.csv', index=False)
df_sup.to_csv('clean_suppliers.csv', index=False)
df_prod.to_csv('clean_products.csv', index=False)
df_cust.to_csv('clean_customers.csv', index=False)
df_promo.to_csv('clean_promotions.csv', index=False)
df_date.to_csv('clean_date.csv', index=False)

print(f"\n✅ Clean files saved!")
print(f"Date dimension: {len(df_date)} rows")
print("Quality log saved: data_quality_log.json")
print("\n=== CLEANING COMPLETE ===")