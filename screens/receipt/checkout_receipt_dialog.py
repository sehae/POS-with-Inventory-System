from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSizeF
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox, QGridLayout

class CheckoutReceiptDialog(QDialog):
    def __init__(self, order_details, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Order Receipt")
        self.order_details = order_details

        main_layout = QVBoxLayout()

        # Header details
        header_label = QLabel("MOON HEY HOTPOT AND GRILL\n848A Banawe St, Quezon City, 1114 Metro Manila\nContact Number: 0917 123 4567")
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # Creating a grid layout for the order details
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(10)  # Set spacing between columns

        # Splitting order details into lines for label-value pairs
        details_lines = order_details.split('\n')[3:]  # Skipping the first three lines which are used in the header
        for i, line in enumerate(details_lines):
            if ':' in line:  # Check if line is in label:value format
                label, value = line.split(':', 1)  # Split only on the first colon
                label_widget = QLabel(label.strip() + ':')
                value_widget = QLabel(value.strip())
                label_widget.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                value_widget.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                grid_layout.addWidget(label_widget, i, 0)
                grid_layout.addWidget(value_widget, i, 1)
            else:  # If not, assume it's a standalone line
                single_line_label = QLabel(line)
                single_line_label.setAlignment(QtCore.Qt.AlignCenter)
                grid_layout.addWidget(single_line_label, i, 0, 1, 2)  # Span both columns

        main_layout.addLayout(grid_layout)

        # Thank you label
        thank_you_label = QLabel("Thank you for your visit!")
        thank_you_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(thank_you_label)

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

        self.adjustSize()  # Adjust size based on content
        self.centerDialog()

    def centerDialog(self):
        # Center dialog within its parent or screen
        frame_geometry = self.frameGeometry()
        screen_center = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def print_order(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setPaperSize(QPrinter.Custom)
        printer.setFullPage(True)

        # Initialize painter to calculate content height
        painter = QPainter()
        painter.begin(printer)
        painter.setFont(QFont('Arial', 10))

        # Define margins in mm
        left_margin_mm = 5
        right_margin_mm = 5
        top_margin_mm = 5
        bottom_margin_mm = 5

        # Convert margins from mm to pixels
        resolution = printer.resolution()
        left_margin = int(left_margin_mm / 25.4 * resolution)
        right_margin = int(right_margin_mm / 25.4 * resolution)
        top_margin = int(top_margin_mm / 25.4 * resolution)
        bottom_margin = int(bottom_margin_mm / 25.4 * resolution)

        # Set the custom page size (e.g., 80mm x 200mm initially)
        page_width_mm = 80
        page_height_mm = 200
        printer.setPageSizeMM(QSizeF(page_width_mm, page_height_mm))

        # Calculate content height and split into chunks
        content_rect = printer.pageRect(QPrinter.DevicePixel)
        content_rect.adjust(left_margin, top_margin, -right_margin, -bottom_margin)

        line_spacing = painter.fontMetrics().lineSpacing()
        lines = self.order_details.split('\n')
        chunks = []
        chunk = []
        current_height = 0
        max_height = int(40 / 25.4 * resolution)  # Convert 40mm to pixels

        for line in lines:
            bounding_rect = painter.boundingRect(content_rect, QtCore.Qt.TextWordWrap, line)
            line_height = bounding_rect.height() + line_spacing
            if current_height + line_height > max_height:
                chunks.append(chunk)
                chunk = []
                current_height = 0
            chunk.append(line)
            current_height += line_height
        if chunk:
            chunks.append(chunk)

        painter.end()

        # Debugging: Log the number of chunks
        print(f"Number of Chunks: {len(chunks)}")

        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            painter.begin(printer)
            painter.setFont(QFont('Arial', 10))

            # Print each chunk as a separate page
            for chunk_index, chunk in enumerate(chunks):
                if chunk_index > 0:
                    printer.newPage()
                y_position = content_rect.top()
                for line in chunk:
                    bounding_rect = painter.boundingRect(content_rect, QtCore.Qt.TextWordWrap, line)
                    painter.drawText(content_rect.adjusted(0, y_position - content_rect.top(), 0, 0),
                                     QtCore.Qt.TextWordWrap, line)
                    y_position += bounding_rect.height() + line_spacing

                    # Debugging: Log coordinates and dimensions
                    print(f"Chunk: {chunk_index}, Line: {line}")
                    print(f"Bounding Rect: {bounding_rect}")
                    print(f"Y Position: {y_position}")

            painter.end()
        else:
            QMessageBox.information(self, "Print Cancelled", "The print job was cancelled.")

