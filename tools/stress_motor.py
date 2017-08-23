#!/usr/bin/python

import sys
import time
from epics import PV

from optparse import OptionParser
parser = OptionParser(description="Stress an in-vacuum motor")
parser.add_option("-m", "--motor", type="str", dest="motor", default="para",
                  help="motor to move (*para|perp|pitch|roll)")
parser.add_option("-c", "--counts", type="int", dest="counts", default=3000,
                  help="number of measurements -- default 3000")
parser.add_option("-s", "--stepsize", type="float", dest="stepsize", default=1.0,
                  help="step size in whatever units -- default 1.0")
(options,args) = parser.parse_args()




if options.motor == 'para':
    axis = 'Par2'
    temp = 'Para'
    ax   = 'AX'
elif options.motor == 'perp':
    axis = 'Per2'
    temp = 'Perp'
    ax   = 'Ax'
elif options.motor == 'pitch':
    axis = 'P2'
    temp = 'P'
    ax   = 'Ax'
elif options.motor == 'roll':
    axis = 'R2'
    temp = 'R'
    ax   = 'Ax'



    
template = "XF:06BMA-OP{Mono:DCM1-Ax:%s}Mtr%s"
val  =  PV(template % (axis, '.VAL'))
rbv  =  PV(template % (axis, '.RBV'))
kill =  PV(template % (axis, '_KILL_CMD.PROC'))

temptemp = "XF:06BMA-OP{Mono:DCM-Crys:2-%s:%s}T-I-I"
temperature = PV(temptemp % (ax, temp))

begin = time.time()


count = 0
parity = 1

print "# taking %d measurements" % options.counts
print "# ---------------------------------------------"
print "# time_sec  readback  target  temperature  step"
sys.stdout.flush()

while count < options.counts:
    newpos = val.get() + (options.stepsize*parity)

    val.put(newpos, wait=True)
    elapsed = time.time() - begin
    print " %.3f   %.4f   %.4f   %.1f   %s" % \
        (elapsed, rbv.get(), newpos, temperature.get(), count)
    sys.stdout.flush()
    
    count = count + 1
    parity = -1 * parity
    if temperature.get() > 105:
        break

time.sleep(2)                   # pitch and roll need a bit of time to settle...
kill.put(1, use_complete=True)
waiting = True
while waiting:
    time.sleep(0.001)
    waiting = not kill.put_complete

