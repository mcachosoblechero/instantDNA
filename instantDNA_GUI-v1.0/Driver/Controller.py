import os
from datetime import datetime
from PyQt5 import QtCore
from Driver.STM_Interface import STM_Interface
from Driver.IO_Plots import IO_Plots
from Driver.FSM import State, Transition, FSM
from Driver.Actions import List_Actions, Action, No_Action
from Driver.Conditions import Condition, Condition_Empty, Cond_SA_Ready, Cond_SA_Operation, Cond_UniqueTransition

class ListControllers(object):
	def __init__(self):
		self.Controllers = {}

	def addController(self, controller):
		self.Controllers[controller.name] = controller

	def isBusy(self):
		for i in self.Controllers.keys():
			if self.Controllers[i].ControllerBusy == True:
				return True
		return False
		
	def FinishAllActions(self):
		# To be done
		pass

class Controller(object):
	def __init__(self, name, Interface, Timeout=10):

		#########################################
		# EACH CONTROLLER INCLUDES AT LEAST:	#
		# - A list of actions			#
		# - An FSM with:			#
		# 	-> States [Action + Condition]	#
		#	-> Transition [Action]		#
		# - A timer that ticks the FSM		#
		# - A pointer to the STM Interface	#
		#########################################
		self.name = name
		self.FSM = FSM(self)
		self.Plots = IO_Plots()
		self.Timer = QtCore.QTimer()
		self.Timer.timeout.connect(self.FSM.Execute)
		self.Timeout = Timeout
		self.Interface = Interface	

		#########################
		# Actions Definitions	#
		#########################
		self.Actions = List_Actions(self)
		self.Actions.Create_Action("STM", "Frame", "RequestFrame", 6)
		self.Actions.Create_Action("STM", "Frame", "CharactCurves", 7)
		self.Actions.Create_Action("STM", "Frame", "CalibArray", 8)
		self.Actions.Create_Action("STM", "Frame", "LAMP", 10)
		self.Actions.Create_Action("STM", "RefTemp", "PCR", 11)
		self.Actions.Create_Action("STM", "Pixel", "TempControl", 12)
		self.Actions.Create_Action("STM", "Frame", "TempCharact", 13)
		self.Actions.Create_Action("STM", "RefTemp", "TempRefMeas", 14)
		self.Actions.Create_Action("STM", "Pixel", "TempNoise", 15)
		self.Actions.Create_Action("STM", "RefTemp", "TempCoilCharact", 16)
		self.Actions.Create_Action("STM", "RefTemp", "TempCoilDynamics", 17)
		self.Actions.Create_Action("STM", "Frame", "WaveGen", 18)
		self.Actions.Create_Action("STM", "Pixel", "ChemNoise", 19)
		self.Actions.Create_Action("STM", "Frame", "MultipleFrames", 20, 10.0)
		self.Actions.Create_Action("STM", "Frame", "SampleFor10Minutes", 21, 10.0)
		self.Actions.Create_Action("STM", "Frame", "DACSensitivityTest", 22)
		self.No_Action = No_Action()

		self.ControllerBusy = False
		self.InterruptEnable = False
		self.InterruptAction = None
		self.InterruptReady = False

	def LaunchController(self, cargo, Plot_3D, Plot_2D, Text = None):
		self.ControllerBusy = True
		self.Timer.start(self.Timeout)
		self.DefinePlots(Plot_3D, Plot_2D)
		if Text != None:
			self.DefineTextBox(Text)

	def StopController(self):
		self.Timer.stop()
		self.ControllerBusy = False

	def DefinePlots(self, Plot_3D, Plot_2D):
		self.Plots.SetupPlots(Plot_3D, Plot_2D)

	def DefineTextBox(self, Text):
		self.Plots.SetupText(Text)

	def EnableInterrupt(self, Action):
		self.InterruptEnable = True

	def DisableInterrupt(self):
		self.InterruptEnable = False

	def DataTransferBetweenStates(self, StateName_Sender, StateName_Receiver):
		self.FSM.states[StateName_Receiver].Action.action_data = self.FSM.states[StateName_Sender].Action.action_data	

class debug_Controller(Controller):
	def __init__(self, name, Interface, Timeout=10):

		self.SavePath = "Results/Debug"
		if not os.path.exists(self.SavePath):
			os.makedirs(self.SavePath)
		super(debug_Controller, self).__init__(name,Interface,Timeout)

		self.FSM.AddState("Ready",self.No_Action, Cond_SA_Ready())
		self.FSM.AddState("Single_RequestFrame",self.Actions.Assing("RequestFrame"), Cond_SA_Operation())
		self.FSM.AddState("Single_CharactCurves",self.Actions.Assing("CharactCurves"), Cond_SA_Operation())
		self.FSM.AddState("Single_CalibArray", self.Actions.Assing("CalibArray"), Cond_SA_Operation())
		self.FSM.AddState("Single_LAMP", self.Actions.Assing("LAMP"), Cond_SA_Operation())
		self.FSM.AddState("Single_PCR", self.Actions.Assing("PCR"), Cond_SA_Operation())
		self.FSM.AddState("Single_TempControl", self.Actions.Assing("TempControl"), Cond_SA_Operation())
		self.FSM.AddState("Single_TempCharact", self.Actions.Assing("TempCharact"), Cond_SA_Operation())
		self.FSM.AddState("Single_ObtainRefTemp", self.Actions.Assing("TempRefMeas"), Cond_SA_Operation())
		self.FSM.AddState("Single_TempNoise", self.Actions.Assing("TempNoise"), Cond_SA_Operation())
		self.FSM.AddState("Single_TempCoilCharact", self.Actions.Assing("TempCoilCharact"), Cond_SA_Operation())
		self.FSM.AddState("Single_TempCoilDynamics", self.Actions.Assing("TempCoilDynamics"), Cond_SA_Operation())
		self.FSM.AddState("Single_WaveGen", self.Actions.Assing("WaveGen"), Cond_SA_Operation())
		self.FSM.AddState("Single_ChemNoise", self.Actions.Assing("ChemNoise"), Cond_SA_Operation())
		self.FSM.AddState("Single_MultipleFrames", self.Actions.Assing("MultipleFrames"), Cond_SA_Operation())
		self.FSM.AddState("Single_SampleFor10Minutes", self.Actions.Assing("SampleFor10Minutes"), Cond_SA_Operation())		
		self.FSM.AddState("Done", self.No_Action, Condition_Empty())
		self.FSM.SetState("Done")
		
		self.FSM.AddTransition("toRequestFrame",Transition("Single_RequestFrame",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toCharactCurves",Transition("Single_CharactCurves",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toCalibArray",Transition("Single_CalibArray",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toLAMP",Transition("Single_LAMP",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toPCR",Transition("Single_PCR",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toTempControl",Transition("Single_TempControl",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toTempCharact",Transition("Single_TempCharact",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toObtainRefTemp",Transition("Single_ObtainRefTemp",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toTempNoise",Transition("Single_TempNoise",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toTempCoilCharact",Transition("Single_TempCoilCharact",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toTempCoilDynamics",Transition("Single_TempCoilDynamics",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toWaveGen",Transition("Single_WaveGen",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toChemNoise",Transition("Single_ChemNoise",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toMultipleFrames",Transition("Single_MultipleFrames",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toSampleFor10Minutes",Transition("Single_SampleFor10Minutes",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toDone",Transition("Done",self.StopController))		

	def LaunchController(self, cargo, Plot_3D, Plot_2D, Text = None):
		self.StartTime = datetime.now()
		self.SavePath = "Results/Debug/" + self.StartTime.strftime("%Y-%d-%b_%H-%M-%S")
		if not os.path.exists(self.SavePath):
			os.makedirs(self.SavePath)

		self.FSM.SetSavePath(self.SavePath)
		self.FSM.SetCargo(cargo)
		self.FSM.SetState("Ready")
		super(debug_Controller, self).LaunchController(cargo, Plot_3D, Plot_2D, Text = None)

class DriftAnalysis_Controller(Controller):
	def __init__(self, name, Interface, Timeout=10):
		
		self.SavePath = "Results/Drift"
		if not os.path.exists(self.SavePath):
			os.makedirs(self.SavePath)
		super(DriftAnalysis_Controller, self).__init__(name,Interface,Timeout)

		## STATES ##
		self.FSM.AddState("Ready",self.No_Action, Cond_UniqueTransition("InitialCalibration"))
		self.FSM.AddState("InitialCalibration", self.Actions.Assing("CalibArray"), Cond_UniqueTransition("DACSensitivity"))
		self.FSM.AddState("DACSensitivity", self.Actions.Assing("DACSensitivityTest"), Cond_UniqueTransition("InitialDriftSampling"))
		self.FSM.AddState("InitialDriftSampling", self.Actions.Assing("SampleFor10Minutes"), Cond_UniqueTransition("Done"))
		self.FSM.AddState("Done", self.No_Action, Condition_Empty())
		self.FSM.SetState("Done")

		## TRANSITIONS ##
		self.FSM.AddTransition("toInitialCalibration",Transition("InitialCalibration",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toDACSensitivity",Transition("DACSensitivity",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toInitialDriftSampling",Transition("InitialDriftSampling",self.Plots.ClearAllPlots))
		self.FSM.AddTransition("toDone",Transition("Done",self.StopController))		

	def LaunchController(self, cargo, Plot_3D, Plot_2D, Text = None):
		self.StartTime = datetime.now()
		self.SavePath = "Results/Drift/" + self.StartTime.strftime("%Y-%d-%b_%H-%M-%S")
		if not os.path.exists(self.SavePath):
			os.makedirs(self.SavePath)

		self.FSM.SetSavePath(self.SavePath)
		self.FSM.SetCargo(cargo)
		self.FSM.SetState("Ready")

		super(DriftAnalysis_Controller, self).LaunchController(cargo, Plot_3D, Plot_2D, Text = None)
