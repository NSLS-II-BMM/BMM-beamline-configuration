#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="Yes"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
# 10.7.2.81 - MC:01
# 10.7.2.82 - MC:02
# 10.7.2.83 - MC:03
# 10.7.2.84 - MC:04
# 10.7.2.85 - MC:05
# 10.7.2.86 - MC:06
# 10.7.2.87 - MC:07
# 10.7.2.88 - MC:08
# 10.7.2.89 - MC:09
# 10.7.2.90 - MC:10
# 10.7.2.91 - MC:11
# 10.7.2.92 - MC:12
# 10.7.2.93 - MC:13
# 10.7.2.94 - MC:14
# 10.7.2.95 - MC:15
# 10.7.2.96 - MC:16
# 10.7.2.97 - MC:17
# 10.7.2.98 - MC:18

export EDMDATAFILES=/opt/epics/apps/MC03/opi_MC
#export EDMDATAFILES=/opt/epics/opi
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "P=XF:07IDA-OP,R={Slt:02-Ax:,A5=O}Mtr,A6=I}Mtr,A7=T}Mtr,A8=B}Mtr,S=FMB,T={Slt:02},MC=XF:07ID-OP{MC:03}" Slt02_MainPanel.edl
