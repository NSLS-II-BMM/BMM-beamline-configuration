TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = PIE625
# PIE625.dbd will be created and installed
DBD += PIE625.dbd

# PIE625.dbd will be made up from these files:
PIE625_DBD += base.dbd

# Include dbd files from all support applications:
PIE625_DBD += asyn.dbd
PIE625_DBD += drvAsynIPPort.dbd
PIE625_DBD += $(MOTOR)/dbd/motorSupport.dbd
PIE625_DBD += $(MOTOR)/dbd/motorRecord.dbd
PIE625_DBD += $(MOTOR)/dbd/PIE625Support.dbd
PIE625_DBD += asSupport.dbd
PIE625_DBD += devIocStats.dbd

# Add all the support libraries needed by this IOC
PIE625_LIBS += motor PIE625 asyn autosave devIocStats

# PIE625_registerRecordDeviceDriver.cpp derives from PIE625.dbd
PIE625_SRCS += PIE625_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
PIE625_SRCS_DEFAULT += PIE625Main.cpp
PIE625_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#PIE625_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
PIE625_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

