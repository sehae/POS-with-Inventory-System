import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap

class ImageApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Get the path to the current script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the image inside the 'assets' folder
        image_path = os.path.join(script_dir, '..', 'assets', 'logo1.png')  # Adjust the image file name
        print("Script Directory:", script_dir)
        print("Image Path:", image_path)

        # Create a QPixmap object and load the image
        pixmap = QPixmap(image_path)

        # Create a QLabel and set the pixmap as its content
        label = QLabel(self)
        label.setPixmap(pixmap)

        # Resize the label to fit the image
        label.resize(pixmap.width(), pixmap.height())

        # Set the window size to fit the image
        self.resize(pixmap.width(), pixmap.height())

        self.setWindowTitle('Image Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageApp()
    sys.exit(app.exec_())
