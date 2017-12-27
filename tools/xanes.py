
from subprocess import call
import signal
import epics
import numpy
import matplotlib         as mpl
mpl.use('Qt4Agg')
import matplotlib.pyplot as plt

ic1 = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
ic2 = epics.PV("XF:06BM-BI{EM:1}EM180:Current2:MeanValue_RBV")


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
e0      = 11564
element = 'Pt'

grid = numpy.arange(e0-40, e0+60, 0.5)

# pre   = numpy.arange(e0-200, e0-30, 10.0)
# edge  = numpy.arange(e0-30,  e0+30,  0.5)
# begin = etok(30.)
# end   = etok(1200.)
# post  = e0+ktoe(numpy.arange(begin, end, 0.05))
# grid = list(pre) + list(edge) + list(post)

fname = 'mono_calibration/111/cal/%sfoil.103' % element

data = open(fname, 'w')
data.write('# Si(111) calibration, %s edge\n' % element)
data.write('# -------------------------------------------\n')
data.write('# energy i0 it mu\n')

plt.ion()
plt.show()

for en in grid:
    ee = "%.3f" % en
    call(['./DCM/dcm.py', '-c', '-e', ee, '-m'])
    i0 = ic1.get()
    it = ic2.get()
        
    data.write(" %.3f   %.7g   %.7g   %.7g\n" % (en, i0, it, numpy.log(i0/it)))
    energy = numpy.append(energy, [ee])
    # inot   = numpy.append(inot,   [i0])
    # itrans = numpy.append(itrans, [it])
    mu     = numpy.append(mu,     [numpy.log(i0/it)])

    if en > grid[1]:
        plt.clf()
        plt.title('%s foil' % element)
        plt.grid(True)
        plt.xlabel('energy (eV)')
        plt.ylabel('absorption')
        plt.plot(energy, mu)
        plt.draw()
        plt.pause(0.001)

# name = raw_input("Hit enter to finish")
plt.close()
data.close()
