# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Src.coloredGraph import MplCmapImageView
import pyqtgraph as pg
import time
from functools import partial

class Ui_Diagnose_S6(object):
	def setupUi(self):
	
		self.stack.setObjectName("self.stack")
		self.stack.resize(480, 800)
		self.stack.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.nurse = QtWidgets.QLabel(self.stack)
		self.nurse.setGeometry(QtCore.QRect(30, 20, 227.5, 162.5))
		self.nurse.setText("")
		self.nurse.setPixmap(QtGui.QPixmap(":/newPrefix/doctor3.png"))
		self.nurse.setScaledContents(True)
		self.nurse.setObjectName("nurse")

		self.textLabel = QtWidgets.QLabel(self.stack)
		self.textLabel.setGeometry(QtCore.QRect(110, 35, 211, 41))
		self.textLabel.setStyleSheet("background-color: transparent;")
		self.textLabel.setText("")
		self.textLabel.setObjectName("textLabel")

		self.continue1 = QtWidgets.QPushButton(self.stack)
		self.continue1.setGeometry(QtCore.QRect(270, 20, 200, 80))
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
		self.continue1.setObjectName("continue1")
		self.continue1.setText("Start Test")

		self.continue2 = QtWidgets.QPushButton(self.stack)
		self.continue2.setGeometry(QtCore.QRect(270, 110, 200, 80))
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
		self.continue2.setText("End Test")

		self.graphicsView = MplCmapImageView(parent=self.stack) 
		self.graphicsView.setGeometry(QtCore.QRect(10, 200, 450, 330))
		self.graphicsView.setObjectName("graphicsView")
		self.graphicsView.ui.roiBtn.hide() #added this bit of code to remoce roi and memu buttons as we dont need them
		self.graphicsView.ui.menuBtn.hide()

		self.graphicsView_2 = pg.PlotWidget(self.stack)
		self.graphicsView_2.setGeometry(QtCore.QRect(10, 550, 450, 200))
		self.graphicsView_2.setObjectName("graphicsView_2")
		self.graphicsView_2.setLabel('bottom', 'Samples')
		self.graphicsView_2.setLabel('left', 'Duty Cycle [%]')
		self.graphicsView_2.setYRange(0, 1, padding=0.01)

		self.retranslateUi()

	def RunTest(self, iDNA_driver):
		if (iDNA_driver.State == "Ready"):
			iDNA_driver.RunningDNATest = 1
			iDNA_driver.SetupTextBox(self.textLabel)
			iDNA_driver.SetupPlots(self.graphicsView, self.graphicsView_2)

			iDNA_driver.DNATest()

	def EndTest(self, Main, iDNA_driver):
		iDNA_driver.EndOngoingTest()
		Main.OpenMainMenu()

	def retranslateUi(self):
		self.stack.setWindowTitle("Diagnosis - Stage 6")

	def __init__(self, Main, iDNA_driver):
		self.stack = QtWidgets.QWidget()
		self.DisplayList = ["Heating the solution", "Calibrating platform", "Sampling ISFETs", "Amplifying DNA", "Detecting changes in pH", "Preparing diagnosis"]
		self.StateList = list(range(len(self.DisplayList)))
		self.setupUi()
		self.continue1.clicked.connect(partial(self.RunTest, iDNA_driver))
		self.continue2.clicked.connect(partial(self.EndTest, Main, iDNA_driver))
		

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

