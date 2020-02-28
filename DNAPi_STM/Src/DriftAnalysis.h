#ifndef __DRIFTANALYSIS_H
#define __DRIFTANALYSIS_H

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f4xx_hal.h"
#include "tm_stm32_ds18b20.h"
#include "main.h"
#include <stdlib.h>

/**************************/
/* EXTERNAL FUNCTIONS 		*/
/**************************/
extern TIM_HandleTypeDef htim7;
extern void Calib_Array_Chem_STM(volatile int*);
extern void ObtainAndSendFrame_Chem(volatile int*);
/**************************/

/**************************/
/* FSM VARIABLES 					*/
/**************************/
enum DA_States { 
									FSM_Start, CalibrateArray, RefElectSens, DACSens, // Initial phase - Calibration
									Sample, WaitSampleRPi, RecieveValues,
									FSM_Finished
} DA_State;
int Sampling_ElapsedTime;
/**************************/

void TickFSM_DA(volatile int*);

/***********/
/* DRIVERS */
/***********/
void Start_SamplingTimer(void);
void Stop_SamplingTimer(void);
/***********/

/****************************************************/

void TickFSM_DA(volatile int* FrameBuf){

	// Mealy FSM
	switch(DA_State) { // Transitions & Actions
		case FSM_Start: 								// Initial transition
			DA_State = CalibrateArray;
			Calib_Array_Chem_STM(FrameBuf);
			break;
		
		case CalibrateArray:						// Calibrate Array
			DA_State = Sample;
			Start_SamplingTimer();
			break;
			
		case Sample:					// Sampling for 30 seconds
			if(Sampling_ElapsedTime < 30){
				ObtainAndSendFrame_Chem(FrameBuf);
			}
			else{
				Stop_SamplingTimer();
				DA_State = FSM_Finished;
			}
			break;
		
		case WaitSampleRPi:	// Wait for RPi Confirmation
			break;

		case FSM_Finished:
			break;
		
		default:								// If error, send to start if error
			DA_State = FSM_Start;
			break;
	} // End Transitions

}

/**********************************/
/* DRIVERS 												*/
/**********************************/
void Start_SamplingTimer(void){
	HAL_TIM_Base_Start_IT(&htim7);
	Sampling_ElapsedTime = 0;
}

void Stop_SamplingTimer(void){
	HAL_TIM_Base_Stop_IT(&htim7);
}

#endif /* __DRIFTANALYSIS_H */
