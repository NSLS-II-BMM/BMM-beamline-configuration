#!/usr/bin/python

import time
from numpy import pi, sin, cos, arcsin
from termcolor import colored
from optparse import OptionParser
parser = OptionParser(description="Compute Bragg, para, and perp from a specified energy and for a 30 mm beam offset")
parser.add_option("-e", "--energy", type="float", dest="energy", default=6000,
                  help="DCM energy in eV for calculation -- default 6000 eV")
parser.add_option("-m", "--move", action="store_true", dest="move",
                  help="Flag to use CA to move to the computed DCM position")
parser.add_option("-1", "--111", action="store_false", dest="threeoneone",
                  help="Flag for Si(111) -- default Si(111)")
parser.add_option("-3", "--311", action="store_true", dest="threeoneone",
                  help="Flag for Si(311) -- default Si(111)")
(options,args) = parser.parse_args()

from epics import PV

def e2l(val):
    hbarc=1973.27053324
    return 2*pi*hbarc/val

offset = 30
twod = 2*3.1356
reflection = 'Si(111)'
if options.threeoneone:
    twod = 2*1.6375
    reflection = 'Si(311)'
wavelength = e2l(options.energy)
angle = arcsin(wavelength / twod)
para = offset / (2*sin(angle))
perp = offset / (2*cos(angle))

print "%s = %.1f   %s = %s" % \
    (colored('energy',    'cyan', attrs=['bold']), options.energy,
     colored('reflection','cyan', attrs=['bold']), reflection)
print "\t%s = %.4f   %s = %.4f   %s = %.4f\n" % \
    (colored('angle','green', attrs=['bold']), angle*180/pi,
     colored('perp', 'green', attrs=['bold']), perp,
     colored('para', 'green', attrs=['bold']), para)

bragg = PV("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr.RBV")
per2 = PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr.RBV")
par2 = PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr.RBV")

if options.move:
    print "(Not actually moving yet, these are caget actions on RBVs)"
    print bragg.get()
    print per2.get()
    print par2.get()

    # pvgroup = (bragg, per2, par2)
    # newvals = (angle, perp, para))
    # for pv, val in zip(pvgroup, newvals):
    #     pv.put(val, use_complete=True)

    # waiting = True
    # while waiting:
    #     time.sleep(0.001)
    #     waiting = not all([pv.put_complete for pv in pvgroup])
    # print 'Mono at %.1f' % eoptions.energy
    
    ## dict of PVs for disabling in vacuum motors
    kill = {'p2'  : PV("XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr_KILL_CMD.PROC"),
            'r2'  : PV("XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr_KILL_CMD.PROC"),
            'per2': PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr_KILL_CMD.PROC"),
            'par2': PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr_KILL_CMD.PROC")}
    ## disable the in vacuum motors
    kill['per2'].put(1)
    kill['par2'].put(1)
    ## give CA some time to do its thing before exiting
    time.sleep(0.2)



