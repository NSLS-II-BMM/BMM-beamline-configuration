/* THIS IS A GENERATED FILE. DO NOT EDIT! */
/* Generated from ../O.Common/vme.dbd */

#include <string.h>

#include "epicsStdlib.h"
#include "iocsh.h"
#include "iocshRegisterCommon.h"
#include "registryCommon.h"

extern "C" {

epicsShareExtern rset *pvar_rset_aaiRSET;
epicsShareExtern int (*pvar_func_aaiRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_aaoRSET;
epicsShareExtern int (*pvar_func_aaoRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_aiRSET;
epicsShareExtern int (*pvar_func_aiRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_aoRSET;
epicsShareExtern int (*pvar_func_aoRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_aSubRSET;
epicsShareExtern int (*pvar_func_aSubRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_biRSET;
epicsShareExtern int (*pvar_func_biRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_boRSET;
epicsShareExtern int (*pvar_func_boRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_calcRSET;
epicsShareExtern int (*pvar_func_calcRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_calcoutRSET;
epicsShareExtern int (*pvar_func_calcoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_compressRSET;
epicsShareExtern int (*pvar_func_compressRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_dfanoutRSET;
epicsShareExtern int (*pvar_func_dfanoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_eventRSET;
epicsShareExtern int (*pvar_func_eventRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_fanoutRSET;
epicsShareExtern int (*pvar_func_fanoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_histogramRSET;
epicsShareExtern int (*pvar_func_histogramRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_longinRSET;
epicsShareExtern int (*pvar_func_longinRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_longoutRSET;
epicsShareExtern int (*pvar_func_longoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_mbbiRSET;
epicsShareExtern int (*pvar_func_mbbiRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_mbbiDirectRSET;
epicsShareExtern int (*pvar_func_mbbiDirectRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_mbboRSET;
epicsShareExtern int (*pvar_func_mbboRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_mbboDirectRSET;
epicsShareExtern int (*pvar_func_mbboDirectRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_permissiveRSET;
epicsShareExtern int (*pvar_func_permissiveRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_selRSET;
epicsShareExtern int (*pvar_func_selRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_seqRSET;
epicsShareExtern int (*pvar_func_seqRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_stateRSET;
epicsShareExtern int (*pvar_func_stateRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_stringinRSET;
epicsShareExtern int (*pvar_func_stringinRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_stringoutRSET;
epicsShareExtern int (*pvar_func_stringoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_subRSET;
epicsShareExtern int (*pvar_func_subRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_subArrayRSET;
epicsShareExtern int (*pvar_func_subArrayRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_waveformRSET;
epicsShareExtern int (*pvar_func_waveformRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_mcaRSET;
epicsShareExtern int (*pvar_func_mcaRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_transformRSET;
epicsShareExtern int (*pvar_func_transformRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_scalcoutRSET;
epicsShareExtern int (*pvar_func_scalcoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_acalcoutRSET;
epicsShareExtern int (*pvar_func_acalcoutRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_sseqRSET;
epicsShareExtern int (*pvar_func_sseqRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_swaitRSET;
epicsShareExtern int (*pvar_func_swaitRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_scanparmRSET;
epicsShareExtern int (*pvar_func_scanparmRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_sscanRSET;
epicsShareExtern int (*pvar_func_sscanRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_scalerRSET;
epicsShareExtern int (*pvar_func_scalerRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_epidRSET;
epicsShareExtern int (*pvar_func_epidRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_timestampRSET;
epicsShareExtern int (*pvar_func_timestampRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_asynRSET;
epicsShareExtern int (*pvar_func_asynRecordSizeOffset)(dbRecordType *pdbRecordType);
epicsShareExtern rset *pvar_rset_busyRSET;
epicsShareExtern int (*pvar_func_busyRecordSizeOffset)(dbRecordType *pdbRecordType);

static const char * const recordTypeNames[42] = {
    "aai",
    "aao",
    "ai",
    "ao",
    "aSub",
    "bi",
    "bo",
    "calc",
    "calcout",
    "compress",
    "dfanout",
    "event",
    "fanout",
    "histogram",
    "longin",
    "longout",
    "mbbi",
    "mbbiDirect",
    "mbbo",
    "mbboDirect",
    "permissive",
    "sel",
    "seq",
    "state",
    "stringin",
    "stringout",
    "sub",
    "subArray",
    "waveform",
    "mca",
    "transform",
    "scalcout",
    "acalcout",
    "sseq",
    "swait",
    "scanparm",
    "sscan",
    "scaler",
    "epid",
    "timestamp",
    "asyn",
    "busy"
};

static const recordTypeLocation rtl[42] = {
    {pvar_rset_aaiRSET, pvar_func_aaiRecordSizeOffset},
    {pvar_rset_aaoRSET, pvar_func_aaoRecordSizeOffset},
    {pvar_rset_aiRSET, pvar_func_aiRecordSizeOffset},
    {pvar_rset_aoRSET, pvar_func_aoRecordSizeOffset},
    {pvar_rset_aSubRSET, pvar_func_aSubRecordSizeOffset},
    {pvar_rset_biRSET, pvar_func_biRecordSizeOffset},
    {pvar_rset_boRSET, pvar_func_boRecordSizeOffset},
    {pvar_rset_calcRSET, pvar_func_calcRecordSizeOffset},
    {pvar_rset_calcoutRSET, pvar_func_calcoutRecordSizeOffset},
    {pvar_rset_compressRSET, pvar_func_compressRecordSizeOffset},
    {pvar_rset_dfanoutRSET, pvar_func_dfanoutRecordSizeOffset},
    {pvar_rset_eventRSET, pvar_func_eventRecordSizeOffset},
    {pvar_rset_fanoutRSET, pvar_func_fanoutRecordSizeOffset},
    {pvar_rset_histogramRSET, pvar_func_histogramRecordSizeOffset},
    {pvar_rset_longinRSET, pvar_func_longinRecordSizeOffset},
    {pvar_rset_longoutRSET, pvar_func_longoutRecordSizeOffset},
    {pvar_rset_mbbiRSET, pvar_func_mbbiRecordSizeOffset},
    {pvar_rset_mbbiDirectRSET, pvar_func_mbbiDirectRecordSizeOffset},
    {pvar_rset_mbboRSET, pvar_func_mbboRecordSizeOffset},
    {pvar_rset_mbboDirectRSET, pvar_func_mbboDirectRecordSizeOffset},
    {pvar_rset_permissiveRSET, pvar_func_permissiveRecordSizeOffset},
    {pvar_rset_selRSET, pvar_func_selRecordSizeOffset},
    {pvar_rset_seqRSET, pvar_func_seqRecordSizeOffset},
    {pvar_rset_stateRSET, pvar_func_stateRecordSizeOffset},
    {pvar_rset_stringinRSET, pvar_func_stringinRecordSizeOffset},
    {pvar_rset_stringoutRSET, pvar_func_stringoutRecordSizeOffset},
    {pvar_rset_subRSET, pvar_func_subRecordSizeOffset},
    {pvar_rset_subArrayRSET, pvar_func_subArrayRecordSizeOffset},
    {pvar_rset_waveformRSET, pvar_func_waveformRecordSizeOffset},
    {pvar_rset_mcaRSET, pvar_func_mcaRecordSizeOffset},
    {pvar_rset_transformRSET, pvar_func_transformRecordSizeOffset},
    {pvar_rset_scalcoutRSET, pvar_func_scalcoutRecordSizeOffset},
    {pvar_rset_acalcoutRSET, pvar_func_acalcoutRecordSizeOffset},
    {pvar_rset_sseqRSET, pvar_func_sseqRecordSizeOffset},
    {pvar_rset_swaitRSET, pvar_func_swaitRecordSizeOffset},
    {pvar_rset_scanparmRSET, pvar_func_scanparmRecordSizeOffset},
    {pvar_rset_sscanRSET, pvar_func_sscanRecordSizeOffset},
    {pvar_rset_scalerRSET, pvar_func_scalerRecordSizeOffset},
    {pvar_rset_epidRSET, pvar_func_epidRecordSizeOffset},
    {pvar_rset_timestampRSET, pvar_func_timestampRecordSizeOffset},
    {pvar_rset_asynRSET, pvar_func_asynRecordSizeOffset},
    {pvar_rset_busyRSET, pvar_func_busyRecordSizeOffset}
};

epicsShareExtern dset *pvar_dset_devAaiSoft;
epicsShareExtern dset *pvar_dset_devAaoSoft;
epicsShareExtern dset *pvar_dset_devAiSoft;
epicsShareExtern dset *pvar_dset_devAiSoftRaw;
epicsShareExtern dset *pvar_dset_devTimestampAI;
epicsShareExtern dset *pvar_dset_devAiGeneralTime;
epicsShareExtern dset *pvar_dset_devNtpShmAiDelta;
epicsShareExtern dset *pvar_dset_devAIFromDouble;
epicsShareExtern dset *pvar_dset_devAIFromUINT32;
epicsShareExtern dset *pvar_dset_devAIFromUINT16;
epicsShareExtern dset *pvar_dset_devAiTodSeconds;
epicsShareExtern dset *pvar_dset_asynAiInt32;
epicsShareExtern dset *pvar_dset_asynAiInt32Average;
epicsShareExtern dset *pvar_dset_asynAiFloat64;
epicsShareExtern dset *pvar_dset_asynAiFloat64Average;
epicsShareExtern dset *pvar_dset_devAiStats;
epicsShareExtern dset *pvar_dset_devAiClusts;
epicsShareExtern dset *pvar_dset_devAoSoft;
epicsShareExtern dset *pvar_dset_devAoSoftRaw;
epicsShareExtern dset *pvar_dset_devAoSoftCallback;
epicsShareExtern dset *pvar_dset_devAOFromDouble;
epicsShareExtern dset *pvar_dset_devAOFromUINT32;
epicsShareExtern dset *pvar_dset_devAOFromUINT16;
epicsShareExtern dset *pvar_dset_asynAoInt32;
epicsShareExtern dset *pvar_dset_asynAoFloat64;
epicsShareExtern dset *pvar_dset_devAoStats;
epicsShareExtern dset *pvar_dset_devBiSoft;
epicsShareExtern dset *pvar_dset_devBiSoftRaw;
epicsShareExtern dset *pvar_dset_devBiASStatus;
epicsShareExtern dset *pvar_dset_devBiEvgTimestampInpMode;
epicsShareExtern dset *pvar_dset_devBiEvgLoadStatus;
epicsShareExtern dset *pvar_dset_devBiEvgEnaStatus;
epicsShareExtern dset *pvar_dset_devBiEvgCommitStatus;
epicsShareExtern dset *pvar_dset_devBIFromUINT32;
epicsShareExtern dset *pvar_dset_devBIFromUINT16;
epicsShareExtern dset *pvar_dset_devBIFromBool;
epicsShareExtern dset *pvar_dset_asynBiInt32;
epicsShareExtern dset *pvar_dset_asynBiUInt32Digital;
epicsShareExtern dset *pvar_dset_devBoSoft;
epicsShareExtern dset *pvar_dset_devBoSoftRaw;
epicsShareExtern dset *pvar_dset_devBoSoftCallback;
epicsShareExtern dset *pvar_dset_devBoGeneralTime;
epicsShareExtern dset *pvar_dset_devBoEvgResetMxc;
epicsShareExtern dset *pvar_dset_devBoEvgSyncTS;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtMxc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtAc;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgTrigEvtInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgDbusSrcInp;
epicsShareExtern dset *pvar_dset_devBoEvgTimestampInpMode;
epicsShareExtern dset *pvar_dset_devBoEvgSoftTrig;
epicsShareExtern dset *pvar_dset_devBoEvgLoadSeq;
epicsShareExtern dset *pvar_dset_devBoEvgUnloadSeq;
epicsShareExtern dset *pvar_dset_devBoEvgCommitSeq;
epicsShareExtern dset *pvar_dset_devBoEvgEnableSeq;
epicsShareExtern dset *pvar_dset_devBoEvgDisableSeq;
epicsShareExtern dset *pvar_dset_devBoEvgAbortSeq;
epicsShareExtern dset *pvar_dset_devBoEvgPauseSeq;
epicsShareExtern dset *pvar_dset_devBOFromUINT32;
epicsShareExtern dset *pvar_dset_devBOFromUINT16;
epicsShareExtern dset *pvar_dset_devBOFromBool;
epicsShareExtern dset *pvar_dset_asynBoInt32;
epicsShareExtern dset *pvar_dset_asynBoUInt32Digital;
epicsShareExtern dset *pvar_dset_devCalcoutSoft;
epicsShareExtern dset *pvar_dset_devCalcoutSoftCallback;
epicsShareExtern dset *pvar_dset_devEventSoft;
epicsShareExtern dset *pvar_dset_devHistogramSoft;
epicsShareExtern dset *pvar_dset_devLiSoft;
epicsShareExtern dset *pvar_dset_devLiGeneralTime;
epicsShareExtern dset *pvar_dset_devLiASSum;
epicsShareExtern dset *pvar_dset_devLiNumOfRuns;
epicsShareExtern dset *pvar_dset_devNtpShmLiOk;
epicsShareExtern dset *pvar_dset_devNtpShmLiFail;
epicsShareExtern dset *pvar_dset_devLIFromUINT32;
epicsShareExtern dset *pvar_dset_devLIFromUINT16;
epicsShareExtern dset *pvar_dset_devLIFromBool;
epicsShareExtern dset *pvar_dset_asynLiInt32;
epicsShareExtern dset *pvar_dset_asynLiUInt32Digital;
epicsShareExtern dset *pvar_dset_devLoSoft;
epicsShareExtern dset *pvar_dset_devLoSoftCallback;
epicsShareExtern dset *pvar_dset_devLOEVRPulserMap;
epicsShareExtern dset *pvar_dset_devEventEVR;
epicsShareExtern dset *pvar_dset_devLOEVRMap;
epicsShareExtern dset *pvar_dset_devLOFromUINT32;
epicsShareExtern dset *pvar_dset_devLOFromUINT16;
epicsShareExtern dset *pvar_dset_devLOFromBool;
epicsShareExtern dset *pvar_dset_asynLoInt32;
epicsShareExtern dset *pvar_dset_asynLoUInt32Digital;
epicsShareExtern dset *pvar_dset_devMbbiSoft;
epicsShareExtern dset *pvar_dset_devMbbiSoftRaw;
epicsShareExtern dset *pvar_dset_devMbbiEvgTimestampResolution;
epicsShareExtern dset *pvar_dset_devMbbiEvgRunMode;
epicsShareExtern dset *pvar_dset_devMbbiEvgTrigSrc;
epicsShareExtern dset *pvar_dset_devMBBIFromUINT32;
epicsShareExtern dset *pvar_dset_devMBBIFromUINT16;
epicsShareExtern dset *pvar_dset_asynMbbiInt32;
epicsShareExtern dset *pvar_dset_asynMbbiUInt32Digital;
epicsShareExtern dset *pvar_dset_devMbbiDirectSoft;
epicsShareExtern dset *pvar_dset_devMbbiDirectSoftRaw;
epicsShareExtern dset *pvar_dset_devMBBIDirFromUINT32;
epicsShareExtern dset *pvar_dset_devMBBIDirFromUINT16;
epicsShareExtern dset *pvar_dset_asynMbbiDirectUInt32Digital;
epicsShareExtern dset *pvar_dset_devMbboSoft;
epicsShareExtern dset *pvar_dset_devMbboSoftRaw;
epicsShareExtern dset *pvar_dset_devMbboSoftCallback;
epicsShareExtern dset *pvar_dset_devMbboEvgTimestampResolution;
epicsShareExtern dset *pvar_dset_devMbboEvgRunMode;
epicsShareExtern dset *pvar_dset_devMbboEvgTrigSrc;
epicsShareExtern dset *pvar_dset_devMBBOFromUINT32;
epicsShareExtern dset *pvar_dset_devMBBOFromUINT16;
epicsShareExtern dset *pvar_dset_asynMbboInt32;
epicsShareExtern dset *pvar_dset_asynMbboUInt32Digital;
epicsShareExtern dset *pvar_dset_devMbboDirectSoft;
epicsShareExtern dset *pvar_dset_devMbboDirectSoftRaw;
epicsShareExtern dset *pvar_dset_devMbboDirectSoftCallback;
epicsShareExtern dset *pvar_dset_devMBBODirFromUINT32;
epicsShareExtern dset *pvar_dset_devMBBODirFromUINT16;
epicsShareExtern dset *pvar_dset_devMbboDirectRestore;
epicsShareExtern dset *pvar_dset_asynMbboDirectUInt32Digital;
epicsShareExtern dset *pvar_dset_devSiSoft;
epicsShareExtern dset *pvar_dset_devTimestampSI;
epicsShareExtern dset *pvar_dset_devSiGeneralTime;
epicsShareExtern dset *pvar_dset_devSiTimeStamp;
epicsShareExtern dset *pvar_dset_devSiErr;
epicsShareExtern dset *pvar_dset_devSIEVR;
epicsShareExtern dset *pvar_dset_devSIFromString;
epicsShareExtern dset *pvar_dset_devSiTodString;
epicsShareExtern dset *pvar_dset_asynSiOctetCmdResponse;
epicsShareExtern dset *pvar_dset_asynSiOctetWriteRead;
epicsShareExtern dset *pvar_dset_asynSiOctetRead;
epicsShareExtern dset *pvar_dset_devStringinStats;
epicsShareExtern dset *pvar_dset_devStringinEnvVar;
epicsShareExtern dset *pvar_dset_devStringinEpics;
epicsShareExtern dset *pvar_dset_devSoSoft;
epicsShareExtern dset *pvar_dset_devSoSoftCallback;
epicsShareExtern dset *pvar_dset_devSoStdio;
epicsShareExtern dset *pvar_dset_devSOFromString;
epicsShareExtern dset *pvar_dset_asynSoOctetWrite;
epicsShareExtern dset *pvar_dset_devSASoft;
epicsShareExtern dset *pvar_dset_devWfSoft;
epicsShareExtern dset *pvar_dset_devwaveformoutdataBufTx;
epicsShareExtern dset *pvar_dset_devWfEvgTimestamp;
epicsShareExtern dset *pvar_dset_devWfEvgTimestampRB;
epicsShareExtern dset *pvar_dset_devWfEvgEventCode;
epicsShareExtern dset *pvar_dset_devWfEvgEventCodeRB;
epicsShareExtern dset *pvar_dset_devWfEvgLoadedSeq;
epicsShareExtern dset *pvar_dset_devWfMailbox;
epicsShareExtern dset *pvar_dset_devWFIn;
epicsShareExtern dset *pvar_dset_devWFOut;
epicsShareExtern dset *pvar_dset_devwaveformindataBufRx;
epicsShareExtern dset *pvar_dset_asynWfOctetCmdResponse;
epicsShareExtern dset *pvar_dset_asynWfOctetWriteRead;
epicsShareExtern dset *pvar_dset_asynWfOctetRead;
epicsShareExtern dset *pvar_dset_asynWfOctetWrite;
epicsShareExtern dset *pvar_dset_asynInt8ArrayWfIn;
epicsShareExtern dset *pvar_dset_asynInt8ArrayWfOut;
epicsShareExtern dset *pvar_dset_asynInt16ArrayWfIn;
epicsShareExtern dset *pvar_dset_asynInt16ArrayWfOut;
epicsShareExtern dset *pvar_dset_asynInt32ArrayWfIn;
epicsShareExtern dset *pvar_dset_asynInt32ArrayWfOut;
epicsShareExtern dset *pvar_dset_asynInt32TimeSeries;
epicsShareExtern dset *pvar_dset_asynFloat32ArrayWfIn;
epicsShareExtern dset *pvar_dset_asynFloat32ArrayWfOut;
epicsShareExtern dset *pvar_dset_asynFloat64ArrayWfIn;
epicsShareExtern dset *pvar_dset_asynFloat64ArrayWfOut;
epicsShareExtern dset *pvar_dset_asynFloat64TimeSeries;
epicsShareExtern dset *pvar_dset_devMCA_soft;
epicsShareExtern dset *pvar_dset_devMcaAsyn;
epicsShareExtern dset *pvar_dset_devsCalcoutSoft;
epicsShareExtern dset *pvar_dset_devaCalcoutSoft;
epicsShareExtern dset *pvar_dset_devSWaitIoEvent;
epicsShareExtern dset *pvar_dset_devScalerAsyn;
epicsShareExtern dset *pvar_dset_devEpidSoft;
epicsShareExtern dset *pvar_dset_devEpidSoftCB;
epicsShareExtern dset *pvar_dset_devEpidFast;
epicsShareExtern dset *pvar_dset_asynRecordDevice;
epicsShareExtern dset *pvar_dset_devBusySoft;
epicsShareExtern dset *pvar_dset_devBusySoftRaw;
epicsShareExtern dset *pvar_dset_asynBusyInt32;

static const char * const deviceSupportNames[195] = {
    "devAaiSoft",
    "devAaoSoft",
    "devAiSoft",
    "devAiSoftRaw",
    "devTimestampAI",
    "devAiGeneralTime",
    "devNtpShmAiDelta",
    "devAIFromDouble",
    "devAIFromUINT32",
    "devAIFromUINT16",
    "devAiTodSeconds",
    "asynAiInt32",
    "asynAiInt32Average",
    "asynAiFloat64",
    "asynAiFloat64Average",
    "devAiStats",
    "devAiClusts",
    "devAoSoft",
    "devAoSoftRaw",
    "devAoSoftCallback",
    "devAOFromDouble",
    "devAOFromUINT32",
    "devAOFromUINT16",
    "asynAoInt32",
    "asynAoFloat64",
    "devAoStats",
    "devBiSoft",
    "devBiSoftRaw",
    "devBiASStatus",
    "devBiEvgTimestampInpMode",
    "devBiEvgLoadStatus",
    "devBiEvgEnaStatus",
    "devBiEvgCommitStatus",
    "devBIFromUINT32",
    "devBIFromUINT16",
    "devBIFromBool",
    "asynBiInt32",
    "asynBiUInt32Digital",
    "devBoSoft",
    "devBoSoftRaw",
    "devBoSoftCallback",
    "devBoGeneralTime",
    "devBoEvgResetMxc",
    "devBoEvgSyncTS",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtMxc",
    "devBoEvgTrigEvtAc",
    "devBoEvgTrigEvtInp",
    "devBoEvgTrigEvtInp",
    "devBoEvgTrigEvtInp",
    "devBoEvgTrigEvtInp",
    "devBoEvgTrigEvtInp",
    "devBoEvgTrigEvtInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgDbusSrcInp",
    "devBoEvgTimestampInpMode",
    "devBoEvgSoftTrig",
    "devBoEvgLoadSeq",
    "devBoEvgUnloadSeq",
    "devBoEvgCommitSeq",
    "devBoEvgEnableSeq",
    "devBoEvgDisableSeq",
    "devBoEvgAbortSeq",
    "devBoEvgPauseSeq",
    "devBOFromUINT32",
    "devBOFromUINT16",
    "devBOFromBool",
    "asynBoInt32",
    "asynBoUInt32Digital",
    "devCalcoutSoft",
    "devCalcoutSoftCallback",
    "devEventSoft",
    "devHistogramSoft",
    "devLiSoft",
    "devLiGeneralTime",
    "devLiASSum",
    "devLiNumOfRuns",
    "devNtpShmLiOk",
    "devNtpShmLiFail",
    "devLIFromUINT32",
    "devLIFromUINT16",
    "devLIFromBool",
    "asynLiInt32",
    "asynLiUInt32Digital",
    "devLoSoft",
    "devLoSoftCallback",
    "devLOEVRPulserMap",
    "devEventEVR",
    "devLOEVRMap",
    "devLOFromUINT32",
    "devLOFromUINT16",
    "devLOFromBool",
    "asynLoInt32",
    "asynLoUInt32Digital",
    "devMbbiSoft",
    "devMbbiSoftRaw",
    "devMbbiEvgTimestampResolution",
    "devMbbiEvgRunMode",
    "devMbbiEvgTrigSrc",
    "devMBBIFromUINT32",
    "devMBBIFromUINT16",
    "asynMbbiInt32",
    "asynMbbiUInt32Digital",
    "devMbbiDirectSoft",
    "devMbbiDirectSoftRaw",
    "devMBBIDirFromUINT32",
    "devMBBIDirFromUINT16",
    "asynMbbiDirectUInt32Digital",
    "devMbboSoft",
    "devMbboSoftRaw",
    "devMbboSoftCallback",
    "devMbboEvgTimestampResolution",
    "devMbboEvgRunMode",
    "devMbboEvgTrigSrc",
    "devMBBOFromUINT32",
    "devMBBOFromUINT16",
    "asynMbboInt32",
    "asynMbboUInt32Digital",
    "devMbboDirectSoft",
    "devMbboDirectSoftRaw",
    "devMbboDirectSoftCallback",
    "devMBBODirFromUINT32",
    "devMBBODirFromUINT16",
    "devMbboDirectRestore",
    "asynMbboDirectUInt32Digital",
    "devSiSoft",
    "devTimestampSI",
    "devSiGeneralTime",
    "devSiTimeStamp",
    "devSiErr",
    "devSIEVR",
    "devSIFromString",
    "devSiTodString",
    "asynSiOctetCmdResponse",
    "asynSiOctetWriteRead",
    "asynSiOctetRead",
    "devStringinStats",
    "devStringinEnvVar",
    "devStringinEpics",
    "devSoSoft",
    "devSoSoftCallback",
    "devSoStdio",
    "devSOFromString",
    "asynSoOctetWrite",
    "devSASoft",
    "devWfSoft",
    "devwaveformoutdataBufTx",
    "devWfEvgTimestamp",
    "devWfEvgTimestampRB",
    "devWfEvgEventCode",
    "devWfEvgEventCodeRB",
    "devWfEvgLoadedSeq",
    "devWfMailbox",
    "devWFIn",
    "devWFOut",
    "devwaveformindataBufRx",
    "asynWfOctetCmdResponse",
    "asynWfOctetWriteRead",
    "asynWfOctetRead",
    "asynWfOctetWrite",
    "asynInt8ArrayWfIn",
    "asynInt8ArrayWfOut",
    "asynInt16ArrayWfIn",
    "asynInt16ArrayWfOut",
    "asynInt32ArrayWfIn",
    "asynInt32ArrayWfOut",
    "asynInt32TimeSeries",
    "asynFloat32ArrayWfIn",
    "asynFloat32ArrayWfOut",
    "asynFloat64ArrayWfIn",
    "asynFloat64ArrayWfOut",
    "asynFloat64TimeSeries",
    "devMCA_soft",
    "devMcaAsyn",
    "devsCalcoutSoft",
    "devaCalcoutSoft",
    "devSWaitIoEvent",
    "devScalerAsyn",
    "devEpidSoft",
    "devEpidSoftCB",
    "devEpidFast",
    "asynRecordDevice",
    "devBusySoft",
    "devBusySoftRaw",
    "asynBusyInt32"
};

static const dset * const devsl[195] = {
    pvar_dset_devAaiSoft,
    pvar_dset_devAaoSoft,
    pvar_dset_devAiSoft,
    pvar_dset_devAiSoftRaw,
    pvar_dset_devTimestampAI,
    pvar_dset_devAiGeneralTime,
    pvar_dset_devNtpShmAiDelta,
    pvar_dset_devAIFromDouble,
    pvar_dset_devAIFromUINT32,
    pvar_dset_devAIFromUINT16,
    pvar_dset_devAiTodSeconds,
    pvar_dset_asynAiInt32,
    pvar_dset_asynAiInt32Average,
    pvar_dset_asynAiFloat64,
    pvar_dset_asynAiFloat64Average,
    pvar_dset_devAiStats,
    pvar_dset_devAiClusts,
    pvar_dset_devAoSoft,
    pvar_dset_devAoSoftRaw,
    pvar_dset_devAoSoftCallback,
    pvar_dset_devAOFromDouble,
    pvar_dset_devAOFromUINT32,
    pvar_dset_devAOFromUINT16,
    pvar_dset_asynAoInt32,
    pvar_dset_asynAoFloat64,
    pvar_dset_devAoStats,
    pvar_dset_devBiSoft,
    pvar_dset_devBiSoftRaw,
    pvar_dset_devBiASStatus,
    pvar_dset_devBiEvgTimestampInpMode,
    pvar_dset_devBiEvgLoadStatus,
    pvar_dset_devBiEvgEnaStatus,
    pvar_dset_devBiEvgCommitStatus,
    pvar_dset_devBIFromUINT32,
    pvar_dset_devBIFromUINT16,
    pvar_dset_devBIFromBool,
    pvar_dset_asynBiInt32,
    pvar_dset_asynBiUInt32Digital,
    pvar_dset_devBoSoft,
    pvar_dset_devBoSoftRaw,
    pvar_dset_devBoSoftCallback,
    pvar_dset_devBoGeneralTime,
    pvar_dset_devBoEvgResetMxc,
    pvar_dset_devBoEvgSyncTS,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtMxc,
    pvar_dset_devBoEvgTrigEvtAc,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgTrigEvtInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgDbusSrcInp,
    pvar_dset_devBoEvgTimestampInpMode,
    pvar_dset_devBoEvgSoftTrig,
    pvar_dset_devBoEvgLoadSeq,
    pvar_dset_devBoEvgUnloadSeq,
    pvar_dset_devBoEvgCommitSeq,
    pvar_dset_devBoEvgEnableSeq,
    pvar_dset_devBoEvgDisableSeq,
    pvar_dset_devBoEvgAbortSeq,
    pvar_dset_devBoEvgPauseSeq,
    pvar_dset_devBOFromUINT32,
    pvar_dset_devBOFromUINT16,
    pvar_dset_devBOFromBool,
    pvar_dset_asynBoInt32,
    pvar_dset_asynBoUInt32Digital,
    pvar_dset_devCalcoutSoft,
    pvar_dset_devCalcoutSoftCallback,
    pvar_dset_devEventSoft,
    pvar_dset_devHistogramSoft,
    pvar_dset_devLiSoft,
    pvar_dset_devLiGeneralTime,
    pvar_dset_devLiASSum,
    pvar_dset_devLiNumOfRuns,
    pvar_dset_devNtpShmLiOk,
    pvar_dset_devNtpShmLiFail,
    pvar_dset_devLIFromUINT32,
    pvar_dset_devLIFromUINT16,
    pvar_dset_devLIFromBool,
    pvar_dset_asynLiInt32,
    pvar_dset_asynLiUInt32Digital,
    pvar_dset_devLoSoft,
    pvar_dset_devLoSoftCallback,
    pvar_dset_devLOEVRPulserMap,
    pvar_dset_devEventEVR,
    pvar_dset_devLOEVRMap,
    pvar_dset_devLOFromUINT32,
    pvar_dset_devLOFromUINT16,
    pvar_dset_devLOFromBool,
    pvar_dset_asynLoInt32,
    pvar_dset_asynLoUInt32Digital,
    pvar_dset_devMbbiSoft,
    pvar_dset_devMbbiSoftRaw,
    pvar_dset_devMbbiEvgTimestampResolution,
    pvar_dset_devMbbiEvgRunMode,
    pvar_dset_devMbbiEvgTrigSrc,
    pvar_dset_devMBBIFromUINT32,
    pvar_dset_devMBBIFromUINT16,
    pvar_dset_asynMbbiInt32,
    pvar_dset_asynMbbiUInt32Digital,
    pvar_dset_devMbbiDirectSoft,
    pvar_dset_devMbbiDirectSoftRaw,
    pvar_dset_devMBBIDirFromUINT32,
    pvar_dset_devMBBIDirFromUINT16,
    pvar_dset_asynMbbiDirectUInt32Digital,
    pvar_dset_devMbboSoft,
    pvar_dset_devMbboSoftRaw,
    pvar_dset_devMbboSoftCallback,
    pvar_dset_devMbboEvgTimestampResolution,
    pvar_dset_devMbboEvgRunMode,
    pvar_dset_devMbboEvgTrigSrc,
    pvar_dset_devMBBOFromUINT32,
    pvar_dset_devMBBOFromUINT16,
    pvar_dset_asynMbboInt32,
    pvar_dset_asynMbboUInt32Digital,
    pvar_dset_devMbboDirectSoft,
    pvar_dset_devMbboDirectSoftRaw,
    pvar_dset_devMbboDirectSoftCallback,
    pvar_dset_devMBBODirFromUINT32,
    pvar_dset_devMBBODirFromUINT16,
    pvar_dset_devMbboDirectRestore,
    pvar_dset_asynMbboDirectUInt32Digital,
    pvar_dset_devSiSoft,
    pvar_dset_devTimestampSI,
    pvar_dset_devSiGeneralTime,
    pvar_dset_devSiTimeStamp,
    pvar_dset_devSiErr,
    pvar_dset_devSIEVR,
    pvar_dset_devSIFromString,
    pvar_dset_devSiTodString,
    pvar_dset_asynSiOctetCmdResponse,
    pvar_dset_asynSiOctetWriteRead,
    pvar_dset_asynSiOctetRead,
    pvar_dset_devStringinStats,
    pvar_dset_devStringinEnvVar,
    pvar_dset_devStringinEpics,
    pvar_dset_devSoSoft,
    pvar_dset_devSoSoftCallback,
    pvar_dset_devSoStdio,
    pvar_dset_devSOFromString,
    pvar_dset_asynSoOctetWrite,
    pvar_dset_devSASoft,
    pvar_dset_devWfSoft,
    pvar_dset_devwaveformoutdataBufTx,
    pvar_dset_devWfEvgTimestamp,
    pvar_dset_devWfEvgTimestampRB,
    pvar_dset_devWfEvgEventCode,
    pvar_dset_devWfEvgEventCodeRB,
    pvar_dset_devWfEvgLoadedSeq,
    pvar_dset_devWfMailbox,
    pvar_dset_devWFIn,
    pvar_dset_devWFOut,
    pvar_dset_devwaveformindataBufRx,
    pvar_dset_asynWfOctetCmdResponse,
    pvar_dset_asynWfOctetWriteRead,
    pvar_dset_asynWfOctetRead,
    pvar_dset_asynWfOctetWrite,
    pvar_dset_asynInt8ArrayWfIn,
    pvar_dset_asynInt8ArrayWfOut,
    pvar_dset_asynInt16ArrayWfIn,
    pvar_dset_asynInt16ArrayWfOut,
    pvar_dset_asynInt32ArrayWfIn,
    pvar_dset_asynInt32ArrayWfOut,
    pvar_dset_asynInt32TimeSeries,
    pvar_dset_asynFloat32ArrayWfIn,
    pvar_dset_asynFloat32ArrayWfOut,
    pvar_dset_asynFloat64ArrayWfIn,
    pvar_dset_asynFloat64ArrayWfOut,
    pvar_dset_asynFloat64TimeSeries,
    pvar_dset_devMCA_soft,
    pvar_dset_devMcaAsyn,
    pvar_dset_devsCalcoutSoft,
    pvar_dset_devaCalcoutSoft,
    pvar_dset_devSWaitIoEvent,
    pvar_dset_devScalerAsyn,
    pvar_dset_devEpidSoft,
    pvar_dset_devEpidSoftCB,
    pvar_dset_devEpidFast,
    pvar_dset_asynRecordDevice,
    pvar_dset_devBusySoft,
    pvar_dset_devBusySoftRaw,
    pvar_dset_asynBusyInt32
};

epicsShareExtern drvet *pvar_drvet_drvEvgMrm;
epicsShareExtern drvet *pvar_drvet_drvEvrMrm;
epicsShareExtern drvet *pvar_drvet_ntpShared;
epicsShareExtern drvet *pvar_drvet_drvAsyn;

static const char *driverSupportNames[4] = {
    "drvEvgMrm",
    "drvEvrMrm",
    "ntpShared",
    "drvAsyn"
};

static struct drvet *drvsl[4] = {
    pvar_drvet_drvEvgMrm,
    pvar_drvet_drvEvrMrm,
    pvar_drvet_ntpShared,
    pvar_drvet_drvAsyn
};

epicsShareExtern void (*pvar_func_asSub)(void);
epicsShareExtern void (*pvar_func_evgMrmRegistrar)(void);
epicsShareExtern void (*pvar_func_asub_evg)(void);
epicsShareExtern void (*pvar_func_asub_nsls2_evg)(void);
epicsShareExtern void (*pvar_func_mrmsetupreg)(void);
epicsShareExtern void (*pvar_func_asub_evr)(void);
epicsShareExtern void (*pvar_func_EVRTime_Registrar)(void);
epicsShareExtern void (*pvar_func_ntpShmRegister)(void);
epicsShareExtern void (*pvar_func_FracSynthRegistrar)(void);
epicsShareExtern void (*pvar_func_objectsreg)(void);
epicsShareExtern void (*pvar_func_registerISRHack)(void);
epicsShareExtern void (*pvar_func_vmecsr)(void);
epicsShareExtern void (*pvar_func_vmesh)(void);
epicsShareExtern void (*pvar_func_devReplaceVirtualOS)(void);
epicsShareExtern void (*pvar_func_devLibPCIIOCSH)(void);
epicsShareExtern void (*pvar_func_devLibPCIRegisterBaseDefault)(void);
epicsShareExtern void (*pvar_func_pcish)(void);
epicsShareExtern void (*pvar_func_fastSweepRegister)(void);
epicsShareExtern void (*pvar_func_drvSIS3801Register)(void);
epicsShareExtern void (*pvar_func_drvSIS3820Register)(void);
epicsShareExtern void (*pvar_func_SIS38XX_SNLRegistrar)(void);
epicsShareExtern void (*pvar_func_subAveRegister)(void);
epicsShareExtern void (*pvar_func_interpRegister)(void);
epicsShareExtern void (*pvar_func_arrayTestRegister)(void);
epicsShareExtern void (*pvar_func_saveDataRegistrar)(void);
epicsShareExtern void (*pvar_func_pvHistoryRegister)(void);
epicsShareExtern void (*pvar_func_drvScalerSoftRegister)(void);
epicsShareExtern void (*pvar_func_femtoRegistrar)(void);
epicsShareExtern void (*pvar_func_Scaler974Register)(void);
epicsShareExtern void (*pvar_func_asynRegister)(void);
epicsShareExtern void (*pvar_func_asynInterposeFlushRegister)(void);
epicsShareExtern void (*pvar_func_asynInterposeEosRegister)(void);
epicsShareExtern void (*pvar_func_save_restoreRegister)(void);
epicsShareExtern void (*pvar_func_dbrestoreRegister)(void);
epicsShareExtern void (*pvar_func_asInitHooksRegister)(void);
epicsShareExtern void (*pvar_func_configMenuRegistrar)(void);
epicsShareExtern void (*pvar_func_caPutLogRegister)(void);
epicsShareExtern void (*pvar_func_register_func_rebootProc)(void);
epicsShareExtern void (*pvar_func_register_func_scanMonInit)(void);
epicsShareExtern void (*pvar_func_register_func_scanMon)(void);

epicsShareExtern int *pvar_int_asCaDebug;
epicsShareExtern int *pvar_int_dbRecordsOnceOnly;
epicsShareExtern int *pvar_int_dbBptNotMonotonic;
epicsShareExtern int *pvar_int_mrmEVGSeqDebug;
epicsShareExtern int *pvar_int_seqConstDebug;
epicsShareExtern double *pvar_double_mrmEvrFIFOPeriod;
epicsShareExtern int *pvar_int_devPCIDebug;
epicsShareExtern int *pvar_int_mcaRecordDebug;
epicsShareExtern int *pvar_int_debugSubAve;
epicsShareExtern int *pvar_int_sCalcPostfixDebug;
epicsShareExtern int *pvar_int_sCalcPerformDebug;
epicsShareExtern int *pvar_int_sCalcoutRecordDebug;
epicsShareExtern int *pvar_int_devsCalcoutSoftDebug;
epicsShareExtern int *pvar_int_sCalcStackHW;
epicsShareExtern int *pvar_int_sCalcStackLW;
epicsShareExtern int *pvar_int_sCalcLoopMax;
epicsShareExtern int *pvar_int_aCalcPostfixDebug;
epicsShareExtern int *pvar_int_aCalcPerformDebug;
epicsShareExtern int *pvar_int_aCalcoutRecordDebug;
epicsShareExtern int *pvar_int_devaCalcoutSoftDebug;
epicsShareExtern int *pvar_int_aCalcLoopMax;
epicsShareExtern int *pvar_int_aCalcAsyncThreshold;
epicsShareExtern int *pvar_int_transformRecordDebug;
epicsShareExtern int *pvar_int_interpDebug;
epicsShareExtern int *pvar_int_arrayTestDebug;
epicsShareExtern int *pvar_int_sseqRecDebug;
epicsShareExtern int *pvar_int_swaitRecordDebug;
epicsShareExtern int *pvar_int_recDynLinkDebug;
epicsShareExtern int *pvar_int_recDynLinkQsize;
epicsShareExtern int *pvar_int_debug_saveData;
epicsShareExtern int *pvar_int_debug_saveDataMsg;
epicsShareExtern int *pvar_int_saveData_MessagePolicy;
epicsShareExtern int *pvar_int_sscanRecordDebug;
epicsShareExtern int *pvar_int_sscanRecordViewPos;
epicsShareExtern int *pvar_int_sscanRecordDontCheckLimits;
epicsShareExtern int *pvar_int_sscanRecordLookupTime;
epicsShareExtern int *pvar_int_sscanRecordConnectWaitSeconds;
epicsShareExtern int *pvar_int_pvHistoryDebug;
epicsShareExtern int *pvar_int_save_restoreDebug;
epicsShareExtern int *pvar_int_save_restoreNumSeqFiles;
epicsShareExtern int *pvar_int_save_restoreSeqPeriodInSeconds;
epicsShareExtern int *pvar_int_save_restoreIncompleteSetsOk;
epicsShareExtern int *pvar_int_save_restoreDatedBackupFiles;
epicsShareExtern int *pvar_int_save_restoreRemountThreshold;
epicsShareExtern int *pvar_int_configMenuDebug;
static struct iocshVarDef vardefs[] = {
	{"asCaDebug", iocshArgInt, (void * const)pvar_int_asCaDebug},
	{"dbRecordsOnceOnly", iocshArgInt, (void * const)pvar_int_dbRecordsOnceOnly},
	{"dbBptNotMonotonic", iocshArgInt, (void * const)pvar_int_dbBptNotMonotonic},
	{"mrmEVGSeqDebug", iocshArgInt, (void * const)pvar_int_mrmEVGSeqDebug},
	{"seqConstDebug", iocshArgInt, (void * const)pvar_int_seqConstDebug},
	{"mrmEvrFIFOPeriod", iocshArgDouble, (void * const)pvar_double_mrmEvrFIFOPeriod},
	{"devPCIDebug", iocshArgInt, (void * const)pvar_int_devPCIDebug},
	{"mcaRecordDebug", iocshArgInt, (void * const)pvar_int_mcaRecordDebug},
	{"debugSubAve", iocshArgInt, (void * const)pvar_int_debugSubAve},
	{"sCalcPostfixDebug", iocshArgInt, (void * const)pvar_int_sCalcPostfixDebug},
	{"sCalcPerformDebug", iocshArgInt, (void * const)pvar_int_sCalcPerformDebug},
	{"sCalcoutRecordDebug", iocshArgInt, (void * const)pvar_int_sCalcoutRecordDebug},
	{"devsCalcoutSoftDebug", iocshArgInt, (void * const)pvar_int_devsCalcoutSoftDebug},
	{"sCalcStackHW", iocshArgInt, (void * const)pvar_int_sCalcStackHW},
	{"sCalcStackLW", iocshArgInt, (void * const)pvar_int_sCalcStackLW},
	{"sCalcLoopMax", iocshArgInt, (void * const)pvar_int_sCalcLoopMax},
	{"aCalcPostfixDebug", iocshArgInt, (void * const)pvar_int_aCalcPostfixDebug},
	{"aCalcPerformDebug", iocshArgInt, (void * const)pvar_int_aCalcPerformDebug},
	{"aCalcoutRecordDebug", iocshArgInt, (void * const)pvar_int_aCalcoutRecordDebug},
	{"devaCalcoutSoftDebug", iocshArgInt, (void * const)pvar_int_devaCalcoutSoftDebug},
	{"aCalcLoopMax", iocshArgInt, (void * const)pvar_int_aCalcLoopMax},
	{"aCalcAsyncThreshold", iocshArgInt, (void * const)pvar_int_aCalcAsyncThreshold},
	{"transformRecordDebug", iocshArgInt, (void * const)pvar_int_transformRecordDebug},
	{"interpDebug", iocshArgInt, (void * const)pvar_int_interpDebug},
	{"arrayTestDebug", iocshArgInt, (void * const)pvar_int_arrayTestDebug},
	{"sseqRecDebug", iocshArgInt, (void * const)pvar_int_sseqRecDebug},
	{"swaitRecordDebug", iocshArgInt, (void * const)pvar_int_swaitRecordDebug},
	{"recDynLinkDebug", iocshArgInt, (void * const)pvar_int_recDynLinkDebug},
	{"recDynLinkQsize", iocshArgInt, (void * const)pvar_int_recDynLinkQsize},
	{"debug_saveData", iocshArgInt, (void * const)pvar_int_debug_saveData},
	{"debug_saveDataMsg", iocshArgInt, (void * const)pvar_int_debug_saveDataMsg},
	{"saveData_MessagePolicy", iocshArgInt, (void * const)pvar_int_saveData_MessagePolicy},
	{"sscanRecordDebug", iocshArgInt, (void * const)pvar_int_sscanRecordDebug},
	{"sscanRecordViewPos", iocshArgInt, (void * const)pvar_int_sscanRecordViewPos},
	{"sscanRecordDontCheckLimits", iocshArgInt, (void * const)pvar_int_sscanRecordDontCheckLimits},
	{"sscanRecordLookupTime", iocshArgInt, (void * const)pvar_int_sscanRecordLookupTime},
	{"sscanRecordConnectWaitSeconds", iocshArgInt, (void * const)pvar_int_sscanRecordConnectWaitSeconds},
	{"pvHistoryDebug", iocshArgInt, (void * const)pvar_int_pvHistoryDebug},
	{"save_restoreDebug", iocshArgInt, (void * const)pvar_int_save_restoreDebug},
	{"save_restoreNumSeqFiles", iocshArgInt, (void * const)pvar_int_save_restoreNumSeqFiles},
	{"save_restoreSeqPeriodInSeconds", iocshArgInt, (void * const)pvar_int_save_restoreSeqPeriodInSeconds},
	{"save_restoreIncompleteSetsOk", iocshArgInt, (void * const)pvar_int_save_restoreIncompleteSetsOk},
	{"save_restoreDatedBackupFiles", iocshArgInt, (void * const)pvar_int_save_restoreDatedBackupFiles},
	{"save_restoreRemountThreshold", iocshArgInt, (void * const)pvar_int_save_restoreRemountThreshold},
	{"configMenuDebug", iocshArgInt, (void * const)pvar_int_configMenuDebug},
	{NULL, iocshArgInt, NULL}
};

int vme_registerRecordDeviceDriver(DBBASE *pbase)
{
    const char *bldTop = "/epics/iocs/vme-05idd";
    const char *envTop = getenv("TOP");

    if (envTop && strcmp(envTop, bldTop)) {
        printf("Warning: IOC is booting with TOP = \"%s\"\n"
               "          but was built with TOP = \"%s\"\n",
               envTop, bldTop);
    }

    if (!pbase) {
        printf("pdbbase is NULL; you must load a DBD file first.\n");
        return -1;
    }

    registerRecordTypes(pbase, 42, recordTypeNames, rtl);
    registerDevices(pbase, 195, deviceSupportNames, devsl);
    registerDrivers(pbase, 4, driverSupportNames, drvsl);
    (*pvar_func_asSub)();
    (*pvar_func_evgMrmRegistrar)();
    (*pvar_func_asub_evg)();
    (*pvar_func_asub_nsls2_evg)();
    (*pvar_func_mrmsetupreg)();
    (*pvar_func_asub_evr)();
    (*pvar_func_EVRTime_Registrar)();
    (*pvar_func_ntpShmRegister)();
    (*pvar_func_FracSynthRegistrar)();
    (*pvar_func_objectsreg)();
    (*pvar_func_registerISRHack)();
    (*pvar_func_vmecsr)();
    (*pvar_func_vmesh)();
    (*pvar_func_devReplaceVirtualOS)();
    (*pvar_func_devLibPCIIOCSH)();
    (*pvar_func_devLibPCIRegisterBaseDefault)();
    (*pvar_func_pcish)();
    (*pvar_func_fastSweepRegister)();
    (*pvar_func_drvSIS3801Register)();
    (*pvar_func_drvSIS3820Register)();
    (*pvar_func_SIS38XX_SNLRegistrar)();
    (*pvar_func_subAveRegister)();
    (*pvar_func_interpRegister)();
    (*pvar_func_arrayTestRegister)();
    (*pvar_func_saveDataRegistrar)();
    (*pvar_func_pvHistoryRegister)();
    (*pvar_func_drvScalerSoftRegister)();
    (*pvar_func_femtoRegistrar)();
    (*pvar_func_Scaler974Register)();
    (*pvar_func_asynRegister)();
    (*pvar_func_asynInterposeFlushRegister)();
    (*pvar_func_asynInterposeEosRegister)();
    (*pvar_func_save_restoreRegister)();
    (*pvar_func_dbrestoreRegister)();
    (*pvar_func_asInitHooksRegister)();
    (*pvar_func_configMenuRegistrar)();
    (*pvar_func_caPutLogRegister)();
    (*pvar_func_register_func_rebootProc)();
    (*pvar_func_register_func_scanMonInit)();
    (*pvar_func_register_func_scanMon)();
    iocshRegisterVariable(vardefs);
    return 0;
}

/* registerRecordDeviceDriver */
static const iocshArg registerRecordDeviceDriverArg0 =
                                            {"pdbbase",iocshArgPdbbase};
static const iocshArg *registerRecordDeviceDriverArgs[1] =
                                            {&registerRecordDeviceDriverArg0};
static const iocshFuncDef registerRecordDeviceDriverFuncDef =
                {"vme_registerRecordDeviceDriver",1,registerRecordDeviceDriverArgs};
static void registerRecordDeviceDriverCallFunc(const iocshArgBuf *)
{
    vme_registerRecordDeviceDriver(*iocshPpdbbase);
}

} // extern "C"
/*
 * Register commands on application startup
 */
static int Registration() {
    iocshRegisterCommon();
    iocshRegister(&registerRecordDeviceDriverFuncDef,
        registerRecordDeviceDriverCallFunc);
    return 0;
}

static int done = Registration();
