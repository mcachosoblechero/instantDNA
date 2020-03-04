##########################################################################################
# GENERIC CONDITION DEFINITION								 #
##########################################################################################
class Condition(object):
	def __init__(self):
		pass

	def Execute(self, State):
		pass

##########################################################################################
# DEBUG - SINGLE OPERATION - CONDITIONS							 #
##########################################################################################
class Condition_Empty(Condition):
	def __init__(self):
		pass

	def Execute(self, State):
		pass

class Cond_SA_Ready(Condition):
	def __init__(self):
		super(Cond_SA_Ready,self).__init__()

	def Execute(self, State):
		if State.FSM.cargo == "RequestFrame":
			State.FSM.Transition("toRequestFrame")
		elif State.FSM.cargo == "CharactCurves":
			State.FSM.Transition("toCharactCurves")
		elif State.FSM.cargo == "CalibArray":
			State.FSM.Transition("toCalibArray")
		elif State.FSM.cargo == "LAMP":
			State.FSM.Transition("toLAMP")
		elif State.FSM.cargo == "PCR":
			State.FSM.Transition("toPCR")
		elif State.FSM.cargo == "TempControl":
			State.FSM.Transition("toTempControl")
		elif State.FSM.cargo == "TempCharact":
			State.FSM.Transition("toTempCharact")
		elif State.FSM.cargo == "ObtainRefTemp":
			State.FSM.Transition("toObtainRefTemp")
		elif State.FSM.cargo == "TempNoise":
			State.FSM.Transition("toTempNoise")
		elif State.FSM.cargo == "TempCoilCharact":
			State.FSM.Transition("toTempCoilCharact")
		elif State.FSM.cargo == "TempCoilDynamics":
			State.FSM.Transition("toTempCoilDynamics")
		elif State.FSM.cargo == "WaveGen":
			State.FSM.Transition("toWaveGen")
		elif State.FSM.cargo == "ChemNoise":
			State.FSM.Transition("toChemNoise")
		elif State.FSM.cargo == "MultipleFrames":
			State.FSM.Transition("toMultipleFrames")
		elif State.FSM.cargo == "SampleFor10Minutes":
			State.FSM.Transition("toSampleFor10Minutes")

class Cond_SA_Operation(Condition):
	def __init__(self):
		super(Cond_SA_Operation,self).__init__()

	def Execute(self, State):
		if State.Action.ActionActive == 0:
			State.FSM.Transition("toDone")
		
class Cond_UniqueTransition(Condition):
	def __init__(self, nextState):
		super(Cond_UniqueTransition,self).__init__()
		self.nextState = nextState

	def Execute(self, State):
		if State.Action.ActionActive == 0:
			State.FSM.Transition("to" + self.nextState)
		
