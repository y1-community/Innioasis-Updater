---
title: "如何在 Innioasis Y1 或 Y2 - Innioasis 更新程序上安装 Rockbox"
description: "使用更新程序在 Innioasis Y1 或 Y2 上安装 Rockbox：主题、稳定版本、Type A 和 Type B 说明，以及如何在之后恢复原始软件。"
language: "zh-cn"
source: "https://innioasis.app/rockbox_zh-cn.html"
---

# 如何在 Innioasis Y1 或 Y2 - Innioasis 更新程序上安装 Rockbox

Rockbox参考

# 在您的 Y1 或 Y2 上获得 Rockbox

Rockbox 更改了播放器软件并打开了更深层次的音乐播放器界面、播放控件、排序和主题选项。安装是引导式的，但 Y1 和 Y2 是不同的过程。[Y1 上的 Rockbox](guides/rockbox-y1.html)[Y2 上的 Rockbox](guides/rockbox-y2.html)[为什么是Rockbox？](rockbox-benefits_zh-CN.html)

## 安装发生了什么变化

Rockbox 是定制软件。当匹配的原始软件包可用时，它不会消除您返回到库存界面的能力。它可以改进音乐浏览和定制，但功能、分辨率、电池寿命和主题兼容性取决于构建。请勿混用型号。 为 Y1 玩家选择 Y1，为 Y2 玩家选择 Y2。看起来相似的版本名称不足以证明软件包是兼容的。

## 观看视频

视频由弗劳吉斯拍摄。它显示了 Innioasis 更新程序路由；对于您的 Y1 或 Y2，请使用下面特定于型号的书面步骤。

视频由 [克里斯蒂安广场](https://www.youtube.com/@CristianPlaza) （西班牙语），在 Y1 上显示 Rockbox。请针对您的播放器使用以下特定于型号的步骤。

## 共享Updater路由
  - 安装更新程序并在出现询问之前不进行任何连接。
  - 选择播放器上印有的型号 设备型号.
  - 选择 Rockbox 在 软件.
  - 选择稳定版本，除非您有意测试夜间构建。
  - 点击 安装 / 恢复，然后按照关机和USB连接提示进行操作。
  - 仅在成功消息后断开连接。

## 240p、360p 和主题

较早的 Rockbox 主题合集可能以 240p 制作。 Y1 社区构建也使用 360p 兼容性标签。在选择版本之前，请阅读发行说明和主题源。为一种分辨率或软件系列制作的主题可能不适用于另一种分辨率或软件系列。[浏览社区主题](https://themes.innioasis.app/?lang=zh-CN)[主题工具](https://themes.innioasis.app/?lang=zh-CN)

## 返回原始软件

再次选择相同型号，选择 原厂软件，选择一个稳定的版本，并使用 安装 / 恢复。如果故障发生在 USB 提示之前，请检查计算机和提取的文件。如果检测到播放器但刷新失败，请从 [故障排除](troubleshooting_zh-CN.html).[Y1恢复](guides/restore-original-y1.html)[Y2恢复](guides/restore-original-y2.html)

## 常见问题我重新安装了 Rockbox，但没有解决任何问题。

重新安装 Rockbox 会在相同的文件上写入相同的版本，因此无法重置 Rockbox 保留在 MicroSD 上的内容。如果问题是卡上的设置、主题、播放列表或数据库损坏，重新安装将无法清除它。可靠的重置是删除 `.rockbox` MicroSD - Rockbox 中的文件夹会在下次启动时构建一个新的文件夹。
  - 完全关闭播放器电源并取出 MicroSD 卡，或将播放器连接为 USB 驱动器。
  - 显示计算机上的隐藏文件，以便该文件夹可见。 如何显示隐藏文件在您的计算机上显示点文件Windows: 在文件资源管理器中打开 看法 选项卡并勾选 隐藏物品.macOS: 在 Finder 中按 Cmd+Shift+. 切换隐藏文件。Linux·GNOME 文件： 按 Ctrl+H，或打开菜单并选择 显示隐藏文件.Linux·KDE 海豚： 按 Ctrl+H，或使用 查看 → 显示隐藏文件.
  - 删除 `.rockbox` 卡根目录中的文件夹。
  - 重新插入卡并启动播放器。 Rockbox 使用默认值重新创建文件夹。
  - 重新应用您的主题和设置。如果问题仅在特定主题之后出现，则该主题就是原因。

正在删除 `.rockbox` 不会卸载 Rockbox，也不会影响您的音乐 — 该文件夹包含设置、主题和缓存，并且会自动重建。如果您想保留主题，请将文件夹复制到 `.rockbox` 删除之前，或将文件夹重命名为 `.rockbox-old` 首先。为什么我在 MicroSD 上看不到 .rockbox 文件夹？

在大多数计算机上，名称以点开头的文件夹默认是隐藏的。您无需查看它即可安装 Rockbox — 更新程序会处理这些文件。如果您正在排除故障并想要删除它，请先打开隐藏文件。 如何显示隐藏文件在您的计算机上显示点文件Windows: 在文件资源管理器中打开 看法 选项卡并勾选 隐藏物品.macOS: 在 Finder 中按 Cmd+Shift+. 切换隐藏文件。Linux·GNOME 文件： 按 Ctrl+H，或打开菜单并选择 显示隐藏文件.Linux·KDE 海豚： 按 Ctrl+H，或使用 查看 → 显示隐藏文件.删除 .rockbox 会重置我的主题和设置吗？

是的 - `.rockbox` 保存 Rockbox 的设置、主题、播放列表和缓存数据库。删除它会使 Rockbox 恢复到干净的默认状态。备份整个文件夹（或将其重命名为 `.rockbox-old`）如果您可能想要恢复其中任何内容，请启动播放器并 Rockbox 创建一个新文件夹。

## 更多 Rockbox-Y1 和 Rockbox-Y2 指南

探索在两种型号上安装、下载、主题化、恢复和故障排除的分步指南 Rockbox：[Rockbox-Y1 轮毂](rockbox-y1/)[Rockbox-Y2 轮毂](rockbox-y2/)[Rockbox ROM 下载](rockbox-rom-download_zh-CN.html)[Y1 的 Rockbox](rockbox-for-y1_zh-CN.html)[Y2 的 Rockbox](rockbox-for-y2_zh-CN.html)[Rockbox-Y1 与 Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 主题](rockbox-y1-themes.html)[Rockbox-Y2 主题](rockbox-y2-themes.html)

## 这个参考有用吗？

您的回答有助于改进本指南。是的还没有[让我们知道如何改进](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
