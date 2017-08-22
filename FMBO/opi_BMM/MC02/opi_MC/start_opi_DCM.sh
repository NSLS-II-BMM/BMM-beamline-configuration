#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC02/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BMA-OP,R={Mono:DCM1-Ax:,A1=Bragg}Mtr,A2=Bragg2}Mtr,A3=P2}Mtr,A4=R2}Mtr,A5=Per2}Mtr,A6=Par2}Mtr,A7=X}Mtr,A8=Y}Mtr,S=FMB,T={Mono:DCM1},MC=XF:06BM-OP{MC:02}" DCM_MainPanel.edl

