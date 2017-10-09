from time import sleep
from UUGear import *

UUGearDevice.setShowLogs(0)
device1 = UUGearDevice('UUGear-Arduino-7519-9895')
#device2 = UUGearDevice('UUGear-Arduino-XXXX-XXXX')
#devices = [device1, device2]
devices =[device1]

i = 0
while i<len(devices):
        if devices[i].isValid():
                print 'Device %i is ready.' %(i+1)
        else:
                print 'Device %i is not ready.' %(i+1)
        i=i+1

device1.setPinModeAsOutput(2)
device1.setPinModeAsOutput(3)
device1.setPinModeAsOutput(4)
device1.setPinModeAsOutput(5)


device1.setPinHigh(2)
device1.setPinHigh(3)
device1.setPinLow(4)
device1.setPinLow(5)
for i in range(0, 5):
        value = device1.analogRead(1)
        print value
        sleep(0.1)

device1.setPinLow(2)
device1.setPinLow(3)
device1.setPinLow(4)
device1.setPinLow(5)

device1.detach()
device1.stopDaemon()
