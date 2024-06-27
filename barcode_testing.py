from PyQt5.QtGui import QPixmap

from modules.inventory.barcode_generator import generate_barcode


def main():
    name = "Coca-Cola (330ml)"
    # Get the batch number for the product
    generate_barcode(name)

# Call the main function to start the process
main()
