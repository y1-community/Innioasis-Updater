---
title: "Innioasis 更新程式疑難排解 | Innioasis 與 Timmkoo 安裝問題 - Innioasis 更新程序"
description: "修正 Innioasis 更新程式安裝在任何 Innioasis 或 Timmkoo 播放器上的問題。檢查型號、電纜、驅動程式、關機時間以及安裝停止的位置 - 然後讓它再次閃爍。"
language: "zh-TW"
source: "https://innioasis.app/troubleshooting_zh-TW.html"
---

# Innioasis 更新程式疑難排解 | Innioasis 與 Timmkoo 安裝問題 - Innioasis 更新程序

疑難排解

# 找到安裝停止的點。

停在哪裡了？这会告诉您要修复什么。[返回正常引導](guide_zh-TW.html)[檢查韌體](firmware_zh-TW.html)

## 它在 USB 提示符號之前停止

這是計算機問題，而不是電纜問題。檢查您的型號。再次解壓縮文件。然後嘗試 安裝 / 還原。如果發布清單為空，則開啟 [韌體目錄](firmware_zh-TW.html).

## 無法連接到播放器
  - 完全關閉正確的 Y1 或 Y2 的電源。
  - 拔下電纜，關閉其他快閃記憶體或 Android 工具，然後重新開始安裝。
  - 僅當更新程式表示已準備就緒時才連線。
  - 如果可能，請直接在電腦中使用短的 USB 資料線，而不是集線器。
  - 在 Windows 上，重新安裝 MediaTek 驅動程式並重新啟動。在 Linux 上，檢查 USB/serial 權限。
更新程式連線提示即時更新程式提示對於目前型號和平台具有權威性。

## 偵測到播放器但閃光失敗

停在這裡。不要嘗試不同的模型。關閉其他工具，檢查您選擇了正確的Y1或Y2，如果播放器無法啟動，請使用相符的原始軟體。 [SP Flash Tool](sp-flash-tool_zh-TW.html) 和 MTKClient 如果您需要的話，它們也包含在內，並且文件位於 [韌體頁面](firmware_zh-TW.html).

## Windows 驅動程式註釋

由於核心隔離，某些 Windows 安裝會阻止 MediaTek 驅動程式。在更改記憶體完整性之前，請遵循當前的 Windows 安全指南，並在完成後將其重新開啟（如果系統允許）。[開啟司機指南](drivers_zh-TW.html)[清潔安裝指南](Troubleshooting/clean_install.html)

## 輪子不工作，或者播放器將無法啟動

輸入和電源故障需要採取與快閃記憶體故障不同的步驟。這些指南涵蓋了常見的 Y1 和 Y2 情況。[Y1滾輪](guides/y1-scroll-wheel-not-working.html)[Y2滾輪](guides/y2-scroll-wheel-not-working.html)[Y1打不開](guides/y1-wont-turn-on.html)[Y2打不開](guides/y2-wont-turn-on.html)[恢復指南](guides/recovery.html)

## 還卡住了嗎？

尋求協助時，請包含型號、作業系統、確切的更新程式訊息、是否偵測到播放器以及您選擇的套件/項目。不要發布私人令牌或無關的系統檔案。[求人](https://discord.gg/zHrT2zrcek)[支援維修](support_devs_zh-TW.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
