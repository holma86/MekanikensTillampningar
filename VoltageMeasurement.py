from time import sleep
from UUGear import *

UUGearDevice.setShowLogs(0)

device = UUGearDevice('UUGear-Arduino-7519-9895')

if device.isValid():
	for i in range(3):
		print "%0.2f" % (float(device.analogRead(0)) * 5 / 1024), "V"
		sleep(0.2)
	
	device.detach()
	device.stopDaemon()
else:
	print 'UUGear device is not correctly initialized.'
