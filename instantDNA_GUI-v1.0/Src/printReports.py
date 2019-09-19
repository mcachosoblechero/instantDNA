# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np
import pandas as pd

pg.setConfigOption('background', 'w')


class Ui_Dialog(object):
		
	def setupUi(self, Dialog):

		file = pd.read_csv(os.getcwd() + '/db/dataFile.csv')
		self.patientData = file.loc[file['ID'] == float(self.Id)]
		self.numOfRecords = len(self.patientData)

		Dialog.setObjectName("Dialog")
		Dialog.resize(450, 650)
		Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.listView = QtWidgets.QListView(Dialog)
		self.listView.setGeometry(QtCore.QRect(40, 20, 370, 320))
		self.listView.setObjectName("listView")
		self.listView.setAlternatingRowColors(True)
		self.close = QtWidgets.QPushButton(Dialog)
		self.close.setGeometry(QtCore.QRect(160, 570, 130, 45))
		self.close.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"font: 18pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"color: rgb(46, 117, 182);\n"
		"\n"
		"\n"
		"")
		self.close.setAutoDefault(False)
		self.close.setDefault(True)
		self.close.setFlat(False)
		self.close.setObjectName("close")
		self.model = QtGui.QStandardItemModel()
		self.listView.setModel(self.model)

		self.graphicsView = PlotWidget(Dialog)
		self.graphicsView.setGeometry(QtCore.QRect(80, 360, 270, 180))
		self.graphicsView.setObjectName("graphicsView")


		self.right0 = QtWidgets.QPushButton(Dialog)# add the name of the tab
		self.right0.setGeometry(QtCore.QRect(290, 565, 60, 50))
		self.right0.setStyleSheet("background-color: transparent;\n"
		"border-image: url(:/newPrefix/right.png);")
		self.right0.setText("")
		self.right0.setObjectName("right0")
		self.left0 = QtWidgets.QPushButton(Dialog)
		self.left0.setGeometry(QtCore.QRect(100, 565, 60, 50))
		self.left0.setStyleSheet("background-color: transparent;\n"
		"border-image: url(:/newPrefix/left.png);")
		self.left0.setText("")
		self.left0.setObjectName("left0")

		self.updateUI()
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)
		self.close.clicked.connect(Dialog.close)

	def updateUI(self):
		self.model.clear()
		self.currentRecord = self.patientData.iloc[self.RecordIndex]
		data2 = [
			"Date of Test:                     " + str(self.currentRecord.Date),
			"  ",
			"Patient's Name:                 " + str(self.currentRecord.Name) + " " + str(self.currentRecord.Surname),
			"Nationality:                         " + str(self.currentRecord.Nationality),
			"ID number:                          " + str(self.currentRecord.ID),
			"Age:                                     " + str(self.currentRecord.Age),
			"Body Temperature:            " + str(self.currentRecord.BodyTemp),
			"Gender:                               " + str(self.currentRecord.Gender),
			"Weight (Kg):                        " + str(self.currentRecord.Weight),
			"Height (cm):                        " + str(self.currentRecord.Height),
			"Respiration rate (bpm):      " + str(self.currentRecord.Respiration),
			"Heart rate (bpm):                " + str(self.currentRecord.HR),
			"Blood Pressure (mmHg):    " + str(self.currentRecord.BloodPress),
			"Symptoms:                           " + str(self.currentRecord.Symptoms)
		]

		# Dummy data
		x = np.linspace(0, 3, 50)
		y = np.exp(x)
		
		self.graphicsView.plot(x, y)

		self.right0.clicked.connect(self.nextPage)
		self.left0.clicked.connect(self.prevPage)

		for item in data2:
			data = QtGui.QStandardItem(item)
			self.model.appendRow(data)    
       

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Medical report"))
		self.close.setText(_translate("Dialog", "OK"))

	def nextPage(self):
		if (self.RecordIndex < self.numOfRecords-1):
			self.RecordIndex = self.RecordIndex + 1
			self.updateUI()

	def prevPage(self):
		if (self.RecordIndex > 0):
			self.RecordIndex = self.RecordIndex - 1
			self.updateUI()

	def __init__(self, number):
		self.Id = number
		self.RecordIndex = 0

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog(2)
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

