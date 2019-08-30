# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseSymptoms.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from diagnoseCartridge import Ui_cartridgePage
from datetime import date

class Ui_fourthPage(object):
    def open5(self):
         self.window=QtWidgets.QDialog() 
         self.ui = Ui_cartridgePage()
         self.ui.setupUi(self.window) #setupUi as in other program
         self.window.showFullScreen()

         symptoms= []

         if self.cough.isChecked():
              symptoms.append("cough")
         if self.diarrhea.isChecked():
              symptoms.append("diarrhea")
         if self.dizziness.isChecked():
              symptoms.append("dizziness")
         if self.fatigue.isChecked():
              symptoms.append("fatigue")
         if self.fever.isChecked():
              symptoms.append("fever")
         if self.headache.isChecked():
              symptoms.append("headache")
         if self.nausea.isChecked():
              symptoms.append("nausea")
         if self.cramp.isChecked():
              symptoms.append("muscle cramp")

         additional = str(self.lineEdit.text())

         if len(additional) == 0:
                pass
         else:
             symptoms.append(additional)

         f = open("patient.txt", "a+")

         for data in symptoms:
             f.write(data + " ")

         f.write("\n")
         f.write(str(date.today())) #new code to also include the date

    def setupUi(self, fourthPage):
        fourthPage.setObjectName("fourthPage")
        fourthPage.resize(480, 801)
        fourthPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(fourthPage)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 421, 71))
        self.label_5.setStyleSheet("background-color: transparent;\n"
"font: 36pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.label_5.setObjectName("label_5")
        self.cough = QtWidgets.QPushButton(fourthPage)
        self.cough.setGeometry(QtCore.QRect(50, 130, 165, 80))
        self.cough.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"")
        self.cough.setCheckable(True)
        self.cough.setAutoDefault(False)
        self.cough.setDefault(True)
        self.cough.setObjectName("cough")
        self.dizziness = QtWidgets.QPushButton(fourthPage)
        self.dizziness.setGeometry(QtCore.QRect(50, 230, 165, 80))
        self.dizziness.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.dizziness.setCheckable(True)
        self.dizziness.setAutoDefault(False)
        self.dizziness.setDefault(True)
        self.dizziness.setObjectName("dizziness")
        self.fever = QtWidgets.QPushButton(fourthPage)
        self.fever.setGeometry(QtCore.QRect(50, 330, 165, 80))
        self.fever.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.fever.setCheckable(True)
        self.fever.setAutoDefault(False)
        self.fever.setDefault(True)
        self.fever.setObjectName("fever")
        self.diarrhea = QtWidgets.QPushButton(fourthPage)
        self.diarrhea.setGeometry(QtCore.QRect(260, 130, 165, 80))
        self.diarrhea.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.diarrhea.setCheckable(True)
        self.diarrhea.setAutoDefault(False)
        self.diarrhea.setDefault(True)
        self.diarrhea.setObjectName("diarrhea")
        self.fatigue = QtWidgets.QPushButton(fourthPage)
        self.fatigue.setGeometry(QtCore.QRect(260, 230, 165, 80))
        self.fatigue.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.fatigue.setCheckable(True)
        self.fatigue.setAutoDefault(False)
        self.fatigue.setDefault(True)
        self.fatigue.setObjectName("fatigue")
        self.headache = QtWidgets.QPushButton(fourthPage)
        self.headache.setGeometry(QtCore.QRect(260, 330, 165, 80))
        self.headache.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.headache.setCheckable(True)
        self.headache.setAutoDefault(False)
        self.headache.setDefault(True)
        self.headache.setObjectName("headache")
        self.label_6 = QtWidgets.QLabel(fourthPage)
        self.label_6.setGeometry(QtCore.QRect(50, 525, 371, 41))
        self.label_6.setStyleSheet("background-color: transparent;\n"
"font: 18pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.label_6.setObjectName("label_6")
        self.nausea = QtWidgets.QPushButton(fourthPage)
        self.nausea.setGeometry(QtCore.QRect(50, 430, 165, 80))
        self.nausea.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.nausea.setCheckable(True)
        self.nausea.setAutoDefault(False)
        self.nausea.setDefault(True)
        self.nausea.setObjectName("nausea")
        self.cramp = QtWidgets.QPushButton(fourthPage)
        self.cramp.setGeometry(QtCore.QRect(260, 430, 165, 80))
        self.cramp.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"font: 16pt \"Arial Rounded MT Bold\";")
        self.cramp.setCheckable(True)
        self.cramp.setAutoDefault(False)
        self.cramp.setDefault(True)
        self.cramp.setObjectName("cramp")
        self.label = QtWidgets.QLabel(fourthPage)
        self.label.setGeometry(QtCore.QRect(0, 730, 479, 63))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/nav3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.continue4 = QtWidgets.QPushButton(fourthPage)
        self.continue4.setGeometry(QtCore.QRect(140, 630, 200, 52))
        self.continue4.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue4.setAutoDefault(False)
        self.continue4.setDefault(True)
        self.continue4.setFlat(False)
        self.continue4.setObjectName("continue4")
        self.continue4.clicked.connect(self.open5)

        self.lineEdit = QtWidgets.QLineEdit(fourthPage)
        self.lineEdit.setGeometry(QtCore.QRect(50, 570, 361, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(fourthPage)
        self.continue4.clicked.connect(fourthPage.close)
        QtCore.QMetaObject.connectSlotsByName(fourthPage)

    def retranslateUi(self, fourthPage):
        _translate = QtCore.QCoreApplication.translate
        fourthPage.setWindowTitle(_translate("fourthPage", "Dialog"))
        self.label_5.setText(_translate("fourthPage", " Main symptoms"))
        self.cough.setText(_translate("fourthPage", "Cough"))
        self.dizziness.setText(_translate("fourthPage", "Dizziness"))
        self.fever.setText(_translate("fourthPage", "Fever"))
        self.diarrhea.setText(_translate("fourthPage", "Diarrhea"))
        self.fatigue.setText(_translate("fourthPage", "Fatique"))
        self.headache.setText(_translate("fourthPage", "Headache"))
        self.label_6.setText(_translate("fourthPage", "If other please type:"))
        self.nausea.setText(_translate("fourthPage", "Nausea"))
        self.cramp.setText(_translate("fourthPage", "Muscle cramp"))
        self.continue4.setText(_translate("fourthPage", "CONTINUE"))

import First_page_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fourthPage = QtWidgets.QDialog()
    ui = Ui_fourthPage()
    ui.setupUi(fourthPage)
    fourthPage.show()
    sys.exit(app.exec_())

