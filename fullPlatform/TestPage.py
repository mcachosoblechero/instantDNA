# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 800)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nurse = QtWidgets.QLabel(Dialog)
        self.nurse.setGeometry(QtCore.QRect(60, 70, 350, 250))
        self.nurse.setText("")
        self.nurse.setPixmap(QtGui.QPixmap(":/newPrefix/doctor3.png"))
        self.nurse.setScaledContents(True)
        self.nurse.setObjectName("nurse")
        self.textLabel = QtWidgets.QLabel(Dialog)
        self.textLabel.setGeometry(QtCore.QRect(190, 90, 211, 41))
        self.textLabel.setStyleSheet("background-color: transparent;")
        self.textLabel.setText("")
        self.textLabel.setObjectName("textLabel")
        
        self.continue2 = QtWidgets.QPushButton(Dialog)
        self.continue2.setGeometry(QtCore.QRect(140, 630, 200, 52))
        self.continue2.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue2.setAutoDefault(False)
        self.continue2.setDefault(True)
        self.continue2.setFlat(False)
        self.continue2.setObjectName("continue2")

        self.continue2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.list1 = list1
        self.counter = 0
        self.len = len(self.list1)

        timer = QtCore.QTimer(Dialog)
        timer.timeout.connect(self.show_text)
        timer.start(350)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def show_text(self):
        if self.counter == 6:
            time.sleep(2)
        if self.counter == 11:
            time.sleep(2)
        if self.counter == 18:
            time.sleep(2)
        if self.counter == 27:
            time.sleep(2)
        if self.counter >= self.len:
            return
            #time.sleep(7)
            #self.counter = 0
        self.textLabel.setText(str(self.list1[self.counter]))
        self.counter += 1

list1 = ["Ini", "Initial", "Initialising", "Initialising pla", "Initialising platf",
         "Initialising platform", " ", "Fir", "Firing", "Firing IS", "Firing ISFETs", " ",
         "Amp", "Ampli", "Amplifyi", "Amplifying", "Amplifying D", "Amplifying DNA", " ",
         "Det", "Detec", "Detecting", "Detecting cha", "Detecting chang", "Detecting changes",
         "Detecting changes in", "Detecting changes in pH", " ",
         "Pre", "Prepar", "Preparing", "Preparing dia", "Preparing diagno", "Preparing diagnosis"]

import Test_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

