import pigpio
import time
import struct
import numpy as np


class instantDNA:
	def __init__(self):
		self.pi = pigpio.pi()
		self.spi_h = self.pi.spi_open(0, 5000000, 192) # Flag for SPI CH1&2 disable
		self.SamplingFreq = 84e6
		self.State = "Ready"
		self.cb = self.pi.callback(7,pigpio.RISING_EDGE, self.isr_frame)
		self.StoredAvFrames_DutyCycle = list()
		self.RunningDNATest = 0
		self.Patient_Diagnosis = False
		self.HelloWorld()

	def HelloWorld(self):
		print("Welcome to InstantDNA!")

	def CloseSPI(self):
		self.pi.spi_close(self.spi_h)
		self.pi.stop()

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

			
	def isr_frame(self, gpio, level, tick):
		if self.State == "Ready":
			pass
		elif self.State == "RequestFrame":
			self.ReceiveFrame()
			self.ProcessFrame()
			self.StoreAverageFrame()
			self.PlotFrame()
			if self.RunningDNATest == 1:
				self.State = "RequestFrame"
				self.DNATest()
			else:
				self.State = "Ready"

		elif self.State == "CharactCurves":
			self.ReceiveFrame()
			self.ProcessFrame()
			self.StoreAverageFrame()
			self.PlotFrame()

		elif self.State == "CalibArray":
			self.ReceiveFrame()
			if not self.CheckEndOfMessage():# CHECK IF SENT MESSAGE IS EoM			
				self.ProcessFrame()
				self.StoreAverageFrame()
				self.PlotFrame()
			else:
				if self.RunningDNATest == 1:
					self.State = "RequestFrame"
					self.DNATest()
				else:
					self.State = "Ready"
		elif self.State == "MeasTemp":
			self.ReceiveFrame()
			self.ProcessFrame()
			self.StoreAverageFrame()
			self.PlotFrame()
			self.State = "Ready"	


	def Setup_DAC_VRef_Value(self, DAC_Value):
		spi_message = [1] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		# NEED TO ADD WAITING TIME

	def Setup_DAC_VBias_Value(self, DAC_Value):
		spi_message = [2] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		# NEED TO ADD WAITING TIME

	def Setup_DAC_IOTA_Value(self, DAC_Value):
		spi_message = [3] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		# NEED TO ADD WAITING TIME

	def Setup_DAC_RefElect_Value(self, DAC_Value):
		spi_message = [4] + list(bytearray(struct.pack("f",DAC_Value)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		# NEED TO ADD WAITING TIME

	def Test_OnChipDAC(self):
		spi_message = [5] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		
	def RequestFrame(self):
		self.State = "RequestFrame"		
		spi_message = [6] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def ObtainCharactCurves(self):
		self.State = "CharactCurves"
		spi_message = [7] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def CalibArray(self): # Need to include 2D plot
		self.State = "CalibArray"
		spi_message = [8] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def SetLAMPTemp(self):
		spi_message = [10] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		print ("Bytes transferred: " + str(count))
		print ("Data recieved:")
		print (list(data))

	def PCRControl(self):
		spi_message = [11] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def MeasTemp(self):
		self.State = "MeasTemp"
		spi_message = [12] + list(bytearray(struct.pack("f",63.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

	def ReceiveFrame(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*2048)
		data = struct.unpack("<" + ("L"*2048),data)
		self.ticks_high = data[::2]
		self.ticks_period = data[1::2]

	def CheckEndOfMessage(self):
		for x in self.ticks_high:
			if x!=0xAAAAAAAA:
				return False
		for x in self.ticks_period:
			if x!=0xAAAAAAAA:
				return False		
		return True

	def ProcessFrame(self):
		self.DutyCycle = [i / j for i, j in zip(self.ticks_high, self.ticks_period)]
		self.Frequency = [self.SamplingFreq / j for j in self.ticks_period]
		print(self.DutyCycle[528])

	def FlushFrameBuffer(self):
		self.StoredAvFrames_DutyCycle = list()
		frame = np.transpose(np.array(np.zeros(1024)).reshape((32,32)))
		self.TargetPlot3D.setImage(frame, autoRange=False, autoLevels=False, autoHistogramRange=False)
		self.Curve.setData(list())

	def StoreAverageFrame(self):
		self.StoredAvFrames_DutyCycle.append(sum(self.DutyCycle)/len(self.DutyCycle))

	def SetupTextBox(self, TextBox):
		self.TextBox = TextBox

	def SetupPlots(self, PlotWindow_3D, PlotWindow_2D):
		self.TargetPlot3D = PlotWindow_3D
		self.TargetPlot2D = PlotWindow_2D
		self.Curve = self.TargetPlot2D.plot()

	def PlotFrame(self):
		frame = np.transpose(np.array(self.DutyCycle).reshape((32,32)))
		self.TargetPlot3D.setImage(frame, autoRange=False, autoLevels=False, autoHistogramRange=False)
		self.TargetPlot3D.update()
		self.Curve.setData(self.StoredAvFrames_DutyCycle)

	def EndOngoingTest(self):
		# STORE VALUES #
		self.FlushFrameBuffer()
		if (self.RunningDNATest == 1):
			self.RunningDNATest = 0
		else:
			self.State = "Ready"

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
