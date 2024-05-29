from screens.admin_screens.admin_maintenance.maintenanceEDIT import Ui_MainWindow
from setup.connector import conn


class adminMaintenanceEDIT(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.saveBTN.clicked.connect(self.edit_user)
        self.searchFIELD.returnPressed.connect(self.search_user)
        self.userlogsBTN.clicked.connect(self.show_rightcontent)
        self.rightcontent.hide()
        self.edituserCONTENT.hide()

    def edit_user(self):
        print("edit_user method called")

    def search_user(self):
        try:
            search_text = self.searchFIELD.text()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT first_name, last_name, email FROM employee WHERE last_name LIKE %s OR first_name LIKE %s OR email LIKE %s "
                "UNION "
                "SELECT first_name, last_name, email FROM admin WHERE last_name LIKE %s OR first_name LIKE %s OR email LIKE %s",
                (search_text, search_text, search_text, search_text, search_text, search_text)
            )
            results = cursor.fetchall()

            if results:
                for result in results:
                    self.edituserCONTENT.show()
                    self.nameDISPLAY.setText(f"{result[0]} {result[1]}")
                    self.emailDISPLAY.setText(result[2])
        except Exception as e:
            print(f"An error occurred: {e}")


    def show_rightcontent(self):
        self.rightcontent.show()