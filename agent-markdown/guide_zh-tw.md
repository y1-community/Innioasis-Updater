---
title: "開始使用 Innioasis 更新程式 CE |在任何 Innioasis 或 Timmkoo 播放器上安裝或恢復韌體 - Innioasis 更新程序"
description: "下載適用於 Windows、macOS 或 Linux 的 Innioasis 更新程式 CE，然後按照幾個指導步驟在任何 Innioasis 或 Timmkoo 播放器上安裝或恢復韌體。"
language: "zh-tw"
source: "https://innioasis.app/guide_zh-tw.html"
---

# 開始使用 Innioasis 更新程式 CE |在任何 Innioasis 或 Timmkoo 播放器上安裝或恢復韌體 - Innioasis 更新程序

快速啟動

# Innioasis 更新程式 CE 入門

適用於所有 Innioasis 和 Timmkoo 音訊播放器。在您的電腦上安裝 Innioasis Updater CE，選擇您的型號和所需的軟體，然後按照提示進行操作。

## 

[取得 Updater CE](guide_zh-TW.html#download-updater)[完整的書面教程](guide_zh-TW.html)

## 取得 Innioasis Updater CE

Innioasis Updater 行政長官 是在您的播放器上安裝官方更新和社群軟體的應用程式。它會保留您的音樂和設置，並且可以在 Windows、macOS 和 Linux 上運行。

### Windows

下載安裝程序，運行它，然後在完成後重新啟動您的電腦。[取得驅動程式](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[下載Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

如果 Windows 阻止您執行該應用程式或無法啟動該應用程序，請開啟“設定”，按一下“隱私和安全性”→“Windows 安全性”→“應用程式和瀏覽器控制”，然後關閉“智慧型應用程式控制”。智慧型應用程式控制目前影響流行的應用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的並且經過驗證可以使用。 [Windows 無法啟動該應用程式？幫助](#smart-app-control)

安裝後重新啟動您的電腦。驅動程式幫助位於 [Windows 設定說明](drivers_zh-TW.html#windows).

### macOS[下載Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

如果您的 Mac 首次執行該應用程式時將其阻止，請打開「系統設定」，點擊「隱私與安全性」，向下滾動至「安全性」，然後點擊 [無論如何打開](https://support.apple.com/en-gb/102445#openanyway)。您也可以在訪達（Finder）中按住 Control 鍵點按（或右鍵點按）該應用程式並選擇「打開」。

適用於搭載 macOS Monterey 及更高版本的 Intel 和 Apple Silicon Mac。

### Linux

下載適用於 Intel 和 AMD 系統的 AppImage，使其可執行並運行它。[下載適用於 Intel/AMD 的 AppImage](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Linux 設定注意事項](drivers_zh-TW.html#linux)另一個平台？

您需要您的播放器、一條可傳輸資料的 USB 數據線（無法安裝只能充電的數據線）以及幾分鐘的時間。保持電纜連接，直到更新程序 CE 表示已完成。

## 選擇您的型號和軟體
  - 設備型號： 選擇播放器上印有的型號， Y1 或 Y2。為一種型號製作的軟體無法安裝在另一種型號上。
  - 軟體及發布： 當列出您的型號時，請選擇原始軟體、Rockbox、Solar、JJ Launcher、Inniclassic、Y2Player 或 Koensayr，然後選擇一個版本。穩定是安全的選擇。
  - 安裝： 點選 安裝 / 還原，完全關閉播放器電源，僅在更新程式 CE 要求時連接 USB 電纜。
  - 結束： 將播放器和電纜放在一邊，直到出現成功訊息，然後斷開連接並啟動播放器。

Y1 2.0.0 之前附帶原始軟體的玩家需要 設備 Type B。其他人都保留預設值 Type A。用於連接已關閉播放器的更新程式連線說明請按照適用於您的型號的即時 Updater CE 提示進行操作。

## 返回原始軟體

客製化軟體是可逆的。在 Updater CE 中，選擇您的型號，然後選擇 原廠軟體，選擇一個穩定版本，然後運行 安裝 / 還原 同樣的方式。沒有什麼可以手動刪除的。[Y1恢復指南](guides/restore-original-y1.html)[Y2恢復指南](guides/restore-original-y2.html)

如果閃光在 USB 提示之前停止，請先檢查電纜、平台設定和型號。看 [故障排除](troubleshooting_zh-TW.html) 對於修復， [Y1 和 Y2 恢復指南](guides/recovery.html) 對於動力和車輪故障，以及 [SP Flash Tool](sp-flash-tool_zh-TW.html) 用於高級復健。

## 按型號劃分的軟體指南

開啟適合您的型號和您選擇的軟體的指南。

### Innioasis Y1

Y1 的軟體：

### Innioasis Y2

Y2 的軟體：

## 我該使用哪個工具？

本指南使用 Innioasis 更新程式 2.5.1，也稱為更新程式 CE。它可以確保您的歌曲、影片和藍牙配對的安全。它會告訴您更新何時準備就緒。 Innioasis Universal Flash Tool 會擦除您的播放器並需要手動步驟。 [比較工具 →](updater-comparison_zh-TW.html)

## Windows 無法啟動該應用程式？智慧型應用程式控制解決方法

Windows Defender SmartScreen 或智慧型應用程式控制可以在簽署信譽傳播之前阻止新下載的社群應用程式。智慧型應用程式控制目前正在影響流行的應用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的並且經過驗證可以使用。關閉智慧型應用程式控制允許 Updater CE 正常開啟和運作。
  - 打開 設定 在您的 Windows PC 上（按 Win + I).
  - 點選 隱私與安全 ，然後按一下左側邊欄中的 Windows Security.
  - 點選 應用程式和瀏覽器控制.
  - 在下面 智慧應用程式控制， 點選 智慧應用程式控制設定.
  - 將切換開關設定為 離開 以允許 Updater CE 啟動。

透過 Edge 下載？ 如果 Edge 本身阻止下載，請按一下「更多選項」按鈕 (…) → 保持 → 顯示更多 → 無論如何都要保留.

稍後重新啟用智慧型應用程式控制： 當您想要重新開啟智慧型應用程式控制時，您可以透過 Windows 註冊表重新啟用它 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 透過設定 `VerifiedAndReputablePolicyState` 到 `1` （開）或 `2` （評估模式）並重新啟動。

### Windows 無法啟動該應用程式？如何關閉智慧應用程式控制

Windows Defender SmartScreen 或智慧型應用程式控制可以在簽署信譽傳播之前阻止新下載的社群應用程式。智慧型應用程式控制目前正在影響流行的應用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的並且經過驗證可以使用。關閉智慧型應用程式控制允許 Updater CE 正常開啟和運作。
  - 打開 設定 在您的 Windows PC 上（按 Win + I).
  - 點選 隱私與安全 ，然後按一下左側邊欄中的 Windows Security.
  - 點選 應用程式和瀏覽器控制.
  - 在下面 智慧應用程式控制， 點選 智慧應用程式控制設定.
  - 將切換開關設定為 離開 以允許 Updater CE 啟動。

被邊緣阻止？ 如果 Microsoft Edge 本身阻止下載，請按一下「更多選項」按鈕 (…) → 保持 → 顯示更多 → 無論如何都要保留.

稍後重新啟用智慧型應用程式控制： 當您想要重新開啟智慧型應用程式控制時，您可以透過 Windows 註冊表重新啟用它 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 透過設定 `VerifiedAndReputablePolicyState` 到 `1` （開）或 `2` （評估模式）並重新啟動。關閉幫助

## 這有用嗎？

您的回答有助於改進本指南。是的，我發現它很有用還沒有[讓我們知道如何改進](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
