import pigpio
import time
import struct
import numpy as np
from datetime import datetime


class instantDNA:
	def __init__(self):
		self.pi = pigpio.pi()
		self.spi_h = self.pi.spi_open(0, 5000000, 192) # Flag for SPI CH1&2 disable
		self.SamplingFreq = 84e6
		self.State = "Ready"
		self.cb = self.pi.callback(7,pigpio.RISING_EDGE, self.isr_frame)
		self.now = datetime.now()
		self.Test_StartTime = datetime.now()

		self.StoredAvFrames_DutyCycle = list()
		self.StoredAvFrames_Frequency = list()
		self.StoredPixels_DutyCycle = list()
		self.StoredPixels_Frequency = list()
		self.StoredRefTemp = list()
		self.CalibValues = list()

		self.RunningDNATest = 0
		self.Patient_Diagnosis = False
		self.HelloWorld()

	#########################################################
	# DNA PROTOCOL ##########################################
	#########################################################	
	def DNATest(self):
		# STEP 1 - HEAT THE SOLUTION #		
		if self.State == "Ready":
			print("Starting Test")
			self.Patient_Diagnosis = self.RunLottery()
			print("Patient Diagnosis is: " + str(self.Patient_Diagnosis))
			self.State = "CalibArray" ## <- Change when heating is available
			self.DNATest()

		# STEP 2 - CALIBRATE ARRAY #
		elif self.State == "CalibArray":
			print("Step 2: Calibrate Array")
			self.TextBox.setText("Calibrating platform")
			self.CalibArray()

		# STEP 3 - OBTAIN SAMPLES UNTIL EoT #
		elif self.State == "RequestFrame":
			print("Step 3: Obtain Sample")
			self.TextBox.setText("Sampling Array")
			if (self.Patient_Diagnosis == True):
				self.FakepH()
			self.RequestFrame()
	######################################################

	######################################################
	# INTERRUPT ##########################################
	######################################################			
	def isr_frame(self, gpio, level, tick):
		if self.State == "Ready":
			pass
		elif self.State == "RequestFrame":
			self.ReceiveFrame()
			self.ProcessFrame()
			self.PlotFrame()
			if self.RunningDNATest == 1:
				self.State = "RequestFrame"
				self.DNATest()
			else:
				self.State = "Ready"

		elif self.State == "CharactCurves":
			self.ReceiveFrame()
			if not self.CheckEndOfMessage():
				self.ProcessFrame()
				self.PlotFrame()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "CalibArray":
			self.ReceiveFrame()
			if not self.CheckEndOfMessage():			
				self.ProcessFrame()
				self.PlotFrame()
			else:
				if self.RunningDNATest == 1:
					self.State = "RequestFrame"
					self.DNATest()
				else:
					self.Close_Storage()
					self.State = "Ready"

		elif self.State == "TempControl":
			self.ReceivePixel()
			if not self.CheckEndOfMessage():
				self.ProcessPixel()
				self.PlotTempPixel()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "LAMP":
			self.ReceiveFrame()
			if not self.CheckEndOfMessage():
				self.ProcessFrame()
				self.PlotTempFrame()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "PCR":
			self.ReceiveFrame()
			if not self.CheckEndOfMessage():
				self.ProcessFrame()
				self.PlotTempFrame()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "TempCharact":
			self.ReceiveFrameAndCalib()
			if not self.CheckEndOfMessage():
				self.ProcessFrame()
				self.SaveLineCSV(self.FileHandle, self.DutyCycle + [self.StoredAvFrames_DutyCycle[-1]] + self.Frequency + [self.StoredAvFrames_Frequency[-1]] + self.CalibValues)
				self.PlotTempFrame()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "TempRefMeas":
			self.ReceiveRefTemp()
			if not self.CheckTempEndOfMessage():
				self.ProcessRefTemp()
				self.SaveLineCSV(self.FileHandle, self.RefTemp)
				self.PlotTempRefFrame()
			else:
				self.Close_Storage()
				self.State = "Ready"

		elif self.State == "TempNoise":
			self.ReceivePixel()
			if not self.CheckEndOfMessage():
				self.ProcessPixel()
				self.SaveLineCSV(self.FileHandle, [self.ElapsedTime(self.Test_StartTime)] + [self.DutyCycle] + [self.Frequency])
				self.PlotTempPixel()
			else:
				self.Close_Storage()
				self.State = "Ready"
	######################################################	

	######################################################
	# STM ACTIONS ########################################
	######################################################
	def Setup_DAC_VRef_Value(self, DAC_Value):
		spi_message = [1] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def Setup_DAC_VBias_Value(self, DAC_Value):
		spi_message = [2] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def Setup_DAC_IOTA_Value(self, DAC_Value):
		spi_message = [3] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def Setup_DAC_RefElect_Value(self, DAC_Value):
		spi_message = [4] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def Test_OnChipDAC(self):
		spi_message = [5] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		
	def RequestFrame(self):
		self.State = "RequestFrame"		
		self.Init_Storage()		
		spi_message = [6] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def ObtainCharactCurves(self):
		self.State = "CharactCurves"
		self.Init_Storage()		
		spi_message = [7] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def CalibArray(self):
		self.State = "CalibArray"
		self.Init_Storage()
		spi_message = [8] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def LAMPControl(self):
		self.State = "LAMP"
		self.Init_Storage()
		spi_message = [10] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def PCRControl(self):
		self.State = "PCR"
		self.Init_Storage()
		spi_message = [11] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def TempControl(self):
		self.State = "TempControl"
		self.Init_Storage()
		spi_message = [12] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def TempCharact(self):
		self.State = "TempCharact"
		self.Init_Storage()
		spi_message = [13] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def ObtainRefTemp(self):
		self.State = "TempRefMeas"
		self.Init_Storage()
		spi_message = [14] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def TempNoise(self):
		self.State = "TempNoise"
		self.Init_Storage()
		self.Test_StartTime = datetime.now()
		spi_message = [15] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)	
	######################################################

	def ReceiveFrame(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*2048)
		data = struct.unpack("<" + ("L"*2048),data)
		self.ticks_high = data[::2]
		self.ticks_period = data[1::2]
		print(data)

	def ReceivePixel(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*2)
		data = struct.unpack("<" + ("L"*2),data)
		self.ticks_high = data[0]
		self.ticks_period = data[1]

	def ReceiveFrameAndCalib(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*3072)
		data = struct.unpack("<" + ("L"*3072),data)
		self.ticks_high = data[:2048:2]
		self.ticks_period = data[1:2048:2]
		self.CalibValues = list(data[2048::1])
		print ("Bytes transferred: " + str(count))
		print ("Data recieved:")
		print (list(data))

	def ReceiveRefTemp(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*1)
		data = struct.unpack("<" + ("f"*1),data)
		self.RefTemp = data[0];

	def ProcessFrame(self):
		self.DutyCycle = [i / j for i, j in zip(self.ticks_high, self.ticks_period)]
		self.Frequency = [self.SamplingFreq / j for j in self.ticks_period]
		self.StoredAvFrames_DutyCycle.append(sum(self.DutyCycle)/len(self.DutyCycle))	
		self.StoredAvFrames_Frequency.append(sum(self.Frequency)/len(self.Frequency))
#		self.SaveLineCSV(self.FileHandle, self.DutyCycle + self.StoredAvFrames_DutyCycle[-1] + self.Frequency + self.StoredAvFrames_Frequency[-1])
		print(self.DutyCycle[528])

	def ProcessPixel(self):
		self.DutyCycle = (self.ticks_high / self.ticks_period)
		self.Frequency = (self.SamplingFreq / self.ticks_period)
		self.StoredPixels_DutyCycle.append(self.DutyCycle)	
		self.StoredPixels_Frequency.append(self.Frequency)
		#print("DC: " + str(self.DutyCycle) + " Freq: " + str(self.Frequency))

	def ProcessRefTemp(self):
		self.StoredRefTemp.append(self.RefTemp)
		print("Reference Temperature Received: " + str(self.RefTemp))

	def CheckEndOfMessage(self):
		if type(self.ticks_high) is tuple:
			if self.ticks_high[0]!=0xAAAAAAAA or self.ticks_period[0]!=0xAAAAAAAA:
				return False
		else:
			if self.ticks_high!=0xAAAAAAAA or self.ticks_period!=0xAAAAAAAA:
				return False
		print("Command Finished")
		return True

	def CheckTempEndOfMessage(self):
		if self.RefTemp != -50.0:
			return False
		print("Command Finished")
		return True

	def FlushFrameBuffer(self):
		self.StoredAvFrames_DutyCycle = list()
		self.StoredAvFrames_Frequency = list()
		self.StoredPixels_DutyCycle = list()
		self.StoredPixels_Frequency = list()
		self.StoredRefTemp = list()
		self.CalibValues = list()
		frame = np.transpose(np.array(np.zeros(1024)).reshape((32,32)))
		self.TargetPlot3D.setImage(frame, autoRange=True, autoLevels=True, autoHistogramRange=True)
		self.Curve.setData(list())

	def EndOngoingTest(self):
		self.FlushFrameBuffer()
		if (self.RunningDNATest == 1):
			self.RunningDNATest = 0
		else:
			self.State = "Ready"

	#####################################################
	# STORAGE ACTIONS ###################################
	#####################################################
	def Init_Storage(self):
		self.now = datetime.now()
		self.FileHandle = open('Out/'+self.State+'_'+self.now.strftime("%Y-%d-%b_%H-%M-%S")+'.csv','w') 
		
	def SaveLineCSV(self, File, Line):
		np.savetxt(File, [Line], delimiter=',', fmt='%f')

	def ElapsedTime(self, InitialTime):
		diffTime = (datetime.now() - InitialTime)
		return diffTime.total_seconds()

	def Close_Storage(self):
		self.FileHandle.close()
	#####################################################

	######################################################
	# PLOTTING ACTIONS ###################################
	######################################################
	def SetupTextBox(self, TextBox):
		self.TextBox = TextBox

	def DisplayText(self, Text):
		self.TextBox.setText(Text)

	def SetupPlots(self, PlotWindow_3D, PlotWindow_2D):
		self.TargetPlot3D = PlotWindow_3D
		self.TargetPlot2D = PlotWindow_2D
		self.Curve = self.TargetPlot2D.plot()

	def PlotFrame(self):
		frame = np.transpose(np.array(self.DutyCycle).reshape((32,32)))
		self.TargetPlot3D.setImage(frame, autoRange=False, autoLevels=False, autoHistogramRange=False)
		self.TargetPlot3D.update()
		self.Curve.setData(self.StoredAvFrames_DutyCycle)

	def PlotTempFrame(self):
		frame = np.transpose(np.array(self.Frequency).reshape((32,32)))
		self.TargetPlot3D.setImage(frame, autoRange=True, autoLevels=True, autoHistogramRange=True)
		self.TargetPlot3D.update()
		self.Curve.setData(self.StoredAvFrames_Frequency, autoRange=True, autoLevels=True)

	def PlotTempRefFrame(self):
		self.Curve.setData(self.StoredRefTemp)

	def PlotPixel(self):
		self.Curve.setData(self.StoredPixels_DutyCycle)

	def PlotTempPixel(self):
		self.Curve.setData(self.StoredPixels_Frequency)
	######################################################

	######################################################
	# DRIVER METHODS #####################################
	######################################################
	def HelloWorld(self):
		print("Welcome to InstantDNA!")

	def CloseSPI(self):
		self.pi.spi_close(self.spi_h)
		self.pi.stop()
	######################################################

	####################################################
	# DEMO METHODS #####################################
	####################################################
	def RunLottery(self):
		value = np.random.randint(2,size = 1)
		if (value == 1):
			return True
		else:
			return False

	def FakepH(self):
		if len(self.StoredAvFrames_DutyCycle) > 55 and len(self.StoredAvFrames_DutyCycle) < 65:
			spi_message = [9] + list(bytearray(struct.pack("f",1.0)))
			(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
	#####################################################
