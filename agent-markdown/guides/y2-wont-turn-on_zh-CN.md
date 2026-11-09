---
title: "Innioasis Y2 无法打开 | Innioasis 固件存档 - Innioasis 固件下载"
description: "Innioasis Y2 无法开机或充电？强制重新启动，检查计算机是否发现它，然后恢复 Y2 固件或使用手动 SP Flash Tool 恢复。"
language: "zh-CN"
source: "https://innioasis.app/guides/y2-wont-turn-on_zh-CN.html"
---

# Innioasis Y2 无法打开 | Innioasis 固件存档 - Innioasis 固件下载

玩家恢复·Innioasis Y2

# Innioasis Y2 无法开启

黑屏并不总是意味着玩家死亡。在尝试手动闪光之前，请先完成充电、强制重启和计算机检测。[获取 Updater CE](../guide_zh-CN.html#platform)[固件下载](../firmware_zh-CN.html)[恢复指南](recovery_zh-CN.html)

## 先给 Y2 正确充电

大多数“Y2 无法开机”报告是电池没电、仅充电的电缆或无法提供足够电流的充电器。严重耗尽的 Y2 可能需要 20 到 30 分钟才能在屏幕上显示任何内容。
  - 使用已知的 USB 数据 电缆，而不是仅充电电缆。
  - 尝试使用壁式充电器，然后直接使用计算机 USB 端口 - 而不是集线器。
  - 将其保持连接 30 到 60 分钟，然后观察充电图标或背光。
  - 在继续之前尝试使用第二根电缆和充电器。

## 强制重启

按住电源按钮约 15 秒钟，松开，等待五秒钟，然后按电源一次。这会清除挂起的启动，并且可以安全地重复。

如果屏幕显示徽标然后变黑，则表示播放器正在启动但出现故障 - 跳到下面的固件恢复。如果没有任何反应，请保持充电状态，半小时后重试。

## 检查电脑是否可以看到播放器

用数据线连接已关闭电源的Y2，并在Windows上打开设备管理器， `lsusb` 在 Linux 上，或在 macOS 上 MTKClient。正在运行的播放器显示为具有供应商 ID 的 MediaTek 设备 `0e8d`。如果出现，则即使屏幕保持黑暗，硬件也足够活跃以重新闪烁。

如果没有出现任何内容，请先在 Windows 上安装 MediaTek 驱动程序 — [司机指南](../drivers_zh-CN.html) 涵盖 Windows 和 Linux 权限。

## 恢复 Y2 库存固件

如果检测到播放器但无法启动，请重新安装 Y2 原始软件。仅使用 Y2 包； Y1 构建不会在 Y2 硬件上启动。
  - 打开 [更新程序 CE](../guide_zh-CN.html#platform) 在您的计算机上。
  - 套装 设备型号 至 Y2.
  - 选择 原厂软件 在 软件 并选择一个稳定的 Y2 版本 - 手册包是 `rom_y2.zip`.
  - 点击 安装 / 恢复 并让包解压。
  - 完全关闭 Y2 电源，仅在更新程序要求时连接 USB 数据线，直到出现成功消息为止。
保持电源稳定。 闪光灯断电可能导致播放器无法使用。先充电，然后直接连接电脑。

## 当更新程序无法看到播放器时手动恢复

更新程序 CE 包含手动恢复工具，用于指导安装无法完成的情况。 [SP Flash Tool](../sp-flash-tool_zh-CN.html) 捆绑在 Windows 和 Linux x86 上，MTKClient 路线涵盖 macOS。两者都需要来自 [固件下载](../firmware_zh-CN.html) 页。

请遵循适合您平台的工具指南，而不是即兴创作分散文件或偏移。如果任何工具均未检测到播放器，则故障可能出在电池、充电端口或主板上。

## 如果仍然无法启动

停止闪烁并将其视为硬件。请勿打开外壳或按压电池。询问社区的型号、屏幕的用途、计算机是否检测到它以及您尝试过哪些软件包 - [Discord 社区](https://discord.gg/zHrT2zrcek) 可以帮助确定服务路线。

库存恢复会取代系统，因此在刷新之前请备份播放器内存中存储的所有内容。恢复不会影响 MicroSD 卡上的音乐。

## Innioasis Y2电源常见问题解答

### 为什么我的 Innioasis Y2 无法打开？

通常的原因是电池完全耗尽、仅充电的电缆或充电器电量不足、固件崩溃导致启动停止或硬件故障。在假设玩家死亡之前，使用已知的数据线为其充电 30 分钟。

### 如何强制重启 Innioasis Y2？

按住电源按钮约 15 秒钟，松开，等待五秒钟，然后按电源一次。如果没有任何反应，请保持充电状态，并在 30 分钟后重试。

### 我可以恢复无法开机的 Y2 吗？

经常是的。如果计算机仍然检测到 MediaTek 设备，请使用 Updater CE 重新安装 Y2 原始软件包。如果未检测到，请使用 Updater CE 附带的 SP Flash Tool 或 MTKClient 恢复以及与型号匹配的 Y2 固件文件。

### Y2 刷机前需要充电吗？

是的。闪光灯断电可能导致播放器无法使用。首先为其充电，然后将其直接连接到计算机，而不是通过集线器。

## 相关修复
  - [Y1打不开](y1-wont-turn-on_zh-CN.html) — 对 Y1 进行相同的检查
  - [Y2滚轮不工作](y2-scroll-wheel-not-working_zh-CN.html) — 如果它启动但轮子不启动
  - [Innioasis恢复指南](recovery_zh-CN.html) — 所有症状指南都集中在一处
  - [SP Flash Tool 指南](../sp-flash-tool_zh-CN.html) — Windows 和 Linux 上手动刷新
  - [安装故障排除](../troubleshooting_zh-CN.html) — 失败的闪光灯是什么样子的

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
