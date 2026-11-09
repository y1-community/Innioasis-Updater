---
title: "透過全新安裝修復 Innioasis 更新程式和 Y1 幫助程式 - Innioasis 更新程序"
description: "Innioasis 更新程式和 Y1 幫助程式的逐步全新安裝：刪除剩餘文件，重新安裝，然後返回刷新韌體。"
language: "zh-TW"
source: "https://innioasis.app/Troubleshooting/clean_install_zh-TW.html"
---

# 透過全新安裝修復 Innioasis 更新程式和 Y1 幫助程式 - Innioasis 更新程序

## 確認您需要全新安裝

當您看到以下任何症狀時，建議手動重新安裝：
  - 更新程序需要幾分鐘才能啟動，或在檢查更新時停止。
  - 即使存在較新的版本，也會停止更新。
  - 設備韌體更新無法下載或應用，即使它們可用。
  - 您跳過了多個版本並且已經很長時間沒有使用更新程式了。

## Windows：執行全新重新安裝

使用官方 Windows 安裝程式在 Windows 10 或 Windows 11（64 位元）上刷新更新程式。這完全取代了舊版本並恢復了自我更新通道。

在運行安裝程式之前，請打開 設定 › 應用程式 › 已安裝的應用程式 （或遺產 新增/刪除程序 面板）並卸載 Innioasis 更新程式的任何現有副本。乾淨啟動可以防止文件衝突。[ 下載適用於 Windows 的全新安裝程序 ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)步驟1

### 下載最新的安裝程序

將安裝程式儲存到您的下載資料夾中。如果 Innioasis 更新程式目前正在運行，請將其關閉。步驟2

### 刪除任何現有安裝

打開 設定 › 應用程式 › 已安裝的應用程式 （或遺產 控制面板 › 新增/移除程序）並解除安裝 Innioasis 更新程序，以便重新安裝從頭開始。步驟3

### 安裝並重新啟動

執行您下載的安裝程式 - Windows 將提示您授予權限。安裝完成後，啟動 Innioasis 更新程式；它現在應該會自動偵測 1.8.2.8 並再次取得更新。

 這也修復了啟動緩慢的問題，並讓更新程式再次直接從開發人員取得韌體版本。 

## macOS：使用 DMG 安裝程式進行刷新

macOS 安裝程式會清除舊檔案並安裝 1.8.2.8。[ 下載 Innioasis 更新程式 DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - 打開下載的 DMG 並展開 Finder 窗口，以便您可以看到 重新安裝 選項。
  - 執行重新安裝命令以刷新更新程式的現有副本。這會刪除可能阻止新功能的舊幫助程式檔案。
  - 從應用程式中再次啟動 Innioasis 更新程式。確認「關於」面板所列的版本 1.8.2.8.
 如果重新安裝後看到“Innioasis更新程式無法開啟”，請前往 系統設定 › 隱私與安全 並選擇 無論如何打開 批准該應用程式。 

## 更新到 1.8.2.8 後

一旦您使用最新版本，您就可以使用以下功能。這些僅適用於目前版本。
  - 一鍵安裝 適用於原始韌體、社群版本和直接從開發人員版本下載的 Rockbox 版本。
  - 清晰的引導步驟 告訴您何時連接播放器以及何時可以安全地拔掉插頭。
  - 兩個平台的整體穩定性得到改進，啟動時間也顯著縮短。

 需要協助驗證您的版本嗎？開啟Innioasis更新程序，選擇 幫助 › 關於，並確認建置顯示 1.8.2.8. 

## 仍需要幫助嗎？

如果全新安裝失敗，請擷取所有錯誤訊息並聯絡 Innioasis 社群支援管道。包括您的作業系統版本、更新程式版本（如果有）以及您已嘗試過的步驟。

保持安裝最新可確保您始終收到最新推出的韌體套件和工具。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
