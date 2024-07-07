# checkout_receipt_dialog.py
from PyQt5.QtCore import QSizeF
from PyQt5.QtGui import QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
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
        printer = QPrinter(QPrinter.HighResolution)
        # Set a default page size or adjust based on content
        printer.setPageSizeMM(QSizeF(80, 200))  # Example size, adjust as needed

        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)

            # Optional: Adjust page size based on the length of the order_details
            # This step is more complex with text than images because you need to calculate the text height.
            # For simplicity, this example uses a fixed page size.

            # Draw the text
            rect = painter.viewport()  # Get the drawable area's rectangle
            painter.drawText(rect, 0, self.order_details)  # Draw the order details within the rectangle

            painter.end()
        else:
            print('Print cancelled')
