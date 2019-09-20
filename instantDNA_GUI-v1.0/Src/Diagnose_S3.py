# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseThird.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_Diagnose_S3(QtWidgets.QWidget):

	def CheckDefault(self, str):
		if not str:
			var = "-"
		else:
			var = str
		return var

	def PrepareData(self,Main):
		Weight = self.CheckDefault(self.weightEdit.text())
		Height = self.CheckDefault(self.heightEdit.text())
		Resp = self.CheckDefault(self.respEdit.text())
		HR = self.CheckDefault(self.heartEdit.text())
		Blood = self.CheckDefault(str(self.bloodEdit1.text()) + "/" + str(self.bloodEdit2.text()))
		Main.SetPatientDetails_S3(Weight, Height, Resp, HR, Blood)
	

	def setupUi(self):
	
		self.stack.setObjectName("Diagnosis_S3")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.pushButton = QtWidgets.QPushButton(self.stack)
		self.pushButton.setGeometry(QtCore.QRect(460, 860, 113, 32))
		self.pushButton.setObjectName("pushButton")

		self.label = QtWidgets.QLabel(self.stack)
		self.label.setGeometry(QtCore.QRect(0, 730, 479, 63))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap(":/newPrefix/nav2.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")

		self.continue3 = QtWidgets.QPushButton(self.stack)
		self.continue3.setGeometry(QtCore.QRect(140, 630, 200, 52))
		self.continue3.setStyleSheet("background-color: rgb(157, 195, 230);\n"
		"font: 20pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"color: rgb(46, 117, 182);\n"
		"\n"
		"\n"
		"")
		self.continue3.setAutoDefault(False)
		self.continue3.setDefault(True)
		self.continue3.setFlat(False)
		self.continue3.setObjectName("continue3")

		self.weightEdit = QtWidgets.QLineEdit(self.stack)
		self.weightEdit.setGeometry(QtCore.QRect(280, 100, 80, 45))
		self.weightEdit.setObjectName("weightEdit")
		self.heightEdit = QtWidgets.QLineEdit(self.stack)
		self.heightEdit.setGeometry(QtCore.QRect(280, 190, 80, 45))
		self.heightEdit.setObjectName("heightEdit")
		self.respEdit = QtWidgets.QLineEdit(self.stack)
		self.respEdit.setGeometry(QtCore.QRect(280, 280, 80, 45))
		self.respEdit.setObjectName("respEdit")
		self.heartEdit = QtWidgets.QLineEdit(self.stack)
		self.heartEdit.setGeometry(QtCore.QRect(280, 370, 80, 45))
		self.heartEdit.setObjectName("heartEdit")
		self.bloodEdit1 = QtWidgets.QLineEdit(self.stack)
		self.bloodEdit1.setGeometry(QtCore.QRect(280, 460, 80, 45))
		self.bloodEdit1.setObjectName("bloodEdit1")
		self.bloodEdit2 = QtWidgets.QLineEdit(self.stack)
		self.bloodEdit2.setGeometry(QtCore.QRect(375, 460, 80, 45))
		self.bloodEdit2.setObjectName("bloodEdit2")
		self.personal_details_2 = QtWidgets.QLabel(self.stack)
		self.personal_details_2.setGeometry(QtCore.QRect(40, 100, 171, 41))
		self.personal_details_2.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_2.setObjectName("personal_details_2")
		self.personal_details_3 = QtWidgets.QLabel(self.stack)
		self.personal_details_3.setGeometry(QtCore.QRect(40, 190, 171, 41))
		self.personal_details_3.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_3.setObjectName("personal_details_3")
		self.personal_details_4 = QtWidgets.QLabel(self.stack)
		self.personal_details_4.setGeometry(QtCore.QRect(40, 280, 261, 41))
		self.personal_details_4.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_4.setObjectName("personal_details_4")
		self.personal_details_5 = QtWidgets.QLabel(self.stack)
		self.personal_details_5.setGeometry(QtCore.QRect(40, 370, 241, 41))
		self.personal_details_5.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_5.setObjectName("personal_details_5")
		self.personal_details_6 = QtWidgets.QLabel(self.stack)
		self.personal_details_6.setGeometry(QtCore.QRect(40, 460, 271, 41))
		self.personal_details_6.setStyleSheet("background-color: transparent;\n"
		"font: 14pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_6.setObjectName("personal_details_6")
		self.personal_details_7 = QtWidgets.QLabel(self.stack)
		self.personal_details_7.setGeometry(QtCore.QRect(365, 460, 21, 41))
		self.personal_details_7.setStyleSheet("background-color: transparent;\n"
		"font: 16pt \"Arial Rounded MT Bold\";\n"
		"color: rgb(46, 117, 182);\n"
		"")
		self.personal_details_7.setObjectName("personal_details_7")

		self.retranslateUi()
		self.stack.showFullScreen()


	def retranslateUi(self):
		self.stack.setWindowTitle("Dialog")
		self.pushButton.setText("Cancel")
		self.continue3.setText("CONTINUE")
		self.personal_details_2.setText("Weight (kg):")
		self.personal_details_3.setText("Height (cm):")
		self.personal_details_4.setText("Respiration rate (bpm):")
		self.personal_details_5.setText("Heart rate (bpm):")
		self.personal_details_6.setText("Blood Pressure (mmHg):")
		self.personal_details_7.setText("/")
		
	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.continue3.clicked.connect(Main.OpenDiagnose_S4)
		self.continue3.clicked.connect(partial(self.PrepareData,Main))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thirdPage = QtWidgets.QDialog()
    ui = Ui_thirdPage()
    ui.setupUi(thirdPage)
    thirdPage.show()
    sys.exit(app.exec_())

