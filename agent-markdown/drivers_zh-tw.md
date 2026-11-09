---
title: "Innioasis Y1 和 Y2 USB 驅動程式 | Windows 驅動程式與 Linux 權限 - Innioasis 更新程式"
description: "設定您的電腦的 Innioasis 更新程式：Windows MediaTek 驅動程式和 Linux USB 權限 - 以及電纜和計時修復。"
language: "zh-tw"
source: "https://innioasis.app/drivers_zh-tw.html"
---

# Innioasis Y1 和 Y2 USB 驅動程式 | Windows 驅動程式與 Linux 權限 - Innioasis 更新程式

電腦設定

# 在播放器之前先準備好計算機。

大多數連接問題來自驅動程式、權限、電纜或計時。 Windows 需要安裝 MediaTek 驅動程式。 Linux 需要正確的 USB 權限。在下面找到您的平台。[取得 Updater CE](guide_zh-TW.html#platform)[疑難排解](troubleshooting_zh-TW.html)

## Windows
  - 下載下面的 MediaTek 驅動程式安裝程式。
  - 運行安裝程式並允許 Windows 安裝驅動程式。
  - 重新啟動電腦。
  - 開啟 Updater CE 並等待連線提示，然後再插入已關閉的播放器。

某些 Windows 系統透過核心隔離（記憶體完整性）來阻止驅動程式。如果重新啟動後 Updater CE 仍然無法看到播放器，請在 Windows 安全性中關閉記憶體完整性，重新啟動並重新安裝驅動程式。如果系統允許，完成後請重新開啟該設定。

Windows 無法啟動該應用程式？ 如果 Windows 安全性或智慧型應用程式控制阻止 Updater CE 打開，請打開 設定 （按 Win + I) → 隱私與安全 → Windows Security → 應用程式和瀏覽器控制 → 智慧應用程式控制設定 並將其設為 離開。智慧型應用程式控制目前正在影響熱門應用程式，例如 Epic Overlay Service（Fortnite 所用）——Updater CE 安全且經驗證。如需日後重新啟用，請將 `VerifiedAndReputablePolicyState` 到 `1` （開）或 `2` （評估模式）下 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 在登錄編輯器中。[下載 Windows 驅動程式](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[返回主要指南](guide_zh-TW.html#windows) · [軟體下載](firmware_zh-TW.html)

## Linux USB 權限

Linux 需要讓您的使用者帳號與播放器內的 MediaTek USB 晶片對話。更新程式 CE 通常會在安裝過程中解決此問題，並且相同的權限涵蓋 SP Flash Tool，因此請將其視為修復步驟而不是正常階段。
  - 以普通使用者身分（而非 root 使用者）執行 Updater CE。安裝程式僅在需要時才請求管理員存取權限。
  - 檢查玩家是否被看見。關閉播放器電源，連接電纜，然後在終端機中執行 lsusb 命令。連接的播放器顯示為 MediaTek 設備，供應商 ID 為 0e8d。
`lsusb`
  - 如果它出現在 lsusb 中，但 Innioasis 更新程式 CE 或 SP Flash Tool 表示權限被拒絕或無法開啟端口，則您的使用者無法存取 USB 裝置。相同的 udev 規則涵蓋這兩種工具，因此請新增一個讓使用者群組讀取它的規則。
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

將該行儲存到名為 /etc/udev/rules.d/51-innioasis.rules 的新文件，然後執行：`sudo udevadm control --reload && sudo udevadm trigger`
  - 完全拔掉播放器的插頭，重新插入，然後再次嘗試安裝。
  - 如果 SP Flash Tool 報告序列權限或連接埠爭用，請完全拔出插頭並僅在出現提示時重新連線。
不要臨時調整閃光偏移。如果您轉向手動復原工具，請使用專案附帶的檔案和特定於模型的配置。

[返回主要指南](guide_zh-TW.html#linux) · [軟體下載](firmware_zh-TW.html) · [SP Flash Tool 指南](sp-flash-tool_zh-TW.html)

## 電纜和時序
  - 使用已知的 USB 資料線。
  - 故障排除時避免使用集線器。
  - 完全關閉正確型號的電源。
  - 僅在出現提示時連接。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
