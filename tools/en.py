
from argparse import ArgumentParser
parser = ArgumentParser(description="Compute energy from current mono position")
parser.add_argument("-3", "--311", action="store_true", dest="threeoneone", default=False,
                    help="Flag for Si(311) -- default Si(111)")
args = parser.parse_args()

from BMMcontrols import DCM

dcm = DCM()
if args.threeoneone:
    dcm.xtals(crystals='311')

dcm.prettyline(color='yellow')
dcm.prettyprint_energy(dcm.current_energy(), status='energy', color='cyan',  attrs=['bold'])
dcm.prettyprint_three_motors(dcm.bragg, dcm.perp, dcm.para, color="yellow", status="current")
dcm.prettyline(color='yellow')
