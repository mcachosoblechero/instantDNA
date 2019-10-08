/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2019 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define Not_PWM_Pin GPIO_PIN_0
#define Not_PWM_GPIO_Port GPIOA
#define PWM_Pin GPIO_PIN_1
#define PWM_GPIO_Port GPIOA
#define IRQ_Frame_Pin GPIO_PIN_3
#define IRQ_Frame_GPIO_Port GPIOA
#define DAC_COIL_Pin GPIO_PIN_4
#define DAC_COIL_GPIO_Port GPIOA
#define V_REF_CS_Pin GPIO_PIN_6
#define V_REF_CS_GPIO_Port GPIOC
#define V_BIAS_CS_Pin GPIO_PIN_7
#define V_BIAS_CS_GPIO_Port GPIOC
#define IOTA_CS_Pin GPIO_PIN_8
#define IOTA_CS_GPIO_Port GPIOC
#define CHIP_CS_Pin GPIO_PIN_10
#define CHIP_CS_GPIO_Port GPIOA
#define PELTIER_CS_Pin GPIO_PIN_11
#define PELTIER_CS_GPIO_Port GPIOA
#define REF_E_CS_Pin GPIO_PIN_12
#define REF_E_CS_GPIO_Port GPIOA
#define N5V_EN_Pin GPIO_PIN_8
#define N5V_EN_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
