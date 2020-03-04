import numpy as np
from collections import deque

class Drift_Analysis(object):
	def __init__(self, controller, prevState):

		# Drift Analysis constants
		self.DriftWindow = 25
		self.NumPixels = 1024
		
		self.controller = controller
		self.prevCalib = []
		self.currentCalib = []
		self.nextCalib = []
		self.linearRegresion = []
		self.prevState = prevState
		
		self.DC_window = deque(maxlen=self.DriftWindow)
		self.time_window = deque(maxlen=self.DriftWindow)

	def ExtractSTMData(self):
		actionData = self.controller.FSM.states[self.prevState].Action.action_data
		self.DC_window.append(actionData.DC)
	
	def CalculateDACSensitivity(self):
		pass
		
	def LinearRegression(self):
		self.x_array = np.array(self.DC_window)
		self.x = np.array(self.DC_window)

	def CalculateNewCalib(self):
		pass


if __name__ == '__main__':
	# Test linear Regression
