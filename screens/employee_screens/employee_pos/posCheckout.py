# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'posCheckout.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1801, 761)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.navbar_2 = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navbar_2.sizePolicy().hasHeightForWidth())
        self.navbar_2.setSizePolicy(sizePolicy)
        self.navbar_2.setStyleSheet("QWidget {\n"
"    border-right: 3px solid #D8DBD9;\n"
"}\n"
"")
        self.navbar_2.setObjectName("navbar_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.navbar_2)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.orderBTN = QtWidgets.QPushButton(self.navbar_2)
        self.orderBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.orderBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.orderBTN.setStyleSheet("QPushButton {\n"
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
        self.orderBTN.setObjectName("orderBTN")
        self.verticalLayout_6.addWidget(self.orderBTN)
        self.menuBTN = QtWidgets.QPushButton(self.navbar_2)
        self.menuBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.menuBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.menuBTN.setStyleSheet("QPushButton {\n"
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
        self.menuBTN.setObjectName("menuBTN")
        self.verticalLayout_6.addWidget(self.menuBTN)
        self.modifyBTN = QtWidgets.QPushButton(self.navbar_2)
        self.modifyBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.modifyBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.modifyBTN.setStyleSheet("QPushButton {\n"
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
        self.modifyBTN.setObjectName("modifyBTN")
        self.verticalLayout_6.addWidget(self.modifyBTN)
        self.checkoutBTN = QtWidgets.QPushButton(self.navbar_2)
        self.checkoutBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.checkoutBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.checkoutBTN.setStyleSheet("QPushButton {\n"
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
        self.checkoutBTN.setObjectName("checkoutBTN")
        self.verticalLayout_6.addWidget(self.checkoutBTN)
        self.historyBTN_2 = QtWidgets.QPushButton(self.navbar_2)
        self.historyBTN_2.setMinimumSize(QtCore.QSize(100, 100))
        self.historyBTN_2.setMaximumSize(QtCore.QSize(100, 100))
        self.historyBTN_2.setStyleSheet("QPushButton {\n"
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
        self.historyBTN_2.setObjectName("historyBTN_2")
        self.verticalLayout_6.addWidget(self.historyBTN_2)
        self.backBTN = QtWidgets.QPushButton(self.navbar_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBTN.sizePolicy().hasHeightForWidth())
        self.backBTN.setSizePolicy(sizePolicy)
        self.backBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.backBTN.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backBTN.setFont(font)
        self.backBTN.setStyleSheet("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Icons/entypo_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBTN.setIcon(icon)
        self.backBTN.setAutoRepeat(False)
        self.backBTN.setObjectName("backBTN")
        self.verticalLayout_6.addWidget(self.backBTN)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.navbar_2, 1, 0, 1, 1)
        self.header_2 = QtWidgets.QWidget(self.frame)
        self.header_2.setStyleSheet("QWidget {\n"
"    border-bottom: 3px solid #D8DBD9; \n"
"}\n"
"")
        self.header_2.setObjectName("header_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.header_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"    font-size: 45px;\n"
"}")
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.frame_3 = QtWidgets.QFrame(self.header_2)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.gridLayout_2.addWidget(self.header_2, 0, 0, 1, 2)
        self.contentContainer_2 = QtWidgets.QFrame(self.frame)
        self.contentContainer_2.setObjectName("contentContainer_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.contentContainer_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainContent_2 = QtWidgets.QWidget(self.contentContainer_2)
        self.mainContent_2.setObjectName("mainContent_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.mainContent_2)
        self.horizontalLayout_6.setContentsMargins(25, 25, 50, 25)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leftContent_2 = QtWidgets.QWidget(self.mainContent_2)
        self.leftContent_2.setMinimumSize(QtCore.QSize(1000, 0))
        self.leftContent_2.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.leftContent_2.setObjectName("leftContent_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.leftContent_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_2 = QtWidgets.QWidget(self.leftContent_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 30))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.widget_11 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_10.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_9.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_11.setMaximumSize(QtCore.QSize(200, 35))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_9.addWidget(self.pushButton_11)
        spacerItem3 = QtWidgets.QSpacerItem(58, 32, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_7.addWidget(self.widget_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel {\n"
"    color: #67B99A;\n"
"}")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.verticalLayout_9.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.leftContent_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setContentsMargins(100, 25, 100, 25)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget)
        spacerItem5 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem5)
        self.verticalLayout_9.addWidget(self.widget_3)
        self.horizontalLayout_6.addWidget(self.leftContent_2)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.rightContent_2 = QtWidgets.QWidget(self.mainContent_2)
        self.rightContent_2.setObjectName("rightContent_2")
        self.widget_4 = QtWidgets.QWidget(self.rightContent_2)
        self.widget_4.setGeometry(QtCore.QRect(9, 9, 76, 24))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.widget_8 = QtWidgets.QWidget(self.rightContent_2)
        self.widget_8.setGeometry(QtCore.QRect(9, 39, 334, 54))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_22 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_13.addWidget(self.label_22)
        self.widget_7 = QtWidgets.QWidget(self.widget_8)
        self.widget_7.setStyleSheet("QWidget {\n"
"    background-color: #C4FFF9;\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.verticalLayout_13.addWidget(self.widget_7)
        self.widget_10 = QtWidgets.QWidget(self.rightContent_2)
        self.widget_10.setGeometry(QtCore.QRect(9, 99, 296, 54))
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_24 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_14.addWidget(self.label_24)
        self.widget_9 = QtWidgets.QWidget(self.widget_10)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_23 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_11.addWidget(self.label_23)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_11.addWidget(self.lineEdit_2)
        self.verticalLayout_14.addWidget(self.widget_9)
        self.pushButton_2 = QtWidgets.QPushButton(self.rightContent_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 360, 371, 75))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #99E2B4;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7FD69E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #66B97E;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.rightContent_2)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 391, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 50, 361, 77))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_14.addWidget(self.label_30)
        spacerItem7 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 75))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #07BEB8;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #06AFA8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #059A96;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_14.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 75, 25))
        self.pushButton.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_29 = QtWidgets.QLabel(self.frame_2)
        self.label_29.setGeometry(QtCore.QRect(11, 11, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(80, 10, 200, 25))
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_6.addWidget(self.rightContent_2)
        self.verticalLayout_8.addWidget(self.mainContent_2)
        self.gridLayout_2.addWidget(self.contentContainer_2, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orderBTN.setText(_translate("MainWindow", "Order"))
        self.menuBTN.setText(_translate("MainWindow", "Menu"))
        self.modifyBTN.setText(_translate("MainWindow", "Modify"))
        self.checkoutBTN.setText(_translate("MainWindow", "Checkout"))
        self.historyBTN_2.setText(_translate("MainWindow", "History"))
        self.backBTN.setText(_translate("MainWindow", "Back"))
        self.label_10.setText(_translate("MainWindow", "POS"))
        self.label_11.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.label_12.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.label_13.setText(_translate("MainWindow", "ORDER #:"))
        self.pushButton_10.setText(_translate("MainWindow", "Checkout"))
        self.pushButton_11.setText(_translate("MainWindow", "Discard"))
        self.label_19.setText(_translate("MainWindow", "RECEIPT"))
        self.label_22.setText(_translate("MainWindow", "PAID IN CASH"))
        self.label_21.setText(_translate("MainWindow", "ADD CASH"))
        self.label_24.setText(_translate("MainWindow", "PAID IN E-WALLET"))
        self.label_23.setText(_translate("MainWindow", "ENTER REFERENCE #"))
        self.pushButton_2.setText(_translate("MainWindow", "PAY NOW"))
        self.label_30.setText(_translate("MainWindow", "DISCOUNT"))
        self.pushButton_5.setText(_translate("MainWindow", "PWD/ELDER"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
        self.label_29.setText(_translate("MainWindow", "LEFTOVER (Grams)"))
import assets.resourceFile_rc
