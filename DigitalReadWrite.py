from time import sleep
from UUGear import *

UUGearDevice.setShowLogs(0)

device = UUGearDevice('UUGear-Arduino-7519-9895')

if device.isValid():
	device.setPinModeAsOutput(2)
	for i in range(5):
		device.setPinHigh(2)
		sleep(0.2)
		device.setPinLow(2)
		sleep(0.2)
	
	device.setPinModeAsInput(9)
	print 'Pin 9 status=', device.getPinStatus(9)
	
	device.detach()
	device.stopDaemon()
else:
	print 'UUGear device is not correctly initialized.'
