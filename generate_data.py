import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# ============================================================
# CONFIG
# ============================================================
n_skus = 200  # sku=stock keeping unit
n_warehouses = 3
n_days = 730
n_customers = 500

# ============================================================
# MASTER DATA
# ============================================================
skus = [f"SKU-{i:04d}" for i in range(1, n_skus + 1)] 
warehouses = ["WH-East", "WH-West", "WH-Central"]
categories = ["Electronics", "Apparel", "Home", "Sports", "Food"]
suppliers = [f"SUP-{i:03d}" for i in range(1, 31)]

customer_segments = ["Premium", "Standard", "Budget"]
customer_regions = ["North", "South", "East", "West", "Central"]
customer_genders = ["M", "F", "Other"]
age_groups = ["18-25", "26-35", "36-45", "46-55", "55+"]

seasonal_events = {
    "Black Friday": {"dates": [(2024, 11, 29), (2025, 11, 28)], "multiplier": 3.5, "duration": 3},
    "Christmas": {"dates": [(2024, 12, 20), (2025, 12, 20)], "multiplier": 2.5, "duration": 7},
    "Diwali": {"dates": [(2024, 11, 1), (2025, 10, 21)], "multiplier": 2.8, "duration": 5},
    "New Year": {"dates": [(2024, 12, 31), (2025, 12, 31)], "multiplier": 2.0, "duration": 2},
    "Summer Sale": {"dates": [(2024, 6, 15), (2025, 6, 15)], "multiplier": 1.8, "duration": 5},
}

# ============================================================
# PRODUCTS
# ============================================================
products_list = []
for sku in skus:
    category = np.random.choice(categories)
    unit_cost = round(np.random.uniform(10, 500), 2)
    markup = np.random.uniform(0.15, 0.80)
    selling_price = round(unit_cost * (1 + markup), 2)
    n_wh = np.random.randint(1, 4)
    assigned_wh = np.random.choice(warehouses, size=n_wh, replace=False).tolist()
    delay_prob = round(np.random.uniform(0.05, 0.35), 2)
    quality_score = round(np.random.uniform(75, 98), 1)
    defect_rate = round(np.random.uniform(0.01, 0.08), 3)
    
    for wh in assigned_wh:
        products_list.append({
            'SKU': sku,
            'Product_Name': f"Product {sku}",
            'Category': category,
            'Unit_Cost': unit_cost,
            'Selling_Price': selling_price,
            'Lead_Time_Days': np.random.randint(3, 21),
            'Supplier_ID': np.random.choice(suppliers),
            'Min_Order_Qty': np.random.randint(50, 500),
            'Shelf_Life_Days': np.random.choice([30, 60, 90, 180, 365, 999]),
            'Warehouse': wh,
            'Delay_Probability': delay_prob,
            'Supplier_Quality_Score': quality_score,
            'Defect_Rate': defect_rate
        })

df_products = pd.DataFrame(products_list)

# ============================================================
# CUSTOMERS
# ============================================================
customers = []
for i in range(1, n_customers + 1):
    customers.append({
        'Customer_ID': f"CUST-{i:05d}",
        'Customer_Name': f"Customer {i}",
        'Region': np.random.choice(customer_regions),
        'Segment': np.random.choice(customer_segments),
        'Gender': np.random.choice(customer_genders),
        'Age_Group': np.random.choice(age_groups),
        'Registration_Date': pd.Timestamp('2024-07-11') + timedelta(days=np.random.randint(0, 730))
    })
df_customers = pd.DataFrame(customers)

# ============================================================
# PROMOTIONS
# ============================================================
promotions = []
promo_names = ["Summer Blast", "Flash Sale", "Weekend Special", "Clearance", "Member Exclusive"]
for i in range(20):
    start = pd.Timestamp('2024-07-11') + timedelta(days=np.random.randint(0, 600))
    end = start + timedelta(days=np.random.randint(3, 14))
    promotions.append({
        'Promotion_ID': f"PROMO-{i+1:03d}",
        'Promotion_Name': np.random.choice(promo_names),
        'Discount_Pct': round(np.random.uniform(10, 50), 1),
        'Start_Date': start,
        'End_Date': end,
        'Category': np.random.choice(categories + ['All'])
    })
df_promotions = pd.DataFrame(promotions)

# ============================================================
# SALES TRANSACTIONS
# ============================================================
dates = pd.date_range(end=datetime(2026, 7, 10), periods=n_days, freq='D')

def get_event_multiplier(date, category):
    mult = 1.0
    for event_name, event_info in seasonal_events.items():
        for (y, m, d) in event_info['dates']:
            event_start = pd.Timestamp(y, m, d)
            event_end = event_start + timedelta(days=event_info['duration'])
            if event_start <= date <= event_end:
                if category in ["Electronics", "Apparel"] or event_name == "Black Friday":
                    mult = max(mult, event_info['multiplier'])
                else:
                    mult = max(mult, event_info['multiplier'] * 0.7)
    return mult

def get_promotion_discount(date, category):
    active = df_promotions[
        (df_promotions['Start_Date'] <= date) & 
        (df_promotions['End_Date'] >= date) &
        ((df_promotions['Category'] == category) | (df_promotions['Category'] == 'All'))
    ]
    if len(active) > 0:
        best = active.loc[active['Discount_Pct'].idxmax()]
        return best['Discount_Pct'] / 100, best['Promotion_ID']
    return 0, None

transactions = []
returns = []

for _, product in df_products.iterrows():
    sku = product['SKU']
    wh = product['Warehouse']
    category = product['Category']
    unit_cost = product['Unit_Cost']
    base_price = product['Selling_Price']
    base_demand = np.random.poisson(np.random.randint(2, 15))
    days = np.arange(n_days)
    seasonality = 1 + 0.4 * np.sin(2 * np.pi * days / 365.25)
    trend = 1 + days * 0.0002
    noise = np.random.normal(1, 0.3, n_days)
    
    for i, date in enumerate(dates):
        event_mult = get_event_multiplier(date, category)
        discount, promo_id = get_promotion_discount(date, category)
        daily_demand = (base_demand * seasonality[i] * trend[i] * noise[i] * event_mult).clip(0).astype(int)
        
        if daily_demand > 0:
            final_price = round(base_price * (1 - discount), 2)
            customer = df_customers.sample(1).iloc[0]
            txn_id = f"TXN-{len(transactions)+1:07d}"
            
            transactions.append({
                'Transaction_ID': txn_id,
                'Date': date,
                'SKU': sku,
                'Warehouse': wh,
                'Category': category,
                'Customer_ID': customer['Customer_ID'],
                'Quantity_Sold': daily_demand,
                'Unit_Price': final_price,
                'Revenue': round(daily_demand * final_price, 2),
                'COGS': round(daily_demand * unit_cost, 2),
                'Promotion_ID': promo_id,
                'Discount_Pct': round(discount * 100, 1) if discount > 0 else 0
            })
            
            if np.random.random() < 0.05:
                return_qty = np.random.randint(1, max(2, daily_demand // 3 + 1))
                return_reasons = ["Defective", "Wrong Item", "Changed Mind", "Expired", "Damaged"]
                returns.append({
                    'Return_ID': f"RET-{len(returns)+1:05d}",
                    'Original_Transaction_ID': txn_id,
                    'Date': date + timedelta(days=np.random.randint(1, 30)),
                    'SKU': sku,
                    'Warehouse': wh,
                    'Customer_ID': customer['Customer_ID'],
                    'Return_Qty': return_qty,
                    'Return_Reason': np.random.choice(return_reasons),
                    'Refund_Amount': round(return_qty * final_price, 2)
                })

df_sales = pd.DataFrame(transactions)
df_returns = pd.DataFrame(returns)

# ============================================================
# PURCHASE ORDERS
# ============================================================
purchase_orders = []
for _, product in df_products.iterrows():
    order_dates = pd.date_range(start=dates[0], end=dates[-1], freq=f"{np.random.randint(14, 45)}D")
    for od in order_dates:
        qty = np.random.randint(product['Min_Order_Qty'], product['Min_Order_Qty'] * 3)
        expected = od + timedelta(days=product['Lead_Time_Days'])
        if np.random.random() < product['Delay_Probability']:
            actual = expected + timedelta(days=np.random.randint(1, 10))
            status = 'Delayed'
        else:
            actual = expected
            status = np.random.choice(['Delivered', 'In-Transit', 'Pending'], p=[0.85, 0.10, 0.05])
        
        purchase_orders.append({
            'PO_ID': f"PO-{len(purchase_orders)+1:06d}",
            'PO_Date': od,
            'SKU': product['SKU'],
            'Warehouse': product['Warehouse'],
            'Supplier_ID': product['Supplier_ID'],
            'Order_Qty': qty,
            'Unit_Cost': product['Unit_Cost'],
            'Expected_Delivery': expected,
            'Actual_Delivery': actual,
            'Status': status
        })

df_po = pd.DataFrame(purchase_orders)

# ============================================================
# INVENTORY MOVEMENTS
# ============================================================
inventory_movements = []

for _, po in df_po[df_po['Status'] == 'Delivered'].iterrows():
    inventory_movements.append({
        'Movement_ID': f"MOV-{len(inventory_movements)+1:08d}",
        'Date': po['Actual_Delivery'],
        'SKU': po['SKU'],
        'Warehouse': po['Warehouse'],
        'Movement_Type': 'Goods Received',
        'Quantity': po['Order_Qty'],
        'Reference_ID': po['PO_ID']
    })

for _, sale in df_sales.iterrows():
    inventory_movements.append({
        'Movement_ID': f"MOV-{len(inventory_movements)+1:08d}",
        'Date': sale['Date'],
        'SKU': sale['SKU'],
        'Warehouse': sale['Warehouse'],
        'Movement_Type': 'Sale',
        'Quantity': -sale['Quantity_Sold'],
        'Reference_ID': sale['Transaction_ID']
    })

for _, ret in df_returns.iterrows():
    inventory_movements.append({
        'Movement_ID': f"MOV-{len(inventory_movements)+1:08d}",
        'Date': ret['Date'],
        'SKU': ret['SKU'],
        'Warehouse': ret['Warehouse'],
        'Movement_Type': 'Return',
        'Quantity': ret['Return_Qty'],
        'Reference_ID': ret['Return_ID']
    })

all_sku_wh = df_products[['SKU', 'Warehouse']].drop_duplicates()
for _ in range(int(len(all_sku_wh) * 0.02 * n_days / 30)):
    row = all_sku_wh.sample(1).iloc[0]
    adj_date = pd.Timestamp('2024-07-11') + timedelta(days=np.random.randint(0, n_days))
    adj_qty = np.random.randint(-20, 21)
    if adj_qty != 0:
        inventory_movements.append({
            'Movement_ID': f"MOV-{len(inventory_movements)+1:08d}",
            'Date': adj_date,
            'SKU': row['SKU'],
            'Warehouse': row['Warehouse'],
            'Movement_Type': 'Stock Adjustment',
            'Quantity': adj_qty,
            'Reference_ID': f"ADJ-{len(inventory_movements):06d}"
        })

df_inventory_movements = pd.DataFrame(inventory_movements)

# ============================================================
# CURRENT INVENTORY SNAPSHOT
# ============================================================
current_stock = []
for _, product in df_products.iterrows():
    sku = product['SKU']
    wh = product['Warehouse']
    movements = df_inventory_movements[
        (df_inventory_movements['SKU'] == sku) & 
        (df_inventory_movements['Warehouse'] == wh)
    ]
    total_in = movements[movements['Quantity'] > 0]['Quantity'].sum()
    total_out = abs(movements[movements['Quantity'] < 0]['Quantity'].sum())
    stock = total_in - total_out
    
    sku_sales = df_sales[(df_sales['SKU'] == sku) & (df_sales['Warehouse'] == wh)]
    avg_daily_demand = sku_sales['Quantity_Sold'].sum() / n_days if len(sku_sales) > 0 else 0
    safety_stock = avg_daily_demand * np.random.uniform(1.5, 3.0)
    reorder_point = int(avg_daily_demand * product['Lead_Time_Days'] + safety_stock)
    max_stock = int(reorder_point * 3)
    
    last_received = df_inventory_movements[
        (df_inventory_movements['SKU'] == sku) & 
        (df_inventory_movements['Warehouse'] == wh) &
        (df_inventory_movements['Movement_Type'] == 'Goods Received')
    ]['Date'].max()
    
    days_in_stock = (pd.Timestamp('2026-07-10') - last_received).days if pd.notna(last_received) else 999
    shelf_life = product['Shelf_Life_Days']
    expiry_status = 'Fresh' if days_in_stock < shelf_life * 0.3 else 'Aging' if days_in_stock < shelf_life * 0.7 else 'Near Expiry' if days_in_stock < shelf_life else 'Expired'
    
    current_stock.append({
        'SKU': sku,
        'Warehouse': wh,
        'Current_Stock': max(stock, 0),
        'Reorder_Point': reorder_point,
        'Max_Stock': max_stock,
        'Last_Stock_Count': pd.Timestamp('2026-07-01') - timedelta(days=np.random.randint(1, 10)),
        'Stock_Status': 'OK' if stock > reorder_point else 'LOW' if stock > 0 else 'OUT',
        'Days_In_Stock': days_in_stock,
        'Shelf_Life_Days': shelf_life,
        'Expiry_Status': expiry_status
    })

df_inventory = pd.DataFrame(current_stock)

# ============================================================
# SUPPLIER PERFORMANCE
# ============================================================
supplier_perf = []
for sup in suppliers:
    sup_pos = df_po[df_po['Supplier_ID'] == sup]
    if len(sup_pos) > 0:
        delivered = sup_pos[sup_pos['Status'] == 'Delivered']
        if len(delivered) > 0:
            on_time = (delivered['Actual_Delivery'] <= delivered['Expected_Delivery']).sum()
            on_time_rate = round(on_time / len(delivered) * 100, 1)
            avg_delay = (delivered['Actual_Delivery'] - delivered['Expected_Delivery']).dt.days.mean()
            avg_delay = round(avg_delay, 1) if pd.notna(avg_delay) else 0
        else:
            on_time_rate = 0
            avg_delay = 0
        
        sup_products = df_products[df_products['Supplier_ID'] == sup]
        avg_quality = sup_products['Supplier_Quality_Score'].mean() if len(sup_products) > 0 else 85
        avg_defect = sup_products['Defect_Rate'].mean() if len(sup_products) > 0 else 0.05
        
        supplier_perf.append({
            'Supplier_ID': sup,
            'Total_Orders': len(sup_pos),
            'Delivered_Orders': len(delivered),
            'On_Time_Rate': on_time_rate,
            'Avg_Delay_Days': avg_delay,
            'Quality_Score': round(avg_quality, 1),
            'Defect_Rate': round(avg_defect, 3),
            'Avg_Lead_Time': sup_pos['Expected_Delivery'].sub(sup_pos['PO_Date']).dt.days.mean().round(1)
        })

df_suppliers = pd.DataFrame(supplier_perf)

# ============================================================
# SAVE ALL FILES
# ============================================================
df_sales.to_csv('data_sales.csv', index=False)
df_returns.to_csv('data_returns.csv', index=False)
df_po.to_csv('data_purchase_orders.csv', index=False)
df_inventory.to_csv('data_current_inventory.csv', index=False)
df_inventory_movements.to_csv('data_inventory_movements.csv', index=False)
df_suppliers.to_csv('data_suppliers.csv', index=False)
df_products.to_csv('data_products.csv', index=False)
df_customers.to_csv('data_customers.csv', index=False)
df_promotions.to_csv('data_promotions.csv', index=False)

print("✅ Data generated successfully!")
print(f"Sales transactions: {len(df_sales):,}")
print(f"Returns: {len(df_returns):,}")
print(f"Purchase orders: {len(df_po):,}")
print(f"Inventory movements: {len(df_inventory_movements):,}")
print(f"Products (SKU-WH combos): {len(df_products)}")
print(f"Current SKUs in inventory: {len(df_inventory)}")
print(f"Customers: {len(df_customers)}")
print(f"Promotions: {len(df_promotions)}")
print(f"Suppliers: {len(df_suppliers)}")