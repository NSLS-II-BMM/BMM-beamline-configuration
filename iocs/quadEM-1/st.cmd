#!/epics/support/quadEM/R7-0/bin/linux-x86_64/quadEMTestApp

##ln -s bin/linux-x86_64/quadEMTestApp quadEMIOC
##or ln -s bin/linux-x86/quadEMTestApp quadEMIOC

errlogInit(5000)
epicsEnvSet("QUADEM",   "/epics/support/quadEM/R7-0")
epicsEnvSet("QUAD_DET", "NSLS_EM.cmd")
epicsEnvSet("IOC",      "iocNSLS_EM")
epicsEnvSet("RECORD",    "EM180")
epicsEnvSet("PORT",      "EM180")
epicsEnvSet("TEMPLATE",  "NSLS_EM")
epicsEnvSet("QSIZE",     "20")
epicsEnvSet("RING_SIZE", "10000")
epicsEnvSet("TSPOINTS",  "1000")
< $(QUADEM)/iocBoot/$(IOC)/envPaths
< unique.cmd

dbLoadDatabase("$(QUADEM)/dbd/quadEMTestApp.dbd")
quadEMTestApp_registerRecordDeviceDriver(pdbbase)
# Note: the separator between the path entries needs to be changed to a semicolon (;) on Windows
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db:$(QUADEM)/db")

drvNSLS_EMConfigure("$(PORT)", "$(BROADCAST)", $(MODULE_ID), $(RING_SIZE))

# Load asynRecord record
dbLoadRecords("$(ASYN)/db/asynRecord.db", "P=$(PREFIX), R=asyn1,PORT=$(PORT),ADDR=0,OMAX=256,IMAX=256")
#asynSetTraceIOMask("UDP_$(PORT)", 0, 2)
#asynSetTraceMask("UDP_$(PORT)", 0, 9)
#asynSetTraceMask("TCP_Command_$(PORT)", 0, 9)
#asynSetTraceIOMask("TCP_Data_$(PORT)", 0, 2)
#asynSetTraceMask("TCP_Data_$(PORT)", 0, 9)
asynSetTraceIOMask("$(PORT)", 0, 2)
#asynSetTraceMask("$(PORT)",  0,9)

dbLoadRecords("$(QUADEM)/db/$(TEMPLATE).template", "P=$(PREFIX), R=$(RECORD):, PORT=$(PORT)")

< $(QUADEM)/commonPlugins.cmd

set_requestfile_path("./")
set_requestfile_path("$(QUADEM)/quadEMApp/Db")
set_requestfile_path("$(ADCORE)/ADApp/Db")
set_requestfile_path("/usr/lib/epics/as/req")
set_savefile_path("./as/save")
set_pass0_restoreFile("auto_settings.sav")
set_pass1_restoreFile("auto_settings.sav")
save_restoreSet_status_prefix("$(PREFIX)")
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=$(PREFIX)")
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(PREFIX)IOC")

iocInit()

# save settings every thirty seconds
create_monitor_set("auto_settings.req",30,"P=$(PREFIX), R=$(RECORD):, R_TS=$(RECORD)_TS:")

dbl > ./records.dbl
system "cp ./records.dbl /cf-update/$HOSTNAME.$IOCNAME.dbl"
