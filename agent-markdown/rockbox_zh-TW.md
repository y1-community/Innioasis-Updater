---
title: "如何在 Innioasis Y1 或 Y2 - Innioasis 更新程式上安裝 Rockbox"
description: "使用更新程式在 Innioasis Y1 或 Y2 上安裝 Rockbox：主題、穩定版本、Type A 和 Type B 說明，以及如何在之後恢復原始軟體。"
language: "zh-TW"
source: "https://innioasis.app/rockbox_zh-TW.html"
---

# 如何在 Innioasis Y1 或 Y2 - Innioasis 更新程式上安裝 Rockbox

Rockbox參考

# 在您的 Y1 或 Y2 上獲得 Rockbox

Rockbox 更改了播放器軟體並開啟了更深層的音樂播放器介面、播放控制、排序和主題選項。安裝是引導式的，但 Y1 和 Y2 是不同的過程。[Y1 上的 Rockbox](guides/rockbox-y1.html)[Y2 上的 Rockbox](guides/rockbox-y2.html)[為什麼是Rockbox？](rockbox-benefits_zh-TW.html)

## 安裝發生了什麼變化

Rockbox 是客製化軟體。當匹配的原始軟體包可用時，它不會消除您返回庫存介面的能力。它可以改進音樂瀏覽和定制，但功能、解析度、電池壽命和主題相容性取決於構建。請勿混用型號。 為 Y1 玩家選擇 Y1，為 Y2 玩家選擇 Y2。看起來相似的版本名稱不足以證明軟體包是相容的。

## 觀看影片

影片由弗勞吉斯拍攝。它顯示了 Innioasis 更新程式路由；對於您的 Y1 或 Y2，請使用下面特定於型號的書面步驟。

影片由 [克里斯蒂安廣場](https://www.youtube.com/@CristianPlaza) （西班牙文），在 Y1 上顯示 Rockbox。請針對您的播放器使用以下特定於型號的步驟。

## 共享Updater路由
  - 安裝更新程式並在出現詢問之前不進行任何連接。
  - 選擇播放器上印有的型號 裝置型號.
  - 選擇 Rockbox 在 軟體.
  - 選擇穩定版本，除非您有意測試夜間建置。
  - 點選 安裝 / 還原，然後按照關閉電源和USB連接提示進行操作。
  - 僅在成功訊息後斷開連線。

## 240p、360p 和主題

較早的 Rockbox 主題合集可能以 240p 製作。 Y1 社群建構也使用 360p 相容性標籤。在選擇版本之前，請閱讀發行說明和主題來源。為一種解析度或軟體系列製作的主題可能不適用於另一種解析度或軟體系列。[瀏覽社群主題](https://themes.innioasis.app/?lang=zh-TW)[主題工具](https://themes.innioasis.app/?lang=zh-TW)

## 返回原始軟體

再次選擇相同型號，選擇 原廠軟體，選擇一個穩定的版本，並使用 安裝 / 還原。如果故障發生在 USB 提示之前，請檢查電腦和擷取的檔案。如果偵測到播放器但刷新失敗，請從 [故障排除](troubleshooting_zh-TW.html).[Y1恢復](guides/restore-original-y1.html)[Y2恢復](guides/restore-original-y2.html)

## 常見問題我重新安裝了 Rockbox，但沒有解決任何問題。

重新安裝 Rockbox 會在相同的檔案上寫入相同的版本，因此無法重設 Rockbox 保留在 MicroSD 上的內容。如果問題是卡片上的設定、主題、播放清單或資料庫損壞，重新安裝將無法清除它。可靠的重置是刪除 `.rockbox` MicroSD - Rockbox 中的資料夾會在下次啟動時建置一個新的資料夾。
  - 完全關閉播放器電源並取出 MicroSD 卡，或將播放器連接為 USB 驅動器。
  - 顯示電腦上的隱藏文件，以便該文件夾可見。 如何顯示隱藏文件在您的電腦上顯示點文件Windows: 在檔案總管中開啟 看法 選項卡並勾選 隱藏物品.macOS: 在 Finder 中按 Cmd+Shift+. 切換隱藏檔案。Linux·GNOME 檔案： 按 Ctrl+H，或開啟選單並選擇 顯示隱藏文件.Linux·KDE 海豚： 按 Ctrl+H，或使用 查看 → 顯示隱藏文件.
  - 刪除 `.rockbox` 卡根目錄中的資料夾。
  - 重新插入卡片並啟動播放器。 Rockbox 使用預設值重新建立資料夾。
  - 重新套用您的主題和設定。如果問題僅在特定主題之後出現，則該主題就是原因。

正在刪除 `.rockbox` 不會卸載 Rockbox，也不會影響您的音樂 — 該資料夾包含設定、主題和緩存，並且會自動重建。如果您想保留主題，請將資料夾複製到 `.rockbox` 刪除之前，或將資料夾重新命名為 `.rockbox-old` 首先。為什麼我在 MicroSD 上看不到 .rockbox 資料夾？

在大多數電腦上，名稱以點開頭的資料夾預設是隱藏的。您無需查看它即可安裝 Rockbox — 更新程式會處理這些檔案。如果您正在排除故障並想要刪除它，請先開啟隱藏檔案。 如何顯示隱藏文件在您的電腦上顯示點文件Windows: 在檔案總管中開啟 看法 選項卡並勾選 隱藏物品.macOS: 在 Finder 中按 Cmd+Shift+. 切換隱藏檔案。Linux·GNOME 檔案： 按 Ctrl+H，或開啟選單並選擇 顯示隱藏文件.Linux·KDE 海豚： 按 Ctrl+H，或使用 查看 → 顯示隱藏文件.刪除 .rockbox 會重置我的主題和設定嗎？

是的 - `.rockbox` 儲存 Rockbox 的設定、主題、播放清單和快取資料庫。刪除它會使 Rockbox 恢復到乾淨的預設狀態。備份整個資料夾（或將其重命名為 `.rockbox-old`）如果您可能想要恢復其中任何內容，請啟動播放器並 Rockbox 建立新資料夾。

## 更多 Rockbox-Y1 和 Rockbox-Y2 指南

探索在兩種型號上安裝、下載、主題化、恢復和故障排除的逐步指南 Rockbox：[Rockbox-Y1 輪轂](rockbox-y1/)[Rockbox-Y2 輪轂](rockbox-y2/)[Rockbox ROM 下載](rockbox-rom-download_zh-TW.html)[Y1 的 Rockbox](rockbox-for-y1_zh-TW.html)[Y2 的 Rockbox](rockbox-for-y2_zh-TW.html)[Rockbox-Y1 與 Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 主題](rockbox-y1-themes.html)[Rockbox-Y2 主題](rockbox-y2-themes.html)

## 這個參考有用嗎？

您的回答有助於改進本指南。是的還沒有[讓我們知道如何改進](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
