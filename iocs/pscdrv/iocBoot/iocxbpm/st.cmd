#!../bpmIOCpscdrv/pscdrv/bin/linux-x86-debug/psc

## You may have to change psc to something else
## everywhere it appears in this file

epicsEnvSet("TOP","../bpmIOCpscdrv/pscdrv")
epicsEnvSet("BPMDIR","$(TOP)")


# Register all support components
dbLoadDatabase("$(BPMDIR)/dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 


#
#****************************************************************************
# XBPM SETTINGS
#
epicsEnvSet("XBPM1_IP", "10.0.143.151"); ## Electrometer IP
epicsEnvSet("XBPM2_IP", "10.0.143.155"); ## Electrometer IP


epicsEnvSet("EPICS_CA_ADDR_LIST", "10.0.143.255") ##
epicsEnvSet("CNO","03")   			  ## Electrometer Cell Number
#epicsEnvSet("NO","1")   			  ## Electrometer Number
epicsEnvSet("IOCNAME", "SR:C$(CNO)-BI")		  ## Electrometer NAME
#****************************************************************************
#
epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "50000000")
##**Load record instances
dbLoadRecords("/home/mead/epics/xbpm_blade.db", "P=$(IOCNAME), NO=1, ADC_WFM_LEN=102400, FA_WFM_LEN=131072")




##**PSC Settings
var(PSCDebug, 2) #5 full debug

#bpm1
createPSC("aie_tx_1", $(XBPM1_IP), 7, 0)
createPSC("aie_wfm_rx_1", $(XBPM1_IP), 20, 1)
createPSC("Rx1", $(XBPM1_IP), 600, 1)
#bpm2
createPSC("aie_tx_2", $(XBPM2_IP), 7, 0)
createPSC("aie_wfm_rx_2", $(XBPM2_IP), 20, 1)
createPSC("Rx2", $(XBPM2_IP), 600, 1)




##**IOC Initialization
iocInit()
#epicsThreadSleep 1
#****************************************************************************
# ELECTROMETER INITIALIZATION PARAMETERS
#
#Initialization Start

#xbpm1
epicsEnvSet("NO","1")   #Electrometer Number

dbpf $(IOCNAME){XBPM:$(NO)}Trig:EventNum-SP 33
dbpf $(IOCNAME){XBPM:$(NO)}Trig:Dly-SP 100
dbpf $(IOCNAME){XBPM:$(NO)}Trig:NumSamples-SP 8192

#Bias Output
dbpf $(IOCNAME){XBPM:$(NO)}Bias:Conn-SP 1 #Connected
dbpf $(IOCNAME){XBPM:$(NO)}Bias:InnerShieldConn-SP 0 #Grounded
dbpf $(IOCNAME){XBPM:$(NO)}Bias:BiasSource-SP 0 #Internal
#Channel
dbpf $(IOCNAME){XBPM:$(NO)}Channel:BiasSource-SP 0 #Internal
dbpf $(IOCNAME){XBPM:$(NO)}Channel:InnerShieldConn-SP 0 #Grounded
#Internal Bias
dbpf $(IOCNAME){XBPM:$(NO)}IntBias:Level-SP 0
dbpf $(IOCNAME){XBPM:$(NO)}IntBias:Pol-SP 1 #Negative
#Internal Bias Calibration
dbpf $(IOCNAME){XBPM:$(NO)}IntBias:Level-SP.ESLO 0.0007305818
dbpf $(IOCNAME){XBPM:$(NO)}IntBias:Level-SP.AOFF 1018
#Gain Calibration
#1uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO1 -1893
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO1 -1488
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO1 -1820
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO1 -1618
#1uA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO2 7787
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO2 7792
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO2 7750
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO2 7771
#10uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO3 -1890
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO3 -1484
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO3 -1818
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO3 -1615
#10uA Gains (fA/bit)
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO4 77682
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO4 77703
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO4 77804
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO4 77476
#100uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO5 -1890
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO5 -1484
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO5 -1818
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO5 -1614
#100uA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO6 776610
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO6 777328
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO6 777780
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO6 774496
#1mA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO7 -1890
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO7 -1485
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO7 -1818
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO7 -1621
#1mA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO8 8873345
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO8 8881521
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO8 8888107
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO8 8850341
#10mA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO9 -1920
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO9 -1515
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO9 -1849
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO9 -1647
#10mA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DOA 73121587
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DOA 72449054
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DOA 72228634
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DOA 72595240
#Set Gain
dbpf $(IOCNAME){XBPM:$(NO)}Gain:Level-SP 3 #1mA
#Clock Source
dbpf $(IOCNAME){XBPM:$(NO)}ClkSrc-SP 2 #0=External, 1=Internal, 2=evr
#Position Calibration
dbpf $(IOCNAME){XBPM:$(NO)}Pos:Kx-SP 2960000
dbpf $(IOCNAME){XBPM:$(NO)}Pos:Ky-SP 2160000
#Initialization Complete
epicsThreadSleep 1
dbpf $(IOCNAME){XBPM:$(NO)}Leds-SP 0



#xbpm2 (diamond)
epicsEnvSet("NO","2")   #Electrometer Number

dbpf $(IOCNAME){XBPM:$(NO)}Trig:EventNum-SP 33
dbpf $(IOCNAME){XBPM:$(NO)}Trig:Dly-SP 100
dbpf $(IOCNAME){XBPM:$(NO)}Trig:NumSamples-SP 8192

#Gain Calibration
#1uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO1 -1925
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO1 -1519
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO1 -1854
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO1 -1647
#1uA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO2 7787
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO2 7792
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO2 7750
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO2 7771
#10uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO3 -1921
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO3 -1515
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO3 -1849
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO3 -1542
#10uA Gains (fA/bit)
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO4 77682
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO4 77703
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO4 77804
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO4 77476
#100uA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO5 -1920
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO5 -1514
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO5 -1849
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO5 -1641
#100uA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO6 776610
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO6 777328
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO6 777780
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO6 774496
#1mA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO7 -1920
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO7 -1515
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO7 -1849
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO7 -1647
#1mA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO8 8873345
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO8 8881521
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO8 8888107
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO8 8850341
#10mA Offsets
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DO9 -1920
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DO9 -1515
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DO9 -1849
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DO9 -1647
#10mA Gains
dbpf $(IOCNAME){XBPM:$(NO)}ACalib_Set.DOA 73121587
dbpf $(IOCNAME){XBPM:$(NO)}BCalib_Set.DOA 72449054
dbpf $(IOCNAME){XBPM:$(NO)}CCalib_Set.DOA 72228634
dbpf $(IOCNAME){XBPM:$(NO)}DCalib_Set.DOA 72595240
#Set Gain
dbpf $(IOCNAME){XBPM:$(NO)}Gain:Level-SP 3 #1mA
#Clock Source
dbpf $(IOCNAME){XBPM:$(NO)}ClkSrc-SP 2 #0=External, 1=Internal, 2=evr
#Position Calibration
dbpf $(IOCNAME){XBPM:$(NO)}Pos:Kx-SP 2960000
dbpf $(IOCNAME){XBPM:$(NO)}Pos:Ky-SP 2160000
#Initialization Complete
dbpf $(IOCNAME){XBPM:$(NO)}Leds-SP 0
