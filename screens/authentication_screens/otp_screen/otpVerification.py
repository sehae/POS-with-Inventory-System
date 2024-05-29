# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otpVerification.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import assets.resourceFile_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logoWidget = QtWidgets.QWidget(self.frame)
        self.logoWidget.setObjectName("logoWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logoWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.logoWidget)
        self.logo.setEnabled(True)
        self.logo.setMaximumSize(QtCore.QSize(250, 80))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap(":/logos/Icons/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.verticalLayout_2.addWidget(self.logoWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.instructionLabel = QtWidgets.QLabel(self.frame)
        self.instructionLabel.setMinimumSize(QtCore.QSize(400, 0))
        self.instructionLabel.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setKerning(False)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setTextFormat(QtCore.Qt.AutoText)
        self.instructionLabel.setScaledContents(False)
        self.instructionLabel.setWordWrap(False)
        self.instructionLabel.setIndent(-1)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout_2.addWidget(self.instructionLabel)
        self.userEmail = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.userEmail.setFont(font)
        self.userEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.userEmail.setObjectName("userEmail")
        self.verticalLayout_2.addWidget(self.userEmail)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.OTP = QtWidgets.QFrame(self.frame)
        self.OTP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OTP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OTP.setObjectName("OTP")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.OTP)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.otp1 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otp1.sizePolicy().hasHeightForWidth())
        self.otp1.setSizePolicy(sizePolicy)
        self.otp1.setMinimumSize(QtCore.QSize(50, 50))
        self.otp1.setMaximumSize(QtCore.QSize(50, 50))
        self.otp1.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.otp1.setObjectName("otp1")
        self.horizontalLayout_2.addWidget(self.otp1)
        self.otp2 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otp2.sizePolicy().hasHeightForWidth())
        self.otp2.setSizePolicy(sizePolicy)
        self.otp2.setMinimumSize(QtCore.QSize(50, 50))
        self.otp2.setMaximumSize(QtCore.QSize(50, 50))
        self.otp2.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.otp2.setObjectName("otp2")
        self.horizontalLayout_2.addWidget(self.otp2)
        self.top3 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top3.sizePolicy().hasHeightForWidth())
        self.top3.setSizePolicy(sizePolicy)
        self.top3.setMinimumSize(QtCore.QSize(50, 50))
        self.top3.setMaximumSize(QtCore.QSize(50, 50))
        self.top3.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.top3.setObjectName("top3")
        self.horizontalLayout_2.addWidget(self.top3)
        self.otp4 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otp4.sizePolicy().hasHeightForWidth())
        self.otp4.setSizePolicy(sizePolicy)
        self.otp4.setMinimumSize(QtCore.QSize(50, 50))
        self.otp4.setMaximumSize(QtCore.QSize(50, 50))
        self.otp4.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.otp4.setObjectName("otp4")
        self.horizontalLayout_2.addWidget(self.otp4)
        self.otp5 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otp5.sizePolicy().hasHeightForWidth())
        self.otp5.setSizePolicy(sizePolicy)
        self.otp5.setMinimumSize(QtCore.QSize(50, 50))
        self.otp5.setMaximumSize(QtCore.QSize(50, 50))
        self.otp5.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.otp5.setObjectName("otp5")
        self.horizontalLayout_2.addWidget(self.otp5)
        self.otp6 = QtWidgets.QLineEdit(self.OTP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otp6.sizePolicy().hasHeightForWidth())
        self.otp6.setSizePolicy(sizePolicy)
        self.otp6.setMinimumSize(QtCore.QSize(50, 50))
        self.otp6.setMaximumSize(QtCore.QSize(50, 50))
        self.otp6.setStyleSheet("QLineEdit {\n"
"        border: 2px solid #ADD8E6;\n"
"        border-radius: 5px;\n"
"        padding: 12px;\n"
"        font-size: 16px;\n"
"    }")
        self.otp6.setObjectName("otp6")
        self.horizontalLayout_2.addWidget(self.otp6)
        self.verticalLayout_2.addWidget(self.OTP)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.submitButton = QtWidgets.QPushButton(self.frame)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 56))
        self.submitButton.setMaximumSize(QtCore.QSize(400, 46))
        self.submitButton.setStyleSheet("QPushButton {\n"
"    padding: 5px;\n"
"    border: 1px solid #036666;\n"
"    border-radius: 6px;\n"
"    background-color: #036666;\n"
"    color: white;\n"
"    font-size: 20px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #049393;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #024c4c;\n"
"}")
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout_2.addWidget(self.submitButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.helpLabel = QtWidgets.QLabel(self.frame)
        self.helpLabel.setMinimumSize(QtCore.QSize(400, 0))
        self.helpLabel.setMaximumSize(QtCore.QSize(400, 16777215))
        self.helpLabel.setSizeIncrement(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.helpLabel.setFont(font)
        self.helpLabel.setTextFormat(QtCore.Qt.AutoText)
        self.helpLabel.setScaledContents(False)
        self.helpLabel.setWordWrap(True)
        self.helpLabel.setObjectName("helpLabel")
        self.verticalLayout_2.addWidget(self.helpLabel)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "OTP Verification"))
        self.instructionLabel.setText(_translate("MainWindow", "We will send you a one time password on this e-mail"))
        self.userEmail.setText(_translate("MainWindow", "jcmoonhey@gmail.com"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.helpLabel.setText(_translate("MainWindow", "If you don’t have an account, please coordinate with your manager for registering an account through admin."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())