# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Diagnose_S6(object):
	def setupUi(self):
	
		self.stack.setObjectName("self.stack")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.nurse = QtWidgets.QLabel(self.stack)
		self.nurse.setGeometry(QtCore.QRect(60, 70, 350, 250))
		self.nurse.setText("")
		self.nurse.setPixmap(QtGui.QPixmap(":/newPrefix/doctor3.png"))
		self.nurse.setScaledContents(True)
		self.nurse.setObjectName("nurse")

		self.textLabel = QtWidgets.QLabel(self.stack)
		self.textLabel.setGeometry(QtCore.QRect(190, 90, 211, 41))
		self.textLabel.setStyleSheet("background-color: transparent;")
		self.textLabel.setText("")
		self.textLabel.setObjectName("textLabel")

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

		self.retranslateUi()

	def TestControl(self):
		if 		self.State == 0:
			self.textLabel.setText(self.DisplayList[self.State])
			self.continue2.clicked.connect(self.RunControl)
			
		elif 	self.State == 1:
			self.textLabel.setText(self.DisplayList[self.State])
			self.continue2.clicked.connect(self.RunControl)
			
		elif 	self.State == 2:
			self.textLabel.setText(self.DisplayList[self.State])
			self.continue2.clicked.connect(self.RunControl)
			
		elif 	self.State == 3:
			self.textLabel.setText(self.DisplayList[self.State])
			self.continue2.clicked.connect(self.RunControl)
			
		elif 	self.State == 4:
			self.textLabel.setText(self.DisplayList[self.State])
			self.continue2.clicked.connect(Main.OpenMainMenu)

	def RunControl(self):
		self.State = self.State + 1
		self.TestControl()

	def retranslateUi(self):
		self.stack.setWindowTitle("Diagnosis - Stage 6")

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.DisplayList = ["Initialising platform", "Firing ISFETs", "Amplifying DNA", "Detecting changes in pH", "Preparing diagnosis"]
		self.StateList = list(range(len(self.DisplayList)))
		self.State = 0
		self.setupUi()
		self.TestControl()
		

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

