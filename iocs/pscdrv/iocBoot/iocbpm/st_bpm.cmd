#!../../bin/linux-x86/psc

## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 


epicsEnvSet("BPM1_IP", "10.0.142.22");
#epicsEnvSet("BPM1_IP", "10.0.143.73");  ## C24-1
#epicsEnvSet("NO", "3");


epicsEnvSet("CNO","24")   ## Cell Number
epicsEnvSet("HOSTNAME","diagioc-c$(CNO)")
epicsEnvSet("IOCNAME", "SR:C$(CNO)-BI")
epicsEnvSet("IOC_NAME","SR-CS{IOC:SR:C$(CNO)}")

#epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
#epicsEnvSet("EPICS_CA_ADDR_LIST", "10.0.153.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "50000000")



## Load record instances

########## use template 
dbLoadRecords("../../db/bpm.db", "P=SR:C24-BI, NO=1,     ADC_WFM_LEN=102400, TBT_WFM_LEN=100000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm_alarm_sumery.db", "P=SR:C24-BI, CNO=24, MAXBPM=1")

var(PSCDebug, 2)	#5 full debug

#bpm1
createPSC("aie_tx_1", $(BPM1_IP), 7, 0)
createPSC("aie_wfm_rx_1", $(BPM1_IP), 20, 1)
createPSC("Rx1", $(BPM1_IP), 600, 1)


iocInit()

epicsThreadSleep 1



