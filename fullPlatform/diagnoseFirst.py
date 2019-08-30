# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseFirst.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from diagnoseSecond import Ui_secondPage
from datetime import datetime
import os.path
import csv



class Ui_firstPage(object):
    QtWidgets.QApplication.setStyle("Fusion")
    
    
    def indexChanged(self):
        self.Index = int(self.comboBox.currentIndex())
        
        patients = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_4,
                        self.lineEdit_5]

        if self.Index == 0:
            for i in range(len(patients)):
                patients[i-1].setText(" ")
            

        else:
            with open('patientData.csv') as csvfile:
                    data = []
                    reader = csv.reader(csvfile)
                    for row in reader:
                        data.append(row)

            f = data[self.Index] # +1 essential to pick the correct user
            print(f)
            
            for i in range(0, len(f)):
                name = str(f[i-1])
                patients[i-1].setText(name) # no need to translate
                patients[i-1].setReadOnly(True)

            
            
                
    def open2(self):
        #print (data2)
        self.Index = int(self.comboBox.currentIndex())
        data2 = [
                str(self.lineEdit_1.text()),
                str(self.lineEdit_2.text()),
                str(self.lineEdit_4.text()),
                str(self.lineEdit_5.text())
                ]

        if self.Index == 0:

            f = open("patient.txt", "w+")
            for line in data2:
                # write line to output file
                f.write(line)
                f.write("\n")


            with open('patientData.csv', 'a+') as f: #create a new user if there is no excisting one
                writer = csv.writer(f)
                writer.writerow(data2)   #working
        else:
                        
            f = open("patient.txt", "w+")
            for line in data2:
                # write line to output file
                f.write(line)
                f.write("\n")

        self.window=QtWidgets.QDialog() 
        self.ui = Ui_secondPage()
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.showFullScreen()
        

    def setupUi(self, firstPage):
        firstPage.setObjectName("firstPage")
        firstPage.resize(480, 800)
        firstPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        #firstPage.setIconSize(QtCore.QSize(70, 70))
        #self.centralwidget = QtWidgets.QWidget(firstPage)
        #self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_1 = QtWidgets.QLineEdit(firstPage)
        self.lineEdit_1.setGeometry(QtCore.QRect(260, 190, 181, 31))
        self.lineEdit_1.setStyleSheet("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.nationality = QtWidgets.QLabel(firstPage)
        self.nationality.setGeometry(QtCore.QRect(40, 320, 61, 61))
        self.nationality.setText("")
        self.nationality.setPixmap(QtGui.QPixmap(":/newPrefix/nationality.png"))
        self.nationality.setScaledContents(True)
        self.nationality.setObjectName("nationality")
        self.id = QtWidgets.QLabel(firstPage)
        self.id.setGeometry(QtCore.QRect(40, 420, 61, 61))
        self.id.setText("")
        self.id.setPixmap(QtGui.QPixmap(":/newPrefix/ID.png"))
        self.id.setScaledContents(True)
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(firstPage)
        self.name.setGeometry(QtCore.QRect(40, 200, 61, 61))
        self.name.setText("")
        self.name.setPixmap(QtGui.QPixmap(":/newPrefix/name.png"))
        self.name.setScaledContents(True)
        self.name.setObjectName("name")
        self.lineEdit_2 = QtWidgets.QLineEdit(firstPage)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 240, 181, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(firstPage)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 330, 181, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(firstPage)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 435, 181, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(firstPage)
        self.label_2.setGeometry(QtCore.QRect(0, 730, 479, 63))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.continue1 = QtWidgets.QPushButton(firstPage)
        self.continue1.setGeometry(QtCore.QRect(140, 630, 200, 52))
        self.continue1.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue1.setAutoDefault(False)
        self.continue1.setDefault(True)
        self.continue1.setFlat(False)
        self.continue1.setObjectName("continue1")
        self.personal_details = QtWidgets.QLabel(firstPage)
        self.personal_details.setGeometry(QtCore.QRect(20, 55, 420, 60))
        self.personal_details.setStyleSheet("background-color: transparent;\n"
"font: 38pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.personal_details.setObjectName("personal_details")
        self.name_2 = QtWidgets.QLabel(firstPage)
        self.name_2.setGeometry(QtCore.QRect(120, 180, 101, 41))
        self.name_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.name_2.setObjectName("name_2")
        self.surname = QtWidgets.QLabel(firstPage)
        self.surname.setGeometry(QtCore.QRect(120, 230, 111, 41))
        self.surname.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.surname.setObjectName("surname")
        self.nationality_2 = QtWidgets.QLabel(firstPage)
        self.nationality_2.setGeometry(QtCore.QRect(120, 325, 131, 41))
        self.nationality_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.nationality_2.setObjectName("nationality_2")
        self.id_2 = QtWidgets.QLabel(firstPage)
        self.id_2.setGeometry(QtCore.QRect(120, 430, 131, 41))
        self.id_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.id_2.setObjectName("id_2")

        self.comboBox = QtWidgets.QComboBox(firstPage)
        self.comboBox.setGeometry(QtCore.QRect(230, 540, 180, 30))
        self.comboBox.setObjectName("comboBox")

        self.existing_patient = QtWidgets.QLabel(firstPage)
        self.existing_patient.setGeometry(QtCore.QRect(45, 535, 171, 41))
        self.existing_patient.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.existing_patient.setObjectName("existing_patient")

        with open('patientData.csv') as csvfile:
            data = []
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        people = []

        for i in range(1, len(data)):
            f = data[i]
            name = str(f[0]) + " " + str(f[1])
            people.append(name)
            
        self.comboBox.addItem("New Patient")    
        self.comboBox.addItems(people)
        
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentIndexChanged.connect(self.indexChanged)
        

        self.retranslateUi(firstPage)

        
        self.continue1.clicked.connect(self.open2)
        self.continue1.clicked.connect(firstPage.close)
        
        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        _translate = QtCore.QCoreApplication.translate
        firstPage.setWindowTitle(_translate("firstPage", "MainWindow"))
        self.continue1.setText(_translate("firstPage", "CONTINUE"))
        self.existing_patient.setText(_translate("firstPage", "Existing Patient:"))
        self.personal_details.setText(_translate("firstPage", " Personal details"))
        self.name_2.setText(_translate("firstPage", "Name"))
        self.surname.setText(_translate("firstPage", "Surname"))
        self.nationality_2.setText(_translate("firstPage", "Nationality"))
        self.id_2.setText(_translate("firstPage", "ID Number"))

import First_page_file

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setStyle("Fusion") # important, effectively changes the style
    app = QtWidgets.QApplication(sys.argv) 
    firstPage = QtWidgets.QDialog()
    ui = Ui_firstPage()
    ui.setupUi(firstPage)
    firstPage.show()
    sys.exit(app.exec_())

