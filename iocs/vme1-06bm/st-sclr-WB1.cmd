epicsEnvSet("SYS",                      "XF:06BM-ES:1")
epicsEnvSet("DEV",                      "{Sclr:1}")
epicsEnvSet("RNAME",                    "mca")
epicsEnvSet("MAX_SIGNALS",              "32")
epicsEnvSet("MAX_CHANS",                "10000")
#epicsEnvSet("MAX_CHANS",                "2048")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "8400000")
epicsEnvSet("PORT",                     "SIS3820/1")
# For MCA records FIELD=READ, for waveform records FIELD=PROC
epicsEnvSet("FIELD",                    "READ")
epicsEnvSet("MODEL",                    "SIS3820")
epicsEnvSet("MCA",                      "mca")

#drvSIS3820Config("Port name",
#                  baseAddress,
#                  interruptVector,
#                  int interruptLevel,
#                  channels,
#                  signals,
#                  use DMA
#                  fifoBufferWords)
drvSIS3820Config($(PORT), 0x22000000, 224, 6, $(MAX_CHANS), $(MAX_SIGNALS), 1, 0x20000)

# This loads the scaler record and supporting records
dbLoadRecords("db/scaler32.db", "P=$(SYS), S=$(DEV), DTYP=Asyn Scaler, OUT=@asyn($(PORT)), FREQ=50000000")

# This database provides the support for the MCS functions
dbLoadRecords("db/SIS38XX.template", "P=$(SYS)$(DEV), PORT=$(PORT), SCALER=$(SYS)$(DEV)scaler1")

# Load either MCA or waveform records below
# The number of records loaded must be the same as MAX_SIGNALS defined above
# Load the MCA records
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)1,  DTYP=asynMCA, INP=@asyn($(PORT) 0),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)2,  DTYP=asynMCA, INP=@asyn($(PORT) 1),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)3,  DTYP=asynMCA, INP=@asyn($(PORT) 2),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)4,  DTYP=asynMCA, INP=@asyn($(PORT) 3),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)5,  DTYP=asynMCA, INP=@asyn($(PORT) 4),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)6,  DTYP=asynMCA, INP=@asyn($(PORT) 5),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)7,  DTYP=asynMCA, INP=@asyn($(PORT) 6),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)8,  DTYP=asynMCA, INP=@asyn($(PORT) 7),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)9,  DTYP=asynMCA, INP=@asyn($(PORT) 8),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)10,  DTYP=asynMCA, INP=@asyn($(PORT) 9),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)11,  DTYP=asynMCA, INP=@asyn($(PORT) 10),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)12,  DTYP=asynMCA, INP=@asyn($(PORT) 11),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)13,  DTYP=asynMCA, INP=@asyn($(PORT) 12),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)14,  DTYP=asynMCA, INP=@asyn($(PORT) 13),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)15,  DTYP=asynMCA, INP=@asyn($(PORT) 14),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)16,  DTYP=asynMCA, INP=@asyn($(PORT) 15),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)17,  DTYP=asynMCA, INP=@asyn($(PORT) 16),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)18,  DTYP=asynMCA, INP=@asyn($(PORT) 17),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)19,  DTYP=asynMCA, INP=@asyn($(PORT) 18),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)20,  DTYP=asynMCA, INP=@asyn($(PORT) 19),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)21,  DTYP=asynMCA, INP=@asyn($(PORT) 20),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)22,  DTYP=asynMCA, INP=@asyn($(PORT) 21),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)23,  DTYP=asynMCA, INP=@asyn($(PORT) 22),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)24,  DTYP=asynMCA, INP=@asyn($(PORT) 23),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)25,  DTYP=asynMCA, INP=@asyn($(PORT) 24),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)26,  DTYP=asynMCA, INP=@asyn($(PORT) 25),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)27,  DTYP=asynMCA, INP=@asyn($(PORT) 26),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)28,  DTYP=asynMCA, INP=@asyn($(PORT) 27),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)29,  DTYP=asynMCA, INP=@asyn($(PORT) 28),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)30,  DTYP=asynMCA, INP=@asyn($(PORT) 29),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)31,  DTYP=asynMCA, INP=@asyn($(PORT) 30),  PREC=3, CHANS=$(MAX_CHANS)")
dbLoadRecords("$(MCA)/db/simple_mca.db", "P=$(SYS)$(DEV), M=$(RNAME)32,  DTYP=asynMCA, INP=@asyn($(PORT) 31),  PREC=3, CHANS=$(MAX_CHANS)")

# This loads the waveform records
#dbLoadRecords("$(MCA)/db/SIS38XX_waveform.template", "P=$(SYS), R=$(DEV),  INP=@asyn($(PORT) 0),  CHANS=$(MAX_CHANS)")

#asynSetTraceIOMask($(PORT),0,2)
#asynSetTraceFile("$(PORT)",0,"$(MODEL).out")
#asynSetTraceMask("$(PORT)",0,0xff)

