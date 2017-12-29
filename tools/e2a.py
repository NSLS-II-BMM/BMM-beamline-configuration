
from argparse import ArgumentParser
parser = ArgumentParser(description="Compute energy from current mono position")
parser.add_argument("-3", "--311", action="store_true", dest="threeoneone", default=False,
                    help="Flag for Si(311) -- default Si(111)")
parser.add_argument('energy')
args = parser.parse_args()

from BMMcontrols import DCM
dcm = DCM()
if args.threeoneone:
    dcm.xtals(crystals='311')

print "%s eV is %.6f degrees with %s" % (args.energy, dcm.angle(float(args.energy)), dcm.description)
    
