#!../../bin/linux-x86/psc

## You may have to change psc to something else
## everywhere it appears in this file

## Register all support components
dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

### Active Interlock
#epicsEnvSet("C31_IP", "10.0.142.31");
#epicsEnvSet("C31_IP", "10.0.143.191");
=======
epicsEnvSet("C31_IP", "10.0.142.16");
=======
#epicsEnvSet("C31_IP", "10.0.140.33");

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST", "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST", "10.0.153.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "50000000")

## Load record instances
epicsEnvSet("P1",  "SR:C31-{AI}")
dbLoadRecords("../../db/ActiveInterlock.db","P=$(P1), NO=1")
dbLoadRecords("../../db/aie_din.db", "P=$(P1)")


#dbLoadRecords("../../db/ail_rwfm.db")
### Logic Setting
## INDEX is BPM Position address


### A1 - A11   BRAM address memory mpa
### X1 - X3    SDI BPM Position Address 
###
## Cell 3
dbLoadRecords("../../db/aie.db", "P=$(P1), ID=3,  U=0, A1=600, A2=900, A3=1200,A4=1500,A5=1800,A6=2100,A7=2400,A8=2700,A9=3000, A10=3300,A11=3600, A12=3900,A13=4200,A14=4500,A15=4800, INDX_X1=64,INDX_X2=66,INDX_X3=68,INDX_Y1=65,INDX_Y2=67,INDX_Y3=69,INDX_CD0=76,INDX_CD1=77, N=0")

#####################
### Cell 5 UP
dbLoadRecords("../../db/aie.db", "P=$(P1), U=1, ID=5,  A1=604, A2=904, A3=1204,A4=1504,A5=1804,A6=2104,A7=2404,A8=2704,A9=3004,A10=3304, A11=3604,A12=3904,A13=4204,A14=4504,A15=4804, INDX_X1=116,INDX_X2=118,INDX_X3=120,INDX_Y1=117,INDX_Y2=119,INDX_Y3=121,INDX_CD0=128,INDX_CD1=129, N=4")

### Cell 5-2 DOWN
dbLoadRecords("../../db/aie.db", "P=$(P1), U=2, ID=5-2, A1=608, A2=908, A3=1208,A4=1508,A5=1808,A6=2108,A7=2408,A8=2708,A9=3008,A10=3308, A11=3608,A12=3908,A13=4208,A14=4508,A15=4808, INDX_X1=116,INDX_X2=118,INDX_X3=120,INDX_Y1=117,INDX_Y2=119,INDX_Y3=121,INDX_CD0=128,INDX_CD1=129, N=8")


### Cell 10
dbLoadRecords("../../db/aie.db", "P=$(P1), U=3, ID=10, A1=612, A2=912, A3=1212,A4=1512,A5=1812,A6=2112,A7=2412,A8=2712,A9=3012,A10=3312, A11=3612,A12=3912,A13=4212,A14=4512,A15=4812, INDX_X1=246,INDX_X2=248,INDX_X3=250,INDX_Y1=247,INDX_Y2=249,INDX_Y3=251,INDX_CD0=2,INDX_CD1=207, N=12")

### Cell 11
dbLoadRecords("../../db/aie.db", "P=$(P1), U=4, ID=11,  A1=616, A2=916, A3=1216,A4=1516,A5=1816,A6=2116,A7=2416,A8=2716,A9=3016, A10=3316, A11=3616,A12=3916,A13=4216,A14=4516,A15=4816, INDX_X1=272,INDX_X2=274,INDX_X3=276,INDX_Y1=273,INDX_Y2=275,INDX_Y3=277,INDX_CD0=284,INDX_CD1=285,N=16")

### Cell 23
dbLoadRecords("../../db/aie.db", "P=$(P1), U=5, ID=23,  A1=620, A2=920, A3=1220,A4=1520,A5=1820,A6=2120,A7=2420,A8=2720,A9=3020, A10=3320, A11=3620,A12=3920,A13=4220,A14=4520,A15=4820, INDX_X1=584,INDX_X2=586,INDX_X3=588,INDX_Y1=585,INDX_Y2=587,INDX_Y3=589,INDX_CD0=596,INDX_CD1=597,N=20")

##############
### Cell 23-2
### 
dbLoadRecords("../../db/aie.db", "P=$(P1), U=6, ID=23-2, A1=624, A2=924, A3=1224,A4=1524,A5=1824,A6=2124,A7=2424,A8=2724,A9=3024,A10=3324, A11=3624,A12=3924,A13=4224,A14=4524,A15=4824, INDX_X1=584,INDX_X2=586,INDX_X3=588,INDX_Y1=585,INDX_Y2=587,INDX_Y3=589,INDX_CD0=596,INDX_CD1=597,N=24")



### Cell 28
dbLoadRecords("../../db/aie.db", "P=$(P1), U=7, ID=28,  A1=628, A2=928, A3=1228,A4=1528,A5=1828,A6=2128,A7=2428,A8=2728,A9=3028,A10=3328, A11=3628,A12=3928,A13=4228,A14=4528,A15=4828, INDX_X1=714,INDX_X2=716,INDX_X3=718,INDX_Y1=715,INDX_Y2=717,INDX_Y3=719,INDX_CD0=726,INDX_CD1=727,N=28")


### Cell 8
dbLoadRecords("../../db/aie.db", "P=$(P1), U=8, ID=8,  A1=632, A2=932, A3=1232,A4=1532,A5=1832,A6=2132,A7=2432,A8=2732,A9=3032,A10=3332, A11=3632,A12=3932,A13=4232,A14=4532,A15=4832, INDX_X1=194,INDX_X2=196,INDX_X3=198,INDX_Y1=195,INDX_Y2=197,INDX_Y3=199,INDX_CD0=206,INDX_CD1=207,N=32")
### Cell 18
dbLoadRecords("../../db/aie.db", "P=$(P1), U=9, ID=18, A1=636, A2=936, A3=1236,A4=1536,A5=1836,A6=2136,A7=2436,A8=2736,A9=3036,A10=3336, A11=3636,A12=3936,A13=4236,A14=4536,A15=4836, INDX_X1=454,INDX_X2=456,INDX_X3=458,INDX_Y1=455,INDX_Y2=457,INDX_Y3=459,INDX_CD0=466,INDX_CD1=467,N=36")





var(PSCDebug, 2)	#5 full debug

createPSC("aie_tx", $(C31_IP), 7, 0)
#setPSCSendBlockSize("aie_tx", 1, 720)

createPSC("aie_wfm_rx", $(C31_IP), 20, 1)
createPSC("Rx1", $(C31_IP), 600, 1)

iocInit()

epicsThreadSleep 3
# Trigger 1 delay just for C31 if Cell controller delay is 1000
dbpf SR:C31-{AI}Evr:Trig1_Dly-SP, 1
#
#dbpf SR:C31-{AI}Bm_LowOffset-SP, -5
#dbpf SR:C31-{AI}Bm_HiOffset-SP, 5
#
dbpf SR:C31-{AI}Aie3:Logic-SP, 2
dbpf SR:C31-{AI}Aie5:Logic-SP, 2
dbpf SR:C31-{AI}Aie52:Logic-SP, 2
dbpf SR:C31-{AI}Aie10:Logic-SP, 2
dbpf SR:C31-{AI}Aie11:Logic-SP, 2
dbpf SR:C31-{AI}Aie23:Logic-SP, 2
dbpf SR:C31-{AI}Aie28:Logic-SP, 2
dbpf SR:C31-{AI}Aie8:Logic-SP, 2


#
dbpf SR:C31-{AI}Aie3:S1-SP, -2.543
dbpf SR:C31-{AI}Aie3:S3-SP, 0
dbpf SR:C31-{AI}Aie3:S2-SP, 2.679

dbpf SR:C31-{AI}Aie5:S1-SP, -2.543
dbpf SR:C31-{AI}Aie5:S3-SP, 0
dbpf SR:C31-{AI}Aie5:S2-SP, 2.679
###
dbpf SR:C31-{AI}Aie52:S1-SP, -2.543
dbpf SR:C31-{AI}Aie52:S3-SP, 0
dbpf SR:C31-{AI}Aie52:S2-SP, 2.679
#
dbpf SR:C31-{AI}Aie11:S1-SP, -2.543
dbpf SR:C31-{AI}Aie11:S3-SP, 0
dbpf SR:C31-{AI}Aie11:S2-SP, 2.679
#
dbpf SR:C31-{AI}Aie23:S1-SP, -2.543
dbpf SR:C31-{AI}Aie23:S3-SP, 0
dbpf SR:C31-{AI}Aie23:S2-SP, 2.679
#
dbpf SR:C31-{AI}Aie28:S1-SP, -2.543
dbpf SR:C31-{AI}Aie28:S3-SP, 0
dbpf SR:C31-{AI}Aie28:S2-SP, 2.679
################


dbpf SR:C31-{AI}Aie3:AIOL-H1-SP, 0
dbpf SR:C31-{AI}Aie3:AIOL-H2-SP, 0
dbpf SR:C31-{AI}Aie3:AIOL-H3-SP, 0.5
dbpf SR:C31-{AI}Aie3:AIOL-V1-SP, 0
dbpf SR:C31-{AI}Aie3:AIOL-V2-SP, 0 
dbpf SR:C31-{AI}Aie3:AIOL-V3-SP, 0.5

dbpf SR:C31-{AI}Aie5:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie5:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie5:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie5:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie5:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie5:AIOL-V3-SP, 5

dbpf SR:C31-{AI}Aie52:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie52:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie52:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie52:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie52:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie52:AIOL-V3-SP, 5



dbpf SR:C31-{AI}Aie10:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie10:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie10:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie10:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie10:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie10:AIOL-V3-SP, 5

dbpf SR:C31-{AI}Aie11:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie11:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie11:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie11:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie11:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie11:AIOL-V3-SP, 5

dbpf SR:C31-{AI}Aie23:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie23:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie23:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie23:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie23:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie23:AIOL-V3-SP, 5


dbpf SR:C31-{AI}Aie28:AIOL-H1-SP, 5
dbpf SR:C31-{AI}Aie28:AIOL-H2-SP, 5
dbpf SR:C31-{AI}Aie28:AIOL-H3-SP, 5
dbpf SR:C31-{AI}Aie28:AIOL-V1-SP, 5
dbpf SR:C31-{AI}Aie28:AIOL-V2-SP, 5
dbpf SR:C31-{AI}Aie28:AIOL-V3-SP, 5



###########
dbpf SR:C31-{AI}Aie3:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie3:Rec-Ymrad-SP, 0.25
###
dbpf SR:C31-{AI}Aie5:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie5:Rec-Ymrad-SP, 0.25
#

###
dbpf SR:C31-{AI}Aie52:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie52:Rec-Ymrad-SP, 0.25
#


###
dbpf SR:C31-{AI}Aie10:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie10:Rec-Ymrad-SP, 0.25
#
dbpf SR:C31-{AI}Aie10:S1-SP, -2.543
dbpf SR:C31-{AI}Aie10:S3-SP, 0
dbpf SR:C31-{AI}Aie10:S2-SP, 2.679
###

dbpf SR:C31-{AI}Aie11:Rec-Yoff-SP, 0.5
dbpf SR:C31-{AI}Aie11:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie11:Rec-Ymrad-SP, 0.25
#

###

dbpf SR:C31-{AI}Aie23:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie23:Rec-Ymrad-SP, 0.25
#


### C28
dbpf SR:C31-{AI}Aie28:Rec-Xmrad-SP, 0.25
dbpf SR:C31-{AI}Aie28:Rec-Ymrad-SP, 0.25
#

dbpf SR:C31-{AI}SR-BPM:Xoff-SP 5
dbpf SR:C31-{AI}SR-BPM:Yoff-SP 3
dbpf SR:C31-{AI}ID:MaskEnable1-SP 3
dbpf SR:C31-{AI}PlcIdDump-SP 0

dbpf SR:C31-{AI}Sim:Enable-SP 1
dbpf SR:C31-{AI}Sim:BeamTest-SP 1

