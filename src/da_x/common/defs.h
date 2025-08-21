// Copyright 2024 (c) B.Kerler
// Use of this source code is governed by a GPLv3 license, see LICENSE.txt.

#ifndef DA_X_DEFS_H
#define DA_X_DEFS_H
#define WRAP_RD32(addr)            (*(volatile uint32_t *)(addr))
#define WRAP_WR32(addr,data)       ((*(volatile uint32_t *)(addr)) = (uint32_t)data)
#define WRAP_SET_BIT(BS,REG)       ((*(volatile uint32_t*)(REG)) |= (uint32_t)(BS))
#define WRAP_CLR_BIT(BS,REG)       ((*(volatile uint32_t*)(REG)) &= ~((uint32_t)(BS)))
#endif //DA_X_DEFS_H
