---
title: "我应该使用哪个工具？更新程序 CE 与 Universal Flash Tool - Innioasis 更新程序"
description: "Innioasis Updater CE 和 Innioasis Universal Flash Tool（共享闪存工具）之间的全面比较。了解创建者推荐 Innioasis Updater CE 的原因。"
language: "zh"
source: "https://innioasis.app/updater-comparison_zh.html"
---

# 我应该使用哪个工具？更新程序 CE 与 Universal Flash Tool - Innioasis 更新程序

比较和技术指南

# 我应该使用哪个工具？

了解为什么社区创建者推荐 Innioasis Updater CE：它是与官方软件和自定义软件开发人员一起构建的，更新时不会删除您的音乐和设置，在新更新到达时提醒您，并且可以在 Windows、Linux 和所有 Mac 上轻松运行。[获取 Updater CE](guide_zh-CN.html#platform)[浏览软件和固件](firmware_zh-CN.html)

## 适用于 Innioasis 和 Timmkoo 玩家的 Flash 工具

这两种工具都会对播放器进行闪光，因此区别在于闪光周围发生的情况。当您想要保留音乐、设置和蓝牙配对时，Updater CE 是适用于 Innioasis 和 Timmkoo 播放器的刷新工具：它会选择型号的软件包，运行安装，并在使用不兼容的文件之前向您发出警告。 Universal Flash Tool 是恢复优先选项，它会擦除​​玩家。

使用 Updater CE 进行正常安装、更新或恢复原始软件。仅当 Updater CE 无法完成且您拥有与模型匹配的软件包和分散文件时，才需要获取 Universal Flash Tool。这 [SP Flash Tool 指南](sp-flash-tool_zh-CN.html) 涵盖 Innioasis Y1 和 Y2 的手动路线。

社区路线

## Innioasis 更新程序 CE（社区版）

Innioasis Updater 行政长官 是创建者首先推荐的工具。它可以更新、自定义和恢复您的播放器，而不会让您的音乐或设置面临风险。
  - 更新而不擦除内部媒体或设置： 更新程序 CE 会更新您的播放器，而不会擦除内部存储。您的设置、配对的蓝牙音频设备（耳机和扬声器）以及板载音乐和视频都会安全保存。 （存储在 microSD 卡上的媒体不受这两种工具的影响。）
  - 主动更新通知： 当新的软件更新、功能或稳定性版本可用时，该应用程序会在您的计算机上主动通知您 - 无论是播放器上的固件/软件还是更新程序应用程序本身。播放器更新和该工具的新版本显示在同一位置。
  - 与定制软件开发人员一起构建： 与 Rockbox、Better-Y、Solar、JJ Launcher、Inniclassic、Y2Player 和原始工厂软件背后的开发人员携手创建，因此一切都可以协同工作并不断得到维护。
  - 适用于较旧和更多类型的计算机： 在旧版和现代机器上都能可靠地工作 - 支持 Intel x86_64 Mac 和 Apple Silicon Mac (macOS 10.15+)、Linux（Intel/AMD 的官方 AppImage）和 Windows（Windows 10/11 x64 和实验性 ARM64）。
  - 不言自明的交互式提示： 通过视觉提示直接在屏幕上引导您完成每个步骤（何时关闭电源、何时插入 USB 以及闪烁完成时）。无需外部视频手册或 PDF 指南。

工厂公用设施

## Innioasis 通用刷机工具/共享刷机工具

的 Innioasis Universal Flash Tool 也称为 Innioasis 共享 Flash 工具。它是严格为工厂库存软件包的离线手动安装而创建的，并不是与定制软件创建者合作设计的。
  - 擦拭内部存储： 使用共享/通用闪存工具进行刷新会完全擦除设备上的内部存储。这意味着每次更新后都必须重新连接蓝牙音频设备、重新配置所有首选项并更换音乐和视频。 （microSD 卡上的媒体不受这两种工具的影响。）
  - 无更新通知： 仅限离线使用的闪烁器，没有任何机制在为您的播放器发布新更新或改进时提醒您。
  - 不是由自定义项目创建者构建的： 专为官方原始ROM档案设计；不支持社区固件项目。
  - 支持的计算机较少： Mac 版本需要 macOS 15 或更高版本上的 Apple Silicon，因此英特尔 Mac 已不再适用。也没有 Linux 或 ARM64 Windows 版本。
  - 很难遵循： 没有应用内指导。您必须查阅外部视频和多页 PDF 才能连接和刷新。

## 特性比较

| 特征 | Innioasis Updater 行政长官 | 通用/共享Flash工具 |
| --- | --- | --- |
| 内部存储和设置 | 无需擦除即可更新；保留蓝牙配对、设置和板载音乐/视频 | 擦拭内部存储；需要重新连接蓝牙音频并更换媒体 |
| microSD 存储 | 保留（不受影响） | 保留（不受影响） |
| 更新通知 | 是 - 通知您播放器的更新以及更新程序应用程序本身的新版本 | 无通知 |
| 开发者协作 | 使用原始软件并与定制项目开发人员一起构建 | 仅限工厂公用设施；没有定制软件开发人员协作 |
| 电脑支持 | 老式和现代机器：Intel 和 Apple Silicon Mac、Linux、Windows | 受限：仅限 Apple Silicon macOS 15+（无 Intel Mac）、仅限 Windows x64（无 Linux） |
| 易于使用 | 应用内分步指导；不言自明 | 复杂的手动流程需要视频和 PDF 手册 |
| 软件库 | 原始软件 + Rockbox、Better-Y、Solar、Reborn、Rondo | 仅线下工厂库存包 |

## 为什么创作者推荐 Innioasis Updater CE？

当社区创建者和评论者 - 包括 [Catsteal3r 上 TikTok](https://www.tiktok.com/@catsteal3r/video/7572687586867612942), [该死的杰夫在 YouTube](https://www.youtube.com/watch?v=3d2cATPt8Nk&t=477)、Daniel T. Gaming 和 doitall - 指导观众在 Innioasis 和 Timmkoo 播放器上安装软件，他们一直推荐 Innioasis Updater 行政长官。原因如下：
  - 由原始软件和定制开发人员构建： 它是使用原始软件构建的，并与开发人员一起开发、协作并考虑到针对 Innioasis 和 Timmkoo 设备（Rockbox、Better-Y、Solar、JJ Launcher、Inniclassic、Y2Player、Koensayr）的自定义软件项目。
  - 不擦除设备媒体和设置： 使用 Updater CE 进行更新可保留您的内部存储空间。您配对的蓝牙音频设备、个性化声音设置以及板载音乐和视频保持不变。相比之下，Innioasis 中的共享/通用闪存工具会擦除设备上的内部存储，这意味着必须在更新后重新连接蓝牙音频设备并替换音乐和视频。 （存储在 microSD 卡上的媒体不受这两种工具的影响。）
  - 主动更新提醒： 一旦您的播放器有新的更新或错误修复，以及更新程序应用程序本身的新版本发布，该应用程序就会在您的计算机上主动通知您。
  - 支持较旧和更多类型的计算机： 创作者希望教程适合每个观看者，无论他们的设置如何。 Updater CE 支持较旧和较新的 PC，包括 Intel Mac、Apple Silicon Mac、Linux 发行版和 Windows。
[阅读 CE 安装指南](guide_zh-CN.html)[帮我选软件](firmware-faq_zh-CN.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
