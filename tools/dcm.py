#!/usr/bin/python

import time
import os
from numpy import pi, sin, cos, arcsin
from termcolor import colored
import epics

## ----------------------------------------------------------------------
## gather command line arguments
from argparse import ArgumentParser
parser = ArgumentParser(description="Compute Bragg, para, and perp from a specified energy and for a 30 mm beam offset")
parser.add_argument("-e", "--energy", type=float, dest="energy", default=6000,
                    help="DCM energy in eV for calculation -- default 6000 eV")
parser.add_argument("-c", "--current", action="store_true", dest="current",
                    help="Print current readback values")
parser.add_argument("-m", "--move", action="store_true", dest="move",
                    help="Flag to use CA to move to the computed DCM position")
parser.add_argument("-1", "--111", action="store_false", dest="threeoneone", default=False,
                    help="Flag for Si(111) -- default Si(111)")
parser.add_argument("-3", "--311", action="store_true", dest="threeoneone", default=False,
                    help="Flag for Si(311) -- default Si(111)")
parser.add_argument("-pe", "--perpoffset", type=float, dest="perpoffset", default=0, #-4.58,
                    help="Size of offset on 2nd crystal perp -- default -4.58")
parser.add_argument("-pa", "--paraoffset", type=float, dest="paraoffset", default=0, #2.5,
                    help="Size of offset on 2nd crystal perp -- default 2.5")
args = parser.parse_args()

if args.move: args.current = True

if args.energy > 22300:
    print "Energy too high (limit is 22.3 keV / 2nd para = 156.05)"
    exit()

if args.energy < 4000:
    print "Energy too low"
    exit()

hbarc=1973.27053324
def e2l(val):
    return 2*pi*hbarc/val

## ----------------------------------------------------------------------
## constants and equations of motion
offset     = 30
twod       = 2*3.13543952
reflection = 'Si(111)'
if args.threeoneone:
    # twod       = 2*1.6375
    twod       = 2*1.63761489
    reflection = 'Si(311)'
wavelength = e2l(args.energy)
angle      = arcsin(wavelength / twod)
para       = offset / (2*sin(angle)) + args.paraoffset
perp       = offset / (2*cos(angle)) + args.perpoffset
angle      = angle*180/pi

## ----------------------------------------------------------------------
## report on motor positions for given energy
# print "%s = %.1f   %s = %s   (perp/para offset = %.2f/%.2f)" % \
#    (colored('energy',    'cyan', attrs=['bold']), args.energy,
#     colored('reflection','cyan', attrs=['bold']), reflection, args.perpoffset, args.paraoffset)
# print "targets: %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)" % \
#     (colored('angle','green', attrs=['bold']), angle,
#      colored('perp', 'green', attrs=['bold']), perp, perp - args.perpoffset,
#      colored('para', 'green', attrs=['bold']), para, para - args.paraoffset)
print "%s = %.1f   %s = %s" % \
    (colored('energy',    'cyan', attrs=['bold']), args.energy,
     colored('reflection','cyan', attrs=['bold']), reflection)
print "targets: %s = %8.5f   %s = %7.4f   %s = %8.4f" % \
    (colored('angle','green', attrs=['bold']), angle,
     colored('perp', 'green', attrs=['bold']), perp,
     colored('para', 'green', attrs=['bold']), para)


## ----------------------------------------------------------------------
## establish PVs
bragg = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr")
per2  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr")
par2  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr")

if args.current:
    # print "current: %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)\n" % \
    #     (colored('angle','yellow'), bragg.RBV,
    #      colored('perp', 'yellow'), per2.RBV, per2.RBV - args.perpoffset,
    #      colored('para', 'yellow'), par2.RBV, par2.RBV - args.paraoffset)
    print "current: %s = %8.5f   %s = %7.4f   %s = %8.4f\n" % \
        (colored('angle','yellow'), bragg.RBV,
         colored('perp', 'yellow'), per2.RBV,
         colored('para', 'yellow'), par2.RBV)
    


if args.move:
    ##------------------------------------------------------------------------
    ## gather up PVs and move them to targets
    pvgroup = (bragg, per2, par2)
    newvals = (angle, perp, para)
    for pv, val in zip(pvgroup, newvals):
        pv.move(val, wait=False)

    ##------------------------------------------------------------------------
    ## wait for all three motors to get where they are going
    waiting = True
    while waiting:
        time.sleep(0.001)
        waiting = not all([pv.done_moving for pv in pvgroup])
    print 'Mono at %.1f' % args.energy
    # print "RBVs:    %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)\n" % \
    #     (colored('angle','green', attrs=['bold']), bragg.RBV,
    #      colored('perp', 'green', attrs=['bold']), per2.RBV, per2.RBV - args.perpoffset,
    #      colored('para', 'green', attrs=['bold']), par2.RBV, par2.RBV - args.paraoffset)
    print "RBVs:    %s = %8.5f   %s = %7.4f   %s = %8.4f\n" % \
        (colored('angle','green', attrs=['bold']), bragg.RBV,
         colored('perp', 'green', attrs=['bold']), per2.RBV,
         colored('para', 'green', attrs=['bold']), par2.RBV)

    ##------------------------------------------------------------------------
    ## dict of PVs for disabling in vacuum motors
    kill = {'p2'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr_KILL_CMD.PROC"),
            'r2'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr_KILL_CMD.PROC"),
            'per2': epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr_KILL_CMD.PROC"),
            'par2': epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr_KILL_CMD.PROC")}
    ##------------------------------------------------------------------------
    ## disable the in vacuum motors
    kill['p2'].put(1)
    kill['r2'].put(1)
    kill['per2'].put(1)
    kill['par2'].put(1)
    ##------------------------------------------------------------------------
    ## give CA some time to do its thing before exiting
    time.sleep(0.2)



