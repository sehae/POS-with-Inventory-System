# checkout_receipt_dialog.py
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class CheckoutReceiptDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Checkout Receipt")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def set_receipt_details(self, order_id, customer_name, package_name, guest_pax, order_type, cash_amount,
                            penalty_fee):
        receipt_content = f"""
        Moon Hey Hotpot and Grill

        ----------------------------------------

        Order ID: {order_id}
        Customer Name: {customer_name}

        -- Order Details --
        Package Name: {package_name}
        Guest Pax: {guest_pax}
        Order Type: {order_type}
        Cash Amount: {cash_amount}
        Penalty Fee: {penalty_fee}

        Thank you for dining with us!

        [Leave space for any additional notes or signatures]
        """
        self.layout.addWidget(QLabel(receipt_content))
