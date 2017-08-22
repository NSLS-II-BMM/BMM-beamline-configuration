#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC04/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BMA-BI,R={Diag:02-Ax:,A7=Y}Mtr,S=FMB,T={FS:02},MC=XF:06BMA-BI{MC:04}" MISC_MainPanel.edl
