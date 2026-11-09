---
title: "Rockbox-Y1 主題：使用 Updater CE 傳輸主題、240p 與 360p 並套用主題"
description: "如何使用 Updater CE 將主題傳輸到 Innioasis Y1（可用時自動推送，或在 macOS 和 Linux 上 MTKClient 刷新後引導逐步傳輸），以及 240p 與 360p 相容性和應用主題。"
language: "zh-TW"
source: "https://innioasis.app/rockbox-y1-themes_zh-TW.html"
---

# Rockbox-Y1 主題：使用 Updater CE 傳輸主題、240p 與 360p 並套用主題

[← Rockbox-Y1 中心](rockbox-y1/)

Rockbox-Y1 · 主題與更新程式 CE

# Rockbox-Y1 主題：使用 Updater CE 傳輸，選擇構建，然後選擇外觀

更新程式 CE 會為您處理 Rockbox-Y1 主題和字型 - 只要有可能，就會自動將它們傳輸到 Y1，並在無法無人值守的情況下逐步指導您完成傳輸（例如，在 macOS 或 Linux 上安裝 MTKClient 韌體後）。[取得 Rockbox 和更新程式 CE](guides/rockbox-y1.html)[瀏覽社群主題](https://themes.innioasis.app/)[240p 與 360p](rockbox-y1/resolution.html)

## 使用 Updater CE 將主題傳輸到 Y1

Rockbox 將其韌體儲存在 Y1 的內部快閃記憶體中，而主題、字體和使用者設定則儲存在隱藏的快閃記憶體中 `.rockbox` 播放器記憶體（MicroSD 卡）上的資料夾。因為刷新 ROM 和將文件複製到存儲使用兩個不同的連接， 更新程式 CE 自動適應您的作業系統和安裝方法：
  - 當Updater CE可以到達玩家時自動傳輸： 當您安裝 360p Rockbox-Y1 版本（或在「設定」中啟用自動主題同步）時，Updater CE 會在背景下載並合併精選的 360p 主題和字型套件。一旦 Y1 可以到達 亞洲開發銀行 （Android 調試橋）或安裝為 USB驅動器 與一個 `.rockbox` 資料夾中，Updater CE 會將主題和字體直接推送到播放器，無需手動解壓縮。
  - 當無法在無人值守的情況下進行引導式逐步傳輸（例如 macOS 和 Linux 上的 MTKClient）： 當您使用 Rockbox 閃爍時 MTKClient 在 macOS 或 Linux 上安裝方法時，當 Y1 在低階預載器/BROM 模式下關閉電源時，會發生刷新 — 在 Rockbox 首次啟動以建立之前 `.rockbox` 並且在將播放器的儲存安裝到您的電腦上之前。每當 Updater CE 在刷新期間無法在無人值守的情況下完成傳輸時，它會自動打開 安裝後主題和字型助手 並引導您完成它： 
    - 首先啟動 Rockbox： 如果需要，更新程式 CE 會提示您斷開 USB 電纜並開啟 Y1 電源，以便 Rockbox 啟動一次並初始化 `.rockbox` 卡片上的資料夾。
    - 透過 USB 重新連接： 將 Y1 插回您的 Mac 或 Linux PC。如果 ADB 可用，Updater CE 會偵測啟動的播放器並自動推送主題和字體包。
    - 或使用 USB 儲存模式和引導資料夾選擇器： 如果 ADB 未啟動或您喜歡直接儲存傳輸，Updater CE 會引導您進入 Y1 上的 USB 儲存模式，按一下 選擇 .rockbox 資料夾，顯示隱藏資料夾（Cmd+Shift+. 在 macOS 檔案對話方塊中或 Ctrl+H 在 Linux 上），然後選擇 `.rockbox` 在 Y1 磁碟機上 — 然後 Updater CE 會將所有主題和字體合併到位。

  - 按需隨時新增或刷新主題： 您可以隨時運行相同的自動或引導傳輸，而無需重新刷新韌體 - 打開 Updater CE 並選擇 設定 → 安裝 Rockbox 360p 主題 (Cmd+T 在 macOS 上， Ctrl+T 在 Windows 和 Linux 上），或拖曳單一主題 `.zip` 打包到 Updater CE 上 智慧投放 窗戶。

## 240p、360p，以及為何標籤位於機身上

Y1 社群版本發佈時有解析度標籤，主題集合也有相同的標籤。 240p 版本與較舊的主題包具有最廣泛的兼容性； 360p 版本是為較新的 Y1 主題路徑製作的。安裝一個並應用另一個並不危險——它只是看起來不對，有剪切的文本、丟失的元素或無法閱讀的介面。

如果您還沒有主題首選項，請採用較新的穩定版本及其預設主題，然後選擇與其標籤相符的主題。這 [解析度頁](rockbox-y1/resolution.html) 更深入；經驗法則很簡單：建立標籤和主題標籤必須一致。

## 主題所在

主題是 MicroSD 卡上的文件，位於 `.rockbox` 資料夾 — 儲存設定和快取的相同資料夾。韌體本身位於內部快閃記憶體上，因此新增、變更或刪除主題不需要重新刷新。
  - 將主題自己的資料夾複製到 `.rockbox/themes` 在卡片上。
  - 然後在播放器的主題設定中選擇它並重新啟動以查看它是否已應用。
  - 在更新版本之前保留您喜歡的主題的副本 - 它是一個文件，而不是安裝。

如果看不到資料夾，請先開啟隱藏檔案：macOS Cmd+Shift+.、Windows 檢視 → 隱藏項目、Linux Ctrl+H.

## 按順序應用主題
  - 首先安裝並啟動Rockbox-Y1；主題需要運行建置。
  - 將主題資料夾複製到 `.rockbox/themes` 在卡片上。
  - 開啟主題設定並選擇主題。
  - 重新啟動，以便整個介面（而不僅僅是選單）都能拾取它。
  - 如果它看起來壞了，請選擇另一個主題；如果您想稍後重試，這些文件仍然存在。

## 撤銷破壞介面的主題

如果播放器啟動後出現無法使用的情況，您無需重新安裝韌體。重新命名或刪除 `.rockbox` 卡上的資料夾並啟動播放器：建置使用預設設定和預設主題重新建立資料夾。您的音樂不會受到影響，您可以稍後將您想要的主題複製回來。[.rockbox 資料夾](rockbox-y1/sd-card.html)[第一次開始](rockbox-y1/first-start.html)[更新建置](rockbox-y1/update.html)

## 人們提出的問題為什麼 Updater CE 在 macOS 或 Linux 上安裝 MTKClient 後會引導我傳輸主題？

當您的 Y1 在低階預載器/BROM 模式下斷電時，Rockbox 啟動以初始化之前，MTKClient 將 Rockbox ROM 閃存到內部記憶體 `.rockbox` 資料夾並在 MicroSD 卡安裝到您的電腦之前。只要 Updater CE 可以直接到達啟動的播放器（透過 ADB 或安裝的 USB 驅動器），它就會自動傳輸主題；如果在刷新過程中無法在無人值守的情況下執行此操作，它會在刷新後立即打開引導主題和字體步驟，以幫助您打開 Y1 電源並透過 ADB 或 SDBUSB 儲存模式。Y2 主題適用於 Y1 嗎？

不。連接埠是獨立的，Y2 上的主題支援遵循其測試版本。看 [Rockbox-Y2 主題](rockbox-y2-themes_zh-TW.html).主題在更新後還能繼續存在嗎？

通常是的，因為它們位於卡上並且閃存寫入 ROM。如果新版本變更了主題路徑，請重新套用與其標籤相符的主題。為什麼主題只應用了一半？

重新啟動通常可以解決該問題。如果不是，主題的文件不完整 - 重新複製其資料夾而不是編輯單一文件。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
