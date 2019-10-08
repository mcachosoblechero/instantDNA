#ifndef __INSTANTDNA_H
#define __INSTANTDNA_H

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f4xx_hal.h"
#include "main.h"
#include <stdlib.h>

// DAC SELECTION
#define DAC_VREF 			0x00
#define DAC_VBIAS 		0x01
#define DAC_IOTA 			0x02
#define DAC_REFELEC		0x03

// CHIP INTERFACE
#define ISFET_OFF			0x00
#define ISFET_ON 			0x01
#define DAC_INTERNAL	0x00
#define DAC_EXTERNAL 	0x01
#define DAC_ACTIVE		0x00
#define DAC_DEBUGMODE 0x01

// RPI ACTIONS
#define HELLOWORLD			0x00
#define SET_DAC_VREF		0x01
#define SET_DAC_VBIAS		0x02
#define SET_DAC_IOTA		0x03
#define SET_DAC_REFE		0x04
#define TEST_ONCHIPDAC  0x05
#define OBTAIN_FRAME  	0x06
#define CHARACTCURVES		0x07
#define CALIB_ARRAY			0x08
#define INCREASE_PH			0x09

#define PIXEL_TIMEOUT		84000 // -> 1ms @ 84MHz

// PLATFORM DEFAULTS
#define NUMROWS				0x20			// 32
#define NUMCOLS				0x20			// 32
#define NUMPIXELS			1024
#define DAC_VREF_DEFAULT			0.0
#define DAC_VBIAS_DEFAULT			0.272
#define DAC_IOTA_DEFAULT			0.3
#define DAC_REFELECT_DEFAULT	0.0

// CALIBRATION PARAMETERS
#define CALIB_MAXITER		25
#define CALIB_MINLRANGE	0.48
#define CALIB_MAXLRANGE	0.52
#define CONTROLLER_KP		200
#define ON_LIMIT				0.85
#define OFF_LIMIT				0.15

/************* PLATFORM VARIABLES ***********/
extern DAC_HandleTypeDef hdac;

extern SPI_HandleTypeDef hspi1;
extern SPI_HandleTypeDef hspi2;

extern TIM_HandleTypeDef htim2;
extern TIM_HandleTypeDef htim3;
extern TIM_HandleTypeDef htim5;
/********************************************/

/************* GLOBAL VARIABLES *************/
struct PlatformParameters {

	char NumRows;
	char NumColumns;
	
	float DAC_VRef_Voltage;
	float DAC_VBias_Voltage;
	float DAC_IOTA_Voltage;
	float DAC_RefElect_Voltage;
	
	int CalibrationBuffer[1024];
	float DutyCycleBuffer[1024];
	
};

struct TimerChannelParam {

	__IO uint32_t TicksPeriod;
	__IO uint32_t TicksHigh;
	__IO uint32_t NumSamples;
	__IO float Frequency;
	__IO float DutyCycle;
	__IO char ValidSample;
	
};

int i;
uint8_t buf[5];
char RPi_ActionReq;
char RPi_Param[4];
uint8_t tx[5] = {0x00, 0x00, 0xAB, 0x00, 0xCD};
int counter=0;
uint16_t data_to_send;
volatile int spi_int_counter = 0;
volatile int ctrl = 0;
static volatile char SPIMessage_Available = 0;

volatile struct PlatformParameters instantDNA;
volatile struct TimerChannelParam TimerCh2;
volatile int FrameBuffer[2048];

/* IRQ Variables */

volatile char PixTimeout = 0;

/*********************************************/

// FUNCTIONS HEADERS
/******* HIGH LEVEL FUNCTIONS *************/
void InitPlatform(void);
void ObtainAndSendFrame(volatile int*);
void TestOnChipDAC_Platform(void);
void ObtainCharactCurves(volatile int*);
void Calib_Array_STM(volatile int*);
/******* DRIVERS **************************/
void WaitSPICommand(void);
uint16_t voltage_to_dac(float voltage, float max, float min);
uint16_t dac_to_binary(uint16_t dac_value);
void setup_DAC(char DAC_Select);
void setup_Chip(char Enable, char Row, char Column, int DAC_Value, char DAC_Source, char DAC_Debug);
void Start_Timers(void);
void Stop_Timers(void);
volatile int* ObtainFrame(volatile int*);
void SendFrame_RPi(volatile int*);
void CalculateFrameDutyCycle(volatile int*);
int CalibrationController(float);

/*********************************************************************/

// FUNCTIONS DEFINITION
/*********** HIGH LEVEL FUNCTIONS **************************/
void InitPlatform(void){
	
	instantDNA.NumRows = NUMROWS;
	instantDNA.NumColumns = NUMCOLS;
	instantDNA.DAC_VRef_Voltage = DAC_VREF_DEFAULT;
	instantDNA.DAC_VBias_Voltage = DAC_VBIAS_DEFAULT;
	instantDNA.DAC_IOTA_Voltage = DAC_IOTA_DEFAULT;
	instantDNA.DAC_RefElect_Voltage = DAC_REFELECT_DEFAULT;
	for (i = 0; i < 1024; i++) instantDNA.CalibrationBuffer[i] = 1024;
	
}

void ObtainAndSendFrame(volatile int *FrameBuf){
	
	FrameBuf = ObtainFrame(FrameBuf);
	SendFrame_RPi(FrameBuf);
	
}

void TestOnChipDAC_Platform(void){

	float DAC_Value;
	int i;
	
	for (i=0;i<2048;i++) {
		DAC_Value = i;
		setup_Chip(ISFET_OFF,0, 0, DAC_Value,DAC_INTERNAL,DAC_DEBUGMODE);
		HAL_Delay(1);
	}

}

void ObtainCharactCurves(volatile int *FrameBuf){
	
	instantDNA.DAC_RefElect_Voltage = -1.5;
	
	while (instantDNA.DAC_RefElect_Voltage < (float)1.5){
		setup_DAC(DAC_REFELEC);
		FrameBuf = ObtainFrame(FrameBuf);
		FrameBuf = ObtainFrame(FrameBuf); // Second frame for stabilisation
		SendFrame_RPi(FrameBuf);
		instantDNA.DAC_RefElect_Voltage += (float)0.025;
		
	}

}

void Calib_Array_STM(volatile int *FrameBuf){

	int NumCalibPixels = 0;
	int NumIter = 0;
	int pixel;
	
	int PrevNumPixels_Osc = 0;
	int NumPixels_Osc = 0;
	int NumPixels_Off = 0;
	int NumPixels_On = 0;
	int Flag = 0;
	float RefStep;
	
	/****************************************/
	/* Step 0 - Initialise Variables				*/
	/****************************************/
	
	/****************************************/
	/* Step 1 - Set Ideal Ref								*/
	/****************************************/
	// Initialise Ref Elect to zero
	instantDNA.DAC_RefElect_Voltage = 0.0;
	setup_DAC(DAC_REFELEC);
	
	// Obtain sample
	FrameBuf = ObtainFrame(FrameBuf);
	CalculateFrameDutyCycle(FrameBuf);
	for(pixel=0;pixel<NUMPIXELS;pixel++){
		if (instantDNA.DutyCycleBuffer[pixel] > (float)ON_LIMIT) NumPixels_On++;
		else if (instantDNA.DutyCycleBuffer[pixel] < (float)OFF_LIMIT) NumPixels_Off++;
		else NumPixels_Osc++;
	}
	
	if (NumPixels_Off > NumPixels_On) RefStep = -0.1;
	else RefStep = 0.1;
	
	while(!Flag){
		instantDNA.DAC_RefElect_Voltage += RefStep;
		setup_DAC(DAC_REFELEC);
		
		FrameBuf = ObtainFrame(FrameBuf);
		CalculateFrameDutyCycle(FrameBuf);
		PrevNumPixels_Osc = NumPixels_Osc;
		NumPixels_Osc = 0;
		NumPixels_On = 0;
		NumPixels_Off = 0;
		for(pixel=0;pixel<NUMPIXELS;pixel++){
			if (instantDNA.DutyCycleBuffer[pixel] > (float)ON_LIMIT) NumPixels_On++;
			else if (instantDNA.DutyCycleBuffer[pixel] < (float)OFF_LIMIT) NumPixels_Off++;
			else NumPixels_Osc++;
		}
		
		if ((NumPixels_Osc - PrevNumPixels_Osc < 0) && (PrevNumPixels_Osc > 200)) Flag = 1;
		SendFrame_RPi(FrameBuf);
	}
	
	instantDNA.DAC_RefElect_Voltage -= RefStep;
	setup_DAC(DAC_REFELEC);
	
	/****************************************/
	/* Step 2 - Set Calib Values						*/
	/****************************************/
	while (NumCalibPixels < NUMPIXELS && NumIter < CALIB_MAXITER){
	
		FrameBuf = ObtainFrame(FrameBuf);
		CalculateFrameDutyCycle(FrameBuf);
		NumCalibPixels = 0;
		
		for(pixel=0;pixel<NUMPIXELS;pixel++){
			// IF Pixel is in range or CalibDac is out of range
			if ((instantDNA.DutyCycleBuffer[pixel] >= (float)CALIB_MINLRANGE && 
					instantDNA.DutyCycleBuffer[pixel] <= (float)CALIB_MAXLRANGE) || 
					instantDNA.CalibrationBuffer[pixel] <= 0 || 
					instantDNA.CalibrationBuffer[pixel] >= 2047){
				NumCalibPixels++;
			}
			
			// Controller
			instantDNA.CalibrationBuffer[pixel] += CalibrationController(instantDNA.DutyCycleBuffer[pixel]);
			
			// Prevent overflow
			if (instantDNA.CalibrationBuffer[pixel] > 2047) instantDNA.CalibrationBuffer[pixel] = 2047;
			else if (instantDNA.CalibrationBuffer[pixel] < 0) instantDNA.CalibrationBuffer[pixel] = 0;
		}

		// Calculate NumCalibPixels
		NumIter++;	
		SendFrame_RPi(FrameBuf);
		
	}
	
	// SEND End Of Action
	for(pixel=0; pixel<2048; pixel++){
		FrameBuf[pixel] = 0xAAAAAAAA;
	}
	SendFrame_RPi(FrameBuf);
	
	
}

/************************ DRIVERS **************************/

void Start_Timers(void){

	/* Start the timer */
	if (HAL_TIM_IC_Start_IT(&htim2, TIM_CHANNEL_1) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_IC_Start_IT(&htim2, TIM_CHANNEL_2) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_Base_Start_IT(&htim3) != HAL_OK)
	{
		Error_Handler();
	}
	/*******************/
	
}

void Stop_Timers(void){

	/* Close the timer */
	if (HAL_TIM_IC_Stop_IT(&htim2, TIM_CHANNEL_1) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_IC_Stop_IT(&htim2, TIM_CHANNEL_2) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_Base_Stop_IT(&htim3) != HAL_OK)
	{
		Error_Handler();
	}
	/*******************/
	
}

void WaitSPICommand(void){

	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)tx, (uint8_t*)buf, 5);
	while (SPIMessage_Available == 0x00){}
	SPIMessage_Available = 0;
	
}

uint16_t voltage_to_dac(float voltage, float max, float min)
{
	uint16_t dac_value = 0;
	if (voltage > max)
	{
		dac_value = 0xFFF;
	}else if (voltage < min)
	{
		dac_value = 0;
	}else
	{
		dac_value = (uint16_t)(((float)4096/(max-min))*voltage);
	}
	return dac_value;
}	

uint16_t dac_to_binary(uint16_t dac_value)
{
	dac_value = (dac_value & 0x0FFF)<<2;
	dac_value = (((dac_value & 0xFF)<<8) + (dac_value >> 8));
	return dac_value;
}

void setup_DAC(char DAC_Select)
{
	
	uint16_t dac_value;

	switch(DAC_Select){
		case DAC_VREF:
			data_to_send = dac_to_binary(voltage_to_dac(instantDNA.DAC_VRef_Voltage, 3.24, 0));
			HAL_GPIO_WritePin(GPIOC, V_REF_CS_Pin, GPIO_PIN_RESET);
			HAL_SPI_Transmit(&hspi2, (uint8_t*)&data_to_send, 2, 256);
			HAL_GPIO_WritePin(GPIOC, V_REF_CS_Pin, GPIO_PIN_SET);
			break;
			
		case DAC_VBIAS:
			data_to_send = dac_to_binary(voltage_to_dac(instantDNA.DAC_VBias_Voltage, 3.24, 0));
			HAL_GPIO_WritePin(GPIOC, V_BIAS_CS_Pin, GPIO_PIN_RESET);
			HAL_SPI_Transmit(&hspi2, (uint8_t*)&data_to_send, 2, 256);
			HAL_GPIO_WritePin(GPIOC, V_BIAS_CS_Pin, GPIO_PIN_SET);
			break;
		
		case DAC_IOTA:
			data_to_send = dac_to_binary(voltage_to_dac(instantDNA.DAC_IOTA_Voltage, 3.24, 0));
			HAL_GPIO_WritePin(GPIOC, IOTA_CS_Pin, GPIO_PIN_RESET);
			HAL_SPI_Transmit(&hspi2, (uint8_t*)&data_to_send, 2, 256);
			HAL_GPIO_WritePin(GPIOC, IOTA_CS_Pin, GPIO_PIN_SET);
			break;
		
		case DAC_REFELEC:
			dac_value = voltage_to_dac(instantDNA.DAC_RefElect_Voltage+5, 10, 0);
			data_to_send = dac_to_binary(dac_value);
			HAL_GPIO_WritePin(GPIOA, REF_E_CS_Pin, GPIO_PIN_RESET);
			HAL_SPI_Transmit(&hspi2, (uint8_t*)&data_to_send, 2, 256);
			HAL_GPIO_WritePin(GPIOA, REF_E_CS_Pin, GPIO_PIN_SET);
			break;
	}
}

void setup_Chip(char Enable, char Row, char Column, int DAC_Value, char DAC_Source, char DAC_Debug){
	
	uint8_t Chip_Byte1 = 0;
	uint8_t Chip_Byte2 = 0;
	uint8_t Chip_Byte3 = 0;
	uint16_t DAC_Input = 0;
	
	if (DAC_Value > 2047) DAC_Input = 0x7FF;
	else if (DAC_Value < 0) DAC_Input = 0;
	else DAC_Input = DAC_Value;
	
	Chip_Byte1 = ((Enable & 0x01) << 7) | ((Row & 0x1F) << 2) | ((Column & 0x18) >> 3);
	Chip_Byte2 = ((Column & 0x07) << 5) | ((DAC_Input & 0x07C0) >> 6);
	Chip_Byte3 = ((DAC_Input & 0x003F) << 2) | ((DAC_Source & 0x01) << 1) | (DAC_Debug & 0x01);

	HAL_GPIO_WritePin(GPIOA, CHIP_CS_Pin, GPIO_PIN_RESET);
	HAL_SPI_Transmit(&hspi2, (uint8_t*)&Chip_Byte1, 1, 256);
	HAL_SPI_Transmit(&hspi2, (uint8_t*)&Chip_Byte2, 1, 256);
	HAL_SPI_Transmit(&hspi2, (uint8_t*)&Chip_Byte3, 1, 256);
	HAL_GPIO_WritePin(GPIOA, CHIP_CS_Pin, GPIO_PIN_SET);
	
}

volatile int* ObtainFrame(volatile int* FrameBuf){

	int row;
	int column;
	
	// SETUP External DACs
	// Loop around pixels and obtain measurement
	Start_Timers(); // Start Timers
	
	for (column = 0; column < instantDNA.NumColumns; column++){
		for (row = 0; row < instantDNA.NumRows; row++){
			
				// SETUP CHIP
				setup_Chip(ISFET_ON,row, column, instantDNA.CalibrationBuffer[row+column*NUMROWS],DAC_INTERNAL,DAC_ACTIVE); 
				while (PixTimeout == 0x00){} // Wait until end of pix measurement
					
				// Store variables
				FrameBuf[(row+column*NUMROWS)*2] = TimerCh2.TicksHigh; 
				FrameBuf[(row+column*NUMROWS)*2+1] = TimerCh2.TicksPeriod;
			
				// Restart variables
				PixTimeout = 0;
				TimerCh2.TicksHigh = 0;
				TimerCh2.TicksPeriod = 0;
				TimerCh2.NumSamples = 0;
				TimerCh2.ValidSample = 0;
					
		}
	}
	
	Stop_Timers();
	return FrameBuf;
	
}

void SendFrame_RPi(volatile int* FrameBuf){

	// ASSERT RPi IRQ WHEN FRAME DONE
	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)FrameBuf, (uint8_t *)FrameBuf, 8192);
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_SET);
	while (SPIMessage_Available == 0x00){}
	SPIMessage_Available = 0;
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_RESET);

}

void CalculateFrameDutyCycle(volatile int* FrameBuf){

	int pixel;
	
	for(pixel=0;pixel<NUMPIXELS;pixel++){
		instantDNA.DutyCycleBuffer[pixel] = (float)FrameBuf[(pixel*2)] / (float)FrameBuf[(pixel*2)+1];
	}
	
}

int CalibrationController(float DutyCycle){

	int DeltaDAC;
	
	// K Controller - Not working yet
	DeltaDAC = (int)((float)CONTROLLER_KP * ((float)0.5 - DutyCycle));

	// If-statements based
	/*if (DutyCycle < (float) 0.05) DeltaDAC = 200;
	else if (DutyCycle < (float) 0.25) DeltaDAC = 50;
	else if (DutyCycle < (float) 0.35) DeltaDAC = 10;
	else if (DutyCycle < (float) 0.48) DeltaDAC = 5;
	else if (DutyCycle < (float) 0.5) DeltaDAC =  1;
	else if (DutyCycle > (float) 0.95) DeltaDAC = (-200);
	else if (DutyCycle > (float) 0.75) DeltaDAC = (-50);
	else if (DutyCycle > (float) 0.65) DeltaDAC = (-10);
	else if (DutyCycle > (float) 0.52) DeltaDAC = (-5);
	else if (DutyCycle > (float) 0.5) DeltaDAC = (-1);
	else DeltaDAC = 0;*/
	
	return DeltaDAC;
	
}

#endif /* __INSTANTDNA_H */
