# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/admin_ui/admin_inventory/inventorySupplier.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1485, 955)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.header = QtWidgets.QWidget(self.frame)
        self.header.setStyleSheet("QWidget {\n"
"    border-bottom: 3px solid #D8DBD9; \n"
"}\n"
"")
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"    font-size: 45px;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.navbar = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setStyleSheet("QWidget {\n"
"    border-right: 3px solid #D8DBD9;\n"
"}\n"
"")
        self.navbar.setObjectName("navbar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.navbar)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_11 = QtWidgets.QPushButton(self.navbar)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.navbar)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton = QtWidgets.QPushButton(self.navbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.navbar, 1, 0, 1, 1)
        self.Content = QtWidgets.QFrame(self.frame)
        self.Content.setObjectName("Content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Content)
        self.verticalLayout_3.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.Content)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchLBL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.searchLBL.setFont(font)
        self.searchLBL.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.searchLBL.setIndent(0)
        self.searchLBL.setObjectName("searchLBL")
        self.verticalLayout.addWidget(self.searchLBL)
        self.searchFIELD = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFIELD.sizePolicy().hasHeightForWidth())
        self.searchFIELD.setSizePolicy(sizePolicy)
        self.searchFIELD.setMinimumSize(QtCore.QSize(800, 46))
        self.searchFIELD.setMaximumSize(QtCore.QSize(800, 46))
        self.searchFIELD.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.searchFIELD.setObjectName("searchFIELD")
        self.verticalLayout.addWidget(self.searchFIELD)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.Content)
        self.widget_6.setObjectName("widget_6")
        self.formLayout = QtWidgets.QFormLayout(self.widget_6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_13.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_16 = QtWidgets.QLabel(self.widget_6)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_10.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_17 = QtWidgets.QLabel(self.widget_6)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_11.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_18 = QtWidgets.QLabel(self.widget_6)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 3px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 3px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.widget_7)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.Content)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    padding: 5px;\n"
"    border: 2px solid #07BEB8;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px;\n"
"    border-left: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/logos/Icons/gridicons_dropdown.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_7.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_8.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(400, 35))
        self.lineEdit_9.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid #67B99A;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_2.setMinimumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 35))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    padding: 5px;\n"
"    border: 2px solid #07BEB8;\n"
"    border-radius: 6px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px;\n"
"    border-left: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/logos/Icons/gridicons_dropdown.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 3px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 3px 16px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #4D926D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F0F0F0;\n"
"    border: 2px solid #265C42;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.widget_5)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.gridLayout.addWidget(self.Content, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INVENTORY"))
        self.label_2.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.pushButton_11.setText(_translate("MainWindow", "Inventory"))
        self.pushButton_12.setText(_translate("MainWindow", "Supplier"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.searchLBL.setText(_translate("MainWindow", "Search for Supplier"))
        self.label_15.setText(_translate("MainWindow", "Supplier Name"))
        self.label_16.setText(_translate("MainWindow", "Contact Number"))
        self.label_17.setText(_translate("MainWindow", "Email"))
        self.label_18.setText(_translate("MainWindow", "Address"))
        self.pushButton_8.setText(_translate("MainWindow", "Add Supplier"))
        self.pushButton_9.setText(_translate("MainWindow", "Discard"))
        self.label_7.setText(_translate("MainWindow", "Add Supplier"))
        self.label_6.setText(_translate("MainWindow", "Modify Supplier"))
        self.label_10.setText(_translate("MainWindow", "Supplier Name"))
        self.label_11.setText(_translate("MainWindow", "Contact Number"))
        self.label_12.setText(_translate("MainWindow", "Email"))
        self.label_13.setText(_translate("MainWindow", "Address"))
        self.label_14.setText(_translate("MainWindow", "Status"))
        self.pushButton_6.setText(_translate("MainWindow", "Modify Supplier"))
        self.pushButton_7.setText(_translate("MainWindow", "Discard"))
import assets.resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
