# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DebugMenu(QtWidgets.QWidget):
	def setupUi(self):
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")

		# Push Button - General Setting #
		self.Settings = QtWidgets.QPushButton(self.stack)
		self.Settings.setGeometry(QtCore.QRect(10, 150, 461, 201))
		self.Settings.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"font: 36pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"\n"
		"\n"
		"")
		self.Settings.setAutoDefault(False)
		self.Settings.setDefault(True)
		self.Settings.setFlat(False)
		self.Settings.setText("General Setting")

		# Push Button - Run Tests #
		self.Tests = QtWidgets.QPushButton(self.stack)
		self.Tests.setGeometry(QtCore.QRect(10, 380, 461, 201))
		self.Tests.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"font: 36pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"\n"
		"\n"
		"")
		self.Tests.setAutoDefault(False)
		self.Tests.setDefault(True)
		self.Tests.setFlat(False)
		self.Tests.setText("Run tests")

		# Push Button - Main Page #
		self.MainPage = QtWidgets.QPushButton(self.stack)
		self.MainPage.setGeometry(QtCore.QRect(140, 660, 200, 52))
		self.MainPage.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"font: 20pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 15px;\n"
		"\n"
		"\n"
		"")
		self.MainPage.setAutoDefault(False)
		self.MainPage.setDefault(True)
		self.MainPage.setFlat(False)
		self.MainPage.setText("Main page")

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.MainPage.clicked.connect(Main.OpenMainMenu)
		self.Settings.clicked.connect(Main.OpenDebugSettings)
		self.Tests.clicked.connect(Main.OpenDebugRunTest)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	debugFirst = QtWidgets.QDialog()
	ui = Ui_debugFirst()
	ui.setupUi(debugFirst)
	debugFirst.show()
	sys.exit(app.exec_())

