#!../../bin/linux-x86_64/oneWire

## Location of stream protocol files
#epicsEnvSet("ENGINEER", "hxu x4394")
epicsEnvSet("ENGINEER",  "kgofron x5283")
epicsEnvSet("LOCATION", "740 BM6")

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.6.0.255")

< envPaths

epicsEnvSet("STREAM_PROTOCOL_PATH", "$(TOP)/protocol")

## Register all support components
dbLoadDatabase "$(TOP)/dbd/oneWire.dbd"
oneWire_registerRecordDeviceDriver pdbbase

## Configure serial port for Rex-F9000 controller
#drvAsynIPPortConfigure("XF_TC1","10.0.131.50:4004")
#drvAsynIPPortConfigure("XF_TC2","10.0.131.50:4008")

#drvAsynIPPortConfigure("HA7E_1","192.168.127.254:4001")
drvAsynIPPortConfigure("HA7E_1","10.6.130.56:4016")
#drvAsynIPPortConfigure("HA7E_1","10.18.2.51:4014")
#drvAsynIPPortConfigure("HA7E_A","10.10.2.51:4008")
#drvAsynIPPortConfigure("HA7E_B","10.10.2.53:4008")
#drvAsynIPPortConfigure("HA7E_C","10.10.2.55:4008")
#drvAsynIPPortConfigure("HA7E_D","10.10.2.57:4008")

## Load record instances
dbLoadRecords "$(TOP)/db/asynRecord.db"
#dbLoadRecords "$(TOP)/db/ha7e.db"
#dbLoadRecords "$(TOP)/db/humidity_test.db"
dbLoadRecords "$(TOP)/db/temp_ds18b20.db"

iocInit
dbpf("XF:6BMA{SENS:001}Val:Raw-Wf.SCAN", "1 second")
#dbpf("XF:18IDA{SENS:002}Val:Page0-Wf.SCAN", "1 second")
#dbpf("XF:10IDA{SENS:001}Val:Raw-Wf.SCAN", "10 second")
#dbpf("XF:10IDB{SENS:001}Val:Raw-Wf.SCAN", "10 second")
#dbpf("XF:10IDC{SENS:001}Val:Raw-Wf.SCAN", "10 second")
#dbpf("XF:10IDD{SENS:001}Val:Raw-Wf.SCAN", "10 second")
