TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
DB += SAI_Global.db
DB += SAI_Global.substitutions
DB += SAI_8MotorStatus.db
DB += SAI_8MotorStatus.substitutions
DB += SAI_SingleMotorStatus.template
DB += SAI_SingleMotorStatus.substitutions
DB += SAI_MotorRecord.template
DB += SAI_MotorRecord.substitutions
DB += SAI_MotorHoming.template
DB += SAI_MotorHoming.substitutions
DB += SAI_EncoderLoss.template
DB += SAI_EncoderLoss.substitutions
DB += SAI_DigitalChannels.template
DB += SAI_DigitalChannels.substitutions
##foreign modules
#external module: uIOCsystem
DB += SAI_IOCsystem.substitutions
#external  module: generic-scan
DB += SAI_generic_scan.substitutions
DB += SAI_GSCAN_Saver.substitutions
DB += SAI_save_restoreStatus.substitutions


#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
#EOF
