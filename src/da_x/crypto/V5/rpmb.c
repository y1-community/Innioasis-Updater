// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#include "rpmb.h"
#include "../../common/defs.h"
#include "../dxcc.h"
#include "../hmac-sha256.h"

void ufshcd_put_tag(struct ufs_hba *hba, int tag)
{
    /* clear_bit(tag, &hba->lrb_in_use); */
    hba->lrb_in_use &= ~(1 << tag);
}

void cmd_scsi_security_protocol_out(struct ufs_aio_scsi_cmd *cmd, int tag)
{
    uint32_t blk_cnt = 1;
    uint8_t protocol=UFS_SECURITY_PROTOCOL;
    uint32_t protocol_specific=RPMB_PROTOCOL_ID;
    memset(cmd->cmd_data, 0, MAX_CDB_SIZE);
    cmd->lun = WLUN_RPMB;
    cmd->tag = tag;
    cmd->cmd_len = 0xC;
    cmd->dir = DMA_TO_DEVICE;
    cmd->exp_len = blk_cnt << 9;
    cmd->attr = 0;
    cmd->cmd_data[0] = SECURITY_PROTOCOL_OUT; //0xB5 .. 0xA2 ?
    cmd->cmd_data[1] = protocol; //0xEC
    cmd->cmd_data[2] = (protocol_specific >> 8) & 0xFF; //security protocol specific
    cmd->cmd_data[3] = protocol_specific & 0xFF; //security protocol specific
    cmd->cmd_data[4] = 0x0;  // INC_512 = 0
    cmd->cmd_data[5] = 0;             // reserved
    cmd->cmd_data[6] = ((blk_cnt  << 9) >> 24) & 0xFF; //Reserved
    cmd->cmd_data[7] = ((blk_cnt  << 9) >> 16) & 0xFF; //Reserved
    cmd->cmd_data[8] = ((blk_cnt  << 9) >> 8) & 0xFF; //Reserved
    cmd->cmd_data[9] = 0x0; //(blk_cnt  << 9) & 0xFF; actually = 0 //Reserved
    cmd->cmd_data[0xA] =  0x0; //Reserved
    cmd->cmd_data[0xB] = (uint8_t)0;  // control
}

void cmd_scsi_security_protocol_in(struct ufs_aio_scsi_cmd *cmd, int tag)
{
    uint32_t blk_cnt = 1;
    uint8_t protocol=UFS_SECURITY_PROTOCOL;
    uint32_t protocol_specific=RPMB_PROTOCOL_ID;
    memset(cmd->cmd_data, 0, MAX_CDB_SIZE);
    cmd->exp_len = blk_cnt * 512;
    cmd->tag = tag;
    cmd->dir = DMA_FROM_DEVICE;
    cmd->cmd_len = 0xC;
    cmd->lun = WLUN_RPMB;
    cmd->attr = ATTR_SIMPLE;
    cmd->cmd_len = 12;
    cmd->cmd_data[0] = SECURITY_PROTOCOL_IN; //opcode
    cmd->cmd_data[1] = protocol; //security protocol
    cmd->cmd_data[2] = (protocol_specific >> 8) & 0xFF; //security protocol specific
    cmd->cmd_data[3] = protocol_specific & 0xFF; //security protocol specific
    cmd->cmd_data[4] = 0x0;  // INC_512 = 0
    cmd->cmd_data[5] = 0x0; //Reserved
    cmd->cmd_data[6] = ((blk_cnt  << 9) >> 24) & 0xFF; //Reserved
    cmd->cmd_data[7] = ((blk_cnt  << 9) >> 16) & 0xFF; //Reserved
    cmd->cmd_data[8] = ((blk_cnt  << 9) >> 8) & 0xFF; //Reserved
    cmd->cmd_data[9] = 0x0; //(blk_cnt  << 9) & 0xFF; actually = 0 //Reserved
    cmd->cmd_data[10] = 0x0; //Reserved
    cmd->cmd_data[11] = 0x0; //control = 0
}

int rpmb_key_generate(struct rpmb_data_frame frame, uint8_t* rpmb_key)
{
    uint8_t hash[34]={0};
    uint8_t rpmbiv[16]={'RPMB KEYSASI'};
    uint8_t sw_rpmb[0x20]={'vutsrqponmlkjihgfedcba9876543210'};
    uint8_t* sasi=&rpmbiv[8];
    int res = -2;
    hmac_sha256(hash, frame.data, 512 - RPMB_DATA_BEG, (const uint8_t*)rpmb_key, 32);
    if (!memcmp(frame.key_MAC, hash, 32))
    {
        res=0;
    }
    else {
        memset(rpmb_key, 0, 0x20);
        hmac_sha256(hash, frame.data, 512 - RPMB_DATA_BEG, (const uint8_t *) rpmb_key, 32);
        if (!memcmp(frame.key_MAC, hash, 32)) {
            res=0;
        } else {
            WRAP_WR32(0x1000108C, 0x18000000);
            dxcc((volatile uint32_t *) 0x10210000, 1, rpmbiv, 8, sasi, 4, rpmb_key, 32);
            WRAP_WR32(0x10001088, 0x18000000);
            hmac_sha256(hash, frame.data, 512 - RPMB_DATA_BEG, (const uint8_t *) rpmb_key, 0x20);
            if (!memcmp(frame.key_MAC, hash, 32)) {
                res=0;
            } else {
                WRAP_WR32(0x10210A64, 0xFFFFFFFF);
                WRAP_WR32(0x1000108C, 0x18000000);
                dxcc((volatile uint32_t *) 0x10210000, 1, rpmbiv, 8, sasi, 4, rpmb_key, 32);
                WRAP_WR32(0x10001088, 0x18000000);
                hmac_sha256(hash, frame.data, 512 - RPMB_DATA_BEG, (const uint8_t *) rpmb_key, 0x20);
                if (!memcmp(frame.key_MAC, hash, 32)) {
                    res=0;
                } else {
                    memcpy(rpmb_key, sw_rpmb, 0x20);
                    hmac_sha256(hash, frame.data, 512 - RPMB_DATA_BEG, (const uint8_t *) rpmb_key, 0x20);
                    if (!memcmp(frame.key_MAC, hash, 32)) {
                        res=0;
                    }
                }
            }
        }
    }
    return res;
}

