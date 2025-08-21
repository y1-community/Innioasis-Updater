// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#include "sej.h"

uint32_t g_UnqKey_IV[8] = {0x6786CFBD, 0x44B7F1E0, 0x1544B07B, 0x53A28EB3, 0xD7AB8AA2, 0xB9E30E7E, 0x172156E0, 0x3064C973};

volatile uint32_t hacc_base=0x1000a000;

int32_t toSigned32(uint32_t n){
    n = n & 0xffffffff;
    return n | (-(n & 0x80000000));
}

static uint32_t get_world_clock_value(){
    return INREG32(0x10017008);
}

int32_t check_timeout(const uint32_t clockvalue, int32_t timeout){
    uint32_t tmp = -clockvalue;
    const uint32_t curtime = get_world_clock_value();
    if (curtime < clockvalue){
        tmp = ~clockvalue;
    }
    return tmp + get_world_clock_value() >= ((uint32_t)timeout)*1000*13;
}

void HACC_V3_Terminate(void) {
    OUTREG32(HACC_ACON2,HACC_AES_CLR);
    for (int32_t i = 0; i < 8; i++){
        OUTREG32(HACC_AKEY0 + (4 * i),0);
    }
}

int32_t sej_set_otp(uint32_t* otp){
    for (int32_t i = 0; i < 8; i++) {
        OUTREG32(HACC_SW_OTP0 + (4 * i),otp[i]);
    }
    return 0;
}

int32_t HACC_V3_Run(volatile uint32_t *p_src, uint32_t src_len, volatile uint32_t *p_dst, bool legacy, uint8_t attr, uint8_t sej_param){
    if (src_len>0x40){
        return 0x9999;
    }
    if (legacy){
        if ((attr&8)!=0&&(sej_param&2)!=0) {
            SETREG32(HACC_ACONK, HACC_AES_R2K);
        } else {
            OUTREG32(HACC_ACONK, INREG32(HACC_ACONK)&0xFFFFFEFF);
        }
    }
    for (int32_t i = 0; i < (int)(src_len / 4); i += 4) {
        for (int32_t x = 0; x < 4; x++) {
            OUTREG32(HACC_ASRC0 + (4 * x), p_src[x+i]);
        }
        OUTREG32(HACC_ACON2, HACC_AES_START);
        const uint32_t clockvalue = get_world_clock_value();
        while ((INREG32(HACC_ACON2) & HACC_AES_RDY) == 0) {
            if (check_timeout(clockvalue, 200)) {
                return 0x4006;
            }
        }
        for (int32_t x = 0; x < 4; x++) {
            p_dst[x+i]= INREG32(HACC_AOUT0 + ((4*x)));
        }
    }
    if (legacy){
        if ((attr&8)!=0 && (sej_param&2)==0){
            for (int32_t x = 0; x < 4; x++) {
                OUTREG32(HACC_AKEY0 + (4 * x),INREG32(HACC_AOUT0 + (4 * x))^INREG32(HACC_AKEY0 + (4 * x)));
            }
        }
    }
    return 0;
}
