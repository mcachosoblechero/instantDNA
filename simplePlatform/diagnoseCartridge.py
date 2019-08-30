# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseCartridge.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv
from TestPage import Ui_Dialog


class Ui_cartridgePage(object):
    def sent_data(self):
        """
        f = open("patient.txt", "r+") #opens texts file and stores data to csv file
        lines = f.readlines()
        dic = []
        for line in lines:
            dic.append(line.strip())
        with open('dataFile.csv', 'a+') as f: #this should be a+ to change row
            writer = csv.writer(f)
            writer.writerow(dic)
        """

        self.window=QtWidgets.QDialog() 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.showFullScreen()

    def setupUi(self, cartridgePage):
        cartridgePage.setObjectName("cartridgePage")
        cartridgePage.resize(480, 800)
        cartridgePage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(cartridgePage)
        self.label.setGeometry(QtCore.QRect(50, 110, 370, 360))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(cartridgePage)
        self.label_2.setGeometry(QtCore.QRect(0, 730, 479, 63))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav4.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(cartridgePage)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 221, 61))
        self.label_3.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);")
        self.label_3.setObjectName("label_3")
        self.continue5 = QtWidgets.QPushButton(cartridgePage)
        self.continue5.setGeometry(QtCore.QRect(140, 520, 200, 52))
        self.continue5.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue5.setAutoDefault(False)
        self.continue5.setDefault(True)
        self.continue5.setFlat(False)
        self.continue5.setObjectName("continue5")
        self.continue5.clicked.connect(cartridgePage.close)
        self.continue5.clicked.connect(self.sent_data)

        self.continue5.setAutoDefault(False)
        self.continue5.setDefault(True)
        self.continue5.setFlat(False)
        self.continue5.setObjectName("continue5")
        self.cancel5 = QtWidgets.QPushButton(cartridgePage)
        self.cancel5.setGeometry(QtCore.QRect(140, 600, 200, 52))
        self.cancel5.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.cancel5.setAutoDefault(False)
        self.cancel5.setDefault(True)
        self.cancel5.setFlat(False)
        self.cancel5.setObjectName("cancel5")
        self.cancel5.clicked.connect(cartridgePage.close)

        




        self.retranslateUi(cartridgePage)
        QtCore.QMetaObject.connectSlotsByName(cartridgePage)

    def retranslateUi(self, cartridgePage):
        _translate = QtCore.QCoreApplication.translate
        cartridgePage.setWindowTitle(_translate("cartridgePage", "Dialog"))
        self.label_3.setText(_translate("cartridgePage", "Please insert cartridge!"))
        self.continue5.setText(_translate("cartridgePage", "START TEST"))
        self.cancel5.setText(_translate("cartridgePage", "CANCEL"))

import First_page_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cartridgePage = QtWidgets.QDialog()
    ui = Ui_cartridgePage()
    ui.setupUi(cartridgePage)
    cartridgePage.show()
    sys.exit(app.exec_())

