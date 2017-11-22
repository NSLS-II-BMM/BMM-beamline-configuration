
from subprocess import call
import epics
import numpy
import matplotlib         as mpl
mpl.use('Qt4Agg')
import matplotlib.pyplot as plt
plt.ion()
plt.show()

ic1 = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
ic2 = epics.PV("XF:06BM-BI{EM:1}EM180:Current2:MeanValue_RBV")


energy = numpy.array([])
#inot   = numpy.array([])
#itrans = numpy.array([])
mu     = numpy.array([])


KTOE = 3.8099819442818976
def etok(ee):
    return numpy.sqrt(ee/KTOE)
def ktoe(k):
    return k*k*KTOE
e0    = 11564  # 7709.0 # 11919  8979  7112   5989
pre   = numpy.arange(e0-200, e0-30, 10.0)
edge  = numpy.arange(e0-30,  e0+30,  0.5)
begin = etok(30.)
end   = etok(1200.)
post  = e0+ktoe(numpy.arange(begin, end, 0.05))

grid = list(pre) + list(edge) + list(post)

for i in (0, 1):
    if i%2:
        grid = list(reversed(grid))
        fname = 'mono_calibration/3/ptfoil.down'
    else:
        fname = 'mono_calibration/3/ptfoil.up'
        
    data = open(fname, 'w')
    data.write('# energy i0 it mu\n')

    for en in grid:
        ee = "%.3f" % en
        call(['./DCM/dcm.py', '-c', '-e', ee, '-m'])
        i0 = ic1.get()
        it = ic2.get()
       
        data.write(" %.3f   %.7g   %.7g   %.7g\n" % (en, i0, it, numpy.log(i0/it)))
        energy = numpy.append(energy, [ee])
        #inot   = numpy.append(inot,   [i0])
        #itrans = numpy.append(itrans, [it])
        mu     = numpy.append(mu,     [numpy.log(i0/it)])

        if en > e0-198:
            plt.clf()
            plt.plot(energy, mu)
            plt.draw()
            plt.pause(0.001)

    #name = raw_input("Hit enter to finish")
    plt.close()
    data.close()
