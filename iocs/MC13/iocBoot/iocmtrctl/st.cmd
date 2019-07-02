#!../../bin/linux-x86_64/tpmac

< envPaths

epicsEnvSet("ENGINEER",  "ZY @5525")
epicsEnvSet("LOCATION",  "06BM -hutch RG:C2")
epicsEnvSet("STREAM_PROTOCOL_PATH", ".:../protocols:$(PMACUTIL)/protocol:/$(PMACCOORD)/protocol")

epicsEnvSet("SYS",           "XF:06BM-CT")
epicsEnvSet("IOC_ASYN",      "$(SYS){MC:13}")
epicsEnvSet("IOC_PREFIX",    "$(SYS){IOC:MC13}")
epicsEnvSet("CONTROLLER_IP", "10.6.130.93")

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.6.128.255")

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/tpmac.dbd",0,0)
tpmac_registerRecordDeviceDriver(pdbbase) 

# pmacAsynIPConfigure() is a wrapper for drvAsynIPPort::drvAsynIPPortConfigure() and
# pmacAsynIPPort::pmacAsynIPPortConfigureEos().
# See pmacAsynIPPort.c
pmacAsynIPConfigure("P0", "$(CONTROLLER_IP):1025")

# WARNING: a trace-mask of containing 0x10 will TRACE_FLOW (v. noisy!!)
#asynSetTraceMask("P0",-1,0x9)
#asynSetTraceIOMask("P0",-1,0x2)

# pmacAsynMotorCreate(port,addr,card,nAxes)
# see pmacAsynMotor.c
#pmacAsynMotorCreate("P0", 0, 1, 8)
# Setup the motor Asyn layer (port, drvet name, card, nAxes+1)
#drvAsynMotorConfigure("M0", "pmacAsynMotor", 1, 9)

#New model 3 driver
#pmacCreateController(motor record port name, low level port, low level port address, num axes, moving polling period (ms), idle polling period (ms))
pmacCreateController("M0","P0",0,8,100,1000)
pmacCreateAxis("M0", 1)
pmacCreateAxis("M0", 2)
pmacCreateAxis("M0", 3)
pmacCreateAxis("M0", 4)
pmacCreateAxis("M0", 5)
pmacCreateAxis("M0", 6)
pmacCreateAxis("M0", 7)
pmacCreateAxis("M0", 8)

# Disable the limits disabled check for some axes (normally this should be left enabled)
# pmacDisableLimitsCheck(string portname, int axis, int allAxes)
#### disable limit check for all axes
#pmacDisableLimitsCheck("M0", 0, 1)
#### disable limit check for axis 3
#pmacDisableLimitsCheck("M0", 3, 0)

#Set the axis scale factor
#pmacSetAxisScale("M0", 1, 1)

#Set the encoder axis for an open loop axis.
#pmacSetOpenLoopEncoderAxis(const char *controller, int axis, int encoder_axis)
#pmacSetOpenLoopEncoderAxis("M0", 1, 2)


# Initialize the coord-system(port,addr,cs,ref,prog#)
# pmacAsynCoordCreate("P0",0,1,1,10)
# pmacAsynCoordCreate("P0",0,2,2,10)

# setup the coord-sys(portName,drvel-name,ref#(from create),nAxes+1)
# drvAsynMotorConfigure("CS1","pmacAsynCoord",1,9)
# drvAsynMotorConfigure("CS2","pmacAsynCoord",2,9)

# change poll rates (card, poll-period in ms)
pmacSetMovingPollPeriod(1, 100)
pmacSetIdlePollPeriod(1, 1000)
pmacSetCoordMovingPollPeriod(5,200)
pmacSetCoordIdlePollPeriod(5,2000)

#Set scale factor (int ref, int axis, double stepsPerUnit)
#pmacSetCoordStepsPerUnit(0, 6, 10000.0)
#pmacSetCoordStepsPerUnit(0, 7, 10000.0)

## Load record instances
dbLoadTemplate("db/motor.substitutions")
dbLoadTemplate("db/motorstatus.substitutions")
dbLoadTemplate("db/pmacStatus.substitutions")
dbLoadTemplate("db/pmac_asyn_motor.substitutions")
dbLoadTemplate("db/autohome.substitutions")
#dbLoadTemplate("db/cs.substitutions")
dbLoadRecords("db/asynComm.db","P=$(IOC_ASYN),PORT=P0,ADDR=0")
dbLoadRecords("db/kill_all.db","P=$(IOC_ASYN),Port=P0")

dbLoadRecords("$(EPICS_BASE)/db/save_restoreStatus.db","P=$(IOC_PREFIX)")
dbLoadRecords("$(EPICS_BASE)/db/iocAdminSoft.db","IOC=$(IOC_PREFIX)")


## autosave/restore machinery
save_restoreSet_Debug(0)
save_restoreSet_IncompleteSetsOk(1)
save_restoreSet_DatedBackupFiles(1)

set_savefile_path("${TOP}/as","/save")
set_requestfile_path("${TOP}/as","/req")

system("install -m 777 -d ${TOP}/as/save")
system("install -m 777 -d ${TOP}/as/req")

set_pass0_restoreFile("info_positions.sav")
set_pass0_restoreFile("info_settings.sav")
set_pass1_restoreFile("info_settings.sav")

save_restoreSet_status_prefix("$(IOC_PREFIX)")
# asSetFilename("/cf-update/acf/default.acf")

iocInit()

# caPutLogInit("xf-ca1:7004", 1)

## more autosave/restore machinery
cd ${TOP}/as/req
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5 , "")
create_monitor_set("info_settings.req", 15 , "")

cd ${TOP}
dbl > ./records.dbl
#system "cp ./records.dbl /cf-update/xf06BMc-ioc1.mcc13.dbl"
