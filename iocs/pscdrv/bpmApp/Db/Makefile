TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
DB += iocAdminSoft.db
DB += save_restoreStatus.db
DB += bpm.db
DB += bpmpsd.db
DB += cc.db
DB += fofb.db
DB += ActiveInterlock.db
DB += aie.db
DB += aie_din.db
DB += aie_fpga_cal.db
DB += cc_sdi_pos.db
DB += bpm_alarm_sumery.db
DB += bpm_id23_alarm_sum.db
DB += ai_xy_pos.db
DB += ai_fail_safe.db
DB += ai_bpm_pos_erri_cal.db

DB += bpm_pos_alarm_sumery.db
DB += bpm_id_pos_alarm_sumery.db
DB += z100_sa.db
DB += ai_sa_angle_cal.db
DB += cc_pm_wfm.db
DB += cc_orbit.db
DB += z100_wfm.db
DB += z100_bpm.db


### Xbpm db
DB += xbpm_blade.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

