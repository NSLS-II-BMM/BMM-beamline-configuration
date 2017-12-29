

#----------------
e0       = 8333
element  = 'Ni'
material = 'NiAl2O4'
nscans   = 3
bothways = False
#----------------



from subprocess import call
import signal


## ----- deal with plotting
import numpy
import matplotlib         as mpl
#mpl.use('Qt4Agg')
import matplotlib.pyplot as plt
energy = numpy.array([])
#inot   = numpy.array([])
#itrans = numpy.array([])
mu     = numpy.array([])


import os.path
from termcolor import colored

from BMMcontrols import DCM, StepScan

dcm = DCM()
signal.signal(signal.SIGINT, dcm.handler)


## ----- define the scalars
scalars = (epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV"),
           epics.PV("XF:06BM-BI{EM:1}EM180:Current2:MeanValue_RBV"),
           epics.PV("XF:06BM-BI{EM:1}EM180:Current3:MeanValue_RBV"))




## ----- make the grid
# pre   = numpy.arange(e0-200, e0-30, 10.0)
# edge  = numpy.arange(e0-30,  e0+30,  0.5)
# begin = dcm.etok(30.)
# end   = 15 # dcm.etok(1200.)
# post  = e0+dcm.ktoe(numpy.arange(begin, end, 0.05))
# grid = list(pre) + list(edge) + list(post)

# basegrid = xanes_grid(-40,60,0.5)
basegrid = scan.conventional_grid((-200,-30,30,15),(10,0.5,0.05))


for i in range(1, nscans, 1):
    fname = 'data/%s_%s.%3.3d' % (element, material, i)
    if os.path.isfile(fname):
        print colored("%s already exists!" % fname, 'red', attrs=['bold'])
        exit()

    direction = 'increasing'
    if bothways:
        if i%2:
            grid = list(reversed(basegrid))
            direction = 'decreasing'
        else:
            grid = basegrid
            direction = 'increasing'
    else:
        grid = basegrid
        
    scan = StepScan(fname=fname)
    scan.file_header(element=element, e0=e0, material=material, monodir=direction)
    scan.column_labels()
    scan.handle.write(scan.file_header_text)
    
    plt.ion()
    plt.show()

    for en in grid:
        #ee = "%.3f" % en
        #call(['./DCM/dcm.py', '-c', '-e', ee, '-m'])
        dcm.moveto(en)
        values = [en]
        for s in scalars:
            values.append(s.get())

        line = " %.3f   %.7g   %.7g   %.7g\n" % (values)
        print line
        scan.handle.write(line)
        energy = numpy.append(energy, [en])
        mu     = numpy.append(mu,     [numpy.log(values[1]/values[2])])

        if en > e0-198:
            plt.clf()
            plt.title('%s %s scan %d' % (element, material, i))
            plt.grid(True)
            plt.xlabel('energy (eV)')
            plt.ylabel('absorption')
            plt.plot(energy, mu)
            plt.draw()
            plt.pause(0.001)

    plt.close()
    scan.handle.close()
