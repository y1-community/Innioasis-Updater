---
title: "Rockbox for Y2 (Rockbox-Y2)：概述、建置與安裝指南"
description: "Y2、Rockbox-Y2 的 Rockbox 和 rockbox-y2 參考 Innioasis Y2 的社區 Rockbox 韌體連接埠。了解它包含哪些內容以及如何使用 Innioasis Updater CE 安裝它。"
language: "zh-TW"
source: "https://innioasis.app/rockbox-for-y2_zh-TW.html"
---

# Rockbox for Y2 (Rockbox-Y2)：概述、建置與安裝指南

[← 韌體下載](firmware_zh-TW.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox 為 Y2 (Rockbox-Y2)

Rockbox-Y2（也稱為「Y2的Rockbox」）是Innioasis Y2的專用社群Rockbox韌體連接埠。它使用自己的 ROM 套件（`rom_y2.zip`）並透過 Innioasis 更新程式 CE 直接安裝。[安裝Rockbox-Y2](rockbox-y2/install.html)[下載ROM](rockbox-y2/download.html)[書面教程](guides/rockbox-y2.html)[Rockbox-Y2 輪轂](rockbox-y2/)

## 專為 Innioasis Y2 打造

在 Innioasis Updater CE 中，此韌體被列為 Rockbox 什麼時候 Y2 被選中。其版本由 [spycemagic/y2-rockbox](firmware_zh-TW.html?model=Y2&software=rockbox-y2) 帶有包名的項目 `rom_y2.zip`.

切勿在 Y2 上安裝 Y1 韌體包。選擇 Y2 Updater CE 中會自動將版本清單過濾為僅與 Y2 相容的版本。

## Rockbox-Y2 提供什麼
  - 基於標籤的音樂庫 — 從音訊檔案標籤瀏覽專輯、藝人和流派，或直接瀏覽資料夾。
  - 播放控制 — 無縫播放、交叉淡出、ReplayGain 和等化器設定。
  - 自訂主題 — 安裝與您的 Rockbox-Y2 版本相容的主題 ([Y2 主題指南](rockbox-y2-themes.html)).
  - 100%離線 — 無需帳戶或訂閱即可播放 MicroSD 卡中的本機檔案。
  - 輕鬆恢復原廠設置 — 在 Updater CE 中隨時回傳 Y2 原始軟體。

## 選擇 Rockbox-Y2 版本
  - 始終選擇 Y2 在 裝置型號 首先。
  - 除非您正在測試特定版本，否則請選擇最新版本。
  - 閱讀 [Rockbox-Y2 發行說明](release-notes/rockbox-y2/index_zh-TW.html) 查看每個版本中發生了什麼變化。

## 社群開發者直接下載

Innioasis 更新程式 CE 始終直接從社區韌體開發人員下載韌體套件（[spycemagic/y2-rockbox](firmware_zh-TW.html?model=Y2&software=rockbox-y2)），而這些開發人員全權負責在 Updater CE 中列出他們的軟體版本。

您可以讓Updater CE下載並刷新 `rom_y2.zip` 自動，或從我們的下載包 [Rockbox-Y2下載頁面](rockbox-y2/download.html) 和 [Rockbox ROM 下載頁面](rockbox-rom-download_zh-TW.html).[Rockbox-Y2下載](rockbox-y2/download.html)[從本機 ZIP 安裝](rockbox-y2/portable-zip.html)

## 如何安裝Rockbox-Y2
  - 開啟 Innioasis 更新程式 CE 並設置 裝置型號 到 Y2.
  - 選擇 Rockbox 在 軟體.
  - 從清單中選擇 Y2 版本。
  - 點選 安裝 / 還原 所以Updater CE直接從開發者下載套件。
  - 當更新程式 CE 要求時，請完全關閉 Y2 電源並使用 USB 資料線將其連接。
  - 等待完成訊息，然後拔下並開啟 Y2。

有關完整的逐步演練，請閱讀 [Rockbox-Y2教程](guides/rockbox-y2.html).

## 恢復原始Y2軟體

若要返回出廠固件，請選擇 Y2 和 原廠軟體 在 Updater CE 中，選擇一個穩定版本，然後按一下 安裝 / 還原。請參閱 [恢復指南](rockbox-y2/restore-stock.html) 和 [Y2 原始軟體頁面](original-software-y2_zh-TW.html).

## 常見問題Updater CE 從哪裡下載 Rockbox-Y2？

更新程式 CE 始終直接從社區韌體開發人員自己的版本下載韌體套件（`spycemagic/y2-rockbox`）。開發人員全權負責在 Updater CE 中列出其軟體版本。為什麼這個包被命名為rom_y2.zip？

開發人員命名 Y2 韌體存檔 `rom_y2.zip` 所以它不能與 Y1 混淆 `rom.zip`.Y1 主題適用於 Y2 嗎？

並非總是如此。檢查您的 Y2 版本的發行說明並查看 [Rockbox-Y2 主題指南](rockbox-y2-themes.html).

## 相關指南

### [Rockbox-Y2 輪轂](rockbox-y2/)

所有 Y2 指南：安裝、下載、主題、復原、雙重啟動和故障排除。

### [Rockbox-Y1 與 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 和 Y2 Rockbox 建構有何不同。

### [Rockbox-Y2 主題](rockbox-y2-themes.html)

在 Rockbox-Y2 上安裝和重設主題。

### [Y1 的 Rockbox](rockbox-for-y1_zh-TW.html)

Innioasis Y1 連接埠的概述和安裝指南。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
