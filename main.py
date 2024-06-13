import sys
from PyQt5 import QtWidgets
from screens.employee_screens.employee_pos.posOrder_functions import posOrder
from screens.employee_screens.employee_pos.posPayment_functions import posPayment
from screens.employee_screens.employee_pos.posTable_functions import posTable
from screens.employee_screens.employee_pos.posHome_functions import posHome

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up fullscreen
        self.showFullScreen()

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.pos_order = posOrder()
        self.pos_payment = posPayment()
        self.pos_table = posTable()
        self.pos_home = posHome()

        self.stacked_widget.addWidget(self.pos_table)  # pos_table is now the home screen
        self.stacked_widget.addWidget(self.pos_home)   # pos_home is now the menu screen
        self.stacked_widget.addWidget(self.pos_payment)
        self.stacked_widget.addWidget(self.pos_order)

        # Connect signals to change screens within MainWindow
        self.pos_order.payment_signal.connect(self.show_pos_payment)
        self.pos_order.menu_signal.connect(self.show_pos_menu)
        self.pos_order.home_signal.connect(self.show_pos_home)
        self.pos_payment.home_signal.connect(self.show_pos_home)        # Connect posPayment's home_signal
        self.pos_payment.menu_signal.connect(self.show_pos_menu)        # Connect posPayment's menu_signal
        self.pos_payment.order_signal.connect(self.show_pos_order)
        self.pos_table.payment_signal.connect(self.show_pos_payment)
        self.pos_table.order_signal.connect(self.show_pos_order)
        self.pos_table.menu_signal.connect(self.show_pos_menu)
        self.pos_home.payment_signal.connect(self.show_pos_payment)
        self.pos_home.order_signal.connect(self.show_pos_order)
        self.pos_home.home_signal.connect(self.show_pos_home)
        self.pos_home.back_signal.connect(self.show_pos_home)


    def show_pos_order(self):
        self.stacked_widget.setCurrentWidget(self.pos_order)

    def show_pos_payment(self):
        self.stacked_widget.setCurrentWidget(self.pos_payment)

    def show_pos_home(self):
        self.stacked_widget.setCurrentWidget(self.pos_table)

    def show_pos_menu(self):
        self.stacked_widget.setCurrentWidget(self.pos_home)  # Switch to pos_home (menu screen)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
