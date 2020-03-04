import pigpio
import time
import struct
import numpy as np
from datetime import datetime
from Driver.STM_Interface import STM_Interface
from Driver.Controller import ListControllers, debug_Controller, DriftAnalysis_Controller
from Driver.FSM import State, Transition, FSM
from Driver.Actions import List_Actions

class instantDNA:
	def __init__(self):
		self.now = datetime.now()
		self.Test_StartTime = datetime.now()
		self.NumSample = 0
		self.RefElectVoltage = -1.5;
		self.DeltaRefElect = 0.025; 
		self.StoredAvFrames_DutyCycle = list()
		self.StoredAvFrames_Frequency = list()
		self.StoredPixels_DutyCycle = list()
		self.StoredPixels_Frequency = list()
		self.StoredRefTemp = list()
		self.CalibValues = list()
		self.RunningDNATest = 0
		self.Patient_Diagnosis = False
		self.State = "Ready"

		#########################
		# Interfaces		#
		#########################
		self.STM_Interface = STM_Interface()
		self.STM_Interface.pi.callback(7,pigpio.RISING_EDGE, self.isr_frame)
		
		
		#########################
		# Platform Controllers	#
		#########################
		self.CmdBoard = ListControllers()
		self.CmdBoard.addController(debug_Controller("Debug", self.STM_Interface, 10))
		self.CmdBoard.addController(DriftAnalysis_Controller("Drift", self.STM_Interface, 10))
		
		self.HelloWorld()

	def __del__(self):
		self.STM_Interface.close()
	######################################################

	######################################################
	# INTERRUPT ##########################################
	######################################################			
	def isr_frame(self, gpio, level, tick):
		print("Interrupt!")
		for i in self.CmdBoard.Controllers.keys():
			if self.CmdBoard.Controllers[i].InterruptEnable == True:
				self.CmdBoard.Controllers[i].InterruptReady = True

	######################################################	

	######################################################
	# DRIVER METHODS #####################################
	######################################################
	def HelloWorld(self):
		print("Welcome to InstantDNA!")
	######################################################

	####################################################
	# DEMO METHODS #####################################
	####################################################
	def RunLottery(self):
		value = np.random.randint(2,size = 1)
		if (value == 1):
			return True
		else:
			return False

	def FakepH(self):
		if len(self.StoredAvFrames_DutyCycle) > 55 and len(self.StoredAvFrames_DutyCycle) < 65:
			spi_message = [9] + list(bytearray(struct.pack("f",1.0)))
			(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
	#####################################################
