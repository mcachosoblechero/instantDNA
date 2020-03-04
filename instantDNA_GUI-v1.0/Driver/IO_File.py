import numpy as np
from datetime import datetime

class IO_File(object):
	def __init__(self, folderName, fileName):
		self.Start = datetime.now()
		self.folderName = folderName
		self.fileName = fileName
		self.FileHandle = []

	def OpenFile(self):
		self.FileHandle = open(self.folderName + '/'+ self.fileName +'.csv','a') 

	def ElapsedTime(self):
		diffTime = (datetime.now() - self.Start)
		return diffTime.total_seconds()

	def SaveLine(self, Line):
		np.savetxt(self.FileHandle, [Line], delimiter=',', fmt='%f')

	def SaveFrame(self, data):
		self.SaveLine([self.ElapsedTime()] + data.DC + [data.Av_DC[-1]] + data.Freq + [data.Av_Freq[-1]] + data.Calib)

	def SavePixel(self, data):
		self.SaveLine([self.ElapsedTime()] + [data.DC] + [data.Freq])
		
	def SaveRefTemp(self, data):
		self.SaveLine([self.ElapsedTime()] + data.RefTemp)

	def SaveData(self, data):
		if data.data_type == "Frame":
			self.SaveFrame(data)
		elif data.data_type == "Pixel":
			self.SavePixel(data)
		elif data.data_type == "RefTemp":
			self.SaveRefTemp(data)
		else:
			print("ERROR - TRYING TO SAVE AN UNKNOWN DATA TYPE")

	def CloseFile(self):
		if self.FileHandle != []:
			self.FileHandle.close()

	def UpdatePath(self, Path):
		self.folderName = Path
