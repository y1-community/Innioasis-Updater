---
title: "韌體安裝和庫存恢復指南| Innioasis 更新程式 CE - Innioasis 韌體下載"
description: "使用 Innioasis 更新程式 CE 在 Innioasis Y1、Y2、G1、G3、G5、R1、PR1 和 Timmkoo Q5、Q3 上安裝自訂韌體或恢復官方原廠韌體。"
language: "zh-TW"
source: "https://innioasis.app/firmware-guide_zh-TW.html"
---

# 韌體安裝和庫存恢復指南| Innioasis 更新程式 CE - Innioasis 韌體下載

韌體安裝和庫存恢復指南

# 在您的裝置上安裝或恢復韌體

選擇播放器上印有的型號。然後按照 Updater CE 中的步驟進行操作。它處理其餘的事情。[取得 Updater CE](guide_zh-TW.html#platform)[瀏覽韌體存檔](firmware_zh-TW.html)[疑難排解](troubleshooting_zh-TW.html)

選擇播放器上印有的型號和所需的軟體，然後開啟本指南。 [依型號瀏覽軟體和庫存固件](firmware_zh-TW.html).

## 

[取得 Updater CE](guide_zh-TW.html#download-updater)[完整的書面教程](guide_zh-TW.html)

## 取得 Innioasis Updater CE

如果您尚未獲得 Updater CE，請從這裡開始。在 Updater CE 上獲取帶引導安裝

### Windows

下載安裝程序，打開它，然後按照安裝提示進行操作。[下載並安裝驅動程式](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[下載應用程式和驅動程式](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[被邊緣阻止？](#)

如果 Windows 阻止您執行該應用程式或無法啟動該應用程序，請開啟“設定”，按一下“隱私和安全性”→“Windows 安全性”→“應用程式和瀏覽器控制”，然後關閉“智慧型應用程式控制”。 [Windows 無法啟動該應用程式？幫助](#smart-app-control)

安裝後您需要重新啟動電腦才能使其正常運作。

### macOS

下載應用程式並將其移至應用程式。如果 macOS 封鎖它，請開啟“系統設定”，然後開啟“隱私權和安全性”，然後按一下“仍然開啟”。 [這是如何運作的](https://support.apple.com/en-gb/102445#openanyway)[下載Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

下載適用於 Intel 和 AMD 系統的 AppImage，使其可執行並運行它。[下載適用於 Intel/AMD 的 AppImage](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linux 設定注意事項](drivers_zh-TW.html#linux)另一個平台？

需要更長的計算機設定說明嗎？打開 [Windows](drivers_zh-TW.html#windows) 或 [Linux](drivers_zh-TW.html#linux) 設定指南。

## 返回原始軟體

要返回，請選擇您的型號，然後選擇 原廠軟體，然後運行 安裝 / 還原。僅此而已。更新程式為您更換系統軟體。[Y1恢復指南](guides/restore-original-y1.html)[Y2恢復指南](guides/restore-original-y2.html)

## 按型號劃分的軟體指南

選擇您的型號，然後開啟您的軟體指南。

### Innioasis Y1

Y1 的軟體：

### Innioasis Y2

Y2 的軟體：

關於這兩個工具的說明

## 我該使用哪個工具？

Innioasis Updater 行政長官 是更新播放器最安全的方法。它可以保存您的音樂、影片和藍牙配對。它會告訴您更新何時準備就緒。它可以在 Windows、macOS 和 Linux 上運行。 Innioasis Universal Flash Tool 會擦除您的播放器並在更少的電腦上運行。[開啟完整比較](updater-comparison_zh-TW.html)

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
