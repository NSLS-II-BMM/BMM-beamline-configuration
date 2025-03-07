#!/usr/bin/env python

import warnings
warnings.filterwarnings("ignore",".*GUI is implemented.*")
from time import sleep
from datetime import datetime
from os import mkdir
import os.path

from termcolor import colored
from argparse import ArgumentParser
parser = ArgumentParser(description="Perform and XAFS step scan")

##########
## macros!
parser.add_argument("-i", "--ini",                             dest="inifile",    default=None,
                    help="ini file name")
parser.add_argument("-r", "--run",      action="store_true",   dest="run",        default=False,
                    help="flag to skip sanity confirmation")
##########

parser.add_argument("-e", "--e0",       type=float,            dest="e0",         default=None,
                    help="edge energy")
parser.add_argument("-t", "--time",     type=float,            dest="inttime",    default=None,
                    help="integration time at each point")
parser.add_argument("-f", "--folder",                          dest="folder",     default=None,
                    help="folder in data directory")
parser.add_argument("-d", "--edge",                            dest="edge",       default=None,
                    help="edge energy")
parser.add_argument("-l", "--element",                         dest="element",    default=None,
                    help="absorber element")
parser.add_argument("-m", "--material",                        dest="filename",   default=None,
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
            'inttime'    : 1.0,
            'edge'       : 'K',
            'folder'     : '/home/bravel/commissioning/data',
            'element'    : 'Fe',
            'filename'   : 'Fe foil',
            'comment'    : 'quick measurement',
            'prep'       : '',
            'nscans'     : 1,
            'start'      : 0,
            'bothways'   : False,
            'channelcut' : False,
            'focus'      : True,
            'hr'         : False}
inifile = 'scan.ini'
if getattr(args, 'inifile') is not None:
    inifile = getattr(args, 'inifile')
if not os.path.isfile(inifile):
    print colored("%s does not exist!" % inifile, 'red', attrs=['bold'])
    exit()

print colored("\nInitializing from %s" % inifile, 'white', attrs=['bold'])

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

from BMMcontrols import DCM, StepScan, IonChambers, Vortex

dcm = DCM(crystals='111')
signal.signal(signal.SIGINT, dcm.handler)
xtals = '111'
if dcm.is311:
    xtals = '311'


################################################################################
## defaults, command line arguments, scan.ini

import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(inifile))

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
        try:
            times.append(float(f))
        except:
            times.append(f)
except:
    times = [0.5, 0.5, 0.5]



## handle single value times by make a list len(steps) long of that value
## truncate or fill in values so len(times) == len(steps)
## also k-weighted times

## ----- all other scan parameters
p = dict()

## strings
for a in ('folder', 'element', 'edge', 'filename'):
    if getattr(args, a) is not None:
        p[a] = getattr(args, a)
    else:
        try:
            p[a] = config.get('scan', a)
        except ConfigParser.NoOptionError:
            p[a] = defaults[a]

try:
    p['comment'] = config.get('scan', 'comment')
except ConfigParser.NoOptionError:
    p['comment'] = defaults['comment']


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
for a in ('e0', 'inttime'):
    if getattr(args, a) is not None:
        p[a] = args.e0
    else:
        try:
            p[a] = float(config.get('scan', a))
        except ConfigParser.NoOptionError:
            p[a] = defaults[a]


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

ic  = IonChambers()
vor = Vortex()
ic.set_avgtime(p['inttime'])
ic.acquiremode.put(2)
vor.set_avgtime(p['inttime'])
vor.acquiremode.put(1)


scalars = {'i0': True, 'it': True, 'ir': True,
           'vortex1': False, 'vortex2': False, 'vortex3': False, 'vortex4': False }
labels  = ['energy', 'requested_energy', 'encoder', 'measurement_time']
measure = list()
multiplier = list()
plotmode = config.get('scan', 'mode')

if 'fluo' in plotmode:
    scalars['vortex1'] = True
    scalars['vortex2'] = True
    scalars['vortex3'] = True
    scalars['vortex4'] = True

for s in ('i0', 'it', 'ir', 'vortex1', 'vortex2', 'vortex3', 'vortex4'):
    #try:
        #scalars[s] = config.getboolean('scalars', s)
    if s in ('i0', 'it', 'ir'):
        labels.append(s)
        measure.append(getattr(ic, s))
        multiplier.append(ic.multiplier)
    elif 'vortex' in s:
        n = s[-1]
        if scalars[s]:
            labels.extend(['roi'+n, 'icr'+n, 'ocr'+n, 'corr'+n])
            measure.extend([getattr(vor,'roi'+n), getattr(vor,'icr'+n), getattr(vor,'ocr'+n), 'corr'])
            multiplier.extend([1,1,1,1])
    #except ConfigParser.NoOptionError:
    #    scalars[s] = False

template = " %.3f  %.3f  %11d  %.4f"
for f in range(0, len(measure)):
    template = template + '   %.9g'
template = template + '\n'


#print labels
#print template
#print plotmode
#exit()

################################################################################

if not os.path.isdir(p['folder']):
    mkdir(p['folder'])


## ----- verify scan parameters before moving on
fname = '%s/%s.###' % (p['folder'], p['filename'])
print ''
for item in sorted(p.keys()):
    print '%s : %s' % (colored('%-10s'%item, 'green'), p[item])

print colored('\nscan mode', 'cyan'), '         :', plotmode
print colored('mono crystals', 'cyan'), '     :', dcm.description

print colored('\ngrid boundaries', 'cyan'), '   :', bounds
print colored('grid steps', 'cyan'), '        :', steps
print colored('integration times', 'cyan'), ' :', times
if p["channelcut"]:
    channelenergy = dcm.channelcut_energy(p["e0"], bounds)
    print '%s : %.1f' % (colored('channel cut energy', 'cyan'), channelenergy)
    print '%s : %.4f' % (colored('channel cut angle ', 'cyan'), dcm.angle(channelenergy))

print '\n%s : %s' % (colored('files written to', 'cyan'), fname)
print ''

if getattr(args, 'run') is False:
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
    fname = '%s/%s.%3.3d' % (p['folder'], p['filename'], i)
    if os.path.isfile(fname):
        print colored("%s already exists!" % fname, 'red', attrs=['bold'])
        exit()
    if not args.quiet:
        print fname
    scan = StepScan(fname=fname)
    for item in p.keys():
        setattr(scan, item, p[item])

    scan.e0 = float(scan.e0)

    (basegrid, timegrid) = scan.conventional_grid(bounds,steps,times)
    if basegrid is None:
        print colored("Invalid step scan parameters", 'red', attrs=['bold'])
        exit()

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
    scan.column_labels(labels)        # labels=('I0', 'It', 'Ir')
    scan.handle.write(scan.file_header_text())

    plt.ion()
    plt.show()

    ## pre-measure one point below the energy range, then toss it
    dcm.moveto(scan.grid[0]-5, quiet=True)
    ic.on()
    if 'fluo' in plotmode:
        vor.on()
    ic.measure()

    npts = len(scan.grid)
    begin = 0
    for (ne,en) in enumerate(scan.grid):
        #begin = datetime.now()
        requested_time = timegrid[ne]
        number_of_measurements = int(requested_time / 0.004)
        measurement_time = number_of_measurements * 0.004
        ic.set_avgtime(measurement_time)
        vor.set_avgtime(measurement_time)
        dcm.moveto(en, quiet=True)

        #sleep(1.1*p['inttime'])

        ic.acquire.put(1)
        vor.acquire.put(1)
        sleep(1.1*measurement_time)     # the pause should be a hair longer than the requested integration time
                                    # this gives the best linarity between the Vortex and electrometer signals.
        #values = [dcm.current_energy(), en, dcm.bragg.pv.REP, p['inttime']]
        values = [dcm.current_energy(), en, dcm.bragg.pv.REP, measurement_time]

        ## caput XF:06BM-BI{EM:1}EM180:AcquireMode 2             this puts the electrometer in Single acquire mode
        ## caput XF:06BM-BI{EM:1}EM180:Acquire 1                 this makes one measurement over the averaging time
        ## caput XF:06BM-ES:1{Sclr:1}.CONT 0                     this puts the Struck in OneCount mode
        ## caput XF:06BM-ES:1{Sclr:1}.CNT 1                      this makes one measurement over the count time

        for (j,pv) in enumerate(measure):
            try:
                this = pv.get()
                values.append(this*multiplier[j])
            except:
                (roi,icr,ocr) = values[-3:]
                values.append(vor.dtcorrect(roi,icr,ocr, time=p['inttime']))

        line = template % tuple(values)
        if not args.quiet:
            print "%d/%d  "%(ne+1, npts), line[:-1]
        scan.handle.write(line)
        scan.handle.flush()
        energy = numpy.append(energy, [en])
        if plotmode[0] is 'f':
            mu = numpy.append(mu, [(values[10]+values[14]+values[18]+values[22])/values[4]])
        elif plotmode[0] is 'r':
            mu = numpy.append(mu, [numpy.log(values[5]/values[6])])
        else:
            mu = numpy.append(mu, [numpy.log(values[4]/values[5])])

        plt.clf()
        plt.title('%s %s scan %d' % (p['element'], p['filename'], i))
        plt.grid(True)
        plt.xlabel('energy (eV)')
        plt.ylabel('absorption')
        plt.plot(energy, mu)
        plt.draw()
        plt.pause(0.001)

    scan.handle.close()
    #print('That scan took ', datetime.now()-begin)
    #print '\n'

if p["channelcut"]:
    print "Moving to %.1f and returning to fixed exit mode" % channelenergy
    dcm.channelcut = False
    dcm.moveto(channelenergy, quiet=True)


ic.reset_avgtime()
vor.reset_avgtime()
if getattr(args, 'run') is False:
    action = raw_input("RET to quit ")
plt.close()
