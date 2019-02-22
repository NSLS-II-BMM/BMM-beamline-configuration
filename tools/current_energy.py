#!/usr/bin/env python
import sys
import epics
from numpy import pi, sin, deg2rad
HBARC = 1973.27053324

exec(open('/home/xf06bm/.ipython/profile_collection/startup/19-dcm-parameters.py').read())
#execfile()
bragg        = epics.PV('XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr.RBV')
dcmx         = epics.PV('XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr.RBV')

if dcmx.get() < 0:
    current_energy = (2*pi*HBARC) / (2*BMM_dcm.dspacing_111*sin(deg2rad(bragg.get())))
else:
    current_energy = (2*pi*HBARC) / (2*BMM_dcm.dspacing_311*sin(deg2rad(bragg.get())))

print("%.1f"%current_energy)
