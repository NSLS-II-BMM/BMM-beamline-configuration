#!/usr/bin/python

import time
from numpy import pi, sin, cos, arcsin
from termcolor import colored
from argparse import ArgumentParser
parser = ArgumentParser(description="Compute Bragg, para, and perp from a specified energy and for a 30 mm beam offset")
parser.add_argument("-e", "--energy", type=float, dest="energy", default=6000,
                    help="DCM energy in eV for calculation -- default 6000 eV")
parser.add_argument("-c", "--current", action="store_true", dest="current",
                    help="Print current readbacl values")
parser.add_argument("-m", "--move", action="store_true", dest="move",
                    help="Flag to use CA to move to the computed DCM position")
parser.add_argument("-1", "--111", action="store_false", dest="threeoneone", default=False,
                    help="Flag for Si(111) -- default Si(111)")
parser.add_argument("-3", "--311", action="store_true", dest="threeoneone", default=False,
                    help="Flag for Si(311) -- default Si(111)")
args = parser.parse_args()

import epics

def e2l(val):
    hbarc=1973.27053324
    return 2*pi*hbarc/val

offset = 30
twod = 2*3.1356
reflection = 'Si(111)'
if args.threeoneone:
    twod = 2*1.6375
    reflection = 'Si(311)'
wavelength = e2l(args.energy)
angle = arcsin(wavelength / twod)
para = offset / (2*sin(angle))
perp = offset / (2*cos(angle))
angle = angle*180/pi

print "%s = %.1f   %s = %s" % \
    (colored('energy',    'cyan', attrs=['bold']), args.energy,
     colored('reflection','cyan', attrs=['bold']), reflection)
print "targets: %s = %.5f   %s = %.4f   %s = %.4f" % \
    (colored('angle','green', attrs=['bold']), angle,
     colored('perp', 'green', attrs=['bold']), perp,
     colored('para', 'green', attrs=['bold']), para)



#bragg = PV("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr.RBV")
#per2 = PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr.RBV")
#par2 = PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr.RBV")
bragg = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr")
per2  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr")
par2  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr")

if args.current:
    print "current: %s = %.5f   %s = %.4f   %s = %.4f\n" % \
        (colored('angle','green', attrs=['bold']), bragg.RBV,
         colored('perp', 'green', attrs=['bold']), per2.RBV,
         colored('para', 'green', attrs=['bold']), par2.RBV)
    


if args.move:
    #print "(Not actually moving yet, these are caget actions on RBVs)"
    #print bragg.VAL
    #print per2.VAL
    #print par2.VAL

    pvgroup = (bragg, per2, par2)
    newvals = (angle, perp, para)
    for pv, val in zip(pvgroup, newvals):
        pv.move(val, wait=False)

    waiting = True
    while waiting:
        time.sleep(0.001)
        waiting = not all([pv.done_moving for pv in pvgroup])
    print 'Mono at %.1f' % args.energy
    print "RBVs: %s = %.4f   %s = %.4f   %s = %.4f\n" % \
        (colored('angle','green', attrs=['bold']), bragg.RBV,
         colored('perp', 'green', attrs=['bold']), per2.RBV,
         colored('para', 'green', attrs=['bold']), par2.RBV)

    
    ## dict of PVs for disabling in vacuum motors
    kill = {'p2'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr_KILL_CMD.PROC"),
            'r2'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr_KILL_CMD.PROC"),
            'per2': epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr_KILL_CMD.PROC"),
            'par2': epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr_KILL_CMD.PROC")}
    ## disable the in vacuum motors
    kill['per2'].put(1)
    kill['par2'].put(1)
    ## give CA some time to do its thing before exiting
    time.sleep(0.2)



