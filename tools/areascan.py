#!/usr/bin/env python

import epics

## ----- configuration ------------------------------------------------------------
x     = epics.Motor('xafs_linx')
x0    = 46
xwidth = 4
xstep  = 0.2

y     = epics.Motor('xafs_liny')
y0    = 124.7
ywidth = 4
ystep  = 0.2

filename = 'data/Nick/area_ReO3_in_BN.dat'
## --------------------------------------------------------------------------------

from time import sleep
from BMMcontrols import IonChambers, StepScan, DCM
import signal


## ----- deal with plotting
import numpy
import matplotlib        as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt

dcm = DCM()
dcm.xtals(crystals='111')
scan = StepScan(fname=filename, element='Re', e0=10535, edge='L3')
scan.file_header(dcm=dcm)
scan.column_labels()        # labels=('I0', 'It', 'Ir')
scan.handle.write(scan.file_header_text())


ic = IonChambers()
avgtm = epics.PV("XF:06BM-BI{EM:1}EM180:AveragingTime")
saveat = 0.5 # avgtm.get()
avgtm.put(0.1)

plt.ion()
plt.show()



def return_home():
    x.move(x0, wait=True)
    waiting = True
    while waiting:
        sleep(0.001)
        waiting = not x.done_moving
    y.move(y0, wait=True)
    waiting = True
    while waiting:
        sleep(0.001)
        waiting = not y.done_moving
    avgtm.put(saveat)



def handler(signum, frame):
    print '\n\nGot CTRL+C, stopping motor scan!'
    x.put('STOP', 1)
    y.put('STOP', 1)
    #plt.close()
    scan.handle.close()
    return_home()
    exit()

signal.signal(signal.SIGINT, handler)


posx = numpy.arange(x0-xwidth, x0+xwidth, xstep)
posy = numpy.arange(y0-xwidth, y0+xwidth, ystep)
sig  = numpy.zeros((posx.size, posy.size))


xi = 0
for px in posx:
    x.move(px, wait=True)
    waiting = True
    while waiting:
        sleep(0.001)
        waiting = not x.done_moving

    yi = 0
    for py in posy:
        y.move(py, wait=True)
        waiting = True
        while waiting:
            sleep(0.001)
            waiting = not y.done_moving

        values = [px, py]
        values.extend(ic.measure())

        sig[yi,xi] = values[3]  # 3 is It
        
        plt.clf()
        plt.title('area scan')
        plt.grid(True)
        plt.xlabel('X (mm)')
        plt.ylabel('Y (mm)')
        vmin=1e-11
        if sig.max() > 1e-8:
            vmin=1e-8
        plt.pcolor(posx, posy, sig, cmap=mpl.cm.hot, vmin=1e-8, vmax=sig.max())
        plt.gca().invert_yaxis()
        plt.colorbar()
        plt.draw()
        plt.pause(0.001)
        
        line = " %.3f   %.3f   %.7g   %.7g   %.7g\n" % tuple(values)
        print line[:-1]
        scan.handle.write(line)
        yi = yi+1
    print ''
    scan.handle.write("\n")
    xi = xi+1

scan.handle.close()
return_home()
avgtm.put(saveat)
action = raw_input("RET to quit ")
plt.close()
