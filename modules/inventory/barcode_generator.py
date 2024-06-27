import logging
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
from server.local_server import conn

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_barcode(name):
    logging.debug("Starting barcode generation for product: %s", name)

    # Map category names to numbers
    category_numbers = {"ingredient": 1, "beverage": 2, "food": 3, "misc": 4}

    cursor = conn.cursor()
    cursor.execute("SELECT category, product_id, date, expiry_date FROM product WHERE name = %s", (name,))
    products = cursor.fetchall()

    if not products:
        logging.error("No products found for name: %s", name)
        return

    logging.debug("Fetched products: %s", products)

    # Sort the products by date in ascending order
    products.sort(key=lambda product: product[2])
    logging.debug("Sorted products: %s", products)

    # Get the last product (latest batch)
    product = products[-1]
    logging.debug("Selected latest product: %s", product)

    # Get the number for the product's category
    category_number = category_numbers.get(product[0].lower(), 0)  # Use 0 as the default value
    logging.debug("Category number: %d", category_number)

    # Get the last three digits of the product id
    last_three_digits = product[1][-3:]
    logging.debug("Last three digits of product ID: %s", last_three_digits)

    # Format the expiry date in the YYMMDD format
    expiry_date = datetime.strptime(product[3], "%Y-%m-%d").strftime("%y%m%d")
    logging.debug("Formatted expiry date: %s", expiry_date)

    # Ensure the batch number is always two digits
    batch_number = f"{len(products):02d}"
    logging.debug("Batch number: %s", batch_number)

    # Combine parts to form the first 12 digits of the barcode
    barcode_without_check_digit = f"{category_number}{last_three_digits}{batch_number}{expiry_date}"
    logging.debug("Barcode without check digit: %s", barcode_without_check_digit)

    # Calculate the check digit
    check_digit = calculate_ean13_check_digit(barcode_without_check_digit)
    logging.debug("Check digit: %d", check_digit)

    # Form the full EAN-13 barcode
    full_barcode = f"{barcode_without_check_digit}{check_digit}"
    logging.debug("Full EAN-13 barcode: %s", full_barcode)

    # Generate the barcode image
    generate_barcode_image(full_barcode)

    cursor.close()
    return full_barcode

def calculate_ean13_check_digit(barcode):
    logging.debug("Calculating check digit for barcode: %s", barcode)

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
    logging.debug("Calculated check digit: %d", check_digit)
    return check_digit

def generate_barcode_image(barcode_number):
    logging.debug("Generating barcode image for number: %s", barcode_number)

    # Create an EAN13 barcode instance with the given number and an ImageWriter
    ean = barcode.get('ean13', barcode_number, writer=ImageWriter())

    # Save the barcode as an image file for debugging
    filename = "debug_barcode"
    ean.save(filename)
    logging.debug("Saved barcode image to file: %s", filename)

    return filename
