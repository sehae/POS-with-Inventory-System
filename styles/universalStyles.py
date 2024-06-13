HEADER_TITLE = """
QLabel {
    color: #67B99A;
    font-size: 45px;
    padding: 10px;
}
"""

SYSTEM_LABEL = """
QLabel {
    font-size: 15px;
    padding: 0px;
}
"""

NAVBAR_BUTTON_STYLE = """
QPushButton {
    background-color: #FFFFFF;
    color: black;
    border: 1.3px solid #67B99A;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #E5F7EF;
    border: 1px solid #4D926D;
}
QPushButton:pressed {
    background-color: #C2E1D2;
    border: 1px solid #265C42;
    }
"""

ACTIVE_BUTTON_STYLE = """
QPushButton {
    background-color: #67B99A;
    color: white;
    padding: 8px 16px;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #5CAE8B;
}
QPushButton:pressed {
    background-color: #4D9C7F;
}
"""

INACTIVE_BUTTON_STYLE = """
QPushButton {
    background-color: #9D9D9D;
    color: white;
    padding: 8px 16px;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #7A7A7A;
}
QPushButton:pressed {
    background-color: #666666;
}
"""

ENABLED_RESEND_BTN = """
QPushButton {
    border: none;
    color: #036666;
    background: transparent;
}

QPushButton:hover {
    color: #049393;
}

QPushButton:pressed {
    color: #024c4c;
}
"""

DISABLED_RESEND_BTN = """
QPushButton {
    background-color: transparent;
    color: #A9A9A9;
}
QPushButton:hover {
    border-color: #A9A9A9;
    color: #A9A9A9;
}
QPushButton:pressed {
    border-color: #A9A9A9;
    color: #A9A9A9;
}
"""

COMBOBOX_STYLE = """
QComboBox::down-arrow {
    image: url(assets/Icons/dropdown.png);
    width: 20px;
    height: 20px;
}
QComboBox {
    padding: 5px;
    border: 2px solid #07BEB8;
    border-radius: 6px;
    background-color: #FFFFFF;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: right center;
    width: 20px;
    border-left: none;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}
"""

COMBOBOX_DISABLED_STYLE = """
QComboBox::down-arrow {
    image: url(assets/Icons/dropdown_disabled.png);
    width: 20px;
    height: 20px;
}
QComboBox {
    padding: 5px;
    border: 2px solid #A9A9A9;
    border-radius: 6px;
    background-color: #FFFFFF;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: right center;
    width: 20px;
    border-left: none;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}
"""

COMBOBOX_STYLE_VIEW = """
QAbstractItemView {
    padding: 5px;
    border: 2px solid #07BEB8;
    border-radius: 6px;
    background-color: #FFFFFF;
    selection-background-color: #07BEB8;
}
"""
