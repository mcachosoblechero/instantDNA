import pigpio
import time
import struct


class instantDNA:
	def __init__(self):
		self.pi = pigpio.pi()
		self.spi_h = self.pi.spi_open(0, 5000000, 0)
		self.SamplingFreq = 84e6
		self.cb = self.pi.callback(21,pigpio.RISING_EDGE, self.isr_frame)

	def HelloWorld():
		print("Welcome to InstantDNA")

	def CloseSPI(self):
		self.pi.spi_close(self.spi_h)
		self.pi.stop()

	def isr_frame(self, gpio, level, tick):
		(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00, 0x00,0x00]*2048)
		data = struct.unpack("<" + ("L"*2048),data)
		self.ticks_high = data[::2]
		self.ticks_period = data[1::2]
		print(self.ticks_high)
		print(self.ticks_period)
		spi_message = [6] + list(bytearray(struct.pack("f",1.0)))		
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)

#		print("High:" + str(High) + " Frequency:" + str(Frequency))
#		print ("Bytes transferred: " + str(count))
#		print ("Data recieved:")
#		print (list(data))
		#(count,data) = self.pi.spi_xfer(self.spi_h, [0x00, 0x00,0x00,0x00]*1024)
		#print ("Bytes transferred: " + str(count))
		#print ("Data recieved:")
		#print (list(data))

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
		spi_message = [6] + list(bytearray(struct.pack("f",1.0)))
		(count, data) = self.pi.spi_xfer(self.spi_h, spi_message)
		print ("Bytes transferred: " + str(count))
		print ("Data recieved:")
		print (list(data))
