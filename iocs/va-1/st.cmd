#!/usr/lib/epics/bin/linux-x86_64/vactrl

## You may have to change blvac to something else
## everywhere it appears in this file
epicsEnvSet("EPICS_BASE", "/usr/lib/epics")
epicsEnvSet("TOP","${PWD}") 

epicsEnvSet("ENGINEER", "Huijuan Xu x4394")
epicsEnvSet("LOCATION", "06BM RG:B1")
epicsEnvSet("STREAM_PROTOCOL_PATH", "/usr/share/epics-vactrl-dev/protocol")
epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.6.131.255")

## Register all support components
dbLoadDatabase("$(EPICS_BASE)/dbd/vactrl.dbd",0,0)
vactrl_registerRecordDeviceDriver(pdbbase) 

############ Asyn Communication Config ############
# cfg comms for gauge controllers
drvAsynIPPortConfigure("tsrvB1-P1","10.6.130.56:4001")
drvAsynIPPortConfigure("tsrvB1-P2","10.6.130.56:4002")
drvAsynIPPortConfigure("tsrvB1-P3","10.6.130.56:4003")
drvAsynIPPortConfigure("tsrvB1-P4","10.6.130.56:4004")

# cfg comms for pump controllers
drvAsynIPPortConfigure("tsrvB1-P9","10.6.130.56:4009")
drvAsynIPPortConfigure("tsrvB1-P10","10.6.130.56:4010")
drvAsynIPPortConfigure("tsrvB1-P11","10.6.130.56:4011")
drvAsynIPPortConfigure("tsrvB1-P12","10.6.130.56:4012")

############ Load record instances ################
### gauge controller
dbLoadTemplate("vgc.substitutions")

### pump controller
dbLoadTemplate("ipc.substitutions")

### Load asynTemplate for general comms to each PORT
dbLoadTemplate("asyn.substitutions")

### devIocStats
dbLoadRecords("$(EPICS_BASE)/db/iocAdminSoft.db", "IOC=XF:06BM-CT{IOC:VA}")
dbLoadRecords("$(EPICS_BASE)/db/save_restoreStatus.db", "P=XF:06BM-CT{IOC:VA}")
###################################################

## autosave/restore machinery
save_restoreSet_Debug(0)
save_restoreSet_IncompleteSetsOk(1)
save_restoreSet_DatedBackupFiles(1)
save_restoreSet_status_prefix("XF:06BMA-VA{Dev}")


set_savefile_path("${TOP}/as","/save")
set_requestfile_path("${TOP}/as","/req")
system("install -m 777 -d ${TOP}/as/save")
system("install -m 777 -d ${TOP}/as/req")

set_pass0_restoreFile("info_positions.sav")
set_pass0_restoreFile("info_settings.sav")
set_pass1_restoreFile("info_settings.sav")

iocInit()

## more autosave/restore machinery
cd ${TOP}/as/req
makeAutosaveFiles()
create_monitor_set("info_positions.req", 15 , "")
create_monitor_set("info_settings.req", 15 , "")

# Dump database contents to Channelfinder
cd ${TOP}
dbl > ./records.dbl
system "cp ./records.dbl /cf-update/$HOSTNAME.$IOCNAME.dbl"

caPutLogInit("xf06bm-ca1:7004", 1)
