---
title: "SP Flash Tool 适合 Innioasis 和 Timmkoo 玩家"
description: "在 Windows 和 Linux 上找到与 Innioasis 更新程序捆绑在一起的 SP Flash Tool，提取 rom.zip 或 rom_y2.zip，并使用匹配的分散文件刷新 Innioasis Y1 或 Y2。"
language: "zh-cn"
source: "https://innioasis.app/sp-flash-tool_zh-cn.html"
---

# SP Flash Tool 适合 Innioasis 和 Timmkoo 玩家

手动闪光

# 适用于 Innioasis 和 Timmkoo 玩家的 Flash 工具

SP Flash Tool 包含在 Innioasis 更新程序中 [Windows](drivers_zh-CN.html#windows) 和 [Linux](drivers_zh-CN.html#linux)。你已经拥有了。本指南展示了在 Innioasis Y1 或 Y2 上使用它的安全方法，以及 Timmkoo 玩家的更新程序路线。[返回更新程序指南](guide_zh-CN.html)[固件下载](firmware_zh-CN.html)[故障排除](troubleshooting_zh-CN.html)

以 Innioasis Updater 开头

## 更新程序一次性完成整个工作

更新程序一次性完成大部分安装。选择软件，按照步骤操作，就完成了。它还会告诉您修复或新版本何时发布。 SP Flash Tool 位于更新程序工具包内，用于更新程序无法完成的极少数情况。以下步骤是例外。

## 这个工具的用途

更新程序会为您刷新播放器。 SP Flash Tool 是同一台发动机，但没有护栏。当更新程序无法启动、播放器无法连接或您了解分散文件时，请使用它。首先尝试更新程序。 对于大多数安装和大多数恢复，引导 [更新者路线](guide_zh-CN.html) 是更安全的选择。当您知道为什么需要它时，请使用 SP Flash Tool，并准备好已充电的电池和 USB 数据线。

## 适合 Innioasis 玩家的 Flash 工具

Innioasis Updater 是 Innioasis 玩家的刷机工具。它通过模型匹配的流程安装官方软件、更新和恢复包，并保留您的音乐和设置。

### Innioasis Y1 闪存工具

在更新程序中选择 Y1 版本，然后在应用程序询问时连接已关闭的播放器。当您需要手动路由时，相同的 Y1 包可与 SP Flash Tool 配合使用。

### Innioasis Y2 闪存工具

选择 Y2 列出的版本。 Y2 软件包不能与 Y1 软件包互换，因此在开始之前请检查型号。

## 适合 Timmkoo 玩家的 Flash 工具

Timmkoo 玩家使用相同的更新程序安装流程。它直接读取 Timmkoo 的 ZIP 和 RAR 包，因此您不需要单独的刷新工具或分散文件。

### Timmkoo Q5 闪存工具

在Updater中选择Q5型号，选择Timmkoo包，然后运行Install / Restore并根据提示连接播放器。

### Timmkoo Q3 和 Q3E 闪存工具

Q3 条目同样涵盖了 Q3 和 Q3E。更新程序从项目发布的包中选择匹配的文件。

### Timmkoo A5 闪存工具

在选择软件包之前选择 A5 型号，然后按照相同的安装提示进行操作。

## 更新程序放置的位置

SP Flash Tool 随更新程序安装文件夹一起提供，而不是作为单独下载。当您需要时从那里打开它。

### Windows

打开更新程序安装文件夹并运行 `flash_tool.exe`。该文件夹通常位于 `%LOCALAPPDATA%\Innioasis Updater`。某些设置中包含带有 SP Flash Tool 快捷方式的 Toolkit 文件夹。

### Linux

运行捆绑的 `flash_tool` x86 / x86_64 上的 Updater 应用程序文件夹中的二进制文件。项目安装程序使用 udev 规则准备 USB 权限，因此连接时应该出现播放器。

### macOS

SP Flash Tool 未捆绑在 macOS 上。更新程序使用 MTKClient 路线代替。使用 [引导安装](guide_zh-CN.html) 在 Mac 上，并在 Windows 或 Linux 计算机上保留 SP Flash Tool。

该工具附带 MediaTek 下载代理和特定于模型的配置，因此您无需从其他地方收集 DA 或分散文件。

## 准备固件
  - 获取您想要的版本 [固件下载](firmware_zh-CN.html)。选择 `rom.zip` 对于 Y1 或 `rom_y2.zip` 对于 Y2。
  - 将 ZIP 解压缩到其自己的文件夹中。 Windows 可以使用全部提取。在 Linux 上，使用存档管理器或 `unzip` 在终端中。
  - 检查分散文件是否位于提取的文件夹中。它通常被命名为 `MT6572_Android_scatter.txt` 对于 Y1 包和 `MT6582_Android_scatter_def.txt` 对于 Y2 包，尽管发行版可能以其项目命名。
将模型分开。 Y1 散点描述了 MT6572 设备，Y2 散点描述了 MT6582 设备。刷错了就会导致玩家变砖。如果 ZIP 内的分散与您的型号不匹配，请停止并使用为您的型号列出的软件包。

## 加载散射和闪光
  - 从更新程序安装文件夹中打开 SP Flash Tool。
  - 在下载选项卡中，单击 选择 旁边的分散加载文件，然后从提取的文件夹中选择分散文件。分区列表将被填充。
  - 保持闪光灯模式开启 仅供下载 除非你有意进行完全恢复，这需要 固件升级.
  - 点击 下载。该工具将等待玩家。
  - 完全关闭播放器电源，然后连接 USB 数据线。将播放器放下，不要移动它。
  - 等待绿色复选标记。然后断开电缆并启动播放器。

保持与引导路线相同的 USB 电缆和计时规则：数据电缆，无集线器，并且仅在工具准备就绪时进行连接。

## 如果不闪烁
  - 检查分散图和 ZIP 是否与播放器上打印的型号匹配。
  - 连接前请确认播放器已完全断电。
  - 在 Windows 上，确认通过更新程序安装安装了 MediaTek 驱动程序；在 Linux 上，从项目安装程序确认 udev 规则。
  - 仅当工具等待时才重新连接电缆。港口比赛可能需要完全拔掉插头并重新进行 下载 点击。

对于除此之外的任何事情，请打开 [故障排除](troubleshooting_zh-CN.html)。请记住：更新程序仍然是正常途径，并且 [Y1](guides/restore-original-y1.html) 和 [Y2](guides/restore-original-y2.html) 恢复指南也使用它。

## 这有用吗？

您的回答有助于改进本指南。是的，我发现它很有用还没有[让我们知道如何改进](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
