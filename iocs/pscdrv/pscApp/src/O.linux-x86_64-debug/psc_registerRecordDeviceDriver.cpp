/* THIS IS A GENERATED FILE. DO NOT EDIT! */
/* Generated from ../O.Common/psc.dbd */

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
epicsShareExtern rset *pvar_rset_waveAnlRSET;
epicsShareExtern int (*pvar_func_waveAnlRecordSizeOffset)(dbRecordType *pdbRecordType);

static const char * const recordTypeNames[30] = {
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
    "waveAnl"
};

static const recordTypeLocation rtl[30] = {
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
    {pvar_rset_waveAnlRSET, pvar_func_waveAnlRecordSizeOffset}
};

epicsShareExtern dset *pvar_dset_devAaiSoft;
epicsShareExtern dset *pvar_dset_devAaoSoft;
epicsShareExtern dset *pvar_dset_devAiSoft;
epicsShareExtern dset *pvar_dset_devAiSoftRaw;
epicsShareExtern dset *pvar_dset_devTimestampAI;
epicsShareExtern dset *pvar_dset_devAiGeneralTime;
epicsShareExtern dset *pvar_dset_devPSCRegAi;
epicsShareExtern dset *pvar_dset_devPSCRegF32Ai;
epicsShareExtern dset *pvar_dset_devPSCRegF64Ai;
epicsShareExtern dset *pvar_dset_devPSCRegRBAi;
epicsShareExtern dset *pvar_dset_devPSCRegRBF32Ai;
epicsShareExtern dset *pvar_dset_devPSCRegRBF64Ai;
epicsShareExtern dset *pvar_dset_devAIFFTTotPwrTime;
epicsShareExtern dset *pvar_dset_devAIFFTTotPwrFreq;
epicsShareExtern dset *pvar_dset_devAIFFTLasttime;
epicsShareExtern dset *pvar_dset_devAiStats;
epicsShareExtern dset *pvar_dset_devAiClusts;
epicsShareExtern dset *pvar_dset_devAoSoft;
epicsShareExtern dset *pvar_dset_devAoSoftRaw;
epicsShareExtern dset *pvar_dset_devAoSoftCallback;
epicsShareExtern dset *pvar_dset_devPSCRegAo;
epicsShareExtern dset *pvar_dset_devPSCRegF32Ao;
epicsShareExtern dset *pvar_dset_devPSCRegF64Ao;
epicsShareExtern dset *pvar_dset_devPSCSingleS32Ao;
epicsShareExtern dset *pvar_dset_devPSCSingleF32Ao;
epicsShareExtern dset *pvar_dset_devPSCSingleF64Ao;
epicsShareExtern dset *pvar_dset_devPSCTblAo1Mode;
epicsShareExtern dset *pvar_dset_devPSCTblAo2Mode;
epicsShareExtern dset *pvar_dset_devAOFFTFSamp;
epicsShareExtern dset *pvar_dset_devAOFFTScale;
epicsShareExtern dset *pvar_dset_devAoStats;
epicsShareExtern dset *pvar_dset_devBiSoft;
epicsShareExtern dset *pvar_dset_devBiSoftRaw;
epicsShareExtern dset *pvar_dset_devBiASStatus;
epicsShareExtern dset *pvar_dset_devPSCConnectedBi;
epicsShareExtern dset *pvar_dset_devPSCRegBi;
epicsShareExtern dset *pvar_dset_devPSCRegRBBi;
epicsShareExtern dset *pvar_dset_devBoSoft;
epicsShareExtern dset *pvar_dset_devBoSoftRaw;
epicsShareExtern dset *pvar_dset_devBoSoftCallback;
epicsShareExtern dset *pvar_dset_devBoGeneralTime;
epicsShareExtern dset *pvar_dset_devPSCSendAllBo;
epicsShareExtern dset *pvar_dset_devPSCForceReConn;
epicsShareExtern dset *pvar_dset_devPSCRegBo;
epicsShareExtern dset *pvar_dset_devPSCSingleU32Bo;
epicsShareExtern dset *pvar_dset_devCalcoutSoft;
epicsShareExtern dset *pvar_dset_devCalcoutSoftCallback;
epicsShareExtern dset *pvar_dset_devEventSoft;
epicsShareExtern dset *pvar_dset_devHistogramSoft;
epicsShareExtern dset *pvar_dset_devLiSoft;
epicsShareExtern dset *pvar_dset_devLiGeneralTime;
epicsShareExtern dset *pvar_dset_devLiASSum;
epicsShareExtern dset *pvar_dset_devPSCUknCountLi;
epicsShareExtern dset *pvar_dset_devPSCConnCountLi;
epicsShareExtern dset *pvar_dset_devPSCBlockCountLi;
epicsShareExtern dset *pvar_dset_devPSCRegLi;
epicsShareExtern dset *pvar_dset_devPSCRegRBLi;
epicsShareExtern dset *pvar_dset_devLoSoft;
epicsShareExtern dset *pvar_dset_devLoSoftCallback;
epicsShareExtern dset *pvar_dset_devPSCSendLo;
epicsShareExtern dset *pvar_dset_devPSCRegLo;
epicsShareExtern dset *pvar_dset_devPSCSingleS32Lo;
epicsShareExtern dset *pvar_dset_devPSCTblLoStart;
epicsShareExtern dset *pvar_dset_devLOFFTnfft;
epicsShareExtern dset *pvar_dset_devLOFFTstart;
epicsShareExtern dset *pvar_dset_devLOFFTwidth;
epicsShareExtern dset *pvar_dset_devMbbiSoft;
epicsShareExtern dset *pvar_dset_devMbbiSoftRaw;
epicsShareExtern dset *pvar_dset_devPSCRegMbbi;
epicsShareExtern dset *pvar_dset_devPSCRegRBMbbi;
epicsShareExtern dset *pvar_dset_devMbbiDirectSoft;
epicsShareExtern dset *pvar_dset_devMbbiDirectSoftRaw;
epicsShareExtern dset *pvar_dset_devPSCRegMbbiDirect;
epicsShareExtern dset *pvar_dset_devPSCRegRBMbbiDirect;
epicsShareExtern dset *pvar_dset_devPSCTblMbbiDirectAlarms;
epicsShareExtern dset *pvar_dset_devMbboSoft;
epicsShareExtern dset *pvar_dset_devMbboSoftRaw;
epicsShareExtern dset *pvar_dset_devMbboSoftCallback;
epicsShareExtern dset *pvar_dset_devPSCRegMbbo;
epicsShareExtern dset *pvar_dset_devPSCSingleU32Mbbo;
epicsShareExtern dset *pvar_dset_devPSCTblMbboMode;
epicsShareExtern dset *pvar_dset_devMBBOFFTsetwin;
epicsShareExtern dset *pvar_dset_devMbboDirectSoft;
epicsShareExtern dset *pvar_dset_devMbboDirectSoftRaw;
epicsShareExtern dset *pvar_dset_devMbboDirectSoftCallback;
epicsShareExtern dset *pvar_dset_devPSCRegMbboDirect;
epicsShareExtern dset *pvar_dset_devPSCSingleU32MbboDirect;
epicsShareExtern dset *pvar_dset_devSiSoft;
epicsShareExtern dset *pvar_dset_devTimestampSI;
epicsShareExtern dset *pvar_dset_devSiGeneralTime;
epicsShareExtern dset *pvar_dset_devPSCMessageSI;
epicsShareExtern dset *pvar_dset_devPSCBlockSi;
epicsShareExtern dset *pvar_dset_devStringinStats;
epicsShareExtern dset *pvar_dset_devStringinEnvVar;
epicsShareExtern dset *pvar_dset_devStringinEpics;
epicsShareExtern dset *pvar_dset_devSoSoft;
epicsShareExtern dset *pvar_dset_devSoSoftCallback;
epicsShareExtern dset *pvar_dset_devSoStdio;
epicsShareExtern dset *pvar_dset_devPSCBlockSo;
epicsShareExtern dset *pvar_dset_devSASoft;
epicsShareExtern dset *pvar_dset_devWfSoft;
epicsShareExtern dset *pvar_dset_devPSCBlockInWf8;
epicsShareExtern dset *pvar_dset_devPSCBlockOutWf8;
epicsShareExtern dset *pvar_dset_devPSCBlockInWf16;
epicsShareExtern dset *pvar_dset_devPSCBlockOutWf16;
epicsShareExtern dset *pvar_dset_devPSCBlockInWf32;
epicsShareExtern dset *pvar_dset_devPSCBlockOutWf32;
epicsShareExtern dset *pvar_dset_devPSCBlockInWfF32;
epicsShareExtern dset *pvar_dset_devPSCBlockOutWfF32;
epicsShareExtern dset *pvar_dset_devPSCBlockInWfF64;
epicsShareExtern dset *pvar_dset_devPSCBlockOutWfF64;
epicsShareExtern dset *pvar_dset_devPSCTblOutWfTG;
epicsShareExtern dset *pvar_dset_devWFFFTInput;
epicsShareExtern dset *pvar_dset_devWFFFTOutput;
epicsShareExtern dset *pvar_dset_devWFFFTOutputInt;
epicsShareExtern dset *pvar_dset_devWFFFTFScale;
epicsShareExtern dset *pvar_dset_devWFFFTFWindow;

static const char * const deviceSupportNames[117] = {
    "devAaiSoft",
    "devAaoSoft",
    "devAiSoft",
    "devAiSoftRaw",
    "devTimestampAI",
    "devAiGeneralTime",
    "devPSCRegAi",
    "devPSCRegF32Ai",
    "devPSCRegF64Ai",
    "devPSCRegRBAi",
    "devPSCRegRBF32Ai",
    "devPSCRegRBF64Ai",
    "devAIFFTTotPwrTime",
    "devAIFFTTotPwrFreq",
    "devAIFFTLasttime",
    "devAiStats",
    "devAiClusts",
    "devAoSoft",
    "devAoSoftRaw",
    "devAoSoftCallback",
    "devPSCRegAo",
    "devPSCRegF32Ao",
    "devPSCRegF64Ao",
    "devPSCSingleS32Ao",
    "devPSCSingleF32Ao",
    "devPSCSingleF64Ao",
    "devPSCTblAo1Mode",
    "devPSCTblAo2Mode",
    "devAOFFTFSamp",
    "devAOFFTScale",
    "devAoStats",
    "devBiSoft",
    "devBiSoftRaw",
    "devBiASStatus",
    "devPSCConnectedBi",
    "devPSCRegBi",
    "devPSCRegRBBi",
    "devBoSoft",
    "devBoSoftRaw",
    "devBoSoftCallback",
    "devBoGeneralTime",
    "devPSCSendAllBo",
    "devPSCForceReConn",
    "devPSCRegBo",
    "devPSCSingleU32Bo",
    "devCalcoutSoft",
    "devCalcoutSoftCallback",
    "devEventSoft",
    "devHistogramSoft",
    "devLiSoft",
    "devLiGeneralTime",
    "devLiASSum",
    "devPSCUknCountLi",
    "devPSCConnCountLi",
    "devPSCBlockCountLi",
    "devPSCRegLi",
    "devPSCRegRBLi",
    "devLoSoft",
    "devLoSoftCallback",
    "devPSCSendLo",
    "devPSCRegLo",
    "devPSCSingleS32Lo",
    "devPSCTblLoStart",
    "devLOFFTnfft",
    "devLOFFTstart",
    "devLOFFTwidth",
    "devMbbiSoft",
    "devMbbiSoftRaw",
    "devPSCRegMbbi",
    "devPSCRegRBMbbi",
    "devMbbiDirectSoft",
    "devMbbiDirectSoftRaw",
    "devPSCRegMbbiDirect",
    "devPSCRegRBMbbiDirect",
    "devPSCTblMbbiDirectAlarms",
    "devMbboSoft",
    "devMbboSoftRaw",
    "devMbboSoftCallback",
    "devPSCRegMbbo",
    "devPSCSingleU32Mbbo",
    "devPSCTblMbboMode",
    "devMBBOFFTsetwin",
    "devMbboDirectSoft",
    "devMbboDirectSoftRaw",
    "devMbboDirectSoftCallback",
    "devPSCRegMbboDirect",
    "devPSCSingleU32MbboDirect",
    "devSiSoft",
    "devTimestampSI",
    "devSiGeneralTime",
    "devPSCMessageSI",
    "devPSCBlockSi",
    "devStringinStats",
    "devStringinEnvVar",
    "devStringinEpics",
    "devSoSoft",
    "devSoSoftCallback",
    "devSoStdio",
    "devPSCBlockSo",
    "devSASoft",
    "devWfSoft",
    "devPSCBlockInWf8",
    "devPSCBlockOutWf8",
    "devPSCBlockInWf16",
    "devPSCBlockOutWf16",
    "devPSCBlockInWf32",
    "devPSCBlockOutWf32",
    "devPSCBlockInWfF32",
    "devPSCBlockOutWfF32",
    "devPSCBlockInWfF64",
    "devPSCBlockOutWfF64",
    "devPSCTblOutWfTG",
    "devWFFFTInput",
    "devWFFFTOutput",
    "devWFFFTOutputInt",
    "devWFFFTFScale",
    "devWFFFTFWindow"
};

static const dset * const devsl[117] = {
    pvar_dset_devAaiSoft,
    pvar_dset_devAaoSoft,
    pvar_dset_devAiSoft,
    pvar_dset_devAiSoftRaw,
    pvar_dset_devTimestampAI,
    pvar_dset_devAiGeneralTime,
    pvar_dset_devPSCRegAi,
    pvar_dset_devPSCRegF32Ai,
    pvar_dset_devPSCRegF64Ai,
    pvar_dset_devPSCRegRBAi,
    pvar_dset_devPSCRegRBF32Ai,
    pvar_dset_devPSCRegRBF64Ai,
    pvar_dset_devAIFFTTotPwrTime,
    pvar_dset_devAIFFTTotPwrFreq,
    pvar_dset_devAIFFTLasttime,
    pvar_dset_devAiStats,
    pvar_dset_devAiClusts,
    pvar_dset_devAoSoft,
    pvar_dset_devAoSoftRaw,
    pvar_dset_devAoSoftCallback,
    pvar_dset_devPSCRegAo,
    pvar_dset_devPSCRegF32Ao,
    pvar_dset_devPSCRegF64Ao,
    pvar_dset_devPSCSingleS32Ao,
    pvar_dset_devPSCSingleF32Ao,
    pvar_dset_devPSCSingleF64Ao,
    pvar_dset_devPSCTblAo1Mode,
    pvar_dset_devPSCTblAo2Mode,
    pvar_dset_devAOFFTFSamp,
    pvar_dset_devAOFFTScale,
    pvar_dset_devAoStats,
    pvar_dset_devBiSoft,
    pvar_dset_devBiSoftRaw,
    pvar_dset_devBiASStatus,
    pvar_dset_devPSCConnectedBi,
    pvar_dset_devPSCRegBi,
    pvar_dset_devPSCRegRBBi,
    pvar_dset_devBoSoft,
    pvar_dset_devBoSoftRaw,
    pvar_dset_devBoSoftCallback,
    pvar_dset_devBoGeneralTime,
    pvar_dset_devPSCSendAllBo,
    pvar_dset_devPSCForceReConn,
    pvar_dset_devPSCRegBo,
    pvar_dset_devPSCSingleU32Bo,
    pvar_dset_devCalcoutSoft,
    pvar_dset_devCalcoutSoftCallback,
    pvar_dset_devEventSoft,
    pvar_dset_devHistogramSoft,
    pvar_dset_devLiSoft,
    pvar_dset_devLiGeneralTime,
    pvar_dset_devLiASSum,
    pvar_dset_devPSCUknCountLi,
    pvar_dset_devPSCConnCountLi,
    pvar_dset_devPSCBlockCountLi,
    pvar_dset_devPSCRegLi,
    pvar_dset_devPSCRegRBLi,
    pvar_dset_devLoSoft,
    pvar_dset_devLoSoftCallback,
    pvar_dset_devPSCSendLo,
    pvar_dset_devPSCRegLo,
    pvar_dset_devPSCSingleS32Lo,
    pvar_dset_devPSCTblLoStart,
    pvar_dset_devLOFFTnfft,
    pvar_dset_devLOFFTstart,
    pvar_dset_devLOFFTwidth,
    pvar_dset_devMbbiSoft,
    pvar_dset_devMbbiSoftRaw,
    pvar_dset_devPSCRegMbbi,
    pvar_dset_devPSCRegRBMbbi,
    pvar_dset_devMbbiDirectSoft,
    pvar_dset_devMbbiDirectSoftRaw,
    pvar_dset_devPSCRegMbbiDirect,
    pvar_dset_devPSCRegRBMbbiDirect,
    pvar_dset_devPSCTblMbbiDirectAlarms,
    pvar_dset_devMbboSoft,
    pvar_dset_devMbboSoftRaw,
    pvar_dset_devMbboSoftCallback,
    pvar_dset_devPSCRegMbbo,
    pvar_dset_devPSCSingleU32Mbbo,
    pvar_dset_devPSCTblMbboMode,
    pvar_dset_devMBBOFFTsetwin,
    pvar_dset_devMbboDirectSoft,
    pvar_dset_devMbboDirectSoftRaw,
    pvar_dset_devMbboDirectSoftCallback,
    pvar_dset_devPSCRegMbboDirect,
    pvar_dset_devPSCSingleU32MbboDirect,
    pvar_dset_devSiSoft,
    pvar_dset_devTimestampSI,
    pvar_dset_devSiGeneralTime,
    pvar_dset_devPSCMessageSI,
    pvar_dset_devPSCBlockSi,
    pvar_dset_devStringinStats,
    pvar_dset_devStringinEnvVar,
    pvar_dset_devStringinEpics,
    pvar_dset_devSoSoft,
    pvar_dset_devSoSoftCallback,
    pvar_dset_devSoStdio,
    pvar_dset_devPSCBlockSo,
    pvar_dset_devSASoft,
    pvar_dset_devWfSoft,
    pvar_dset_devPSCBlockInWf8,
    pvar_dset_devPSCBlockOutWf8,
    pvar_dset_devPSCBlockInWf16,
    pvar_dset_devPSCBlockOutWf16,
    pvar_dset_devPSCBlockInWf32,
    pvar_dset_devPSCBlockOutWf32,
    pvar_dset_devPSCBlockInWfF32,
    pvar_dset_devPSCBlockOutWfF32,
    pvar_dset_devPSCBlockInWfF64,
    pvar_dset_devPSCBlockOutWfF64,
    pvar_dset_devPSCTblOutWfTG,
    pvar_dset_devWFFFTInput,
    pvar_dset_devWFFFTOutput,
    pvar_dset_devWFFFTOutputInt,
    pvar_dset_devWFFFTFScale,
    pvar_dset_devWFFFTFWindow
};

epicsShareExtern drvet *pvar_drvet_drvPSC;

static const char *driverSupportNames[1] = {
    "drvPSC"
};

static struct drvet *drvsl[1] = {
    pvar_drvet_drvPSC
};

epicsShareExtern void (*pvar_func_asSub)(void);
epicsShareExtern void (*pvar_func_PSCRegister)(void);
epicsShareExtern void (*pvar_func_fftcalcReg)(void);
epicsShareExtern void (*pvar_func_save_restoreRegister)(void);
epicsShareExtern void (*pvar_func_dbrestoreRegister)(void);
epicsShareExtern void (*pvar_func_asInitHooksRegister)(void);
epicsShareExtern void (*pvar_func_configMenuRegistrar)(void);
epicsShareExtern void (*pvar_func_iocshSystemCommand)(void);
epicsShareExtern void (*pvar_func_caPutLogRegister)(void);
epicsShareExtern void (*pvar_func_register_func_subCopyWaveform)(void);
epicsShareExtern void (*pvar_func_register_func_subADCWfProc)(void);
epicsShareExtern void (*pvar_func_register_func_subApplyCoefficient)(void);
epicsShareExtern void (*pvar_func_register_func_subFFT)(void);
epicsShareExtern void (*pvar_func_register_func_subSlice)(void);
epicsShareExtern void (*pvar_func_register_func_subSampling)(void);
epicsShareExtern void (*pvar_func_register_func_subArraySubtraction)(void);
epicsShareExtern void (*pvar_func_register_func_subArrayMovingAverage)(void);
epicsShareExtern void (*pvar_func_register_func_subArrayStatsVariance)(void);
epicsShareExtern void (*pvar_func_register_func_subZero)(void);
epicsShareExtern void (*pvar_func_register_func_subArrayCompare)(void);
epicsShareExtern void (*pvar_func_register_func_fbckSupInit)(void);
epicsShareExtern void (*pvar_func_register_func_fbckSupRMSCalc)(void);
epicsShareExtern void (*pvar_func_register_func_SaStdCalSupInit)(void);
epicsShareExtern void (*pvar_func_register_func_SaStdCalSup)(void);
epicsShareExtern void (*pvar_func_register_func_bpmPosXyUnitConvrsion)(void);
epicsShareExtern void (*pvar_func_register_func_bpmWfmPolyCoeffCalSup)(void);
epicsShareExtern void (*pvar_func_register_func_posPolyCoeffCalSupInit)(void);
epicsShareExtern void (*pvar_func_register_func_posPolyCoeffCalSup)(void);
epicsShareExtern void (*pvar_func_register_func_bpmPosButtonSum)(void);
epicsShareExtern void (*pvar_func_register_func_subEncStreamProc)(void);
epicsShareExtern void (*pvar_func_register_func_subEncFormatProc)(void);
epicsShareExtern void (*pvar_func_register_func_subEncTSProc)(void);
epicsShareExtern void (*pvar_func_register_func_subEncABProc)(void);
epicsShareExtern void (*pvar_func_register_func_subGenStreamProc)(void);
epicsShareExtern void (*pvar_func_register_func_subGenFormatProc)(void);
epicsShareExtern void (*pvar_func_register_func_subGenTSProc)(void);
epicsShareExtern void (*pvar_func_register_func_subGenVoltProc)(void);
epicsShareExtern void (*pvar_func_register_func_subSlice2)(void);
epicsShareExtern void (*pvar_func_register_func_subCalcInit)(void);
epicsShareExtern void (*pvar_func_register_func_subCalcAlarm)(void);
epicsShareExtern void (*pvar_func_register_func_subAlarmCalcInit)(void);
epicsShareExtern void (*pvar_func_register_func_subAlarmCalcProc)(void);
epicsShareExtern void (*pvar_func_register_func_asubAlarmCalcInit)(void);
epicsShareExtern void (*pvar_func_register_func_asubAlarmCalcProc)(void);
epicsShareExtern void (*pvar_func_register_func_wf_stats)(void);
epicsShareExtern void (*pvar_func_register_func_rebootProc)(void);
epicsShareExtern void (*pvar_func_register_func_scanMonInit)(void);
epicsShareExtern void (*pvar_func_register_func_scanMon)(void);

epicsShareExtern int *pvar_int_asCaDebug;
epicsShareExtern int *pvar_int_dbRecordsOnceOnly;
epicsShareExtern int *pvar_int_dbBptNotMonotonic;
epicsShareExtern int *pvar_int_PSCDebug;
epicsShareExtern int *pvar_int_PSCInactivityTime;
epicsShareExtern int *pvar_int_PSCMaxSendBuffer;
epicsShareExtern int *pvar_int_PSCTblCtlDebug;
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
	{"PSCDebug", iocshArgInt, (void * const)pvar_int_PSCDebug},
	{"PSCInactivityTime", iocshArgInt, (void * const)pvar_int_PSCInactivityTime},
	{"PSCMaxSendBuffer", iocshArgInt, (void * const)pvar_int_PSCMaxSendBuffer},
	{"PSCTblCtlDebug", iocshArgInt, (void * const)pvar_int_PSCTblCtlDebug},
	{"save_restoreDebug", iocshArgInt, (void * const)pvar_int_save_restoreDebug},
	{"save_restoreNumSeqFiles", iocshArgInt, (void * const)pvar_int_save_restoreNumSeqFiles},
	{"save_restoreSeqPeriodInSeconds", iocshArgInt, (void * const)pvar_int_save_restoreSeqPeriodInSeconds},
	{"save_restoreIncompleteSetsOk", iocshArgInt, (void * const)pvar_int_save_restoreIncompleteSetsOk},
	{"save_restoreDatedBackupFiles", iocshArgInt, (void * const)pvar_int_save_restoreDatedBackupFiles},
	{"save_restoreRemountThreshold", iocshArgInt, (void * const)pvar_int_save_restoreRemountThreshold},
	{"configMenuDebug", iocshArgInt, (void * const)pvar_int_configMenuDebug},
	{NULL, iocshArgInt, NULL}
};

int psc_registerRecordDeviceDriver(DBBASE *pbase)
{
    const char *bldTop = "/epics/iocs/pscdrv";
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

    registerRecordTypes(pbase, 30, recordTypeNames, rtl);
    registerDevices(pbase, 117, deviceSupportNames, devsl);
    registerDrivers(pbase, 1, driverSupportNames, drvsl);
    (*pvar_func_asSub)();
    (*pvar_func_PSCRegister)();
    (*pvar_func_fftcalcReg)();
    (*pvar_func_save_restoreRegister)();
    (*pvar_func_dbrestoreRegister)();
    (*pvar_func_asInitHooksRegister)();
    (*pvar_func_configMenuRegistrar)();
    (*pvar_func_iocshSystemCommand)();
    (*pvar_func_caPutLogRegister)();
    (*pvar_func_register_func_subCopyWaveform)();
    (*pvar_func_register_func_subADCWfProc)();
    (*pvar_func_register_func_subApplyCoefficient)();
    (*pvar_func_register_func_subFFT)();
    (*pvar_func_register_func_subSlice)();
    (*pvar_func_register_func_subSampling)();
    (*pvar_func_register_func_subArraySubtraction)();
    (*pvar_func_register_func_subArrayMovingAverage)();
    (*pvar_func_register_func_subArrayStatsVariance)();
    (*pvar_func_register_func_subZero)();
    (*pvar_func_register_func_subArrayCompare)();
    (*pvar_func_register_func_fbckSupInit)();
    (*pvar_func_register_func_fbckSupRMSCalc)();
    (*pvar_func_register_func_SaStdCalSupInit)();
    (*pvar_func_register_func_SaStdCalSup)();
    (*pvar_func_register_func_bpmPosXyUnitConvrsion)();
    (*pvar_func_register_func_bpmWfmPolyCoeffCalSup)();
    (*pvar_func_register_func_posPolyCoeffCalSupInit)();
    (*pvar_func_register_func_posPolyCoeffCalSup)();
    (*pvar_func_register_func_bpmPosButtonSum)();
    (*pvar_func_register_func_subEncStreamProc)();
    (*pvar_func_register_func_subEncFormatProc)();
    (*pvar_func_register_func_subEncTSProc)();
    (*pvar_func_register_func_subEncABProc)();
    (*pvar_func_register_func_subGenStreamProc)();
    (*pvar_func_register_func_subGenFormatProc)();
    (*pvar_func_register_func_subGenTSProc)();
    (*pvar_func_register_func_subGenVoltProc)();
    (*pvar_func_register_func_subSlice2)();
    (*pvar_func_register_func_subCalcInit)();
    (*pvar_func_register_func_subCalcAlarm)();
    (*pvar_func_register_func_subAlarmCalcInit)();
    (*pvar_func_register_func_subAlarmCalcProc)();
    (*pvar_func_register_func_asubAlarmCalcInit)();
    (*pvar_func_register_func_asubAlarmCalcProc)();
    (*pvar_func_register_func_wf_stats)();
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
                {"psc_registerRecordDeviceDriver",1,registerRecordDeviceDriverArgs};
static void registerRecordDeviceDriverCallFunc(const iocshArgBuf *)
{
    psc_registerRecordDeviceDriver(*iocshPpdbbase);
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
