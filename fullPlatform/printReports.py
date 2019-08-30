# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import record_file
import csv
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy as np
import pandas as pd

pg.setConfigOption('background', 'w')


class Ui_Dialog(object):


    def nextPage(self):
         # pandas method to extract the same user
        if (self.page < self.numOfRecords-1):
            self.page = self.page + 1
            temp = self.recordDataFrame.iloc[self.page].values
            self.updateUI(temp)
##        if (self.page == self.numOfRecords-1):
##            self.right0.setStyleSheet("background-color: transparent;\n"
##"")
##            self.left0.setStyleSheet("background-color: transparent;\n"
##"border-image: url(:/newPrefix/left.png);")
            
                
    def prevPage(self):
        if (self.page > 0):
            self.page = self.page - 1
            temp = self.recordDataFrame.iloc[self.page].values
            self.updateUI(temp)
##        if (self.page == 0):
##            self.left0.setStyleSheet("background-color: transparent;\n"
##"")
##            self.right0.setStyleSheet("background-color: transparent;\n"
##"border-image: url(:/newPrefix/right.png);")

        
    def __init__(self, number):
        self.number = int(number) + 1
        self.page = 0


    
    def setupUi(self, Dialog):

        #print(self.number)
        
        with open('patientData.csv') as csvfile:
            reader = csv.reader(csvfile)
            data =[]
            for row in reader:
                data.append(row)
        patient = data[self.number]
        surname = patient[1]
        #print(str(surname))


        file = pd.read_csv('dataFile.csv')
        users = file.Surname.str.contains(str(surname))
        self.recordDataFrame = file[users]
        self.numOfRecords = len(self.recordDataFrame)

        
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

            
##        with open('dataFile.csv') as csvfile:
##            data = []
##            reader = csv.reader(csvfile)
##            for row in reader:
##                data.append(row)
##        f = data[self.number] # need to change the value of this to pick correct row
        

        f = self.recordDataFrame.iloc[0].values
        self.updateUI(f)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.close.clicked.connect(Dialog.close)

    def updateUI(self, f):
        self.model.clear()
        data2 = [
            "Date of Test:                     " + str(f[13]),
            "  ",
            "Patient's Name:                 " + str(f[0]) + " " + str(f[1]),
            "Nationality:                         " + str(f[2]),
            "ID number:                          " + str(f[3]),
            "Age:                                     " + str(f[4]),
            "Body Temperature:            " + str(f[5]),
            "Gender:                               " + str(f[6]),
            "Weight (Kg):                        " + str(f[7]),
            "Height (cm):                        " + str(f[8]),
            "Respiration rate (bpm):      " + str(f[9]),
            "Heart rate (bpm):                " + str(f[10]),
            "Blood Pressure (mmHg):    " + str(f[11]),
            "Symptoms:                           " + str(f[12])
            
            ]

        x = np.linspace(0, 3, 50)
        y = np.exp(x)

        self.graphicsView.plot(x, y)

        self.right0.clicked.connect(self.nextPage)
        self.left0.clicked.connect(self.prevPage)

        for item in data2:
            data = QtGui.QStandardItem(item)
            self.model.appendRow(data)
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
       

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Medical report"))
        self.close.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(2)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

