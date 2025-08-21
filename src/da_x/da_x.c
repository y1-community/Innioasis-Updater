// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#include <stdint.h>
#include "common/defs.h"
#include "common/libc.h"
#include "crypto/sej.h"
#include "common/flash_handler.h"

static uint32_t storage=STORAGE_EMMC;

typedef struct
{
    int (*read)(uint8_t* buffer, uint32_t* length);
    int (*write)(uint8_t* buffer, uint32_t length);
    int (*log_to_pc)(const uint8_t* buffer, uint32_t length);
    int (*log_to_uart)(const uint8_t* buffer, uint32_t length);
} com_channel_struct;

typedef int (*HHANDLE)(com_channel_struct*);
extern void apmcu_dcache_clean_invalidate();
extern void apmcu_dcache_invalidate();
extern int cache_init(int param);
extern int cache_close(int param);

int (*register_major_command)(uint32_t /*ctrl_code*/, HHANDLE /*handle*/)=(const void*)0x11111111;
uint32_t efuse_addr=0x88888888;

/* -------------------------------- Commands --------------------------------------- */

int cmd_readmem(com_channel_struct *channel){
    volatile uint64_t addr=0;
    uint8_t buffer[0x20000]={0};
    uint32_t length=0;
    uint32_t cmdlen=8;
    channel->read((uint8_t*)&addr,&cmdlen);
    cmdlen=4;
    channel->read((uint8_t*)&length,&cmdlen);
    if (length>0x20000) length=0x20000;
    memcpy(buffer,(volatile uint64_t*)addr,length);
    return channel->write((uint8_t *)buffer,length);
}

int cmd_readregister(com_channel_struct *channel){
    volatile uint32_t addr=0;
    volatile uint32_t dword=0;
    uint32_t cmdlen=4;
    channel->read((uint8_t*)&addr,&cmdlen);
    cmdlen=4;
    dword=WRAP_RD32(addr);
    //dword=*(volatile uint32_t*)addr;
    return channel->write((uint8_t *)&dword,cmdlen);
}

int cmd_writemem(com_channel_struct *channel){
    volatile uint64_t addr=0;
    uint32_t length=0;
    uint32_t cmdlen=8;
    channel->read((uint8_t*)&addr,&cmdlen);
    cmdlen=4;
    channel->read((uint8_t*)&length,&cmdlen);
    return channel->read((uint8_t *)addr,&length);
}

int cmd_writeregister(com_channel_struct *channel){
    volatile uint32_t addr=0;
    volatile uint32_t dword=0;
    uint32_t cmdlen=4;
    channel->read((uint8_t*)&addr,&cmdlen);
    cmdlen=4;
    channel->read((uint8_t*)&dword,&cmdlen);
    WRAP_WR32(addr,dword);
    //*(volatile uint32_t*)addr=dword;
    return 0;
}

int cmd_ack(com_channel_struct *channel){
    uint32_t ack=0xA1A2A3A4;
    return channel->write((uint8_t *)&ack,4);
}

int cmd_rpmb_read(com_channel_struct *channel)
{
    uint32_t size = 4;
    uint32_t address = 0;
    uint32_t sectors = 0;
    channel->read((uint8_t*)&address, &size);
    size=4;
    channel->read((uint8_t*)&sectors, &size);
    uint8_t data[0x100]={0};
    int res = -1;
    for (uint32_t cursector=address;cursector<address+sectors;cursector++){
        if (storage==STORAGE_UFS) {
            res = ufs_read_frame(cursector,data);
        }
        else if (storage==STORAGE_EMMC) {
            res = mmc_read_frame(cursector,data);
        }
        if (res) {
            channel->write((uint8_t *)&res, 2);
            break;
        }
        else {
            channel->write((uint8_t *)data, 0x100);
        }
    }
    return res;
}

int cmd_rpmb_write(com_channel_struct *channel, const char* /*xml*/)
{
    uint32_t size = 4;
    uint32_t address = 0;
    uint32_t sectors = 0;
    uint8_t data[0x100]={0};
    channel->read((uint8_t*)&address, &size);
    size=4;
    channel->read((uint8_t*)&sectors, &size);
    int res = -1;
    size = 0x100;
    for (uint32_t cursector=address;cursector<address+sectors;cursector++) {
        channel->read(data, &size);
        if (storage == STORAGE_UFS) {
            res = ufs_write_frame(cursector, data);
        } else if (storage == STORAGE_EMMC) {
            res = mmc_write_frame(cursector, data);
        }
        channel->write((uint8_t*)&res, 2);
        if (res) {
            break;
        }
    }
    return 0;
}

int cmd_rpmb_init(com_channel_struct *channel)
{
  int res = -1;
  if (storage==STORAGE_UFS){
      res=ufs_init();
  } else if (storage==STORAGE_EMMC) {
      res=mmc_init();
  }
  channel->write((uint8_t*)&res, 2);
  if (!res) {
      channel->write((uint8_t*)get_current_rpmb_key(),0x20);
  }
  return 0;
}

int cmd_rpmb_set_key(com_channel_struct *channel)
{
  uint32_t size = 0x20;
  uint8_t rpmbkey[0x20];
  channel->read((uint8_t*)rpmbkey, &size);
  set_current_rpmb_key(rpmbkey);
  channel->write(get_current_rpmb_key(),0x20);
  return 0;
}

int cmd_set_storage(com_channel_struct *channel)
{
    uint32_t size = 0x4;
    channel->read((uint8_t*)&storage, &size);
    return 0;
}

__attribute__ ((section(".text.main"))) int main() {
    cache_init(3);
    register_major_command(0xF0000,(void*)cmd_ack);
    register_major_command(0xF0001,(void*)cmd_readmem);
    register_major_command(0xF0002,(void*)cmd_readregister);
    register_major_command(0xF0003,(void*)cmd_writemem);
    register_major_command(0xF0004,(void*)cmd_writeregister);
    register_major_command(0xF0005,(void*)cmd_set_storage);
    register_major_command(0xF0006,(void*)cmd_rpmb_set_key);
    register_major_command(0xF0008,(void*)cmd_rpmb_init);
    register_major_command(0xF0009,(void*)cmd_rpmb_read);
    register_major_command(0xF000A,(void*)cmd_rpmb_write);
    cache_close(1);
    return 0;
}