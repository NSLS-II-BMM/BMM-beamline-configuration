#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC05/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BMA-BI,R={Fltr:01-Ax:,A6=Y1}Mtr,A7=Y2}Mtr,S=FMB,T={Fltr:01},MC=XF:06BM-OP{MC:05}" DM1_MainPanel.edl
