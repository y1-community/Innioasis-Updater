// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#ifndef DA_X_RPMB_H
#define DA_X_RPMB_H
#include <stdint.h>
#include <stdbool.h>
#include "../../common/libc.h"

#define EXT_CSD_PART_CFG 179
#define WLUN_ID (1<<7)
#define WLUN_REPORT_LUNS (WLUN_ID | 0x1)
#define WLUN_UFS_DEVICE (WLUN_ID | 0x50)
#define WLUN_BOOT (WLUN_ID | 0x30)
#define WLUN_RPMB (WLUN_ID | 0x44)

enum {
    ATTR_SIMPLE = 0,
    ATTR_ORDERED = 1,
    ATTR_HEAD_OF_QUEUE = 2,
};

/*#define UFS_UPIU_RPMB_WLUN 0xC4*/
#define SECURITY_PROTOCOL_IN 0xA2
#define SECURITY_PROTOCOL_OUT 0xB5
#define UFS_SECURITY_PROTOCOL            0xEC
#define RPMB_PROTOCOL_ID        (0x1)

#define RPMB_PROGRAM_KEY       1       /* Program RPMB Authentication Key */
#define RPMB_GET_WRITE_COUNTER 2       /* Read RPMB write counter */
#define RPMB_WRITE_DATA        3       /* Write data to RPMB partition */
#define RPMB_READ_DATA         4       /* Read data from RPMB partition */
#define RPMB_RESULT_READ       5       /* Read result request */
#define RPMB_REQ_SEC_WPCB_WRITE 6
#define RPMB_REQ_SEC_WPCB_READ  7
#define RPMB_REQ               1       /* RPMB request mark */
#define RPMB_RESP              (1 << 1)/* RPMB response mark */
#define RPMB_AVALIABLE_SECTORS 8       /* 4K page size */

#define RPMB_TYPE_BEG          510  // FF
#define RPMB_RES_BEG           508  // FE
#define RPMB_BLKS_BEG          506  // FD
#define RPMB_ADDR_BEG          504  // FC
#define RPMB_WCOUNTER_BEG      500  // FA

#define RPMB_NONCE_BEG         484
#define RPMB_DATA_BEG          228
#define RPMB_MAC_BEG           196

#define UFS_UPIU_MAX_GENERAL_LUN    3

#define dma_data_direction uint8_t

struct rpmb_data_frame
{
    uint8_t stuff[196];
    uint8_t key_MAC[32];
    uint8_t data[256];
    uint8_t nonce[16];
    uint32_t wr_cnt;
    uint16_t addr;
    uint16_t blk_cnt;
    uint16_t result;
    uint16_t req_resp;
};

struct mmc_cid {
    unsigned int   manfid;
    char           prod_name[8];
    unsigned int   serial;
    unsigned short oemid;
    unsigned short year;
    unsigned char  hwrev;
    unsigned char  fwrev;
    unsigned char  month;
    unsigned char  cbx;
};

struct mmc_csd {
    unsigned char  csd_struct;          /* csd structure version */
    unsigned char  mmca_vsn;
    unsigned short cmdclass;            /* card command classes */
    unsigned short tacc_clks;           /* data read access-time-1 in clks */
    unsigned int   tacc_ns;             /* data read access-time-2 */
    unsigned int   r2w_factor;          /* write speed factor */
    unsigned int   max_dtr;             /* max. data transfer rate */
    unsigned int   read_blkbits;        /* max. read data block length */
    unsigned int   write_blkbits;       /* max. write data block length */
    unsigned int   capacity;            /* card capacity */
    unsigned int   erase_sctsz;         /* erase sector size */
    unsigned int   write_prot_grpsz;
    unsigned int   read_partial:1,
            read_misalign:1,
            write_partial:1,
            write_misalign:1,
            write_prot_grp:1,
            perm_wr_prot:1,
            tmp_wr_prot:1,
            erase_blk_en:1,
            copy:1,
            dsr:1;
};

struct mmc_raw_ext_csd {
    /* mode segment */
    unsigned char   rsv1[134];
    unsigned char   sec_bad_blk_mgmt;
    unsigned char   rsv2[1];
    unsigned char   enh_start_addr[4];
    unsigned char   enh_sz_mult[3];
    unsigned char   gp_sz_mult[12];
    unsigned char   part_set_cmpl;
    unsigned char   part_attr;
    unsigned char   max_enh_sz_mult[3];
    unsigned char   part_supp;
    unsigned char   rsv3[1];
    unsigned char   rst_n_func;
    unsigned char   rsv4[5];
    unsigned char   rpmb_sz_mult;
    unsigned char   fw_cfg;
    unsigned char   rsv5[1];
    unsigned char   user_wp;
    unsigned char   rsv6[1];
    unsigned char   boot_wp;
    unsigned char   rsv7[1];
    unsigned char   erase_grp_def;
    unsigned char   rsv8[1];
    unsigned char   boot_bus_width;
    unsigned char   boot_cfg_prot;
    unsigned char   part_cfg;
    unsigned char   rsv9[1];
    unsigned char   erase_mem_cont;
    unsigned char   rsv10[1];
    unsigned char   bus_width;
    unsigned char   rsv11[1];
    unsigned char   hs_timing;
    unsigned char   rsv12[1];
    unsigned char   pwr_cls;
    unsigned char   rsv13[1];
    unsigned char   cmd_set_rev;
    unsigned char   rsv14[1];
    unsigned char   cmd_set;

    /* propertities segment */
    unsigned char   ext_csd_rev;
    unsigned char   rsv15[1];
    unsigned char   csd_struct;
    unsigned char   rsv16[1];
    unsigned char   card_type;
    unsigned char   rsv17[1];
    unsigned char   pwr_cls_52_195;
    unsigned char   pwr_cls_26_195;
    unsigned char   pwr_cls_52_360;
    unsigned char   pwr_cls_26_360;
    unsigned char   rsv18[1];
    unsigned char   min_perf_r_4_26;
    unsigned char   min_perf_w_4_26;
    unsigned char   min_perf_r_8_26_4_52;
    unsigned char   min_perf_w_8_26_4_52;
    unsigned char   min_perf_r_8_52;
    unsigned char   min_perf_w_8_52;
    unsigned char   rsv19[1];
    unsigned char   sec_cnt[4];
    unsigned char   rsv20[1];
    unsigned char   slp_awake_tmo;
    unsigned char   rsv21[1];
    unsigned char   slp_curr_vccq;
    unsigned char   slp_curr_vcc;
    unsigned char   hc_wp_grp_sz;
    unsigned char   rel_wr_sec_cnt;
    unsigned char   erase_tmo_mult;
    unsigned char   hc_erase_grp_sz;
    unsigned char   acc_sz;
    unsigned char   boot_sz_mult;
    unsigned char   rsv22[1];
    unsigned char   boot_info;
    unsigned char   sec_trim_mult;
    unsigned char   sec_erase_mult;
    unsigned char   sec_supp;
    unsigned char   trim_mult;
    unsigned char   rsv23[1];
    unsigned char   min_perf_ddr_r_8_52;
    unsigned char   min_perf_ddr_w_8_52;
    unsigned char   rsv24[2];
    unsigned char   pwr_cls_ddr_52_195;
    unsigned char   pwr_cls_ddr_52_360;
    unsigned char   rsv25[1];
    unsigned char   ini_tmo_ap;
    unsigned char   rsv26[262];
    unsigned char   supp_cmd_set;
    unsigned char   rsv27[7];
};

struct mmc_ext_csd {
    unsigned int    trim_tmo_ms;
    unsigned int    hc_wp_grp_sz;
    unsigned int    hc_erase_grp_sz;
    unsigned int    sectors;
    unsigned int    hs_max_dtr;
    unsigned int    boot_part_sz;
    unsigned int    rpmb_sz;
    unsigned int    access_sz;
    unsigned int    enh_sz;
    unsigned int    enh_start_addr;
    unsigned char   rev;
    unsigned char   boot_info;
    unsigned char   part_en:1,
            enh_attr_en:1,
            ddr_support:1;
    unsigned char   erased_mem_cont;
};


struct sd_scr {
    unsigned char   scr_struct;
    unsigned char   sda_vsn;
    unsigned char   data_bit_after_erase;
    unsigned char   security;
    unsigned char   bus_widths;
    unsigned char   sda_vsn3;
    unsigned char   ex_security;
    unsigned char   cmd_support;
};

struct sd_switch_caps {
    unsigned int    hs_max_dtr;
    unsigned int    ddr;
    unsigned int    drv_strength;
    unsigned int    max_cur;
};

struct mmc_host
{
    struct mmc_card *card;
    uint64_t max_hw_segs;
    uint64_t max_phys_segs;
    uint64_t max_seg_size;
    uint32_t max_blk_size;
    uint32_t max_blk_count;
    uint32_t base;
    uint32_t caps;
    uint32_t f_min;
    uint32_t f_max;
    uint32_t clk;
    uint32_t sclk;
    uint32_t blklen;
    uint32_t blkbits;
    uint32_t ocr;
    uint32_t ocr_avail;
    uint32_t timeout_ns;
    uint32_t timeout_clks;
    uint8_t  clksrc;
    uint8_t  id;
    uint8_t  boot_type;
    uint8_t  app_cmd;
    uint32_t  app_cmd_arg;
    uint32_t  time_read;
    void *priv;
    int (*blk_read)(struct mmc_host *host, uint8_t *dst, uint32_t src, uint32_t nblks);
    int (*blk_write)(struct mmc_host *host, uint32_t dst, uint8_t *src, uint32_t nblks);
};

/* MMC device */
struct mmc_card {
    struct mmc_host        *host;
    unsigned int            nblks;
    unsigned int            blklen;
    unsigned int            ocr;
    unsigned int            maxhz;
    unsigned int            uhs_mode;
    unsigned int            rca;
    unsigned int            type;
    unsigned short          state;
    unsigned short          ready;
    uint32_t                raw_cid[4];
    uint32_t                raw_csd[4];
    uint32_t                raw_scr[2];
    uint8_t                 raw_ext_csd[512];
    struct mmc_cid          cid;
    struct mmc_csd          csd;
    struct mmc_ext_csd      ext_csd;
    struct sd_scr           scr;
    struct sd_switch_caps   sw_caps;
};


#define MAX_CDB_SIZE                16

enum dma_data_direction {
    DMA_BIDIRECTIONAL = 0,
    DMA_TO_DEVICE = 1,
    DMA_FROM_DEVICE = 2,
    DMA_NONE = 3,
};

struct ufs_aio_scsi_cmd {
    uint32_t lun;
    int tag;
    dma_data_direction dir; //dma_data_direction
    uint8_t attr;
    uint8_t cmd_data[MAX_CDB_SIZE];
    uint16_t cmd_len;
    uint32_t exp_len;
    struct rpmb_data_frame * data_buf;
};

/* UTP QUERY Transaction Specific Fields OpCode */
enum query_opcode {
    UPIU_QUERY_OPCODE_NOP        = 0x0,
    UPIU_QUERY_OPCODE_READ_DESC    = 0x1,
    UPIU_QUERY_OPCODE_WRITE_DESC    = 0x2,
    UPIU_QUERY_OPCODE_READ_ATTR    = 0x3,
    UPIU_QUERY_OPCODE_WRITE_ATTR    = 0x4,
    UPIU_QUERY_OPCODE_READ_FLAG    = 0x5,
    UPIU_QUERY_OPCODE_SET_FLAG    = 0x6,
    UPIU_QUERY_OPCODE_CLEAR_FLAG    = 0x7,
    UPIU_QUERY_OPCODE_TOGGLE_FLAG    = 0x8,
};

/* Flag idn for Query Requests*/
enum flag_idn {
    QUERY_FLAG_IDN_FDEVICEINIT      = 0x01,
    QUERY_FLAG_IDN_PWR_ON_WPE    = 0x03,
    QUERY_FLAG_IDN_BKOPS_EN         = 0x04,
};

/* Attribute idn for Query requests */
enum attr_idn {
    QUERY_ATTR_IDN_ACTIVE_ICC_LVL    = 0x03,
    QUERY_ATTR_IDN_BKOPS_STATUS    = 0x05,
    QUERY_ATTR_IDN_REF_CLK_FREQ    = 0x0A,
    QUERY_ATTR_IDN_EE_CONTROL    = 0x0D,
    QUERY_ATTR_IDN_EE_STATUS    = 0x0E,
};

/* Descriptor idn for Query requests */
enum desc_idn {
    QUERY_DESC_IDN_DEVICE           = 0x0,
    QUERY_DESC_IDN_CONFIGURATION    = 0x1,
    QUERY_DESC_IDN_UNIT             = 0x2,
    QUERY_DESC_IDN_RFU_0            = 0x3,
    QUERY_DESC_IDN_INTERCONNECT     = 0x4,
    QUERY_DESC_IDN_STRING           = 0x5,
    QUERY_DESC_IDN_RFU_1            = 0x6,
    QUERY_DESC_IDN_GEOMETRY         = 0x7,
    QUERY_DESC_IDN_POWER            = 0x8,
    QUERY_DESC_IDN_HEALTH       = 0x9,
    QUERY_DESC_IDN_MAX,
};

#define ufs_paddr_t uint32_t

struct ufs_pa_layer_attr {
    uint32_t gear_rx;
    uint32_t gear_tx;
    uint32_t lane_rx;
    uint32_t lane_tx;
    uint32_t pwr_rx;
    uint32_t pwr_tx;
    uint32_t hs_rate;
};

#define UFS_MAX_CMD_DATA_SIZE   (64)

enum dev_cmd_type {
    DEV_CMD_TYPE_NOP        = 0x0,
    DEV_CMD_TYPE_QUERY        = 0x1,
};

#define MAX_PRODUCT_ID_LEN              (16)
#define MAX_PRODUCT_REVISION_LEVEL_LEN  (4)
#define MAX_SERAL_NUMBER_LEN            (64) /* spec (126*2), 64 because code size */

struct ufs_device_info {
    uint16_t wmanufacturerid;                     // from Device Descriptor
    uint8_t  num_active_lu;                       // from Device Descriptor
    uint16_t ufs_ver;                             // from Device Descriptor
    uint8_t  bootable;
    char product_id[MAX_PRODUCT_ID_LEN + 1];
    char product_revision_level[MAX_PRODUCT_REVISION_LEVEL_LEN + 1];
    char serial_number[MAX_SERAL_NUMBER_LEN * 2 + 1]; /* 1 byte need 2 char(ex.FF) + 1 end */
    uint8_t  serial_number_len;
    uint8_t  ud0_base_offset;
    uint8_t  ud_config_len;
    uint8_t  hpb_support;
    uint16_t hpb_ver;
    uint8_t  tw_support;
    uint8_t  tw_red;
    uint8_t  tw_type;
    uint16_t tw_ver;
    uint32_t wb_buf_au;
    uint8_t pre_eol_info;
    uint8_t life_time_est_a;
    uint8_t life_time_est_b;
};
struct ufs_custom_info {
    uint32_t  custom_flag;
    uint32_t  force_provision; /* default:0, force:1, skip:2 */
    uint32_t  tw_size_gb;
    uint32_t  tw_no_red;
    uint32_t  hpb_size_gb;
};

struct ufs_pwr_mode_info {
    bool is_valid;
    struct ufs_pa_layer_attr info;
};

struct ufs_unit_desc_cfg_param {
    uint8_t b_lu_enable;
    uint8_t b_boot_lun_id;
    uint8_t b_lu_write_protect;
    uint8_t b_memory_type;
    uint8_t d_num_alloc_units[4];
    uint8_t b_data_reliability;
    uint8_t b_logical_block_size;
    uint8_t b_provisioning_type;
    uint8_t w_context_capabilities[2];
    uint8_t reserved[3];
};

typedef enum {
    UFS_LU_0 = 0
    ,UFS_LU_1 = 1
    ,UFS_LU_2 = 2
    ,UFS_LU_3 = 3
    ,UFS_LU_INTERNAL_CNT = 3
} ufs_logical_unit_internal;

/**
 * struct utp_upiu_query - upiu request buffer structure for
 * query request.
 * @opcode: command to perform B-0
 * @idn: a value that indicates the particular type of data B-1
 * @index: Index to further identify data B-2
 * @selector: Index to further identify data B-3
 * @reserved_osf: spec reserved field B-4,5
 * @length: number of descriptor bytes to read/write B-6,7
 * @value: Attribute value to be written DW-5
 * @reserved: spec reserved DW-6,7
 */
struct utp_upiu_query {
    uint8_t opcode;
    uint8_t idn;
    uint8_t index;
    uint8_t selector;
    uint16_t reserved_osf;
    uint16_t length;
    uint32_t value;
    uint32_t reserved[2];
};

/**
 * struct ufs_query_req - parameters for building a query request
 * @query_func: UPIU header query function
 * @upiu_req: the query request data
 */
struct ufs_query_req {
    uint8_t query_func;
    struct utp_upiu_query upiu_req;
};

/**
 * struct ufs_query_resp - UPIU QUERY
 * @response: device response code
 * @upiu_res: query response data
 */
struct ufs_query_res {
    uint8_t response;
    struct utp_upiu_query upiu_res;
};

/**
 * struct ufs_query - holds relevent data structures for query request
 * @request: request upiu and function
 * @descriptor: buffer for sending/receiving descriptor
 * @response: response upiu and response
 */
struct ufs_query {
    struct ufs_query_req request;
    uint8_t *descriptor;
    struct ufs_query_res response;
};

/**
 * struct ufs_dev_cmd - all assosiated fields with device management commands
 * @type: device management command type - Query, NOP OUT
 * @lock: lock to allow one command at a time
 * @complete: internal commands completion
 * @tag_wq: wait queue until free command slot is available
 */
struct ufs_dev_cmd {
    enum dev_cmd_type type;
    struct ufs_query query;
};

struct ufs_hba {
    void    *hci_base;
    void    *pericfg_base;
    void    *mphy_base;
    int     nutrs;
    //int     nutmrs;

    /* Virtual memory reference */
    struct utp_transfer_cmd_desc *ucdl_base_addr;
    struct utp_transfer_req_desc *utrdl_base_addr;
    //struct utp_task_req_desc *utmrdl_base_addr;
    //void * sense_buf_base_addr[UFS_AIO_MAX_NUTRS];

    /* DMA memory reference */
    ufs_paddr_t ucdl_dma_addr;
    ufs_paddr_t utrdl_dma_addr;
    //ufs_paddr_t utmrdl_dma_addr;
    //ufs_paddr_t sense_buf_dma_addr[UFS_AIO_MAX_NUTRS];

    unsigned int hci_quirks;
    unsigned int dev_quirks;

    struct uic_command *active_uic_cmd;
    struct ufs_pa_layer_attr pwr_info;

    struct ufshcd_lrb *lrb;
    unsigned long lrb_in_use;

    struct ufs_device_info dev_info;
    struct ufs_custom_info custom_info;

    uint8_t  active_tr_tag;
    uint8_t  mode;
    uint8_t  unit_desc_cfg_param_valid;
    //uint8_t  active_tm_tag;
    int  active_lun;

    unsigned long outstanding_reqs;

    struct ufs_pwr_mode_info max_pwr_info;

    /* Device management request data */
    struct ufs_dev_cmd dev_cmd;

    int (* blk_read)(struct ufs_hba * hba, uint32_t lun, uint32_t blk_start, uint32_t blk_cnt, unsigned long * buf);
    int (* blk_write)(struct ufs_hba * hba, uint32_t lun, uint32_t blk_start, uint32_t blk_cnt, unsigned long * buf);
    int (* blk_erase)(struct ufs_hba * hba, uint32_t lun, uint32_t blk_start, uint32_t blk_cnt);
    int (* nopin_nopout)(struct ufs_hba * hba);
    int (* query_flag)(struct ufs_hba *hba, enum query_opcode opcode, enum flag_idn idn, bool *flag_res);
    int (* query_attr)(struct ufs_hba *hba, enum query_opcode opcode, enum attr_idn idn, uint8_t index, uint8_t selector, uint32_t *attr_val);
    int (* read_descriptor)(struct ufs_hba * hba, enum desc_idn desc_id, int desc_index, uint8_t selector, uint8_t *buf, uint32_t size);
    int (* write_descriptor)(struct ufs_hba * hba, enum desc_idn desc_id, int desc_index, uint8_t selector, uint8_t *buf, uint32_t size);
    int (* dme_get)(struct ufs_hba *hba, uint32_t attr_sel, uint32_t *mib_val);
    int (* dme_peer_get)(struct ufs_hba *hba, uint32_t attr_sel, uint32_t *mib_val);
    int (* dme_set)(struct ufs_hba *hba, uint32_t attr_sel, uint32_t mib_val);
    int (* dme_peer_set)(struct ufs_hba *hba, uint32_t attr_sel, uint32_t mib_val);
    int (* ffu_write)(struct ufs_hba * hba, unsigned long * buf, uint32_t buf_size);

    // unit descriptor configurable parameters (in Configuration Descriptor)
    struct ufs_unit_desc_cfg_param unit_desc_cfg_param[UFS_UPIU_MAX_GENERAL_LUN];

    uint32_t drv_status;
    uint32_t irq;
};

void ufshcd_put_tag(struct ufs_hba *hba, int tag);
void cmd_scsi_security_protocol_out(struct ufs_aio_scsi_cmd *cmd, int tag);
void cmd_scsi_security_protocol_in(struct ufs_aio_scsi_cmd *cmd, int tag);
int rpmb_key_generate(struct rpmb_data_frame frame, uint8_t* rpmb_key);

#endif //DA_X_RPMB_H
