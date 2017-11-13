#!/usr/bin/env python

## cat pvsave.json | jq '.[\"XF:06BM-BI{BCT-Ax:Y}Mtr\"]

import epics
import json

motors = ("XF:06BMA-OP{Mir:M3-Ax:YU}Mtr",
          "XF:06BMA-OP{Mir:M3-Ax:YDO}Mtr",
          "XF:06BMA-OP{Mir:M3-Ax:YDI}Mtr",
          "XF:06BMA-OP{Mir:M3-Ax:XU}Mtr",
          "XF:06BMA-OP{Mir:M3-Ax:XD}Mtr",
          "XF:06BM-BI{FS:03-Ax:Y}Mtr",
          "XF:06BM-OP{Mir:M1-Ax:YU}Mtr",
          "XF:06BM-OP{Mir:M1-Ax:YDO}Mtr",
          "XF:06BM-OP{Mir:M1-Ax:YDI}Mtr",
          "XF:06BM-OP{Mir:M1-Ax:XU}Mtr",
          "XF:06BM-OP{Mir:M1-Ax:XD}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:Bragg2}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr",
          "XF:06BMA-OP{Mono:DCM1-Ax:Y}Mtr",
          "XF:06BMA-OP{Slt:01-Ax:O}Mtr",
          "XF:06BMA-OP{Slt:01-Ax:I}Mtr",
          "XF:06BMA-OP{Slt:01-Ax:T}Mtr",
          "XF:06BMA-OP{Slt:01-Ax:B}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:YU}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:YDO}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:YDI}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:XU}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:XD}Mtr",
          "XF:06BMA-OP{Mir:M2-Ax:Bend}Mtr",
          "XF:06BMA-BI{Diag:02-Ax:Y}Mtr",
          "XF:06BMA-BI{Fltr:01-Ax:Y1}Mtr",
          "XF:06BMA-BI{Fltr:01-Ax:Y2}Mtr",
          "XF:06BM-BI{Fltr:01-Ax:Y}Mtr",
          "XF:06BM-BI{BPM:1-Ax:Y}Mtr",
          "XF:06BM-BI{BCT-Ax:Y}Mtr",
          "XF:06BM-BI{Slt:02-Ax:O}Mtr",
          "XF:06BM-BI{Slt:02-Ax:I}Mtr",
          "XF:06BM-BI{Slt:02-Ax:T}Mtr",
          "XF:06BM-BI{Slt:02-Ax:B}Mtr",)

fields = ( "ACCL", "MRES", "BACC", "MSTA", "BDST", "OFF", "BVEL",
           "OMSL", "CARD", "OUT", "DHLM", "PCOF", "DIR", "PREC", "DLLM",
           "RBV", "DLY", "RTRY", "DMOV", "RCNT", "DRBV", "RDBD", "DESC",
           "RDIF", "DVAL", "REP", "EGU", "RHLS", "ERES", "RLLS", "FOFF",
           "RLV", "FRAC", "RMP", "HHSV", "RRBV", "HIGH", "RRES", "HIHI",
           "RVAL", "HLM", "RVEL", "HLS", "S", "HLSV", "SBAK", "HOMF", "SBAS",
           "HOMR", "SMAX", "HOPR", "SET", "HSV", "SPMG", "ICOF", "SREV",
           "JAR", "STOP", "JOGF", "TDIR", "JOGR", "TWF", "JVEL", "TWR",
           "LDVL", "TWV", "LLM", "UEIP", "LLS", "UREV", "LLSV", "URIP",
           "LOLO", "VAL", "LOPR", "VBAS", "LOW", "VELO", "LRLV", "VERS",
           "LRVL", "VMAX", "LSPG", "ATHM", "LSV", "DCOF",)

collate = dict()

for m in motors:
    pv = epics.Motor(m)
    print "Querying %s:\t%s" % (m, pv.DESC)
    this = dict()
    for f in fields:
        this[f] = pv.get(f)
    collate[m] = this

file = open("pvsave.json", "w") 
file.write(json.dumps(collate, sort_keys=True, indent=4, separators=(',', ': ')))
file.close()

print "you can query the json file like so:"
print "  cat pvsave.json | jq '.[\"XF:06BM-BI{BCT-Ax:Y}Mtr\"]"
