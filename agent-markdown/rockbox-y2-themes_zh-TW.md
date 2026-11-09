---
title: "Rockbox-Y2 主題：在 Y2 上安裝並重設主題"
description: "如何在 Innioasis Y2 上安裝、管理和重置 Rockbox-Y2 主題：主題位於 .rockbox 資料夾中的位置以及如何檢查建置相容性。"
language: "zh-TW"
source: "https://innioasis.app/rockbox-y2-themes_zh-TW.html"
---

# Rockbox-Y2 主題：在 Y2 上安裝並重設主題

[← Rockbox-Y2 中心](rockbox-y2/)

Rockbox-Y2 · 主題

# Rockbox-Y2 主題

如何在 Rockbox-Y2 上安裝主題，檢查主題與已安裝版本的兼容性，並在主題無法正常顯示時重設主題。[Rockbox-Y2 發行說明](release-notes/rockbox-y2/index.html)[瀏覽社群主題](https://themes.innioasis.app/)[安裝Rockbox-Y2](rockbox-y2/install.html)

## 檢查您的建置的主題相容性

Rockbox-Y2 與 Y1 連接埠分開開發，因此主題相容性遵循您安裝的 Y2 建置版本。檢查 [Rockbox-Y2 發行說明](release-notes/rockbox-y2/index.html) 在安裝主題包之前先選擇您的版本。

看 [Rockbox-Y1 與 Rockbox-Y2](rockbox-y1-vs-y2_zh-TW.html) 對兩個連接埠進行全面比較。

## 如何在 Y2 上安裝主題

主題儲存在隱藏的 MicroSD 卡上 `.rockbox` 資料夾。
  - 至少啟動 Rockbox-Y2 一次，以便創建 `.rockbox` 您的 MicroSD 卡上的資料夾。
  - 將主題文件提取或複製到 `.rockbox/` （所以 `themes`, `wps`, `fonts`, 和 `backdrops` 合併到 `.rockbox/`).
  - 在播放器上，打開 設定 → 主題設定 → 瀏覽主題文件 並選擇您的主題。

若要查看電腦上的隱藏資料夾：按 Cmd+Shift+. 在 macOS 上，啟用 看 → 隱藏項目 在 Windows 上，或按 Ctrl+H 在 Linux 上。

## 如何重置損壞的主題

如果主題使螢幕難以閱讀，請重新命名或刪除該主題 `.rockbox` 您的 MicroSD 卡上的資料夾並重新啟動播放器。 Rockbox-Y2將創造一個新的 `.rockbox` 具有預設主題的資料夾，同時保持音樂完好無損。[.rockbox 資料夾](rockbox-y2/sd-card.html)[正在更新 Rockbox-Y2](rockbox-y2/update.html)[Rockbox-Y2 建構註釋](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
