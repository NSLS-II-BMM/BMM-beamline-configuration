
from subprocess import call
import signal
import epics
import numpy
import matplotlib         as mpl
#mpl.use('Qt4Agg')
import matplotlib.pyplot as plt
from time import strftime
import os.path
from termcolor import colored

ic1 = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
ic2 = epics.PV("XF:06BM-BI{EM:1}EM180:Current2:MeanValue_RBV")
ic3 = epics.PV("XF:06BM-BI{EM:1}EM180:Current3:MeanValue_RBV")


energy = numpy.array([])
#inot   = numpy.array([])
#itrans = numpy.array([])
mu     = numpy.array([])


def handler(signum, frame):
    print '\n\nGot CTRL+C, stopping all motors'

    for pv in (epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr"),
               epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr"),
               epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr")):
        pv.put('STOP', 1)
    for pv in (epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr_KILL_CMD.PROC"),
               epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr_KILL_CMD.PROC"),
               epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr_KILL_CMD.PROC"),
               epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr_KILL_CMD.PROC")):
        pv.put(1)
        
    print ""
    call(['python', '/home/bravel/commissioning/en.py'])
    exit(0)

signal.signal(signal.SIGINT, handler)


KTOE = 3.8099819442818976
def etok(ee):
    return numpy.sqrt(ee/KTOE)
def ktoe(k):
    return k*k*KTOE
#----------------
e0       = 8333
element  = 'Ni'
material = 'NiAl2O4'
#----------------

pre   = numpy.arange(e0-200, e0-30, 10.0)
edge  = numpy.arange(e0-30,  e0+30,  0.5)
begin = etok(30.)
end   = 15 # etok(1200.)
post  = e0+ktoe(numpy.arange(begin, end, 0.05))

grid = list(pre) + list(edge) + list(post)

#for i in (0, 1):
#    if i%2:
#        grid = list(reversed(grid))
#        fname = 'mono_calibration/311/ptfoil.down'
#    else:
for i in range(1, 3, 1):
    fname = 'data/%s_%s.%3.3d' % (element, material, i)
    if os.path.isfile(fname):
        print colored("%s already exists!" % fname, 'red', attrs=['bold'])
        exit()
    
    data = open(fname, 'w')
    data.write('# XDI/1.0\n')
    data.write('# Column.1: energy eV\n')
    data.write('# Column.2: i0\n')
    data.write('# Column.3: itrans\n')
    data.write('# Column.4: iref\n')
    data.write('# Element.edge: K\n')
    data.write('# Element.symbol: %s\n' % element)
    data.write('# Scan.edge_energy: %.1f\n' % e0)
    data.write('# Mono.name: Si 111\n')
    data.write('# Mono.d_spacing: 3.13572865\n')
    data.write('# Beamline.name: 06BM\n')
    data.write('# Beamline.collimation: paraboloid mirror, 5 nm Rh on 30 nm Pt\n')
    data.write('# Beamline.focusing: none\n')
    data.write('# Beamline.harmonic_rejection: Rh/Pt mirror\n')
    data.write('# Facility.name: NSLS-II\n')
    data.write('# Facility.energy: 3 GeV\n')
    data.write('# Facility.xray_source: NSLS-II three-pole wiggler\n')
    data.write('# Scan.start_time: %s\n' % strftime("%Y-%m-%dT%H:%M:%S"))
    data.write('# Detector.I0: 10cm  N2\n')
    data.write('# Detector.I1: 25cm  N2\n')
    
    data.write('# Sample.name: %s\n' % material)
    data.write('# Sample.prep: powder on kapton tape\n')

    data.write('# ///\n')
    data.write('# quick measurement\n')
    data.write('# -------------------------------------------\n')
    data.write('# energy i0 it ir\n')

    plt.ion()
    plt.show()

    for en in grid:
        ee = "%.3f" % en
        call(['./DCM/dcm.py', '-c', '-e', ee, '-m'])
        i0 = ic1.get()
        it = ic2.get()
        ir = ic3.get()
        
        data.write(" %.3f   %.7g   %.7g   %.7g\n" % (en, i0, it, ir))
        #data.write(" %.3f   %.7g   %.7g\n" % (en, i0, it))
        energy = numpy.append(energy, [ee])
        mu     = numpy.append(mu,     [numpy.log(i0/it)])

        if en > e0-198:
            plt.clf()
            plt.title('%s %s scan %d' % (element, material, i))
            plt.grid(True)
            plt.xlabel('energy (eV)')
            plt.ylabel('absorption')
            plt.plot(energy, mu)
            plt.draw()
            plt.pause(0.001)

    # name = raw_input("Hit enter to finish")
    plt.close()
    data.close()
