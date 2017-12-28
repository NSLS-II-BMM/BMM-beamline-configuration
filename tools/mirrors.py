#!/usr/bin/python

from numpy import pi, sin, cos, arcsin, tan, arctan2

## ----------------------------------------------------------------------
## gather command line arguments
from argparse import ArgumentParser
parser = ArgumentParser(description="Move a specified mirror vertically, laterally, in pitch, in roll, or in yaw",
                        epilog = "Note: All motions are relative to the current position unless the -a flag is specified")
parser.add_argument("-m", "--mirror",   type=int,   dest="mirror", default=3,
                    help="mirror number, 1, 2, 3, 4 -- default 3 (mirror 4 = XAFS table")
parser.add_argument("-v", "--vertical", type=float, dest="vertical", default=None,
                    help="vertical motion in mm -- default 0 mm")
parser.add_argument("-l", "--lateral",  type=float, dest="lateral",  default=None,
                    help="lateral motion in mm -- default 0 mm")
parser.add_argument("-p", "--pitch",    type=float, dest="pitch",    default=None,
                    help="pitch in urad -- default 0 urad")
parser.add_argument("-r", "--roll",     type=float, dest="roll",     default=None,
                    help="roll in urad -- default 0 urad")
parser.add_argument("-y", "--yaw",      type=float, dest="yaw",      default=None,
                    help="yaw in urad -- default 0 urad")
parser.add_argument("-a", "--absolute", action="store_true", dest="absolute", default=False,
                    help="flag specifying absolute motion -- default relative")
parser.add_argument("-w", "--where", action="store_true", dest="where", default=False,
                    help="flag for reporting current mirror position in mm/urad")
args = parser.parse_args()

if args.mirror in (1,2,3,4):
    mirror = 'm' + str(args.mirror)
else:
    print "Mirror argument (-m) must be 1, 2, 3, or 4!"
    exit()


from BMMcontrols import Mirror
mirror = Mirror(args.mirror)

import signal
signal.signal(signal.SIGINT, mirror.handler)


if args.where:
    mirror.where(color='cyan', attrs=['bold'])
    exit()


## ----------------------------------------------------------------------
## verify that we are moving only one virtual axis
def is_not_none(val):
    return not val is None

directions = (args.vertical, args.lateral, args.pitch, args.roll, args.yaw)
naxes = sum(map(is_not_none, directions))
if naxes > 1:
    print colored("You are trying to move in %d directions at once!\n" % naxes, 'red', attrs=['bold'])
    parser.print_help()
    exit()
elif naxes == 0:
    print colored("You did not specify a direction!\n", 'red', attrs=['bold'])
    parser.print_help()
    exit()


## ----------------------------------------------------------------------
## -a flag -- compute relative motion from given value
if args.absolute:
    mirror.current_positions()
    if args.vertical  is not None:
       args.vertical  = args.vertical - mirror.vert
    elif args.lateral is not None:
       args.lateral   = args.lateral - mirror.lat
    elif args.pitch   is not None:
       args.pitch     = args.pitch - mirror.pitch
    elif args.roll    is not None:
       args.roll      = args.roll - mirror.roll
    elif args.yaw     is not None:
       args.yaw       = args.yaw - mirror.yaw


## ----------------------------------------------------------------------
## finally, move the motors along the virtual axes
    
if args.vertical is not None:
    mirror.direction = 'vertical'
    mirror.common_text(args.vertical, color='cyan', attrs=['bold']) 
    mirror.move((mirror.yu,                     mirror.ydo,                     mirror.ydi),
                (mirror.yu.RBV + args.vertical, mirror.ydo.RBV + args.vertical, mirror.ydi.RBV + args.vertical))

elif args.lateral is not None:
    mirror.direction = 'lateral'
    mirror.common_text(args.lateral, color='cyan', attrs=['bold']) 
    mirror.move((mirror.xu,                    mirror.xd),
                (mirror.xu.RBV + args.lateral, mirror.xd.RBV + args.lateral))

elif args.pitch is not None:
    mirror.direction = 'pitch'
    mirror.common_text(args.pitch, color='cyan', attrs=['bold']) 
    dbar  = (mirror.ydo.RBV + mirror.ydi.RBV) / 2
    angle = arctan2( (dbar-mirror.yu.RBV), mirror.length )
    y0    = mirror.length * tan(angle)
    angle = angle + args.pitch/1000
    y     = mirror.length * tan(angle)
    yrel  = (y-y0)/2
    mirror.move((mirror.yu, mirror.ydo, mirror.ydi), (-yrel, yrel, yrel), True)

elif args.roll is not None:
    mirror.direction = 'roll'
    mirror.common_text(args.roll, color='cyan', attrs=['bold']) 
    angle = arctan2(mirror.ydo.RBV-mirror.ydi.RBV, mirror.width)
    angle = angle + args.roll/1000
    y     = mirror.width * tan(angle)
    ybar  = ((mirror.ydo.RBV+mirror.ydi.RBV) / 2)
    mirror.move((mirror.ydo, mirror.ydi), (ybar+y/2, ybar-y/2), False)

elif args.yaw is not None:
    mirror.direction = 'yaw'
    mirror.common_text(args.yaw, color='cyan', attrs=['bold']) 
    angle = arctan2(mirror.xd.RBV-mirror.xu.RBV, mirror.width)
    xx0   = mirror.length * tan(angle)
    angle = angle + args.yaw/1000
    xx    = mirror.length * tan(angle)
    xxrel = (xx-xx0)/2
    mirror.move((mirror.xd, mirror.xu), (xxrel, -xxrel), True)

mirror.prettyprint_motors(color1='green', color2='yellow')
