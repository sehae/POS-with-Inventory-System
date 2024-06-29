import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QDateTime, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from screens.help_screen.help_userManual import Ui_MainWindow
from shared.navigation_signal import auth_back
from styles.universalStyles import ACTIVE_BUTTON_STYLE, INACTIVE_BUTTON_STYLE
from server.local_server import conn
from validator.user_manager import userManager

class helpManual(QMainWindow, Ui_MainWindow):
    back_signal = pyqtSignal()
    back_kitchen_signal = pyqtSignal()
    back_cashier_signal = pyqtSignal()
    faq_signal = pyqtSignal()
    support_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.zoom_level = 1.0

        self.backButton.clicked.connect(lambda: auth_back(self.user_manager, self.back_signal,
                                                          self.back_kitchen_signal, self.back_cashier_signal))
        self.addUserButton.clicked.connect(self.faq_signal.emit)
        self.pushButton.clicked.connect(self.support_signal.emit)

        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        layout = QVBoxLayout(self.pdfViewerPlaceholder)
        layout.addWidget(self.web_view)

        self.pdf_path = os.path.abspath("User_Manual.pdf")

        if self.pdf_path:
            if os.path.isfile(self.pdf_path):
                self.web_view.setUrl(QtCore.QUrl.fromLocalFile(self.pdf_path))
            else:
                print(f"Error: File not found: {self.pdf_path}")

        self.zoomin.clicked.connect(self.zoom_in)
        self.zoomout.clicked.connect(self.zoom_out)

        # Create an instance of userManager
        self.user_manager = userManager()

        # Create a QTimer object
        self.timer = QTimer()

        # Connect the timeout signal of the timer to the updateDateTime slot
        self.timer.timeout.connect(self.updateDateTime)

        # Set the interval for the timer (in milliseconds)
        self.timer.start(1000)  # Update every second

    def execute_zoom_script(self):
        script = f"""
            var embed = document.querySelector('embed');
            embed.style.transform = 'scale({self.zoom_level})';
            embed.style.transformOrigin = '50% 50%';
        """
        self.web_view.page().runJavaScript(script)

    def zoom_in(self):
        self.zoom_level += 0.1
        self.execute_zoom_script()

    def zoom_out(self):
        self.zoom_level -= 0.1
        self.execute_zoom_script()

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Format the date and time together as desired
        formattedDateTime = currentDateTime.toString("MMMM d, yyyy, hh:mm:ss AP")

        # Set the text of dateLabel to the formatted date and time
        self.sysTimeDate.setText(formattedDateTime)
