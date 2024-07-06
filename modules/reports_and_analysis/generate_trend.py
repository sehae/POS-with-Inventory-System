import configparser
import pandas as pd
from datetime import datetime, timedelta
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

from validator.user_manager import userManager


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def save_config(trend_path):
    config = configparser.ConfigParser()
    config.read('config.ini')

    if trend_path:
        if 'DEFAULT' not in config:
            config['DEFAULT'] = {}
        config['DEFAULT']['trend_path'] = trend_path

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Replace 'username', 'password', 'localhost', 'dbname' with your actual MySQL credentials and database name
engine = create_engine('mysql+pymysql://root:root@localhost/poswithinventorysystem')

# Query to join order, leftover, package, and add_on tables
query = """
SELECT 
    o.Order_ID, 
    o.Date,
    o.Time,
    o.Total_Amount,
    o.Customer_Name,
    o.Soup_Variation,
    o.Guest_Pax,
    o.Order_Type,
    o.Payment_Method,
    p.Package_Name,
    a.Product_Details
FROM 
    `order` o
LEFT JOIN 
    leftover l ON o.Leftover_ID = l.Leftover_ID
LEFT JOIN 
    package p ON o.Package_ID = p.Package_ID
LEFT JOIN
    add_on a ON o.Order_ID = a.Order_ID
"""


dataframe = pd.read_sql(query, engine)

# Combine Date and Time into a single DateTime column
dataframe['DateTime'] = pd.to_datetime(dataframe['Date'].astype(str) + ' ' + dataframe['Time'].astype(str))

# Peak Days/Weeks Analysis
def peak_analysis(df):
    df['Date'] = df['DateTime'].dt.date
    daily_orders = df.groupby('Date').size()
    weekly_orders = df.groupby(df['DateTime'].dt.to_period('W')).size()
    monthly_orders = df.groupby(df['DateTime'].dt.to_period('M')).size()

    return daily_orders, weekly_orders, monthly_orders

# Customer Pattern Analysis
def customer_pattern_analysis(df):
    repeat_visits = df['Customer_Name'].value_counts()
    avg_guest_pax = df['Guest_Pax'].mean()
    preferred_soup_variations = df['Soup_Variation'].value_counts()

    return repeat_visits, avg_guest_pax, preferred_soup_variations

# Popular Items Using Add-Ons
def popular_add_ons(df):
    df['Add_On_Items'] = df['Product_Details'].apply(lambda x: eval(x) if isinstance(x, str) else [])
    all_add_ons = [item.get('items', []) for item in df['Add_On_Items'] if isinstance(item, dict)]
    add_on_counts = pd.Series([item for sublist in all_add_ons for item in sublist]).value_counts()

    return add_on_counts

# Plotting function
def plot_trends(report_data, daily_orders, weekly_orders, monthly_orders, repeat_visits, preferred_soup_variations,
                add_on_counts, file_path):
    if daily_orders is not None:
        plt.figure(figsize=(12, 8))
        daily_orders.plot(kind='bar', color='skyblue', title='Daily Orders')
        plt.xlabel('Date')
        plt.ylabel('Number of Orders')
        plt.tight_layout()
        plt.savefig(f'{file_path}/daily_orders.png')
        plt.close()

    if weekly_orders is not None:
        plt.figure(figsize=(12, 8))
        weekly_orders.plot(kind='bar', color='orange', title='Weekly Orders')
        plt.xlabel('Week')
        plt.ylabel('Number of Orders')
        plt.tight_layout()
        plt.savefig(f'{file_path}/weekly_orders.png')
        plt.close()

    if monthly_orders is not None:
        plt.figure(figsize=(12, 8))
        monthly_orders.plot(kind='bar', color='green', title='Monthly Orders')
        plt.xlabel('Month')
        plt.ylabel('Number of Orders')
        plt.tight_layout()
        plt.savefig(f'{file_path}/monthly_orders.png')
        plt.close()

    # Plot Customer Pattern Analysis
    plt.figure(figsize=(12, 8))
    repeat_visits.plot(kind='bar', color='purple', title='Repeat Visits')
    plt.xlabel('Customer Name')
    plt.ylabel('Number of Visits')
    plt.tight_layout()
    plt.savefig(f'{file_path}/repeat_visits.png')
    plt.close()

    plt.figure(figsize=(12, 8))
    preferred_soup_variations.plot(kind='bar', color='teal', title='Preferred Soup Variations')
    plt.xlabel('Soup Variation')
    plt.ylabel('Number of Orders')
    plt.tight_layout()
    plt.savefig(f'{file_path}/preferred_soup_variations.png')
    plt.close()

    # Plot Popular Add-Ons
    plt.figure(figsize=(12, 8))
    add_on_counts.plot(kind='bar', color='red', title='Popular Add-Ons')
    plt.xlabel('Add-On Items')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{file_path}/add_ons.png')
    plt.close()



# Save Report to Word
def save_report_to_word(df, frequency, file_path):
    document = Document()

    section = document.sections[0]
    header = section.header
    month = datetime.now().strftime("%B")
    content_header = [
        "Moon Hey Hotpot and Grill",
        "848A Banawe St, Quezon City, 1114 Metro Manila",
        "0917 624 9289",
        "Trend Analysis Report",
        f"({month})",
    ]

    for content_h in content_header:
        header_paragraph = header.add_paragraph(content_h)
        run = header_paragraph.runs[0]

        # Center align the paragraph
        header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Remove spacing before and after the paragraph
        header_paragraph.paragraph_format.space_before = Pt(0)
        header_paragraph.paragraph_format.space_after = Pt(0)

    footer = section.footer
    date = datetime.now().strftime("%B %d, %Y")
    time = datetime.now().strftime("%I:%M %p")
    user_manager = userManager._instance
    username = user_manager.get_current_username()
    footer_paragraph = footer.add_paragraph()
    footer_paragraph.text = f"{date} | {time}    Created by: {username}"
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    document.save(f'{file_path}/Sales_Trend_Report_{frequency}.docx')

# Main function to generate report
def generate_report(df, frequency, file_path):
    print("Original DataFrame:")
    print(df.head())  # Print the DataFrame before filtering
    print(datetime.now().date())  # Print the current date

    if frequency == 'Daily':
        report_data = df[df['DateTime'].dt.date == datetime.now().date()]
    elif frequency == 'Weekly':
        last_week = datetime.now().date() - timedelta(days=7)
        report_data = df[(df['DateTime'].dt.date >= last_week) & (df['DateTime'].dt.date <= datetime.now().date())]
    elif frequency == 'Monthly':
        last_month = datetime.now().date() - timedelta(days=30)
        report_data = df[(df['DateTime'].dt.date >= last_month) & (df['DateTime'].dt.date <= datetime.now().date())]

    print(f"Report Data Length for {frequency}: {len(report_data)}")  # Print length of filtered data

    if len(report_data) == 0:
        print(f"No data available for {frequency} report.")
        return

    # Analysis
    daily_orders, weekly_orders, monthly_orders = peak_analysis(report_data)
    repeat_visits, avg_guest_pax, preferred_soup_variations = customer_pattern_analysis(report_data)
    add_on_counts = popular_add_ons(report_data)

    # Generate Plots based on frequency
    plot_trends(report_data, daily_orders if frequency == 'Daily' else None,
                weekly_orders if frequency == 'Weekly' else None,
                monthly_orders if frequency == 'Monthly' else None,
                repeat_visits, preferred_soup_variations, add_on_counts, file_path)

    # Save Report to Word
    save_report_to_word(report_data, frequency, file_path)

