# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseFirst.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import datetime
from functools import partial
import pandas as pd
import os.path
import csv


class Ui_Diagnose_S1(QtWidgets.QWidget):
	def PrepareData(self, Main):
		if self.comboBox.currentIndex() == 0:
			New = 1
		else:
			New = 0

		Main.SetPatientDetails_S1(New,
								str(self.lineEdit_1.text()),
								str(self.lineEdit_2.text()),
								str(self.lineEdit_4.text()),
								str(self.lineEdit_5.text()))
		Main.OpenDiagnose_S2()

	def VerifyData(self, Main):
		if self.lineEdit_1.text() and self.lineEdit_2.text() and self.lineEdit_4.text() and self.lineEdit_5.text():
			self.PrepareData(Main)

	def indexChanged(self):
		if int(self.comboBox.currentIndex()) == 0:
			self.lineEdit_1.setText("")
			self.lineEdit_1.setReadOnly(False)
			self.lineEdit_2.setText("")
			self.lineEdit_2.setReadOnly(False)
			self.lineEdit_4.setText("")
			self.lineEdit_4.setReadOnly(False)
			self.lineEdit_5.setText("")
			self.lineEdit_5.setReadOnly(False)
		else:
			file = pd.read_csv(os.getcwd() + '/db/patientData.csv')
			comboValue = self.comboBox.currentText().split()
			recordSelected = file.loc[(file['Surname'] == comboValue[1]) & (file['Name'] == comboValue[0])]
			self.lineEdit_1.setText(recordSelected.iloc[0]['Name'])
			self.lineEdit_1.setReadOnly(True)
			self.lineEdit_2.setText(recordSelected.iloc[0]['Surname'])
			self.lineEdit_2.setReadOnly(True)
			self.lineEdit_4.setText(recordSelected.iloc[0]['Nationality'])
			self.lineEdit_4.setReadOnly(True)
			self.lineEdit_5.setText(str(recordSelected.iloc[0]['ID']))
			self.lineEdit_5.setReadOnly(True)

	def setupUi(self):
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.stack.setWindowTitle("Diagnose - Personal Details")

		# Line ??? # 
		self.lineEdit_1 = QtWidgets.QLineEdit(self.stack)
		self.lineEdit_1.setGeometry(QtCore.QRect(260, 190, 181, 31))
		self.lineEdit_1.setStyleSheet("")
		self.lineEdit_1.setText("")

		# Nationality field #
		self.nationality = QtWidgets.QLabel(self.stack)
		self.nationality.setGeometry(QtCore.QRect(40, 320, 61, 61))
		self.nationality.setText("")
		self.nationality.setPixmap(QtGui.QPixmap(":/newPrefix/nationality.png"))
		self.nationality.setScaledContents(True)
		self.nationality.setObjectName("nationality")

		# Id Field # 
		self.id = QtWidgets.QLabel(self.stack)
		self.id.setGeometry(QtCore.QRect(40, 420, 61, 61))
		self.id.setText("")
		self.id.setPixmap(QtGui.QPixmap(":/newPrefix/ID.png"))
		self.id.setScaledContents(True)
		self.id.setObjectName("id")

		# Name Field #
		self.name = QtWidgets.QLabel(self.stack)
		self.name.setGeometry(QtCore.QRect(40, 200, 61, 61))
		self.name.setText("")
		self.name.setPixmap(QtGui.QPixmap(":/newPrefix/name.png"))
		self.name.setScaledContents(True)
		self.name.setObjectName("name")

		# Line ??? #
		self.lineEdit_2 = QtWidgets.QLineEdit(self.stack)
		self.lineEdit_2.setGeometry(QtCore.QRect(260, 240, 181, 31))
		self.lineEdit_2.setText("")
		self.lineEdit_2.setObjectName("lineEdit_2")

		# Line ??? #
		self.lineEdit_4 = QtWidgets.QLineEdit(self.stack)
		self.lineEdit_4.setGeometry(QtCore.QRect(260, 330, 181, 31))
		self.lineEdit_4.setText("")
		self.lineEdit_4.setObjectName("lineEdit_4")

		# Line ??? #
		self.lineEdit_5 = QtWidgets.QLineEdit(self.stack)
		self.lineEdit_5.setGeometry(QtCore.QRect(260, 435, 181, 31))
		self.lineEdit_5.setText("")
		self.lineEdit_5.setObjectName("lineEdit_5")

		# Line ??? #
		self.label_2 = QtWidgets.QLabel(self.stack)
		self.label_2.setGeometry(QtCore.QRect(0, 730, 479, 63))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav1.png"))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName("label_2")

		# Continue Button #
		self.continue1 = QtWidgets.QPushButton(self.stack)
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
		self.continue1.setText("CONTINUE")
		self.continue1.setObjectName("continue1")
		
		# Personal Details #
		self.personal_details = QtWidgets.QLabel(self.stack)
		self.personal_details.setGeometry(QtCore.QRect(20, 55, 420, 60))
		self.personal_details.setStyleSheet("background-color: transparent;\n"
		"font: 38pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details.setObjectName("personal_details")
		self.personal_details.setText(" Personal details")
		
		# Name ??? #
		self.name_2 = QtWidgets.QLabel(self.stack)
		self.name_2.setGeometry(QtCore.QRect(120, 180, 101, 41))
		self.name_2.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.name_2.setObjectName("name_2")
		self.name_2.setText("Name")
		
		# Surname ??? #
		self.surname = QtWidgets.QLabel(self.stack)
		self.surname.setGeometry(QtCore.QRect(120, 230, 111, 41))
		self.surname.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.surname.setObjectName("surname")
		self.surname.setText("Surname")
		
		# Nationality ??? #
		self.nationality_2 = QtWidgets.QLabel(self.stack)
		self.nationality_2.setGeometry(QtCore.QRect(120, 325, 131, 41))
		self.nationality_2.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.nationality_2.setObjectName("nationality_2")
		self.nationality_2.setText("Nationality")
		
		# Id ??? #
		self.id_2 = QtWidgets.QLabel(self.stack)
		self.id_2.setGeometry(QtCore.QRect(120, 430, 131, 41))
		self.id_2.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.id_2.setObjectName("id_2")
		self.id_2.setText("ID Number")


		# Combo Box ??? #
		self.comboBox = QtWidgets.QComboBox(self.stack)
		self.comboBox.setGeometry(QtCore.QRect(230, 540, 180, 30))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.setStyleSheet("color: rgb(46, 117, 182);\n"
		"font: 10pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 25px;")

		# Existing Patient # 
		self.existing_patient = QtWidgets.QLabel(self.stack)
		self.existing_patient.setGeometry(QtCore.QRect(45, 535, 171, 41))
		self.existing_patient.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.existing_patient.setObjectName("existing_patient")
		self.existing_patient.setText("Existing Patient:")

		file = pd.read_csv(os.getcwd() + '/db/patientData.csv')
		self.KnownRecords = file.Name + ' ' + file.Surname

		self.comboBox.addItem("New Patient")
		self.comboBox.addItems(self.KnownRecords)
		self.comboBox.setCurrentIndex(0)
		self.comboBox.blockSignals(False)


	def __init__(self, Main):
		QtWidgets.QApplication.setStyle("Fusion")
		self.stack = QtWidgets.QWidget()
		self.KnownRecords = []
		self.setupUi()
		self.continue1.clicked.connect(partial(self.VerifyData, Main))
		self.comboBox.activated.connect(partial(self.indexChanged))
