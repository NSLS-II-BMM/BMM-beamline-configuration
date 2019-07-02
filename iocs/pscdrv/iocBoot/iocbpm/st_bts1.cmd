#!../../bin/linux-x86/psc

## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 


epicsEnvSet("BPM1_IP", "10.0.142.51");
epicsEnvSet("NO", "1");

## Load record instances

########## use template 
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=$(NO), ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")


var(PSCDebug, 2)	#5 full debug

#bpm1
createPSC("aie_tx_$(NO)", $(BPM1_IP), 7, 0)
setPSCSendBlockSize("aie_tx_$(NO)", 1, 720)
createPSC("aie_wfm_rx_$(NO)", $(BPM1_IP), 20, 1)
createPSC("Rx$(NO)", $(BPM1_IP), 600, 1)



iocInit()

epicsThreadSleep 1



