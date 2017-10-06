TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += plc1Support

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord
# Install devXxxSoft.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Compile and add the code to the support library
plc1Support_SRCS += xxxRecord.c
plc1Support_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
plc1Support_SRCS += dbSubExample.c
plc1Support_SRCS += plc1Hello.c
plc1Support_SRCS += initTrace.c

plc1Support_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = plc1
# plc1.dbd will be created and installed
DBD += plc1.dbd

# plc1.dbd will be made up from these files:
plc1_DBD += base.dbd
plc1_DBD += xxxSupport.dbd
plc1_DBD += dbSubExample.dbd
plc1_DBD += plc1Hello.dbd
plc1_DBD += initTrace.dbd
plc1_DBD += ether_ip.dbd
plc1_DBD += system.dbd
plc1_DBD += caPutLog.dbd
plc1_DBD += asSupport.dbd
plc1_DBD += devIocStats.dbd

# plc1_registerRecordDeviceDriver.cpp derives from plc1.dbd
plc1_SRCS += plc1_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
plc1_SRCS_DEFAULT += plc1Main.cpp
plc1_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#plc1_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
plc1_LIBS += plc1Support
plc1_LIBS += ether_ip
plc1_LIBS += caPutLog
plc1_LIBS += devIocStats
plc1_LIBS += autosave

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into plc1Support
    sncExample_SNCFLAGS += +r
    plc1_DBD += sncExample.dbd
    plc1Support_SRCS += sncExample.stt
    plc1Support_LIBS += seq pv
    plc1_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link to the EPICS Base libraries
plc1_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

