# checkout_receipt_dialog.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox

class CheckoutReceiptDialog(QDialog):
    def __init__(self, order_details):
        super().__init__()
        self.setWindowTitle("Order Receipt")
        self.order_details = order_details

        main_layout = QVBoxLayout()

        # Example: Display order details
        details_label = QLabel(order_details)
        main_layout.addWidget(details_label)

        # Button layout
        button_layout = QHBoxLayout()
        print_button = QPushButton("Print Now")
        cancel_button = QPushButton("Cancel")
        button_layout.addWidget(print_button)
        button_layout.addWidget(cancel_button)

        # Connect buttons to slots or functions
        print_button.clicked.connect(self.print_order)
        cancel_button.clicked.connect(self.reject)  # Close the dialog on cancel

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def print_order(self):
        try:
            printer_name = "Gprinter GP-1424D"
            with open(printer_name, "w") as printer:
                printer.write(self.order_details)
            QMessageBox.information(self, "Printing", "Order receipt sent to printer.")
            self.accept()  # Close the dialog after printing

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"Printer '{printer_name}' not found.")

        except PermissionError:
            QMessageBox.critical(self, "Error", "Permission denied to access printer.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error printing: {str(e)}")
