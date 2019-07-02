#!../../bin/linux-x86/psc

## You may have to change psc to something else
## everywhere it appears in this file

epicsThreadSleep 1


epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.0.153.255")


epicsEnvSet("CNO","28")   ## Cell Number
epicsEnvSet("HOSTNAME","diagioc-c$(CNO)")
epicsEnvSet("IOCNAME", "SR:C$(CNO)-FOFB-T")
epicsEnvSet("IOC_NAME","SR-CS{IOC:CC:C$(CNO)T}")

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

epicsEnvSet("FLEN", "100000");


### CELL 28 Test Cell controller
epicsEnvSet("CC_IP", "10.0.143.193");



## Load record instances
dbLoadRecords("../../db/cc.db", "P=$(IOCNAME), NO=1, MAX_BYTE=104, FA_WFM_LEN=$(FLEN)")
dbLoadRecords("../../db/cc_sdi_pos.db", "P=$(IOCNAME){CC}") 
dbLoadRecords("../../db/fofb.db", "P=$(IOCNAME)") 


var(PSCDebug, 2)	#5 full debug
createPSC("aie_tx_1", $(CC_IP), 7, 0)
setPSCSendBlockSize("aie_tx_1", 1, 128)
setPSCSendBlockSize("aie_tx_1", 50, 1024)

createPSC("aie_wfm_rx_1", $(CC_IP), 20, 1)
createPSC("Rx1", $(CC_IP), 600, 1)



iocInit()

epicsThreadSleep 1

