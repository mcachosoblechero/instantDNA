# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseFirst.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from diagnoseSecond import Ui_secondPage
from datetime import datetime
import sys


class Ui_firstPage(object):
    
    def open2(self):
        data2 = [
            "Name: " + str(self.lineEdit_1.text()),
            "Surname: " + str(self.lineEdit_2.text()),
            "Nationality: " + str(self.lineEdit_4.text()),
            "ID number: " + str(self.lineEdit_5.text())
            ]
        #print (data2)

        #filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
        #f= sys.stdout = open(filename1 + '.txt', 'w')
        f = open("first_patient.txt", "w+")
        for line in data2:
            # write line to output file
            f.write(line)
            f.write("\n")

            

        self.window=QtWidgets.QDialog() 
        self.ui = Ui_secondPage()
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.show()

    def setupUi(self, firstPage):
        firstPage.setObjectName("firstPage")
        firstPage.resize(480, 800)
        firstPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        firstPage.setIconSize(QtCore.QSize(70, 70))
        self.centralwidget = QtWidgets.QWidget(firstPage)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 180, 101, 41))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"color: rgb(46, 117, 182);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(120, 320, 141, 41))
        self.textBrowser_6.setStyleSheet("background-color: transparent;\n"
"color: rgb(46, 117, 182);\n"
"")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(120, 420, 141, 41))
        self.textBrowser_7.setStyleSheet("background-color: transparent;\n"
"color: rgb(46, 117, 182);\n"
"")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(230, 180, 191, 31))
        self.lineEdit_1.setStyleSheet("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.nationality = QtWidgets.QLabel(self.centralwidget)
        self.nationality.setGeometry(QtCore.QRect(50, 310, 61, 61))
        self.nationality.setText("")
        self.nationality.setPixmap(QtGui.QPixmap(":/newPrefix/nationality.png"))
        self.nationality.setScaledContents(True)
        self.nationality.setObjectName("nationality")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(50, 410, 61, 61))
        self.id.setText("")
        self.id.setPixmap(QtGui.QPixmap(":/newPrefix/ID.png"))
        self.id.setScaledContents(True)
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(50, 190, 61, 61))
        self.name.setText("")
        self.name.setPixmap(QtGui.QPixmap(":/newPrefix/name.png"))
        self.name.setScaledContents(True)
        self.name.setObjectName("name")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 230, 191, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 320, 191, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 420, 191, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 230, 101, 41))
        self.textBrowser_3.setStyleSheet("color: rgb(46, 117, 182);\n"
"background-color: transparent;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 710, 470, 60))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.continue1 = QtWidgets.QPushButton(self.centralwidget)
        self.continue1.setGeometry(QtCore.QRect(140, 530, 200, 52))
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

        self.continue1.clicked.connect(self.open2)#
         
        self.personal_details = QtWidgets.QLabel(self.centralwidget)
        self.personal_details.setGeometry(QtCore.QRect(55, 45, 361, 60))
        self.personal_details.setStyleSheet("background-color: transparent;\n"
"font: 44pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.personal_details.setObjectName("personal_details")
        #self.back1 = QtWidgets.QPushButton(self.centralwidget)
        #self.back1.setGeometry(QtCore.QRect(20, 660, 100, 40))
        """self.back1.setStyleSheet("font: 22pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")"""
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(":/newPrefix/back_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.back1.setIcon(icon)
        #self.back1.setIconSize(QtCore.QSize(22, 36))
        #self.back1.setAutoDefault(False)
        #self.back1.setDefault(True)
        #self.back1.setFlat(False)
        #self.back1.setObjectName("back1")
        self.textBrowser_6.raise_()
        self.lineEdit_1.raise_()
        self.nationality.raise_()
        self.id.raise_()
        self.name.raise_()
        self.textBrowser.raise_()
        self.textBrowser_7.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.textBrowser_3.raise_()
        self.label_2.raise_()
        self.continue1.raise_()
        self.personal_details.raise_()
        #self.back1.raise_()
        firstPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(firstPage)
        self.statusbar.setObjectName("statusbar")
        firstPage.setStatusBar(self.statusbar)

        self.retranslateUi(firstPage)
        self.continue1.clicked.connect(firstPage.close)

        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        _translate = QtCore.QCoreApplication.translate
        firstPage.setWindowTitle(_translate("firstPage", "MainWindow"))
        self.textBrowser.setHtml(_translate("firstPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Name</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("firstPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Nationality</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("firstPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">ID number</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("firstPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Surname</span></p></body></html>"))
        self.continue1.setText(_translate("firstPage", "CONTINUE"))
        self.personal_details.setText(_translate("firstPage", " Personal details"))
        #self.back1.setText(_translate("firstPage", "BACK"))

import First_page_file


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstPage = QtWidgets.QMainWindow()
    ui = Ui_firstPage()
    ui.setupUi(firstPage)
    firstPage.show()
    sys.exit(app.exec_())



 #self.input1 = "Name: " + str(self.lineEdit_1.text())
        #self.input2 = "Surname: " + str(self.lineEdit_2.text())
        #self.input4 = "Nationality: " + str(self.lineEdit_4.text())
        #self.input5 = "ID number: " + str(self.lineEdit_5.text())
        #data1 = []
        #data1.append(self.input1)
        #data1.append(self.input2)
        #data1.append(self.input4)
        #data1.append(self.input5)


