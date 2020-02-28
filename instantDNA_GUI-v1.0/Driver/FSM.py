###########################################

class Transition(object):
	def __init__(self,toState, Action):
		self.toState = toState 
		self.Action = Action
	
	def Execute(self):
		self.Action()
		print("Transitioning to..." + self.toState)

class State(object):
	def __init__(self, FSM, stateName, Action, Condition):
		self.FSM = FSM
		self.Plots = FSM.control.Plots
		self.stateName = stateName
		self.Action = Action
		self.Condition = Condition

	def Enter(self):
		print("State '" + self.stateName + "' launched")
		self.Action.Enter()

	def Execute(self):
		self.Action.Execute()
		self.Condition.Execute(self)
		
	def Exit(self):
		print("State '" + self.stateName + "' finalised")
		self.Action.Exit()
			

############################################

class FSM(object):
	def __init__(self,char):
		self.control = char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.prevState = None
		self.trans = None
		self.cargo = ""

	def AddTransition(self,transName,transition):
		self.transitions[transName] = transition

	def AddState(self,stateName,Action,Condition):
		self.states[stateName] = State(self, stateName,Action,Condition)

	def SetState(self, stateName):
		self.curState = self.states[stateName]

	def SetCargo(self, cargo):
		self.cargo = cargo

	def Transition(self, transName):
		self.trans = self.transitions[transName]

	def Execute(self):
		self.curState.Execute()
		if (self.trans):
			self.curState.Exit()
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.curState.Enter()
			self.trans = None
