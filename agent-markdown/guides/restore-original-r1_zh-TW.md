---
title: "恢復 Innioasis R1 上的原始軟體 - 逐步"
description: "如何使用經過驗證的 rom_r1.zip 軟體包，使用 Innioasis 更新程式 CE 或 SP Flash Tool 在 Innioasis R1 上恢復官方原始軟體。"
language: "zh-TW"
source: "https://innioasis.app/guides/restore-original-r1_zh-TW.html"
---

# 恢復 Innioasis R1 上的原始軟體 - 逐步

恢復指南·InnioasisR1

# 恢復 Innioasis R1 上的原始軟體

完全回歸播放器附帶的軟體。在更新失敗後、出售播放器之前或自訂系統不適合您時使用它。[取得 Updater CE](../guide_zh-TW.html#platform)[R1下載](../firmware_zh-TW.html?model=R1)[R1 手冊](../manuals/r1.html)

適用於您的電腦的安裝指南

## 使用電腦復原 R1 上的原始軟體

選擇適合您正在使用的計算機的指南。 每個版本都有平台設定、Updater CE步驟和返回庫存的方式。[Windows 指南](/install/original-r1-windows.html)[macOS 指南](/install/original-r1-mac.html)[Linux指南](/install/original-r1-linux.html)

[所有 Innioasis R1 指南](/install/r1.html) · [所有原始軟體指南](/install/original-software.html)

## 你需要什麼
  - Windows、macOS 或 Linux 電腦。 Updater CE 在所有三個上運行。
  - 播放器隨附的USB線。僅充電電纜將不起作用。
  - 官方 `rom_r1.zip` 包，更新程式為您下載，或從 [R1 存檔](../firmware_zh-TW.html?model=R1) 如果您喜歡手動閃光。
  - 在播放器中充電。斷電恢復是使糟糕情況變得更糟的唯一常見方法。

這會替換系統並擦除內部儲存。 首先將音樂、錄音和照片複製到電腦上。

## 路線A：Updater CE（建議）
  - 安裝 [Innioasis 更新程式 CE](../guide_zh-TW.html#platform) 並打開它。
  - 套裝 裝置型號 到 R1。該模型必須與玩家完全匹配。
  - 選擇 原廠軟體 在軟體清單中。
  - 選擇一個版本。最新的穩定版本是安全的預設版本。
  - 新聞 安裝 / 還原 並等待包下載和解壓。
  - 完全關閉播放器電源，然後僅在更新程式要求時連接 USB 連接線。
  - 在出現成功訊息之前，請勿觸摸播放器或電纜。斷開連線並啟動播放器。
切勿選擇不同的模型來「使其發揮作用」。 R1 需要 R1 包。混合模型是玩家最終需要手動恢復的原因。

## 路線 B：SP Flash Tool（手動）

當電腦無法運作 Updater CE 時，或當您已經擁有該軟體包並且更喜歡經典工具時，請使用此選項。
  - 下載 `rom_r1.zip` 從 [R1 存檔](../firmware_zh-TW.html?model=R1) 並解壓縮它。
  - 將分散檔案保留在影像旁邊。請勿重新命名或移動影像。
  - 開啟SP Flash Tool，選擇 僅供下載，並載入分散文件。
  - 關閉播放器電源，按 下載，然後連接電纜。
  - 等待綠色成功標記後再斷開連線。

的 [SP Flash Tool 指南](../sp-flash-tool_zh-TW.html) 更詳細地介紹了驅動程式和 Windows 提示。在 Linux 和 macOS 上，Updater CE 是更簡單的路線，因為它帶來了自己的 USB 處理。

## 恢復後
  - 斷開播放器並讓它自行啟動。
  - 選擇您的語言並設定時鐘。
  - 如果您使用 Wi-Fi 或藍牙，請重新連接它們。
  - 將您的音樂複製回來。的 [轉乘指南](../manuals/transfer-music.html) 有資料夾名稱。

如果播放器啟動但螢幕、滾輪或按鈕仍出現故障，則恢復成功；這是硬體或設定問題，而不是軟體問題。的 [故障排除指南](../troubleshooting_zh-TW.html) 是下一站。

## 如果不起作用

### 更新者永遠看不到玩家

更換電纜，然後更換 USB 連接埠。避免樞紐。在 Windows 上，從下列位置安裝 MediaTek 驅動程式 [驅動程式頁面](../drivers_zh-TW.html).

### 閃光燈提前停止

重新連接，為播放器充電，然後重新開始。請勿切換至不同型號的封裝。

### 玩家保持黑色

充電一小時，然後維持電量十秒鐘。如果它仍然死了，請閱讀 [恢復指南](../guides/recovery_zh-TW.html) 再次嘗試之前。

## 人們提出的問題

### 這會刪除我的音樂嗎？

是的，內部儲存已被刪除。 microSD 卡上的文件通常會保留下來，但首先將它們複製到安全的地方。

### 之後我可以返回Rockbox嗎？

是的。恢復原始軟體不是一扇單向門；而是一扇單向門。您的型號的自訂軟體頁面可以再次安裝。

### 我需要 Type A / Type B 設定嗎？

只有 Y1 有這樣的選擇，並且僅限於原始軟體。所有其他型號都使用單一套件。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
