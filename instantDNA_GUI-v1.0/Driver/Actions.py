from Driver.IO_File import IO_File

##########################################################################################
class List_Actions(object):
	def __init__(self, Control):
		self.Action = {}
		self.Control = Control
	
	def Create_Action(self, ActionSource, ActionType, ActionName, ActionCode, parameter=1.0):
		self.Action[ActionName] = Action(ActionSource, ActionType, ActionName, ActionCode, self.Control, parameter)

	def Launch_Action(self,ActionName, parameter=1.0):
		print("Action '" + actionName + "' launched")
		self.Action[ActionName].Launch(parameter)

	def Process_Action(self, ActionName):
		print("Action '" + actionName + "' executed")
		self.Action[ActionName].Process()

	def Finish_Action(self, ActionName):
		print("Action '" + actionName + "' finalised")
		self.Action[ActionName].Finish()

	def Assing(self, ActionName):
		return self.Action[ActionName]

##########################################################################################
class Action(object):
	def __init__(self, ActionSource, ActionType, ActionName, ActionCode, Control, parameter = 0.0):
		self.ActionSource = ActionSource
		self.ActionType = ActionType
		self.ActionCode = ActionCode
		self.ActionName = ActionName
		self.ActionData = Action_Data()
		self.ActionParameter = parameter
		self.ActionActive = 0
		self.ActionControl = Control

		self.IO_File = IO_File(Control.name, ActionName)
		if self.ActionType == "Frame":
			self.ActionHandler = self.ActionControl.Interface.ReceiveFrame
		elif self.ActionType == "Pixel":
			self.ActionHandler = self.ActionControl.Interface.ReceivePixel
		elif self.ActionType == "RefTemp":
			self.ActionHandler = self.ActionControl.Interface.ReceiveRefTemp	

	def Enter(self):
		self.ActionData.Clear()
		self.ActionActive = 1
		self.IO_File.OpenFile()
		if self.ActionSource == "STM":
			self.ActionControl.Interface.sendMessage(self.ActionCode, self.ActionParameter)
			self.ActionControl.EnableInterrupt(self)

	def Execute(self):
		if self.ActionSource == "STM" and self.ActionControl.InterruptReady == True:
			self.ManageInterrupt()
		elif self.ActionSource == "RPi":
			self.ActionHandler()
			#self.UpdatePlots()

	def Exit(self):
		self.IO_File.CloseFile()
		self.ActionControl.DisableInterrupt()

	def ManageInterrupt(self):
		self.ActionControl.InterruptReady = False
		[DC, Freq, Calib, RefTemp, EoM] = self.ActionHandler()
		self.ActionData.Update(DC, Freq, Calib, RefTemp, EoM)
		if self.ActionData.EoM == 0:
			self.IO_File.SaveData(self.ActionData)
			self.UpdatePlots()
		else:
			self.ActionActive = 0


	def UpdatePlots(self):
		if self.ActionType == "Frame":
			self.ActionControl.Plots.PlotFrame(self.ActionData.DC, self.ActionData.Av_DC)
		elif self.ActionType == "Pixel":
			self.ActionControl.Plots.PlotPixel(self.ActionData.Av_DC)
		elif self.ActionType == "RefTemp":
			self.ActionControl.Plots.PlotPixel(self.ActionData.RefTemp)

class No_Action(Action):
	def __init__(self, ActionSource = None, ActionType = None, ActionName = None, ActionCode = None, Control = None, parameter = 0.0):
		self.ActionSource = ActionSource
		self.ActionType = ActionType
		self.ActionCode = ActionCode
		self.ActionName = ActionName
		self.ActionParameter = parameter
		self.ActionActive = 0
		self.ActionControl = Control

	def Enter(self):
		pass

	def Execute(self):
		pass

	def Exit(self):
		pass

##########################################################################################
class Action_Data(object):
	def __init__(self):
		self.DC = []
		self.Freq = []
		self.Calib = []
		self.Av_DC = list()
		self.Av_Freq = list()
		self.RefTemp = list()
		self.data_type = ""
		self.EoM = 0

	def Clear(self):
		self.DC = []
		self.Freq = []
		self.Calib = []
		self.Av_DC = list()
		self.Av_Freq = list()
		self.RefTemp = list()
		self.data_type = ""
		self.EoM = 0
		
	def Update(self,DC, Freq, Calib, RefTemp, EoM):
		self.EoM = EoM		
		if self.EoM == 0:
			if DC != []:
				self.DC = DC
				if type(DC) != float:
					self.Av_DC.append(sum(DC)/len(DC))
					self.data_type = "Frame"
				else:
					self.Av_DC.append(DC)
					self.data_type = "Pixel"

			if Freq != []:
				self.Freq = Freq
				if type(Freq) != float:
					self.Av_Freq.append(sum(Freq)/len(Freq))
				else:
					self.Av_Freq.append(Freq)
			if Calib != []:
				self.Calib = Calib
			if RefTemp != 0.0:
				self.data_type = "RefTemp"
				self.RefTemp.append(RefTemp)

