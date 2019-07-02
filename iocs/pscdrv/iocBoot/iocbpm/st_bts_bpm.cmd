#!../../bin/linux-x86/psc

## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 


epicsEnvSet("BPM1_IP", "10.0.142.51");
epicsEnvSet("BPM2_IP", "10.0.142.52");
epicsEnvSet("BPM3_IP", "10.0.142.53");
epicsEnvSet("BPM4_IP", "10.0.142.54");
epicsEnvSet("BPM5_IP", "10.0.142.55");
epicsEnvSet("BPM6_IP", "10.0.142.56");
epicsEnvSet("BPM7_IP", "10.0.142.57");
epicsEnvSet("BPM8_IP", "10.0.142.58");


## Load record instances

########## use template 
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=1, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=2, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=3, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=4, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=5, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=6, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=7, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")
dbLoadRecords("../../db/bpm.db", "P=BTS-BI, NO=8, ADC_WFM_LEN=10240, TBT_WFM_LEN=10000, FA_WFM_LEN=9000")




var(PSCDebug, 2)	#5 full debug

#bpm1
createPSC("aie_tx_1", $(BPM1_IP), 7, 0)
setPSCSendBlockSize("aie_tx_1", 1, 720)
createPSC("aie_wfm_rx_1", $(BPM1_IP), 20, 1)
createPSC("Rx1", $(BPM1_IP), 600, 1)
#bpm2
createPSC("aie_tx_2", $(BPM2_IP), 7, 0)
setPSCSendBlockSize("aie_tx_2", 1, 720)
createPSC("aie_wfm_rx_2", $(BPM2_IP), 20, 1)
createPSC("Rx2", $(BPM2_IP), 600, 1)
#bpm3
createPSC("aie_tx_3", $(BPM3_IP), 7, 0)
setPSCSendBlockSize("aie_tx_3", 1, 720)
createPSC("aie_wfm_rx_3", $(BPM3_IP), 20, 1)
createPSC("Rx3", $(BPM3_IP), 600, 1)
#bpm4
createPSC("aie_tx_4", $(BPM4_IP), 7, 0)
setPSCSendBlockSize("aie_tx_4", 1, 720)
createPSC("aie_wfm_rx_4", $(BPM4_IP), 20, 1)
createPSC("Rx4", $(BPM4_IP), 600, 1)
#bpm5
createPSC("aie_tx_5", $(BPM5_IP), 7, 0)
setPSCSendBlockSize("aie_tx_5", 1, 720)
createPSC("aie_wfm_rx_5", $(BPM5_IP), 20, 1)
createPSC("Rx5", $(BPM5_IP), 600, 1)
#bpm6
createPSC("aie_tx_6", $(BPM6_IP), 7, 0)
setPSCSendBlockSize("aie_tx_6", 1, 720)
createPSC("aie_wfm_rx_6", $(BPM6_IP), 20, 1)
createPSC("Rx6", $(BPM6_IP), 600, 1)
#bpm7
createPSC("aie_tx_7", $(BPM7_IP), 7, 0)
setPSCSendBlockSize("aie_tx_7", 1, 720)
createPSC("aie_wfm_rx_7", $(BPM7_IP), 20, 1)
createPSC("Rx7", $(BPM7_IP), 600, 1)
#bpm8
createPSC("aie_tx_8", $(BPM8_IP), 7, 0)
setPSCSendBlockSize("aie_tx_8", 1, 720)
createPSC("aie_wfm_rx_8", $(BPM8_IP), 20, 1)
createPSC("Rx8", $(BPM8_IP), 600, 1)



iocInit()

epicsThreadSleep 1



