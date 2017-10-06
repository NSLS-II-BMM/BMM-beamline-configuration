rm -rf opi_genericScan
rm -rf opi_uIOCSystem
rm -rf *.edl~
rm -rf *.sh~
ln -s /opt/epics/modules/uIOCSystem/opi_uIOCSystem opi_uIOCSystem
ln -s /opt/epics/modules/genericScan/opi_genericScan opi_genericScan
#ln -s /opt/epics/modules/PI_E625/opi_PI_E625 opi_PI_E625
rm -rf /opt/epics/iocoutput/autosave/*.*
