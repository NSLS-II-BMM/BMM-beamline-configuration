#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
# 10.6.2.81 - MC:01
# 10.6.2.82 - MC:02
# 10.6.2.83 - MC:03
# 10.6.2.84 - MC:04
# 10.6.2.85 - MC:05
# 10.6.2.86 - MC:06

export EPICS_EXTENSIONS=/opt/epics/extensions
export PATH=$PATH:/opt/epics/extensions/bin/linux-x86_64
export PATH=$PATH:/opt/epics/extensions/src/edm/edmMain/O.linux-x86_64
export EDMFILES=/opt/epics/extensions/src/edm/setup
export EDMOBJECTS=/opt/epics/extensions/src/edm/setup
export EDMPVOBJECTS=/opt/epics/extensions/src/edm/setup
export EDMHELPFILES=/opt/epics/extensions/src/edm/helpFiles

export EDMDATAFILES=/opt/epics/apps/MC02/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

xset fp+ /usr/share/X11/fonts/75dpi
xset fp+ /usr/share/X11/fonts/100dpi
#xset fp+ /usr/share/X11/fonts/100dpi:unscaled
#xset fp+ /usr/share/X11/fonts/misc:unscaled
xset fp+ /usr/share/X11/fonts/misc 

#/opt/epics/extensions/bin/linux-x86_64/edm -eolc -x -m "P=XF:06BM-OP,R={Mir:M1-Ax:,A1=YU}Mtr,A2=YDO}Mtr,A3=YDI}Mtr,A4=XU}Mtr,A6=XD}Mtr,S=FMB,T={Mir:M1},MC=XF:06BM-OP{MC:01}" MirM1_MainPanel.edl

#edm -eolc -x -m "P=XF:06BM-OP,R={Mir:M1-Ax:,A1=YU}Mtr,A2=YDO}Mtr,A3=YDI}Mtr,A4=XU}Mtr,A6=XD}Mtr,S=FMB,T={Mir:M1},MC=XF:06BM-OP{MC:01}" MirM1_MainPanel.edl
edm -eolc -x -m "P=XF:06BMA-OP,R={Mono:DCM1-Ax:,A1=Bragg}Mtr,A2=Bragg2}Mtr,A3=R1}Mtr,A4=P2}Mtr,A5=R2}Mtr,A6=Per2}Mtr,A7=Par2}Mtr,A8=X}Mtr,S=FMB,T={Mono:DCM1},MC=XF:06BM-OP{MC:02}" DCM_MainPanel.edl

