# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runTests.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Src.coloredGraph import MplCmapImageView
import numpy as np
import pyqtgraph as pg
from pyqtgraph import ImageView, PlotWidget

class Ui_DebugRunTest(QtWidgets.QWidget):
	def setupUi(self):
		self.stack.setObjectName("self.stack")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("")
		self.stack.setWindowTitle("Debug - Run Tests")

		#configure the first window
		#self.graphicsView = QtWidgets.QGraphicsView(self.stack)
		self.graphicsView = MplCmapImageView(parent=self.stack) 
		self.graphicsView.setGeometry(QtCore.QRect(40, 130, 400, 300))
		self.graphicsView.setObjectName("graphicsView")
		self.graphicsView.setLevels(0,250)
		self.graphicsView.ui.roiBtn.hide() #added this bit of code to remoce roi and memu buttons as we dont need them
		self.graphicsView.ui.menuBtn.hide()

		#configure the first window
		#self.graphicsView_2 = QtWidgets.QGraphicsView(self.stack)
		self.graphicsView_2 = PlotWidget(self.stack)
		self.graphicsView_2.setGeometry(QtCore.QRect(40, 460, 400, 200))
		self.graphicsView_2.setObjectName("graphicsView_2")


		self.pushButton = QtWidgets.QPushButton(self.stack)
		self.pushButton.setGeometry(QtCore.QRect(270, 60, 113, 32))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Run Test")

		self.comboBox = QtWidgets.QComboBox(self.stack)
		self.comboBox.setGeometry(QtCore.QRect(100, 60, 141, 32))
		self.comboBox.setObjectName("comboBox")

		self.comboBox.addItems(["Test1", "Test2", "Test3", "Test4"])
		self.pushButton.clicked.connect(self.display) # picks test and connects to signal

		self.save = QtWidgets.QPushButton(self.stack)
		self.save.setGeometry(QtCore.QRect(110, 710, 111, 45))
		self.save.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"\n"
		"\n"
		"\n"
		"")
		self.save.setAutoDefault(False)
		self.save.setDefault(True)
		self.save.setFlat(False)
		self.save.setObjectName("save")
		self.save.setText("Save Results")

		self.exit = QtWidgets.QPushButton(self.stack)
		self.exit.setGeometry(QtCore.QRect(270, 710, 111, 45))
		self.exit.setStyleSheet("background-color: rgb(191, 191, 191);\n"
		"\n"
		"\n"
		"\n"
		"")
		self.exit.setAutoDefault(False)
		self.exit.setDefault(True)
		self.exit.setFlat(False)
		self.exit.setObjectName("exit")
		self.exit.setText("Exit")
		self.stack.showFullScreen()

    
	def Test0(self):
		print("Test 0")
		
	def Test1(self):
		print("Test 1")
		
	def Test2(self):
		print("Test 2")
	   
	def Test3(self):
		print("Test 3")
    
	def display(self):
		self.comboText = int(self.comboBox.currentIndex())
		print(self.comboText)

		if self.comboText == 0:
			self.Test0()
		if self.comboText == 1:
			self.Test1()
		if self.comboText == 2:
			self.Test2()
		if self.comboText == 3:
			self.Test3()   

	def __init__(self, Main):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.exit.clicked.connect(Main.OpenMainMenu)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	runTests = QtWidgets.QDialog()
	ui = Ui_runTests()
	ui.setupUi(runTests)
	runTests.show()
	sys.exit(app.exec_())

