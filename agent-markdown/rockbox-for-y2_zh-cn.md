---
title: "Rockbox for Y2 (Rockbox-Y2)：概述、构建和安装指南"
description: "Y2、Rockbox-Y2 的 Rockbox 和 rockbox-y2 参考 Innioasis Y2 的社区 Rockbox 固件端口。了解它包含哪些内容以及如何使用 Innioasis Updater CE 安装它。"
language: "zh-cn"
source: "https://innioasis.app/rockbox-for-y2_zh-cn.html"
---

# Rockbox for Y2 (Rockbox-Y2)：概述、构建和安装指南

[← 固件下载](firmware_zh-CN.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox 为 Y2 (Rockbox-Y2)

Rockbox-Y2（也称为“Y2的Rockbox”）是Innioasis Y2的专用社区Rockbox固件端口。它使用自己的 ROM 包（`rom_y2.zip`）并通过 Innioasis 更新程序 CE 直接安装。[安装Rockbox-Y2](rockbox-y2/install.html)[下载ROM](rockbox-y2/download.html)[书面教程](guides/rockbox-y2.html)[Rockbox-Y2 轮毂](rockbox-y2/)

## 专为 Innioasis Y2 打造

在 Innioasis Updater CE 中，该固件被列为 Rockbox 什么时候 Y2 被选中。其版本由 [spycemagic/y2-rockbox](firmware_zh-CN.html?model=Y2&software=rockbox-y2) 带有包名的项目 `rom_y2.zip`.

切勿在 Y2 上安装 Y1 固件包。选择 Y2 Updater CE 中会自动将版本列表过滤为仅与 Y2 兼容的版本。

## Rockbox-Y2 提供什么
  - 基于标签的音乐库 — 从音频文件标签浏览专辑、艺术家和流派，或直接浏览文件夹。
  - 播放控制 — 无缝播放、交叉淡入淡出、ReplayGain 和均衡器设置。
  - 自定义主题 — 安装与您的 Rockbox-Y2 版本兼容的主题 ([Y2 主题指南](rockbox-y2-themes.html)).
  - 100%离线 — 无需帐户或订阅即可播放 MicroSD 卡中的本地文件。
  - 轻松恢复出厂设置 — 在 Updater CE 中随时返回 Y2 原始软件。

## 选择 Rockbox-Y2 版本
  - 始终选择 Y2 在 设备型号 首先。
  - 除非您正在测试特定版本，否则请选择最新版本。
  - 阅读 [Rockbox-Y2 发行说明](release-notes/rockbox-y2/index_zh-CN.html) 查看每个版本中发生了什么变化。

## 社区开发者直接下载

Innioasis 更新程序 CE 始终直接从社区固件开发人员处下载固件包（[spycemagic/y2-rockbox](firmware_zh-CN.html?model=Y2&software=rockbox-y2)），并且这些开发人员全权负责在 Updater CE 中列出他们的软件版本。

您可以让Updater CE下载并刷新 `rom_y2.zip` 自动，或从我们的下载包 [Rockbox-Y2下载页面](rockbox-y2/download.html) 和 [Rockbox ROM 下载页面](rockbox-rom-download_zh-CN.html).[Rockbox-Y2下载](rockbox-y2/download.html)[从本地 ZIP 安装](rockbox-y2/portable-zip.html)

## 如何安装Rockbox-Y2
  - 打开 Innioasis 更新程序 CE 并设置 设备型号 至 Y2.
  - 选择 Rockbox 在 软件.
  - 从列表中选择 Y2 版本。
  - 点击 安装 / 恢复 所以Updater CE直接从开发者那里下载包。
  - 当更新程序 CE 要求时，完全关闭 Y2 电源并使用 USB 数据线将其连接。
  - 等待完成消息，然后拔下并打开 Y2。

有关完整的分步演练，请阅读 [Rockbox-Y2教程](guides/rockbox-y2.html).

## 恢复原始Y2软件

要返回出厂固件，请选择 Y2 和 原厂软件 在 Updater CE 中，选择一个稳定版本，然后单击 安装 / 恢复。请参阅 [恢复指南](rockbox-y2/restore-stock.html) 和 [Y2 原始软件页面](original-software-y2_zh-CN.html).

## 常见问题Updater CE 从哪里下载 Rockbox-Y2？

更新程序 CE 始终直接从社区固件开发人员自己的版本下载固件包（`spycemagic/y2-rockbox`）。开发人员全权负责在 Updater CE 中列出其软件版本。为什么这个包被命名为rom_y2.zip？

开发人员命名 Y2 固件存档 `rom_y2.zip` 所以它不能与 Y1 混淆 `rom.zip`.Y1 主题适用于 Y2 吗？

并非总是如此。检查您的 Y2 版本的发行说明并查看 [Rockbox-Y2 主题指南](rockbox-y2-themes.html).

## 相关指南

### [Rockbox-Y2 轮毂](rockbox-y2/)

所有 Y2 指南：安装、下载、主题、恢复、双启动和故障排除。

### [Rockbox-Y1 与 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 和 Y2 Rockbox 构建有何不同。

### [Rockbox-Y2 主题](rockbox-y2-themes.html)

在 Rockbox-Y2 上安装和重置主题。

### [Y1 的 Rockbox](rockbox-for-y1_zh-CN.html)

Innioasis Y1 端口的概述和安装指南。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
