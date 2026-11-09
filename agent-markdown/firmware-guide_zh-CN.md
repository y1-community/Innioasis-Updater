---
title: "固件安装和库存恢复指南| Innioasis 更新程序 CE - Innioasis 固件下载"
description: "使用 Innioasis 更新程序 CE 在 Innioasis Y1、Y2、G1、G3、G5、R1、PR1 和 Timmkoo Q5、Q3 上安装自定义固件或恢复官方出厂固件。"
language: "zh-CN"
source: "https://innioasis.app/firmware-guide_zh-CN.html"
---

# 固件安装和库存恢复指南| Innioasis 更新程序 CE - Innioasis 固件下载

固件安装和库存恢复指南

# 在您的设备上安装或恢复固件

选择播放器上印有的型号。然后按照 Updater CE 中的步骤进行操作。它处理其余的事情。[获取 Updater CE](guide_zh-CN.html#platform)[浏览固件存档](firmware_zh-CN.html)[故障排除](troubleshooting_zh-CN.html)

选择播放器上印有的型号和所需的软件，然后打开本指南。 [按型号浏览软件和库存固件](firmware_zh-CN.html).

## 

[获取 Updater CE](guide_zh-CN.html#download-updater)[完整的书面教程](guide_zh-CN.html)

## 获取 Innioasis Updater CE

如果您尚未获得 Updater CE，请从这里开始。在 Updater CE 上获取带引导安装

### Windows

下载安装程序，打开它，然后按照安装提示进行操作。[下载并安装驱动程序](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[下载应用程序和驱动程序](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[被边缘阻止？](#)

如果 Windows 阻止您运行该应用程序或无法启动该应用程序，请打开“设置”，单击“隐私和安全”→“Windows 安全”→“应用程序和浏览器控制”，然后关闭“智能应用程序控制”。 [Windows 无法启动该应用程序？帮助](#smart-app-control)

安装后您需要重新启动电脑才能使其正常工作。

### macOS

下载应用程序并将其移至应用程序。如果 macOS 阻止它，请打开“系统设置”，然后打开“隐私和安全”，然后单击“仍然打开”。 [这是如何运作的](https://support.apple.com/en-gb/102445#openanyway)[下载Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

下载适用于 Intel 和 AMD 系统的 AppImage，使其可执行并运行它。[下载适用于 Intel/AMD 的 AppImage](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linux 设置注意事项](drivers_zh-CN.html#linux)另一个平台？

需要更长的计算机设置说明吗？打开 [Windows](drivers_zh-CN.html#windows) 或 [Linux](drivers_zh-CN.html#linux) 设置指南。

## 返回原始软件

要返回，请选择您的型号，然后选择 原厂软件，然后运行 安装 / 恢复。仅此而已。更新程序为您更换系统软件。[Y1恢复指南](guides/restore-original-y1.html)[Y2恢复指南](guides/restore-original-y2.html)

## 按型号划分的软件指南

选择您的型号，然后打开您的软件指南。

### Innioasis Y1

Y1 的软件：

### Innioasis Y2

Y2 的软件：

关于这两个工具的说明

## 我应该使用哪个工具？

Innioasis Updater 行政长官 是更新播放器的最安全方法。它可以保存您的音乐、视频和蓝牙配对。它会告诉您更新何时准备就绪。它可以在 Windows、macOS 和 Linux 上运行。 Innioasis Universal Flash Tool 会擦除您的播放器并在更少的计算机上运行。[打开完整比较](updater-comparison_zh-CN.html)

### Windows 无法启动该应用程序？如何关闭智能应用程序控制

Windows Defender SmartScreen 或智能应用程序控制可以在签名信誉传播之前阻止新下载的社区应用程序。智能应用程序控制目前正在影响流行的应用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的并且经过验证可以使用。关闭智能应用程序控制允许 Updater CE 正常打开和运行。
  - 打开 设置 在您的 Windows PC 上（按 Win + I).
  - 点击 隐私与安全 ，然后单击左侧边栏中的 Windows Security.
  - 点击 应用程序和浏览器控制.
  - 在下面 智能应用程序控制， 点击 智能应用程序控制设置.
  - 将切换开关设置为 离开 以允许 Updater CE 启动。

被边缘阻止？ 如果 Microsoft Edge 本身阻止下载，请单击“更多选项”按钮 (…) → 保持 → 显示更多 → 无论如何都要保留.

稍后重新启用智能应用程序控制： 当您想要重新打开智能应用程序控制时，您可以通过 Windows 注册表重新启用它 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 通过设置 `VerifiedAndReputablePolicyState` 至 `1` （开）或 `2` （评估模式）并重新启动。关闭帮助

## 这有用吗？

您的回答有助于改进本指南。是的，我发现它很有用还没有[让我们知道如何改进](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
