# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from runTests import Ui_runTests
from debug2 import Ui_debug2

class Ui_debugFirst(object):
    def openSet(self):  #setupUi as in other program
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_debug2()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        
    def openTests(self):  #setupUi as in other program
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_runTests()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
    def setupUi(self, debugFirst):
        debugFirst.setObjectName("debugFirst")
        debugFirst.resize(480, 800)
        debugFirst.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.settings = QtWidgets.QPushButton(debugFirst)
        self.settings.setGeometry(QtCore.QRect(10, 150, 461, 201))
        self.settings.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 36pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.settings.setAutoDefault(False)
        self.settings.setDefault(True)
        self.settings.setFlat(False)
        self.settings.setObjectName("settings")
        self.tests = QtWidgets.QPushButton(debugFirst)
        self.tests.setGeometry(QtCore.QRect(10, 380, 461, 201))
        self.tests.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 36pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.tests.setAutoDefault(False)
        self.tests.setDefault(True)
        self.tests.setFlat(False)
        self.tests.setObjectName("tests")
        self.mainPage = QtWidgets.QPushButton(debugFirst)
        self.mainPage.setGeometry(QtCore.QRect(140, 660, 200, 52))
        self.mainPage.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.mainPage.setAutoDefault(False)
        self.mainPage.setDefault(True)
        self.mainPage.setFlat(False)
        self.mainPage.setObjectName("mainPage")
        self.mainPage.clicked.connect(debugFirst.close)

        self.tests.clicked.connect(self.openTests)#
        self.settings.clicked.connect(self.openSet)#

        self.retranslateUi(debugFirst)
        QtCore.QMetaObject.connectSlotsByName(debugFirst)

    def retranslateUi(self, debugFirst):
        _translate = QtCore.QCoreApplication.translate
        debugFirst.setWindowTitle(_translate("debugFirst", "Dialog"))
        self.settings.setText(_translate("debugFirst", "General settings"))
        self.tests.setText(_translate("debugFirst", "Run tests"))
        self.mainPage.setText(_translate("debugFirst", "Main page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    debugFirst = QtWidgets.QDialog()
    ui = Ui_debugFirst()
    ui.setupUi(debugFirst)
    debugFirst.show()
    sys.exit(app.exec_())

