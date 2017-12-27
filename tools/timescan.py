#!/usr/bin/env python

from subprocess import call
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
saveat = avgtm.get()
avgtm.put(0.1)

#ic1 = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
scalar = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")

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
    


start = os.times()[4]
while True:
    time.sleep(0.01)
    elapsed = numpy.append(elapsed, [os.times()[4] - start])
    reading = numpy.append(reading, [scalar.get()])
    drawme(elapsed, reading)
