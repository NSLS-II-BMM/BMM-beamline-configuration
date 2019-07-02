#!../../bin/linux-x86-debug/psc

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","10000000")

dbLoadDatabase("../../dbd/psc.dbd",0,0)
psc_registerRecordDeviceDriver(pdbbase) 

## Load record instances
#dbLoadRecords("test.db", "P=TST:,NELM=100000,FLNK=TST:In-SP")
dbLoadRecords("../../db/psc-psd.db","P=TST:,NELM=1000000,FLNK=TST:stat:Stats-Calc_,INP=BR-PS{PS:BD1}I:DCCT2-I CP")
dbLoadRecords("../../db/psc-stats.db", "P=TST:stat:,NELM=1000000,DATAY=TST:In-SP")

#set_savefile_path("${PWD}/as","/save")
#set_requestfile_path("${PWD}/as","/req")
#system("install -m 777 -d ${PWD}/as/save")
#system("install -m 777 -d ${PWD}/as/req")

#set_pass0_restoreFile("ioc_settings.sav")

iocInit()

#makeAutosaveFileFromDbInfo("as/req/ioc_settings.req", "autosaveFields_pass0")
#create_monitor_set("ioc_settings.req", 5, "")
