#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC04/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BMA-OP,R={Mir:M2-Ax:,A1=YU}Mtr,A2=YDO}Mtr,A3=YDI}Mtr,A4=XU}Mtr,A5=XD}Mtr,A6=Bend}Mtr,S=FMB,T={Mir:M2},MC=XF:06BM-OP{MC:04}" MirM2_MainPanel.edl