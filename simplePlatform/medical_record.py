# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical_record.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import record_file
import csv
from functools import partial

class Ui_Dialog(object):
    def __init__(self, number):
        self.number = number
        print(number)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 430)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(20, 20, 360, 320))
        self.listView.setObjectName("listView")
        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(110, 360, 180, 45))
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

        with open('dataFile.csv') as csvfile:
            data = []
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        f = data[self.number] # need to change the value of this to pick correct row

        data2 = [
            "Name: " + str(f[0]),
            "Surname: " + str(f[1]),
            "Nationality: " + str(f[2]),
            "ID number: " + str(f[3]),
            "Age: " + str(f[4]),
            "Body Temperature: " + str(f[5]),
            "Gender: " + str(f[6]),
            "Weight (Kg): " + str(f[7]),
            "Height (cm): " + str(f[8]),
            "Respiration rate (bpm): " + str(f[9]),
            "Heart rate (bpm): " + str(f[10]),
            "Blood Pressure (mmHg): " + str(f[11]),
            "Symptoms: " + str(f[12])
            ]

        for item in data2:
            data = QtGui.QStandardItem(item)
            self.model.appendRow(data)
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.close.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Medical report"))
        self.close.setText(_translate("Dialog", "OK"))


class Ui_record1(object):
    def display(self, number):  
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_Dialog(number)
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.show()
    def setupUi(self, record1):
        record1.setObjectName("record1")
        record1.resize(480, 820)
        record1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget = QtWidgets.QTabWidget(record1)
        self.tabWidget.setGeometry(QtCore.QRect(0, -35, 481, 840))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 280, 420, 3))
        self.label_4.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 420, 3))
        self.label_5.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 420, 3))
        self.label_3.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.patient1 = QtWidgets.QLabel(self.tab)
        self.patient1.setGeometry(QtCore.QRect(100, 205, 230, 57))
        self.patient1.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient1.setText("")
        self.patient1.setObjectName("patient1")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 480, 420, 3))
        self.label_11.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(60, 50, 380, 65))
        self.label_10.setStyleSheet("background-color: transparent;\n"
"font: 36pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(30, 580, 420, 3))
        self.label_14.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.report1 = QtWidgets.QPushButton(self.tab)
        self.report1.setGeometry(QtCore.QRect(320, 194, 75, 71))
        self.report1.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report1.setText("")
        self.report1.setObjectName("report1")
        self.report1.clicked.connect(self.display)
        self.report2 = QtWidgets.QPushButton(self.tab)
        self.report2.setGeometry(QtCore.QRect(320, 294, 75, 71))
        self.report2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report2.setText("")
        self.report2.setObjectName("report2")
        self.report3 = QtWidgets.QPushButton(self.tab)
        self.report3.setGeometry(QtCore.QRect(320, 394, 75, 71))
        self.report3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report3.setText("")
        self.report3.setObjectName("report3")
        self.report4 = QtWidgets.QPushButton(self.tab)
        self.report4.setGeometry(QtCore.QRect(320, 494, 75, 71))
        self.report4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report4.setText("")
        self.report4.setObjectName("report4")

                
        self.continue2 = QtWidgets.QPushButton(self.tab)
        self.continue2.setGeometry(QtCore.QRect(140, 660, 200, 52))
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

        self.right1 = QtWidgets.QPushButton(self.tab)# add the name of the tab
        self.right1.setGeometry(QtCore.QRect(340, 650, 80, 70))
        self.right1.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/right.png);")
        self.right1.setText("")
        self.right1.setObjectName("right1")
        self.left1 = QtWidgets.QPushButton(self.tab)
        self.left1.setGeometry(QtCore.QRect(60, 650, 80, 70))
        self.left1.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/left.png);")
        self.left1.setText("")
        self.left1.setObjectName("left1")

        self.right1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        
        self.patient2 = QtWidgets.QLabel(self.tab)
        self.patient2.setGeometry(QtCore.QRect(100, 305, 230, 57))
        self.patient2.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient2.setText("")
        self.patient2.setObjectName("patient2")
        self.patient3 = QtWidgets.QLabel(self.tab)
        self.patient3.setGeometry(QtCore.QRect(100, 405, 230, 57))
        self.patient3.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient3.setText("")
        self.patient3.setObjectName("patient3")
        self.patient4 = QtWidgets.QLabel(self.tab)
        self.patient4.setGeometry(QtCore.QRect(100, 505, 230, 57))
        self.patient4.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient4.setText("")
        self.patient4.setObjectName("patient4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 420, 3))
        self.label_6.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 420, 3))
        self.label_7.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 300, 420, 3))
        self.label_8.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 400, 420, 3))
        self.label_9.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(30, 500, 420, 3))
        self.label_12.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 600, 420, 3))
        self.label_13.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.continue3 = QtWidgets.QPushButton(self.tab_2)
        self.continue3.setGeometry(QtCore.QRect(140, 660, 200, 52))
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

        self.right2 = QtWidgets.QPushButton(self.tab_2)# add the name of the tab
        self.right2.setGeometry(QtCore.QRect(340, 650, 80, 70))
        self.right2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/right.png);")
        self.right2.setText("")
        self.right2.setObjectName("right2")
        self.left2 = QtWidgets.QPushButton(self.tab_2)
        self.left2.setGeometry(QtCore.QRect(60, 650, 80, 70))
        self.left2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/left.png);")
        self.left2.setText("")
        self.left2.setObjectName("left2")
        self.right2.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.left2.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))

        
        self.report6 = QtWidgets.QPushButton(self.tab_2)
        self.report6.setGeometry(QtCore.QRect(320, 215, 75, 71))
        self.report6.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report6.setText("")
        self.report6.setObjectName("report6")
        self.report7 = QtWidgets.QPushButton(self.tab_2)
        self.report7.setGeometry(QtCore.QRect(320, 315, 75, 71))
        self.report7.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report7.setText("")
        self.report7.setObjectName("report7")
        self.report8 = QtWidgets.QPushButton(self.tab_2)
        self.report8.setGeometry(QtCore.QRect(320, 415, 75, 71))
        self.report8.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report8.setText("")
        self.report8.setObjectName("report8")
        self.report9 = QtWidgets.QPushButton(self.tab_2)
        self.report9.setGeometry(QtCore.QRect(320, 515, 75, 71))
        self.report9.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report9.setText("")
        self.report9.setObjectName("report9")
        self.report5 = QtWidgets.QPushButton(self.tab_2)
        self.report5.setGeometry(QtCore.QRect(320, 115, 75, 71))
        self.report5.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report5.setText("")
        self.report5.setObjectName("report5")
        self.patient5 = QtWidgets.QLabel(self.tab_2)
        self.patient5.setGeometry(QtCore.QRect(100, 135, 230, 57))
        self.patient5.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient5.setText("")
        self.patient5.setObjectName("patient5")
        self.patient6 = QtWidgets.QLabel(self.tab_2)
        self.patient6.setGeometry(QtCore.QRect(100, 225, 230, 57))
        self.patient6.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient6.setText("")
        self.patient6.setObjectName("patient6")
        self.patient7 = QtWidgets.QLabel(self.tab_2)
        self.patient7.setGeometry(QtCore.QRect(100, 325, 230, 57))
        self.patient7.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient7.setText("")
        self.patient7.setObjectName("patient7")
        self.patient8 = QtWidgets.QLabel(self.tab_2)
        self.patient8.setGeometry(QtCore.QRect(100, 425, 230, 57))
        self.patient8.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient8.setText("")
        self.patient8.setObjectName("patient8")
        self.patient9 = QtWidgets.QLabel(self.tab_2)
        self.patient9.setGeometry(QtCore.QRect(100, 525, 230, 57))
        self.patient9.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient9.setText("")
        self.patient9.setObjectName("patient9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(30, 100, 420, 3))
        self.label_15.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(30, 200, 420, 3))
        self.label_16.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 300, 420, 3))
        self.label_17.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(30, 400, 420, 3))
        self.label_18.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(30, 600, 420, 3))
        self.label_19.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(30, 500, 420, 3))
        self.label_20.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.report10 = QtWidgets.QPushButton(self.tab_3)
        self.report10.setGeometry(QtCore.QRect(320, 115, 75, 71))
        self.report10.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report10.setText("")
        self.report10.setObjectName("report10")
        self.report11 = QtWidgets.QPushButton(self.tab_3)
        self.report11.setGeometry(QtCore.QRect(320, 215, 75, 71))
        self.report11.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report11.setText("")
        self.report11.setObjectName("report11")
        self.report12 = QtWidgets.QPushButton(self.tab_3)
        self.report12.setGeometry(QtCore.QRect(320, 315, 75, 71))
        self.report12.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report12.setText("")
        self.report12.setObjectName("report12")
        self.report13 = QtWidgets.QPushButton(self.tab_3)
        self.report13.setGeometry(QtCore.QRect(320, 415, 75, 71))
        self.report13.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report13.setText("")
        self.report13.setObjectName("report13")
        self.report14 = QtWidgets.QPushButton(self.tab_3)
        self.report14.setGeometry(QtCore.QRect(320, 515, 75, 71))
        self.report14.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report14.setText("")
        self.report14.setObjectName("report14")
        self.patient10 = QtWidgets.QLabel(self.tab_3)
        self.patient10.setGeometry(QtCore.QRect(100, 125, 230, 57))
        self.patient10.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient10.setText("")
        self.patient10.setObjectName("patient10")
        self.patient11 = QtWidgets.QLabel(self.tab_3)
        self.patient11.setGeometry(QtCore.QRect(100, 225, 230, 57))
        self.patient11.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient11.setText("")
        self.patient11.setObjectName("patient11")
        self.patient12 = QtWidgets.QLabel(self.tab_3)
        self.patient12.setGeometry(QtCore.QRect(100, 325, 230, 57))
        self.patient12.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient12.setText("")
        self.patient12.setObjectName("patient12")
        self.patient13 = QtWidgets.QLabel(self.tab_3)
        self.patient13.setGeometry(QtCore.QRect(100, 425, 230, 57))
        self.patient13.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient13.setText("")
        self.patient13.setObjectName("patient13")
        self.patient14 = QtWidgets.QLabel(self.tab_3)
        self.patient14.setGeometry(QtCore.QRect(100, 525, 230, 57))
        self.patient14.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient14.setText("")
        self.patient14.setObjectName("patient14")
        self.continue4 = QtWidgets.QPushButton(self.tab_3)
        self.continue4.setGeometry(QtCore.QRect(140, 660, 200, 52))
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

        self.right3 = QtWidgets.QPushButton(self.tab_3)# add the name of the tab
        self.right3.setGeometry(QtCore.QRect(340, 650, 80, 70))
        self.right3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/right.png);")
        self.right3.setText("")
        self.right3.setObjectName("right3")
        self.left3 = QtWidgets.QPushButton(self.tab_3)
        self.left3.setGeometry(QtCore.QRect(60, 650, 80, 70))
        self.left3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/left.png);")
        self.left3.setText("")
        self.left3.setObjectName("left3")
        self.right3.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.left3.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.continue5 = QtWidgets.QPushButton(self.tab_4)
        self.continue5.setGeometry(QtCore.QRect(140, 660, 200, 52))
        self.continue5.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue5.setAutoDefault(False)
        self.continue5.setDefault(True)
        self.continue5.setFlat(False)

        self.right4 = QtWidgets.QPushButton(self.tab_4)# add the name of the tab
        self.right4.setGeometry(QtCore.QRect(340, 650, 80, 70))
        self.right4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/right.png);")
        self.right4.setText("")
        self.right4.setObjectName("right4")
        self.left4 = QtWidgets.QPushButton(self.tab_4)
        self.left4.setGeometry(QtCore.QRect(60, 650, 80, 70))
        self.left4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/left.png);")
        self.left4.setText("")
        self.left4.setObjectName("left4")
        self.left4.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))

        
        self.continue5.setObjectName("continue5")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(30, 100, 420, 3))
        self.label_21.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(30, 200, 420, 3))
        self.label_22.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(30, 300, 420, 3))
        self.label_23.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(30, 400, 420, 3))
        self.label_24.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(30, 500, 420, 3))
        self.label_25.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(30, 600, 420, 3))
        self.label_26.setStyleSheet("background-color: rgb(46, 117, 182);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.report15 = QtWidgets.QPushButton(self.tab_4)
        self.report15.setGeometry(QtCore.QRect(320, 115, 75, 71))
        self.report15.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report15.setText("")
        self.report15.setObjectName("report15")
        self.report16 = QtWidgets.QPushButton(self.tab_4)
        self.report16.setGeometry(QtCore.QRect(320, 215, 75, 71))
        self.report16.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report16.setText("")
        self.report16.setObjectName("report16")
        self.report18 = QtWidgets.QPushButton(self.tab_4)
        self.report18.setGeometry(QtCore.QRect(320, 415, 75, 71))
        self.report18.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report18.setText("")
        self.report18.setObjectName("report18")
        self.report17 = QtWidgets.QPushButton(self.tab_4)
        self.report17.setGeometry(QtCore.QRect(320, 315, 75, 71))
        self.report17.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report17.setText("")
        self.report17.setObjectName("report17")
        self.report19 = QtWidgets.QPushButton(self.tab_4)
        self.report19.setGeometry(QtCore.QRect(320, 515, 75, 71))
        self.report19.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/newPrefix/report.png);")
        self.report19.setText("")
        self.report19.setObjectName("report19")
        self.patient15 = QtWidgets.QLabel(self.tab_4)
        self.patient15.setGeometry(QtCore.QRect(100, 125, 230, 57))
        self.patient15.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient15.setText("")
        self.patient15.setObjectName("patient15")
        self.patient16 = QtWidgets.QLabel(self.tab_4)
        self.patient16.setGeometry(QtCore.QRect(100, 225, 230, 57))
        self.patient16.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient16.setText("")
        self.patient16.setObjectName("patient16")
        self.patient17 = QtWidgets.QLabel(self.tab_4)
        self.patient17.setGeometry(QtCore.QRect(100, 325, 230, 57))
        self.patient17.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient17.setText("")
        self.patient17.setObjectName("patient17")
        self.patient18 = QtWidgets.QLabel(self.tab_4)
        self.patient18.setGeometry(QtCore.QRect(100, 425, 230, 57))
        self.patient18.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient18.setText("")
        self.patient18.setObjectName("patient18")
        self.patient19 = QtWidgets.QLabel(self.tab_4)
        self.patient19.setGeometry(QtCore.QRect(100, 525, 230, 57))
        self.patient19.setStyleSheet("font: 13pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;\n"
"")
        self.patient19.setText("")
        self.patient19.setObjectName("patient19")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(record1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(record1)

        self.continue2.clicked.connect(record1.close)
        self.continue3.clicked.connect(record1.close)
        self.continue4.clicked.connect(record1.close)
        self.continue5.clicked.connect(record1.close)

        reports = [self.report1, self.report2, self.report3, self.report4, self.report5,
                   self.report6, self.report7, self.report8, self.report9, self.report10,
                   self.report11, self.report12, self.report13, self.report14, self.report15,
                   self.report16, self.report17, self.report18, self.report19
                   ]
        with open('dataFile.csv') as csvfile:
            data = []
            reader = csv.reader(csvfile)
            for row in reader:
                 data.append(row)
            
        for i in range(len(data)-1):
            reports[i].clicked.connect(partial(self.display, number=i+1))
            

       

    def retranslateUi(self, record1):
        _translate = QtCore.QCoreApplication.translate
        record1.setWindowTitle(_translate("record1", "Dialog"))
        self.label_10.setText(_translate("record1", "Medical Record"))
        self.continue2.setText(_translate("record1", "Main page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("record1", "Page 1"))
        self.continue3.setText(_translate("record1", "Main page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("record1", "Page 2"))
        self.continue4.setText(_translate("record1", "Main page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("record1", "Page 3"))
        self.continue5.setText(_translate("record1", "Main page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("record1", "Page 4"))

        with open('dataFile.csv') as csvfile:
            data = []
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)


        patients = [self.patient1, self.patient2, self.patient3, self.patient4, self.patient5, self.patient6,
                    self.patient7, self.patient8, self.patient9, self.patient10, self.patient11, self.patient12,
                    self.patient13, self.patient14, self.patient15, self.patient16, self.patient17, self.patient18,
                    self.patient19
                    ]
        for i in range(1, len(data)):
            f = data[i]
            name = str(f[0]) + " " + str(f[1])
            patients[i-1].setText(_translate("record1", name))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    record1 = QtWidgets.QDialog()
    ui = Ui_record1()
    ui.setupUi(record1)
    record1.show()
    sys.exit(app.exec_())

