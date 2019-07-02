/*
 *	Bpm array calculation.
 *
 */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <dbAccess.h>
#include <dbDefs.h>
#include <dbFldTypes.h>
#include <registryFunction.h>
#include <aSubRecord.h>
#include <waveformRecord.h>
#include <epicsExport.h>
#include <epicsTime.h>

/* TBT and FA waveform 'nm' to 'mm' unit conversion */
static long bpmPosXyUnitConvrsion(aSubRecord *pasub)
{
int i;
	static float  *px, *py;
	static float data_x[200000];		/* max 200k */
	static float data_y[200000];
	static long *pN;
	static long N;

	// read N
	pN =  (long *)pasub->d;
	N =  (long)(*pN);

	long* pvalue = pasub->c;

	px = (float *)pasub->a;
	py = (float *)pasub->b;

	//printf("max len = %d,   %d\n", pasub->noa, *pvalue );	
	if (*pvalue == 0) {
		//for (i=0; i<pasub->noa; i++) {
		for (i=0; i<N; i++) {
			data_x[i] = *(px+i) * 0.000001;	/* nm to mm */
			data_y[i] = *(py+i) * 0.000001;
	//		printf("%d x =  %.0f, %f, y = %.0f, %f\n", i, *(px+i), data_x[i], *(py+i), data_y[i]);		}
		}
		memcpy(pasub->vala, data_x, pasub->noa*sizeof(float) );
		memcpy(pasub->valb, data_y, pasub->noa*sizeof(float) );
	}
	else {	
		memset(pasub->vala, 0, pasub->noa*sizeof(float) );
		memset(pasub->valb, 0, pasub->noa*sizeof(float) );	
	}

		
	return(0);
}



/*
 *
 record(aSub, "$(P){BPM:$(NO)}PY:Tbt-Calc")
{
        field(SNAM, "bpmWfmPolyCoeffCalSup")
        field(INPA, "$(P){BPM:$(NO)}TBT-X")
        field(INPB, "$(P){BPM:$(NO)}TBT-Y")
        field(INPC,  "$(P){BPM:$(NO)}K:Ky10-SP")
        field(INPD,  "$(P){BPM:$(NO)}K:Ky12-SP")
        field(INPE,  "$(P){BPM:$(NO)}K:Ky30-SP")
		
        field(INPF,  "$(P){BPM:$(NO)}Kx-SP")
        field(INPG,  "$(P){BPM:$(NO)}Ky-SP")		
        field(INPH,  "$(P){BPM:$(NO)}BbaXOff-SP")
        field(INPI,  "$(P){BPM:$(NO)}BbaYOff-SP")	
		
        field(FTA,  "FLOAT")
        field(FTB,  "FLOAT")
        field(FTC,  "FLOAT")
        field(FTD,  "FLOAT")
        field(FTE,  "FLOAT")
		
        field(FTF,  "FLOAT")
        field(FTG,  "FLOAT")
        field(FTH,  "FLOAT")
        field(FTI,  "FLOAT")	
		
        field(NOA,  "$(TBT_WFM_LEN)")
        field(NOB,  "$(TBT_WFM_LEN)")
        field(NOC,  "1")
        field(NOD,  "1")
        field(NOE,  "1")
        field(OUTA, "$(P){BPM:$(NO)}PY:Tbt-x PP")
        field(OUTB, "$(P){BPM:$(NO)}PY:Tbt-y PP")
        field(NOVA, "$(TBT_WFM_LEN)")
        field(NOVB, "$(TBT_WFM_LEN)")
        field(NOVC, "1")
        field(NOVD, "1")
        field(NOVE, "1")
        field(FTVA, "FLOAT")
        field(FTVB, "FLOAT")
        field(FTVC, "FLOAT")
        field(FTVD, "FLOAT")
        field(FTVE, "FLOAT")
}


 */
static long bpmWfmPolyCoeffCalSup(aSubRecord *pasub)
{
	int i;
	static float  *px, *py;
	static float data_x[200000];		/* max 200k */
	static float data_y[200000];
	static float *pK10, *pK12, *pK30;
	static float *pKx, *pKy;
	static float *pBbaOffset_x, *pBbaOffset_y;
	
	static float  Kx, Ky, bba_off_x, bba_off_y, x, y, K1, K3, K5, xp3, xp5, yp3, yp5, sum;
	static float  x_sum_linear;
	static float  y_sum_linear;
	

	px   =  (float *)pasub->a;	/* x position */
	py   =  (float *)pasub->b;	/* y position */
	pK10 =  (float *)pasub->c;
	pK12 =  (float *)pasub->d;
	pK30 =  (float *)pasub->e;
	//Kx, Ky
	pKx =  (float *)pasub->f;
	pKy =  (float *)pasub->g;
	pBbaOffset_x =  (float *)pasub->h;
	pBbaOffset_y =  (float *)pasub->i;
	
	K1   =  (float)(*pK10);
	K3   =  (float)(*pK12);
	K5   =  (float)(*pK30);
	Kx   =  (float)(*pKx);
	Ky   =  (float)(*pKy);
	bba_off_x = (float) (*pBbaOffset_x);
	bba_off_y = (float) (*pBbaOffset_y);
	
	
	//printf("max len = %d, %f, %f, %f\n", pasub->noa, k10, k12, k30);	
	for (i=0; i<pasub->noa; i++) 
	{
		x = *(px+i) * 0.000001;	/* nm to mm */
		y = *(py+i) * 0.000001;	/* nm to mm */
		//printf("%d x =  %.0f, y = %.0f\n", i, x, y);
		
		x_sum_linear = ( x - bba_off_x) / Kx;
		xp3 = pow(x_sum_linear, 3);
		xp5 = pow(x_sum_linear, 5);

		y_sum_linear = ( y - bba_off_y) / Ky ;
		yp3 = pow(y_sum_linear, 3);
		yp5 = pow(y_sum_linear, 5);	
		
		data_x[i] = (K1*x_sum_linear + K3*xp3 + K5*xp5) + bba_off_x;		
		data_y[i] = (K1*y_sum_linear + K3*yp3 + K5*yp5) + bba_off_y;
		//printf("%d x =  %f, %f, y = %f, %f\n", i, x, data_x[i], y, data_y[i] );
	}
	memcpy(pasub->vala, data_x, pasub->noa*sizeof(float) );
	memcpy(pasub->valb, data_y, pasub->noa*sizeof(float) );

	
  	return 0;
}



#if 0
// Button SUM
static long bpmPosButtonSum(aSubRecord *pasub)
{
int i;
	static long  *pA, *pB, *pC, *pD;
	static long data_sum[200000];		/* max 200k */
	
	pA = (long *)pasub->a;
	pB = (long *)pasub->b;
	pC = (long *)pasub->c;
	pD = (long *)pasub->d;

	
//	printf("max len = %d\n", pasub->noa);	
	for (i=0; i<pasub->noa; i++) {
		data_sum[i] = *(pA+i) + *(pB+i) + *(pC+i) + *(pD+i) ;	/* nm to mm */
	//	printf("%d a=%d, b=%d, c= %d, d=%d, sum=%d\n", i, *(pA+i), *(pB+i), *(pC+i), *(pD+i), data_sum[i]);
	}
	memcpy(pasub->vala, data_sum, pasub->noa*sizeof(long) );
		
	return(0);
}
#endif

static long bpmPosButtonSum(aSubRecord *pasub)
{
int i;
int	len;
	static long  *pA, *pB, *pC, *pD;
	static float bsum[200000];           /* max 200k */
	static float ab[200000];
	static float bb[200000];
	static float cb[200000];
	static float db[200000];
	static long *pN;
	static long N;

	pA = (long *)pasub->a;
	pB = (long *)pasub->b;
	pC = (long *)pasub->c;
	pD = (long *)pasub->d;

	// read N
	pN =  (long *)pasub->e;
	N =  (long)(*pN);

#if 1
//	printf("max len = %d, %d\n", N, pasub->noa);
//	for (i=0; i < pasub->noa; i++) {
	for (i=0; i < N; i++) {
		ab[i] = (float) (*(pA+i) * 4.656612875245797e-10);	//2^31
		bb[i] = (float) (*(pB+i) * 4.656612875245797e-10);
		cb[i] = (float) (*(pC+i) * 4.656612875245797e-10);
		db[i] = (float) (*(pD+i) * 4.656612875245797e-10);
		bsum[i] = ab[i] + bb[i] + cb[i] + db[i] ;  
	//  printf("%d a=%f, b=%f, c= %f, d=%f, sum=%f\n", i,  ab[i],  bb[i],  cb[i],  db[i], bsum[i]);
	}	
#endif

	len = pasub->noa*sizeof(float);
	memcpy(pasub->vala, ab,  len);
	memcpy(pasub->valb, bb, len );
	memcpy(pasub->valc, cb, len );
	memcpy(pasub->vald, db, len );
	memcpy(pasub->vale, bsum, len );
	//printf("%d  len=%d\n", N, len);

	return(0);
}


epicsRegisterFunction(bpmPosXyUnitConvrsion);
epicsRegisterFunction(bpmWfmPolyCoeffCalSup);
epicsRegisterFunction(bpmPosButtonSum);

