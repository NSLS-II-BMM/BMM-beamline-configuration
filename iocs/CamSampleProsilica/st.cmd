#!/epics/distrib/ADBundle-R-3-3-2+deb7u1-x86_64/areaDetector/ADProsilica/iocs/prosilicaIOC/bin/linux-x86_64/prosilicaApp
errlogInit(20000)

< envPaths

dbLoadDatabase("$(TOP)/dbd/prosilicaApp.dbd")

prosilicaApp_registerRecordDeviceDriver(pdbbase) 

# Prefix for all records
epicsEnvSet("PREFIX", "XF:28ID1-BI{Cam:testAnton}")
# The port name for the detector
epicsEnvSet("PORT",   "PS1")
# The queue size for all plugins
epicsEnvSet("QSIZE",  "20")
# The maximim image width; used for row profiles in the NDPluginStats plugin
epicsEnvSet("XSIZE",  "1292")
# The maximim image height; used for column profiles in the NDPluginStats plugin
epicsEnvSet("YSIZE",  "964")
# The maximum number of time series points in the NDPluginStats plugin
epicsEnvSet("NCHANS", "2048")
# The maximum number of frames buffered in the NDPluginCircularBuff plugin
epicsEnvSet("CBUFFS", "500")
# The search path for database files
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db")

# More env settings, not include above, and in envpath
epicsEnvSet("ENGINEER", "Oksana Ivashkevych x7028")
epicsEnvSet("LOCATION", "XF28ID1{Bhutch}")
epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.28.33.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "50000000")

# prosilicaConfig(portName,    # The name of the asyn port to be created
#                 cameraId,    # Unique ID, IP address, or IP name of the camera
#                 maxBuffers,  # Maximum number of NDArray buffers driver can allocate. 0=unlimited
#                 maxMemory,   # Maximum memory bytes driver can allocate. 0=unlimited
#                 priority,    # EPICS thread priority for asyn port driver 0=default
#                 stackSize,   # EPICS thread stack size for asyn port driver 0=default
#                 maxPvAPIFrames) # Number of frames to allocate in PvAPI driver. Default=2.
# The simplest way to determine the uniqueId of a camera is to run the Prosilica GigEViewer application, 
# select the camera, and press the "i" icon on the bottom of the main window to show the camera information for this camera. 
# The Unique ID will be displayed on the first line in the information window.
#prosilicaConfig("$(PORT)", 51031, 50, 0, 0, 0, 10)
#prosilicaConfig("$(PORT)", 50022, 50, 0)
prosilicaConfig("$(PORT)", 10.28.33.39, 50, 0)
##prosilicaConfig("$(PORT)", 5000698, 50, 0)

asynSetTraceIOMask("$(PORT)",0,2)
#asynSetTraceMask("$(PORT)",0,255)

dbLoadRecords("$(ADPROSILICA)/db/prosilica.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")

# Create a standard arrays plugin, set it to get data from first Prosilica driver.
NDStdArraysConfigure("Image1", 5, 0, "$(PORT)", 0, 0)

# Use this line if you only want to use the Prosilica in 8-bit mode.  It uses an 8-bit waveform record
# NELEMENTS is set large enough for a 1360x1024x3 image size, which is the number of pixels in RGB images from the GC1380CH color camera. 
# Must be at least as big as the maximum size of your camera images
dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),TYPE=Int8,FTVL=UCHAR,NELEMENTS=3736464")

# Use this line if you want to use the Prosilica in 8,12 or 16-bit modes.  
# It uses an 16-bit waveform record, so it uses twice the memory and bandwidth required for only 8-bit data.
##dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),TYPE=Int16,FTVL=SHORT,NELEMENTS=2490976")

# Load all other plugins using commonPlugins.cmd
#< $(ADCORE)/iocBoot/commonPlugins.cmd
< commonPlugins.cmd
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", " IOC=XF:28ID1-CT{IOC:testAnton}")
set_requestfile_path("$(ADPROSILICA)/prosilicaApp/Db")

#asynSetTraceMask("$(PORT)",0,255)

iocInit()

# save things every thirty seconds
#create_monitor_set("auto_settings.req_sav", 30,"P=$(PREFIX)")
create_monitor_set("auto_settings.req", 30,"P=$(PREFIX)")
