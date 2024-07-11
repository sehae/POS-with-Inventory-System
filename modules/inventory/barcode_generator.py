import logging
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
from server.local_server import conn

def generate_barcode(name):
    # Map category names to numbers
    category_numbers = {"ingredient": 1, "beverage": 2, "food": 3, "misc": 4}

    cursor = conn.cursor()
    cursor.execute("SELECT category, product_id, date, expiry_date FROM product WHERE name = %s", (name,))
    products = cursor.fetchall()

    if not products:
        logging.error("No products found for name: %s", name)
        return

    # Sort the products by date in ascending order
    products.sort(key=lambda product: product[2])

    # Get the last product (latest batch)
    product = products[-1]

    # Get the number for the product's category
    category_number = category_numbers.get(product[0].lower(), 0)  # Use 0 as the default value

    # Get the last three digits of the product id
    last_three_digits = product[1][-3:]

    # Format the expiry date in the YYMMDD format
    date = datetime.strptime(product[3], "%Y-%m-%d").strftime("%y%m%d")

    # Ensure the batch number is always two digits
    batch_number = f"{len(products):02d}"

    # Combine parts to form the first 12 digits of the barcode
    barcode_without_check_digit = f"{category_number}{last_three_digits}{batch_number}{date}"

    # Calculate the check digit
    check_digit = calculate_ean13_check_digit(barcode_without_check_digit)

    # Form the full EAN-13 barcode
    full_barcode = f"{barcode_without_check_digit}{check_digit}"

    # Generate the barcode image
    generate_barcode_image(full_barcode)

    cursor.close()
    return full_barcode

def calculate_ean13_check_digit(barcode):
    # Convert the barcode into a list of integers
    digits = [int(d) for d in barcode]

    # Calculate the checksum using the EAN-13 algorithm
    checksum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            checksum += digit
        else:
            checksum += digit * 3

    # Calculate the check digit
    check_digit = (10 - (checksum % 10)) % 10
    return check_digit

def generate_barcode_image(barcode_number):
    # Create an EAN13 barcode instance with the given number and an ImageWriter
    ean = barcode.get('ean13', barcode_number, writer=ImageWriter())

    # Save the barcode as an image file for debugging
    filename = "debug_barcode"
    ean.save(filename)

    return filename
