// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#include "dxcc.h"

void SaSi_SB_AddDescSequence(volatile uint32_t *result, HwDesc_s *desc)
{
  while ( (result[DX_DSCRPTR_QUEUE0_CONTENT_REG_OFFSET/4] & 0x3FF) == 0 )
    ;
  result[DX_DSCRPTR_QUEUE0_WORD0_REG_OFFSET/4] = (volatile uint32_t)desc->word[0];
  result[DX_DSCRPTR_QUEUE0_WORD1_REG_OFFSET/4] = (volatile uint32_t)desc->word[1];
  result[DX_DSCRPTR_QUEUE0_WORD2_REG_OFFSET/4] = (volatile uint32_t)desc->word[2];
  result[DX_DSCRPTR_QUEUE0_WORD3_REG_OFFSET/4] = (volatile uint32_t)desc->word[3];
  result[DX_DSCRPTR_QUEUE0_WORD4_REG_OFFSET/4] = (volatile uint32_t)desc->word[4];
  result[DX_DSCRPTR_QUEUE0_WORD5_REG_OFFSET/4] = (volatile uint32_t)desc->word[5];
}

void SaSi_PalDmaMap(uint32_t offset, volatile uint64_t* dst)
{
    *dst=offset;
}

int SB_ReadFlag(volatile uint32_t* base)
{
    volatile uint32_t res=0;
    do {
        res=base[0xBA0/4];
    }
    while (!res);
    return res;
}

void SaSi_PalDmaUnMap(volatile uint64_t* dst)
{
    (void)dst;
}

void SB_HalInit(volatile uint32_t* base)
{
    base[DX_HOST_ICR_REG_OFFSET/4]=(volatile uint32_t)4;
}

int SB_CryptoWait(volatile uint32_t* base)
{
    volatile uint32_t val;
    do {
        val=(volatile uint32_t)base[DX_HOST_IRR_REG_OFFSET/4];
    } while (!val);
    return val;
}

int SB_HalWaitDescCompletion(volatile uint32_t* base)
{
  struct HwDesc desc;
  SB_HalInit(base);
  uint32_t outv = 0;
  volatile uint64_t out = 0;
  SaSi_PalDmaMap((uint32_t)&outv, &out);
  desc.word[0] = 0;
  desc.word[1] = 0x8000011;
  desc.word[2] = out;
  desc.word[5] = ((out>>32)&0xFFFFFFFF) << 16;
  desc.word[3] = 0x8000012;
  desc.word[4] = 0x100;
  SaSi_SB_AddDescSequence(base, &desc);
  while ( (SB_CryptoWait(base) & 4) == 0 );
  volatile uint32_t val=0;
  do
  {
    val = SB_ReadFlag(base);
  } while (!val);
  if ( val == 1 )
  {
    SB_HalInit(base);
    SaSi_PalDmaUnMap(&out);
    return 0;
  }
  else
  {
    SaSi_PalDmaUnMap(&out);
    return 0xF6000001;
    }
}

void write_reg(volatile uint32_t addr, volatile uint32_t value)
{
    *(volatile uint32_t*)addr=value;
}

int SBROM_AesCmacDriver(volatile uint32_t *base,
        uint32_t hwmode,
        uint64_t key,
        uint64_t buf,
        int bufferlen,
        uint64_t out)
{
  struct HwDesc desc;
  int keylen = 0;
  if ( hwmode == 1 )
  {
    if (((base[DX_HOST_SEP_HOST_GPR4_REG_OFFSET/4])&2)!=0)
    {
        keylen = 32;
    }
    else
    {
        keylen = 16;
    }
  }
  else
  {
    keylen = 16;
  }
  SB_HalInit(base);
  volatile uint32_t kval = (keylen << 19) - 0x800000;
  desc.word[1] = 0x8000041;
  desc.word[4] = kval | 0x1001C20;
  desc.word[0] = 0;
  desc.word[2] = 0;
  desc.word[3] = 0;
  desc.word[5] = 0;
  SaSi_SB_AddDescSequence(base, &desc);

desc.word[0] = 0;
desc.word[1] = 0;
desc.word[2] = 0;
desc.word[3] = 0;
desc.word[4] = 0;

if ( !hwmode )
{
desc.word[0] = (uint32_t)key;
desc.word[5] = (uint16_t)(key>>32);
desc.word[1] = 0x42;
}
desc.word[4] = kval | ((hwmode&3)<<15) | (((hwmode>>2)&3)<<20) | 0x4001C20;
SaSi_SB_AddDescSequence(base, &desc);

desc.word[2] = 0;
desc.word[0] = (uint32_t)buf;
desc.word[5] = (uint16_t)(buf>>32);
desc.word[3] = 0;
desc.word[1] = (4 * (bufferlen & 0xFFFFFF)) | 2;
desc.word[4] = 1;
SaSi_SB_AddDescSequence(base, &desc);

  if (hwmode!=2)
  {
      desc.word[5] = ((uint16_t)(out>>32)) << 16;
      desc.word[0] = 0;
      desc.word[4] = 0x8001C26;
      desc.word[1] = 0;
      desc.word[2] = (uint32_t)out;
      desc.word[3] = 0x42;
      SaSi_SB_AddDescSequence(base, &desc);
  }

return SB_HalWaitDescCompletion(base);
}

int SBROM_AesCMac(volatile uint32_t* base, int hwmode, uint8_t* buffer, int bufferlen, uint8_t* outbuf)
{
    int ret;
    uint64_t iv=0;
    /*if (val0)
        SaSi_PalDmaMap((uint32_t)&val0, &iv);
    if (buffer)
        SaSi_PalDmaMap((uint32_t)&buffer, &buf);
    if (outbuf)
        SaSi_PalDmaMap((uint32_t)&outbuf, &out);
    */

    ret = SBROM_AesCmacDriver(base, hwmode, iv, (uint32_t)buffer, bufferlen, (uint32_t)outbuf);
    /*if (val0)
        SaSi_PalDmaUnMap(&iv);
    if (buffer)
        SaSi_PalDmaUnMap(&buf);
    if (outbuf)
        SaSi_PalDmaUnMap(&out);
    */
    return ret;
}
int dxcc(volatile uint32_t* base, int hwmode, uint8_t* key, int keylen, uint8_t* seed, int seedlen, uint8_t* outbuf, int derivelen)
{
    uint8_t* buffer=(uint8_t*)0x200d10;
    uint8_t* tmp=(uint8_t*)0x200d00;
    uint32_t i;
    uint32_t pos=0;
    int ret;
    if (!hwmode)
        return 0xF2000002;
    if (!key && (keylen || keylen > 0x20))
        return 0xF2000003;
    if (!seed && (seedlen || seedlen > 0x20))
        return 0xF2000003;
    memset(buffer,0,0x43);
    buffer[pos++]=1;
    if (key)
    {
        memcpy(&buffer[pos++], key, keylen);
        pos += keylen;
    }
    buffer[pos]=0;
    if (seed)
    {
        memcpy(&buffer[pos], seed, seedlen);
        pos += seedlen;
    }
    buffer[pos]=(8*derivelen)&0xFF;
    for (i=0;i<((uint32_t)derivelen+15)>>4;i++)
    {
        buffer[0] = i+1;
        ret = SBROM_AesCMac(base,hwmode,buffer,keylen+seedlen+3,tmp);
        memcpy(outbuf+(16*i),tmp,0x10);
        if (ret)
            return ret;
    }
    return 0;
}