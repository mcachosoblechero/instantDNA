# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseSymptoms.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from functools import partial

class Ui_Diagnose_S4(QtWidgets.QWidget):
	def PrepareData(self,Main):
		symptoms = []

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

		Main.SetPatientDetails_S4(symptoms)

	def setupUi(self):
	
		self.stack.setObjectName("self.stack")
		self.stack.resize(480, 801)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.label_5 = QtWidgets.QLabel(self.stack)
		self.label_5.setGeometry(QtCore.QRect(40, 30, 421, 71))
		self.label_5.setStyleSheet("background-color: transparent;\n"
		"font: 36pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.label_5.setObjectName("label_5")
		self.cough = QtWidgets.QPushButton(self.stack)
		self.cough.setGeometry(QtCore.QRect(50, 130, 165, 80))
		self.cough.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"")
		self.cough.setCheckable(True)
		self.cough.setAutoDefault(False)
		self.cough.setDefault(True)
		self.cough.setObjectName("cough")
		self.dizziness = QtWidgets.QPushButton(self.stack)
		self.dizziness.setGeometry(QtCore.QRect(50, 230, 165, 80))
		self.dizziness.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.dizziness.setCheckable(True)
		self.dizziness.setAutoDefault(False)
		self.dizziness.setDefault(True)
		self.dizziness.setObjectName("dizziness")
		self.fever = QtWidgets.QPushButton(self.stack)
		self.fever.setGeometry(QtCore.QRect(50, 330, 165, 80))
		self.fever.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.fever.setCheckable(True)
		self.fever.setAutoDefault(False)
		self.fever.setDefault(True)
		self.fever.setObjectName("fever")
		self.diarrhea = QtWidgets.QPushButton(self.stack)
		self.diarrhea.setGeometry(QtCore.QRect(260, 130, 165, 80))
		self.diarrhea.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.diarrhea.setCheckable(True)
		self.diarrhea.setAutoDefault(False)
		self.diarrhea.setDefault(True)
		self.diarrhea.setObjectName("diarrhea")
		self.fatigue = QtWidgets.QPushButton(self.stack)
		self.fatigue.setGeometry(QtCore.QRect(260, 230, 165, 80))
		self.fatigue.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.fatigue.setCheckable(True)
		self.fatigue.setAutoDefault(False)
		self.fatigue.setDefault(True)
		self.fatigue.setObjectName("fatigue")
		self.headache = QtWidgets.QPushButton(self.stack)
		self.headache.setGeometry(QtCore.QRect(260, 330, 165, 80))
		self.headache.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.headache.setCheckable(True)
		self.headache.setAutoDefault(False)
		self.headache.setDefault(True)
		self.headache.setObjectName("headache")
		self.label_6 = QtWidgets.QLabel(self.stack)
		self.label_6.setGeometry(QtCore.QRect(50, 525, 371, 41))
		self.label_6.setStyleSheet("background-color: transparent;\n"
		"font: 18pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.label_6.setObjectName("label_6")
		self.nausea = QtWidgets.QPushButton(self.stack)
		self.nausea.setGeometry(QtCore.QRect(50, 430, 165, 80))
		self.nausea.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.nausea.setCheckable(True)
		self.nausea.setAutoDefault(False)
		self.nausea.setDefault(True)
		self.nausea.setObjectName("nausea")
		self.cramp = QtWidgets.QPushButton(self.stack)
		self.cramp.setGeometry(QtCore.QRect(260, 430, 165, 80))
		self.cramp.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 16pt \"Arial Rounded MT Bold\";")
		self.cramp.setCheckable(True)
		self.cramp.setAutoDefault(False)
		self.cramp.setDefault(True)
		self.cramp.setObjectName("cramp")
		self.label = QtWidgets.QLabel(self.stack)
		self.label.setGeometry(QtCore.QRect(0, 730, 479, 63))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/newPrefix/nav3.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.continue4 = QtWidgets.QPushButton(self.stack)
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

		self.lineEdit = QtWidgets.QLineEdit(self.stack)
		self.lineEdit.setGeometry(QtCore.QRect(50, 570, 361, 41))
		self.lineEdit.setObjectName("lineEdit")

		self.retranslateUi()

	def retranslateUi(self):
		self.stack.setWindowTitle("Diagnosis - Stage 4")
		self.label_5.setText(" Main symptoms")
		self.cough.setText("Cough")
		self.dizziness.setText("Dizziness")
		self.fever.setText("Fever")
		self.diarrhea.setText("Diarrhea")
		self.fatigue.setText("Fatique")
		self.headache.setText("Headache")
		self.label_6.setText("If other please type:")
		self.nausea.setText("Nausea")
		self.cramp.setText("Muscle cramp")
		self.continue4.setText("CONTINUE")

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.continue4.clicked.connect(Main.OpenDiagnose_S5)
		self.continue4.clicked.connect(partial(self.PrepareData,Main))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fourthPage = QtWidgets.QDialog()
    ui = Ui_fourthPage()
    ui.setupUi(fourthPage)
    fourthPage.show()
    sys.exit(app.exec_())

