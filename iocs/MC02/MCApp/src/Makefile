TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = MC
# MC.dbd will be created and installed
#DBD += MC.dbd
DBD += ${PROD_IOC}.dbd

# SAI.dbd will be made up from these files:
${PROD_IOC}_DBD += base.dbd
${PROD_IOC}_DBD += sscan.dbd
${PROD_IOC}_DBD += calcSupport.dbd
${PROD_IOC}_DBD += asSupport.dbd
${PROD_IOC}_DBD += busySupport.dbd
${PROD_IOC}_DBD += stream.dbd
${PROD_IOC}_DBD += asyn.dbd
${PROD_IOC}_DBD += motorSupport.dbd
${PROD_IOC}_DBD += drvAsynIPPort.dbd
${PROD_IOC}_DBD += pmacAsynIPPort.dbd
${PROD_IOC}_DBD += pmacAsynMotor.dbd
${PROD_IOC}_DBD += uIOCSystem.dbd
#${PROD_IOC}_DBD += generic_scan.dbd

# Include dbd files from all support applications:
#${PROD_IOC}_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#${PROD_IOC}_LIBS += xxx
${PROD_IOC}_LIBS += autosave
${PROD_IOC}_LIBS += seq pv
${PROD_IOC}_LIBS += calc
${PROD_IOC}_LIBS += sscan busy
${PROD_IOC}_LIBS += stream
${PROD_IOC}_LIBS += asyn
${PROD_IOC}_LIBS += motor
${PROD_IOC}_LIBS += pmacAsynIPPort
${PROD_IOC}_LIBS += pmacAsynMotor
${PROD_IOC}_LIBS += uIOCSystem
#${PROD_IOC}_LIBS += generic_scan

# SAI_registerRecordDeviceDriver.cpp derives from MC.dbd
${PROD_IOC}_SRCS += MC_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
${PROD_IOC}_SRCS_DEFAULT += MCMain.cpp
${PROD_IOC}_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#MC_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
${PROD_IOC}_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

