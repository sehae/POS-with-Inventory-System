import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from screens.employee_screens.employee_pos.posTable import Ui_MainWindow



class posTable(QtWidgets.QMainWindow, Ui_MainWindow):
    payment_signal = QtCore.pyqtSignal()
    back_signal = QtCore.pyqtSignal()
    order_signal = QtCore.pyqtSignal()
    menu_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(posTable, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.firstFloorTableStatus = [True] * 6  # True means available
        self.secondFloorTableStatus = [True] * 6  # True means available

    def initUI(self):
        # Connect buttons to their functions
        self.homeBTN.clicked.connect(self.goHome)
        self.menuBTN.clicked.connect(self.goMenu)
        self.paymentBTN.clicked.connect(self.goPayment)
        self.orderBTN.clicked.connect(self.goOrder)
        self.backBTN.clicked.connect(self.goBack)
        self.firstFloorBTN.clicked.connect(self.showFirstFloorTables)
        self.secondFloorBTN.clicked.connect(self.showSecondFloorTables)
        self.tableOneButton.clicked.connect(lambda: self.selectTable(1))
        self.tableTwoButton.clicked.connect(lambda: self.selectTable(2))
        self.tableThreeButton.clicked.connect(lambda: self.selectTable(3))
        self.tableFourButton.clicked.connect(lambda: self.selectTable(4))
        self.tableFiveButton.clicked.connect(lambda: self.selectTable(5))
        self.tableSixButton.clicked.connect(lambda: self.selectTable(6))


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

    def showFirstFloorTables(self):
        self.firstFloorBTN.setStyleSheet(
            "background-color: #67B99A; color: white; padding: 8px 16px; border-radius: 5px;")
        self.secondFloorBTN.setStyleSheet(
            "background-color: #FAFAFA; color: #D9D9D9; padding: 8px 16px; border-radius: 5px;")
        print("First Floor Tables")

        self.tableOneButton.setText("Table 1")
        self.tableTwoButton.setText("Table 2")
        self.tableThreeButton.setText("Table 3")
        self.tableFourButton.setText("Table 4")
        self.tableFiveButton.setText("Table 5")
        self.tableSixButton.setText("Table 6")

        self.updateTableStatus(self.firstFloorTableStatus)

        self.tableOneButton.clicked.disconnect()
        self.tableTwoButton.clicked.disconnect()
        self.tableThreeButton.clicked.disconnect()
        self.tableFourButton.clicked.disconnect()
        self.tableFiveButton.clicked.disconnect()
        self.tableSixButton.clicked.disconnect()

        self.tableOneButton.clicked.connect(lambda: self.selectTable(1))
        self.tableTwoButton.clicked.connect(lambda: self.selectTable(2))
        self.tableThreeButton.clicked.connect(lambda: self.selectTable(3))
        self.tableFourButton.clicked.connect(lambda: self.selectTable(4))
        self.tableFiveButton.clicked.connect(lambda: self.selectTable(5))
        self.tableSixButton.clicked.connect(lambda: self.selectTable(6))

    def showSecondFloorTables(self):
        self.secondFloorBTN.setStyleSheet(
            "background-color: #67B99A; color: white; padding: 8px 16px; border-radius: 5px;")
        self.firstFloorBTN.setStyleSheet(
            "background-color: #FAFAFA; color: #D9D9D9; padding: 8px 16px; border-radius: 5px;")
        print("Second Floor Tables")

        self.tableOneButton.setText("Table 7")
        self.tableTwoButton.setText("Table 8")
        self.tableThreeButton.setText("Table 9")
        self.tableFourButton.setText("Table 10")
        self.tableFiveButton.setText("Table 11")
        self.tableSixButton.setText("Table 12")

        self.updateTableStatus(self.secondFloorTableStatus)

        self.tableOneButton.clicked.disconnect()
        self.tableTwoButton.clicked.disconnect()
        self.tableThreeButton.clicked.disconnect()
        self.tableFourButton.clicked.disconnect()
        self.tableFiveButton.clicked.disconnect()
        self.tableSixButton.clicked.disconnect()

        self.tableOneButton.clicked.connect(lambda: self.selectSecondFloorTable(7))
        self.tableTwoButton.clicked.connect(lambda: self.selectSecondFloorTable(8))
        self.tableThreeButton.clicked.connect(lambda: self.selectSecondFloorTable(9))
        self.tableFourButton.clicked.connect(lambda: self.selectSecondFloorTable(10))
        self.tableFiveButton.clicked.connect(lambda: self.selectSecondFloorTable(11))
        self.tableSixButton.clicked.connect(lambda: self.selectSecondFloorTable(12))

    def updateTableStatus(self, tableStatus):
        self.tableOneButton.setEnabled(True)
        self.tableTwoButton.setEnabled(True)
        self.tableThreeButton.setEnabled(True)
        self.tableFourButton.setEnabled(True)
        self.tableFiveButton.setEnabled(True)
        self.tableSixButton.setEnabled(True)

        # Update labels for each table
        self.updateTableLabels(tableStatus)

    def updateTableLabels(self, tableStatus):
        labels = [self.tableOneLBL, self.tableTwoLBL, self.tableThreeLBL, self.tableFourLBL, self.tableFiveLBL,
                  self.tableSixLBL]
        buttons = [self.tableOneButton, self.tableTwoButton, self.tableThreeButton, self.tableFourButton,
                   self.tableFiveButton, self.tableSixButton]

        for i, status in enumerate(tableStatus):
            if status:
                labels[i].setText("Available")
                buttons[i].setStyleSheet("background-color: #67B99A; color: white;")
            else:
                labels[i].setText("Unavailable")
                buttons[i].setStyleSheet("background-color: #D9D9D9; color: white;")

    def selectTable(self, table_number):
        if self.firstFloorTableStatus[table_number - 1]:
            guess, ok = QtWidgets.QInputDialog.getInt(self, f"Table {table_number}",
                                                      "Enter the number of guests (1-4):",
                                                      min=1, max=4)
            if ok:
                self.guestNum.setText(str(guess))
                self.tableNum.setText(f"{table_number}")
                print(f"Table {table_number} selected with {guess} guests")
                self.firstFloorTableStatus[table_number - 1] = False  # Mark table as unavailable
                self.updateTableStatus(self.firstFloorTableStatus)
        else:
            QtWidgets.QMessageBox.information(self, "Table Unavailable",
                                              f"Table {table_number} is currently unavailable.")

    def selectSecondFloorTable(self, table_number):
        if self.secondFloorTableStatus[table_number - 7]:
            guess, ok = QtWidgets.QInputDialog.getInt(self, f"Table {table_number}",
                                                      "Enter the number of guests (1-4):",
                                                      min=1, max=4)
            if ok:
                self.guestNum.setText(str(guess))
                self.tableNum.setText(f"{table_number}")
                print(f"Table {table_number} selected with {guess} guests")
                self.secondFloorTableStatus[table_number - 7] = False  # Mark table as unavailable
                self.updateTableStatus(self.secondFloorTableStatus)
        else:
            QtWidgets.QMessageBox.information(self, "Table Unavailable",
                                              f"Table {table_number} is currently unavailable.")
