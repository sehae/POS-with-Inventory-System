# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/admin_ui/admin_maintenance/maintenanceEDIT.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1802, 834)
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
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.adduserBTN = QtWidgets.QPushButton(self.navbar)
        self.adduserBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.adduserBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.adduserBTN.setStyleSheet("QPushButton {\n"
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
        self.adduserBTN.setObjectName("adduserBTN")
        self.verticalLayout_2.addWidget(self.adduserBTN)
        self.editBTN = QtWidgets.QPushButton(self.navbar)
        self.editBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.editBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.editBTN.setStyleSheet("QPushButton {\n"
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
        self.editBTN.setObjectName("editBTN")
        self.verticalLayout_2.addWidget(self.editBTN)
        self.backupBTN = QtWidgets.QPushButton(self.navbar)
        self.backupBTN.setMinimumSize(QtCore.QSize(100, 100))
        self.backupBTN.setMaximumSize(QtCore.QSize(100, 100))
        self.backupBTN.setStyleSheet("QPushButton {\n"
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
        self.backupBTN.setObjectName("backupBTN")
        self.verticalLayout_2.addWidget(self.backupBTN)
        self.backBTN = QtWidgets.QPushButton(self.navbar)
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
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/entypo_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBTN.setIcon(icon)
        self.backBTN.setAutoRepeat(False)
        self.backBTN.setObjectName("backBTN")
        self.verticalLayout_2.addWidget(self.backBTN)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.navbar, 1, 0, 1, 1)
        self.Content = QtWidgets.QWidget(self.frame)
        self.Content.setObjectName("Content")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.leftcontent = QtWidgets.QWidget(self.Content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftcontent.sizePolicy().hasHeightForWidth())
        self.leftcontent.setSizePolicy(sizePolicy)
        self.leftcontent.setObjectName("leftcontent")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftcontent)
        self.verticalLayout_3.setContentsMargins(15, 15, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchLBL = QtWidgets.QLabel(self.leftcontent)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.searchLBL.setFont(font)
        self.searchLBL.setObjectName("searchLBL")
        self.verticalLayout_3.addWidget(self.searchLBL)
        self.searchFIELD = QtWidgets.QLineEdit(self.leftcontent)
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
        self.verticalLayout_3.addWidget(self.searchFIELD)
        self.edituserCONTENT = QtWidgets.QFrame(self.leftcontent)
        self.edituserCONTENT.setObjectName("edituserCONTENT")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.edituserCONTENT)
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem2)
        self.edituserLBL = QtWidgets.QLabel(self.edituserCONTENT)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edituserLBL.setFont(font)
        self.edituserLBL.setObjectName("edituserLBL")
        self.verticalLayout_7.addWidget(self.edituserLBL)
        self.frameBox = QtWidgets.QFrame(self.edituserCONTENT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBox.sizePolicy().hasHeightForWidth())
        self.frameBox.setSizePolicy(sizePolicy)
        self.frameBox.setMinimumSize(QtCore.QSize(800, 0))
        self.frameBox.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frameBox.setStyleSheet("QFrame {\n"
"    border: 2px solid #07BEB8;\n"
"    border-radius: 6px;\n"
"}")
        self.frameBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameBox.setLineWidth(0)
        self.frameBox.setObjectName("frameBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameBox)
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.contents = QtWidgets.QWidget(self.frameBox)
        self.contents.setStyleSheet("")
        self.contents.setObjectName("contents")
        self.formLayout = QtWidgets.QFormLayout(self.contents)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 50, 0)
        self.formLayout.setSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.nameLBL = QtWidgets.QLabel(self.contents)
        self.nameLBL.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.nameLBL.setObjectName("nameLBL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLBL)
        self.nameDISPLAY = QtWidgets.QLabel(self.contents)
        self.nameDISPLAY.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.nameDISPLAY.setObjectName("nameDISPLAY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameDISPLAY)
        self.emailLBL = QtWidgets.QLabel(self.contents)
        self.emailLBL.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.emailLBL.setObjectName("emailLBL")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.emailLBL)
        self.emailDISPLAY = QtWidgets.QLabel(self.contents)
        self.emailDISPLAY.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.emailDISPLAY.setObjectName("emailDISPLAY")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.emailDISPLAY)
        self.loaLBL = QtWidgets.QLabel(self.contents)
        self.loaLBL.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.loaLBL.setObjectName("loaLBL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.loaLBL)
        self.loaBUTTONGRP = QtWidgets.QWidget(self.contents)
        self.loaBUTTONGRP.setObjectName("loaBUTTONGRP")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.loaBUTTONGRP)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.staffBTN = QtWidgets.QPushButton(self.loaBUTTONGRP)
        self.staffBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"}")
        self.staffBTN.setObjectName("staffBTN")
        self.horizontalLayout_3.addWidget(self.staffBTN)
        self.adminBTN = QtWidgets.QPushButton(self.loaBUTTONGRP)
        self.adminBTN.setStyleSheet("QPushButton {\n"
"    background-color: #9D9D9D;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7A7A7A;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.adminBTN.setObjectName("adminBTN")
        self.horizontalLayout_3.addWidget(self.adminBTN)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.loaBUTTONGRP)
        self.restrictionLBL = QtWidgets.QLabel(self.contents)
        self.restrictionLBL.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.restrictionLBL.setObjectName("restrictionLBL")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.restrictionLBL)
        self.restrictionBUTTONGRP = QtWidgets.QWidget(self.contents)
        self.restrictionBUTTONGRP.setObjectName("restrictionBUTTONGRP")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.restrictionBUTTONGRP)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cashierBTN = QtWidgets.QPushButton(self.restrictionBUTTONGRP)
        self.cashierBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"}")
        self.cashierBTN.setObjectName("cashierBTN")
        self.horizontalLayout_4.addWidget(self.cashierBTN)
        self.kitchenBTN = QtWidgets.QPushButton(self.restrictionBUTTONGRP)
        self.kitchenBTN.setStyleSheet("QPushButton {\n"
"    background-color: #9D9D9D;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7A7A7A;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}")
        self.kitchenBTN.setObjectName("kitchenBTN")
        self.horizontalLayout_4.addWidget(self.kitchenBTN)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.restrictionBUTTONGRP)
        self.actionsLBL = QtWidgets.QLabel(self.contents)
        self.actionsLBL.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.actionsLBL.setObjectName("actionsLBL")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.actionsLBL)
        self.actionsBUTTONGRP = QtWidgets.QWidget(self.contents)
        self.actionsBUTTONGRP.setObjectName("actionsBUTTONGRP")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.actionsBUTTONGRP)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.userlogsBTN = QtWidgets.QPushButton(self.actionsBUTTONGRP)
        self.userlogsBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"}")
        self.userlogsBTN.setObjectName("userlogsBTN")
        self.horizontalLayout_5.addWidget(self.userlogsBTN)
        self.deactBTN = QtWidgets.QPushButton(self.actionsBUTTONGRP)
        self.deactBTN.setStyleSheet("QPushButton {\n"
"    background-color: #EE1C1C;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FF4545;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #CC0000;\n"
"}")
        self.deactBTN.setObjectName("deactBTN")
        self.horizontalLayout_5.addWidget(self.deactBTN)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.actionsBUTTONGRP)
        self.verticalLayout_6.addWidget(self.contents)
        self.buttons = QtWidgets.QWidget(self.frameBox)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_6.setContentsMargins(0, 25, 50, 25)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.saveBTN = QtWidgets.QPushButton(self.buttons)
        self.saveBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    padding: 8px 16px;\n"
"    border-radius: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"}")
        self.saveBTN.setObjectName("saveBTN")
        self.horizontalLayout_6.addWidget(self.saveBTN)
        self.discardBTN = QtWidgets.QPushButton(self.buttons)
        self.discardBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    color: #858D9D;\n"
"    border: 2px solid #F0F1F3;\n"
"    padding: 8px 16px;\n"
"    border-radius: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F1F3;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #D9D9D9;\n"
"    border-color: #BEC3C9;\n"
"}\n"
"")
        self.discardBTN.setObjectName("discardBTN")
        self.horizontalLayout_6.addWidget(self.discardBTN)
        self.verticalLayout_6.addWidget(self.buttons)
        self.verticalLayout_7.addWidget(self.frameBox)
        self.verticalLayout_3.addWidget(self.edituserCONTENT)
        self.errorLBL = QtWidgets.QLabel(self.leftcontent)
        self.errorLBL.setStyleSheet("QLabel {\n"
"color: red;\n"
"}")
        self.errorLBL.setObjectName("errorLBL")
        self.verticalLayout_3.addWidget(self.errorLBL)
        self.userRESULTS = QtWidgets.QTableWidget(self.leftcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userRESULTS.sizePolicy().hasHeightForWidth())
        self.userRESULTS.setSizePolicy(sizePolicy)
        self.userRESULTS.setMinimumSize(QtCore.QSize(800, 0))
        self.userRESULTS.setMaximumSize(QtCore.QSize(800, 16777215))
        self.userRESULTS.setObjectName("userRESULTS")
        self.userRESULTS.setColumnCount(0)
        self.userRESULTS.setRowCount(0)
        self.verticalLayout_3.addWidget(self.userRESULTS)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_7.addWidget(self.leftcontent)
        self.rightcontent = QtWidgets.QFrame(self.Content)
        self.rightcontent.setObjectName("rightcontent")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rightcontent)
        self.verticalLayout_5.setContentsMargins(25, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.userlogsLBL = QtWidgets.QLabel(self.rightcontent)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userlogsLBL.setFont(font)
        self.userlogsLBL.setObjectName("userlogsLBL")
        self.verticalLayout_5.addWidget(self.userlogsLBL)
        self.logTABLE = QtWidgets.QTableWidget(self.rightcontent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTABLE.sizePolicy().hasHeightForWidth())
        self.logTABLE.setSizePolicy(sizePolicy)
        self.logTABLE.setMinimumSize(QtCore.QSize(800, 0))
        self.logTABLE.setMaximumSize(QtCore.QSize(800, 16777215))
        self.logTABLE.setObjectName("logTABLE")
        self.logTABLE.setColumnCount(3)
        self.logTABLE.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.logTABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTABLE.setItem(0, 0, item)
        self.logTABLE.horizontalHeader().setDefaultSectionSize(200)
        self.logTABLE.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.logTABLE)
        self.horizontalLayout_7.addWidget(self.rightcontent)
        self.gridLayout.addWidget(self.Content, 1, 1, 1, 1)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateDISPLAY = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateDISPLAY.setFont(font)
        self.dateDISPLAY.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.dateDISPLAY.setObjectName("dateDISPLAY")
        self.verticalLayout.addWidget(self.dateDISPLAY)
        self.usernameDISPLAY = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameDISPLAY.setFont(font)
        self.usernameDISPLAY.setStyleSheet("QLabel {\n"
"    color: black;\n"
"}")
        self.usernameDISPLAY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameDISPLAY.setObjectName("usernameDISPLAY")
        self.verticalLayout.addWidget(self.usernameDISPLAY)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adduserBTN.setText(_translate("MainWindow", "Add User"))
        self.editBTN.setText(_translate("MainWindow", "Edit User"))
        self.backupBTN.setText(_translate("MainWindow", "Backup"))
        self.backBTN.setText(_translate("MainWindow", "Back"))
        self.searchLBL.setText(_translate("MainWindow", "Search for User"))
        self.edituserLBL.setText(_translate("MainWindow", "Edit User"))
        self.nameLBL.setText(_translate("MainWindow", "Name:"))
        self.nameDISPLAY.setText(_translate("MainWindow", "Juan Dela Cruz"))
        self.emailLBL.setText(_translate("MainWindow", "E-mail:"))
        self.emailDISPLAY.setText(_translate("MainWindow", "jcmoonhey@gmail.com"))
        self.loaLBL.setText(_translate("MainWindow", "Level of Acces:"))
        self.staffBTN.setText(_translate("MainWindow", "Staff"))
        self.adminBTN.setText(_translate("MainWindow", "Admin"))
        self.restrictionLBL.setText(_translate("MainWindow", "Restriction:"))
        self.cashierBTN.setText(_translate("MainWindow", "Cashier"))
        self.kitchenBTN.setText(_translate("MainWindow", "Kitchen"))
        self.actionsLBL.setText(_translate("MainWindow", "Other Actions:"))
        self.userlogsBTN.setText(_translate("MainWindow", "User Logs"))
        self.deactBTN.setText(_translate("MainWindow", "Deactivate"))
        self.saveBTN.setText(_translate("MainWindow", "Save Changes"))
        self.discardBTN.setText(_translate("MainWindow", "Discard"))
        self.errorLBL.setText(_translate("MainWindow", "Error Label"))
        self.userlogsLBL.setText(_translate("MainWindow", "User Logs"))
        item = self.logTABLE.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.logTABLE.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.logTABLE.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Action"))
        __sortingEnabled = self.logTABLE.isSortingEnabled()
        self.logTABLE.setSortingEnabled(False)
        self.logTABLE.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "MAINTENANCE"))
        self.dateDISPLAY.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.usernameDISPLAY.setText(_translate("MainWindow", "Juan Dela Cruz"))
import assets.resourceFile_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
