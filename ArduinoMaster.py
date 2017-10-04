from time import sleep
from UUGear import *

UUGearDevice.setShowLogs(1)
device1 = UUGearDevice('UUGear-Arduino-7519-9895')
device2 = UUGearDevice('UUGear-Arduino-XXXX-XXXX')
devices = [device1, device2]

i = 0
while i<len(devices):
        if devices[i].isValid():
                print 'Device %i is ready.' %(i+1)
        else:
                print 'Device %i is not ready.' %(i+1)
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
MaxIterations = 2

Iterations = 1
while Iterations <= MaxIterations:                                      #number of iterations
        i = 0
        while i < len(devices):                                         #loop through Arduino Devices 
                print "----------------------------"
                print "DEVICE %i" %(i+1)
                print "----------------------------"
                j = MuxChannels-1
                while j >= 0:                                           #loop through mux channels
                        BinIndex = "{0:04b}".format(j)                  #convert decimal number of mux channel to binary
                        l = 0
                        while l < len(BinIndex):                        #loop through all characters in the 
                                k = 0
                                state = ""
                                while k < len(DigitalPinsToMux):        #Set digital pins for mux
                                        if BinIndex[l] == '1':
                                                devices[i].setPinHigh(DigitalPinsToMux[k][l])
                                                state = "High"
                                        else:
                                                devices[i].setPinLow(DigitalPinsToMux[k][l])
                                                state = "Low"
                                        k = k + 1
                                        sleep(0.01)
                                print state
                                l = l + 1
                        l = 1
                        while l <= len(DigitalPinsToMux):               #take measurements from position j on each mux card
                                print "muxboard #%i channel #%i" %(l, (j+1))
                                l = l + 1
                        j = j - 1
                device1.detach()
                device1.stopDaemon()
                i=i+1
        Iterations = Iterations +1
