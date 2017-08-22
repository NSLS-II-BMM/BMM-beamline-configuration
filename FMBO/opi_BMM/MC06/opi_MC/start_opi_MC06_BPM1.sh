#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
#export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
export EPICS_CA_ADDR_LIST="193.82.200.104"
export EDMDATAFILES=/opt/epics/opi/opi_BMM/MC06/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:06BM-BI,R={BPM:1-Ax:,A2=Y}Mtr,S=FMB,T={BPM:1},MC=XF:06BM-OP{MC:06}" BPM1_MainPanel.edl

# Sample Naming - XF:07ID6-OP{Mir:L4-Ax:P}Mtr, XF:07ID6-BI{BPM:1-Ax:Y}Mtr
# EOF

