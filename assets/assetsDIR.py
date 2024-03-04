from PyQt5.QtGui import QIcon, QFontDatabase

QUICKSAND_FONT_PATH = "assets/Quicksand-Regular.ttf"
CHANGE_PASS_ICON_PATH = "assets/change_pass.svg"

def load_quicksand_font():
    return QFontDatabase.addApplicationFont(QUICKSAND_FONT_PATH)

def get_navbar_button_icon():
    return QIcon(CHANGE_PASS_ICON_PATH)