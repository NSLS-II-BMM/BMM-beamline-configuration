# Makefie for creating PMAC programs
#
TOP = ../..
PMACUTIL=/usr/share/epics-pmacutil-dev/pmc
include $(TOP)/configure/CONFIG
include $(TOP)/configure/CONFIG_PMC

PMC += xf06BM-mcc12-homing.pmc
PMC += xf06BM-mcc12-plc03-brake.pmc
PMC += xf06BM-mcc12-plc05-cpu.pmc
PMC_INSTALLS += xf06BM-mcc12-plc01-init.pmc
PMC_INSTALLS += xf06BM-mcc12-plc07-power-down.pmc
PMC_TEMPLATES += $(PMACUTIL)/PLC_cpu_load.pmc
PMC_TEMPLATES += $(PMACUTIL)/home_to_enc_ref_template.pmc
PMC_TEMPLATES += $(PMACUTIL)/home_to_limit_template.pmc

include $(TOP)/configure/RULES_PMC
