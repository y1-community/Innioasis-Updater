---
title: "Innioasis Y1 和 Y2 復原指南 | Innioasis 韌體存檔 - Innioasis 韌體下載"
description: "針對更新後無法開機或滾輪停止工作的 Innioasis Y1 和 Y2 玩家的恢復指南。重置和韌體步驟。"
language: "zh-TW"
source: "https://innioasis.app/guides/recovery_zh-TW.html"
---

# Innioasis Y1 和 Y2 復原指南 | Innioasis 韌體存檔 - Innioasis 韌體下載

玩家恢復 · Y1 和 Y2

# Innioasis Y1 和 Y2 恢復指南

無法啟動、輪子不工作或安裝中途停止。從症狀開始，然後按順序執行步驟，而不是直接跳到手動閃光。[取得 Updater CE](../guide_zh-TW.html#platform)[韌體下載](../firmware_zh-TW.html)[疑難排解](../troubleshooting_zh-TW.html)

以 Innioasis Updater 開頭

## 引導安裝修復了大部分問題

更新程序一次性完成此操作。選擇軟體，依照螢幕上的步驟操作，即可完成。它還會告訴您修復或新版本何時發布。

## 從症狀入手

這些指南涵蓋了人們在更新或刷新後最常遇到的兩種故障。選擇與您所看到的相符的一項，然後按順序完成它。

### 滾輪不工作

輪子轉動但玩家忽略它，或更新後輪子立即停止。

[Y1 滾輪引導](y1-scroll-wheel-not-working_zh-TW.html) · [Y2 滾輪引導](y2-scroll-wheel-not-working_zh-TW.html)

### 播放器無法開機

黑屏、充電指示燈不亮或標誌時隱時現。

[Y1電源指南](y1-wont-turn-on_zh-TW.html) · [Y2電源指南](y2-wont-turn-on_zh-TW.html)

### 安裝中途停止

更新程式在 USB 提示之前或之後失敗，或版本清單看起來錯誤。

[故障排除指南](../troubleshooting_zh-TW.html)

### 需要文件

每個型號的原始軟體和定制包。

[韌體下載](../firmware_zh-TW.html)

## Y1 和 Y2 套件不可互換切勿對模型進行交叉閃爍。 一個Y1 `rom.zip` 不是 Y2 包，而是 Y2 `rom_y2.zip` 不會在 Y1 上運行。閃爍錯誤的模型是玩家最終出現死控製或啟動循環的最常見原因之一。

檢查播放器上列印的型號，然後在選擇版本之前在 Updater CE 中進行匹配。

## 先恢復配對的原版軟體

在使用任何手動工具之前，請將正確型號的庫存韌體放回播放器上。這修復了大多數與更新相關的輪子和啟動故障。

Y1: 選擇Y1，選擇原始軟體，選擇穩定的Y1版本，然後執行安裝/復原。 [完整的 Y1 恢復指南](restore-original-y1_zh-TW.html).

Y2: 選擇Y2，選擇原始軟體，選擇穩定的Y2版本，然後執行安裝/復原。 [完整的 Y2 恢復指南](restore-original-y2_zh-TW.html).

僅當更新程式要求時，關閉播放器並連接 USB 數據線。保持連線狀態，直到出現成功訊息。

## Updater CE 附帶的手動恢復

當更新程式無法完成作業時，相同的安裝包括手動工具。 [SP Flash Tool](../sp-flash-tool_zh-TW.html) 捆綁在 Windows 和 Linux x86 機器上，MTKClient 路線涵蓋 macOS。兩者都需要與型號相匹配的固件包，可在 [韌體下載](../firmware_zh-TW.html) 頁。

使用適合您平台的指南並保持播放器電量充足。如果根本沒有工具偵測到播放器，故障可能是硬體而不是韌體。

## 尋求協助時應包括哪些內容
  - 型號 - Y1 或 Y2 - 印在播放器上。
  - 螢幕的作用：什麼都沒有、標誌、啟動循環或主螢幕。
  - 計算機是否將播放器偵測為 MediaTek 裝置。
  - 確切的更新程式訊息和您選擇的軟體包。
  - 您已經嘗試過的內容，包括任何手動工具。

不要發布私人令牌或無關的系統檔案。這 [社區 Discord](https://discord.gg/zHrT2zrcek) 和 [r/innioasis](https://reddit.com/r/innioasis) 是交換意見最快的地方。

## Innioasis 恢復常見問題解答

### 如何修復無法開機的 Innioasis 播放器？

用已知的數據線充電30分鐘，長按15秒強制重啟，然後檢查電腦是否偵測到。如果是，則恢復對應型號的原版軟體；如果沒有，請使用 Updater CE 隨附的手動恢復工具。

### 為什麼我的 Y1 或 Y2 滾輪不工作？

如果更新後輪子停止，通常是韌體不匹配。重新安裝型號匹配的原始軟體並再次測試。如果每個韌體中的輪子都死了，請將其視為硬體故障。

### 在哪裡下載用於恢復的韌體？

innoasis.app/firmware.html 上的韌體下載頁麵包含每個型號的原始套件和自訂套件。始終選擇與玩家相符的 Y1 或 Y2 套件。

### Updater CE 包含哪些復原工具？

更新程式 CE 包括 Windows 和 Linux 上的 SP Flash Tool，以及包含 macOS 的 MTKClient 路線，用於在正常安裝無法完成時進行手動復原。

## 相關修復
  - [Y1滾輪不工作](y1-scroll-wheel-not-working_zh-TW.html) — 更新後點選滾輪無響應
  - [Y2滾輪不工作](y2-scroll-wheel-not-working_zh-TW.html) — 對 Y2 進行相同的檢查
  - [Y1打不開](y1-wont-turn-on_zh-TW.html) — 充電、重新啟動和手動恢復
  - [Y2打不開](y2-wont-turn-on_zh-TW.html) — 對 Y2 進行相同的檢查
  - [SP Flash Tool 指南](../sp-flash-tool_zh-TW.html) — Windows 和 Linux 上手動刷新

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
