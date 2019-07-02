epicsEnvSet("HOSTNAME", "xf06bm-vme1")

## Stats
dbLoadRecords("db/iocAdminRTEMS.db", "IOC=XF:06BM-CT{IOC:VME1}")

## Auto save/restore
dbLoadRecords("db/save_restoreStatus.db", "P=XF:06BM-CT{IOC:VME1}")
save_restoreSet_status_prefix("XF:06BM-CT{IOC:VME1}")
