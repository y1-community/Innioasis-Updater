---
title: "Innioasis Y1 更新后滚轮不工作 | Innioasis 固件存档 - Innioasis 固件下载"
description: "Innioasis Y1 更新后滚轮或点击轮不起作用？重新安装Y1原始软件，检查环，并将固件与硬件故障分开。"
language: "zh-CN"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_zh-CN.html"
---

# Innioasis Y1 更新后滚轮不工作 | Innioasis 固件存档 - Innioasis 固件下载

玩家恢复·Innioasis Y1

# Innioasis Y1 更新后滚轮不工作

轮子转动但没有任何移动，或者点击轮在闪烁后立即停止响应。以下是如何区分固件故障和硬件故障以及首先要做的事情。[获取 Updater CE](../guide_zh-CN.html#platform)[Y1软件下载](../firmware_zh-CN.html?model=Y1&software=original-y1)[恢复指南](recovery_zh-CN.html)

## 判断是轮子有问题还是固件有问题

在 Y1 上，滚轮是物理输入，但固件决定每次转动和点击的作用。如果轮子在您更新或刷新播放器时停止，可能的原因是软件，而不是损坏的部件。如果它忽略您尝试的每个软件（原始软件、Rockbox 或恢复屏幕），请将其视为硬件。
  - 在一种软件中有效，在另一种软件中无效： 固件故障。
  - 在每个屏幕上都死了，包括恢复： 轮、丝带或板。
  - 只有一个方向错过了： 通常是环下有碎屑或磨损。
  - 车轮转动，但没有任何亮点： 玩家可能会被冻结——首先强制重新启动。

## 重新安装固件之前快速检查
  - 按住电源按钮约 15 秒以强制关闭播放器，然后正常启动。
  - 在主屏幕、“设置”和音乐播放器中测试方向盘。
  - 按物理按钮。如果电源和后退有反应，但车轮没有反应，则故障在于车轮本身。
  - 使用已知的数据线为播放器充电 30 分钟 - 电池电量低可能导致输入行为不稳定。
  - 如果您安装了 Rockbox 或其他自定义版本，请返回原始软件并再次测试。

## 重新安装与您的播放器匹配的 Y1 固件

由于轮子是由固件驱动的，因此通过将正确的 Y1 原始软件放回到播放器上可以修复与更新相关的故障。不要使用 Y2 包，也不要选择“足够接近”的版本 - Y1 包是为 Y1 硬件构建的，在 Y1 上构建 Y2 可能会导致控件映射错误。
  - 打开 [更新程序 CE](../guide_zh-CN.html#platform) 在您的计算机上。
  - 套装 设备型号 至 Y1.
  - 选择 原厂软件 在 软件 并选择一个稳定的 Y1 版本 - 手册包是 `rom.zip`.
  - 点击 安装 / 恢复 并让包解压。
  - 完全关闭 Y1 电源，仅在更新程序要求时连接 USB 数据线，直到出现成功消息为止。
匹配型号和版本。 如果版本列表看起来像 Y2 软件，请停止并重新选择 Y1。完整步骤位于 [Y1恢复指南](restore-original-y1_zh-CN.html).

## 检查轮环是否有碎片或损坏

如果轮子僵硬、粘住或仅在一个方向发生故障，则环和外壳之间可能会残留绒毛和砂粒。关闭播放器电源并用干燥的超细纤维布擦拭环周围。请勿将清洁剂或酒精滴入缝隙中，也不要撬起环。

如果环松动、破裂或不再发出咔嗒声，则播放器需要维修。重新安装固件无法修复损坏的轮子、断开的色带或液体损坏。

## 如果播放器也无法启动

更新失败可能导致 Y1 无法启动，这看起来像是轮子问题，因为没有任何响应。工作通过 [Y1 不会打开指南](y1-wont-turn-on_zh-CN.html) 用于充电、强制重启和手动恢复步骤。

## Innioasis Y1滚轮常见问题解答

### 为什么我的 Innioasis Y1 滚轮在更新后停止工作？

更新可能会使轮驱动程序与固件的其余部分不一致，特别是在闪存中断或使用 Y2 包的情况下。重新安装适合您的型号的 Y1 原始软件版本，并在原厂主屏幕上测试方向盘。

### 如何判断Y1点击轮是否损坏或固件有问题？

在多个软件中测试车轮。如果它在库存软件中工作但在 Rockbox 中不起作用，则这是固件映射问题。如果它在任何屏幕（包括恢复菜单）上都没有任何反应，则怀疑是轮子、功能区或主板造成的。

### 恢复原始软件会修复 Y1 滚轮吗？

它修复了由更新或不匹配的软件包引起的故障，这是首先要尝试的事情。它无法修复物理损坏的轮子、松动的色带或液体损坏。

### 我可以使用 Y2 固件包来修复 Y1 车轮问题吗？

不可以。Y1 和 Y2 套件不可互换，闪烁错误的型号可能会使控制变得更糟。在运行安装/恢复之前匹配型号和版本。

## 相关修复
  - [Y2滚轮不工作](y2-scroll-wheel-not-working_zh-CN.html) — 对 Y2 进行相同的检查
  - [Y1打不开](y1-wont-turn-on_zh-CN.html) — 电源和启动恢复
  - [Innioasis恢复指南](recovery_zh-CN.html) — 所有症状指南都集中在一处
  - [安装故障排除](../troubleshooting_zh-CN.html) — 失败的闪光灯是什么样子的
  - [恢复Y1原始软件](restore-original-y1_zh-CN.html) — 完整的恢复演练

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
