# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runTests.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from coloredGraph import MplCmapImageView
import numpy as np
import pyqtgraph as pg
from pyqtgraph import ImageView
from pyqtgraph import PlotWidget

pg.setConfigOption('background', 'w') #placed before the loop

class Ui_runTests(object):
    def setupUi(self, runTests):
        runTests.setObjectName("runTests")
        runTests.resize(480, 800)
        runTests.setStyleSheet("")

        #configure the first window
        #self.graphicsView = QtWidgets.QGraphicsView(runTests)
        self.graphicsView = MplCmapImageView(parent=runTests) 
        self.graphicsView.setGeometry(QtCore.QRect(40, 130, 400, 300))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setLevels(0,250)
        self.graphicsView.ui.roiBtn.hide() #added this bit of code to remoce roi and memu buttons as we dont need them
        self.graphicsView.ui.menuBtn.hide()

        #configure the first window
        #self.graphicsView_2 = QtWidgets.QGraphicsView(runTests)
        self.graphicsView_2 = PlotWidget(runTests)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 460, 400, 200))
        self.graphicsView_2.setObjectName("graphicsView_2")

        
        self.pushButton = QtWidgets.QPushButton(runTests)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(runTests)
        self.comboBox.setGeometry(QtCore.QRect(100, 60, 141, 32))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItems(["Test1", "Test2", "Test3", "Test4"])
        self.pushButton.clicked.connect(self.display) # picks test and connects to signal

        
        self.save = QtWidgets.QPushButton(runTests)
        self.save.setGeometry(QtCore.QRect(110, 710, 111, 45))
        self.save.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"\n"
"\n"
"\n"
"")
        self.save.setAutoDefault(False)
        self.save.setDefault(True)
        self.save.setFlat(False)
        self.save.setObjectName("continue5")
        self.exit = QtWidgets.QPushButton(runTests)
        self.exit.setGeometry(QtCore.QRect(270, 710, 111, 45))
        self.exit.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"\n"
"\n"
"\n"
"")
        self.exit.setAutoDefault(False)
        self.exit.setDefault(True)
        self.exit.setFlat(False)
        self.exit.setObjectName("continue5_2")

        self.exit.clicked.connect(runTests.close)

        self.retranslateUi(runTests)
        QtCore.QMetaObject.connectSlotsByName(runTests)
    """
    def Test0(self):
        
    def Test1(self):
        
    def Test2(self):
       
    def Test3(self):
    """

    
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
            self.Test3()    #use a bracket when you call a function    

    def retranslateUi(self, runTests):
        _translate = QtCore.QCoreApplication.translate
        runTests.setWindowTitle(_translate("runTests", "Dialog"))
        self.pushButton.setText(_translate("runTests", "Run Test"))
        self.save.setText(_translate("runTests", "Save Results"))
        self.exit.setText(_translate("runTests", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    runTests = QtWidgets.QDialog()
    ui = Ui_runTests()
    ui.setupUi(runTests)
    runTests.show()
    sys.exit(app.exec_())

