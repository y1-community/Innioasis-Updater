---
title: "Windows 10/11 應用程式啟動問題和智慧型應用程式控制解決方法 - Innioasis 更新程序"
description: "如果 Windows 10/11 或智慧型應用程式控制阻止您啟動應用程序，請按照此處的解決方法進行操作。"
language: "zh-TW"
source: "https://innioasis.app/notices/2026-11-07-codesigning_zh-TW.html"
---

# Windows 10/11 應用程式啟動問題和智慧型應用程式控制解決方法 - Innioasis 更新程序

2026-10-25 · 至 2026-12-31 · 型號：Y1,Y2

# Windows 10/11 應用程式啟動問題和智慧型應用程式控制解決方法

如果 Windows 10/11 或智慧型應用程式控制阻止您啟動應用程序，請按照此處的解決方法進行操作。

2026-10-25 · 至 2026-12-31 · 型號：Y1,Y2

誤報報告已提交給 Microsoft `installer.exe` 和 `InnioasisUpdater.exe` 並採取行動，但如果 Windows Endpoint Protection 或智慧型應用程式控制仍然阻止電腦上的應用程序，請使用以下解決方法：

### 臨時解決方法：關閉智慧型應用程式控制
  - 打開窗戶 設定 （按 `Win + I`).
  - 前往 隱私與安全 > Windows安全 > 應用程式和瀏覽器控制.
  - 在下面 智慧應用程式控制， 點選 智慧應用程式控制設定.
  - 將智慧型應用程式控制設定為 離開。這會立即允許應用程式開啟並運行。

如果 Windows 或 Edge 阻止您下載 Updater CE，請按一下更多選項 (…） 然後 保持 > 顯示更多 > 無論如何都要保留.

### 重新啟用智慧型應用程式控制

當誤報定義在您的電腦上完成更新時，您可以透過 Windows 註冊表重新啟用智慧型應用程式控制：
  - 新聞 Windows 鍵 + R， 類型 `regedit`，然後按 Enter 以管理員身分開啟登錄編輯程式。
  - 導航至： `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` （或者 `Policies`).
  - 定位 `VerifiedAndReputablePolicyState` 在右側窗格中。
  - 按兩下 `VerifiedAndReputablePolicyState` 並將其值資料變更為：

  - `1` = 開啟（強制）
  - `2` = 評估模式

  - 按一下“確定”，關閉登錄編輯器，然後重新啟動電腦。

[查看向 Microsoft 提交的 installer.exe 報告](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[請參閱向 Microsoft 提交的 InnioasisUpdater.exe 報告](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[開啟連結頁面](https://innioasis.app/notices.html)

[← 所有通知](index_zh-TW.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
