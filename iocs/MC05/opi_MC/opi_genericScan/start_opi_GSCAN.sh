#!/bin/bash
export EPICS_CA_AUTO_ADDR_LIST="YES"
export EPICS_CA_ADDR_LIST="127.0.0.1 localhost"
# 192.168.0.1 - reserved
# 192.168.0.2 - M1
# 192.168.0.3 - M3
export EDMDATAFILES=/opt/epics/apps/GSCAN/opi_genericScan/
export EPICS_CA_MAX_ARRAY_BYTES=240000

edm -eolc -x -m "DEVICE=FMBGSCAN,P=FMB,R=GSCAN:,S=FMB" generic_scan_local.edl
