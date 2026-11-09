---
title: "MTKClient 和低级恢复指南 - Innioasis 和 Timmkoo - Innioasis 固件下载"
description: "使用 MTKClient 和 SP Flash Tool 为 Innioasis 和 Timmkoo 播放器提供低级 MediaTek 恢复、引导加载程序 unbrick 指令以及驱动程序诊断。"
language: "zh-CN"
source: "https://innioasis.app/mtkclient_zh-CN.html"
---

# MTKClient 和低级恢复指南 - Innioasis 和 Timmkoo - Innioasis 固件下载

高级诊断·MediaTek

# MTKClient & Unbrick 诊断

MTKClient 是 Innioasis Updater CE 使用的底层开源 MediaTek 刷新引擎。如果播放器变得无响应或标准刷新失败，请使用这些恢复诊断。[一般故障排除](troubleshooting_zh-CN.html)[驱动程序设置注意事项](drivers_zh-CN.html)

以 Innioasis Updater 开头

## 在低级别路线之前先尝试引导路线

更新程序一次性完成此操作。选择软件，按照屏幕上的步骤操作，即可完成。它还会告诉您修复或新版本何时发布。

## 了解 BootROM (BROM) 模式

当完全断电时，MediaTek MT6572 / MT6580 处理器会在加载主引导加载程序之前在 USB 总线上侦听握手数据包。如果发生损坏的闪存，BROM 模式允许完全恢复重写。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
