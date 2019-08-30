# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseSecond.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from diagnoseThird import Ui_thirdPage


class Ui_secondPage(object):
    def open3(self):
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_thirdPage()
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.showFullScreen()

        age = self.ageSlider.value()
        temp = self.tempSlider_2.value()

        #values below work like this

        if age == 0:
             age = "-"
        else:
             age = age

        if temp == 10:
             temp = "-"
        else:
             temp = temp

        if self.male_button.isChecked():
             gender = "Male"
        elif self.female_button.isChecked():
             gender = "Female"
        else:
             gender = "-"
           
        data3 = [
            str(age),
            str(temp),
            str(gender),
            ]
        
       # print (data3)

        f = open("patient.txt", "a+")
        
        for line in data3:
            f.write(line)
            f.write("\n")
        
        f.close

    def setupUi(self, secondPage):
        secondPage.setObjectName("secondPage")
        secondPage.resize(480, 800)
        secondPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(secondPage)
        self.pushButton.setGeometry(QtCore.QRect(460, 860, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.male_button = QtWidgets.QPushButton(secondPage)
        self.male_button.setGeometry(QtCore.QRect(260, 490, 75, 75))
        self.male_button.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"border-color: rgb(49, 106, 255);\n"
"padding: 3px;\n"
"background-color: rgb(157, 195, 230);\n"
"color: rgb(46, 117, 182);\n"
"\n"
"")
        self.male_button.setCheckable(True)
        self.male_button.setChecked(False)
        self.male_button.setAutoExclusive(True)
        self.male_button.setAutoDefault(False)
        self.male_button.setDefault(True)
        self.male_button.setFlat(False)
        self.male_button.setObjectName("male_button")
        self.gender = QtWidgets.QLabel(secondPage)
        self.gender.setGeometry(QtCore.QRect(50, 500, 60, 60))
        self.gender.setText("")
        self.gender.setPixmap(QtGui.QPixmap(":/newPrefix/gender.png"))
        self.gender.setScaledContents(True)
        self.gender.setObjectName("gender")
        self.age = QtWidgets.QLabel(secondPage)
        self.age.setGeometry(QtCore.QRect(50, 150, 60, 60))
        self.age.setText("")
        self.age.setPixmap(QtGui.QPixmap(":/newPrefix/age.png"))
        self.age.setScaledContents(True)
        self.age.setObjectName("age")
        self.female_button = QtWidgets.QPushButton(secondPage)
        self.female_button.setGeometry(QtCore.QRect(360, 490, 75, 75))
        self.female_button.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"\n"
"background-color: rgb(157, 195, 230);\n"
"alternate-background-color: rgb(87, 180, 255);\n"
"color: rgb(46, 117, 182);\n"
"")
        self.female_button.setCheckable(True)
        self.female_button.setAutoExclusive(True)
        self.female_button.setFlat(False)
        self.female_button.setObjectName("female_button")
        self.ageNumber = QtWidgets.QLCDNumber(secondPage)
        self.ageNumber.setGeometry(QtCore.QRect(249, 139, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ageNumber.setFont(font)
        self.ageNumber.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"border: transparent;\n"                                   
"gridline-color: transparent;\n"
"color: rgb(46, 117, 182);\n"
"")
        self.ageNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ageNumber.setDigitCount(5)
        self.ageNumber.setProperty("value", 0.0)
        self.ageNumber.setObjectName("ageNumber")
        self.ageSlider = QtWidgets.QSlider(secondPage)
        self.ageSlider.setGeometry(QtCore.QRect(60, 235, 290, 41))
        self.ageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ageSlider.setObjectName("ageSlider")
        self.label = QtWidgets.QLabel(secondPage)
        self.label.setGeometry(QtCore.QRect(0, 730, 479, 63))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/nav2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.temperature = QtWidgets.QLabel(secondPage)
        self.temperature.setGeometry(QtCore.QRect(50, 320, 60, 60))
        self.temperature.setText("")
        self.temperature.setPixmap(QtGui.QPixmap(":/newPrefix/temperature.png"))
        self.temperature.setScaledContents(True)
        self.temperature.setObjectName("temperature")
        self.tempSlider_2 = QtWidgets.QSlider(secondPage)
        self.tempSlider_2.setGeometry(QtCore.QRect(60, 405, 290, 41))
        self.tempSlider_2.setMinimum(10)
        self.tempSlider_2.setMaximum(50)
        self.tempSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.tempSlider_2.setObjectName("tempSlider_2")
        self.tempNumber = QtWidgets.QLCDNumber(secondPage)
        self.tempNumber.setGeometry(QtCore.QRect(250, 310, 160, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.tempNumber.setFont(font)
        self.tempNumber.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"border: transparent;\n"                       
"gridline-color: transparent;\n"
"color: rgb(46, 117, 182);\n"
"")
        self.tempNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tempNumber.setDigitCount(5)
        self.tempNumber.setProperty("value", 0.0)
        self.tempNumber.setObjectName("tempNumber")
        self.label_6 = QtWidgets.QLabel(secondPage)
        self.label_6.setGeometry(QtCore.QRect(25, 40, 461, 60))
        self.label_6.setStyleSheet("background-color: transparent;\n"
"font: 29pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.label_6.setObjectName("label_6")
        self.continue2 = QtWidgets.QPushButton(secondPage)
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

        self.continue2.clicked.connect(self.open3)
        
        self.age_2 = QtWidgets.QLabel(secondPage)
        self.age_2.setGeometry(QtCore.QRect(125, 160, 91, 41))
        self.age_2.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.age_2.setObjectName("age_2")
        self.temp = QtWidgets.QLabel(secondPage)
        self.temp.setGeometry(QtCore.QRect(125, 330, 251, 41))
        self.temp.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.temp.setObjectName("temp")
        self.personal_details_5 = QtWidgets.QLabel(secondPage)
        self.personal_details_5.setGeometry(QtCore.QRect(125, 510, 101, 41))
        self.personal_details_5.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.personal_details_5.setObjectName("personal_details_5")

        self.retranslateUi(secondPage)
        self.ageSlider.valueChanged['int'].connect(self.ageNumber.display)
        self.tempSlider_2.valueChanged['int'].connect(self.tempNumber.display)

        self.continue2.clicked.connect(secondPage.close)
        
        QtCore.QMetaObject.connectSlotsByName(secondPage)

    def retranslateUi(self, secondPage):
        _translate = QtCore.QCoreApplication.translate
        secondPage.setWindowTitle(_translate("secondPage", "Dialog"))
        self.pushButton.setText(_translate("secondPage", "Cancel"))
        self.male_button.setText(_translate("secondPage", "MALE"))
        self.female_button.setText(_translate("secondPage", "FEMALE"))
        self.label_6.setText(_translate("secondPage", "Additional information"))
        self.continue2.setText(_translate("secondPage", "CONTINUE"))
        self.age_2.setText(_translate("secondPage", "Age"))
        self.temp.setText(_translate("secondPage", "Body Temperature (C)"))
        self.personal_details_5.setText(_translate("secondPage", "Gender"))

import First_page_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondPage = QtWidgets.QDialog()
    ui = Ui_secondPage()
    ui.setupUi(secondPage)
    secondPage.show()
    sys.exit(app.exec_())

