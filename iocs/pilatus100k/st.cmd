#!/epics/distrib/ADBundle-R-3-3-2+deb7u2-x86_64/areaDetector/ADPilatus/iocs/pilatusIOC/bin/linux-x86_64/pilatusDetectorApp
< envPaths
errlogInit(20000)

dbLoadDatabase("$(TOP)/dbd/pilatusDetectorApp.dbd")
pilatusDetectorApp_registerRecordDeviceDriver(pdbbase) 

# Prefix for all records
epicsEnvSet("PREFIX", "XF:06BMB-ES{Det:PIL100k}:")
# The port name for the detector
epicsEnvSet("PORT",   "PIL")
# The queue size for all plugins
epicsEnvSet("QSIZE",  "20")
# The maximim image width; used for row profiles in the NDPluginStats plugin
epicsEnvSet("XSIZE",  "487")
# The maximim image height; used for column profiles in the NDPluginStats plugin
epicsEnvSet("YSIZE",  "195")
# The maximum number of time seried points in the NDPluginStats plugin
epicsEnvSet("NCHANS", "2048")
# The maximum number of frames buffered in the NDPluginCircularBuff plugin
epicsEnvSet("CBUFFS", "500")
# The search path for database files
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db")

# CA MAX ARRAY BYTES
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES",99999999)

###
# Create the asyn port to talk to the Pilatus on port 41234.
###drvAsynIPPortConfigure("camserver","gse-pilatus1:41234")
drvAsynIPPortConfigure("camserver","10.6.129.5:41234")
# Uncomment the following to enable asynTrace on the camserver port
#asynSetTraceIOMask("camserver",0,2)
#asynSetTraceMask("camserver",0,9)
# Set the input and output terminators.
asynOctetSetInputEos("camserver", 0, "\030")
asynOctetSetOutputEos("camserver", 0, "\n")

pilatusDetectorConfig("$(PORT)", "camserver", $(XSIZE), $(YSIZE), 0, 0)
dbLoadRecords("$(ADPILATUS)/db/pilatus.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1,CAMSERVER_PORT=camserver")

# Create a standard arrays plugin
NDStdArraysConfigure("Image1", 5, 0, "$(PORT)", 0, 0)
dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),TYPE=Int32,FTVL=LONG,NELEMENTS=2476525")

# Load all other plugins using commonPlugins.cmd
###< $(ADCORE)/iocBoot/commonPlugins.cmd
< commonPlugins.cmd
set_requestfile_path("$(ADPILATUS)/pilatusApp/Db")

# Uncomment to enable asynTrace on the driver port
#asynSetTraceMask("$(PORT)",0,255)

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=XF:11BMB-CT{IOC:PIL2M}")

iocInit()

# save things every thirty seconds
create_monitor_set("auto_settings.req", 30,"P=$(PREFIX)")
