---
title: "Innioasis Y2 更新後滾輪不工作 | Innioasis 韌體存檔 - Innioasis 韌體下載"
description: "Innioasis Y2 更新後滾輪或點擊輪不起作用？重新安裝Y2原始軟體，檢查環，並將韌體與硬體故障分開。"
language: "zh-TW"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_zh-TW.html"
---

# Innioasis Y2 更新後滾輪不工作 | Innioasis 韌體存檔 - Innioasis 韌體下載

玩家恢復·Innioasis Y2

# Innioasis Y2 更新後滾輪不工作

輪盤轉動但玩家忽略它，或點擊輪在閃爍後立即停止。以下是如何區分 Y2 上的韌體故障和硬體故障。[取得 Updater CE](../guide_zh-TW.html#platform)[Y2軟體下載](../firmware_zh-TW.html?model=Y2&software=original-y2)[恢復指南](recovery_zh-TW.html)

## 判斷輪子有問題還是韌體有問題

在 Y2 上，滾輪是實體輸入，但韌體決定每次轉動和點擊的作用。當您更新或閃爍軟體時，輪子就會停止。一個忽略所有軟體（庫存、Rockbox 或恢復螢幕）的輪子指向該零件。
  - 在一種軟體中有效，在另一種軟體中無效： 韌體故障。
  - 在每個螢幕上都死了，包括恢復： 輪、絲帶或板。
  - 只有一個方向錯過了： 通常是環下有碎屑或磨損。
  - 車輪轉動，但沒有任何亮點： 玩家可能會被凍結——首先強制重新啟動。

## 重新安裝韌體之前快速檢查
  - 按住電源按鈕約 15 秒以強制關閉播放器，然後正常啟動。
  - 在主畫面、「設定」和音樂播放器中測試方向盤。
  - 按實體按鈕。如果電源和後退有反應，但車輪沒有反應，故障在於車輪本身。
  - 使用已知的數據線為播放器充電 30 分鐘。
  - 如果您為 Y2 或其他自訂版本安裝了 Rockbox，請返回原始軟體並再次測試。

## 重新安裝與您的播放器相符的 Y2 韌體

輪子由韌體驅動，因此透過將正確的 Y2 原始軟體放回播放器上可以修復與更新相關的故障。切勿在 Y2 上使用 Y1 軟體包，也不要選擇「夠接近」的版本 — Y2 軟體包是為 Y2 硬體建構的。
  - 打開 [更新程式 CE](../guide_zh-TW.html#platform) 在您的計算機上。
  - 套裝 裝置型號 到 Y2.
  - 選擇 原廠軟體 在 軟體 並選擇一個穩定的 Y2 版本 - 手冊包是 `rom_y2.zip`.
  - 點選 安裝 / 還原 並讓包解壓縮。
  - 完全關閉 Y2 電源，僅在更新程式要求時連接 USB 資料線，直到出現成功訊息為止。
匹配型號和版本。 如果版本清單看起來像 Y1 軟體，請停止並重新選擇 Y2。完整步驟位於 [Y2恢復指南](restore-original-y2_zh-TW.html).

## 檢查輪環是否有碎片或損壞

如果輪子僵硬、黏住或僅在一個方向發生故障，則環和外殼之間可能會殘留絨毛和砂粒。關閉播放器電源並用乾燥的超細纖維布擦拭環周圍。請勿將清潔劑或酒精滴入縫隙中，也不要撬起環。

如果環鬆動、破裂或不再發出咔嗒聲，則播放器需要維修。韌體無法修復損壞的輪子、斷開的色帶或液體損壞。

## 如果播放器也無法啟動

更新失敗可能導致 Y2 無法啟動，這看起來像是輪子故障，因為沒有輸入回應。工作通過 [Y2 不會開啟指南](y2-wont-turn-on_zh-TW.html) 用於充電、強制重啟和手動恢復。

## Innioasis Y2滾輪常見問題解答

### 為什麼我的 Innioasis Y2 滾輪在更新後停止運作？

更新可能會使輪驅動程式與韌體的其餘部分不一致，特別是在快閃記憶體中斷或使用 Y1 套件的情況下。重新安裝適合您的型號的 Y2 原始軟體版本，並在原廠主畫面上測試方向盤。

### 如何判斷Y2點擊輪是否損壞或韌體有問題？

在多個軟體中測試車輪。如果它在庫存軟體中工作但在 Rockbox 中不起作用，則這是韌體映射問題。如果它在任何螢幕（包括恢復選單）上都沒有任何反應，則懷疑是輪子、功能區或主機板造成的。

### 恢復原始軟體會修復 Y2 滾輪嗎？

它修復了由更新或不匹配的軟體包引起的故障，這是首先要嘗試的事情。它無法修復物理損壞的輪子、鬆動的色帶或液體損壞。

### 我可以使用 Y1 韌體套件來修復 Y2 車輪問題嗎？

不可以。 Y1 和 Y2 套件不可互換，閃爍錯誤的型號可能會使控制變得更糟。在運行安裝/恢復之前匹配型號和版本。

## 相關修復
  - [Y1滾輪不工作](y1-scroll-wheel-not-working_zh-TW.html) — 對 Y1 進行相同的檢查
  - [Y2打不開](y2-wont-turn-on_zh-TW.html) — 電源和啟動恢復
  - [Innioasis恢復指南](recovery_zh-TW.html) — 所有症狀指南都集中在一處
  - [安裝故障排除](../troubleshooting_zh-TW.html) — 失敗的閃光燈是什麼樣子的
  - [恢復Y2原始軟體](restore-original-y2_zh-TW.html) — 完整的恢復演練

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
