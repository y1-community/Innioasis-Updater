---
title: "Rockbox for Y1 (Rockbox-Y1)：概述、构建和安装指南"
description: "Y1、Rockbox-Y1 的 Rockbox 和 rockbox-y1 均引用 Innioasis Y1 的社区 Rockbox 固件。了解它添加了什么、选择哪个版本以及如何使用 Innioasis Updater CE 安装它。"
language: "zh-CN"
source: "https://innioasis.app/rockbox-for-y1_zh-CN.html"
---

# Rockbox for Y1 (Rockbox-Y1)：概述、构建和安装指南

[← 固件下载](firmware_zh-CN.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox 为 Y1 (Rockbox-Y1)

“Rockbox”、“Rockbox-Y1”和“Y1 的Rockbox”均指 Innioasis Y1 的同一社区 Rockbox 固件。以下是它向您的播放器添加的内容、要选择的版本以及如何使用 Innioasis Updater CE 安装它。[安装Rockbox-Y1](rockbox-y1/install.html)[下载ROM](rockbox-y1/download.html)[书面教程](guides/rockbox-y1.html)[Rockbox-Y1 轮毂](rockbox-y1/)

## 一个固件，多个名称

在 Innioasis Updater CE 中，该固件显示为 Rockbox 当您选择设备型号时 Y1。指南、视频和发行说明也称其为 Rockbox-Y1 或 Y1 的 Rockbox 因此很明显，构建是针对 Y1 而不是 Y2。

安装前请务必检查播放机上打印的型号：Y1 和 Y2 固件包不可互换。

## Rockbox-Y1 为您的 Y1 添加了什么

Rockbox-Y1 是 Innioasis Y1 的开源 Rockbox 音乐播放器固件的社区端口：
  - 基于标签的音乐库 — 使用音频标签按艺术家、专辑、流派和年份浏览，或直接浏览文件夹。
  - 高级音频播放 — 无缝播放、交叉淡入淡出、ReplayGain 和完整的均衡器。
  - 自定义主题 — 从数百个 240p 和 360p 社区主题中进行选择，包括经典的 iPod 风格布局。
  - 调频收音机 — 内置 FM 收音机支持。
  - 可选附加功能 — 通过 Wi-Fi 和 Last.fm / ListenBrainz / Maloja 在支持的版本上进行播客下载。
  - 双启动 — 切换回工厂原始软件，无需在支持的版本上重新刷新。

## 我应该选择哪个 Y1 版本？
  - 240p 与 360p — 240p 使用经典 320×240 Rockbox 主题构建作品； 360p 构建使用更清晰的 480×360 Y1 主题。将构建分辨率与您要使用的主题相匹配（[240p 与 360p 指南](rockbox-y1/resolution.html)).
  - Type A 与 Type B — Type A 适用于出厂软件 2.0.0 或更高版本的 Y1 播放器； Type B 适用于较早的 Y1 单元。选择 Type A，除非您知道您的 Y1 是 Type B。
  - 稳定版与夜间版 — 选择稳定的版本用于日常聆听，或选择夜间版本来测试最新的更改。

## 社区开发者直接下载

Innioasis 更新程序 CE 始终直接从社区固件开发人员处下载固件包（[rockbox-y1/rockbox](firmware_zh-CN.html?model=Y1&software=rockbox-y1)），开发者自己全权负责在 Updater CE 中列出他们的软件版本。

您可以让 Updater CE 自动下载并安装固件，或者从我们的网站下载 ROM 软件包 [Rockbox-Y1下载页面](rockbox-y1/download.html) 和 [Rockbox ROM 下载页面](rockbox-rom-download_zh-CN.html).[Rockbox-Y1下载](rockbox-y1/download.html)[从本地 ZIP 安装](rockbox-y1/portable-zip.html)

## 如何安装Rockbox-Y1
  - 打开 Innioasis 更新程序 CE 并设置 设备型号 至 Y1.
  - 选择 Rockbox 在 软件.
  - 选择一个稳定的版本（或启用夜间构建来测试预览）。
  - 点击 安装 / 恢复 所以Updater CE直接从开发者那里下载包。
  - 当 Updater CE 提示您时，完全关闭 Y1 电源并使用 USB 数据线连接它。
  - 等待完成消息，然后断开连接并打开播放器。

有关屏幕截图和详细设置提示，请阅读 [完整的 Rockbox-Y1 教程](guides/rockbox-y1.html).

## 恢复原始Y1软件

您可以随时返回出厂软件：选择 Y1 和 原厂软件 在 Updater CE 中，选择一个稳定版本，然后单击 安装 / 恢复。 MicroSD 卡上的音乐将被保留。请参阅 [恢复指南](rockbox-y1/restore-stock.html) 和 [Y1 原始软件页面](original-software-y1_zh-CN.html).

## 常见问题Y1 的 Rockbox 与 Rockbox-Y1 相同吗？

是的。 Rockbox、Rockbox-Y1、Rockbox 代表 Y1，以及 `rockbox-y1` 全部引用 Innioasis Y1 的同一社区 Rockbox 端口。Updater CE 从哪里下载 Rockbox-Y1？

更新程序 CE 始终直接从社区固件开发人员自己的版本下载固件包（`rockbox-y1/rockbox`）。开发人员全权负责在 Updater CE 中列出其软件版本。我可以在 Y2 上安装 Rockbox-Y1 吗？

不会。Y2 有自己独立的固件版本。使用 [Y2 的 Rockbox](rockbox-for-y2_zh-CN.html) 反而。安装 Rockbox-Y1 会删除我的音乐吗？

不会。音乐存储在 MicroSD 卡上，刷新播放器内部固件时不会受到影响。

## 相关指南

### [Rockbox-Y1 轮毂](rockbox-y1/)

所有 Y1 指南：安装、下载、主题、恢复、双启动和故障排除。

### [Rockbox-Y1 与 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 和 Y2 Rockbox 构建有何不同。

### [Rockbox-Y1 主题](rockbox-y1-themes.html)

如何使用 Updater CE 传输 240p 和 360p 主题。

### [Rockbox 概述](rockbox_zh-CN.html)

关于 Innioasis Y1 和 Y2 玩家的 Rockbox 简介。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
