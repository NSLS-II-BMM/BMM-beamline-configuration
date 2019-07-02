#!../../bin/linux-x86-debug/psc

## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../db/psctest.db","P=test:")

var(PSCDebug, 2)

createPSC("test", "10.0.140.31", 20)

iocInit()

