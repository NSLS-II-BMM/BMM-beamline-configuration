#!/usr/bin/env python

import epics
from time import sleep
from BMMcontrols import IonChambers, Vortex
import signal



x     = epics.Motor('xafs_liny')
x0    = 70.45
width = 10
step  = 0.5
mode  = 'fluorescence'
#mode  = 'transmission'

# x     = epics.Motor('xafs_roll')
# x0    = 0.316
# width = 2
# step  = 0.05


## ----- deal with plotting
import numpy
import matplotlib         as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
pos = numpy.array([])
sig = numpy.array([])

ic = IonChambers()
vor = Vortex()

plt.ion()
plt.show()

current = float(x.get('RBV'))
handle = open('linx.dat', 'w')

def handler(signum, frame):
    print '\n\nGot CTRL+C, stopping motor scan!'
    x.put('STOP', 1)
    x.move(current)
    plt.close()
    handle.close()

signal.signal(signal.SIGINT, handler)

for p in numpy.arange(x0-width, x0+width, step):
    x.move(p, wait=True)
    waiting = True
    while waiting:
        sleep(0.001)
        waiting = not x.done_moving
    values = [p]
    values.extend(ic.measure())
    values.append(vor.get('roi1'))
    values.append(vor.get('roi2'))
    values.append(vor.get('roi3'))
    values.append(vor.get('roi4'))
    pos = numpy.append(pos, [p])
    if mode[0] is 'f':
	signal = (values[4]+values[5]+values[6]+values[7])/values[1]
    else:
	signal = values[2]/values[1]
    line = " %.3f   %.7g   %.7g   %.7g   %.7g   %.7g   %.7g   %.7g\n" % tuple(values)
    print line[:-1], signal

    sig = numpy.append(sig, numpy.array([signal]))
    handle.write(line)
    
    plt.clf()
    plt.title('line scan')
    plt.grid(True)
    plt.xlabel('position (mm)')
    plt.ylabel('it/i0')
    plt.plot(pos, sig)
    plt.xlim(x0-width, x0+width)
    #plt.ylim(0, 2.0)
    plt.draw()
    plt.pause(0.001)

action = raw_input("RET to quit ")
plt.close()
handle.close()
x.move(current)
