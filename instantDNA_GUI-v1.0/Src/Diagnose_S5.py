# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseCartridge.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv
import os
from datetime import datetime
from functools import partial

class Ui_Diagnose_S5(QtWidgets.QWidget):

	def SaveData(self, Main):
		if Main.NewPatient == 1:
			with open(os.getcwd() + '/db/patientData.csv', 'a+', newline='') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				spamwriter.writerow(
					[Main.Patient_Name, Main.Patient_Surname, Main.Patient_Nationality, Main.Patient_ID])

		now = datetime.now()
		with open(os.getcwd() + '/db/dataFile.csv', 'a+', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(
				[Main.Patient_Name, Main.Patient_Surname, Main.Patient_Nationality, Main.Patient_ID,
				 Main.Patient_Age, Main.Patient_BodyTemp, Main.Patient_Gender, Main.Patient_Weight, Main.Patient_Height,
				 Main.Patient_RespRate, Main.Patient_HR, Main.Patient_BloodPress, Main.Patient_Symptoms, now.strftime("%d/%m/%Y %H:%M:%S")])



	def setupUi(self):
		self.stack.setObjectName("Diagnosis_S5")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.label = QtWidgets.QLabel(self.stack)
		self.label.setGeometry(QtCore.QRect(50, 110, 370, 360))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/newPrefix/doctor.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")

		self.label_2 = QtWidgets.QLabel(self.stack)
		self.label_2.setGeometry(QtCore.QRect(0, 730, 479, 63))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav4.png"))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName("label_2")

		self.label_3 = QtWidgets.QLabel(self.stack)
		self.label_3.setGeometry(QtCore.QRect(60, 130, 221, 61))
		self.label_3.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);")
		self.label_3.setObjectName("label_3")

		self.continue5 = QtWidgets.QPushButton(self.stack)
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

		self.continue5.setAutoDefault(False)
		self.continue5.setDefault(True)
		self.continue5.setFlat(False)
		self.continue5.setObjectName("continue5")
		self.cance5 = QtWidgets.QPushButton(self.stack)
		self.cance5.setGeometry(QtCore.QRect(140, 600, 200, 52))
		self.cance5.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"font: 20pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"color: rgb(46, 117, 182);\n"
		"\n"
		"\n"
		"")
		self.cance5.setAutoDefault(False)
		self.cance5.setDefault(True)
		self.cance5.setFlat(False)
		self.cance5.setObjectName("cance5")

		self.retranslateUi()

	def retranslateUi(self):
		self.stack.setWindowTitle("Diagnosis - Stage 5")
		self.label_3.setText("Please insert cartridge!")
		self.continue5.setText("START TEST")
		self.cance5.setText("CANCEL")

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.cance5.clicked.connect(Main.OpenMainMenu)
		self.continue5.clicked.connect(Main.OpenDiagnose_S6)
		self.continue5.clicked.connect(partial(self.SaveData, Main))
