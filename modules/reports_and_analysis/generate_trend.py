import configparser
import json

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
dataframe['DateTime'] = dataframe['Date'].astype(str) + ' ' + dataframe['Time'].astype(str)
dataframe['DateTime'] = pd.to_datetime(dataframe['DateTime'])

def load_product_data():
    product_query = """
    SELECT Product_ID, Name FROM product
    """
    product_data = pd.read_sql(product_query, engine)
    return product_data

# Function to generate a daily report
def generate_daily_report():
    data = dataframe.copy()
    today = datetime.now().date()
    daily_data = data[data['DateTime'].dt.date == today]
    return daily_data

# Function to generate a weekly report
def generate_weekly_report():
    data = dataframe.copy()
    today = datetime.now().date()
    last_week = today - timedelta(days=7)
    weekly_data = data[(data['DateTime'].dt.date >= last_week) & (data['DateTime'].dt.date <= today)]
    return weekly_data

# Function to generate a monthly report
def generate_monthly_report():
    data = dataframe.copy()
    today = datetime.now().date()
    last_month = today - timedelta(days=30)
    monthly_data = data[(data['DateTime'].dt.date >= last_month) & (data['DateTime'].dt.date <= today)]
    return monthly_data


def analyze_avg_guest_pax(df, frequency):
    if frequency == 'daily':
        # Filter data for 11am to 12am
        df_hourly = df[(df['DateTime'].dt.hour == 11)]

        avg_guest_pax_hourly = df_hourly['Guest_Pax'].mean()
        return avg_guest_pax_hourly

    elif frequency == 'weekly':
        # Group by week and calculate average guest pax
        df['Week'] = df['DateTime'].dt.isocalendar().week
        avg_guest_pax_weekly = df.groupby('Week')['Guest_Pax'].mean()
        return avg_guest_pax_weekly

    elif frequency == 'monthly':
        # Group by month and calculate average guest pax
        df['Month'] = df['DateTime'].dt.month
        avg_guest_pax_monthly = df.groupby('Month')['Guest_Pax'].mean()
        return avg_guest_pax_monthly

    else:
        raise ValueError("Invalid frequency. Choose from 'daily', 'weekly', or 'monthly'.")


def analyze_preferred_soup_variations(df, frequency):
    if frequency == 'daily':
        # Filter data for 11am to 12am
        df_hourly = df[(df['DateTime'].dt.hour == 11)]

        preferred_soup_variations_hourly = df_hourly['Soup_Variation'].value_counts()
        return preferred_soup_variations_hourly

    elif frequency == 'weekly':
        # Group by week and calculate preferred soup variations
        df['Week'] = df['DateTime'].dt.isocalendar().week
        preferred_soup_variations_weekly = df.groupby('Week')['Soup_Variation'].value_counts().unstack().fillna(0)
        return preferred_soup_variations_weekly

    elif frequency == 'monthly':
        # Group by month and calculate preferred soup variations
        df['Month'] = df['DateTime'].dt.month
        preferred_soup_variations_monthly = df.groupby('Month')['Soup_Variation'].value_counts().unstack().fillna(0)
        return preferred_soup_variations_monthly

    else:
        raise ValueError("Invalid frequency. Choose from 'daily', 'weekly', or 'monthly'.")

def analyze_best_selling_product(df):
    # Filter for orders where Order_Type is "add-ons only"
    add_ons = df[df['Order_Type'] == 'add-ons only']

    # Convert Product_Details from JSON string to Python dictionary
    add_ons['Product_Details'] = add_ons['Product_Details'].apply(lambda x: json.loads(x))

    # Flatten the list of products from JSON
    products = [product for sublist in add_ons['Product_Details'].tolist() for product in sublist]

    # Create DataFrame from products list
    products_df = pd.DataFrame(products)

    # Load product data from MySQL
    product_data = load_product_data()

    # Merge with product_data to get Product_Name
    products_df = products_df.merge(product_data, how='left', left_on='Product_ID', right_on='Product_ID')

    # Check for any null values after the merge
    null_counts = products_df['Product_Name'].isnull().sum()
    if null_counts > 0:
        print(f"Warning: {null_counts} rows have null values for Product_Name after merge.")

    # Count occurrences of each product
    best_selling_product = products_df['Product_Name'].value_counts().idxmax()

    return best_selling_product


# Save Report to Word
def save_report_to_word(df, frequency, file_path, avg_guest_pax, preferred_soup_variations, best_selling_product):
    document = Document()

    # Set up sections and headers
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

    # Add header content
    for content_h in content_header:
        header_paragraph = header.add_paragraph(content_h)
        header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        header_paragraph.paragraph_format.space_before = Pt(0)
        header_paragraph.paragraph_format.space_after = Pt(0)

    # Add introductory paragraph
    intro_paragraph = document.add_paragraph()
    intro_paragraph.add_run("\nIntroduction\n").bold = True
    intro_text = (
        f"This report analyzes the sales trends at Moon Hey Hotpot and Grill "
        f"for the {frequency.lower()} period. It includes average guest pax analysis, "
        f"preferred soup variations, and best-selling products."
    )
    intro_paragraph.add_run(intro_text)

    # Add Average Guest Pax Analysis section
    avg_guest_pax_section = document.add_paragraph()
    avg_guest_pax_section.add_run("\nAverage Guest Pax Analysis\n").bold = True
    avg_guest_pax_text = (
        f"The average number of guests per visit during the {frequency.lower()} period was "
        f"{avg_guest_pax:.2f}. This indicates..."
    )
    avg_guest_pax_section.add_run(avg_guest_pax_text)

    # Add Preferred Soup Variations section
    soup_variations_section = document.add_paragraph()
    soup_variations_section.add_run("\nPreferred Soup Variations\n").bold = True
    soup_variations_text = (
        f"The following table shows the preferred soup variations "
        f"during the {frequency.lower()} period:\n"
    )
    soup_variations_section.add_run(soup_variations_text)

    # Create a table for soup variations
    if isinstance(preferred_soup_variations, pd.DataFrame):
        preferred_soup_variations_table = document.add_table(rows=len(preferred_soup_variations) + 1, cols=len(preferred_soup_variations.columns))
        # Add column headers
        for i, col in enumerate(preferred_soup_variations.columns):
            preferred_soup_variations_table.cell(0, i).text = col
        # Add data rows
        for index, row in preferred_soup_variations.iterrows():
            for i, value in enumerate(row):
                preferred_soup_variations_table.cell(index + 1, i).text = str(value)

    # Add Best Selling Product section
    best_selling_product_section = document.add_paragraph()
    best_selling_product_section.add_run("\nBest Selling Product\n").bold = True
    best_selling_product_text = (
        f"The best-selling product during the {frequency.lower()} period was '{best_selling_product}'. "
        f"This product was highly favored among customers, contributing significantly to overall sales."
    )
    best_selling_product_section.add_run(best_selling_product_text)

    # Add plots (example)
    # Example: Plot of Average Guest Pax over time
    plt.figure(figsize=(8, 6))
    plt.plot(df['DateTime'], df['Guest_Pax'], marker='o', linestyle='-', color='b')
    plt.title(f'Average Guest Pax Trend ({frequency.capitalize()})')
    plt.xlabel('Date')
    plt.ylabel('Average Guest Pax')
    plt.grid(True)
    plt.tight_layout()
    avg_guest_pax_plot_path = f'{file_path}/avg_guest_pax_plot_{frequency.lower()}.png'
    plt.savefig(avg_guest_pax_plot_path)
    plt.close()

    # Insert the plot into the document
    document.add_picture(avg_guest_pax_plot_path, width=Inches(6))

    # Add footer
    footer = section.footer
    date = datetime.now().strftime("%B %d, %Y")
    time = datetime.now().strftime("%I:%M %p")
    username = userManager.get_current_username()  # Assuming userManager handles current user
    footer_paragraph = footer.add_paragraph()
    footer_paragraph.text = f"{date} | {time}    Created by: {username}"
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Save document
    document.save(f'{file_path}/Sales_Trend_Report_{frequency.lower()}.docx')

