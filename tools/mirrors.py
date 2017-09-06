#!/usr/bin/python

import time
from numpy import pi, sin, cos, arcsin, tan, arctan2
from termcolor import colored
import epics

## ----------------------------------------------------------------------
## gather command line arguments
from argparse import ArgumentParser
parser = ArgumentParser(description="Move a specified mirror vertically, laterally, in pitch, in roll, or in yaw")
parser.add_argument("-m", "--mirror",   type=int,   dest="mirror", default=3,
                    help="mirror number, 1, 2, or 3 -- default 3")
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

#print args

## ----------------------------------------------------------------------
## interpret + sanity-check mirror argument    
dimensions = { 'm1' : [ 556, 240],
               'm2' : [1288, 240],
               'm3' : [ 667, 240] }
if args.mirror in (1,2,3):
    mirror = 'm' + str(args.mirror)
else:
    print "Mirror argument (-m) must be 1, 2, or 3!"
    exit()

z = dimensions[mirror][0]
x = dimensions[mirror][1]
hutch = 'A'
if args.mirror == 1: hutch = ''

## ----------------------------------------------------------------------
## fetch the Motors for this mirror
yu  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YU}Mtr"  % (hutch, args.mirror))
ydo = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YDO}Mtr" % (hutch, args.mirror))
ydi = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YDI}Mtr" % (hutch, args.mirror))
xu  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:XU}Mtr"  % (hutch, args.mirror))
xd  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:XD}Mtr"  % (hutch, args.mirror))

## ----------------------------------------------------------------------
## compute current vert, lat, pitch, roll, yaw positions
def current_positions():
    vert  = (yu.RBV + (ydo.RBV+ydi.RBV)/2) / 2
    lat   = (xu.RBV+xd.RBV)/2
    dbar  = (ydo.RBV + ydi.RBV) / 2
    pitch = 1000*arctan2( (dbar-yu.RBV),   z )
    roll  = 1000*arctan2( ydo.RBV-ydi.RBV, x )
    yaw   = 1000*arctan2( xd.RBV-xu.RBV,   z )
    return (vert, lat, pitch, roll, yaw)

## ----------------------------------------------------------------------
## -w flag, then exit
if args.where:
    (v, l, p, r, y) = current_positions()
    print colored('Mirror '+str(args.mirror), 'cyan', attrs=['bold'])
    print "\tvertical = %.3f" % v
    print "\tlateral  = %.3f" % l
    print "\tpitch    = %.3f" % p
    print "\troll     = %.3f" % r
    print "\tyaw      = %.3f" % y
    exit()

## ----------------------------------------------------------------------
## verify that we are moving only one virtual axis
def is_not_none(val):
    return not val is None

directions = (args.vertical, args.lateral, args.pitch, args.roll, args.yaw)
naxes = sum(map(is_not_none, directions))
if naxes > 1:
    print "You are trying to move in two directions at once!"
    exit()
elif naxes == 0:
    print "You did not specify a direction!"
    exit()

## ----------------------------------------------------------------------
## -a flag -- compute relative motion from given value
if args.absolute:
    (v, l, p, r, y) = current_positions()
    if args.vertical is not None:
       args.vertical = args.vertical - v
    elif args.lateral is not None:
       args.lateral  = args.lateral - l
    elif args.pitch is not None:
       args.pitch    = args.pitch - p
    elif args.roll is not None:
       args.roll     = args.roll - r
    elif args.yaw is not None:
       args.yaw      = args.yaw - y

#print args

## ----------------------------------------------------------------------
## define some support functions
       
## args are tuple of PVs, tuple of target values
def perform_move(pvs, vals, rel=False):
    for pv, val in zip(pvs, vals):
        if not pv.within_limits(val):
            print "Invalid motion on %s" % pv.DESC
            exit()
        pv.move(val, relative=rel, wait=False)
    waiting = True
    while waiting:
        time.sleep(0.001)
        waiting = not all([pv.done_moving for pv in pvs])
    return 0

def common_text(name):
    print "%s: moving in %s by %.3f" % \
        (colored('Mirror '+str(args.mirror), 'cyan', attrs=['bold']),
         name, getattr(args, name))
     

## ----------------------------------------------------------------------
## finally, move the motors along the virtual axes
    
if args.vertical is not None:
    common_text('vertical') 
    perform_move((yu, ydo, ydi),
                 (yu.RBV + args.vertical, ydo.RBV + args.vertical, ydi.RBV + args.vertical))
    print '\t%s = %.3f' % \
        (colored('vertical position', 'green', attrs=['bold']),
         (yu.RBV + (ydo.RBV+ydi.RBV)/2) / 2)
    print "\tRBVs: %s = %.4f   %s = %.4f   %s = %.4f\n" % \
        (colored('YU',  'green', attrs=['bold']), yu.RBV,
         colored('YDO', 'green', attrs=['bold']), ydo.RBV,
         colored('YDI', 'green', attrs=['bold']), ydi.RBV)

elif args.pitch is not None:
    common_text('pitch') 
    dbar = (ydo.RBV + ydi.RBV) / 2
    angle = arctan2( (dbar-yu.RBV), z )
    y0 = z * tan(angle)
    angle = angle + args.pitch/1000
    y = z * tan(angle)
    yrel = (y-y0)/2
    perform_move((yu, ydo, ydi), (-yrel, yrel, yrel), True)
    dbar = (ydo.RBV + ydi.RBV) / 2
    angle = 1000*arctan2( (dbar-yu.RBV), z )
    print '\t%s = %.3f' % \
        (colored('pitch', 'green', attrs=['bold']), angle)
    print "\tRBVs: %s = %.4f   %s = %.4f   %s = %.4f\n" % \
        (colored('YU',  'green', attrs=['bold']), yu.RBV,
         colored('YDO', 'green', attrs=['bold']), ydo.RBV,
         colored('YDI', 'green', attrs=['bold']), ydi.RBV)

elif args.lateral is not None:
    common_text('lateral') 
    perform_move((xu, xd),
                 (xu.RBV + args.lateral, xd.RBV + args.lateral))
    print '\t%s = %.3f' % \
        (colored('lateral position', 'green', attrs=['bold']),
         (xu.RBV+xd.RBV)/2)
    print "\tRBVs: %s = %.4f   %s = %.4f\n" % \
        (colored('XU', 'green', attrs=['bold']), xu.RBV,
         colored('XD', 'green', attrs=['bold']), xd.RBV)

elif args.roll is not None:
    common_text('roll') 
    angle = arctan2(ydo.RBV-ydi.RBV, x)
    angle = angle + args.roll/1000
    y = x * tan(angle)
    ybar = ((ydo.RBV+ydi.RBV) / 2)
    perform_move((ydo, ydi), (ybar+y/2, ybar-y/2), False)
    angle = 1000*arctan2(ydo.RBV-ydi.RBV, x)
    print '\t%s = %.3f' % \
        (colored('roll', 'green', attrs=['bold']), angle)
    print "\tRBVs: %s = %.4f   %s = %.4f   %s = %.4f\n" % \
        (colored('YU',  'green', attrs=['bold']), yu.RBV,
         colored('YDO', 'green', attrs=['bold']), ydo.RBV,
         colored('YDI', 'green', attrs=['bold']), ydi.RBV)

elif args.yaw is not None:
    common_text('yaw') 
    angle = arctan2(xd.RBV-xu.RBV, x)
    xx0 = z * tan(angle)
    angle = angle + args.yaw/1000
    xx  = z * tan(angle)
    xxrel = (xx-xx0)/2
    perform_move((xd, xu), (xxrel, -xxrel), True)
    angle = 1000*arctan2(xd.RBV-xu.RBV, z)
    print '\t%s = %.3f' % \
        (colored('yaw', 'green', attrs=['bold']), angle)
    print "\tRBVs: %s = %.4f   %s = %.4f\n" % \
        (colored('XU', 'green', attrs=['bold']), xu.RBV,
         colored('XD', 'green', attrs=['bold']), xd.RBV)
    
