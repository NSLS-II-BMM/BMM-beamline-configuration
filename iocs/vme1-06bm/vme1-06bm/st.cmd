#
# Environment variables must be set from DHCP
# RACK - Rack group letter and rack number (eg. RACK="D1")

epicsEnvSet("ENGINEER","ZY, x5525")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000")
epicsEnvSet("IOCNAME", "RG${RACK}")

## Register all support components
dbLoadDatabase("dbd/vme.dbd")
vme_registerRecordDeviceDriver(pdbbase)

installRTEMSHack()


##bspExtVerbosity=0

# Load instance specific
# No timing module for 06BM VME rack
#< "st-timing-${RACK}.cmd"

# iocadm is included below
< "st-adm.cmd"

# Struck Scaler: SIS3820
< "st-sclr-${RACK}.cmd"

# Load aliases
#  Does not exist for all systems
#< "alias-c${RACK}.cmd"

#asSetFilename("/cf-update/acf/default.acf")
#asSetFilename("/common/CtrSwitch-log.acf")
#asSetSubstitutions("P=CtrlSwitch:")

set_savefile_path("/mnt/as","/${RACK}/save")
set_requestfile_path("/mnt/as","/${RACK}/req")
# Scaler
#set_requestfile_path("/mnt/as","req")
set_requestfile_path("/mnt/mca/mcaApp","Db")

#set_pass0_restoreFile("mrf_settings.sav")
#set_pass0_restoreFile("mrf_values.sav")
#set_pass1_restoreFile("mrf_values.sav")
#set_pass1_restoreFile("mrf_waveforms.sav")

# Scaler
set_pass0_restoreFile("auto_settings_$(MODEL).sav")
set_pass1_restoreFile("auto_settings_$(MODEL).sav")

iocInit()

#makeAutosaveFileFromDbInfo("as/${RACK}/req/mrf_settings.req", "autosaveFields_pass0")
#makeAutosaveFileFromDbInfo("as/${RACK}/req/mrf_values.req", "autosaveFields")
#makeAutosaveFileFromDbInfo("as/${RACK}/req/mrf_waveforms.req", "autosaveFields_pass1")

#create_monitor_set("mrf_settings.req", 15 , "")
#create_monitor_set("mrf_values.req", 15 , "")
#create_monitor_set("mrf_waveforms.req", 30 , "")
# Scaler: save settings every thirty seconds
create_monitor_set("auto_settings_$(MODEL).req",30,"P=$(SYS)$(DEV),S=scaler1")

#caPutLogInit("ioclog.cs.nsls2.local:7004")

# to be called AFTER iocInit()
# NOTE: "R" here cannot be null, else "mca" is appended to record names automagically.
# As is, the sequencer will expand the macros to look for records of the form
# "$(P)(R)N", where 1 <= N <= NUM_SIGNALS
# <eyes rolling>F**k me...</eyes rolling> 
seq(&SIS38XX_SNL, "P=$(SYS)$(DEV), R=mca, NUM_SIGNALS=$(MAX_SIGNALS), FIELD=$(FIELD)")

# NOTE: "/cf-update" mounted from web01.cs.nsls2.local
#dbl > /cf-update/${HOSTNAME}.${IOCNAME}.dbl
