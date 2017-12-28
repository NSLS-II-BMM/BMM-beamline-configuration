
import epics
from numpy import pi, sin, cos, arcsin, tan, arctan2
from time import sleep
from termcolor import colored
import signal


HBARC = 1973.27053324
kill_pv = {'pitch' : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr_KILL_CMD.PROC"),
           'roll'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr_KILL_CMD.PROC"),
           'perp'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr_KILL_CMD.PROC"),
           'para'  : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr_KILL_CMD.PROC"),
           'bragg' : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr_KILL_CMD.PROC"),
           'x'     : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr_KILL_CMD.PROC"),
           'y'     : epics.PV("XF:06BMA-OP{Mono:DCM1-Ax:Y}Mtr_KILL_CMD.PROC") }

class DCM():
    def __init__(self):
        self.twod = None
        self.description = None
        self.xtals()
        self.mono_offset = 30
        self.emin = 4000
        self.emax = 22300
        self.bragg = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr")
        self.perp  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr")
        self.para  = epics.Motor("XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr")
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
        angle = self.bragg.RBV
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
    
    def kill(self, axis="pitch"):
        if axis not in ("pitch", "roll", "para", "perp", "bragg", "x", "y"):
            return 0
        kill_pv[axis].put(1)
        return 1

    def kill_invacuum(self):
        for axis in ("pitch", "roll", "para", "perp"):
            self.kill(axis)
        
    def moveto(self, energy, para=None, perp=None):
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

        angle = dcm.angle(energy)
        pvgroup = (dcm.bragg, dcm.perp, dcm.para)
        newvals = (angle, perp, para)
        for pv, val in zip(pvgroup, newvals):
            pv.move(val, wait=False)
            
        ##------------------------------------------------------------------------
        ## wait for all three motors to get where they are going
        waiting = True
        while waiting:
            sleep(0.001)
            waiting = not all([pv.done_moving for pv in pvgroup])
            
        return self.current_energy()

    def prettyprint_energy(self, energy, status="Mono at", color="white", attrs=None):
        # print "%s = %.1f   %s = %s   (perp/para offset = %.2f/%.2f)" % \
        print "%s = %.1f   %s = %s" % \
            (colored(status,       color, attrs=attrs), energy,
             colored('reflection', color, attrs=attrs), self.description)  #  args.perpoffset, args.paraoffset)

    
    def prettyprint_motors(self, bragg, perp, para, color="white", status="current", attrs=None):
        # print "current: %s = %8.5f   %s = %7.4f (%7.4f)   %s = %8.4f (%8.4f)\n" %
        print "%s: %s = %8.5f   %s = %7.4f   %s = %8.4f" %\
            (status,
             colored('angle',color, attrs=attrs), bragg,
             colored('perp', color, attrs=attrs), perp,  #  - args.perpoffset,
             colored('para', color, attrs=attrs), para)  #  - args.paraoffset)
        
    def prettyline(self, color="white"):
        print colored('='*65, color)
   
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
        self.direction = None
    
    def set_mirror(self, m):
        if m in (1,2,3,4):
            self.m   = m
        else:
            return 0
        if m<4:
            if m is 1:
                self.length = 556
                self.width = 240
                self.description = 'M1: collimating mirror'
                self.hutch = ''
            elif m is 2:
                self.length = 1288
                self.width = 240
                self.description = 'M2: focusing mirror'
            elif m is 3:
                self.length = 667
                self.width = 240
                self.description = 'M3: harmonic rejection mirror'
            self.yu  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YU}Mtr"  % (self.hutch, self.m))
            self.ydo = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YDO}Mtr" % (self.hutch, self.m))
            self.ydi = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:YDI}Mtr" % (self.hutch, self.m))
            self.xu  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:XU}Mtr"  % (self.hutch, self.m))
            self.xd  = epics.Motor("XF:06BM%s-OP{Mir:M%d-Ax:XD}Mtr"  % (self.hutch, self.m))
            self.kill = {'xu'  : epics.PV("XF:06BM%s-OP{Mir:M%d-Ax:XU}Mtr_KILL_CMD.PROC" % (self.hutch, self.m)),
                         'xd'  : epics.PV("XF:06BM%s-OP{Mir:M%d-Ax:XD}Mtr_KILL_CMD.PROC" % (self.hutch, self.m))}

        else:
            self.yu  = epics.Motor("XF:06BMA-BI{XAFS-Ax:Tbl_YU}Mtr")
            self.ydo = epics.Motor("XF:06BMA-BI{XAFS-Ax:Tbl_YDO}Mtr")
            self.ydi = epics.Motor("XF:06BMA-BI{XAFS-Ax:Tbl_YDI}Mtr")
            self.xu  = epics.Motor("XF:06BMA-BI{XAFS-Ax:Tbl_XU}Mtr")
            self.xd  = epics.Motor("XF:06BMA-BI{XAFS-Ax:Tbl_XD}Mtr")
            self.length = 1160
            self.width = 558
            self.description = 'XAFS table'
            self.hutch = ''
            self.kill = {'xu'  : epics.PV("XF:06BMA-BI{XAFS-Ax:Tbl_XU}Cmd:Kill-Cmd"),
                         'xd'  : epics.PV("XF:06BMA-BI{XAFS-Ax:Tbl_XD}Cmd:Kill-Cmd")}


    def handler(self, signum, frame):
        print colored('\n\nGot CTRL+C, stopping all motors, killing in-vacuum motors', 'red', attrs=['bold'])
        for pv in (self.yu, self.ydo, self.ydi, self.xu, self.xd):
            pv.put('STOP', 1)
        for ax in ('xu', 'xd'):
            self.kill[ax].put('1')
        print ""
        self.where()
        exit(0)

            
    def current_positions(self):
        self.vert  = (self.yu.RBV  + (self.ydo.RBV+self.ydi.RBV)/2) / 2
        self.lat   = (self.xu.RBV  + self.xd.RBV)  / 2
        dbar       = (self.ydo.RBV + self.ydi.RBV) / 2
        self.pitch = 1000*arctan2( (dbar-self.yu.RBV),        self.length )
        self.roll  = 1000*arctan2( self.ydo.RBV-self.ydi.RBV, self.width )
        self.yaw   = 1000*arctan2( self.xd.RBV-self.xu.RBV,   self.length )

    def where(self, color='white', attrs=None):
        self.current_positions()
        print colored(self.description, color, attrs=attrs)
        print "\tvertical = %7.3f mm\t\tYU  = %7.3f"   % (self.vert,  self.yu.RBV)
        print "\tlateral  = %7.3f mm\t\tYDO = %7.3f"   % (self.lat,   self.ydo.RBV)
        print "\tpitch    = %7.3f mrad\t\tYDI = %7.3f" % (self.pitch, self.ydi.RBV)
        print "\troll     = %7.3f mrad\t\tXU  = %7.3f" % (self.roll,  self.xu.RBV)
        print "\tyaw      = %7.3f mrad\t\tXD  = %7.3f" % (self.yaw,   self.xd.RBV)

    def common_text(self, amount, color='white', attrs=None):
        print "%s: moving in %s by %.3f" % \
            (colored(self.description, color, attrs=attrs), self.direction, amount)

        
    def move(self, pvs, vals, rel=False):
        for pv, val in zip(pvs, vals):
            if not pv.within_limits(val):
                print colored("Request to move outside limits on %s" % pv.DESC, 'red', attrs=['bold'])
                exit()
            pv.move(val, relative=rel, wait=False)
        waiting = True
        while waiting:
            sleep(0.001)
            waiting = not all([pv.done_moving for pv in pvs])
        self.kill['xu'].put('1')
        self.kill['xd'].put('1')
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
                (colored('YU',  color1, attrs=['bold']), self.yu.RBV,
                 colored('YDO', color1, attrs=['bold']), self.ydo.RBV,
                 colored('YDI', color1, attrs=['bold']), self.ydi.RBV)
            print "\tREPs: %s = %8d\t%s = %8d\t%s = %8d\n" % \
                (colored('YU',  color2), self.yu.REP,
                 colored('YDO', color2), self.ydo.REP,
                 colored('YDI', color2), self.ydi.REP)

        elif self.direction in ('lateral', 'yaw'):
            print "\tRBVs: %s = %.4f\t%s = %.4f" % \
                (colored('XU', color1, attrs=['bold']), self.xu.RBV,
                 colored('XD', color1, attrs=['bold']), self.xd.RBV)
            print "\tREPs: %s = %d\t%s = %d\n" % \
                (colored('XU', color2), self.xu.REP,
                 colored('XD', color2), self.xd.REP)
