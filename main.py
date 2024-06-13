import sys
from PyQt5 import QtWidgets

from screens.authentication_screens.login_screen.login_functions import myLoginScreen
from screens.admin_screens.admin_dashboard.adminDashboard_functions import myAdminDashboard
from screens.admin_screens.admin_maintenance.m_ADDuser_functions import adminMaintenance
from screens.admin_screens.admin_maintenance.m_EDITuser_functions import adminMaintenanceEDIT
from screens.admin_screens.admin_inventory.inventoryAddProduct_functions import adminInventoryAddProduct
from screens.admin_screens.admin_inventory.inventoryModify_functions import adminInventoryModifyProduct
from screens.about_screen.about_devCredits_functions import aboutdevCredits
from screens.about_screen.about_Info_functions import aboutInfo
from screens.help_screen.help_FAQ_functions import helpFAQ
from screens.help_screen.help_support_functions import helpSupport
from screens.help_screen.help_usermanual_functions import helpManual
from screens.password_screen.changePassword_functions import changePassword
from screens.employee_screens.employee_dashboard.employeeDashboard_functions import myEmployeeDashboard
from screens.employee_screens.employee_pos.posOrder_functions import posOrder
from screens.employee_screens.employee_pos.posPayment_functions import posPayment
from screens.employee_screens.employee_pos.posTable_functions import posTable
from screens.employee_screens.employee_inventory.inventory_Modify_functions import inventoryModify
from screens.employee_screens.employee_inventory.inventory_Barcode_functions import inventoryBarcode
from screens.employee_screens.employee_inventory.inventory_Table_functions import inventoryTable
from screens.admin_screens.admin_inventory.inventoryViewProduct_functions import adminInventoryViewProduct

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
        self.inventory_table = inventoryTable()
        self.inventory_view = adminInventoryViewProduct()

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
        self.stacked_widget.addWidget(self.inventory_table)
        self.stacked_widget.addWidget(self.inventory_view)

        self.admin_inventoryMODIFY.view_signal.connect(self.show_view_product)
        self.admin_inventory.view_signal.connect(self.show_view_product)
        self.inventory_view.back_signal.connect(self.show_admin_dashboard)
        self.inventory_view.modify_signal.connect(self.show_admin_inventory_modify)
        self.inventory_view.add_signal.connect(self.show_admin_inventory)
        self.inventory_modify.inventory_table.connect(self.show_inventory_table)
        self.inventory_barcode.inventory_table.connect(self.show_inventory_table)
        self.inventory_table.back_signal.connect(self.show_employee_dashboard)
        self.inventory_table.modify_signal.connect(self.show_employee_inventory)
        self.inventory_table.barcode_signal.connect(self.show_inventory_barcode)
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

        self.help_manual.back_employee_signal.connect(self.show_employee_dashboard)
        self.help_support.back_employee_signal.connect(self.show_employee_dashboard)

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

        self.employee_dashboard.about_signal.connect(self.show_about_devcredits)
        self.about_devCredits.back_employee_signal.connect(self.show_employee_dashboard)
        self.about_info.back_employee_signal.connect(self.show_employee_dashboard)
        self.employee_dashboard.changepass_signal.connect(self.show_change_password)
        self.change_password.back_employee_signal.connect(self.show_employee_dashboard)

        # Ensure the inventoryTable instance uses the inventoryModify instance from MainWindow
        self.inventory_table.inventory_modify = self.inventory_modify
        self.inventory_modify.product_update_signal.connect(self.inventory_table.populate_table)

        # Repopulate table
        self.inventory_view.admin_inventoryMODIFY = self.admin_inventoryMODIFY
        self.admin_inventoryMODIFY.product_update_signal.connect(self.inventory_view.populate_table)

        # Repopulate admin inventory table from modification changes by employee
        self.inventory_view.inventory_modify = self.inventory_modify
        self.inventory_modify.employee_update_signal.connect(self.inventory_view.populate_table)

        # Repopulate table from inventoryAddProduct
        self.inventory_view.admin_inventory = self.admin_inventory
        self.admin_inventory.product_update_signal.connect(self.inventory_view.populate_table)

        # Repopulate table from modify changes in admin to employee
        self.inventory_table.admin_inventoryMODIFY = self.admin_inventoryMODIFY
        self.admin_inventoryMODIFY.admin_product_update_signal.connect(self.inventory_table.populate_table)

        # Repopulate table from add changes in admin to employee
        self.inventory_table.admin_inventory = self.admin_inventory
        self.admin_inventory.admin_product_update_signal.connect(self.inventory_table.populate_table)


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

    def show_inventory_table(self):
        self.stacked_widget.setCurrentWidget(self.inventory_table)

    def show_view_product(self):
        self.stacked_widget.setCurrentWidget(self.inventory_view)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
