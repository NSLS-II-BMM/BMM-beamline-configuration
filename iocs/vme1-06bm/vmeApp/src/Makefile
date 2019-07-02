TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

USE_GESYS=YES

PROD_IOC_RTEMS = vme
# vme.dbd will be created and installed
DBD += vme.dbd

# vme.dbd will be made up from these files:
vme_DBD += base.dbd

# Include dbd files from all support applications:
vme_DBD += evgInit.dbd
vme_DBD += drvemSupport.dbd
vme_DBD += epicsvme.dbd
vme_DBD += epicspci.dbd

vme_DBD += mca.dbd
vme_DBD += mcaSupport.dbd
vme_DBD += SIS38XXSupport.dbd
vme_DBD += calcSupport.dbd
vme_DBD += sscanSupport.dbd
vme_DBD += stdSupport.dbd
vme_DBD += asyn.dbd

vme_DBD += busySupport.dbd
vme_DBD += devIocStats.dbd
vme_DBD += asSupport.dbd
#vme_DBD += generalTime.dbd
vme_DBD += caPutLog.dbd


# Add all the support libraries needed by this IOC
vme_LIBS += evgmrm
vme_LIBS += evrMrm
vme_LIBS += mrmShared
vme_LIBS += epicspci
vme_LIBS += epicsvme
vme_LIBS += evr
vme_LIBS += mrfCommon

vme_LIBS += mca
vme_LIBS += SIS38XX
vme_LIBS += calc
vme_LIBS += sscan
vme_LIBS += std
vme_LIBS += seq pv
vme_LIBS += asyn

vme_LIBS += busy
vme_LIBS += devIocStats
vme_LIBS += autosave
#vme_LIBS += generalTime
vme_LIBS += caPutLog

# vme_registerRecordDeviceDriver.cpp derives from vme.dbd
vme_SRCS += vme_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
vme_SRCS_DEFAULT += vmeMain.cpp
vme_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#vme_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
vme_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

