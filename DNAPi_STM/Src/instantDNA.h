#ifndef __INSTANTDNA_H
#define __INSTANTDNA_H

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f4xx_hal.h"
#include "tm_stm32_ds18b20.h"
#include "main.h"
#include <stdlib.h>

// DAC SELECTION
#define DAC_VREF 			0x00
#define DAC_VBIAS 		0x01
#define DAC_IOTA 			0x02
#define DAC_REFELEC		0x03
#define DAC_PELTIER		0x04

// CHIP INTERFACE
#define ISFET_OFF			0x00
#define ISFET_ON 			0x01
#define DAC_INTERNAL	0x00
#define DAC_EXTERNAL 	0x01
#define DAC_ACTIVE		0x00
#define DAC_DEBUGMODE 0x01

// RPI ACTIONS
#define HELLOWORLD				0x00
#define SET_DAC_VREF			0x01
#define SET_DAC_VBIAS			0x02
#define SET_DAC_IOTA			0x03
#define SET_DAC_REFE			0x04
#define TEST_ONCHIPDAC  	0x05
#define OBTAIN_FRAME  		0x06
#define CHARACTCURVES			0x07
#define CALIB_ARRAY				0x08
#define INCREASE_PH				0x09
#define LAMP_CONTROL			0x0A
#define PCR_CONTROL				0x0B
#define TEMP_CONTROL 			0x0C
#define TEMP_CHARACT			0x0D
#define TEMP_REFMEAS			0x0E
#define TEMP_NOISE 				0x0F

#define PIXEL_TIMEOUT		10 // -> 1ms @ 84MHz
#define PIXEL_PRESCALER 4		// -> 1 sample every 4 samples

// PLATFORM DEFAULTS
#define NUMROWS				0x20			// 32
#define NUMCOLS				0x20			// 32
#define NUMPIXELS			1024
#define DAC_VREF_DEFAULT			0.0
#define DAC_VBIAS_DEFAULT			0.272
#define DAC_IOTA_DEFAULT			0.3
#define DAC_REFELECT_DEFAULT	0.0
#define DAC_PELTIER_DEFAULT 	0.0

// CALIBRATION PARAMETERS
#define CALIB_DC_MAXITER			25
#define CALIB_DC_MINLRANGE		0.48
#define CALIB_DC_MAXLRANGE		0.52
#define CALIB_FREQ_MAXITER		10
#define CALIB_FREQ_MINLRANGE	0.48
#define CALIB_FREQ_MAXLRANGE	0.52
#define TEMP_ROW							16
#define TEMP_COLUMN						16
#define CONTROLLER_KP					175
#define ON_LIMIT							0.85
#define OFF_LIMIT							0.15

// TEST PARAMETERS
#
#define SAMPLES_TNOISE					100000
#define SAMPLES_TCHARACT				10
#define SAMPLES_REFTEMP					100

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
	float DAC_Peltier_Voltage;
	float Platform_Temp;
	
	int CalibrationBuffer_DutyCycle[1024];
	int CalibrationBuffer_Frequency[1024];
	float DutyCycleBuffer[1024];
	
};

struct TimerChannelParam {
	__IO uint32_t TicksPeriod_Sample;
	__IO uint32_t TicksHigh_Sample;
	
	__IO uint32_t Prev_TicksPeriod_Sample;
	__IO uint32_t Prev_TicksHigh_Sample;

	__IO char ActiveMeas;
	__IO char FirstIgnored;
	__IO char NumIter;
};

struct ReferenceTempParam {

	TM_OneWire_t OW; 		/* Onewire structure */
	uint8_t DS_ROM[8]; 	/* Array for DS18B20 ROM number */
	float RefTemp; 				/* Temperature variable */
	char ConfigReady;
	
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
struct ReferenceTempParam DS18B20;

volatile int FrameBuffer[3072];
volatile int PixelBuffer[2];

/*********************************************/

// FUNCTIONS HEADERS
/******* HIGH LEVEL FUNCTIONS *************/
void InitPlatform(void);
void TestOnChipDAC_Platform(void);
void ObtainCharactCurves(volatile int*);
void ObtainAndSendFrame_Chem(volatile int*);
void ObtainAndSendFrame_Temp(volatile int*);
void ObtainAndSendPixel_Temp(volatile int*);
void Calib_Array_Chem_STM(volatile int*);
void Calib_Array_Temp_STM(volatile int*);
void Calib_Pixel_Temp_STM(volatile int*);
void TempControl(float, volatile int*);
void LAMPControl(float, volatile int*);
void PCRControl(volatile int*, int);
void TempCharact(volatile int*);
void ObtainAndSendRefTemp(void);
void TempNoise(volatile int*);
/******* DRIVERS **************************/
void WaitSPICommand(void);
uint16_t voltage_to_dac(float voltage, float max, float min);
uint16_t dac_to_binary(uint16_t dac_value);
float freq_to_temp(volatile int*);
void setup_DAC(char DAC_Select);
void setup_Chip(char Enable, char Row, char Column, int DAC_Value, char DAC_Source, char DAC_Debug);
void Start_Timers(void);
void Stop_Timers(void);
volatile int* ObtainFrame(volatile int*, volatile int*);
volatile int* ObtainPixel(volatile int*, int, int, volatile int*);
void SendFrame_RPi(volatile int*);
void SendPixel_RPi(volatile int*);
void SendFrameAndCalibration_RPi(volatile int*);
void CalculateFrameDutyCycle(volatile int*);
void CalculatePixelDutyCycle(volatile int*);
void Send_EndOfAction_Frame(volatile int*);
void Send_EndOfAction_Pixel(volatile int*);
void Send_EndOfAction_FrameCalib(volatile int*);
void InitReferenceTemp(void);
void ReadReferenceTemp(void);
void SendReferenceTemp(void);
void EndReferenceTemp(void);
int CalibrationController(float);
void Delay_2ms(void);

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
	instantDNA.DAC_Peltier_Voltage = DAC_PELTIER_DEFAULT;
	for (i = 0; i < 1024; i++) instantDNA.CalibrationBuffer_DutyCycle[i] = 1024;
	for (i = 0; i < 1024; i++) instantDNA.CalibrationBuffer_Frequency[i] = 1024;
	
}

void ObtainAndSendFrame_Chem(volatile int *FrameBuf){
	
	FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle);
	SendFrame_RPi(FrameBuf);
	
}

void ObtainAndSendFrame_Temp(volatile int *FrameBuf){

	Calib_Array_Temp_STM(FrameBuf);
	FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_Frequency);
	SendFrameAndCalibration_RPi(FrameBuf);

}

void ObtainAndSendPixel_Temp(volatile int *PixelBuf){

	Calib_Pixel_Temp_STM(PixelBuf);
	PixelBuf = ObtainPixel(PixelBuf, TEMP_ROW, TEMP_COLUMN, instantDNA.CalibrationBuffer_Frequency);
	SendPixel_RPi(PixelBuf);

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
		FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle);
		FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle); // Second frame for stabilisation
		SendFrame_RPi(FrameBuf);
		instantDNA.DAC_RefElect_Voltage += (float)0.025;
	}
	
}

void Calib_Array_Chem_STM(volatile int *FrameBuf){

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
	/* Step 1 - Set Ideal Ref								*/
	/****************************************/
	// Initialise Ref Elect to zero
	instantDNA.DAC_RefElect_Voltage = 0.0;
	setup_DAC(DAC_REFELEC);
	
	// Obtain sample
	FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle);
	CalculateFrameDutyCycle(FrameBuf);
	for(pixel=0;pixel<NUMPIXELS;pixel++){
		if (instantDNA.DutyCycleBuffer[pixel] > (float)ON_LIMIT) NumPixels_On++;
		else if (instantDNA.DutyCycleBuffer[pixel] < (float)OFF_LIMIT) NumPixels_Off++;
		else NumPixels_Osc++;
	}
	
	if (NumPixels_Off > NumPixels_On) RefStep = -0.1;
	else RefStep = 0.1;
	
	while(!Flag & instantDNA.DAC_RefElect_Voltage > (float) -4.0 & instantDNA.DAC_RefElect_Voltage < (float) 4.0){
		instantDNA.DAC_RefElect_Voltage += RefStep;
		setup_DAC(DAC_REFELEC);
		
		FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle);
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
	while (NumCalibPixels < NUMPIXELS && NumIter < CALIB_DC_MAXITER){
	
		FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_DutyCycle);
		CalculateFrameDutyCycle(FrameBuf);
		NumCalibPixels = 0;
		
		for(pixel=0;pixel<NUMPIXELS;pixel++){
			// IF Pixel is in range or CalibDac is out of range
			if ((instantDNA.DutyCycleBuffer[pixel] >= (float)CALIB_DC_MINLRANGE && 
					instantDNA.DutyCycleBuffer[pixel] <= (float)CALIB_DC_MAXLRANGE) || 
					instantDNA.CalibrationBuffer_DutyCycle[pixel] <= 0 || 
					instantDNA.CalibrationBuffer_DutyCycle[pixel] >= 2047){
				NumCalibPixels++;
			}
			
			// Controller
			instantDNA.CalibrationBuffer_DutyCycle[pixel] += CalibrationController(instantDNA.DutyCycleBuffer[pixel]);
			
			// Prevent overflow
			if (instantDNA.CalibrationBuffer_DutyCycle[pixel] > 2047) instantDNA.CalibrationBuffer_DutyCycle[pixel] = 2047;
			else if (instantDNA.CalibrationBuffer_DutyCycle[pixel] < 0) instantDNA.CalibrationBuffer_DutyCycle[pixel] = 0;
		}

		// Calculate NumCalibPixels
		NumIter++;	
		SendFrame_RPi(FrameBuf);
		
	}
	
	// SEND End Of Action
	Send_EndOfAction_Frame(FrameBuf);
	
	for(pixel = 0; pixel<1024; pixel++) instantDNA.CalibrationBuffer_Frequency[pixel] = instantDNA.CalibrationBuffer_DutyCycle[pixel];
	
}

void Calib_Array_Temp_STM(volatile int *FrameBuf){

	int NumIter = 0;
	int NumCalibPixels = 0;
	int pixel;
	
	/************************************/
	/* Set Freq Calib Values						*/
	/************************************/
	while (NumCalibPixels < NUMPIXELS && NumIter < CALIB_DC_MAXITER){
	
		FrameBuf = ObtainFrame(FrameBuf, instantDNA.CalibrationBuffer_Frequency);
		CalculateFrameDutyCycle(FrameBuf);
		NumCalibPixels = 0;
		
		for(pixel=0;pixel<NUMPIXELS;pixel++){
			// IF Pixel is in range or CalibDac is out of range
			if ((instantDNA.DutyCycleBuffer[pixel] >= (float)CALIB_FREQ_MINLRANGE && 
					instantDNA.DutyCycleBuffer[pixel] <= (float)CALIB_FREQ_MAXLRANGE) || 
					instantDNA.CalibrationBuffer_Frequency[pixel] <= 0 || 
					instantDNA.CalibrationBuffer_Frequency[pixel] >= 2047){
				NumCalibPixels++;
			}
			
			// Controller
			instantDNA.CalibrationBuffer_Frequency[pixel] += CalibrationController(instantDNA.DutyCycleBuffer[pixel]);
			
			// Prevent overflow
			if (instantDNA.CalibrationBuffer_Frequency[pixel] > 2047) instantDNA.CalibrationBuffer_Frequency[pixel] = 2047;
			else if (instantDNA.CalibrationBuffer_Frequency[pixel] < 0) instantDNA.CalibrationBuffer_Frequency[pixel] = 0;
		}

		// Calculate NumCalibPixels
		NumIter++;	

	}
}

void Calib_Pixel_Temp_STM(volatile int *FrameBuf){

	char CalibDone = 0; 
	int NumIter = 0;
	const int TempPixel = TEMP_ROW+TEMP_COLUMN*NUMROWS;
	
	/****************************************/
	/* Step 2 - Set Calib Values						*/
	/****************************************/
	while (!CalibDone && NumIter < CALIB_FREQ_MAXITER){
	
		FrameBuf = ObtainPixel(FrameBuf, TEMP_ROW, TEMP_COLUMN, instantDNA.CalibrationBuffer_Frequency);
		CalculatePixelDutyCycle(FrameBuf);
		
		if ((instantDNA.DutyCycleBuffer[0] >= (float)CALIB_FREQ_MINLRANGE && 
				instantDNA.DutyCycleBuffer[0] <= (float)CALIB_FREQ_MAXLRANGE) || 
				instantDNA.CalibrationBuffer_Frequency[TempPixel] <= 0 || 
				instantDNA.CalibrationBuffer_Frequency[TempPixel] >= 2047){
			CalibDone = 1;
		}
			
			// Controller
		instantDNA.CalibrationBuffer_Frequency[TempPixel] += CalibrationController(instantDNA.DutyCycleBuffer[0]);
		
		// Prevent overflow
		if (instantDNA.CalibrationBuffer_Frequency[TempPixel] > 2047) instantDNA.CalibrationBuffer_Frequency[TempPixel] = 2047;
		else if (instantDNA.CalibrationBuffer_Frequency[TempPixel] < 0) instantDNA.CalibrationBuffer_Frequency[TempPixel] = 0;

		// Calculate NumCalibPixels
		NumIter++;	
	}
}

void TempControl(float Temp, volatile int* PixBuf){
	
	/*static float Temp_Coil = 0.0;
	
	HAL_DAC_SetValue(&hdac, DAC_CHANNEL_1, DAC_ALIGN_12B_R, voltage_to_dac(Temp_Coil,3.3,0.0));
	Temp_Coil += (float)0.1;
	
	if (Temp_Coil >= (float)3.3) Temp_Coil = 0.0;
	Send_EndOfAction_Pixel(PixBuf);*/
	
	
	int j;
	
	for(j = 0; j<10; j++) ObtainAndSendPixel_Temp(PixBuf);
	instantDNA.DAC_Peltier_Voltage = (float)2.5;
	setup_DAC(DAC_PELTIER);
	for(j = 0; j<40; j++) ObtainAndSendPixel_Temp(PixBuf);
	instantDNA.DAC_Peltier_Voltage = (float)0.0;
	setup_DAC(DAC_PELTIER);
	Send_EndOfAction_Pixel(PixBuf);
	
}

void LAMPControl(float Temp, volatile int* FrameBuf){
	instantDNA.DAC_Peltier_Voltage = (float)2.75;
	setup_DAC(DAC_PELTIER);
	Send_EndOfAction_Frame(FrameBuf);
}

void PCRControl(volatile int* FrameBuf, int NumCycles){
	Send_EndOfAction_Frame(FrameBuf);
	/* ALOKIRA TO POPULATE */
}


void TempCharact(volatile int* FrameBuf){

	int j;
	for(j=0; j<SAMPLES_TCHARACT; j++) ObtainAndSendFrame_Temp(FrameBuf);
	
	Send_EndOfAction_FrameCalib(FrameBuf);
	
}

void ObtainAndSendRefTemp(){
	
	int j;
	
	for(j=0; j<SAMPLES_REFTEMP; j++){
		ReadReferenceTemp();
		SendReferenceTemp();
	}
	Delay_2ms();
	EndReferenceTemp();
}

void TempNoise(volatile int* PixelBuf){
	
	int j;
	for(j=0; j<SAMPLES_TNOISE; j++) ObtainAndSendPixel_Temp(PixelBuf);
	
	Send_EndOfAction_Pixel(PixelBuf);
	
}

/************************ DRIVERS **************************/


void Start_Timers(void){

	/* Start the timer */
	if (HAL_TIM_IC_Start(&htim2, TIM_CHANNEL_1) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_IC_Start(&htim2, TIM_CHANNEL_2) != HAL_OK)
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
	if (HAL_TIM_IC_Stop(&htim2, TIM_CHANNEL_1) != HAL_OK)
	{
		Error_Handler();
	}
	if (HAL_TIM_IC_Stop(&htim2, TIM_CHANNEL_2) != HAL_OK)
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
			data_to_send = dac_to_binary(voltage_to_dac(0.275, 3.24, 0));
			//data_to_send = dac_to_binary(voltage_to_dac(instantDNA.DAC_VBias_Voltage, 3.24, 0));
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
		
		case DAC_PELTIER:
			data_to_send = dac_to_binary(voltage_to_dac(instantDNA.DAC_Peltier_Voltage, 5.0, 0));
			HAL_GPIO_WritePin(GPIOA, PELTIER_CS_Pin, GPIO_PIN_RESET);
			HAL_SPI_Transmit(&hspi2, (uint8_t*)&data_to_send, 2, 256);
			HAL_GPIO_WritePin(GPIOA, PELTIER_CS_Pin, GPIO_PIN_SET);
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

volatile int* ObtainFrame(volatile int* FrameBuf, volatile int* CalibrationBuffer){

	int row;
	int column;
	
	// SETUP External DACs
	// Loop around pixels and obtain measurement
	Start_Timers(); // Start Timers
	
	for (column = 0; column < instantDNA.NumColumns; column++){
		for (row = 0; row < instantDNA.NumRows; row++){
			
				// SETUP CHIP
				setup_Chip(ISFET_ON,row, column, CalibrationBuffer[row+column*NUMROWS],DAC_INTERNAL,DAC_ACTIVE); 
			
				// Check previous state
				TimerCh2.Prev_TicksHigh_Sample = HAL_TIM_ReadCapturedValue(&htim2, TIM_CHANNEL_1);
				TimerCh2.Prev_TicksPeriod_Sample = HAL_TIM_ReadCapturedValue(&htim2, TIM_CHANNEL_2);
				
				TimerCh2.ActiveMeas = 1;
				while (TimerCh2.ActiveMeas){} // Wait until end of pix measurement
					
				// Store variables
				FrameBuf[(row+column*NUMROWS)*2] = TimerCh2.TicksHigh_Sample; 
				FrameBuf[(row+column*NUMROWS)*2+1] = TimerCh2.TicksPeriod_Sample;
			
				// Restart variables
				TimerCh2.TicksHigh_Sample = 0;
				TimerCh2.TicksPeriod_Sample = 0;
				TimerCh2.NumIter = 0;
				TimerCh2.FirstIgnored = 0;
					
		}
	}
	
	Stop_Timers();
	return FrameBuf;
	
}

volatile int* ObtainPixel(volatile int* FrameBuf, int row, int column, volatile int* CalibrationBuffer){
	
	Start_Timers(); // Start Timers
	
	setup_Chip(ISFET_ON,row, column, CalibrationBuffer[row+column*NUMROWS],DAC_INTERNAL,DAC_ACTIVE); 
	TimerCh2.ActiveMeas = 1;
	while (TimerCh2.ActiveMeas){} // Wait until end of pix measurement
	
	FrameBuf[0] = TimerCh2.TicksHigh_Sample; 
	FrameBuf[1] = TimerCh2.TicksPeriod_Sample;

	// Reset Values	
	TimerCh2.Prev_TicksHigh_Sample = TimerCh2.TicksHigh_Sample;
	TimerCh2.Prev_TicksPeriod_Sample = TimerCh2.TicksPeriod_Sample;
	TimerCh2.TicksHigh_Sample = 0;
	TimerCh2.TicksPeriod_Sample = 0;
	TimerCh2.NumIter = 0;
	TimerCh2.FirstIgnored = 0;

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

void SendPixel_RPi(volatile int* PixelBuf){

	// ASSERT RPi IRQ WHEN FRAME DONE
	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)PixelBuf, (uint8_t *)PixelBuf, 8);
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_SET);
	while (SPIMessage_Available == 0x00){}
	SPIMessage_Available = 0;
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_RESET);

}

void SendFrameAndCalibration_RPi(volatile int* FrameBuf){

	int pixel;
	
	for(pixel = 0; pixel < NUMPIXELS; pixel++)  FrameBuf[pixel+2048]= instantDNA.CalibrationBuffer_Frequency[pixel];
	
	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)FrameBuf, (uint8_t *)FrameBuf, 12288);
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

void CalculatePixelDutyCycle(volatile int* FrameBuf){

	instantDNA.DutyCycleBuffer[0] = (float)FrameBuf[0] / (float)FrameBuf[1];
	
}

int CalibrationController(float DutyCycle){

	int DeltaDAC;
	
	// K Controller - Not working yet
	DeltaDAC = (int)((float)CONTROLLER_KP * ((float)0.5 - DutyCycle));
	return DeltaDAC;
	
}

void Send_EndOfAction_Frame(volatile int* FrameBuf){

	FrameBuf[0] = 0xAAAAAAAA;
	FrameBuf[1] = 0xAAAAAAAA;
	Delay_2ms();
	SendFrame_RPi(FrameBuf);
	
}

void Send_EndOfAction_Pixel(volatile int* PixelBuf){

	PixelBuf[0] = 0xAAAAAAAA;
	PixelBuf[1] = 0xAAAAAAAA;
	Delay_2ms();
	SendPixel_RPi(PixelBuf);
	
}

void Send_EndOfAction_FrameCalib(volatile int* FrameBuf){

	FrameBuf[0] = 0xAAAAAAAA;
	FrameBuf[1] = 0xAAAAAAAA;
	Delay_2ms();
	SendFrameAndCalibration_RPi(FrameBuf);
	
}

void Delay_2ms(){

	Start_Timers(); // Start Timers

	TimerCh2.ActiveMeas = 1;
	while (TimerCh2.ActiveMeas){} // Wait until end of pix measurement - Aprox 1ms
	
	// Restart variables
	TimerCh2.Prev_TicksHigh_Sample = TimerCh2.TicksHigh_Sample;
	TimerCh2.Prev_TicksPeriod_Sample = TimerCh2.TicksPeriod_Sample;
	TimerCh2.TicksHigh_Sample = 0;
	TimerCh2.TicksPeriod_Sample = 0;
	TimerCh2.NumIter = 0;
	TimerCh2.FirstIgnored = 0;

	Stop_Timers();
	
}

void InitReferenceTemp(){
	
	TM_OneWire_Init(&DS18B20.OW, GPIOC, GPIO_PIN_1);
	if (TM_OneWire_First(&DS18B20.OW)) {	
		/* Read ROM number */
		TM_OneWire_GetFullROM(&DS18B20.OW, DS18B20.DS_ROM);
		DS18B20.ConfigReady = 1;
	}
	else DS18B20.ConfigReady = 0;
	
}

void ReadReferenceTemp(){

	if (!DS18B20.ConfigReady) InitReferenceTemp();
	if (!DS18B20.ConfigReady) return; // NOTHING TO ANSWER - DEVICE NOT THERE
	
	TM_DS18B20_Start(&DS18B20.OW, DS18B20.DS_ROM); 									/* START DEVICE */
	while (!TM_DS18B20_AllDone(&DS18B20.OW)){}											/* CHECK ALL DEVICES ARE DONE */
	TM_DS18B20_Read(&DS18B20.OW, DS18B20.DS_ROM, &DS18B20.RefTemp);	/* READ DEVICE */
	
	// SEND THROUGH SPI
		
}

void SendReferenceTemp(){

	uint8_t *byte = (uint8_t *)(&DS18B20.RefTemp);
	
	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)byte, (uint8_t *)byte, 4);
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_SET);
	while (SPIMessage_Available == 0x00){}
	SPIMessage_Available = 0;
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_RESET);
	
}

void EndReferenceTemp(){

	float EndTemp = -50.0;
	uint8_t *byte = (uint8_t *)(&EndTemp);
	
	HAL_SPI_TransmitReceive_IT(&hspi1, (uint8_t *)byte, (uint8_t *)byte, 4);
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_SET);
	while (SPIMessage_Available == 0x00){}
	SPIMessage_Available = 0;
	HAL_GPIO_WritePin(IRQ_Frame_GPIO_Port, IRQ_Frame_Pin, GPIO_PIN_RESET);
	
}

#endif /* __INSTANTDNA_H */
