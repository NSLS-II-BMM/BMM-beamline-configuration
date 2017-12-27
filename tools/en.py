
import epics
from numpy import pi, sin
from termcolor import colored
from argparse import ArgumentParser
parser = ArgumentParser(description="Compute energy from current mono position")
parser.add_argument("-3", "--311", action="store_true", dest="threeoneone", default=False,
                    help="Flag for Si(311) -- default Si(111)")
args = parser.parse_args()

hbarc=1973.27053324
def e2l(val):
    return 2*pi*hbarc/val

bragg      = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr")
angle      = bragg.RBV
#twod       = 2*3.1356
twod       = 2*3.13543952
xtals      = 'Si(111)'
if args.threeoneone:
    # twod = 2*1.6375
    twod  = 2*1.63761489
    xtals = 'Si(311)'
wavelength = twod * sin(angle * pi / 180)
energy     = e2l(wavelength)

print colored('='*65, 'yellow')
print "%s = %.2f -- %s" % (colored('energy', 'cyan', attrs=['bold']), energy, xtals)

perp = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr")
para = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr")
print "current: %s = %8.5f   %s = %7.4f   %s = %8.4f" % \
    (colored('angle','yellow'), bragg.RBV,
     colored('perp', 'yellow'), perp.RBV,
     colored('para', 'yellow'), para.RBV)
print colored('='*65, 'yellow')
