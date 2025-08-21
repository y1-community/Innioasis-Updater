// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.
#include "flash_handler.h"
#include "libc.h"
#include "../crypto/hmac-sha256.h"
#include "../crypto/V5/rpmb.h"

int (*mmc_get_card)(int /*id*/)=(const void*)0x22222222;
int (*mmc_set_part_config)(struct mmc_card */*card*/, uint8_t /*cfg*/)=(const void*)0x33333333;
int (*mmc_rpmb_send_command)(struct mmc_card */*card*/, uint8_t */*data_frame*/, uint32_t /*blks*/, int /*type*/, uint8_t /*req_type*/)=(const void*)0x44444444;
int (*ufshcd_queuecommand)(struct ufs_hba */*hba*/, struct ufs_aio_scsi_cmd */*cmd*/)=(const void*)0x55555555;
bool (*ufshcd_get_free_tag)(struct ufs_hba */*hba*/, int */*tag_out*/)=(const void*)0x66666666;
uint32_t g_ufs_hba=0x77777777;
static uint8_t rpmb_key[32]={0x64, 0x76, 0xEE, 0xF0, 0xF1, 0x6B, 0x30, 0x47, 0xE9, 0x79, 0x31, 0x58, 0xF6, 0x42, 0xDA, 0x46, 0xF7, 0x3B, 0x53, 0xFD, 0xC5, 0xF8, 0x84, 0xCE, 0x03, 0x73, 0x15, 0xBC, 0x54, 0x47, 0xD4, 0x6A};

uint8_t* get_current_rpmb_key(){
    return rpmb_key;
}

void set_current_rpmb_key(uint8_t* rpmbkey){
    memcpy(rpmb_key,rpmbkey,0x20);
}

void mcpy(uint8_t* src, uint8_t* dst, int len)
{
    uint8_t* i;
    uint8_t* m;
    uint8_t* t;

    for (i=src;len--;i++)
    {
        m=dst++;
        t=i;
        *t=*m;
    }
}

int ufs_init() {
    struct rpmb_data_frame frame;
    struct ufs_aio_scsi_cmd cmd;
    struct ufs_hba* hba = (struct ufs_hba*)g_ufs_hba;
    int tag;
    ufshcd_get_free_tag(hba, &tag);
    cmd.data_buf = &frame;
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.req_resp = __builtin_bswap16(RPMB_GET_WRITE_COUNTER);
    cmd_scsi_security_protocol_out(&cmd, tag);
    int res = ufshcd_queuecommand(hba, &cmd);
    if (!res) {
        memset(&frame, 0, sizeof(struct rpmb_data_frame));
        cmd_scsi_security_protocol_in(&cmd, tag);
        res = ufshcd_queuecommand(hba, &cmd);
        if (!res) {
            res=__builtin_bswap16(frame.result);
            if (!res){
                res = rpmb_key_generate(frame, rpmb_key);
            }
        }
    }
    ufshcd_put_tag(hba, tag);
    return res;
}


int ufs_read_frame(uint32_t address, uint8_t* data){
    struct ufs_hba* hba = (struct ufs_hba*)g_ufs_hba;
    struct rpmb_data_frame frame;
    struct ufs_aio_scsi_cmd cmd;
    int tag;
    int res;
    if (!ufshcd_get_free_tag(hba, &tag))
    {
        return -1;
    }
    cmd.data_buf = &frame;
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.addr = __builtin_bswap16(address);
    frame.blk_cnt = __builtin_bswap16(1);
    frame.req_resp = __builtin_bswap16(RPMB_READ_DATA);
    cmd_scsi_security_protocol_out(&cmd, tag);
    res = ufshcd_queuecommand(hba, &cmd);
    if (!res) {
        memset(&frame, 0, sizeof(struct rpmb_data_frame));
        cmd_scsi_security_protocol_in(&cmd, tag);
        res = ufshcd_queuecommand(hba, &cmd);
        if (!res) {
            res = __builtin_bswap16(frame.result);
            if (!res) {
                memcpy(data,frame.data,0x100);
            }
        }
    }
    ufshcd_put_tag(hba, tag);
    return res;
}

int ufs_write_frame(uint32_t address, uint8_t* data)
{
    struct ufs_hba* hba = (struct ufs_hba*)g_ufs_hba;
    struct rpmb_data_frame frame;
    struct ufs_aio_scsi_cmd cmd;
    int tag;
    int res;
    if (!ufshcd_get_free_tag(hba, &tag)){
        return -1;
    }
    // 1. Step: Write counter read request
    cmd.data_buf = &frame;
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.req_resp = __builtin_bswap16(RPMB_GET_WRITE_COUNTER);
    cmd_scsi_security_protocol_out(&cmd, tag);
    res=ufshcd_queuecommand(hba, &cmd);
    if (!res) {
        // 1. Step: Read counter to frame.wc_cnt
        memset(&frame, 0, sizeof(struct rpmb_data_frame));
        cmd_scsi_security_protocol_in(&cmd, tag);
        res = ufshcd_queuecommand(hba, &cmd);
        if (!res) {
            // 2. Step: Write data
            frame.addr = __builtin_bswap16(address);
            frame.blk_cnt = __builtin_bswap16(1);
            frame.result = 0;
            //frame.wr_cnt = __builtin_bswap32(wr_cnt);
            frame.req_resp = __builtin_bswap16(RPMB_WRITE_DATA);
            memcpy(frame.data,data,0x100);
            hmac_sha256(frame.key_MAC, frame.data, 0x200 - RPMB_DATA_BEG, rpmb_key, 0x20);
            cmd_scsi_security_protocol_out(&cmd, tag);
            res = ufshcd_queuecommand(hba, &cmd);
            if (!res) {
                // Step 3: Send Request for Result Read
                memset(&frame, 0, sizeof(struct rpmb_data_frame));
                frame.req_resp = __builtin_bswap16(RPMB_RESULT_READ);
                cmd_scsi_security_protocol_out(&cmd, tag);
                res = ufshcd_queuecommand(hba, &cmd);
                if (!res) {
                    // Step 3: Response frame check
                    memset(&frame, 0, sizeof(struct rpmb_data_frame));
                    cmd_scsi_security_protocol_in(&cmd, tag);
                    res = ufshcd_queuecommand(hba, &cmd);
                    if (!res) {
                        res = __builtin_bswap16(frame.result);
                    }
                }
            }
        }
    }
    ufshcd_put_tag(hba, tag);
    return res;
}

int ufs_prog_rpmbkey(uint8_t* rpmbkey){
    struct ufs_hba* hba = (struct ufs_hba*)g_ufs_hba;
    struct rpmb_data_frame frame;
    struct ufs_aio_scsi_cmd cmd;
    cmd.data_buf = &frame;
    int tag;
    int res=0;
    if (!ufshcd_get_free_tag(hba, &tag))
    {
        return -1;
    }
    cmd_scsi_security_protocol_out(&cmd, tag);
    // ufshcd_authen_key_prog_req_prepare
    memset(&frame,0,sizeof(struct rpmb_data_frame));
    memcpy(frame.key_MAC,rpmbkey,0x20);
    frame.req_resp = __builtin_bswap16(RPMB_PROGRAM_KEY);
    //
    res = ufshcd_queuecommand(hba, &cmd);
    if (!res) {
        cmd_scsi_security_protocol_out(&cmd, tag);
        //ufshcd_authen_result_read_req_prepare
        memset(&frame,0,sizeof(struct rpmb_data_frame));
        frame.req_resp = __builtin_bswap16(RPMB_RESULT_READ);
        //
        res = ufshcd_queuecommand(hba, &cmd);
        if (!res) {
            //memset(&frame, 0, sizeof(struct rpmb_data_frame));
            cmd_scsi_security_protocol_in(&cmd, tag);
            res = ufshcd_queuecommand(hba, &cmd);
            if (!res) {
                // ufshcd_authen_result_read_rsp_check
                res = __builtin_bswap16(frame.result);
            }
        }
    }
    ufshcd_put_tag(hba,tag);
    return res;
}

int mmc_init(){
    struct rpmb_data_frame frame;
    struct mmc_card* card = (struct mmc_card*)mmc_get_card(0);
    mmc_set_part_config(card, (card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8) | 3);
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.req_resp = __builtin_bswap16(RPMB_GET_WRITE_COUNTER);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_GET_WRITE_COUNTER, RPMB_REQ);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_GET_WRITE_COUNTER, RPMB_RESP);
    int res=(int)__builtin_bswap16(frame.result);
    if (!res) {
        res = rpmb_key_generate(frame, rpmb_key);
    }
    mmc_set_part_config(card, card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8);
    return res;
}

int mmc_prog_rpmbkey(uint8_t* rpmbkey){
    struct rpmb_data_frame frame;
    struct mmc_card* card = (struct mmc_card*)mmc_get_card(0);
    mmc_set_part_config(card, (card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8) | 3);
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.blk_cnt = __builtin_bswap16(1);
    frame.req_resp = __builtin_bswap16(RPMB_PROGRAM_KEY);
    memcpy(frame.key_MAC,rpmbkey,0x20);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_PROGRAM_KEY, RPMB_REQ);
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.req_resp = __builtin_bswap16(RPMB_RESULT_READ);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_RESULT_READ, RPMB_REQ);
    frame.req_resp = __builtin_bswap16(RPMB_PROGRAM_KEY);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_RESULT_READ, RPMB_RESP);
    int res = __builtin_bswap16(frame.result);
    mmc_set_part_config(card, card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8);
    return res;
}

int mmc_read_frame(uint32_t address, uint8_t* data)
{
    struct rpmb_data_frame frame;
    struct mmc_card* card = (struct mmc_card*)mmc_get_card(0);
    mmc_set_part_config(card, (card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8) | 3);
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.addr = __builtin_bswap16((uint16_t)address&0xFFFF);
    frame.req_resp = __builtin_bswap16(RPMB_READ_DATA);

    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_READ_DATA, RPMB_REQ);
    mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_READ_DATA, RPMB_RESP);
    int res = __builtin_bswap16(frame.result);
    if (!res){
        memcpy(data,frame.data,0x100);
    }
    mmc_set_part_config(card, card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8);
    return res;
}

int mmc_write_frame(uint32_t address, uint8_t* data)
{
    struct rpmb_data_frame frame;
    struct mmc_card* card = (struct mmc_card*)mmc_get_card(0);
    mmc_set_part_config(card, (card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8) | 3);
    memset(&frame, 0, sizeof(struct rpmb_data_frame));
    frame.req_resp = __builtin_bswap16(RPMB_GET_WRITE_COUNTER);
    int res=mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_GET_WRITE_COUNTER, RPMB_REQ);
    if (!res){
        res=mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_GET_WRITE_COUNTER, RPMB_RESP);
        if (!res){
            frame.addr = __builtin_bswap16(address);
            frame.blk_cnt = __builtin_bswap16(1);
            frame.result = 0;
            frame.req_resp = __builtin_bswap16(RPMB_WRITE_DATA);
            memcpy(frame.data,data,0x100);
            hmac_sha256(frame.key_MAC, frame.data, 0x200 - RPMB_DATA_BEG, (const uint8_t*)rpmb_key, 0x20);
            res = mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_WRITE_DATA, RPMB_REQ);
            if (!res) {
                memset(&frame, 0, sizeof(struct rpmb_data_frame));
                frame.req_resp = __builtin_bswap16(RPMB_RESULT_READ);
                res=mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_RESULT_READ, RPMB_REQ);
                if (!res) {
                    res = mmc_rpmb_send_command((struct mmc_card *)card->host, (uint8_t*)&frame, 1, RPMB_RESULT_READ, RPMB_RESP);
                    if (!res) {
                        res = __builtin_bswap16(frame.result);
                    }
                }
            }
        }
    }
    mmc_set_part_config(card, card->raw_ext_csd[EXT_CSD_PART_CFG] & 0xF8);
    return res;
}
