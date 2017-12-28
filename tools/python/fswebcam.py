
from os import system
from os.path import expanduser
from subprocess import Popen, PIPE, call
import fcntl
import datetime

from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color

class fswebcam():
    """
    A class for interacting with fswebcam in a way that meets the needs of 06BM.

    Methods:
      snapshot:   take a snapshot from an analog camera
      reset:      reset the char device for the camera
      crosshairs: draw a cross hair on the image using image magick

    Attributes:
      folder:   location to drop jpg image          [$HOME]
      device:      char device of camera            [/dev/video0]
      camera:      camera number                    [0]
      skip:        number of frames to skip waiting for camera to wake up [30]
      frames:      number of frames to accumulate in image [5]
      brightness:  brightness setting of camera as a percentage [20]
      x:           X-location of cross hair         [320] (middle of image)
      y:           Y-location of cross hair         [240] (middle of image)
      linecolor:   color of cross hair lines        [white]
      nocrosshair: flag to suppress cross hair      [False]
      quiet:       flag to suppress screen messages [False]
      usbid:       vendor and product ID of camera  [534d:0021] (AV to USB device at 06BM)
      title:       title string for fswebcam banner [NIST BMM (NSLS-II 06BM)]
      prefix:      filename prefix                  [BMM_analog_camera_]
      filename:    output file name                 [ISO 8601 timestamp in self.folder]
    """
    def __init__(self):
        self.folder      = expanduser("~")
        self.device      = "/dev/video0"
        self.camera      = 0
        self.skip        = 30
        self.frames      = 5
        self.brightness  = 20
        self.x           = 320
        self.y           = 240
        self.linecolor   = "white"
        self.nocrosshair = False
        self.quiet       = False
        self.usbid       = "534d:0021"
        self.title       = "NIST BMM (NSLS-II 06BM)"
        self.timestamp   = "%Y-%m-%d %H:%M:%S"
        self.prefix      = "BMM_analog_camera_"
        self.filename    = None

    USBDEVFS_RESET= 21780

    def reset(self):
        """Reset the video char device.  Swiped from https://askubuntu.com/a/591979"""
        if not self.quiet: print "resetting video device"
        try:
            lsusb_out = Popen("lsusb | grep -i %s" % self.usbid,
                              shell=True,
                              bufsize=64,
                              stdin=PIPE,
                              stdout=PIPE, close_fds=True).stdout.read().strip().split()
            bus = lsusb_out[1]
            device = lsusb_out[3][:-1]
            f = open("/dev/bus/usb/%s/%s"%(bus, device), 'w', os.O_WRONLY)
            fcntl.ioctl(f, USBDEVFS_RESET, 0)
            sleep(1)
        except Exception, msg:
            print "failed to reset device:", msg


    def snapshot(self):
        """Take a snapshop by making a system call to fswebcam"""
        quiet = ''
        if self.quiet: quiet = '-q '
        if self.filename is None:
            self.filename = "%s/%s%s.jpg" %\
                            (self.folder, self.prefix, datetime.datetime.now().replace(microsecond=0).isoformat())
        command = "fswebcam %s-i %s -d %s -r 640x480 --title \"%s\" --timestamp \"%s\" -S %d -F %d --set brightness=%s%% %s" %\
                  (quiet, self.camera, self.device, self.title, self.timestamp, self.skip, self.frames, self.brightness, self.filename)
        system(command)


    def crosshairs(self):
        """Draw crosshairs at (x,y) using image magick"""
        if not self.quiet: print "Drawing cross hair at %d,%d" % (self.x, self.y)
        with Image(filename=self.filename) as image:
            with Drawing() as draw:
                with Color(self.linecolor) as color:
                    draw.fill_color = color
                    draw.line((self.x, 0), (self.x, 479))
                    draw.line((0, self.y), (639, self.y))
                    draw(image)
                    image.format = 'jpeg'
                    image.save(filename=self.filename)
