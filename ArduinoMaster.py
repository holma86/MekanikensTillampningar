from time import sleep
from UUGear import *
import time
import datetime

UUGearDevice.setShowLogs(1)
device1 = UUGearDevice('UUGear-Arduino-7519-9895')
device2 = UUGearDevice('UUGear-Arduino-4608-5541')
device3 = UUGearDevice('UUGear-Arduino-3835-6554')
device4 = UUGearDevice('UUGear-Arduino-5133-9746')
devices = [device1, device2, device3, device4]

AnalogPinsFromMux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
DigitalPinsToMux = [
        [2, 3, 4, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21],
        [22, 23, 24, 25],
        [26, 27, 28, 29],
        [30, 31, 32, 33],
        [34, 35, 36, 37],
        [38, 39, 40, 41],
        [42, 43, 44, 45],
        [46, 47, 48, 49],
        [50, 51, 52, 53]
        ]
MuxChannels = 16;  #Number of channels on each multiplexer board
MaxIterations = 1


i = 0
while i<len(devices):
        if devices[i].isValid():
                print 'Device %i is ready.' %(i+1)
        else:
                print 'Device %i is not ready.' %(i+1)
        j = 0
        while j<len(DigitalPinsToMux):
                k = 0
                while k<len(DigitalPinsToMux[j]):                               #set output pins on the arduino 
                        devices[i].setPinModeAsOutput(DigitalPinsToMux[j][k])
                        k = k + 1
                j = j + 1
        i=i+1
print '-----------------'
print 'STARTING IN!'
sleep(1)
print '3'
sleep(1)
print '2'
sleep(1)
print '1'
sleep(1)
print 'NOW!!!'
print '----------------------------'
print 'x,y,z,Value,Date,Time,Sample'
print '----------------------------'
Iteration = 1
sample = 1
while Iteration <= MaxIterations:                                      #number of iterations
        i = 0
        while i < len(devices):                                         #loop through Arduino Devices 
                j = MuxChannels-1
                while j >= 0:                                           #loop through mux channels
                        BinIndex = "{0:04b}".format(j)                  #convert decimal number of mux channel to binary
                        l = 0
                        while l < len(BinIndex):                        #loop through all characters in the 
                                k = 0
                                while k < len(DigitalPinsToMux):        #Set digital pins for mux
                                        if BinIndex[l] == '1':
                                                devices[i].setPinHigh(DigitalPinsToMux[k][l])
                                        else:
                                                devices[i].setPinLow(DigitalPinsToMux[k][l])
                                        k = k + 1
                                l = l + 1
                        m = 0
                        while m < len(AnalogPinsFromMux):
                                Value = devices[i].analogRead(AnalogPinsFromMux[m])
                                date = datetime.datetime.now().strftime("%Y-%m-%d")
                                time = datetime.datetime.now().strftime("%H:%M:%S")
                                print "%i,%i,%i,%i,%s,%s,%i" %((m+1), (j+1), (i+1), Value, date, time, sample)
                                m = m + 1
                                sample = sample + 1
                        j = j - 1
                i=i+1
        Iteration = Iteration +1
device1.detach()
device1.stopDaemon()
