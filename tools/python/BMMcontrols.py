
import os
import sys
import signal
from time import sleep, strftime
import epics
import numpy
from numpy import pi, sin, cos, arcsin, tan, arctan2
from termcolor import colored
import json

HBARC = 1973.27053324

GITREPO = '/home/bravel/git/BMM-beamline-configuration/'
MOTORDATA = json.load(open(os.path.join(GITREPO, 'Modes.json')))

################################################################################
################################################################################
################################################################################

class BMM_Motor():
    def __init__(self, alias):
        self.pv           = None
        self.kill_pv      = None
        self.enable_pv    = None
        self.home_pv      = None
        self.invacuum     = False
        self.disconnected = False
        self.units        = None
        self.description  = None
        if alias is not None:
            self.motor(alias)

    def motor(self, alias):
        self.pv = epics.Motor(MOTORDATA[alias]['PV'])
        self.description = MOTORDATA[alias]['desc']
        if alias not in MOTORDATA.keys():
            return False
        if 'xafs' in alias:
            thing = MOTORDATA[alias]['PV'].replace('Mtr', 'Cmd:Kill-Cmd')
            self.kill_pv   = epics.PV(thing)
            self.enable_pv = None
            self.home_pv   = None
        else:
            self.kill_pv   = epics.PV(MOTORDATA[alias]['PV']+'_KILL_CMD.PROC')
            self.enable_pv = epics.PV(MOTORDATA[alias]['PV']+"_ENA_CMD.PROC")
            self.home_pv   = None # epics.PV(MOTORDATA[alias]['PV']+"_HOME_CMD_PROC")
            
    def stop(self):
        self.pv.put('STOP', 1)
        
    def enable(self):
        self.enable_pv.put(1)
        
    def kill(self, really=False):
        if self.kill_pv is not None:
            if self.invacuum:
                self.kill_pv.put('1')
            elif really:
                self.kill_pv.put('1')


    def one_axis_move(self, val, rel=False):
        def message(string):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write(string)
        template = '  %s --> %8.4f'
        sys.stdout.write(template % (self.description, self.pv.RBV))

    
        if not self.pv.within_limits(val):
            print colored("Request to move outside limits on %s" % pv.DESC, 'red', attrs=['bold'])
            exit()
        self.pv.move(val, relative=rel, wait=False)
        waiting = True
        while waiting:
            sleep(0.001)
            message(template % (self.description, self.pv.RBV))
            sleep(0.1)
            waiting = not self.pv.done_moving
        message(template % (self.description, self.pv.RBV))
        print ''
        return 0
            
################################################################################
################################################################################
################################################################################

class DCM():
    def __init__(self):
        self.twod = None
        self.description = None
        self.xtals()
        self.mono_offset = 30   # mm
        self.emin = 4000        # eV
        self.emax = 22300       # eV
        self.bragg = BMM_Motor('dcm-bragg')
        self.perp  = BMM_Motor('dcm-perp')
        self.para  = BMM_Motor('dcm-para')
        self.pitch = BMM_Motor('dcm-pitch')
        self.roll  = BMM_Motor('dcm-roll')
        self.x     = BMM_Motor('dcm-x')
        self.y     = BMM_Motor('dcm-y')
        self.perp.invacuum = self.para.invacuum = self.pitch.invacuum = self.roll.invacuum = True
        self.paraoffset = 0
        self.perpoffset = 0
        
    def xtals(self, crystals='111'):
        if crystals is '311':
            self.twod = 2*1.63761489
            self.description = 'Si(311)'
        else:
            self.twod = 2*3.13543952
            self.description = 'Si(111)'
            
    def e2l(self, val):
        return 2*pi*HBARC/val

    def wavelength(self, val):
        return self.twod * sin(val * pi / 180)

    def current_energy(self):
        angle = self.bragg.pv.RBV
        wavelength = self.wavelength(angle)
        return self.e2l(wavelength)

    def angle(self, energy):
        wavelength = self.e2l(energy)
        return 180 * arcsin(wavelength / self.twod) / pi

    def parallel(self, energy):
        wavelength = self.e2l(energy)
        angle      = arcsin(wavelength / self.twod)
        return self.mono_offset / (2*sin(angle))

    def perpendicular(self, energy):
        wavelength = self.e2l(energy)
        angle      = arcsin(wavelength / self.twod)
        return self.mono_offset / (2*cos(angle))
    
    def kill(self, axis):
        axis.kill_pv.put(1)
        return 1

    def kill_invacuum(self):
        self.perp.kill_pv.put(1)
        self.para.kill_pv.put(1)
        self.pitch.kill_pv.put(1)
        self.roll.kill_pv.put(1)

    def seven(self):
        return(self.bragg, self.perp, self.para, self.pitch, self.roll, self.x, self.y)
        
    def handler(self, signum, frame):
        print colored('\n\nGot CTRL+C, stopping all motors, disabling in-vacuum motors', 'red', attrs=['bold'])
        for ax in self.seven():
            ax.stop()
            ax.kill()
        print ""
        self.prettyprint_motors(self.bragg, self.perp, self.para, color="red", status="current")
        exit()
        
    def moveto(self, energy, para=None, perp=None, quiet=False):
        if energy < self.emin:
            print "cannot move to %.2f -- too low!" % energy
            return 0
        if energy > self.emax:
            print "cannot move to %.2f -- too high!" % energy
            return 0
        if para is None:
            para = self.parallel(energy) + self.paraoffset
        if perp is None:
            perp = self.perpendicular(energy) + self.perpoffset

        angle    = dcm.angle(energy)
        axes     = (dcm.bragg, dcm.perp, dcm.para)
        template = ' bragg, perp, para --> %8.4f  %8.4f  %8.4f'
        newvals  = (angle, perp, para)
        self.generic_move(axes, values, template, quiet)
        return self.current_energy()

    def change_xtals(self, values=None):
        if values is None:
            return 0
        axes     = (dcm.pitch, dcm.roll, dcm.x)
        template = ' pitch, roll, x --> %8.4f  %8.4f  %8.4f'
        self.generic_move(axes, values, template)
        
    def generic_move(self, axes=None, values=None, template=None, quiet=False):
        if axes is None:
            print "Must provide a list of axes to generic_move"
            exit()
        if values is None:
            print "Must provide a list of values to generic_move"
            exit()
        if template is None:
            print "Must provide a template to generic_move"
            exit()
        ## also check on equal lengths of axes and values (and number of %f in template)

        def message(string):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write(string)

        rbvs = list()
        for ax in axes:
            rbvs.append(ax.pv.RBV)
        if not quiet: sys.stdout.write(template % tuple(rbvs))

        for ax, val in zip(axes, values):
            if not ax.pv.within_limits(val):
                print colored("Request to move outside limits on %s" % ax.pv.DESC, 'red', attrs=['bold'])
                exit()
            ax.pv.move(val, wait=False)
            
        ##------------------------------------------------------------------------
        ## wait for all three motors to get where they are going
        waiting = True
        while waiting:
            sleep(0.001)
            updt = list()
            for ax in axes:
                updt.append(ax.pv.RBV)
            if not quiet: message(template % tuple(updt))
            sleep(0.1)
            waiting = not all([ax.pv.done_moving for ax in axes])
        for ax in axes:
            ax.kill()
        updt = list()
        for ax in axes:
            updt.append(ax.pv.RBV)
        if not quiet:
            message(template % tuple(updt))
            print '\n'

    
    def prettyprint_energy(self, energy, status="Mono at", color="white", attrs=None):
        # print "%s = %.1f   %s = %s   (perp/para offset = %.2f/%.2f)" % \
        print "%s = %.1f   %s = %s" % \
            (colored(status,       color, attrs=attrs), energy,
             colored('reflection', color, attrs=attrs), self.description)  #  args.perpoffset, args.paraoffset)

    
    def prettyprint_motors(self, bragg, perp, para, color="white", status="current", attrs=None):
        if status is 'current':
            # print "current: %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)\n" %
            print "%s: %s = %8.5f   %s = %7.4f   %s = %8.4f" %\
                (status,
                 colored(bragg.pv.DESC,color, attrs=attrs), bragg.pv.RBV,
                 colored(perp.pv.DESC, color, attrs=attrs), perp.pv.RBV,  #  - args.perpoffset,
                 colored(para.pv.DESC, color, attrs=attrs), para.pv.RBV)  #  - args.paraoffset)
        else:
            print "%s: %s = %8.5f   %s = %7.4f   %s = %8.4f" %\
                (status,
                 colored('angle',color, attrs=attrs), bragg,
                 colored('perp', color, attrs=attrs), perp,  #  - args.perpoffset,
                 colored('para', color, attrs=attrs), para)  #  - args.paraoffset)
        
    def prettyline(self, color="white"):
        print colored('='*65, color)


################################################################################
################################################################################
################################################################################
class Mirror():
    def __init__(self, m):
        self.m      = None
        self.hutch  = 'A'
        self.length = None
        self.width  = None
        self.vert   = None
        self.lat    = None
        self.pitch  = None
        self.roll   = None
        self.yaw    = None
        self.set_mirror(m)
        self.current_positions()
        self.direction = None
    
    def set_mirror(self, m):
        if m in (1,2,3,4):
            self.m = m
        else:
            return 0
        ## actual mirrors
        if m<4:
            self.yu  = BMM_Motor('m%d-jack1' % m)
            self.ydo = BMM_Motor('m%d-jack2' % m)
            self.ydi = BMM_Motor('m%d-jack3' % m)
            self.xu  = BMM_Motor('m%d-lateral-u' % m)
            self.xd  = BMM_Motor('m%d-lateral-d' % m)
            if m is 1:
                self.length = 556
                self.width = 240
                self.description = 'M1: collimating mirror'
                self.hutch = ''
            elif m is 2:
                self.length = 1288
                self.width = 240
                self.description = 'M2: focusing mirror'
                self.xu.invacuum = self.xd.invacuum = True
            elif m is 3:
                self.length = 667
                self.width = 240
                self.description = 'M3: harmonic rejection mirror'
                self.xu.invacuum = self.xd.invacuum = True

        ## XAFS table
        else:
            self.yu  = BMM_Motor("xafs_tbl_yu")
            self.ydo = BMM_Motor("xafs_tbl_ydo")
            self.ydi = BMM_Motor("xafs_tbl_ydi")
            self.xu  = BMM_Motor("xafs_tbl_xu")
            self.xd  = BMM_Motor("xafs_tbl_xd")
            self.xu.disconnected = self.xd.disconnected = True
            self.length = 1160
            self.width = 558
            self.description = 'XAFS table'
            self.hutch = ''
        self.yu.units = self.ydo.units = self.ydi.units = self.xu.units = self.xd.units = 'mm'
        return 1

    def five(self):
        return (self.yu, self.ydo, self.ydi, self.xu, self.xd)
            
    def handler(self, signum, frame):
        print colored('\n\nGot CTRL+C, stopping all motors, disabling in-vacuum motors', 'red', attrs=['bold'])
        for ax in self.five():
            ax.stop()
            ax.kill()
        print ""
        self.where()
        exit(0)

            
    def current_positions(self):
        self.vert  = (self.yu.pv.RBV  + (self.ydo.pv.RBV+self.ydi.pv.RBV)/2) / 2
        self.lat   = (self.xu.pv.RBV  + self.xd.pv.RBV)  / 2
        dbar       = (self.ydo.pv.RBV + self.ydi.pv.RBV) / 2
        self.pitch = 1000*arctan2( (dbar-self.yu.pv.RBV),        self.length )
        self.roll  = 1000*arctan2( self.ydo.pv.RBV-self.ydi.pv.RBV, self.width )
        self.yaw   = 1000*arctan2( self.xd.pv.RBV-self.xu.pv.RBV,   self.length )

    def where(self, color='white', attrs=None):
        self.current_positions()
        print colored(self.description, color, attrs=attrs)
        print "\tvertical = %7.3f mm\t\tYU  = %7.3f"   % (self.vert,  self.yu.pv.RBV)
        print "\tlateral  = %7.3f mm\t\tYDO = %7.3f"   % (self.lat,   self.ydo.pv.RBV)
        print "\tpitch    = %7.3f mrad\t\tYDI = %7.3f" % (self.pitch, self.ydi.pv.RBV)
        print "\troll     = %7.3f mrad\t\tXU  = %7.3f" % (self.roll,  self.xu.pv.RBV)
        print "\tyaw      = %7.3f mrad\t\tXD  = %7.3f" % (self.yaw,   self.xd.pv.RBV)

    def common_text(self, amount, color='white', attrs=None):
        print "%s: moving in %s by %.3f" % \
            (colored(self.description, color, attrs=attrs), self.direction, amount)

        
    def move(self, axes, vals, rel=False):

        def message(string):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write(string)
        template = ' YU, YDO, YDI, XU, XD --> %8.4f  %8.4f  %8.4f  %8.4f  %8.4f'
        rbvs = list()
        for ax in self.five():
            rbvs.append(ax.pv.RBV)
        sys.stdout.write(template % tuple(rbvs))

        ## start moving...
        for ax, val in zip(axes, vals):
            if not ax.pv.within_limits(val):
                print colored("Request to move outside limits on %s" % ax.pv.DESC, 'red', attrs=['bold'])
                exit()
            if not ax.disconnected:
                ax.pv.move(val, relative=rel, wait=False)

        ## check to see if we have arrived, write screen update
        waiting = True
        while waiting:
            sleep(0.001)
            updt = list()
            for ax in self.five():
                updt.append(ax.pv.RBV)
            message(template % tuple(updt))
            sleep(0.1)
            waiting = not all([ax.pv.done_moving for ax in axes])

        ## kill the in vacuum motors
        for ax in axes:
            ax.kill()

        ## final update
        updt = list()
        for ax in self.five():
            updt.append(ax.pv.RBV)
        message(template % tuple(updt))
        print '\n'
        return 0

    def prettyprint_motors(self, color1="white", color2="white"):
        self.current_positions()
        which = self.direction
        if self.direction is 'vertical':
            which = self.direction + ' position'
            value = self.vert

        elif self.direction is 'lateral':
            which = self.direction + ' position'
            value = self.lat

        elif self.direction is 'pitch':
            value = self.pitch

        elif self.direction is 'roll':
            value = self.roll

        elif self.direction is 'yaw':
            value = self.yaw

        text = '\t%s = %.3f' % (colored(which, color1, attrs=['bold']), value)
        print text
            
        if self.direction in ('vertical', 'pitch', 'roll'):
            print "\tRBVs: %s = %8.4f\t%s = %8.4f\t%s = %8.4f" % \
                (colored('YU',  color1, attrs=['bold']), self.yu.pv.RBV,
                 colored('YDO', color1, attrs=['bold']), self.ydo.pv.RBV,
                 colored('YDI', color1, attrs=['bold']), self.ydi.pv.RBV)
            print "\tREPs: %s = %8d\t%s = %8d\t%s = %8d\n" % \
                (colored('YU',  color2), self.yu.pv.REP,
                 colored('YDO', color2), self.ydo.pv.REP,
                 colored('YDI', color2), self.ydi.pv.REP)

        elif self.direction in ('lateral', 'yaw'):
            print "\tRBVs: %s = %.4f\t%s = %.4f" % \
                (colored('XU', color1, attrs=['bold']), self.xu.pv.RBV,
                 colored('XD', color1, attrs=['bold']), self.xd.pv.RBV)
            print "\tREPs: %s = %d\t%s = %d\n" % \
                (colored('XU', color2), self.xu.pv.REP,
                 colored('XD', color2), self.xd.pv.REP)
        else:
            self.where()

################################################################################
################################################################################
################################################################################

KTOE = 3.8099819442818976
class StepScan():
    def __init__(self, fname=None):
        self.columns = ('I0', 'It', 'Ir')
        self.filename = fname
        self.handle = open(fname, 'w')

    def etok(self, ee):
        return numpy.sqrt(ee/KTOE)
    def ktoe(self, k):
        return k*k*KTOE

    def file_header(self, element='H', edge='K', e0=0, monodir = 'up', material='increasing',
                    comment='quick measurement', focus=True, hr=True):
        self.headers = list(['# XDI/1.0 BMMControls/0',
                             '# Column.1: energy eV',
                             '# Element.edge: K',
                             '# Element.symbol: %s' % element,
                             '# Scan.edge_energy: %.1f' % e0,
                             '# Mono.name: Si 111',
                             '# Mono.d_spacing: 3.13572865',
                             '# Mono.direction: %s energy' % monodir,
                             '# Beamline.name: 06BM',
                             '# Beamline.collimation: paraboloid mirror, 5 nm Rh on 30 nm Pt'])
        if focus:
            self.xdi.append('# Beamline.focusing: none')
        if hr:
            self.xdi.append('# Beamline.harmonic_rejection: Rh/Pt mirror')
        self.xdi.extend(['# Facility.name: NSLS-II',
                         '# Facility.energy: 3 GeV',
                         '# Facility.xray_source: NSLS-II three-pole wiggler',
                         '# Scan.start_time: %s' % strftime("%Y-%m-%dT%H:%M:%S"),
                         '# Detector.I0: 10cm  N2',
                         '# Detector.I1: 25cm  N2',
                         '# Sample.name: %s' % material,
                         '# Sample.prep: powder on kapton tape',
                         '# ///',
                         '# %s' % comment,
                         '# -------------------------------------------'])

    def column_labels(self, labels=('I0', 'It', 'Ir')):
        line = '# energy  '
        i=1
        for l in labels:
            i=i+1
            this = '# Column.%d: %s' % (i, l)
            self.xdi.insert(i, this)
            line = line + l + '  '
        self.xdi.append(line)

    def file_header_text(self):
        text = ''
        for h in self.xdi:
            text = text + h + '\n'
        return text

    ## would be nice to use "k" notation
    def conventional_grid(self, bounds, steps):
        pre   = numpy.arange(self.e0+bounds[0], self.e0+bounds[1], steps[0])
        edge  = numpy.arange(self.e0+bounds[1], self.e0+bounds[2], steps[1])
        begin = self.etok(bounds[2])
        if bounds[2] > bounds[3]: # 4th bound was a k value
            end = bounds[3]
        else:                     # 4th bound was an energy value
            end = self.etok(bounds[3])
        post  = self.e0+self.ktoe(numpy.arange(begin, end, steps[2]))
        return list(pre) + list(edge) + list(post)

        
    def xanes_grid(self, emin, emax, step):
        return numpy.arange(self.e0+emin, self.e0+emax, step)
