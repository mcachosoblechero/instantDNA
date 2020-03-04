##########################################################################################
class List_Actions(object):
	def __init__(self, Control):
		self.Action = {}
		self.Control = Control
	
	def Create_Action(self, ActionSource, ActionType, ActionName, ActionCode, parameter=1.0):
		self.Action[ActionName] = Action(ActionSource, ActionType, ActionName, ActionCode, self.Control, parameter)

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

		if self.ActionType == "Frame":
			self.ActionHandler = self.ActionControl.Interface.ReceiveFrame
		elif self.ActionType == "Pixel":
			self.ActionHandler = self.ActionControl.Interface.ReceivePixel
		elif self.ActionType == "RefTemp":
			self.ActionHandler = self.ActionControl.Interface.ReceiveRefTemp	

	def Enter(self):
		self.ActionData.Clear()
		self.ActionActive = 1
		if self.ActionSource == "STM":
			self.ActionControl.Interface.sendMessage(self.ActionCode, self.ActionParameter)
			self.ActionControl.EnableInterrupt(self)

	def Execute(self, File, Plots):
		if self.ActionSource == "STM" and self.ActionControl.InterruptReady == True:
			self.ManageInterrupt(File, Plots)
		elif self.ActionSource == "RPi":
			self.ActionHandler()
			#self.UpdatePlots()

	def Exit(self):
		self.ActionControl.DisableInterrupt()

	def ManageInterrupt(self, File, Plots):
		self.ActionControl.InterruptReady = False
		[DC, Freq, Calib, RefTemp, EoM] = self.ActionHandler()
		self.ActionData.Update(DC, Freq, Calib, RefTemp, EoM)
		if self.ActionData.EoM == 0:
			self.UpdatePlots(Plots)
			File.SaveData(self.ActionData)
		else:
			self.ActionActive = 0

	def UpdatePlots(self, Plots):
		if self.ActionType == "Frame":
			Plots.PlotFrame(self.ActionData.DC, self.ActionData.Av_DC)
		elif self.ActionType == "Pixel":
			Plots.PlotPixel(self.ActionData.Av_DC)
		elif self.ActionType == "RefTemp":
			Plots.PlotPixel(self.ActionData.RefTemp)

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

	def Execute(self, File, Plots):
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

