import sys
from PyQt5 import QtWidgets

from shared.directories import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up fullscreen
        self.showFullScreen()

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_screen = myLoginScreen()
        self.admin_dashboard = myAdminDashboard()
        self.admin_maintenance = adminMaintenance()
        self.admin_maintenanceEDIT = adminMaintenanceEDIT()
        self.admin_inventory = adminInventoryAddProduct()
        self.admin_inventoryMODIFY = adminInventoryModifyProduct()
        self.about_devCredits = aboutdevCredits()
        self.about_info = aboutInfo()
        self.help_FAQ = helpFAQ()
        self.help_support = helpSupport()
        self.help_manual = helpManual()
        self.change_password = changePassword()

        self.employee_dashboard = myEmployeeDashboard()
        self.pos_order = posOrder()
        self.pos_payment = posPayment()
        self.pos_table = posTable()
        self.inventory_modify = inventoryModify()
        self.inventory_barcode = inventoryBarcode()

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.admin_dashboard)
        self.stacked_widget.addWidget(self.admin_maintenance)
        self.stacked_widget.addWidget(self.admin_maintenanceEDIT)
        self.stacked_widget.addWidget(self.admin_inventory)
        self.stacked_widget.addWidget(self.admin_inventoryMODIFY)
        self.stacked_widget.addWidget(self.about_devCredits)
        self.stacked_widget.addWidget(self.about_info)
        self.stacked_widget.addWidget(self.help_FAQ)
        self.stacked_widget.addWidget(self.help_support)
        self.stacked_widget.addWidget(self.help_manual)
        self.stacked_widget.addWidget(self.change_password)
        self.stacked_widget.addWidget(self.employee_dashboard)
        self.stacked_widget.addWidget(self.pos_order)
        self.stacked_widget.addWidget(self.pos_payment)
        self.stacked_widget.addWidget(self.pos_table)
        self.stacked_widget.addWidget(self.inventory_modify)
        self.stacked_widget.addWidget(self.inventory_barcode)

        self.login_screen.login_successful.connect(self.show_admin_dashboard)
        self.admin_dashboard.logout_signal.connect(self.show_login_screen)
        self.admin_dashboard.maintenance_signal.connect(self.show_admin_maintenance)
        self.admin_dashboard.about_signal.connect(self.show_about_devcredits)
        self.admin_maintenance.edit_signal.connect(self.show_admin_maintenance_edit)
        self.admin_maintenanceEDIT.add_signal.connect(self.show_admin_maintenance)
        self.admin_maintenanceEDIT.back_signal.connect(self.show_admin_dashboard)
        self.admin_maintenance.back_signal.connect(self.show_admin_dashboard)
        self.admin_dashboard.inventory_signal.connect(self.show_admin_inventory)
        self.admin_inventory.back_signal.connect(self.show_admin_dashboard)
        self.admin_inventory.modify_signal.connect(self.show_admin_inventory_modify)
        self.admin_inventoryMODIFY.add_signal.connect(self.show_admin_inventory)
        self.admin_inventoryMODIFY.back_signal.connect(self.show_admin_dashboard)
        self.about_devCredits.back_signal.connect(self.show_admin_dashboard)
        self.about_devCredits.info_signal.connect(self.show_about_info)
        self.about_info.back_signal.connect(self.show_admin_dashboard)
        self.about_info.credits_signal.connect(self.show_about_devcredits)
        self.admin_dashboard.help_signal.connect(self.show_help_faq)
        self.help_FAQ.support_signal.connect(self.show_help_support)
        self.help_FAQ.back_signal.connect(self.show_admin_dashboard)
        self.help_FAQ.back_employee_signal.connect(self.show_employee_dashboard)
        self.help_FAQ.manual_signal.connect(self.show_user_manual)
        self.help_support.back_signal.connect(self.show_admin_dashboard)
        self.help_support.manual_signal.connect(self.show_user_manual)
        self.help_support.faq_signal.connect(self.show_help_faq)
        self.help_manual.support_signal.connect(self.show_help_support)
        self.help_manual.back_signal.connect(self.show_admin_dashboard)
        self.help_manual.faq_signal.connect(self.show_help_faq)
        self.admin_dashboard.changepass_signal.connect(self.show_change_password)
        self.change_password.back_signal.connect(self.show_admin_dashboard)

        self.login_screen.login_successful_employee.connect(self.show_employee_dashboard)
        self.employee_dashboard.pos_signal.connect(self.show_pos_order)
        self.employee_dashboard.logout_signal.connect(self.show_login_screen)
        self.pos_order.back_signal.connect(self.show_employee_dashboard)
        self.pos_order.payment_signal.connect(self.show_pos_payment)
        self.pos_order.menu_signal.connect(self.show_pos_menu)

        self.pos_payment.back_signal.connect(self.show_employee_dashboard)
        self.pos_payment.menu_signal.connect(self.show_pos_menu)
        self.pos_payment.order_signal.connect(self.show_pos_order)
        self.pos_table.payment_signal.connect(self.show_pos_payment)
        self.pos_table.back_signal.connect(self.show_employee_dashboard)
        self.pos_table.order_signal.connect(self.show_pos_order)

        self.employee_dashboard.inventoryModify_signal.connect(self.show_employee_inventory)
        self.inventory_modify.barcode_signal.connect(self.show_inventory_barcode)
        self.inventory_modify.back_signal.connect(self.show_employee_dashboard)
        self.inventory_barcode.back_signal.connect(self.show_employee_dashboard)
        self.inventory_barcode.modify_signal.connect(self.show_employee_inventory)
        self.employee_dashboard.help_signal.connect(self.show_help_faq)


    def show_login_screen(self):
        self.stacked_widget.setCurrentWidget(self.login_screen)

    def show_admin_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.admin_dashboard)

    def show_admin_maintenance(self):
        self.stacked_widget.setCurrentWidget(self.admin_maintenance)

    def show_admin_maintenance_edit(self):
        self.stacked_widget.setCurrentWidget(self.admin_maintenanceEDIT)

    def show_admin_inventory(self):
        self.stacked_widget.setCurrentWidget(self.admin_inventory)

    def show_admin_inventory_modify(self):
        self.stacked_widget.setCurrentWidget(self.admin_inventoryMODIFY)

    def show_about_devcredits(self):
        self.stacked_widget.setCurrentWidget(self.about_devCredits)

    def show_about_info(self):
        self.stacked_widget.setCurrentWidget(self.about_info)

    def show_help_faq(self):
        self.stacked_widget.setCurrentWidget(self.help_FAQ)

    def show_help_support(self):
        self.stacked_widget.setCurrentWidget(self.help_support)

    def show_user_manual(self):
        self.stacked_widget.setCurrentWidget(self.help_manual)

    def show_change_password(self):
        self.stacked_widget.setCurrentWidget(self.change_password)

    def show_employee_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.employee_dashboard)

    def show_pos_order(self):
        self.stacked_widget.setCurrentWidget(self.pos_order)

    def show_pos_payment(self):
        self.stacked_widget.setCurrentWidget(self.pos_payment)

    def show_pos_menu(self):
        self.stacked_widget.setCurrentWidget(self.pos_table)

    def show_employee_inventory(self):
        self.stacked_widget.setCurrentWidget(self.inventory_modify)

    def show_inventory_barcode(self):
        self.stacked_widget.setCurrentWidget(self.inventory_barcode)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
