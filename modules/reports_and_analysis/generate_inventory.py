import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# Replace 'username', 'password', 'localhost', 'dbname' with your actual MySQL credentials and database name
engine = create_engine('mysql+pymysql://root:root@localhost/poswithinventorysystem')

# Query to join product, supplier, and inventory tables
query = """
SELECT 
    p.Product_ID, 
    p.Date, 
    p.Name, 
    p.Quantity, 
    p.Threshold_Value, 
    p.Expiry_Date, 
    p.Availability, 
    p.Category, 
    p.Status,
    i.Selling_Cost,
    i.Buying_Cost,
    s.Supplier_Name,
    s.Contact_Number,
    s.Email,
    s.Address,
    s.Status AS Supplier_Status
FROM 
    product p
LEFT JOIN 
    inventory i ON p.Product_ID = i.Product_ID
LEFT JOIN 
    supplier s ON i.Supplier_ID = s.Supplier_ID
"""

dataframe = pd.read_sql(query, engine)

# Function to generate a daily report
def generate_daily_report():
    data = dataframe.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    daily_data = data[data['Date'] == pd.to_datetime(today)]
    return daily_data

# Function to generate a weekly report
def generate_weekly_report():
    data = dataframe.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    last_week = today - timedelta(days=7)
    weekly_data = data[(data['Date'] >= pd.to_datetime(last_week)) & (data['Date'] <= pd.to_datetime(today))]
    return weekly_data

# Function to generate a monthly report
def generate_monthly_report():
    data = dataframe.copy()
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    last_month = today - timedelta(days=30)
    monthly_data = data[(data['Date'] >= pd.to_datetime(last_month)) & (data['Date'] <= pd.to_datetime(today))]
    return monthly_data

# Generate reports
daily_report = generate_daily_report()
weekly_report = generate_weekly_report()
monthly_report = generate_monthly_report()

# Save reports to Excel
with pd.ExcelWriter('inventory_reports.xlsx') as writer:
    daily_report.to_excel(writer, sheet_name='Daily Report', index=False)
    weekly_report.to_excel(writer, sheet_name='Weekly Report', index=False)
    monthly_report.to_excel(writer, sheet_name='Monthly Report', index=False)

print("Reports have been generated and saved to 'inventory_reports.xlsx'")
