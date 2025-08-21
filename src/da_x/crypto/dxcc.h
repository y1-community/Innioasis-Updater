// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#ifndef DXCC_H
#define DXCC_H
#include <stdint.h>
#include <stdbool.h>
#include "../common/libc.h"
#define HW_DESC_SIZE_WORDS 6
typedef struct HwDesc {
	uint32_t word[HW_DESC_SIZE_WORDS];
} HwDesc_s;

#define DX_DSCRPTR_QUEUE0_WORD0_REG_OFFSET 	0xE80
#define DX_DSCRPTR_QUEUE0_WORD1_REG_OFFSET 	0xE84
#define DX_DSCRPTR_QUEUE0_WORD2_REG_OFFSET 	0xE88
#define DX_DSCRPTR_QUEUE0_WORD3_REG_OFFSET 	0xE8C
#define DX_DSCRPTR_QUEUE0_WORD4_REG_OFFSET 	0xE90
#define DX_DSCRPTR_QUEUE0_WORD5_REG_OFFSET 	0xE94
#define DX_DSCRPTR_QUEUE0_CONTENT_REG_OFFSET 	0xE9C
#define DX_HOST_IRR_REG_OFFSET 	0xA00
#define DX_HOST_ICR_REG_OFFSET 	0xA08
#define DX_HOST_SEP_HOST_GPR4_REG_OFFSET 	0xAA0

int dxcc(volatile uint32_t* base, int hwmode, uint8_t* key, int keylen, uint8_t* seed, int seedlen, uint8_t* outbuf, int derivelen);
#endif