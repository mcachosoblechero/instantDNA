from PyQt5 import QtCore, QtGui, QtWidgets
from Src.debug_menu import Ui_DebugMenu
from Src.debug_settings import Ui_DebugSettings
from Src.debug_runtest import Ui_DebugRunTest
from Src.Diagnose_S1 import Ui_Diagnose_S1
from Src.Diagnose_S2 import Ui_Diagnose_S2
from Src.Diagnose_S3 import Ui_Diagnose_S3
from Src.Diagnose_S4 import Ui_Diagnose_S4
from Src.Diagnose_S5 import Ui_Diagnose_S5
from Src.Diagnose_S6 import Ui_Diagnose_S6
from Src.MedicalRecord import Ui_MedicalRecord
from Src import MediaResources
from Src import MediaResources_Diagnose
from Src import MediaResources_MedicalRecords
from Src import MediaResources_DebugSettings
from Src import MediaResources_TestRunning

import sys

class Ui_Main(QtWidgets.QWidget):

	def setupUi(self, Main):
		Main.setObjectName("instantDNA")

		self.QtStack = QtWidgets.QStackedLayout()
		
		# Create all screen objects
		self.Ui_Diagnose_S1 	= Ui_Diagnose_S1(self)
		self.Ui_Diagnose_S2 	= Ui_Diagnose_S2(self)
		self.Ui_Diagnose_S3 	= Ui_Diagnose_S3(self)
		self.Ui_Diagnose_S4 	= Ui_Diagnose_S4(self)
		self.Ui_Diagnose_S5 	= Ui_Diagnose_S5(self)
		self.Ui_Diagnose_S6 	= Ui_Diagnose_S6(self)		
		self.Ui_MedicalRecord 	= Ui_MedicalRecord(self)
		self.Ui_DebugMenu 		= Ui_DebugMenu(self)
		self.Ui_DebugSettings 	= Ui_DebugSettings(self)
		self.Ui_DebugRunTest 	= Ui_DebugRunTest(self)
				
		# Create main stack layers
		self.stack_Main 				= QtWidgets.QWidget()

		# Create main stack layout
		self.MainMenuUI()
		self.showFullScreen()

		# Create stack
		self.QtStack.insertWidget(0, self.stack_Main)
		self.QtStack.insertWidget(1, self.Ui_Diagnose_S1.stack)
		self.QtStack.insertWidget(2, self.Ui_Diagnose_S2.stack)	
		self.QtStack.insertWidget(3, self.Ui_Diagnose_S3.stack)		
		self.QtStack.insertWidget(4, self.Ui_Diagnose_S4.stack)	
		self.QtStack.insertWidget(5, self.Ui_Diagnose_S5.stack)		
		self.QtStack.insertWidget(6, self.Ui_Diagnose_S6.stack)			
		self.QtStack.insertWidget(7, self.Ui_MedicalRecord.stack)
		self.QtStack.insertWidget(8, self.Ui_DebugMenu.stack)
		self.QtStack.insertWidget(9, self.Ui_DebugSettings.stack)
		self.QtStack.insertWidget(10, self.Ui_DebugRunTest.stack)
		
		# Create connections
		self.PushButton1.clicked.connect(self.OpenDiagnose_S1)
		self.PushButton2.clicked.connect(self.OpenMedicalRecords_T1)
		self.PushButton3.clicked.connect(self.OpenDebugMenu)
	
	def OpenMainMenu(self):
		self.QtStack.setCurrentIndex(0)
	
	def OpenDiagnose_S1(self):
		self.QtStack.setCurrentIndex(1)

	def OpenDiagnose_S2(self):
		self.QtStack.setCurrentIndex(2)

	def OpenDiagnose_S3(self):
		self.QtStack.setCurrentIndex(3)

	def OpenDiagnose_S4(self):
		self.QtStack.setCurrentIndex(4)

	def OpenDiagnose_S5(self):
		self.QtStack.setCurrentIndex(5)

	def OpenDiagnose_S6(self):
		self.QtStack.setCurrentIndex(6)

	def OpenMedicalRecords_T1(self):
		self.QtStack.setCurrentIndex(7)
		
	def OpenDebugMenu(self):
		self.QtStack.setCurrentIndex(8)

	def OpenDebugSettings(self):
		self.QtStack.setCurrentIndex(9)
		
	def OpenDebugRunTest(self):
		self.QtStack.setCurrentIndex(10)
		
	# Define Main screen
	def MainMenuUI(self): 
		self.stack_Main.resize(480, 799)
		self.stack_Main.setStyleSheet("background-color: rgb(255, 255, 255);")

        #PushButton1#
		self.PushButton1 = QtWidgets.QPushButton(self.stack_Main)
		self.PushButton1.setGeometry(QtCore.QRect(10, 110, 460, 181))
		self.PushButton1.setStyleSheet("border-image: url(:/newPrefix/diagnose.png);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 28pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 25px;")
		self.PushButton1.setText("   Diagnose")

        #PushButton2#
		self.PushButton2 = QtWidgets.QPushButton(self.stack_Main)
		self.PushButton2.setGeometry(QtCore.QRect(10, 310, 460, 181))
		self.PushButton2.setStyleSheet("color: rgb(46, 117, 182);\n"
		"border-image: url(:/newPrefix/medical_record.png);\n"
		"font: 28pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 25px")
		self.PushButton2.setText("            Medical record")
		
		#PushButton3#
		self.PushButton3 = QtWidgets.QPushButton(self.stack_Main)
		self.PushButton3.setGeometry(QtCore.QRect(10, 510, 460, 181))
		self.PushButton3.setStyleSheet("border-image: url(:/newPrefix/debug.png);\n"
		"color: rgb(46, 117, 182);\n"
		"font: 28pt \"Arial Rounded MT Bold\";\n"
		"border-radius: 25px\n"
		"")
		self.PushButton3.setText("Debug")
		
	def SetPatientDetails_S1(self, New, Name, Surname, Nationality, ID):
		self.Patient_ID = ID
		self.Patient_Name = Name
		self.Patient_Surname = Surname
		self.Patient_Nationality = Nationality
		self.NewPatient = New
		
	def SetPatientDetails_S2(self, Age, BodyTemp, Gender):
		self.Patient_Age = Age
		self.Patient_BodyTemp = BodyTemp
		self.Patient_Gender = Gender
		
	def SetPatientDetails_S3(self, Weight, Height, RespRate, HR, BloodPress):
		self.Patient_Weight = Weight
		self.Patient_Height = Height
		self.Patient_RespRate = RespRate
		self.Patient_HR = HR
		self.Patient_BloodPress = BloodPress
		
	def SetPatientDetails_S4(self, Symptoms):
		self.Patient_Symptoms = ""
		for i in Symptoms:
			self.Patient_Symptoms = self.Patient_Symptoms + i + " "
