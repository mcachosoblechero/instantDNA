# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseSecond.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_Diagnose_S2(QtWidgets.QWidget):
	def PrepareData(self, Main):
		age = self.ageSlider.value()
		temp = self.tempSlider_2.value()

		if self.AgeUpdated == 0:
			age = "-"

		if self.TempUpdated == 0:
			temp = "-"

		if self.male_button.isChecked():
			gender = "Male"
		elif self.female_button.isChecked():
			gender = "Female"
		else:
			gender = "-"

		Main.SetPatientDetails_S2(age, temp, gender)

	def AgeFlag(self):
		self.AgeUpdated = 1

	def TempFlat(self):
		self.TempUpdated = 1

	def DisplayTemp(self):
		self.tempNumber.display(self.tempSlider_2.value()/10)

	def setupUi(self):

		self.stack.setObjectName("secondPage")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.stack.setWindowTitle("Diagnosis - Stage 2")

		self.pushButton = QtWidgets.QPushButton(self.stack)
		self.pushButton.setGeometry(QtCore.QRect(460, 860, 113, 32))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Cancel")
				
		self.male_button = QtWidgets.QPushButton(self.stack)
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
		self.male_button.setText("MALE")

		self.gender = QtWidgets.QLabel(self.stack)
		self.gender.setGeometry(QtCore.QRect(50, 500, 60, 60))
		self.gender.setText("")
		self.gender.setPixmap(QtGui.QPixmap(":/newPrefix/gender.png"))
		self.gender.setScaledContents(True)
		self.gender.setObjectName("gender")
		
		self.age = QtWidgets.QLabel(self.stack)
		self.age.setGeometry(QtCore.QRect(50, 150, 60, 60))
		self.age.setText("")
		self.age.setPixmap(QtGui.QPixmap(":/newPrefix/age.png"))
		self.age.setScaledContents(True)
		self.age.setObjectName("age")
		
		self.female_button = QtWidgets.QPushButton(self.stack)
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
		self.female_button.setText("FEMALE")
		
		self.ageNumber = QtWidgets.QLCDNumber(self.stack)
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
		self.ageNumber.setProperty("value", 0)
		self.ageNumber.setObjectName("ageNumber")
		
		self.ageSlider = QtWidgets.QSlider(self.stack)
		self.ageSlider.setGeometry(QtCore.QRect(60, 235, 290, 41))
		self.ageSlider.setOrientation(QtCore.Qt.Horizontal)
		self.ageSlider.setObjectName("ageSlider")
		self.ageSlider.setProperty("value",0)
		
		self.label = QtWidgets.QLabel(self.stack)
		self.label.setGeometry(QtCore.QRect(0, 730, 479, 63))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/newPrefix/nav2.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		
		self.temperature = QtWidgets.QLabel(self.stack)
		self.temperature.setGeometry(QtCore.QRect(50, 320, 60, 60))
		self.temperature.setText("")
		self.temperature.setPixmap(QtGui.QPixmap(":/newPrefix/temperature.png"))
		self.temperature.setScaledContents(True)
		self.temperature.setObjectName("temperature")
		
		self.tempSlider_2 = QtWidgets.QSlider(self.stack)
		self.tempSlider_2.setGeometry(QtCore.QRect(60, 405, 290, 41))
		self.tempSlider_2.setMinimum(320)
		self.tempSlider_2.setMaximum(450)
		self.tempSlider_2.setProperty("value",320)
		self.tempSlider_2.setOrientation(QtCore.Qt.Horizontal)
		self.tempSlider_2.setObjectName("tempSlider_2")
		
		self.tempNumber = QtWidgets.QLCDNumber(self.stack)
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
		self.tempNumber.setProperty("value", 32.0)
		self.tempNumber.setObjectName("tempNumber")
		
		self.label_6 = QtWidgets.QLabel(self.stack)
		self.label_6.setGeometry(QtCore.QRect(25, 40, 461, 60))
		self.label_6.setStyleSheet("background-color: transparent;\n"
		"font: 29pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.label_6.setObjectName("label_6")
		self.label_6.setText("Additional information")
		
		self.continue2 = QtWidgets.QPushButton(self.stack)
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
		self.continue2.setText("CONTINUE")

		self.age_2 = QtWidgets.QLabel(self.stack)
		self.age_2.setGeometry(QtCore.QRect(125, 160, 91, 41))
		self.age_2.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.age_2.setObjectName("age_2")
		self.age_2.setText("Age")

		self.temp = QtWidgets.QLabel(self.stack)
		self.temp.setGeometry(QtCore.QRect(125, 330, 251, 41))
		self.temp.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.temp.setObjectName("temp")
		self.temp.setText("Temp (C)")
		
		self.personal_details_5 = QtWidgets.QLabel(self.stack)
		self.personal_details_5.setGeometry(QtCore.QRect(125, 510, 101, 41))
		self.personal_details_5.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_5.setObjectName("personal_details_5")
		self.personal_details_5.setText("Gender")

		self.ageSlider.valueChanged['int'].connect(self.ageNumber.display)
		self.ageSlider.valueChanged.connect(partial(self.AgeFlag))
		self.tempSlider_2.valueChanged.connect(partial(self.DisplayTemp))
		self.tempSlider_2.valueChanged.connect(partial(self.TempFlat))

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.AgeUpdated = 0
		self.TempUpdated = 0
		self.continue2.clicked.connect(Main.OpenDiagnose_S3)
		self.continue2.clicked.connect(partial(self.PrepareData,Main))
