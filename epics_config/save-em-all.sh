#!/bin/bash
suffix=${1:-RBV}
echo "# Restore all axes: .$suffix"

function do_caget {
    if [ $suffix == 'VAL' ]; then
	echo -n "caput "
    fi
    caget $1
}

all="XF:06BMA-OP{Mir:M3-Ax:YU}Mtr
XF:06BMA-OP{Mir:M3-Ax:YDO}Mtr
XF:06BMA-OP{Mir:M3-Ax:YDI}Mtr
XF:06BMA-OP{Mir:M3-Ax:XU}Mtr
XF:06BMA-OP{Mir:M3-Ax:XD}Mtr
XF:06BM-BI{FS:03-Ax:Y}Mtr
XF:06BM-OP{Mir:M1-Ax:YU}Mtr
XF:06BM-OP{Mir:M1-Ax:YDO}Mtr
XF:06BM-OP{Mir:M1-Ax:YDI}Mtr
XF:06BM-OP{Mir:M1-Ax:XU}Mtr
XF:06BM-OP{Mir:M1-Ax:XD}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:Bragg2}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr
XF:06BMA-OP{Mono:DCM1-Ax:Y}Mtr
XF:06BMA-OP{Slt:01-Ax:O}Mtr
XF:06BMA-OP{Slt:01-Ax:I}Mtr
XF:06BMA-OP{Slt:01-Ax:T}Mtr
XF:06BMA-OP{Slt:01-Ax:B}Mtr
XF:06BMA-OP{Mir:M2-Ax:YU}Mtr
XF:06BMA-OP{Mir:M2-Ax:YDO}Mtr
XF:06BMA-OP{Mir:M2-Ax:YDI}Mtr
XF:06BMA-OP{Mir:M2-Ax:XU}Mtr
XF:06BMA-OP{Mir:M2-Ax:XD}Mtr
XF:06BMA-OP{Mir:M2-Ax:Bend}Mtr
XF:06BMA-BI{Diag:02-Ax:Y}Mtr
XF:06BMA-BI{Fltr:01-Ax:Y1}Mtr
XF:06BMA-BI{Fltr:01-Ax:Y2}Mtr
XF:06BM-BI{Fltr:01-Ax:Y}Mtr
XF:06BM-BI{BPM:1-Ax:Y}Mtr
XF:06BM-BI{BCT-Ax:Y}Mtr
XF:06BM-BI{Slt:02-Ax:O}Mtr
XF:06BM-BI{Slt:02-Ax:I}Mtr
XF:06BM-BI{Slt:02-Ax:T}Mtr
XF:06BM-BI{Slt:02-Ax:B}Mtr
"

for axis in $all; do
    do_caget $axis.$suffix
done


# ## Mirror M3
# do_caget XF:06BMA-OP{Mir:M3-Ax:YU}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M3-Ax:YDO}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M3-Ax:YDI}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M3-Ax:XU}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M3-Ax:XD}Mtr.$suffix
# ## end station fluorescent screen
# do_caget XF:06BM-BI{FS:03-Ax:Y}Mtr.$suffix
# ## Mirror M1
# do_caget XF:06BM-OP{Mir:M1-Ax:YU}Mtr.$suffix
# do_caget XF:06BM-OP{Mir:M1-Ax:YDO}Mtr.$suffix
# do_caget XF:06BM-OP{Mir:M1-Ax:YDI}Mtr.$suffix
# do_caget XF:06BM-OP{Mir:M1-Ax:XU}Mtr.$suffix
# do_caget XF:06BM-OP{Mir:M1-Ax:XD}Mtr.$suffix
# ## DCM
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:Bragg}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:Bragg2}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:P2}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:R2}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:Per2}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:Par2}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:X}Mtr.$suffix
# do_caget XF:06BMA-OP{Mono:DCM1-Ax:Y}Mtr.$suffix
# ## DM2 slits (slits 1)
# do_caget XF:06BMA-OP{Slt:01-Ax:O}Mtr.$suffix
# do_caget XF:06BMA-OP{Slt:01-Ax:I}Mtr.$suffix
# do_caget XF:06BMA-OP{Slt:01-Ax:T}Mtr.$suffix
# do_caget XF:06BMA-OP{Slt:01-Ax:B}Mtr.$suffix
# ## Mirror M2
# do_caget XF:06BMA-OP{Mir:M2-Ax:YU}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M2-Ax:YDO}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M2-Ax:YDI}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M2-Ax:XU}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M2-Ax:XD}Mtr.$suffix
# do_caget XF:06BMA-OP{Mir:M2-Ax:Bend}Mtr.$suffix
# ## DM2 fluorescent screen and foils
# do_caget XF:06BMA-BI{Diag:02-Ax:Y}Mtr.$suffix
# ## filter assembly
# do_caget XF:06BMA-BI{Fltr:01-Ax:Y1}Mtr.$suffix
# do_caget XF:06BMA-BI{Fltr:01-Ax:Y2}Mtr.$suffix
# ## foil rack in DM3
# do_caget XF:06BM-BI{Fltr:01-Ax:Y}Mtr.$suffix
# ## NanoBPM
# do_caget XF:06BM-BI{BPM:1-Ax:Y}Mtr.$suffix
# ## DM3 back plate
# do_caget XF:06BM-BI{BCT-Ax:Y}Mtr.$suffix
# ## DM3 slits (slits 2)
# do_caget XF:06BM-BI{Slt:02-Ax:O}Mtr.$suffix
# do_caget XF:06BM-BI{Slt:02-Ax:I}Mtr.$suffix
# do_caget XF:06BM-BI{Slt:02-Ax:T}Mtr.$suffix
# do_caget XF:06BM-BI{Slt:02-Ax:B}Mtr.$suffix
