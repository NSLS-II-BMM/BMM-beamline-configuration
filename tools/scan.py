#!/usr/bin/env python

import warnings
warnings.filterwarnings("ignore",".*GUI is implemented.*")

from termcolor import colored
from argparse import ArgumentParser
parser = ArgumentParser(description="Perform and XAFS step scan")
parser.add_argument("-e", "--e0",       type=float,            dest="e0",         default=None,
                    help="edge energy")
parser.add_argument("-f", "--folder",                          dest="folder",     default=None,
                    help="folder in data directory")
parser.add_argument("-d", "--edge",                            dest="edge",       default=None,
                    help="edge energy")
parser.add_argument("-l", "--element",                         dest="element",    default=None,
                    help="absorber element")
parser.add_argument("-m", "--material",                        dest="material",   default=None,
                    help="material description")
parser.add_argument("-n", "--nscans",   type=int,              dest="nscans",     default=None,
                    help="number of scans")
parser.add_argument("-s", "--start",    type=int,              dest="start",      default=None,
                    help="starting scan number")
parser.add_argument("-b", "--bothways",   action="store_true", dest="bothways",   default=None,
                    help="flag specifying scans in both directions -- default is always up")
parser.add_argument("-c", "--channelcut", action="store_true", dest="channelcut", default=None,
                    help="flag specifying to scan in pseudo-channel-cut mode -- default is not")
parser.add_argument("-q", "--quiet",      action="store_true", dest="quiet",      default=False,
                    help="suppress all in-scan screen output")
args = parser.parse_args()


defaults = {'e0'         : 7112,
            'edge'       : 'K',
            'folder'     : 'data',
            'element'    : 'Fe',
            'material'   : 'Fe foil',
            'comment'    : 'quick measurement',
            'prep'       : '',
            'nscans'     : 1,
            'start'      : 0,
            'bothways'   : False,
            'channelcut' : False,
            'focus'      : True,
            'hr'         : False}


import signal
import epics

## ----- deal with plotting
import numpy
import matplotlib         as mpl
#mpl.use('Qt4Agg')
import matplotlib.pyplot as plt
energy = numpy.array([])
#inot   = numpy.array([])
#itrans = numpy.array([])
mu     = numpy.array([])


from os import mkdir
import os.path

from BMMcontrols import DCM, StepScan, IonChambers

dcm = DCM()
signal.signal(signal.SIGINT, dcm.handler)
xtals = '111'
if dcm.is311:
    xtals = '311'

ic = IonChambers()


################################################################################
## defaults, command line arguments, scan.ini

import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('scan.ini'))

## ----- scan regions
bounds = []
try:
    for f in config.get('scan', 'bounds').split():
        try:
            bounds.append(float(f))
        except:
            bounds.append(f)
except:
    bounds = [-200.0, -30.0, 30.0, '15k']

steps = []
try:
    for f in config.get('scan', 'steps').split():
        try:
            steps.append(float(f))
        except:
            steps.append(f)
except:
    steps = [10.0, 0.5, '0.5k']

times = []
try:
    for f in config.get('scan', 'times').split():
        times.append(float(f))
except:
    times = [0.5, 0.5, 0.5]
    

## ----- all other scan parameters
p = dict()

## strings
for a in ('folder', 'element', 'edge', 'material'):
    if getattr(args, a) is not None:
        p[a] = getattr(args, a)
    else:
        try:
            p[a] = config.get('scan', a)
        except ConfigParser.NoOptionError:
            p[a] = defaults[a]

## integers
for a in ('start', 'nscans'):
    if getattr(args, a) is not None:
        p[a] = getattr(args, a)
    else:
        try:
            p[a] = int(config.get('scan', a))
        except ConfigParser.NoOptionError:
            p[a] = defaults[a]

## floats
if args.e0 is not None:
    p['e0'] = args.e0
else:
    try:
        p['e0'] = float(config.get('scan', 'e0'))
    except ConfigParser.NoOptionError:
        p['e0'] = defaults['e0']


## booleans
for a in ('bothways', 'channelcut'):        
    if getattr(args, a) is not None:
        p[a] = getattr(args, a)
    else:
        try:
            p[a] = config.getboolean('scan', a)
        except ConfigParser.NoOptionError:
            p[a] = defaults[a]
for a in ('focus', 'hr'):
    try:
        p[a] = config.getboolean('scan', a)
    except ConfigParser.NoOptionError:
        p[a] = defaults[a]
            

################################################################################
        
if not os.path.isdir('data/%s' % p['folder']):
    mkdir('data/%s' % p['folder'])


## ----- verify scan parameters before moving on
fname = 'data/%s/%s.###' % (p['folder'], p['material'])
print ''
for item in sorted(p.keys()):
    print '%s : %s' % (colored('%-10s'%item, 'green'), p[item])

print colored('\ngrid boundaries', 'cyan'), '   :', bounds
print colored('grid steps', 'cyan'), '        :', steps       
if p["channelcut"]:
    channelenergy = dcm.channelcut_energy(p["e0"], bounds)
    print '%s : %.1f' % (colored('channel cut energy', 'cyan'), channelenergy)

print '\n%s : %s' % (colored('files written to', 'cyan'), fname)
print ''




action = raw_input("q to quit -- any other key to start scans > ")
if action is 'q':
    exit()

## ----- check if shutter is open
shutter_status = epics.PV("XF:06BM-PPS{Sh:A}Pos-Sts")
while shutter_status.get():
    print "\n", colored("Shutter is closed!  Open the shutter, then ...", "red", attrs=["bold"])
    action = raw_input("q to quit -- any other key to start scans > ")
    if action is 'q':
        exit()

if p["channelcut"]:
    print "Moving to %.1f and setting pseudo channelcut mode" % channelenergy
    dcm.moveto(channelenergy, quiet=True)
    dcm.channelcut = True
        

    
for i in range(p['start'], p['start']+p['nscans'], 1):
    fname = 'data/%s/%s.%3.3d' % (p['folder'], p['material'], i)
    if os.path.isfile(fname):
        print colored("%s already exists!" % fname, 'red', attrs=['bold'])
        exit()
    if not args.quiet:
        print fname
    scan = StepScan(fname=fname)
    for item in p.keys():
        setattr(scan, item, p[item])

    scan.e0 = float(scan.e0)

    basegrid = scan.conventional_grid(bounds,steps)
    if basegrid is None:
        print colored("Invalid step scan parameters", 'red', attrs=['bold'])
    
    scan.direction = 'increasing'
    if p['bothways']:
        if i%2:
            scan.grid = list(reversed(basegrid))
            scan.direction = 'decreasing'
        else:
            scan.grid = basegrid
            scan.direction = 'increasing'
    else:
        scan.grid = basegrid
        
    scan.file_header(dcm=dcm)
    scan.column_labels()        # labels=('I0', 'It', 'Ir')
    scan.handle.write(scan.file_header_text())

    
    plt.ion()
    plt.show()

    for en in scan.grid:
        dcm.moveto(en, quiet=True)
        values = [en]
        values.extend(ic.measure())

        line = " %.3f   %.7g   %.7g   %.7g\n" % tuple(values)
        if not args.quiet:
            print line[:-1]
        scan.handle.write(line)
        energy = numpy.append(energy, [en])
        mu     = numpy.append(mu,     [numpy.log(values[1]/values[2])])

        plt.clf()
        plt.title('%s %s scan %d' % (p['element'], p['material'], i))
        plt.grid(True)
        plt.xlabel('energy (eV)')
        plt.ylabel('absorption')
        plt.plot(energy, mu)
        plt.draw()
        plt.pause(0.001)

    scan.handle.close()

if p["channelcut"]:
    print "Moving to %.1f and returning to fixed exit mode" % channelenergy
    dcm.channelcut = False
    dcm.moveto(channelenergy, quiet=True)

action = raw_input("RET to quit ")
plt.close()
    
