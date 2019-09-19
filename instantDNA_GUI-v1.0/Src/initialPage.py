from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
#from diagnoseFirst import Ui_firstPage
#from medical_record import Ui_record1
#from debug1 import Ui_debugFirst

import sys

class Ui_MainWindow(object):
    def open2(self):  #setupUi as in other program
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_record1()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        
    def open1(self):  #setupUi as in other program
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_firstPage()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()

    def open3(self):  #setupUi as in other program
        self.window=QtWidgets.QDialog() 
        self.ui = Ui_debugFirst()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
		
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 799)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 460, 181))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/diagnose.png);\n"
"color: rgb(46, 117, 182);\n"
"font: 28pt \"Arial Rounded MT Bold\";\n"
"border-radius: 25px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 510, 460, 181))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/debug.png);\n"
"color: rgb(46, 117, 182);\n"
"font: 28pt \"Arial Rounded MT Bold\";\n"
"border-radius: 25px\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 310, 460, 181))
        self.pushButton_3.setStyleSheet("color: rgb(46, 117, 182);\n"
"border-image: url(:/newPrefix/medical_record.png);\n"
"font: 28pt \"Arial Rounded MT Bold\";\n"
"border-radius: 25px")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.open2)
        self.pushButton.clicked.connect(self.open1)#
        self.pushButton_2.clicked.connect(self.open3)#

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "   Diagnose"))
        self.pushButton_2.setText(_translate("MainWindow", "Debug"))
        self.pushButton_3.setText(_translate("MainWindow", "            Medical record"))

import initialPage_file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())

