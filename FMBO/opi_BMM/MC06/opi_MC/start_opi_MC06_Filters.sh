#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC06/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BM-BI,R={Fltr:01-Ax:,A4=Y}Mtr,A7=Y2}Mtr,S=FMB,T={Fltr:01},MC=XF:06BMA-OP{MC:06}" IM_MainPanel.edl
