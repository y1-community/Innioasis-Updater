---
title: "Windows 10/11 应用程序启动问题和智能应用程序控制解决方法 - Innioasis 更新程序"
description: "如果 Windows 10/11 或智能应用程序控制阻止您启动应用程序，请按照此处的解决方法进行操作。"
language: "zh-CN"
source: "https://innioasis.app/notices/2026-11-07-codesigning_zh-CN.html"
---

# Windows 10/11 应用程序启动问题和智能应用程序控制解决方法 - Innioasis 更新程序

2026-10-25 · 至 2026-12-31 · 型号：Y1,Y2

# Windows 10/11 应用程序启动问题和智能应用程序控制解决方法

如果 Windows 10/11 或智能应用程序控制阻止您启动应用程序，请按照此处的解决方法进行操作。

2026-10-25 · 至 2026-12-31 · 型号：Y1,Y2

误报报告已提交给 Microsoft `installer.exe` 和 `InnioasisUpdater.exe` 并采取行动，但如果 Windows Endpoint Protection 或智能应用程序控制仍然阻止计算机上的应用程序，请使用以下解决方法：

### 临时解决方法：关闭智能应用程序控制
  - 打开窗户 设置 （按 `Win + I`).
  - 前往 隐私与安全 > Windows安全 > 应用程序和浏览器控制.
  - 在下面 智能应用程序控制， 点击 智能应用程序控制设置.
  - 将智能应用程序控制设置为 离开。这会立即允许应用程序打开并运行。

如果 Windows 或 Edge 阻止您下载 Updater CE，请单击更多选项 (…） 然后 保持 > 显示更多 > 无论如何都要保留.

### 重新启用智能应用程序控制

当误报定义在您的计算机上完成更新时，您可以通过 Windows 注册表重新启用智能应用程序控制：
  - 新闻 Windows 键 + R， 类型 `regedit`，然后按 Enter 以管理员身份打开注册表编辑器。
  - 导航至： `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` （或者 `Policies`).
  - 定位 `VerifiedAndReputablePolicyState` 在右侧窗格中。
  - 双击 `VerifiedAndReputablePolicyState` 并将其值数据更改为：

  - `1` = 开启（强制）
  - `2` = 评估模式

  - 单击“确定”，关闭注册表编辑器，然后重新启动计算机。

[查看向 Microsoft 提交的 installer.exe 报告](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[请参阅向 Microsoft 提交的 InnioasisUpdater.exe 报告](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[打开链接页面](https://innioasis.app/notices.html)

[← 所有通知](index_zh-CN.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
