#!/usr/bin/env python
import epics

import matplotlib         as mpl
mpl.use('Qt4Agg')
import matplotlib.pyplot  as plt
import numpy              as np
import matplotlib.pyplot  as plt
import matplotlib.image   as mpimg
import matplotlib.patches as patches

from numpy import pi, sin
from scipy import ndimage
from scipy import signal

hbarc=1973.27053324
def e2l(val):
    return 2*pi*hbarc/val

plt.ion()
pvname = 'XF:06BM-BI{Scr:3}image1:ArrayData'
img_pv  = epics.PV(pvname)

array = img_pv.get()

img = np.reshape(array, (960, 1280)).astype('float')
#img = img[:340,:]
#img[img < 1000] = 0
img[img < 2000] = 0

t = 280
b = t+520
i = 680
o = i+190
cropped = img[t:b,i:o]

# Create figure and axes
fig,ax = plt.subplots(1)

gblur = ((1/256., 4/256., 6/256., 4/256.,1/256.),
         (4/256.,16/256.,24/256.,16/256.,4/256.),
         (6/256.,24/256.,36/256.,24/256.,6/256.),
         (4/256.,16/256.,24/256.,16/256.,4/256.),         
         (1/256., 4/256., 6/256., 4/256.,1/256.))
conv = signal.convolve2d(cropped, gblur)
#conv[conv>1.5] = 1
# edged = ((-1,-1,-1),(-1,8,-1),(-01,-1,-1))
# conv = signal.convolve2d(cropped, kernel)
# conv[conv>0] = 100

from BMMcontrols import DCM
dcm = DCM()
com = ndimage.measurements.center_of_mass(conv)
print "%7.1f  %5.1f  %5.1f  %5.1f  %5.1f" % (dcm.current_energy(), com[0]+t, com[1]+i, com[0], com[1])

with open("com.dat", "a") as myfile:
    myfile.write("%7.1f  %5.1f  %5.1f  %5.1f  %5.1f\n" %
                 (dcm.current_energy(), com[0]+t, com[1]+i, com[0], com[1]))

ax.imshow(conv, cmap='hot')
ax.plot(com[1], com[0], 'yo')
plt.show()
name = raw_input("Hit enter to close") 
plt.close()
