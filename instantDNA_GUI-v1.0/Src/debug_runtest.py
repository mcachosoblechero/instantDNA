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
from functools import partial

class Ui_DebugRunTest(QtWidgets.QWidget):
	def setupUi(self):
		self.stack.setObjectName("self.stack")
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.stack.resize(480, 800)
		self.stack.setWindowTitle("Debug - Run Tests")

		#configure the first window
		#self.graphicsView = QtWidgets.QGraphicsView(self.stack)
		self.graphicsView = MplCmapImageView(parent=self.stack) 
		self.graphicsView.setGeometry(QtCore.QRect(40, 130, 400, 300))
		self.graphicsView.setObjectName("graphicsView")
		self.graphicsView.ui.roiBtn.hide() #added this bit of code to remoce roi and memu buttons as we dont need them
		self.graphicsView.ui.menuBtn.hide()

		#configure the first window
		#self.graphicsView_2 = QtWidgets.QGraphicsView(self.stack)
		#self.graphicsView_2 = pg.GraphicsWindow(title="AvSensor")
		self.graphicsView_2 = pg.PlotWidget(self.stack)
		self.graphicsView_2.setGeometry(QtCore.QRect(40, 460, 400, 200))
		self.graphicsView_2.setObjectName("graphicsView_2")
		self.graphicsView_2.setLabel('bottom', 'Samples')
		self.graphicsView_2.setLabel('left', 'Duty Cycle [%]')
		self.graphicsView_2.setYRange(0, 1, padding=0.01)

		self.pushButton = QtWidgets.QPushButton(self.stack)
		self.pushButton.setGeometry(QtCore.QRect(270, 60, 113, 32))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Run Test")

		self.comboBox = QtWidgets.QComboBox(self.stack)
		self.comboBox.setGeometry(QtCore.QRect(100, 60, 141, 32))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.setStyleSheet("color: rgb(46, 117, 182);\n"
		"font: 10pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 25px;")

		self.comboBox.addItems(["Obtain Samples", "Charact. Curves", "Calibrate Array", "Test4"])
	
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

    
	def Test_ObtainSample(self, iDNA_driver):
		print("Running Test: Obtain samples")
		iDNA_driver.SetupPlots(self.graphicsView, self.graphicsView_2)
		iDNA_driver.RequestFrame()
		
	def Test_CharactCurves(self, iDNA_driver):
		print("Running Test: Obtain Characterisation Curves")
		iDNA_driver.SetupPlots(self.graphicsView, self.graphicsView_2)
		iDNA_driver.ObtainCharactCurves()
		
	def Test_CalibArray(self, iDNA_driver):
		print("Running Test: Calibrate Array")
		iDNA_driver.SetupPlots(self.graphicsView, self.graphicsView_2)
		iDNA_driver.CalibArray()

	def Test3(self, iDNA_driver):
		print("Test 3")
    
	def display(self, iDNA_driver):
		self.comboText = int(self.comboBox.currentIndex())
		if self.comboText == 0:
			self.Test_ObtainSample(iDNA_driver)
		if self.comboText == 1:
			self.Test_CharactCurves(iDNA_driver)
		if self.comboText == 2:
			self.Test_CalibArray(iDNA_driver)
		if self.comboText == 3:
			self.Test3(iDNA_driver)   

	def __init__(self, Main, iDNA_driver):
		self.stack = QtWidgets.QWidget()
		self.setupUi()
		self.pushButton.clicked.connect(partial(self.display, iDNA_driver))
		self.exit.clicked.connect(Main.OpenMainMenu)
		self.exit.clicked.connect(iDNA_driver.EndOngoingTest)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	runTests = QtWidgets.QDialog()
	ui = Ui_runTests()
	ui.setupUi(runTests)
	runTests.show()
	sys.exit(app.exec_())

