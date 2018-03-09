#!/usr/bin/env python

import os
import time
import signal
import epics
import numpy
import matplotlib        as mpl
#mpl.use('Qt4Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore",".*GUI is implemented.*")

avgtm = epics.PV("XF:06BM-BI{EM:1}EM180:AveragingTime")
#avgtm = epics.PV("XF:06BM-ES:1{Sclr:1}.TP1")
saveat = 0.5 # avgtm.get()

scalar = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
#scalar = epics.PV("XF:06BM-ES:1{Sclr:1}.S14")

## DM2
#scalar = epics.PV("XF:06BM-BI{F460:1}Cur:I0-I") # Al
#scalar = epics.PV("XF:06BM-BI{F460:1}Cur:I1-I") # Ni
avgtm.put(0.1)

elapsed = numpy.array([])
reading = numpy.array([])

plt.ion()
plt.show()

def handler(signum, frame):
    print '\n\nGot CTRL+C, stopping time scan, resetting averaging time'
    avgtm.put(saveat)
    exit(0)

signal.signal(signal.SIGINT, handler)


def drawme(elapsed, reading):
    plt.clf()
    plt.title('time scan')
    plt.grid(True)
    plt.xlabel('time (sec)')
    plt.ylabel('signal')
    plt.plot(elapsed, reading)
    plt.draw()
    plt.pause(0.001)


toss = True
start = os.times()[4]
while True:
    time.sleep(0.01)
    elapsed = numpy.append(elapsed, [os.times()[4] - start])
    reading = numpy.append(reading, [scalar.get()*1e9])
    drawme(elapsed[1:], reading[1:])
