#!../../bin/linux-x86_64/plc1

< envPaths

cd ${TOP}

## Generic EnvSet
epicsEnvSet("ENGINEER", "Garrett Bischof x5841")
epicsEnvSet("LOCATION", "06BM RG:B")

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.6.128.255")

#epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
#epicsEnvSet("EPICS_CAS_INTF_ADDR_LIST", "10.2.0.1")
#epicsEnvSet("EPICS_CAS_IGNORE_ADDR_LIST", "10.2.0.1 10.2.1.1 10.2.2.5 127.0.0.1")

## Register all support components
dbLoadDatabase "dbd/plc1.dbd"
plc1_registerRecordDeviceDriver pdbbase

## Load PLC driver
EIP_buffer_limit(492)
drvEtherIP_init()
drvEtherIP_define_PLC("XF06BM_BMM_EPS","10.6.130.41",0)
EIP_verbosity(6)

## Load record instances
dbLoadRecords("db/plc1-va.db", "PLC=XF06BM_BMM_EPS")
dbLoadRecords("db/plc1-tc.db", "PLC=XF06BM_BMM_EPS")
dbLoadRecords("db/plc1-wtr.db", "PLC=XF06BM_BMM_EPS")
dbLoadRecords("db/plc1-pps.db", "PLC=XF06BM_BMM_EPS")
dbLoadRecords("db/plc1-smoke.db", "PLC=XF06BM_BMM_EPS")
dbLoadRecords("db/plc1-misc.db", "PLC=XF06BM_BMM_EPS")

dbLoadRecords("$(EPICS_BASE)/db/iocAdminSoft.db", "IOC=XF:06BM-CT{IOC:EPS}")

# Auto save/restore
dbLoadRecords("$(EPICS_BASE)/db/save_restoreStatus.db", "P=XF:06BM-CT{IOC:EPS}")

save_restoreSet_status_prefix("XF:06BM-CT{IOC:EPS}")

#asSetFilename("/cf-update/acf/default.acf")
# Restricted access for SP change 
asSetFilename("$(TOP)/bl-eps.acf")

system("install -d ${TOP}/as")
system("install -m 777 -d ${TOP}/as/save")
system("install -m 777 -d ${TOP}/as/req")

set_savefile_path("${TOP}/as","/save")
set_requestfile_path("${TOP}/as","/req")

set_pass0_restoreFile("ioc_settings.sav")
set_pass0_restoreFile("ioc_values.sav")
set_pass1_restoreFile("ioc_values.sav")

cd ${TOP}/iocBoot/${IOC}
iocInit

# Do caPutlogStuff

#caPutLogInit("xf06bm-ca:7004", 0)

# Write PVlist for channelfinder

dbl > ${TOP}/records.dbl
system("cp ${TOP}/records.dbl /cf-update/xf06bm-ioc1.plc1.dbl")

makeAutosaveFileFromDbInfo("${TOP}/as/req/ioc_settings.req", "autosaveFields_pass1")
makeAutosaveFileFromDbInfo("${TOP}/as/req/ioc_values.req", "autosaveFields")

create_monitor_set("ioc_settings.req", 5, "")
create_monitor_set("ioc_values.req", 5, "")

