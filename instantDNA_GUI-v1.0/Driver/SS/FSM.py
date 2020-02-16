class FSM:
	def __init__(self):
		self.handlers = {}
		self.currentHandler = {}
		self.startState = None
		self.newState = None
		self.endStates = []

	def add_state(self, name, handler, end_state=0):
		name = name.upper()
		self.handlers[name] = handler
		if end_state:
			self.endStates.append(name)

	def set_start(self, name):
		self.startState = name.upper()

	def start_FSM(self):
		self.currentHandler = self.handlers[self.startState]
		self.newState = self.startState

	def transition_FSM(self):
		print("Running State -> ", self.newState)		
		(self.newState) = self.currentHandler()
		if self.newState.upper() in self.endStates:
			print("Reached end state: ", self.newState)
		else:
			self.currentHandler = self.handlers[self.newState.upper()]
