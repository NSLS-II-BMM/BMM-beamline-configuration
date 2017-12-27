#!/usr/bin/env python

## apt install fswebcam python-wand

import os
from os.path import expanduser
import sys
from subprocess import Popen, PIPE, call
import fcntl
import datetime
from time import sleep

USBDEVFS_RESET= 21780

HOME = expanduser("~")
USBID="534d:0021"
TITLE="NIST BMM (NSLS-II 06BM)"

from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color

from argparse import ArgumentParser
parser = ArgumentParser(description="Capture a screenshot from the currently displayed analog camera")
parser.add_argument("-d", "--directory", dest="directory", default=HOME,
                    help="output image directory (%s)"%HOME)
parser.add_argument("-v", "--device", dest="device", default="/dev/video0",
                    help="input device (/dev/video0)")
parser.add_argument("-s", "--skip", type=int, dest="skip", default=30,
                    help="number of frames to skip (30)")
parser.add_argument("-f", "--frames", type=int, dest="frames", default=5,
                    help="number of frames to accumulate (5)")
parser.add_argument("-b", "--brightness", type=int, dest="brightness", default=20,
                    help="percent brightness (20)") ## fswebcam -d v4l2:/dev/video0 --list-controls
parser.add_argument("-x", type=int, dest="x", default=320,
                    help="x-position of cross hairs (320)")
parser.add_argument("-y", type=int, dest="y", default=240,
                    help="y-position of cross hairs (240)")
parser.add_argument("-l", "--linecolor", dest="linecolor", default="white",
                    help="cross hair line color (white)")
parser.add_argument("-n", "--nocrosshair", action="store_true", dest="nocrosshair", default=False,
                    help="flag suppressing cross hair (default is to draw cross hair at x,y)")
parser.add_argument("-r", "--reset", action="store_true", dest="reset", default=False,
                    help="flag for attempting to reset device (default is not to try)")
parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", default=False,
                    help="flag suppressing screen comments (default is false)")
args = parser.parse_args()


## swiped from https://askubuntu.com/a/591979
if args.reset:
    print "resetting video device"
    try:
        lsusb_out = Popen("lsusb | grep -i %s"%USBID,
                          shell=True,
                          bufsize=64,
                          stdin=PIPE,
                          stdout=PIPE,
                          close_fds=True    ).stdout.read().strip().split()
        bus = lsusb_out[1]
        device = lsusb_out[3][:-1]
        f = open("/dev/bus/usb/%s/%s"%(bus, device), 'w', os.O_WRONLY)
        fcntl.ioctl(f, USBDEVFS_RESET, 0)
    except Exception, msg:
        print "failed to reset device:", msg

    sleep(1)    
    
target = "%s/%s.jpg" % (args.directory, datetime.datetime.now().replace(microsecond=0).isoformat())

quiet = ''
if args.quiet: quiet = '-q '
command = "fswebcam %s-i 0 -d %s -r 640x480 --title \"%s\" -S %d -F %d --set brightness=%s%% %s" %\
          (quiet, args.device, TITLE, args.skip, args.frames, args.brightness, target)
os.system(command)


if os.path.isfile(target):
    if not args.nocrosshair:
        ## draw the cross hair
        if not args.quiet: print "Drawing cross hair at %d,%d" % (args.x, args.y)
        with Image(filename=target) as image:
            with Drawing() as draw:
                with Color('white') as color:
                    draw.fill_color = color
                    draw.line((args.x, 0), (args.x, 479))
                    draw.line((0, args.y), (639, args.y))
                    draw(image)
                    image.format = 'jpeg'
                    image.save(filename=target)

else:
    print "fswebcam failed :("
    
