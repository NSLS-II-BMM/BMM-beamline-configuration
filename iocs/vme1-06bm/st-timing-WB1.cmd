epicsEnvSet("HOSTNAME", "xf04ida-ioc-vme1")
epicsEnvSet("MRFIOC","mrfioc2")

#
# Single EVR in slot #2
#

## EVRs
mrmEvrSetupVME("EVR1",2,0x20000000,3,0x26)

dbLoadRecords("${MRFIOC}/db/evr-vmerf-230.db","SYS=XF:04IDC-ES:1, D=EVR:1, EVR=EVR1")

## EVR Pulser Alias
#dbLoadRecords("${MRFIOC}/db/evralias.db", "PN=XF:04IDC-ES:1{EVR:1-DlyGen:0},PNA=SR{Other}")

## Stats
dbLoadRecords("db/iocAdminRTEMS.db", "IOC=XF:04IDC-CT{IOC:VME1}")

## Auto save/restore
dbLoadRecords("db/save_restoreStatus.db", "P=XF:04IDC-CT{IOC:VME1}")
save_restoreSet_status_prefix("XF:04IDC-CT{IOC:VME1}")
