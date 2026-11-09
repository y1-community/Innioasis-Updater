---
title: "Reborn (Y2Linux) - Innioasis 更新程式的 Wi-Fi、藍牙和 FM 收音機設置"
description: "Innioasis Y2 上的 Reborn (Y2Linux / Y2Reborn) 的簡短安裝後指南：複製 system.img，然後設定 Wi-Fi、藍牙和 FM 收音機。"
language: "zh-tw"
source: "https://innioasis.app/y2reborn_wifibt_zh-tw.html"
---

# Reborn (Y2Linux) - Innioasis 更新程式的 Wi-Fi、藍牙和 FM 收音機設置

Innioasis Y2 · Reborn 安裝後

# 設定 Wi-Fi、藍牙和 FM 收音機。

將一個檔案複製到您的播放器。 Reborn 處理剩下的事情。[下載系統.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[安裝指南](guides/reborn-y2linux-y2.html)[為什麼是Y2Reborn？](reborn-y2linux-benefits_zh-TW.html)

## 為什麼是這個文件？

Wi-Fi、藍牙和 FM 收音機需要五個 MediaTek 韌體模組，Reborn 無法出貨。他們在官方內部 Y2 `system.img`。 Reborn 提取它們一次，檢查它們，然後刪除檔案。

## 設定
  - 下載系統.img

下載v3.2.0 FM `system.img` 到您的計算機。[ 下載系統.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - 啟動 Reborn 一次

打開播放器。等待 設定儲存 完成，然後重新啟動一次。
  - 連接到您的計算機

使用 USB 數據線。播放器顯示為 內部儲存.在 Mac 上？

安裝 [開放MTP](https://openmtp.ganeshrvel.com/) 瀏覽播放器。 Windows 和 Linux 會自動掛載它。
  - 將 system.img 複製到韌體

建立一個名為的資料夾 `Firmware` 在內部儲存的根目錄下。複製 `system.img` 進入其中。
  - 等待設定完成

Reborn 自動安裝無線電韌體並刪除 `system.img`。這大約需要 10-20 秒。等待 Wi-Fi 和藍牙已準備就緒.
  - 連接 Wi-Fi、藍牙和 FM 收音機
    - 無線上網： 設定→系統→網路→Wi-Fi。選擇您的 2.4 GHz 網路。
    - 藍牙： 將耳機置於配對模式。設定 → 藍牙 → 選擇它們。
    - 調頻收音機： 插入有線耳機作為天線，然後開啟 FM 收音機。

  - 透過 Wi-Fi 更新

未來的 Reborn 更新從設定 → 系統 → 軟體更新安裝。您的無線電韌體保持不變。

## 本指南有幫助嗎？

您覺得這個安裝後設定指南有幫助嗎？ 是的，有幫助！ [ 需要有關 Discord 的幫助 ](https://discord.gg/zHrT2zrcek) 感謝您的回饋！在 Y2Reborn 上享受無線聆聽。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
