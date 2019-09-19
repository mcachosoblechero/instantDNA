from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

from Src.ui_Main import Ui_Main

class Main(QMainWindow, Ui_Main):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	showMain = Main()
	sys.exit(app.exec_())