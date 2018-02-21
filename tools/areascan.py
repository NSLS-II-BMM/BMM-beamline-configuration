#!/usr/bin/env python

import epics

## ----- configuration ------------------------------------------------------------
x     = epics.Motor('xafs_linx')
x0    = -104.2
xwidth = 0.65
xstep  = 0.0625

y     = epics.Motor('xafs_liny')
y0    = 56.0
ywidth = 0.65
ystep  = 0.0625

filename = 'pinhole.dat'
## --------------------------------------------------------------------------------

from time import sleep
from BMMcontrols import IonChambers, StepScan, DCM, Vortex
import signal


## ----- deal with plotting
import numpy
import matplotlib        as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt

dcm = DCM()
dcm.xtals(crystals='111')
scan = StepScan(fname=filename, element='Fe', e0=7112, edge='K')
scan.file_header(dcm=dcm)
scan.column_labels()        # labels=('I0', 'It', 'Ir')
scan.handle.write(scan.file_header_text())


ic = IonChambers()
vor =Vortex()
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
posy = numpy.arange(y0-ywidth, y0+ywidth, ystep)
x2,y2 = numpy.meshgrid(posx,posy)
#sig  = numpy.zeros((posx.size-1, posy.size-1))
sig  = numpy.zeros(x2.shape)


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
        #values.append(vor.get('roi1'))

        sig[yi,xi] = values[3]/values[2]  # 3 is It, 5 would be roi
        
        plt.clf()
        plt.title('area scan')
        plt.grid(True)
        plt.xlabel('X (mm)')
        plt.ylabel('Y (mm)')
        #vmin=1e-11
        #if sig.max() > 1e-8:
        #    vmin=1e-8
        plt.pcolormesh(x2,y2,sig, cmap=mpl.cm.hot, vmin=0, vmax=sig.max())
        #plt.pcolor(posy, posx, sig, cmap=mpl.cm.hot, vmin=0, vmax=sig.max())
        #plt.gca().invert_yaxis()
        plt.colorbar()
        plt.draw()
        plt.pause(0.001)
        
        #line = " %.3f   %.3f   %.7g   %.7g   %.7g   %.7g\n" % tuple(values)
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
