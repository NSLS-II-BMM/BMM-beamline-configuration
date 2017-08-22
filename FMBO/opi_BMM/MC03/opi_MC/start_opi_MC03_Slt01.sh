#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC03/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BMA-OP,R={Slt:01-Ax:,A1=O}Mtr,A2=I}Mtr,A3=T}Mtr,A4=B}Mtr,S=FMB,T={Slt:01},MC=XF:06BM-OP{MC:03}" Slt01_MainPanel.edl
