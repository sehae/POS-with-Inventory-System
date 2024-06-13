import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from screens.employee_screens.employee_pos.posHome import Ui_Form
import re  # Import regular expressions module

class posHome(QtWidgets.QWidget, Ui_Form):
    payment_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    home_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(posHome, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.resetVariables()
        self.updateLabels()

    def initUI(self):
        # Connect buttons to their functions
        self.homeBTN.clicked.connect(self.goHome)
        self.menuBTN.clicked.connect(self.goMenu)
        self.paymentBTN.clicked.connect(self.goPayment)
        self.orderBTN.clicked.connect(self.goOrder)
        self.backBTN.clicked.connect(self.goBack)
        self.saveBTN.clicked.connect(self.goSave)
        self.removeBTN.clicked.connect(self.goRemove)
        self.editBTN.clicked.connect(self.goEdit)
        self.cancelBTN.clicked.connect(self.goCancel)
        self.holdOrderBTN.clicked.connect(self.goHoldOrder)
        self.comboPackageBTN.clicked.connect(self.goHotpotGrill)
        self.hotpotBTN.clicked.connect(self.goHotpot)
        self.grillBTN.clicked.connect(self.goGrill)

        # Set selection mode for QListWidget
        self.receipt.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    def resetVariables(self):
        self.subtotal = 0.0
        self.discount = 0.0
        self.taxRate = 0.12
        self.payableAmount = 0.0
        self.discountApplied = False

    def goHome(self):
        self.home_signal.emit()

    def goMenu(self):
        self.menu_signal.emit()

    def goPayment(self):
        self.payment_signal.emit()

    def goOrder(self):
        self.order_signal.emit()

    def goBack(self):
        self.back_signal.emit()

    def goSave(self):
        print("Save button clicked")

    def goRemove(self):
        print("Remove button clicked")
        self.removeSelectedItem()

    def goEdit(self):
        print("Edit button clicked")
        selected_items = self.receipt.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            # Extract item name, quantity, and price from item text using regular expressions
            item_text = item.text()
            match = re.match(r'(.+) x(\d+): Php (\d+\.\d+)', item_text)
            if match:
                item_name = match.group(1)
                current_quantity = int(match.group(2))
                total_price = float(match.group(3))

                # Calculate price per item
                price_per_item = total_price / current_quantity

                # Ask the user to enter the quantity change
                quantity_change, ok = QtWidgets.QInputDialog.getInt(self, "Edit Quantity",
                                                                    f"Enter quantity change for {item_name} (positive to add, negative to subtract):",
                                                                    value=0)
                if ok and quantity_change != 0:
                    new_quantity = current_quantity + quantity_change

                    if new_quantity <= 0:
                        # If the new quantity is zero or negative, remove the item
                        self.receipt.takeItem(self.receipt.row(item))
                        # Subtract the total price of the removed item from the subtotal
                        self.subtotal -= total_price
                    else:
                        # Calculate the new total price for the updated quantity
                        new_total_price = price_per_item * new_quantity
                        # Update the receipt item with the new quantity and total price
                        updated_item_text = f"{item_name} x{new_quantity}: Php {new_total_price:.2f}"
                        item.setText(updated_item_text)
                        # Add or subtract the difference to the subtotal based on the quantity change
                        self.subtotal -= total_price  # Remove the old total price
                        self.subtotal += new_total_price  # Add the new total price

                    # Ensure the subtotal does not go below zero
                    self.subtotal = max(self.subtotal, 0)

        # Update the payable amount
        self.calculatePayableAmount()

    def goCancel(self):
        print("Cancel button clicked")
        self.resetVariables()
        self.receipt.clear()  # Clear the receipt field
        self.updateLabels()
        if self.showSeniorCitizenDialog():  # Ask again if there is a senior citizen
            self.discountApplied = True  # Apply the discount
            self.calculatePayableAmount()
        else:
            del self.discountPromptShown  # Reset the flag to show the prompt again

    def goHoldOrder(self):
        print("Hold Order button clicked")

    def goHotpotGrill(self):
        print("Hotpot and Grill button clicked")
        self.addToSubtotal(900.89)
        self.updateReceipt("Hotpot and Grill", 1009.00)

    def goHotpot(self):
        print("Hotpot button clicked")
        self.addToSubtotal(633.04)
        self.updateReceipt("Hotpot", 709.00)

    def goGrill(self):
        print("Grill button clicked")
        self.addToSubtotal(633.04)
        self.updateReceipt("Grill", 709.00)

    def addToSubtotal(self, amount):
        self.subtotal = round(self.subtotal + amount, 2)
        self.calculatePayableAmount()

    def showSeniorCitizenDialog(self):
        if not hasattr(self, 'discountPromptShown'):
            reply = QtWidgets.QMessageBox.question(self, 'Senior Citizen Discount',
                                                   'Is there a senior citizen?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            self.discountPromptShown = True
            self.discountApplied = (reply == QtWidgets.QMessageBox.Yes)
        return self.discountApplied

    def calculateDiscount(self):
        if not self.discountApplied and self.showSeniorCitizenDialog():
            # Apply discount only if it hasn't been applied before and senior citizen is present
            self.discount = self.subtotal * 0.10
            self.discountApplied = True
        else:
            self.discount = 0.0  # Otherwise, set the discount to zero
        return self.discount

    def calculatePayableAmount(self):
        if not self.discountApplied:
            self.calculateDiscount()  # Ensure discount is calculated based on updated subtotal
        self.payableAmount = (self.subtotal - self.discount) * (1 + self.taxRate)

        # Ensure the payable amount does not go below zero
        if self.payableAmount < 0:
            self.payableAmount = 0.0

        # Ensure the subtotal does not go below zero
        if self.subtotal < 0:
            self.subtotal = 0.0

        self.updateLabels()

    def updateLabels(self):
        self.subtotalDISPLAY.setText(f"Php: {self.subtotal:.2f}")
        self.discountDISPLAY.setText(f"Php: {self.discount:.2f}")
        self.taxDISPLAY.setText(f"Php: {self.subtotal * self.taxRate:.2f}")  # Display tax amount
        self.totalamountDISPLAY.setText(f"Php: {self.payableAmount:.2f}")

    def updateReceipt(self, item, price):
        # Ensure that items are treated as distinct based on their full description
        item_found = False

        for index in range(self.receipt.count()):
            item_text = self.receipt.item(index).text()

            # Use a raw string for the pattern to avoid invalid escape sequence warnings
            pattern = rf"{item} x(\d+): Php (\d+\.\d+)"
            match = re.match(pattern, item_text)
            if match:
                current_quantity = int(match.group(1))
                # Increment the quantity of the existing instance
                updated_quantity = current_quantity + 1
                updated_item_text = f"{item} x{updated_quantity}: Php {price * updated_quantity:.2f}"
                self.receipt.item(index).setText(updated_item_text)
                item_found = True
                break

        # If the item is not found, add it to the receipt with '(x1)'
        if not item_found:
            self.receipt.addItem(f"{item} x1: Php {price:.2f}")

    def removeSelectedItem(self):
        selected_items = self.receipt.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            # Extract price from item text using regular expressions
            item_text = item.text()
            match = re.search(r'Php (\d+\.\d+)', item_text)
            if match:
                price = float(match.group(1))
                # Correct the subtotal by removing the original cost price
                self.subtotal = round(self.subtotal - price / (1 + self.taxRate), 2)

                # Ensure the subtotal does not go below zero
                if self.subtotal < 0:
                    self.subtotal = 0.0

                self.calculatePayableAmount()
                self.receipt.takeItem(self.receipt.row(item))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = posHome()
    mainWin.show()
    sys.exit(app.exec_())
