#!../../bin/linux-x86/psc

epicsThreadSleep 5
## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC17")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC17")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC17,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC17,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC18")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC18")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC18,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC18,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC19")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC19")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC19,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC19,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC20")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC20")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC20,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC20,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC21")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC21")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC21,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC21,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC22")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC22")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC22,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC22,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC23")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC23")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC23,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC23,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC24")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC24")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC24,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC24,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC25")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC25")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC25,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC25,WF10K_LENGTH=43440")

dbLoadRecords("../../db/Commands.db","PriSys=BR,PS=PSC26")
dbLoadRecords("../../db/Status.db","PriSys=BR,PS=PSC26")
dbLoadRecords("../../db/ADCWaveform.db","PriSys=BR,PS=PSC26,ADC1K_POINTS=1100,ADC10K_POINTS=11000")
dbLoadRecords("../../db/RampingTable.db","PriSys=BR,PS=PSC26,WF10K_LENGTH=43440")

var(PSCDebug, 1)
#with debug message: var(PSCDebug, 2)

#Tx socket
createPSC("TxPSC17", "10.0.140.1", 7,0)
createPSC("TxPSC18", "10.0.140.2", 7,0)
createPSC("TxPSC19", "10.0.140.3", 7,0)
createPSC("TxPSC20", "10.0.140.4", 7,0)
createPSC("TxPSC21", "10.0.140.5", 7,0)
createPSC("TxPSC22", "10.0.140.6", 7,0)
createPSC("TxPSC23", "10.0.140.7", 7,0)
createPSC("TxPSC24", "10.0.140.8", 7,0)
createPSC("TxPSC25", "10.0.140.9", 7,0)
createPSC("TxPSC26", "10.0.140.10", 7,0)
epicsThreadSleep 0.1
#Rx socket
createPSC("RxPSC17", "10.0.140.1", 20,1)
createPSC("RxPSC18", "10.0.140.2", 20,1)
createPSC("RxPSC19", "10.0.140.3", 20,1)
createPSC("RxPSC20", "10.0.140.4", 20,1)
createPSC("RxPSC21", "10.0.140.5", 20,1)
createPSC("RxPSC22", "10.0.140.6", 20,1)
createPSC("RxPSC23", "10.0.140.7", 20,1)
createPSC("RxPSC24", "10.0.140.8", 20,1)
createPSC("RxPSC25", "10.0.140.9", 20,1)
createPSC("RxPSC26", "10.0.140.10", 20,1)
epicsThreadSleep 0.1
setPSCSendBlockSize("TxPSC17", 80, 128)
setPSCSendBlockSize("TxPSC18", 80, 128)
setPSCSendBlockSize("TxPSC19", 80, 128)
setPSCSendBlockSize("TxPSC20", 80, 128)
setPSCSendBlockSize("TxPSC21", 80, 128)
setPSCSendBlockSize("TxPSC22", 80, 128)
setPSCSendBlockSize("TxPSC23", 80, 128)
setPSCSendBlockSize("TxPSC24", 80, 128)
setPSCSendBlockSize("TxPSC25", 80, 128)
setPSCSendBlockSize("TxPSC26", 80, 128)

iocInit()

