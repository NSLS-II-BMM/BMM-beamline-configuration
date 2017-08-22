#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC06/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BM-BI,R={Slt:02-Ax:,A5=O}Mtr,A6=I}Mtr,A7=T}Mtr,A8=B}Mtr,S=FMB,T={Slt:02},MC=XF:06BM-OP{MC:06}" Slt02_MainPanel.edl
