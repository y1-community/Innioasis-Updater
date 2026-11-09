---
title: "开始使用 Innioasis 更新程序 CE |在任何 Innioasis 或 Timmkoo 播放器上安装或恢复固件 - Innioasis 更新程序"
description: "下载适用于 Windows、macOS 或 Linux 的 Innioasis 更新程序 CE，然后按照几个指导步骤在任何 Innioasis 或 Timmkoo 播放器上安装或恢复固件。"
language: "zh-cn"
source: "https://innioasis.app/guide_zh-cn.html"
---

# 开始使用 Innioasis 更新程序 CE |在任何 Innioasis 或 Timmkoo 播放器上安装或恢复固件 - Innioasis 更新程序

快速启动

# Innioasis 更新程序 CE 入门

适用于所有 Innioasis 和 Timmkoo 音频播放器。在您的计算机上安装 Innioasis Updater CE，选择您的型号和所需的软件，然后按照提示进行操作。

## 

[获取 Updater CE](guide_zh-CN.html#download-updater)[完整的书面教程](guide_zh-CN.html)

## 获取 Innioasis Updater CE

Innioasis Updater 行政长官 是在您的播放器上安装官方更新和社区软件的应用程序。它会保留您的音乐和设置，并且可以在 Windows、macOS 和 Linux 上运行。

### Windows

下载安装程序，运行它，然后在完成后重新启动您的电脑。[获取驱动程序](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[下载Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

如果 Windows 阻止您运行该应用程序或无法启动该应用程序，请打开“设置”，单击“隐私和安全”→“Windows 安全”→“应用程序和浏览器控制”，然后关闭“智能应用程序控制”。智能应用程序控制目前影响流行的应用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的并且经过验证可以使用。 [Windows 无法启动该应用程序？帮助](#smart-app-control)

安装后重新启动您的电脑。驱动程序帮助位于 [Windows 设置说明](drivers_zh-CN.html#windows).

### macOS[下载Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

如果您的 Mac 首次运行该应用程序时将其阻止，请打开“系统设置”，点击“隐私与安全性”，向下滚动至“安全性”，然后点击 [无论如何打开](https://support.apple.com/en-gb/102445#openanyway)。您也可以在访达中按住 Control 键点按（或右键点按）该应用程序并选择“打开”。

适用于搭载 macOS Monterey 及更高版本的 Intel 和 Apple Silicon Mac。

### Linux

下载适用于 Intel 和 AMD 系统的 AppImage，使其可执行并运行它。[下载适用于 Intel/AMD 的 AppImage](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Linux 设置注意事项](drivers_zh-CN.html#linux)另一个平台？

您需要您的播放器、一根可传输数据的 USB 数据线（无法安装只能充电的数据线）以及几分钟的时间。保持电缆连接，直到更新程序 CE 表示已完成。

## 选择您的型号和软件
  - 设备型号： 选择播放器上印有的型号， Y1 或 Y2。为一种型号制作的软件无法安装在另一种型号上。
  - 软件及发布： 当为您的型号列出时，选择原始软件、Rockbox、Solar、JJ Launcher、Inniclassic、Y2Player 或 Koensayr，然后选择一个版本。稳定是安全的选择。
  - 安装： 点击 安装 / 恢复，完全关闭播放器电源，仅在更新程序 CE 要求时连接 USB 电缆。
  - 结束： 将播放器和电缆放在一边，直到出现成功消息，然后断开连接并启动播放器。

Y1 2.0.0 之前附带原始软件的玩家需要 设备 Type B。其他人都保留默认值 Type A。用于连接已关闭播放器的更新程序连接说明按照适用于您的型号的实时 Updater CE 提示进行操作。

## 返回原始软件

定制软件是可逆的。在 Updater CE 中，选择您的型号，然后选择 原厂软件，选择一个稳定版本，然后运行 安装 / 恢复 同样的方式。没有什么可以手动删除的。[Y1恢复指南](guides/restore-original-y1.html)[Y2恢复指南](guides/restore-original-y2.html)

如果闪光在 USB 提示之前停止，请首先检查电缆、平台设置和型号。看 [故障排除](troubleshooting_zh-CN.html) 对于修复， [Y1 和 Y2 恢复指南](guides/recovery.html) 对于动力和车轮故障，以及 [SP Flash Tool](sp-flash-tool_zh-CN.html) 用于高级康复。

## 按型号划分的软件指南

打开适合您的型号和您选择的软件的指南。

### Innioasis Y1

Y1 的软件：

### Innioasis Y2

Y2 的软件：

## 我应该使用哪个工具？

本指南使用 Innioasis 更新程序 2.5.1，也称为更新程序 CE。它可以保证您的歌曲、视频和蓝牙配对的安全。它会告诉您更新何时准备就绪。 Innioasis Universal Flash Tool 会擦除您的播放器并需要手动步骤。 [比较工具 →](updater-comparison_zh-CN.html)

## Windows 无法启动该应用程序？智能应用程序控制解决方法

Windows Defender SmartScreen 或智能应用程序控制可以在签名信誉传播之前阻止新下载的社区应用程序。智能应用程序控制目前正在影响流行的应用程序，例如 Epic Overlay Service（由 Fortnite 使用）——Updater CE 是安全的并且经过验证可以使用。关闭智能应用程序控制允许 Updater CE 正常打开和运行。
  - 打开 设置 在您的 Windows PC 上（按 Win + I).
  - 点击 隐私与安全 ，然后单击左侧边栏中的 Windows Security.
  - 点击 应用程序和浏览器控制.
  - 在下面 智能应用程序控制， 点击 智能应用程序控制设置.
  - 将切换开关设置为 离开 以允许 Updater CE 启动。

通过 Edge 下载？ 如果 Edge 本身阻止下载，请单击“更多选项”按钮 (…) → 保持 → 显示更多 → 无论如何都要保留.

稍后重新启用智能应用程序控制： 当您想要重新打开智能应用程序控制时，您可以通过 Windows 注册表重新启用它 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 通过设置 `VerifiedAndReputablePolicyState` 至 `1` （开）或 `2` （评估模式）并重新启动。

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
