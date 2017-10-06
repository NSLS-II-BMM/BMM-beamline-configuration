TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += softIocCommonSupport

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord
# Install devXxxSoft.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Compile and add the code to the support library
softIocCommonSupport_SRCS += xxxRecord.c
softIocCommonSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
softIocCommonSupport_SRCS += dbSubExample.c
softIocCommonSupport_SRCS += softIocCommonHello.c
softIocCommonSupport_SRCS += initTrace.c

softIocCommonSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = softIocCommon
# softIocCommon.dbd will be created and installed
DBD += softIocCommon.dbd

# softIocCommon.dbd will be made up from these files:
softIocCommon_DBD += base.dbd
softIocCommon_DBD += xxxSupport.dbd
softIocCommon_DBD += dbSubExample.dbd
softIocCommon_DBD += softIocCommonHello.dbd
softIocCommon_DBD += initTrace.dbd
#include iocStatus and autosave which are installed by epics Debian package
# /usr/lib/epics/dbd/
softIocCommon_DBD += caPutLog.dbd
softIocCommon_DBD += devIocStats.dbd
softIocCommon_DBD += asSupport.dbd
softIocCommon_DBD += system.dbd
softIocCommon_DBD += asyn.dbd
softIocCommon_DBD += stream.dbd
softIocCommon_DBD += drvAsynIPPort.dbd
softIocCommon_DBD += drvAsynSerialPort.dbd
softIocCommon_DBD += calcSupport.dbd
softIocCommon_DBD += swaitRecord.dbd

# softIocCommon_registerRecordDeviceDriver.cpp derives from softIocCommon.dbd
softIocCommon_SRCS += softIocCommon_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
softIocCommon_SRCS_DEFAULT += softIocCommonMain.cpp
softIocCommon_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#softIocCommon_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
softIocCommon_LIBS += softIocCommonSupport

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into softIocCommonSupport
    sncExample_SNCFLAGS += +r
    softIocCommon_DBD += sncExample.dbd
    softIocCommonSupport_SRCS += sncExample.stt
    softIocCommonSupport_LIBS += seq pv
    softIocCommon_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

#include autosave and devIocStats libraries which are installed by epics Debian
#package: /usr/lib/epics/lib/linux-x86
softIocCommon_LIBS += caPutLog
softIocCommon_LIBS += autosave
softIocCommon_LIBS += devIocStats
softIocCommon_LIBS += asyn
softIocCommon_LIBS += stream
softIocCommon_LIBS += calc
softIocCommon_LIBS += sscan
# Finally link to the EPICS Base libraries
softIocCommon_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

