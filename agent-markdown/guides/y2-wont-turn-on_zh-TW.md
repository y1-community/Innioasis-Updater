---
title: "Innioasis Y2 無法開啟 | Innioasis 韌體存檔 - Innioasis 韌體下載"
description: "Innioasis Y2 無法開機或充電？強制重新啟動，檢查電腦是否發現它，然後恢復 Y2 韌體或使用手動 SP Flash Tool 恢復。"
language: "zh-TW"
source: "https://innioasis.app/guides/y2-wont-turn-on_zh-TW.html"
---

# Innioasis Y2 無法開啟 | Innioasis 韌體存檔 - Innioasis 韌體下載

玩家恢復·Innioasis Y2

# Innioasis Y2 無法開啟

黑屏並不總是意味著玩家死亡。在嘗試手動閃光之前，請先完成充電、強制重新啟動和電腦偵測。[取得 Updater CE](../guide_zh-TW.html#platform)[韌體下載](../firmware_zh-TW.html)[恢復指南](recovery_zh-TW.html)

## 先給 Y2 正確充電

大多數「Y2 無法開機」報告是電池沒電、僅充電的電纜或無法提供足夠電流的充電器。嚴重耗盡的 Y2 可能需要 20 到 30 分鐘才能在螢幕上顯示任何內容。
  - 使用已知的 USB 數據 電纜，而不是僅充電電纜。
  - 嘗試使用壁式充電器，然後直接使用電腦 USB 連接埠 - 而不是集線器。
  - 將其保持連接 30 到 60 分鐘，然後觀察充電圖示或背光。
  - 在繼續之前嘗試使用第二條電纜和充電器。

## 強制重啟

按住電源按鈕約 15 秒鐘，放開，等待五秒鐘，然後按電源一次。這會清除掛起的啟動，並且可以安全地重複。

如果螢幕顯示徽標然後變黑，則表示播放器正在啟動但發生故障 - 跳到下面的韌體恢復。如果沒有任何反應，請保持充電狀態，半小時後再試一次。

## 檢查電腦是否可以看到播放器

用數據線連接已關閉電源的Y2，並在Windows上開啟裝置管理員， `lsusb` 在 Linux 上，或在 macOS 上 MTKClient。正在運行的播放器顯示為具有供應商 ID 的 MediaTek 設備 `0e8d`。如果出現，即使螢幕保持黑暗，硬體也足夠活躍以重新閃爍。

如果沒有出現任何內容，請先在 Windows 上安裝 MediaTek 驅動程式 — [司機指南](../drivers_zh-TW.html) 涵蓋 Windows 和 Linux 權限。

## 恢復 Y2 庫存固件

如果偵測到播放器但無法啟動，請重新安裝 Y2 原始軟體。僅使用 Y2 套件； Y1 建置不會在 Y2 硬體上啟動。
  - 打開 [更新程式 CE](../guide_zh-TW.html#platform) 在您的計算機上。
  - 套裝 裝置型號 到 Y2.
  - 選擇 原廠軟體 在 軟體 並選擇一個穩定的 Y2 版本 - 手冊包是 `rom_y2.zip`.
  - 點選 安裝 / 還原 並讓包解壓縮。
  - 完全關閉 Y2 電源，僅在更新程式要求時連接 USB 資料線，直到出現成功訊息為止。
保持電源穩定。 閃光燈斷電可能導致播放器無法使用。先充電，然後直接連接電腦。

## 當更新程式無法看到播放器時手動恢復

更新程式 CE 包含手動恢復工具，用於指導安裝無法完成的情況。 [SP Flash Tool](../sp-flash-tool_zh-TW.html) 捆綁在 Windows 和 Linux x86 上，MTKClient 路線涵蓋 macOS。兩者都需要來自 [韌體下載](../firmware_zh-TW.html) 頁。

請遵循適合您平台的工具指南，而不是即興創作分散文件或偏移。如果任何工具都未偵測到播放器，故障可能出在電池、充電埠或主機板上。

## 如果仍然無法啟動

停止閃爍並將其視為硬體。請勿打開外殼或按壓電池。詢問社區的型號、螢幕的用途、電腦是否檢測到它以及您嘗試過哪些軟體包 - [Discord 社區](https://discord.gg/zHrT2zrcek) 可以協助確定服務路線。

庫存恢復會取代系統，因此在刷新之前請備份播放器記憶體中儲存的所有內容。恢復不會影響 MicroSD 卡上的音樂。

## Innioasis Y2電源常見問題解答

### 為什麼我的 Innioasis Y2 無法打開？

通常的原因是電池完全耗盡、僅充電的電纜或充電器電量不足、韌體崩潰導致啟動停止或硬體故障。在假設玩家死亡之前，使用已知的數據線為其充電 30 分鐘。

### 如何強制重啟 Innioasis Y2？

按住電源按鈕約 15 秒鐘，放開，等待五秒鐘，然後按電源一次。如果沒有任何反應，請保持充電狀態，並在 30 分鐘後重試。

### 我可以恢復無法開機的 Y2 嗎？

經常是的。如果電腦仍然偵測到 MediaTek 設備，請使用 Updater CE 重新安裝 Y2 原始軟體包。如果未偵測到，請使用 Updater CE 隨附的 SP Flash Tool 或 MTKClient 恢復以及與型號相符的 Y2 韌體檔案。

### Y2 刷機前需要充電嗎？

是的。閃光燈斷電可能導致播放器無法使用。首先為其充電，然後將其直接連接到計算機，而不是透過集線器。

## 相關修復
  - [Y1打不開](y1-wont-turn-on_zh-TW.html) — 對 Y1 進行相同的檢查
  - [Y2滾輪不工作](y2-scroll-wheel-not-working_zh-TW.html) — 如果它啟動但輪子不啟動
  - [Innioasis恢復指南](recovery_zh-TW.html) — 所有症狀指南都集中在一處
  - [SP Flash Tool 指南](../sp-flash-tool_zh-TW.html) — Windows 和 Linux 上手動刷新
  - [安裝故障排除](../troubleshooting_zh-TW.html) — 失敗的閃光燈是什麼樣子的

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
