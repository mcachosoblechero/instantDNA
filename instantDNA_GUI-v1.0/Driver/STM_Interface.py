import pigpio
import struct

class STM_Interface(object):
	def __init__(self):
		self.pi = pigpio.pi()
		self.spi_h = self.pi.spi_open(0, 5000000, 192) # Flag for SPI CH1&2 disable
		self.SamplingFreq = 84e6

	def sendMessage(self, code, parameter):
		spi_message = [code] + list(bytearray(struct.pack("f",parameter)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

	def ReceiveFrame(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*3072)
		data = struct.unpack("<" + ("L"*3072),data)
		ticks_high = data[:2048:2]
		ticks_period = data[1:2048:2]

		# Check if message is EoM
		# If EoM -> EoM = 1, empty the rest
		if ticks_high[0]==0xAAAAAAAA or ticks_period[0]==0xAAAAAAAA:
			EoM = 1
			DC = []
			Freq = []
			Calib = []
			RefTemp = 0.0

		# If not EoM -> Process
		else:
			EoM = 0
			DC = [i / j for i, j in zip(ticks_high, ticks_period)]
			Freq = [self.SamplingFreq / j for j in ticks_period]
			Calib = list(data[2048::1])
			RefTemp = 0.0

		return [DC, Freq, Calib, RefTemp, EoM]


	def ReceivePixel(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*2)
		data = struct.unpack("<" + ("L"*2),data)
		ticks_high = data[0]
		ticks_period = data[1]	

		if ticks_high==0xAAAAAAAA or ticks_period==0xAAAAAAAA:
			EoM = 1
			DC = []
			Freq = []
			Calib = []
			RefTemp = 0.0
		else:
			EoM = 0
			DC = (ticks_high / ticks_period)
			Freq = (self.SamplingFreq / ticks_period)
			Calib = []
			RefTemp = 0.0

		return [DC, Freq, Calib, RefTemp, EoM]

	def ReceiveRefTemp(self):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*1)
		data = struct.unpack("<" + ("f"*1),data)

		# Check if message is EoM
		# If EoM -> EoM = 1, empty the rest
		if data[0] == -50.0:
			EoM = 1
			DC = []
			Freq = []
			Calib = []
			RefTemp = 0.0
			
		# If not EoM -> Process
		else:
			EoM = 0
			DC = []
			Freq = []
			Calib = []
			RefTemp = data[0]
			print("Ref Temp -> " + str(RefTemp))
		
		return [DC, Freq, Calib, RefTemp, EoM]

	def close(self):
		self.pi.spi_close(self.spi_h)
		self.pi.stop()
	#############################################################

