#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"

#export EPICS_EXTENSIONS=/opt/epics/extensions
#export PATH=$PATH:/opt/epics/extensions/bin/linux-x86_64
#export PATH=$PATH:/opt/epics/extensions/src/edm/edmMain/O.linux-x86_64
#export EDMFILES=/opt/epics/extensions/src/edm/setup
#export EDMOBJECTS=/opt/epics/extensions/src/edm/setup
#export EDMPVOBJECTS=/opt/epics/extensions/src/edm/setup
#export EDMHELPFILES=/opt/epics/extensions/src/edm/helpFiles

export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC06/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

#xset fp+ /usr/share/X11/fonts/75dpi
#xset fp+ /usr/share/X11/fonts/100dpi
#xset fp+ /usr/share/X11/fonts/100dpi:unscaled
#xset fp+ /usr/share/X11/fonts/misc:unscaled
#xset fp+ /usr/share/X11/fonts/misc 

edm -eolc -x -m "P=XF:06BM-BI,R={BCT-Ax:,A3=Y}Mtr,S=FMB,T={BCT},MC=XF:06BM-OP{MC:06}" DM3_MainPanel.edl

##edm -eolc -x -m "P=XF:06BM-BI,R={FS:03-Ax:,A3=Y}Mtr,S=FMB,T={FS:03},MC=XF:06BM-OP{MC:06}" DM3_MainPanel.edl
