# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebugSettings(QtWidgets.QWidget):
	def setupUi(self):
		self.stack.setObjectName("DebugSettings")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.stack.setWindowTitle("DebugSettings")

		# Main Page Button #
		self.mainPage = QtWidgets.QPushButton(self.stack)
		self.mainPage.setGeometry(QtCore.QRect(140, 660, 200, 52))
		self.mainPage.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"font: 20pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"\n"
		"\n"
		"")
		self.mainPage.setAutoDefault(False)
		self.mainPage.setDefault(True)
		self.mainPage.setFlat(False)
		self.mainPage.setObjectName("mainPage")
		self.mainPage.setText("Main page")

		self.left = QtWidgets.QLabel(self.stack)
		self.left.setGeometry(QtCore.QRect(60, 650, 80, 70))
		self.left.setText("")
		self.left.setPixmap(QtGui.QPixmap(":/newPrefix/left2.png"))
		self.left.setScaledContents(True)
		self.left.setObjectName("left")

		self.right = QtWidgets.QLabel(self.stack)
		self.right.setGeometry(QtCore.QRect(340, 650, 80, 70))
		self.right.setText("")
		self.right.setPixmap(QtGui.QPixmap(":/newPrefix/right2.png"))
		self.right.setScaledContents(True)
		self.right.setObjectName("right")

		self.label_5 = QtWidgets.QLabel(self.stack)
		self.label_5.setGeometry(QtCore.QRect(50, 60, 331, 71))
		self.label_5.setStyleSheet("background-color: transparent;\n"
		"font: 38pt \"Arial Rounded MT Bold\";\n"
		"")
		self.label_5.setObjectName("label_5")
		self.label_5.setText("Debug - Chip")

		self.radioButton = QtWidgets.QRadioButton(self.stack)
		self.radioButton.setGeometry(QtCore.QRect(200, 400, 120, 20))
		self.radioButton.setObjectName("radioButton")
		self.radioButton.setText("Working")

		self.label_9 = QtWidgets.QLabel(self.stack)
		self.label_9.setGeometry(QtCore.QRect(60, 470, 151, 31))
		self.label_9.setStyleSheet("background-color: transparent;\n"
		"font: 12pt \"Arial Rounded MT Bold\";\n"
		"")
		self.label_9.setObjectName("label_9")
		self.label_9.setText("Cartridge Status")

		self.label_7 = QtWidgets.QLabel(self.stack)
		self.label_7.setGeometry(QtCore.QRect(60, 290, 111, 31))
		self.label_7.setStyleSheet("background-color: transparent;\n"
		"font: 12pt \"Arial Rounded MT Bold\";\n"
		"")
		self.label_7.setObjectName("label_7")
		self.label_7.setText("Received SPI")

		self.radioButton_2 = QtWidgets.QRadioButton(self.stack)
		self.radioButton_2.setGeometry(QtCore.QRect(300, 400, 130, 20))
		self.radioButton_2.setObjectName("radioButton_2")
		self.radioButton_2.setText("Not Working")

		self.lineEdit_2 = QtWidgets.QLineEdit(self.stack)
		self.lineEdit_2.setGeometry(QtCore.QRect(190, 280, 111, 41))
		self.lineEdit_2.setStyleSheet("font: 20pt \".SF NS Text\";")
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.radioButton_3 = QtWidgets.QRadioButton(self.stack)
		self.radioButton_3.setGeometry(QtCore.QRect(200, 475, 120, 20))
		self.radioButton_3.setObjectName("radioButton_3")
		self.radioButton_3.setText("Inserted")

		self.lineEdit = QtWidgets.QLineEdit(self.stack)
		self.lineEdit.setGeometry(QtCore.QRect(190, 220, 113, 41))
		self.lineEdit.setStyleSheet("font: 20pt \".SF NS Text\";")
		self.lineEdit.setObjectName("lineEdit")

		self.label_6 = QtWidgets.QLabel(self.stack)
		self.label_6.setGeometry(QtCore.QRect(60, 220, 111, 31))
		self.label_6.setStyleSheet("background-color: transparent;\n"
		"font: 12pt \"Arial Rounded MT Bold\";\n"
		"")
		self.label_6.setObjectName("label_6")
		self.label_6.setText("Sent SPI")

		self.label_8 = QtWidgets.QLabel(self.stack)
		self.label_8.setGeometry(QtCore.QRect(60, 395, 111, 31))
		self.label_8.setStyleSheet("background-color: transparent;\n"
		"font: 12pt \"Arial Rounded MT Bold\";\n"
		"")        
		self.label_8.setText("PWM Status")
		self.label_8.setObjectName("label_8")
		
		self.radioButton_4 = QtWidgets.QRadioButton(self.stack)
		self.radioButton_4.setGeometry(QtCore.QRect(300, 475, 120, 20))
		self.radioButton_4.setObjectName("radioButton_4")
		self.radioButton_4.setText("Not inserted")
		
		self.continue5 = QtWidgets.QPushButton(self.stack)
		self.continue5.setGeometry(QtCore.QRect(340, 220, 100, 45))
		self.continue5.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"font: 12pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"\n"
		"\n"
		"\n"
		"")
		self.continue5.setAutoDefault(False)
		self.continue5.setDefault(True)
		self.continue5.setFlat(False)
		self.continue5.setObjectName("continue5")
		self.continue5.setText("Send SPI")

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.mainPage.clicked.connect(Main.OpenMainMenu)
		#self.Settings.clicked.connect(Main.OpenDebugSettings)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	self.stack = QtWidgets.QDialog()
	ui = Ui_self.stack()
	ui.setupUi(self.stack)
	self.stack.show()
	sys.exit(app.exec_())

