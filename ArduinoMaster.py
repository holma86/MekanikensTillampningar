from time import sleep
from UUGear import *

UUGearDevice.setShowLogs(1)
device1 = UUGearDevice('UUGear-Arduino-7519-9895')
#device1 = UUGearDevice('UUGear-Arduino-XXXX-XXXX')
devices = [device1]
#devices = [device2]

i = 0
while i<len(devices):
        if devices[i].isValid():
                print 'Device 1 is ready.'
        else:
                print 'Device 1 is not ready.'
        i=i+1
        
AnalogPinsFromMux = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
DigitalPinsToMux = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32],
        [33, 34, 35, 36],
        [37, 38, 39, 40],
        [41, 42, 43, 44],
        [45, 46, 47, 48],
        [49, 50, 51, 52]
        ]
MuxChannels = 16;
a = 0
i = 0
while i < len(devices):                   #loop through Arduino Devices
        #print BinIndex
        k = 0
        while k < len(DigitalPinsToMux):
                j = 0
                while j < MuxChannels:
                        BinIndex = "{0:04b}".format(j)
                        l = 0
                        while l < len(BinIndex):
                                if BinIndex[l] == '1':
                                        devices[i].setPinHigh(DigitalPinsToMux[k][l])
                                        print "High"
                                else:
                                        devices[i].setPinLow(DigitalPinsToMux[k][l])
                                        print "Low"
                                l = l + 1
                                sleep(0.1)
                        print "Take measurement"
                        l = 0
                        while l < len(BinIndex):
                                devices[i].setPinLow(DigitalPinsToMux[k][l])
                                l = l + 1
                        j = j + 1
                k = k + 1
        device1.detach()
        device1.stopDaemon()
        i=i+1
