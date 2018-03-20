
import os
import sys
import signal
from time import sleep, strftime
import epics
import numpy
from numpy import pi, sin, cos, arcsin, tan, arctan2, exp
from termcolor import colored
import json

HBARC = 1973.27053324

GITREPO = '/home/bravel/git/BMM-beamline-configuration/'
MOTORDATA = json.load(open(os.path.join(GITREPO, 'Modes.json')))

KTOE = 3.8099819442818976
def etok(ee):
    return numpy.sqrt(ee/KTOE)
def ktoe(k):
    return k*k*KTOE

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
        self.target       = 0
        if alias is not None:
            self.motor(alias)

    def motor(self, alias):
        self.pvname = MOTORDATA[alias]['PV']
        self.pv = epics.Motor(MOTORDATA[alias]['PV'])
        self.description = MOTORDATA[alias]['desc']
        self.alias = alias
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
        if 'lateral' in alias:
            self.invacuum = 1
            
    def stop(self):
        if self.pv.get('MOVN'):
            self.pv.put('STOP', 1, wait=True)
        if self.invacuum:
            self.kill_pv.put(1)

    def enable(self):
        self.enable_pv.put(1)
        
    def kill(self, really=False):
        if self.kill_pv is not None:
            if self.invacuum:
                self.kill_pv.put(1)
            elif really:
                self.kill_pv.put(1)


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

class IonChambers():
    def __init__(self):
        self.i0 = epics.PV("XF:06BM-BI{EM:1}EM180:Current1:MeanValue_RBV")
        self.it = epics.PV("XF:06BM-BI{EM:1}EM180:Current2:MeanValue_RBV")
        self.ir = epics.PV("XF:06BM-BI{EM:1}EM180:Current3:MeanValue_RBV")
        self.avgtime = epics.PV("XF:06BM-BI{EM:1}EM180:AveragingTime")
        self.default_avgtime = 0.5
        self.multiplier = 1e9
        
    def each(self):
        return (self.i0, self.it, self.ir)

    def measure(self):
        return [self.multiplier*self.i0.get(), self.multiplier*self.it.get(), self.multiplier*self.ir.get()]

    def set_avgtime(self, time):
        self.avgtime.put(time)
    
    def reset_avgtime(self):
        self.avgtime.put(self.default_avgtime)
    
class Vortex():
    def __init__(self):
        self.roi1 = epics.PV("XF:06BM-ES:1{Sclr:1}.S2")
        self.roi2 = epics.PV("XF:06BM-ES:1{Sclr:1}.S4")
        self.roi3 = epics.PV("XF:06BM-ES:1{Sclr:1}.S6")
        self.roi4 = epics.PV("XF:06BM-ES:1{Sclr:1}.S8")
        self.icr1 = epics.PV("XF:06BM-ES:1{Sclr:1}.S10")
        self.icr2 = epics.PV("XF:06BM-ES:1{Sclr:1}.S12")
        self.icr3 = epics.PV("XF:06BM-ES:1{Sclr:1}.S14")
        self.icr4 = epics.PV("XF:06BM-ES:1{Sclr:1}.S16")
        self.ocr1 = epics.PV("XF:06BM-ES:1{Sclr:1}.S18")
        self.ocr2 = epics.PV("XF:06BM-ES:1{Sclr:1}.S20")
        self.ocr3 = epics.PV("XF:06BM-ES:1{Sclr:1}.S22")
        self.ocr4 = epics.PV("XF:06BM-ES:1{Sclr:1}.S24")
        self.avgtime = epics.PV("XF:06BM-ES:1{Sclr:1}.TP1")
        self.default_avgtime = 0.5
        self.multiplier = 1
        self.maxcount = 20
        self.iterations = 0

    def rois(self):
        return (self.roi1, self.roi2, self.roi3, self.roi4)
    def icrs(self):
        return (self.icr1, self.icr2, self.icr3, self.icr4)
    def ocrs(self):
        return (self.ocr1, self.ocr2, self.ocr3, self.ocr4)

    def get(self, scalar):
        return getattr(self, scalar).get()
    
    def ch1(self):
        r = self.roi1.get()
        i = self.icr1.get()
        o = self.ocr1.get()
        c = self.dtcorrect(r, i, o)
        return [r, i, o, c]
    def ch2(self):
        r = self.roi2.get()
        i = self.icr2.get()
        o = self.ocr2.get()
        c = self.dtcorrect(r, i, o)
        return [r, i, o, c]
    def ch3(self):
        r = self.roi3.get()
        i = self.icr3.get()
        o = self.ocr3.get()
        c = self.dtcorrect(r, i, o)
        return [r, i, o, c]
    def ch4(self):
        r = self.roi4.get()
        i = self.icr4.get()
        o = self.ocr4.get()
        c = self.dtcorrect(r, i, o)
        return [r, i, o, c]
    
    def set_avgtime(self, time):
        self.avgtime.put(time)
    
    def reset_avgtime(self):
        self.avgtime.put(self.default_avgtime)

    ## see https://doi:org/10.1107/S0909049510009064
    ## or X23A2MED plugin for Athena
    ##
    ## roi,icr,ocr: measured counts, time: integartion time at this point, dt: time constant of fast channel
    def dtcorrect(self, roi, icr, ocr, time=1, dt=280):
        rr = float(roi)
        ii = float(icr)
        oo = float(ocr)
        tt = float(time)
        dt = float(dt*1e-9)
        if dt<1e-9:                # deal with an unreasonable value for fast time constant
            return rr*ii/oo
        totn  = 0.0
        test  = 1.0
        count = 0.0
        toto  = ii/tt
        if icr <= 1:
            totn = oo
            test = 0
        while test > dt:
            totn  = (ii/tt) * exp(toto*dt)
            test  = (totn-toto) / toto
            toto  = totn
            count = count + 1
            if (count >= self.maxcount):
                test = 0
        self.iterations = count
        return rr * (totn*tt/oo)
    
################################################################################
################################################################################
################################################################################

class DCM():
    def __init__(self, crystals='111'):
        self.twod          = None
        self.description   = None
        self.xtals(crystals)
        self.mono_offset   = 30   # mm
        self.emin          = 4000        # eV
        self.emax          = 22300       # eV
        self.bragg         = BMM_Motor('dcm_bragg')
        self.perp          = BMM_Motor('dcm_perp')
        self.para          = BMM_Motor('dcm_para')
        self.pitch         = BMM_Motor('dcm_pitch')
        self.roll          = BMM_Motor('dcm_roll')
        self.x             = BMM_Motor('dcm_x')
        self.y             = BMM_Motor('dcm_y')
        self.perp.invacuum = self.para.invacuum = self.pitch.invacuum = self.roll.invacuum = True
        self.paraoffset    = 0
        self.perpoffset    = 0
        self.channelcut    = False
        
    def xtals(self, crystals='111'):
        if crystals is '311':
            self.twod = 2*1.63761489
            self.description = 'Si(311)'
        else:
            ## smaller beam
            #self.twod = 2*3.13543952
            ## larger beam 23 Jan 2018
            self.twod = 2*3.13597211
            self.description = 'Si(111)'

    def is311(self):
        if self.x.pv.RBV > 0:
            return True
        else:
            return False
            
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
        self.perp.kill()
        self.para.kill()
        self.pitch.kill()
        self.roll.kill()

    def seven(self):
        return(self.bragg, self.perp, self.para, self.pitch, self.roll, self.x, self.y)
        
    def handler(self, signum, frame):
        print colored('\n\nGot CTRL+C, stopping all motors, disabling in-vacuum motors', 'red', attrs=['bold'])
        for ax in self.seven():
            ax.stop()
        print ""
        self.prettyprint_three_motors(self.bragg, self.perp, self.para, color="red", status="current")
        #self.kill_invacuum()
        #sleep(0.5)
        self.roll.kill()
        action = raw_input("any key to quit > ")
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

        angle    = self.angle(energy)
        if self.channelcut:
            axes     = (self.bragg,)
            template = ' bragg --> %8.4f'
            newvals  = (angle,)
        else:
            axes     = (self.bragg, self.perp, self.para)
            template = ' bragg, perp, para --> %8.4f  %8.4f  %8.4f'
            newvals  = (angle, perp, para)
        self.generic_move(axes, newvals, template, quiet)
        self.kill_invacuum()
        return self.current_energy()

    def change_xtals(self, values=None):
        if values is None:
            return 0
        axes     = (self.pitch, self.roll, self.x)
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

    def channelcut_energy(self, e0, bounds):
        for i,s in enumerate(bounds):
            if type(s) is str:
                this = float(s[:-1])
                bounds[i] = ktoe(this)
        amin = self.angle(e0+bounds[0])
        amax = self.angle(e0+bounds[-1])
        aave = (amin + amax) / 2
        wavelength = self.wavelength(aave)
        eave = self.e2l(wavelength)
        return eave
    
    def prettyprint_energy(self, energy, status="Mono at", color="white", attrs=None):
        # print "%s = %.1f   %s = %s   (perp/para offset = %.2f/%.2f)" % \
        print "%s = %.1f   %s = %s" % \
            (colored(status,       color, attrs=attrs), energy,
             colored('reflection', color, attrs=attrs), self.description)  #  args.perpoffset, args.paraoffset)

    
    def prettyprint_three_motors(self, mot1, mot2, mot3, color="white", status="current", attrs=None):
        # print "current: %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)\n" %
        print "%s: %s = %8.5f   %s = %7.4f   %s = %8.4f" %\
            (status,
             colored(mot1.pv.DESC, color, attrs=attrs), mot1.pv.RBV,
             colored(mot2.pv.DESC, color, attrs=attrs), mot2.pv.RBV,  #  - args.perpoffset,
             colored(mot3.pv.DESC, color, attrs=attrs), mot3.pv.RBV)  #  - args.paraoffset)

    def prettyprint_target_energy(self, bragg, perp, para, color="white", status='target ', attrs=None):
        print "%s: %s = %8.5f   %s = %7.4f   %s = %8.4f" %\
            (status,
             colored(self.bragg.pv.DESC,color, attrs=attrs), bragg,
             colored(self.perp.pv.DESC, color, attrs=attrs), perp,  #  - args.perpoffset,
             colored(self.para.pv.DESC, color, attrs=attrs), para)  #  - args.paraoffset)
        
    def prettyline(self, color="white"):
        print colored('='*80, color)


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
            self.yu  = BMM_Motor('m%d_yu' % m)
            self.ydo = BMM_Motor('m%d_ydo' % m)
            self.ydi = BMM_Motor('m%d_ydi' % m)
            self.xu  = BMM_Motor('m%d_xu' % m)
            self.xd  = BMM_Motor('m%d_xd' % m)
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
            self.yu  = BMM_Motor("xafs_yu")
            self.ydo = BMM_Motor("xafs_ydo")
            self.ydi = BMM_Motor("xafs_ydi")
            self.xu  = BMM_Motor("xafs_xu")
            self.xd  = BMM_Motor("xafs_xd")
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
                print colored("\nRequest to move outside limits on %s" % ax.pv.DESC, 'red', attrs=['bold'])
                print colored("Requested %.3f   Current %.3f" % (val, ax.pv.RBV), 'red', attrs=['bold'])
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

class StepScan():
    def __init__(self, fname=None, xtals='111', element=None, e0=None, edge='K',
                 material=None, monodir='increasing'):
        self.columns    = ('I0', 'It', 'Ir')
        self.filename   = fname
        self.handle     = open(fname, 'w')
        self.xtals      = xtals
        self.element    = element
        self.e0         = e0
        self.edge       = edge
        self.material   = material
        self.direction  = monodir
        self.prep       = ''
        self.comment    = ''
        self.grid       = None
        self.focus      = True
        self.hr         = True
        self.channelcut = False


    def file_header(self, dcm=None, material='', comment='quick measurement'):
        if dcm is None:
            dcm = DCM(crystals=self.xtals)
        self.xdi = list(['# XDI/1.0 BMMControls/0',
                         #'# Column.1: energy eV',
                         '# Element.edge: %s' % self.edge,
                         '# Element.symbol: %s' % self.element,
                         '# Scan.edge_energy: %.1f' % self.e0,
                         '# Mono.name: %s' % dcm.description,
                         '# Mono.d_spacing: %.7f' % (dcm.twod/2),
                         '# Mono.direction: %s in energy' % self.direction,
                         '# Mono.scan_type: step',
                         '# Beamline.name: 06BM',
                         '# Beamline.collimation: paraboloid mirror, 5 nm Rh on 30 nm Pt'])
        
        if self.focus:
            self.xdi.append('# Beamline.focusing: torroidal mirror with bender, 5 nm Rh on 30 nm Pt')
        else:
            self.xdi.append('# Beamline.focusing: none')
            
        if self.hr:
            self.xdi.append('# Beamline.harmonic_rejection: Pt stripe; Si stripe below 8 keV')
        else:
            self.xdi.append('# Beamline.harmonic_rejection: none')
            
        if self.channelcut:
            self.xdi.append('# Mono.scan_mode: pseudo channel cut')
        else:
            self.xdi.append('# Mono.scan_mode: fixed exit')
            
        self.xdi.extend(['# Facility.name: NSLS-II',
                         '# Facility.energy: 3 GeV',
                         '# Facility.xray_source: NSLS-II three-pole wiggler',
                         '# Scan.start_time: %s' % strftime("%Y-%m-%dT%H:%M:%S"),
                         '# Detector.I0: 10cm  N2',
                         '# Detector.I1: 25cm  N2',
                         '# Sample.name: %s' % self.material,
                         '# Sample.prep: %s' % self.prep,
                         '# ///',
                         '# %s' % self.comment,
                         '# -------------------------------------------'])

    def units(self, label):
        if label is 'energy':
            return 'eV'
        elif label in ('i0', 'it', 'ir'):
            return 'nA'
        elif label[:-1] in ('roi', 'icr', 'ocr'):
            return 'counts'
        elif label[:-1] in ('corr'):
            return 'dead-time corrected count rate'
        elif label is 'encoder':
            return 'counts'
        else:
            return ''

        
    def column_labels(self, labels=('I0', 'It', 'Ir')):
        line = '# '
        i=0
        for l in labels:
            i=i+1
            this = '# Column.%d: %s %s' % (i, l, self.units(l))
            self.xdi.insert(i, this)
            line = line + l + '  '
        self.xdi.append(line)

    def file_header_text(self):
        text = ''
        for h in self.xdi:
            text = text + h + '\n'
        return text

    def conventional_grid(self, bounds, steps):
        if (len(bounds) - len(steps)) != 1:
            return None
        for i,s in enumerate(bounds):
            if type(s) is str:
                this = float(s[:-1])
                bounds[i] = ktoe(this)
        grid = list()
        for i,s in enumerate(steps):
            if type(s) is str:
                step = float(s[:-1])
                ar = self.e0+ktoe(numpy.arange(etok(bounds[i]), etok(bounds[i+1]), step))
            else:
                ar = numpy.arange(self.e0+bounds[i], self.e0+bounds[i+1], steps[i])
            grid = grid + list(ar)
        return grid
