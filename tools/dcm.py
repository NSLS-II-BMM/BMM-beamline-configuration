#!/usr/bin/python


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
                    help="Size of offset on 2nd crystal perp -- default 0")
parser.add_argument("-pa", "--paraoffset", type=float, dest="paraoffset", default=0, #2.5,
                    help="Size of offset on 2nd crystal perp -- default 0")
args = parser.parse_args()

if args.move: args.current = True

from BMMcontrols import DCM
dcm = DCM()
if args.threeoneone:
    dcm.xtals(crystals='311')


if args.energy > dcm.emax:
    print "Energy too high (limit is 22.3 keV / 2nd para = 156.05)"
    exit()

if args.energy < dcm.emin:
    print "Energy too low"
    exit()

angle = dcm.angle(args.energy)
para  = dcm.parallel(args.energy)      + args.paraoffset
perp  = dcm.perpendicular(args.energy) + args.perpoffset

## ----------------------------------------------------------------------
## report on motor positions for given energy
dcm.prettyprint_energy(args.energy, status='moving to energy', color='cyan',  attrs=['bold'])
dcm.prettyprint_target_energy(angle, perp, para, color="green", attrs=['bold'])

## ----------------------------------------------------------------------
## report current positions
if args.current:
    dcm.prettyprint_three_motors(dcm.bragg, dcm.perp, dcm.para, color="yellow", status="current")
    print ''
    

if args.move:
    current = dcm.moveto(args.energy)
    dcm.prettyprint_energy(current, status='Mono at', color='cyan',  attrs=['bold'])
    dcm.prettyprint_target_energy(dcm.bragg.pv.RBV, dcm.perp.pv.RBV, dcm.para.pv.RBV, color="green", attrs=['bold'], status="RBVs   ")



