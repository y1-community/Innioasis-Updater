---
title: "MTKClient 和低階復原指南 - Innioasis 和 Timmkoo - Innioasis 韌體下載"
description: "使用 MTKClient 和 SP Flash Tool 為 Innioasis 和 Timmkoo 播放器提供低階 MediaTek 復原、引導程式 unbrick 指令以及驅動程式診斷。"
language: "zh-TW"
source: "https://innioasis.app/mtkclient_zh-TW.html"
---

# MTKClient 和低階復原指南 - Innioasis 和 Timmkoo - Innioasis 韌體下載

進階診斷·MediaTek

# MTKClient & Unbrick 診斷

MTKClient 是 Innioasis Updater CE 使用的底層開源 MediaTek 刷新引擎。如果播放器變得無回應或標準刷新失敗，請使用這些復原診斷。[一般故障排除](troubleshooting_zh-TW.html)[驅動程式設定注意事項](drivers_zh-TW.html)

以 Innioasis Updater 開頭

## 在低級別路線之前先嘗試引導路線

更新程序一次性完成此操作。選擇軟體，依照螢幕上的步驟操作，即可完成。它還會告訴您修復或新版本何時發布。

## 了解 BootROM (BROM) 模式

當完全斷電時，MediaTek MT6572 / MT6580 處理器會在載入主引導程式之前在 USB 總線上偵聽握手封包。如果發生損壞的閃存，BROM 模式允許完全恢復重寫。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
