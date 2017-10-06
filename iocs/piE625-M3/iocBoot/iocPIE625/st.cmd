#!../../bin/linux-x86_64/PIE625

## You may have to change PIE625 to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet("ENGINEER", "Bruno Luvizotto x2971")
epicsEnvSet("LOCATION", "XF:06{RG:B1}")

#$(TOP)
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/PIE625.dbd",0,0)
PIE625_registerRecordDeviceDriver(pdbbase) 

dbLoadTemplate("db/motor.substitutions")

drvAsynIPPortConfigure("PI","10.6.130.54:4001",0,0,0)
asynOctetSetInputEos("PI",0,"\n")
asynOctetSetOutputEos("PI",0,"\n")

#asynSetTraceMask("PI",0,0x9)
#asynSetTraceIOMask("PI",0,0x9)
#asynSetTraceMask("PI",0,255)
#asynSetTraceIOMask("PI",0,255)

## Load record instances
dbLoadRecords("/usr/lib/epics/db/asynRecord.db", "P=XF\:06BM\-CT\{PIE625-M3\},R=Asyn,PORT=PI,IMAX=255,OMAX=255,ADDR=0")

# MotorNameConfig("Motor number", "Motor name")
MotorNameConfig(0, "A")

# PORT, ASYN PORT, number of axes, active poll period (ms), idle poll period (ms)
PIE625CreateController("PI1", "PI", 1, 100, 1000)

dbLoadRecords("db/iocAdminSoft.db","IOC=XF:06BM-CT{IOC:PI03}")

## autosave/restore machinery
save_restoreSet_Debug(0)
save_restoreSet_IncompleteSetsOk(1)
save_restoreSet_DatedBackupFiles(1)

set_savefile_path("${TOP}/as","/save")
set_requestfile_path("${TOP}/as","/req")

set_pass0_restoreFile("info_positions.sav")
set_pass0_restoreFile("info_settings.sav")
set_pass1_restoreFile("info_settings.sav")

iocInit()

## more autosave/restore machinery
cd ${TOP}/as/req
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5 , "")
create_monitor_set("info_settings.req", 15 , "")

cd ${TOP}/iocBoot/${IOC}

## Start any sequence programs

#dbl > "/cf-update/xf06bm-ioc1.PIE625-M3.dbl"
