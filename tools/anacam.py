#!/usr/bin/env python

## apt install fswebcam python-wand

from fswebcam import fswebcam
import os.path

from argparse import ArgumentParser
parser = ArgumentParser(description="Capture a screenshot from the currently displayed analog camera")

## fswebcam parameters
parser.add_argument("-o", "--folder", dest="folder", default=None,
                    help="output image folder (user's home folder)")
parser.add_argument("-d", "--device", dest="device", default=None,
                    help="input device (/dev/video0)")
parser.add_argument("-c", "--camera", dest="camera", default=None,
                    help="camera number (0, usually N in /dev/videoN)")
parser.add_argument("-s", "--skip", type=int, dest="skip", default=None,
                    help="number of frames to skip (30)")
parser.add_argument("-f", "--frames", type=int, dest="frames", default=None,
                    help="number of frames to accumulate (5)")
parser.add_argument("-b", "--brightness", type=int, dest="brightness", default=None,
                    help="percent brightness (20)") ## fswebcam -d v4l2:/dev/video0 --list-controls
parser.add_argument("-x", type=int, dest="x", default=None,
                    help="x-position of cross hairs (320)")
parser.add_argument("-y", type=int, dest="y", default=None,
                    help="y-position of cross hairs (240)")
parser.add_argument("-l", "--linecolor", dest="linecolor", default=None,
                    help="cross hair line color (white)")
parser.add_argument("-n", "--nocrosshair", action="store_true", dest="nocrosshair", default=None,
                    help="flag suppressing cross hair (default is to draw cross hair at x,y)")
parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", default=None,
                    help="flag suppressing screen comments (default is false)")

## reset flag
parser.add_argument("-r", "--reset", action="store_true", dest="reset", default=None,
                    help="flag for attempting to reset device (default is not to try)")

args = parser.parse_args()
    
camera = fswebcam()
if args.reset:
    camera.reset()

## shuttle command line args into the fswebcam object
for k in vars(args).keys():
    if k is "reset": continue
    if getattr(args, k) is not None:
        setattr(cam, k, getattr(args, k))

camera.snapshot()

if os.path.isfile(camera.filename):
    if not camera.nocrosshair:
        camera.crosshairs()
else:
    print "fswebcam failed :("
    
