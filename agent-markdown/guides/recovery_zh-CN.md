---
title: "Innioasis Y1 和 Y2 恢复指南 | Innioasis 固件存档 - Innioasis 固件下载"
description: "针对更新后无法开机或滚轮停止工作的 Innioasis Y1 和 Y2 玩家的恢复指南。重置和固件步骤。"
language: "zh-CN"
source: "https://innioasis.app/guides/recovery_zh-CN.html"
---

# Innioasis Y1 和 Y2 恢复指南 | Innioasis 固件存档 - Innioasis 固件下载

玩家恢复 · Y1 和 Y2

# Innioasis Y1 和 Y2 恢复指南

无法启动、轮子不工作或安装中途停止。从症状开始，然后按顺序执行步骤，而不是直接跳到手动闪光。[获取 Updater CE](../guide_zh-CN.html#platform)[固件下载](../firmware_zh-CN.html)[故障排除](../troubleshooting_zh-CN.html)

以 Innioasis Updater 开头

## 引导安装修复了大部分问题

更新程序一次性完成此操作。选择软件，按照屏幕上的步骤操作，即可完成。它还会告诉您修复或新版本何时发布。

## 从症状入手

这些指南涵盖了人们在更新或刷新后最常遇到的两种故障。选择与您所看到的相符的一项，然后按顺序完成它。

### 滚轮不工作

轮子转动但玩家忽略它，或者更新后轮子立即停止。

[Y1 滚轮引导](y1-scroll-wheel-not-working_zh-CN.html) · [Y2 滚轮引导](y2-scroll-wheel-not-working_zh-CN.html)

### 播放器无法开机

黑屏、充电指示灯不亮或徽标时隐时现。

[Y1电源指南](y1-wont-turn-on_zh-CN.html) · [Y2电源指南](y2-wont-turn-on_zh-CN.html)

### 安装中途停止

更新程序在 USB 提示之前或之后失败，或者版本列表看起来错误。

[故障排除指南](../troubleshooting_zh-CN.html)

### 需要文件

每个型号的原始软件和定制包。

[固件下载](../firmware_zh-CN.html)

## Y1 和 Y2 包不可互换切勿对模型进行交叉闪烁。 一个Y1 `rom.zip` 不是 Y2 包，而是 Y2 `rom_y2.zip` 不会在 Y1 上运行。闪烁错误的模型是玩家最终出现死控件或启动循环的最常见原因之一。

检查播放器上打印的型号，然后在选择版本之前在 Updater CE 中进行匹配。

## 先恢复匹配的原版软件

在使用任何手动工具之前，请将正确型号的库存固件放回播放器上。这修复了大多数与更新相关的轮子和启动故障。

Y1: 选择Y1，选择原始软件，选择稳定的Y1版本，然后运行安装/恢复。 [完整的 Y1 恢复指南](restore-original-y1_zh-CN.html).

Y2: 选择Y2，选择原始软件，选择稳定的Y2版本，然后运行安装/恢复。 [完整的 Y2 恢复指南](restore-original-y2_zh-CN.html).

仅当更新程序要求时，关闭播放器并连接 USB 数据线。保持连接状态，直到出现成功消息。

## Updater CE 附带的手动恢复

当更新程序无法完成作业时，相同的安装包括手动工具。 [SP Flash Tool](../sp-flash-tool_zh-CN.html) 捆绑在 Windows 和 Linux x86 机器上，MTKClient 路线涵盖 macOS。两者都需要与型号相匹配的固件包，可在 [固件下载](../firmware_zh-CN.html) 页。

使用适合您平台的指南并保持播放器电量充足。如果根本没有工具检测到播放器，则故障可能是硬件而不是固件。

## 寻求帮助时应包括哪些内容
  - 型号 - Y1 或 Y2 - 印在播放器上。
  - 屏幕的作用：什么都没有、徽标、启动循环或主屏幕。
  - 计算机是否将播放器检测为 MediaTek 设备。
  - 确切的更新程序消息和您选择的软件包。
  - 您已经尝试过的内容，包括任何手动工具。

不要发布私人令牌或无关的系统文件。这 [社区 Discord](https://discord.gg/zHrT2zrcek) 和 [r/innioasis](https://reddit.com/r/innioasis) 是交换意见最快的地方。

## Innioasis 恢复常见问题解答

### 如何修复无法开机的 Innioasis 播放器？

用已知的数据线充电30分钟，长按15秒强制重启，然后检查电脑是否检测到。如果是，则恢复对应型号的原版软件；如果没有，请使用 Updater CE 附带的手动恢复工具。

### 为什么我的 Y1 或 Y2 滚轮不工作？

如果更新后轮子停止，通常是固件不匹配。重新安装型号匹配的原版软件并再次测试。如果每个固件中的轮子都死了，请将其视为硬件故障。

### 在哪里下载用于恢复的固件？

innoasis.app/firmware.html 上的固件下载页面包含每个型号的原始包和自定义包。始终选择与玩家匹配的 Y1 或 Y2 包。

### Updater CE 中包含哪些恢复工具？

更新程序 CE 包括 Windows 和 Linux 上的 SP Flash Tool，以及包括 macOS 的 MTKClient 路线，用于在正常安装无法完成时进行手动恢复。

## 相关修复
  - [Y1滚轮不工作](y1-scroll-wheel-not-working_zh-CN.html) — 更新后点击滚轮无响应
  - [Y2滚轮不工作](y2-scroll-wheel-not-working_zh-CN.html) — 对 Y2 进行相同的检查
  - [Y1打不开](y1-wont-turn-on_zh-CN.html) — 充电、重启和手动恢复
  - [Y2打不开](y2-wont-turn-on_zh-CN.html) — 对 Y2 进行相同的检查
  - [SP Flash Tool 指南](../sp-flash-tool_zh-CN.html) — Windows 和 Linux 上手动刷新

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
