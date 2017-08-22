#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 193.83.200.104 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC01/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

#/opt/epics/extensions/bin/linux-x86_64/edm -eolc -x -m "P=XF:06BM-OP,R={Mir:M1-Ax:,A1=YU}Mtr,A2=YDO}Mtr,A3=YDI}Mtr,A4=XU}Mtr,A6=XD}Mtr,S=FMB,T={Mir:M1},MC=XF:06BM-OP{MC:01}" MirM1_MainPanel.edl

edm -eolc -x -m "P=XF:06BM-OP,R={Mir:M1-Ax:,A1=YU}Mtr,A2=YDO}Mtr,A3=YDI}Mtr,A4=XU}Mtr,A5=XD}Mtr,S=FMB,T={Mir:M1},MC=XF:06BM-OP{MC:01}" MirM1_MainPanel.edl
