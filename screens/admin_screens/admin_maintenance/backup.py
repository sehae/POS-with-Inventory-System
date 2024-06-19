# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/admin_ui/admin_maintenance/backup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 780)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_4.setContentsMargins(25, 25, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.Content)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.automaticbackupLBL = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.automaticbackupLBL.setFont(font)
        self.automaticbackupLBL.setObjectName("automaticbackupLBL")
        self.verticalLayout_5.addWidget(self.automaticbackupLBL)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.frequencyLBL = QtWidgets.QLabel(self.widget)
        self.frequencyLBL.setObjectName("frequencyLBL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frequencyLBL)
        self.frequencyBOX = QtWidgets.QComboBox(self.widget)
        self.frequencyBOX.setMinimumSize(QtCore.QSize(480, 0))
        self.frequencyBOX.setMaximumSize(QtCore.QSize(480, 16777215))
        self.frequencyBOX.setStyleSheet("QComboBox {\n"
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
        self.frequencyBOX.setObjectName("frequencyBOX")
        self.frequencyBOX.addItem("")
        self.frequencyBOX.addItem("")
        self.frequencyBOX.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frequencyBOX)
        self.filelocLBL = QtWidgets.QLabel(self.widget)
        self.filelocLBL.setObjectName("filelocLBL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.filelocLBL)
        self.filelocDISPLAY = QtWidgets.QLabel(self.widget)
        self.filelocDISPLAY.setObjectName("filelocDISPLAY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filelocDISPLAY)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.viewBTN = QtWidgets.QPushButton(self.widget_2)
        self.viewBTN.setMinimumSize(QtCore.QSize(600, 0))
        self.viewBTN.setMaximumSize(QtCore.QSize(600, 16777215))
        self.viewBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
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
        self.viewBTN.setObjectName("viewBTN")
        self.verticalLayout_4.addWidget(self.viewBTN)
        self.selectfolderBTN = QtWidgets.QPushButton(self.widget_2)
        self.selectfolderBTN.setMinimumSize(QtCore.QSize(600, 0))
        self.selectfolderBTN.setMaximumSize(QtCore.QSize(600, 16777215))
        self.selectfolderBTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #67B99A;\n"
"    color: black;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
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
        self.selectfolderBTN.setObjectName("selectfolderBTN")
        self.verticalLayout_4.addWidget(self.selectfolderBTN)
        self.backupnowBTN = QtWidgets.QPushButton(self.widget_2)
        self.backupnowBTN.setMinimumSize(QtCore.QSize(600, 50))
        self.backupnowBTN.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setBold(False)
        self.backupnowBTN.setFont(font)
        self.backupnowBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.backupnowBTN.setObjectName("backupnowBTN")
        self.verticalLayout_4.addWidget(self.backupnowBTN)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lastbackupLBL = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lastbackupLBL.setFont(font)
        self.lastbackupLBL.setStyleSheet("QLabel {\n"
"color: gray;\n"
"}")
        self.lastbackupLBL.setObjectName("lastbackupLBL")
        self.horizontalLayout_3.addWidget(self.lastbackupLBL)
        self.lastbackupDISPLAY = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lastbackupDISPLAY.setFont(font)
        self.lastbackupDISPLAY.setStyleSheet("QLabel {\n"
"color: gray;\n"
"}")
        self.lastbackupDISPLAY.setObjectName("lastbackupDISPLAY")
        self.horizontalLayout_3.addWidget(self.lastbackupDISPLAY)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.verticalLayout_5.addWidget(self.widget_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.restorebackupLBL = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.restorebackupLBL.setFont(font)
        self.restorebackupLBL.setObjectName("restorebackupLBL")
        self.verticalLayout_5.addWidget(self.restorebackupLBL)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.backupDatesBOX = QtWidgets.QComboBox(self.widget_5)
        self.backupDatesBOX.setMinimumSize(QtCore.QSize(600, 0))
        self.backupDatesBOX.setMaximumSize(QtCore.QSize(600, 16777215))
        self.backupDatesBOX.setStyleSheet("QComboBox {\n"
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
        self.backupDatesBOX.setObjectName("backupDatesBOX")
        self.verticalLayout_6.addWidget(self.backupDatesBOX)
        self.restoreBTN = QtWidgets.QPushButton(self.widget_5)
        self.restoreBTN.setMinimumSize(QtCore.QSize(600, 50))
        self.restoreBTN.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setBold(False)
        self.restoreBTN.setFont(font)
        self.restoreBTN.setStyleSheet("QPushButton {\n"
"    background-color: #67B99A;\n"
"    color: white;\n"
"    border: 2px solid #67B99A;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5CAE8B;\n"
"    border: 2px solid #5CAE8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4D9C7F;\n"
"    border: 2px solid #4D9C7F;\n"
"}")
        self.restoreBTN.setObjectName("restoreBTN")
        self.verticalLayout_6.addWidget(self.restoreBTN)
        self.verticalLayout_5.addWidget(self.widget_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_4.addWidget(self.widget_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
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
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
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
        self.automaticbackupLBL.setText(_translate("MainWindow", "Automatic Backup"))
        self.frequencyLBL.setText(_translate("MainWindow", "Backup Frequency"))
        self.frequencyBOX.setItemText(0, _translate("MainWindow", "Hourly"))
        self.frequencyBOX.setItemText(1, _translate("MainWindow", "Daily"))
        self.frequencyBOX.setItemText(2, _translate("MainWindow", "Weekly"))
        self.filelocLBL.setText(_translate("MainWindow", "Backup Location"))
        self.filelocDISPLAY.setText(_translate("MainWindow", "You don\'t have current backup location..."))
        self.viewBTN.setText(_translate("MainWindow", "View Backup Folder"))
        self.selectfolderBTN.setText(_translate("MainWindow", "Select Backup Location"))
        self.backupnowBTN.setText(_translate("MainWindow", "Backup Now"))
        self.lastbackupLBL.setText(_translate("MainWindow", "Last Backup at:"))
        self.lastbackupDISPLAY.setText(_translate("MainWindow", "Put date here"))
        self.restorebackupLBL.setText(_translate("MainWindow", "Restore Backup"))
        self.restoreBTN.setText(_translate("MainWindow", "Restore"))
        self.label.setText(_translate("MainWindow", "MAINTENANCE"))
        self.dateDISPLAY.setText(_translate("MainWindow", "November 28th 2023, 12:07AM"))
        self.usernameDISPLAY.setText(_translate("MainWindow", "Juan Dela Cruz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())