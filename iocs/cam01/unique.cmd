#Prosilica GC1290/GT1290: 1280 * 960  = 1228800; MAX_ARRAY = 2457600 Bytes
#Prosilica Mako G-125B:   1292 * 964  = 1245488; MAX_ARRAY = 2490976 Bytes
#Prosilica GX1920:        1936 * 1456 = 2818816; MAX_ARRAY = 5637632 Bytes

epicsEnvSet("ENGINEER",                 "ZY, x5525")
epicsEnvSet("LOCATION",                 "06BM")
epicsEnvSet("TOP",                      "${PWD}")
epicsEnvSet("PORT",                     "CAM")

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST",  "NO")
epicsEnvSet("EPICS_CA_ADDR_LIST",       "10.6.128.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "50000000")

epicsEnvSet("CAM-IP",                   "10.6.129.51")
epicsEnvSet("PREFIX",                   "XF:06BM-BI{Scr:1}")
epicsEnvSet("CTPREFIX",                 "XF:06BM-CT{IOC:cam01}")
epicsEnvSet("HOSTNAME",                 "xf06bm-ioc1")
epicsEnvSet("IOCNAME",                  "cam01")

epicsEnvSet("QSIZE",                    "20")
epicsEnvSet("NCHANS",                   "2048")
epicsEnvSet("HIST_SIZE",                "4096")
epicsEnvSet("XSIZE",                    "1280")
epicsEnvSet("YSIZE",                    "960")
epicsEnvSet("NELMT",                    "2457600")
epicsEnvSet("NDTYPE",                   "Int16") #Int8
epicsEnvSet("NDFTVL",                   "SHORT") #UCHAR

