#!/usr/bin/python

from time import sleep
from numpy import pi, sin, cos, arcsin, tan, arctan2
from termcolor import colored
import epics
import signal
import sys

from BMMcontrols import BMM_Motor

filters = BMM_Motor('filter-assembly-1')
scanrange = 9
rest = 30



def handler(signum, frame):
    print '\n\n*** Got CTRL+C, stopping all motors ***'
    filters.stop()
    print ""
    print "filter at %.4f" % filters.pv.RBV
    exit()

signal.signal(signal.SIGINT, handler)

    
start = 1
for i in range(0,50):
    print "step %d up" % i 
    filters.one_axis_move(scanrange, rel=True)
    print "sleep for %d seconds" % rest
    sleep(rest)
    print "step %d down" % i 
    filters.one_axis_move(-scanrange, rel=True)
    print "sleep for %d seconds" % rest
    sleep(rest)

