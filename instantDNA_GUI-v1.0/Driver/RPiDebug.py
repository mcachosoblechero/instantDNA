import pigpio
import time
import struct
import instantDNA
import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from coloredGraph import MplCmapImageView

#pi = pigpio.pi()
#if not pi:
#	end()
#spi_h = pi.spi_open(0, 100000, 0)
#cb = pi.callback(21,pigpio.RISING_EDGE, isr_frame)

driver = instantDNA.instantDNA() 
#DAC_Value = 0.63; 	
#spi = instantDNA.Setup_DAC_VRef_Value(pi, spi_h ,DAC_Value)
#app.Setup_DAC_VRef_Value(0)
#app.Setup_DAC_VBias_Value(0.265)
#app.Setup_DAC_IOTA_Value(0)
while True:
	for i in range(0, 100):
		DACValue = (i / 10) - 5
		driver.Setup_DAC_RefElect_Value(DACValue)
		time.sleep(0.01)
#app.Test_OnChipDAC()
#app = QtWidgets.QApplication(sys.argv)
#stack = QtWidgets.QWidget()
#graphicsView = MplCmapImageView(parent=stack) 
#driver.RequestFrame(graphicsView)

try:
	while(1):
		variable = 1
except:
	print("End of program")
	app.CloseSPI()


##########################
## SPI Test - Send 0xFFFF

#print ("Bytes transferred: " + str(spi.count))
#print ("Data recieved:")
#print (list(spi.data))
#time.sleep(1)


