#!../../bin/linux-x86_64/I400

## You may have to change I400 to something else
## everywhere it appears in this file

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.6.128.255")

< envPaths

cd ${TOP}

## configuration for stream
epicsEnvSet ("STREAM_PROTOCOL_PATH", ".:./I400App/src/protocol-files/")

## Register all support components
dbLoadDatabase("./dbd/I400.dbd",0,0)
I400_registerRecordDeviceDriver(pdbbase) 

#######  I404 via com-port #########################
###switch the Ixxx to Mode:3 Address:Dont Care
##
#drvAsynSerialPortConfigure "COM1", "/dev/ttyS0"
#drvAsynSerialPortConfigure "COM1", "/dev/ttyUSB2"
#asynOctetSetInputEos "COM1",0,"\r\n"
#asynOctetSetOutputEos "COM1",0,"\r\n"
#asynSetOption ("COM1", 0, "baud", "115200")
#asynSetOption ("COM1", 0, "bits", "8")
#asynSetOption ("COM1", 0, "parity", "none")
#asynSetOption ("COM1", 0, "stop", "1")
#asynSetOption ("COM1", 0, "clocal", "Y")
#asynSetOption ("COM1", 0, "crtscts", "N")


##############  I404 via Moxa TCP Server  #########
##
## drvAsynIPPortConfigure(portName, hostInfo, priority, noAutoConnect, noProcessEos)
drvAsynIPPortConfigure("I400_1", "10.6.130.51:4001",0,0,0)
drvAsynIPPortConfigure("I400_2", "10.6.130.52:4001",0,0,0)
##

#asynSetTraceMask("I400_1",0,9)
#asynSetTraceIOMask("I400_1",0,9)

## Load record instances
#dbLoadRecords("./db/I400.db","user=iocuser")
dbLoadTemplate("./db/I400.substitutions")

## Run this to trace the stages of iocInit
#traceIocInit

iocInit()

## Start any sequence programs
#seq sncI400,"user=iocuser"

###Streamdebug#################################################################
var streamDebug 0
###############################################################################

date
##EOF
