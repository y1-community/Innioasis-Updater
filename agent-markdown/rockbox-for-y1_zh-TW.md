---
title: "Rockbox for Y1 (Rockbox-Y1)：概述、建置與安裝指南"
description: "Y1、Rockbox-Y1 的 Rockbox 和 rockbox-y1 皆引用 Innioasis Y1 的社群 Rockbox 韌體。了解它添加了什麼、選擇哪個版本以及如何使用 Innioasis Updater CE 安裝它。"
language: "zh-TW"
source: "https://innioasis.app/rockbox-for-y1_zh-TW.html"
---

# Rockbox for Y1 (Rockbox-Y1)：概述、建置與安裝指南

[← 韌體下載](firmware_zh-TW.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox 為 Y1 (Rockbox-Y1)

「Rockbox」、「Rockbox-Y1」和「Y1 的Rockbox」均指 Innioasis Y1 的同一社區 Rockbox 韌體。以下是它向您的播放器添加的內容、要選擇的版本以及如何使用 Innioasis Updater CE 安裝它。[安裝Rockbox-Y1](rockbox-y1/install.html)[下載ROM](rockbox-y1/download.html)[書面教程](guides/rockbox-y1.html)[Rockbox-Y1 輪轂](rockbox-y1/)

## 一個韌體，多個名稱

在 Innioasis Updater CE 中，此韌體顯示為 Rockbox 當您選擇設備型號時 Y1。指南、影片和發行說明也稱其為 Rockbox-Y1 或 Y1 的 Rockbox 因此很明顯，構建是針對 Y1 而不是 Y2。

安裝前請務必檢查播放機上列印的型號：Y1 和 Y2 韌體包不可互換。

## Rockbox-Y1 為您的 Y1 增加了什麼

Rockbox-Y1 是 Innioasis Y1 的開源 Rockbox 音樂播放器韌體的社群連接埠：
  - 基於標籤的音樂庫 — 使用音訊標籤按藝術家、專輯、類型和年份瀏覽，或直接瀏覽資料夾。
  - 高級音訊播放 — 無縫播放、交叉淡出、ReplayGain 和完整的均衡器。
  - 自訂主題 — 從數百個 240p 和 360p 社群主題中進行選擇，包括經典的 iPod 風格佈局。
  - 調頻收音機 — 內建 FM 收音機支援。
  - 選用附加功能 — 透過 Wi-Fi 和 Last.fm / ListenBrainz / Maloja 在支援的版本上進行播客下載。
  - 雙啟動 — 切換回工廠原始軟體，無需在支援的版本上重新刷新。

## 我應該選擇哪個 Y1 版本？
  - 240p 與 360p — 240p 使用經典 320×240 Rockbox 主題建構作品； 360p 建構使用更清晰的 480×360 Y1 主題。將構建分辨率與您要使用的主題相匹配（[240p 與 360p 指南](rockbox-y1/resolution.html)).
  - Type A 與 Type B — Type A 適用於出廠軟體 2.0.0 或更高版本的 Y1 播放器； Type B 適用於較早的 Y1 單元。選擇 Type A，除非您知道您的 Y1 是 Type B。
  - 穩定版與夜間版 — 選擇穩定的版本用於日常聆聽，或選擇夜間版本來測試最新的變更。

## 社群開發者直接下載

Innioasis 更新程式 CE 始終直接從社區韌體開發人員下載韌體套件（[rockbox-y1/rockbox](firmware_zh-TW.html?model=Y1&software=rockbox-y1)），開發者自己全權負責在 Updater CE 中列出他們的軟體版本。

您可以讓 Updater CE 自動下載並安裝固件，或從我們的網站下載 ROM 軟體包 [Rockbox-Y1下載頁面](rockbox-y1/download.html) 和 [Rockbox ROM 下載頁面](rockbox-rom-download_zh-TW.html).[Rockbox-Y1下載](rockbox-y1/download.html)[從本機 ZIP 安裝](rockbox-y1/portable-zip.html)

## 如何安裝Rockbox-Y1
  - 開啟 Innioasis 更新程式 CE 並設置 裝置型號 到 Y1.
  - 選擇 Rockbox 在 軟體.
  - 選擇一個穩定的版本（或啟用夜間建置來測試預覽）。
  - 點選 安裝 / 還原 所以Updater CE直接從開發者下載套件。
  - 當 Updater CE 提示您時，請完全關閉 Y1 電源並使用 USB 數據線連接它。
  - 等待完成訊息，然後斷開連接並打開播放器。

有關螢幕截圖和詳細設定提示，請閱讀 [完整的 Rockbox-Y1 教程](guides/rockbox-y1.html).

## 恢復原始Y1軟體

您可以隨時返回出廠軟體：選擇 Y1 和 原廠軟體 在 Updater CE 中，選擇一個穩定版本，然後按一下 安裝 / 還原。 MicroSD 卡片上的音樂將被保留。請參閱 [恢復指南](rockbox-y1/restore-stock.html) 和 [Y1 原始軟體頁面](original-software-y1_zh-TW.html).

## 常見問題Y1 的 Rockbox 與 Rockbox-Y1 相同嗎？

是的。 Rockbox、Rockbox-Y1、Rockbox 代表 Y1，以及 `rockbox-y1` 全部引用 Innioasis Y1 的同一社區 Rockbox 連接埠。Updater CE 從哪裡下載 Rockbox-Y1？

更新程式 CE 始終直接從社區韌體開發人員自己的版本下載韌體套件（`rockbox-y1/rockbox`）。開發人員全權負責在 Updater CE 中列出其軟體版本。我可以在 Y2 上安裝 Rockbox-Y1 嗎？

不會。 Y2 有自己獨立的韌體版本。使用 [Y2 的 Rockbox](rockbox-for-y2_zh-TW.html) 反而。安裝 Rockbox-Y1 會刪除我的音樂嗎？

不會。音樂儲存在 MicroSD 卡上，刷新播放器內部韌體時不會受到影響。

## 相關指南

### [Rockbox-Y1 輪轂](rockbox-y1/)

所有 Y1 指南：安裝、下載、主題、復原、雙重啟動和故障排除。

### [Rockbox-Y1 與 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 和 Y2 Rockbox 建構有何不同。

### [Rockbox-Y1 主題](rockbox-y1-themes.html)

如何使用 Updater CE 傳輸 240p 和 360p 主題。

### [Rockbox 概述](rockbox_zh-TW.html)

關於 Innioasis Y1 和 Y2 玩家的 Rockbox 簡介。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
