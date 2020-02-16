from random import randint
from time import clock
from FSM import State, Transition, SimpleFSM

#################################################
# Create classes for each state inside this FSM #
#################################################
class LightOn(State):
	def __init__(self,FSM):
		super(LightOn, self).__init__(FSM)

	def Enter(self):
		print("Preparing to turn on...")
		super(LightOn,self).Enter()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

	def Execute(self):
		print("Light is on now!")
		self.FSM.Transition("toOff")
		super(LightOn,self).Execute()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

	def Exit(self):
		print("Light is going to be switched off..")
		super(LightOn,self).Exit()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

class LightOff(State):
	def __init__(self,FSM):
		super(LightOff, self).__init__(FSM)

	def Enter(self):
		print("Preparing to turn off...")
		super(LightOff,self).Enter()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

	def Execute(self):
		print("Light is off now!")
		self.FSM.Transition("toOn")
		super(LightOff,self).Execute()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

	def Exit(self):
		print("Light is going to be switched on..")
		super(LightOff,self).Exit()		# STATEMENT TO EXECUTE THE PARENT STATEMENTS

############################################

############################################

class ExampleFSM(object):
	def __init__(self):
		self.FSM = SimpleFSM(self)
		self.FSM.AddState("On",LightOn(self.FSM))
		self.FSM.AddState("Off",LightOff(self.FSM))
		self.FSM.AddTransition("toOn",Transition("On"))
		self.FSM.AddTransition("toOff",Transition("Off"))
		self.FSM.SetState("On")

############################################

if __name__ == "__main__":
	light = ExampleFSM()
	for i in range(20):
		startTime = clock()
		timeInterval = 1
		while(startTime + timeInterval > clock()):
			pass
		light.FSM.Execute()
