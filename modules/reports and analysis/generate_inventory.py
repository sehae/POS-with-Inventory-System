import pandas as pd
from datetime import datetime, timedelta

from server.local_server import conn

cursor = conn.cursor()
query = "SELECT * FROM product"
dataframe = pd.read_sql(query, conn)


# Function to generate a daily report
def generate_daily_report(data):
    # Assuming 'Date' column format is 'YYYY-MM-DD'
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    daily_data = data[data['Date'] == pd.to_datetime(today)]
    return daily_data


# Function to generate a weekly report
def generate_weekly_report(data):
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    last_week = today - timedelta(days=7)
    weekly_data = data[(data['Date'] >= pd.to_datetime(last_week)) & (data['Date'] <= pd.to_datetime(today))]
    return weekly_data


# Function to generate a monthly report
def generate_monthly_report(data):
    data['Date'] = pd.to_datetime(data['Date'])
    today = datetime.now().date()
    last_month = today - timedelta(days=30)
    monthly_data = data[(data['Date'] >= pd.to_datetime(last_month)) & (data['Date'] <= pd.to_datetime(today))]
    return monthly_data


# Generate the reports
daily_report = generate_daily_report(df)
weekly_report = generate_weekly_report(df)
monthly_report = generate_monthly_report(df)

# Save the reports to Excel
with pd.ExcelWriter('inventory_reports.xlsx') as writer:
    daily_report.to_excel(writer, sheet_name='Daily Report', index=False)
    weekly_report.to_excel(writer, sheet_name='Weekly Report', index=False)
    monthly_report.to_excel(writer, sheet_name='Monthly Report', index=False)

print("Reports generated successfully!")
