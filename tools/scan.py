

from termcolor import colored
from argparse import ArgumentParser
parser = ArgumentParser(description="Perform and XAFS step scan")
parser.add_argument("-e", "--e0",       type=float,          dest="e0",       default=None,
                    help="edge energy")
parser.add_argument("-f", "--folder",                        dest="folder",   default=None,
                    help="folder in data directory")
parser.add_argument("-d", "--edge",                          dest="edge",     default=None,
                    help="edge energy")
parser.add_argument("-l", "--element",                       dest="element",  default=None,
                    help="absorber element")
parser.add_argument("-m", "--material",                      dest="material", default=None,
                    help="material description")
parser.add_argument("-n", "--nscans",   type=int,            dest="nscans",   default=None,
                    help="number of scans")
parser.add_argument("-s", "--start",    type=int,            dest="start",    default=None,
                    help="starting scan number")
parser.add_argument("-b", "--bothways", action="store_true", dest="bothways", default=None,
                    help="flag specifying scans in both directions -- default is always up")
args = parser.parse_args()


defaults = {'e0'       : 7112,
            'edge'     : 'K',
            'folder'   : 'data',
            'element'  : 'Fe',
            'material' : 'Fe foil',
            'comment'  : 'quick measurement',
            'prep'     : '',
            'nscans'   : 1,
            'start'    : 0}


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

p = dict()

if args.folder is not None:
    p['folder'] = args.folder
else:
    try:
        p['folder'] = config.get('scan', 'folder')
    except ConfigParser.NoOptionError:
        p['folder'] = defaults['folder']

        
if args.nscans is not None:
    p['nscans'] = args.nscans
else:
    try:
        p['nscans'] = int(config.get('scan', 'nscans'))
    except ConfigParser.NoOptionError:
        p['nscans'] = defaults['nscans']

if args.start is not None:
    p['start'] = args.start
else:
    try:
        p['start'] = int(config.get('scan', 'start'))
    except ConfigParser.NoOptionError:
        p['start'] = defaults['start']

if args.element is not None:
    p['element'] = args.element
else:
    try:
        p['element'] = config.get('scan', 'element')
    except ConfigParser.NoOptionError:
        p['element'] = defaults['element']

if args.edge is not None:
    p['edge'] = args.edge
else:
    try:
        p['edge'] = config.get('scan', 'edge')
    except ConfigParser.NoOptionError:
        p['edge'] = defaults['edge']

if args.e0 is not None:
    p['e0'] = args.e0
else:
    try:
        p['e0'] = float(config.get('scan', 'e0'))
    except ConfigParser.NoOptionError:
        p['e0'] = defaults['e0']

if args.material is not None:
    p['material'] = args.material
else:
    try:
        p['material'] = config.get('scan', 'material')
    except ConfigParser.NoOptionError:
        p['material'] = defaults['material']

if args.bothways is not None:
    p['bothways'] = args.bothways
else:
    try:
        p['bothways'] = config.getboolean('scan', 'bothways')
    except ConfigParser.NoOptionError:
        p['bothways'] = defaults['bothways']

################################################################################
        
if not os.path.isdir('data/%s' % p['folder']):
    mkdir('data/%s' % p['folder'])

fname = 'data/%s/%s.###' % (p['folder'], p['material'])
print ''
for item in sorted(p.keys()):
    print '%s : %s' % (colored('%-9s'%item, 'green'), p[item])
print '\n%s : %s' % (colored('files written to', 'cyan'), fname)
print ''

action = raw_input("q to quit -- any other key to start scans > ")
if action is 'q':
    exit()

for i in range(p['start'], p['start']+p['nscans'], 1):
    fname = 'data/%s/%s.%3.3d' % (p['folder'], p['material'], i)
    if os.path.isfile(fname):
        print colored("%s already exists!" % fname, 'red', attrs=['bold'])
        exit()
    print fname
    scan = StepScan(fname=fname)
    for item in defaults.keys():
        if item in ('nscans', 'bothways'): continue
        try:
            setattr(scan, item, config.get('scan', item))
        except ConfigParser.NoOptionError:
            setattr(scan, item, defaults[item])
    scan.e0 = float(scan.e0)
    
    #basegrid = scan.xanes_grid(-40,60,0.5)
    basegrid = scan.conventional_grid([-200,-30,30,'18k'],[10,0.5,0.05])
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

    plt.close()
    scan.handle.close()
