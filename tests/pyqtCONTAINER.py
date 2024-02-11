from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class GUIApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python GUI")

        # Create a layout as a container
        self.container_layout = QVBoxLayout(self)

        # Create buttons inside the container layout
        self.button1 = QPushButton("Button 1")
        self.container_layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.container_layout.addWidget(self.button2)

        self.button3 = QPushButton("Button 3")
        self.container_layout.addWidget(self.button3)

if __name__ == "__main__":
    app = QApplication([])
    window = GUIApp()
    window.show()
    app.exec_()
