#!/bin/bash
suffix=${1:-RBV}

# caget -t FE:C06B-OP{Slt:12-Ax:X}size
# caget -t FE:C06B-OP{Slt:12-Ax:X}center
# caget -t FE:C06B-OP{Slt:12-Ax:Y}size
# caget -t FE:C06B-OP{Slt:12-Ax:Y}center
# caget -t FE:C06B-OP{Slt:1-Ax:Hrz}Mtr.VAL
# caget -t FE:C06B-OP{Slt:1-Ax:Inc}Mtr.VAL
# caget -t FE:C06B-OP{Slt:1-Ax:O}Mtr.VAL
# caget -t FE:C06B-OP{Slt:1-Ax:T}Mtr.VAL
# caget -t FE:C06B-OP{Slt:2-Ax:Hrz}Mtr.VAL
# caget -t FE:C06B-OP{Slt:2-Ax:Inc}Mtr.VAL
# caget -t FE:C06B-OP{Slt:2-Ax:I}Mtr.VAL
# caget -t FE:C06B-OP{Slt:2-Ax:B}Mtr.VAL
# caget -t XF:06BM-OP{Mir:M1-Ax:YU}Mtr.$suffix
# caget -t XF:06BM-OP{Mir:M1-Ax:YDO}Mtr.$suffix
# caget -t XF:06BM-OP{Mir:M1-Ax:YDI}Mtr.$suffix
# caget -t XF:06BM-OP{Mir:M1-Ax:XU}Mtr.$suffix
# caget -t XF:06BM-OP{Mir:M1-Ax:XD}Mtr.$suffix
# caget -t XF:06BMA-BI{Fltr:01-Ax:Y1}Mtr.$suffix
# caget -t XF:06BMA-BI{Fltr:01-Ax:Y2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:Bragg2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr.$suffix
# caget -t XF:06BMA-OP{Mono:DCM1-Ax:Y}Mtr.$suffix
# caget -t XF:06BMA-OP{Slt:01-Ax:O}Mtr.$suffix
# caget -t XF:06BMA-OP{Slt:01-Ax:I}Mtr.$suffix
# caget -t XF:06BMA-OP{Slt:01-Ax:T}Mtr.$suffix
# caget -t XF:06BMA-OP{Slt:01-Ax:B}Mtr.$suffix
# caget -t XF:06BMA-BI{Diag:02-Ax:Y}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:YU}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:YDO}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:YDI}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:XU}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:XD}Mtr.$suffix
caget -t XF:06BMA-OP{Mir:M2-Ax:Bend}Mtr.$suffix
# caget -t XF:06BMA-OP{Mir:M3-Ax:YU}Mtr.$suffix
# caget -t XF:06BMA-OP{Mir:M3-Ax:YDO}Mtr.$suffix
# caget -t XF:06BMA-OP{Mir:M3-Ax:YDI}Mtr.$suffix
# caget -t XF:06BMA-OP{Mir:M3-Ax:XU}Mtr.$suffix
# caget -t XF:06BMA-OP{Mir:M3-Ax:XD}Mtr.$suffix
# caget -t XF:06BM-BI{FS:03-Ax:Y}Mtr.$suffix
# caget -t XF:06BM-BI{Slt:02-Ax:O}Mtr.$suffix
# caget -t XF:06BM-BI{Slt:02-Ax:I}Mtr.$suffix
# caget -t XF:06BM-BI{Slt:02-Ax:T}Mtr.$suffix
# caget -t XF:06BM-BI{Slt:02-Ax:B}Mtr.$suffix
# caget -t XF:06BM-BI{Fltr:01-Ax:Y}Mtr.$suffix
# caget -t XF:06BM-BI{BCT-Ax:Y}Mtr.$suffix
# caget -t XF:06BM-BI{BPM:1-Ax:Y}Mtr.$suffix
# caget -t XF:06BM-PPS{Sh:FE}Pos-Sts
# caget -t XF:06BM-PPS{Sh:A}Pos-Sts
# caget -t XF:06BMA-OP{FS:1}Pos-Sts
