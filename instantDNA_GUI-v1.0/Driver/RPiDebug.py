import pigpio
import time
import struct
import instantDNA


#pi = pigpio.pi()
#if not pi:
#	end()
#spi_h = pi.spi_open(0, 100000, 0)
#cb = pi.callback(21,pigpio.RISING_EDGE, isr_frame)

app = instantDNA.instantDNA()
#DAC_Value = 0.63; 	
#spi = instantDNA.Setup_DAC_VRef_Value(pi, spi_h ,DAC_Value)
#app.Setup_DAC_VRef_Value(0)
#app.Setup_DAC_VBias_Value(0.265)
#app.Setup_DAC_IOTA_Value(0)
#app.Setup_DAC_RefElect_Value(0)
#app.Test_OnChipDAC()

app.RequestFrame()

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


