#!../../bin/linux-x86-debug/psc

< envPaths

epicsEnvSet("IOCNAME", "iocpscenc")

cd ${TOP}

epicsEnvSet("ENGINEER","rkadyrov x2421")
epicsEnvSet("LOCATION","741, Controls lab")

## Register all support components
dbLoadDatabase("dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("db/GenRx.db","Sys=TEST-CT,Chan=1")
dbLoadRecords("db/GenTx.db","Sys=TEST-CT")
dbLoadRecords("db/GenSts.db","Sys=TEST-CT")

createPSC("TxGen", "10.8.3.55", 7,0)
createPSC("RxGen", "10.8.3.55", 20,1)

asSetFilename("${TOP}/DEFAULT.acf")

var(PSCDebug, 2)

iocInit()

dbl > records.dbl
#system "cp records.dbl /cf-update/$HOSTNAME.$IOCNAME.dbl"

#caPutLogInit("10.0.152.133:7004", 1)

