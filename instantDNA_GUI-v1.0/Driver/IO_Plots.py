import numpy as np

class IO_Plots(object):
	def __init__(self, TextBox = None, Plot_3D = None, Plot_2D = None):
		self.TextBox = None
		self.Plot_3D = None
		self.Plot_2D = None
		self.Curve = None

	def SetupPlots(self, Plot_3D, Plot_2D):
		self.Plot_3D = Plot_3D
		self.Plot_2D = Plot_2D
		self.Curve = self.Plot_2D.plot()
		
	def SetupText(self, TextBox):
		self.TextBox = TextBox

	def DisplayText(self, Text):
		self.TextBox.setText(Text)

	def PlotFrame(self, frame, Av_frames):
		if frame != []:
			frame = np.transpose(np.array(frame).reshape((32,32)))
			self.Plot_3D.setImage(frame, autoRange=True, autoLevels=True, autoHistogramRange=True)
			self.Plot_3D.update()
			self.Curve.setData(Av_frames, autoRange=True, autoLevels=True)

	def PlotPixel(self, value):
		self.Curve.setData(value)

	def ClearAllPlots(self):
		frame = np.transpose(np.array(np.zeros(1024)).reshape((32,32)))
		self.Plot_3D.setImage(frame, autoRange=True, autoLevels=True, autoHistogramRange=True)
		self.Plot_3D.update()
		#self.Curve.remove()

	def __del__(self):
		self.ClearAllPlots()
