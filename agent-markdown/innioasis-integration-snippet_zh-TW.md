---
title: "嵌入 Innioasis 更新程式安裝指南 - Innioasis 更新程序"
description: "將 Innioasis 更新程式安裝指南新增至另一個具有響應式 iframe 嵌入和複製就緒範例的網站。"
language: "zh-TW"
source: "https://innioasis.app/innioasis-integration-snippet_zh-TW.html"
---

# 嵌入 Innioasis 更新程式安裝指南 - Innioasis 更新程序

# 🚀 Innioasis 更新程式 - 可嵌入安裝指南

這是一個完整的、可嵌入的安裝指南小部件，可以輕鬆整合到任何網站中。它具有一個很酷的右下角彈出式 CTA，可以為 Windows、macOS 和 Linux 用戶打開全面的安裝指南。

### 🎨 美麗的設計

現代、響應式設計，適用於所有支援深色模式的設備

### 📱 跨平台

適用於 Windows、macOS 和 Linux 的完整安裝指南以及逐步說明

### 🔧 輕鬆集成

只需複製並貼上程式碼片段 - 無需依賴項或複雜的設置

### 💾 智慧存儲

記住用戶是否關閉了橫幅以避免打擾

## 📋 整合說明

要將 Innioasis 更新程式安裝指南新增至您的網站，只需將此程式碼片段複製並貼上到您的 HTML 中： <!-- Innioasis 更新程式安裝指南小工具 --> <script> (function() { // 建立並註入小工具 const script = document.createElement('script'); script.src = 'https://your-domain.com/innioasis-embed.html'; script.async = true './innoasis-embed.html'; document.head.appendChild(script); // 建立 iframe 容器 const iframe = document.createElement('iframe'); iframe.style.cssText = ` 位置: 20px; 寬度: 400px; iframe.onload = function() { iframe.style.pointerEvents = 'auto'; }; </脚本> 📋複製整合程式碼

## 🎯替代方案：直接嵌入方法

為了更簡單的集成，您可以使用 iframe 直接嵌入小部件： <!-- Direct iframe embed --> <iframe src="https://your-domain.com/innioasis-embed.html" width="400" height="200" frameborder="0" style="position: fixed; bottom: 20px; right: 20px; z-index: 999999; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);" allowtransparency="true"> </iframe> 📋 複製 iframe 程式碼

## 🔧 自訂選項

您可以透過修改以下參數來自訂小工具： // 自訂 CTA 橫幅 window.InnioasisUpdater = { // 更改橫幅文字 ctaTitle: "🚀 Get Innioasis Updater", ctaDescription: "下載適合您平台的桌面應用程式", ctaButtonText: "Get Started", // 更改位置position: "-right-top "left"自動顯示延遲（以毫秒為單位） showDelay: 3000, // 3 秒後顯示 // 自訂樣式 customCSS: ` .cta-banner { background: Linear-gradient(135deg, #your-color1, #your-color2); } ` }; 

## 📱 演示

點擊下面的按鈕查看正在運行的小部件：🎯 顯示演示小部件

## 📚 包含的功能
  - 智慧 CTA 橫幅： 以流暢的動畫顯示在右下角
  - 平台檢測： 自動偵測使用者的作業系統
  - 逐步指南： 適用於 Windows、macOS 和 Linux 的完整安裝說明
  - 進度追蹤： 多步驟安裝的可視進度條
  - 下載整合： 所有必需文件的直接下載鏈接
  - 響應式設計： 在桌上型電腦、平板電腦和行動裝置上完美運行
  - 深色模式支援： 自動適應使用者的系統偏好
  - 用戶偏好： 記住用戶是否關閉了橫幅
  - 輔助功能： 鍵盤導航和螢幕閱讀器友好

## 🌐 託管要求

要在您的網站上使用此小部件，您需要：
  - 上傳 `innioasis-embed.html` 檔案到您的網頁伺服器
  - 更新整合程式碼段中的 URL 以指向您的伺服器
  - 確保您的伺服器支援 HTTPS（現代瀏覽器必要）
  - 在您的網站上測試小部件以確保其正常工作

## 🆘 支持

如果您需要整合此小部件的協助或有疑問，請：
  - 檢查瀏覽器控制台是否有任何錯誤訊息
  - 確保所有檔案都正確上傳到您的伺服器
  - 驗證整合程式碼中的 URL 是否正確
  - 在不同瀏覽器和裝置上測試

 由 Innioasis 團隊使用 ❤️ 製作

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
