---
title: "SP Flash Tool 適合 Innioasis 和 Timmkoo 玩家"
description: "在 Windows 和 Linux 上找到與 Innioasis 更新程式捆綁在一起的 SP Flash Tool，提取 rom.zip 或 rom_y2.zip，並使用匹配的分散文件刷新 Innioasis Y1 或 Y2。"
language: "zh-TW"
source: "https://innioasis.app/sp-flash-tool_zh-TW.html"
---

# SP Flash Tool 適合 Innioasis 和 Timmkoo 玩家

手動閃光

# 適用於 Innioasis 和 Timmkoo 玩家的 Flash 工具

SP Flash Tool 包含在 Innioasis 更新程式中 [Windows](drivers_zh-TW.html#windows) 和 [Linux](drivers_zh-TW.html#linux)。你已經擁有了。本指南展示了在 Innioasis Y1 或 Y2 上使用它的安全方法，以及 Timmkoo 玩家的更新程式路線。[返回更新程序指南](guide_zh-TW.html)[韌體下載](firmware_zh-TW.html)[疑難排解](troubleshooting_zh-TW.html)

以 Innioasis Updater 開頭

## 更新程序一次完成整個工作

更新程式一次完成大部分安裝。選擇軟體，依照步驟操作，就完成了。它還會告訴您修復或新版本何時發布。 SP Flash Tool 位於更新程式工具包內，用於更新程式無法完成的極少數情況。以下步驟為例外。

## 這個工具的用途

更新程式會為您刷新播放器。 SP Flash Tool 是同一台發動機，但沒有護欄。當更新程式無法啟動、播放器無法連線或您了解分散檔案時，請使用它。首先嘗試更新程式。 對於大多數安裝和大多數恢復，引導 [更新者路線](guide_zh-TW.html) 是更安全的選擇。當您知道為什麼需要它時，請使用 SP Flash Tool，並準備好已充電的電池和 USB 數據線。

## 適合 Innioasis 玩家的 Flash 工具

Innioasis Updater 是 Innioasis 玩家的刷機工具。它透過模型匹配的流程安裝官方軟體、更新和恢復包，並保留您的音樂和設定。

### Innioasis Y1 快閃記憶體工具

在更新程式中選擇 Y1 版本，然後在應用程式詢問時連接已關閉的播放器。當您需要手動路由時，相同的 Y1 套件可與 SP Flash Tool 搭配使用。

### Innioasis Y2 快閃記憶體工具

選擇 Y2 列出的版本。 Y2 軟體包不能與 Y1 軟體包互換，因此在開始之前請檢查型號。

## 適合 Timmkoo 玩家的 Flash 工具

Timmkoo 玩家使用相同的更新程式安裝流程。它直接讀取 Timmkoo 的 ZIP 和 RAR 包，因此您不需要單獨的刷新工具或分散檔案。

### Timmkoo Q5 快閃記憶體工具

在Updater中選擇Q5型號，選擇Timmkoo包，然後執行Install / Restore並依照指示連接播放器。

### Timmkoo Q3 和 Q3E 快閃記憶體工具

Q3 條目同樣涵蓋了 Q3 和 Q3E。更新程式從專案發布的套件中選擇相符的檔案。

### Timmkoo A5 快閃記憶體工具

在選擇軟體包之前選擇 A5 型號，然後按照相同的安裝提示進行操作。

## 更新程式放置的位置

SP Flash Tool 隨更新程式安裝資料夾一起提供，而不是作為單獨下載。當您需要時從那裡打開它。

### Windows

打開更新程式安裝資料夾並執行 `flash_tool.exe`。該資料夾通常位於 `%LOCALAPPDATA%\Innioasis Updater`。某些設定中包含帶有 SP Flash Tool 捷徑的 Toolkit 資料夾。

### Linux

運行捆綁的 `flash_tool` x86 / x86_64 上的 Updater 應用程式資料夾中的二進位。專案安裝程式使用 udev 規則準備 USB 權限，因此連線時應該會出現播放器。

### macOS

SP Flash Tool 未捆綁在 macOS 上。更新程式使用 MTKClient 路線代替。使用 [引導安裝](guide_zh-TW.html) 在 Mac 上，並在 Windows 或 Linux 電腦上保留 SP Flash Tool。

此工具附帶 MediaTek 下載代理程式和特定於模型的配置，因此您無需從其他地方收集 DA 或分散文件。

## 準備韌體
  - 取得您想要的版本 [韌體下載](firmware_zh-TW.html)。選擇 `rom.zip` 對於 Y1 或 `rom_y2.zip` 對於 Y2。
  - 將 ZIP 解壓縮到自己的資料夾中。 Windows 可以使用全部提取。在 Linux 上，使用存檔管理器或 `unzip` 在終端中。
  - 檢查分散檔案是否位於提取的資料夾中。它通常被命名為 `MT6572_Android_scatter.txt` 對於 Y1 包和 `MT6582_Android_scatter_def.txt` 對於 Y2 包，儘管發行版可能以其項目命名。
將模型分開。 Y1 散點描述了 MT6572 設備，Y2 散點描述了 MT6582 設備。刷錯了就會導致玩家變磚。如果 ZIP 內的分散與您的型號不匹配，請停止並使用為您的型號列出的軟體包。

## 載入散射和閃光
  - 從更新程式安裝資料夾中開啟 SP Flash Tool。
  - 在下載標籤中，按一下 選擇 旁邊的分散式載入文件，然後從提取的資料夾中選擇分散文件。分區清單將被填入。
  - 保持閃光燈模式開啟 僅供下載 除非你有意進行完全恢復，這需要 韌體升級.
  - 點選 下載。该工具将等待玩家。
  - 完全關閉播放器電源，然後連接 USB 數據線。將播放器放下，不要移動它。
  - 等待綠色複選標記。然後斷開電纜並啟動播放器。

保持與引導路線相同的 USB 電纜和計時規則：資料電纜，無集線器，並且僅在工具準備就緒時進行連接。

## 如果不閃爍
  - 檢查分散圖和 ZIP 是否與播放器上列印的型號相符。
  - 連接前請確認播放器已完全斷電。
  - 在 Windows 上，確認透過更新程式安裝安裝了 MediaTek 驅動程式；在 Linux 上，從專案安裝程式確認 udev 規則。
  - 僅當工具等待時才重新連接電纜。港口比賽可能需要完全拔掉插頭並重新進行 下載 點擊。

對於除此之外的任何事情，請打開 [故障排除](troubleshooting_zh-TW.html)。请记住：更新程序仍然是正常途径，并且 [Y1](guides/restore-original-y1.html) 和 [Y2](guides/restore-original-y2.html) 恢復指南也使用它。

## 這有用嗎？

您的回答有助於改進本指南。是的，我發現它很有用還沒有[讓我們知道如何改進](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
