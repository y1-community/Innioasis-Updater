// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#ifndef DA_X_COMMAND_HANDLER_H
#define DA_X_COMMAND_HANDLER_H
#include <stdint.h>
#include <stdbool.h>
enum storage_type {
    STORAGE_EMMC=0,
    STORAGE_UFS=1
};

void mcpy(uint8_t* src, uint8_t* dst, int len);
int ufs_init();
int ufs_read_frame(uint32_t address, uint8_t* data);
int ufs_write_frame(uint32_t address, uint8_t* data);
int ufs_prog_rpmbkey(uint8_t* rpmbkey);
int mmc_prog_rpmbkey(uint8_t* rpmbkey);
int mmc_init();
int mmc_read_frame(uint32_t address, uint8_t* data);
int mmc_write_frame(uint32_t address, uint8_t* data);
uint8_t* get_current_rpmb_key();
void set_current_rpmb_key(uint8_t* rpmbkey);
#endif //DA_X_COMMAND_HANDLER_H
