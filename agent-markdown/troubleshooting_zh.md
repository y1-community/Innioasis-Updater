---
title: "Innioasis 更新程序疑难解答 | Innioasis 和 Timmkoo 安装问题 - Innioasis 更新程序"
description: "修复 Innioasis 更新程序安装在任何 Innioasis 或 Timmkoo 播放器上的问题。检查型号、电缆、驱动程序、关机时间以及安装停止的位置 - 然后让它再次闪烁。"
language: "zh"
source: "https://innioasis.app/troubleshooting_zh.html"
---

# Innioasis 更新程序疑难解答 | Innioasis 和 Timmkoo 安装问题 - Innioasis 更新程序

故障排除

# 找到安装停止的点。

停在哪里了？这会告诉您要修复什么。[返回正常引导](guide_zh-CN.html)[检查固件](firmware_zh-CN.html)

## 它在 USB 提示符之前停止

这是计算机问题，而不是电缆问题。检查您的型号。再次解压文件。然后尝试 安装 / 恢复。如果发布列表为空，则打开 [固件目录](firmware_zh-CN.html).

## 无法连接到播放器
  - 完全关闭正确的 Y1 或 Y2 的电源。
  - 拔下电缆，关闭其他闪存或 Android 工具，然后重新开始安装。
  - 仅当更新程序表示已准备就绪时才连接。
  - 如果可能，请直接在计算机中使用短的 USB 数据线，而不是集线器。
  - 在 Windows 上，重新安装 MediaTek 驱动程序并重新启动。在 Linux 上，检查 USB/serial 权限。
更新程序连接提示实时更新程序提示对于当前型号和平台具有权威性。

## 检测到播放器但闪光失败

停在这里。不要尝试不同的模型。关闭其他工具，检查您选择了正确的Y1或Y2，如果播放器无法启动，请使用匹配的原始软件。 [SP Flash Tool](sp-flash-tool_zh-CN.html) 和 MTKClient 如果您需要的话，它们也包含在内，并且文件位于 [固件页面](firmware_zh-CN.html).

## Windows 驱动程序注释

由于核心隔离，某些 Windows 安装会阻止 MediaTek 驱动程序。在更改内存完整性之前，请遵循当前的 Windows 安全指南，并在完成后将其重新打开（如果系统允许）。[打开司机指南](drivers_zh-CN.html)[清洁安装指南](Troubleshooting/clean_install.html)

## 轮子不工作，或者播放器将无法启动

输入和电源故障需要采取与闪存故障不同的步骤。这些指南涵盖了常见的 Y1 和 Y2 情况。[Y1滚轮](guides/y1-scroll-wheel-not-working.html)[Y2滚轮](guides/y2-scroll-wheel-not-working.html)[Y1打不开](guides/y1-wont-turn-on.html)[Y2打不开](guides/y2-wont-turn-on.html)[恢复指南](guides/recovery.html)

## 还卡住了吗？

寻求帮助时，请包括型号、操作系统、确切的更新程序消息、是否检测到播放器以及您选择的包/项目。不要发布私人令牌或无关的系统文件。[求人](https://discord.gg/zHrT2zrcek)[支持维修](support_devs_zh-CN.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
