---
title: "恢复 Timmkoo Q5 上的原始软件 - 分步"
description: "如何使用经过验证的 rom_q5.zip 软件包，使用 Innioasis 更新程序 CE 或 SP Flash Tool 在 Timmkoo Q5 上恢复官方原始软件。"
language: "zh-CN"
source: "https://innioasis.app/guides/restore-original-q5_zh-CN.html"
---

# 恢复 Timmkoo Q5 上的原始软件 - 分步

恢复指南·TimmkooQ5

# 恢复 Timmkoo Q5 上的原始软件

完全回归播放器附带的软件。在更新失败后、出售播放器之前或自定义系统不适合您时使用它。[获取 Updater CE](../guide_zh-CN.html#platform)[Q5下载](../firmware_zh-CN.html?model=Q5)[Q5 手册](../manuals/q5.html)

适用于您的计算机的安装指南

## 使用计算机恢复 Q5 上的原始软件

选择适合您正在使用的计算机的指南。 每个版本都有平台设置、Updater CE步骤和返回库存的方式。[Windows 指南](/install/original-q5-windows.html)[macOS 指南](/install/original-q5-mac.html)[Linux指南](/install/original-q5-linux.html)

[所有 Timmkoo Q5 指南](/install/q5.html) · [所有原始软件指南](/install/original-software.html)

## 你需要什么
  - Windows、macOS 或 Linux 计算机。 Updater CE 在所有三个上运行。
  - 播放器附带的USB数据线。仅充电电缆将不起作用。
  - 官方 `rom_q5.zip` 包，更新程序为您下载，或从 [Q5 存档](../firmware_zh-CN.html?model=Q5) 如果您喜欢手动闪光。
  - 在播放器中充电。断电恢复是使糟糕情况变得更糟的唯一常见方法。

这会替换系统并擦除内部存储。 首先将音乐、录音和照片复制到计算机上。

## 路线A：Updater CE（推荐）
  - 安装 [Innioasis 更新程序 CE](../guide_zh-CN.html#platform) 并打开它。
  - 套装 设备型号 至 Q5。该模型必须与玩家完全匹配。
  - 选择 原厂软件 在软件列表中。
  - 选择一个版本。最新的稳定版本是安全的默认版本。
  - 新闻 安装 / 恢复 并等待包下载和解压。
  - 完全关闭播放器电源，然后仅在更新程序要求时连接 USB 电缆。
  - 在出现成功消息之前，请勿触摸播放器或电缆。断开连接并启动播放器。
切勿选择不同的模型来“使其发挥作用”。 Q5 需要 Q5 包。混合模型是玩家最终需要手动恢复的原因。

## 路线 B：SP Flash Tool（手动）

当计算机无法运行 Updater CE 时，或者当您已经拥有该软件包并且更喜欢经典工具时，请使用此选项。
  - 下载 `rom_q5.zip` 从 [Q5 存档](../firmware_zh-CN.html?model=Q5) 并解压它。
  - 将分散文件保留在图像旁边。请勿重命名或移动图像。
  - 打开SP Flash Tool，选择 仅供下载，并加载分散文件。
  - 关闭播放器电源，按 下载，然后连接电缆。
  - 等待绿色成功标记后再断开连接。

的 [SP Flash Tool 指南](../sp-flash-tool_zh-CN.html) 更详细地介绍了驱动程序和 Windows 提示。在 Linux 和 macOS 上，Updater CE 是更简单的路线，因为它带来了自己的 USB 处理。

## 恢复后
  - 断开播放器并让它自行启动。
  - 选择您的语言并设置时钟。
  - 如果您使用 Wi-Fi 或蓝牙，请重新连接它们。
  - 将您的音乐复制回来。的 [转乘指南](../manuals/transfer-music.html) 有文件夹名称。

如果播放器启动但屏幕、滚轮或按钮仍然出现故障，则恢复成功；这是硬件或设置问题，而不是软件问题。的 [故障排除指南](../troubleshooting_zh-CN.html) 是下一站。

## 如果不起作用

### 更新者永远看不到玩家

更换电缆，然后更换 USB 端口。避免枢纽。在 Windows 上，从以下位置安装 MediaTek 驱动程序 [驱动程序页面](../drivers_zh-CN.html).

### 闪光灯提前停止

重新连接，为播放器充电，然后重新开始。请勿切换至不同型号的封装。

### 玩家保持黑色

充电一小时，然后保持电量十秒钟。如果它仍然死了，请阅读 [恢复指南](../guides/recovery_zh-CN.html) 再次尝试之前。

## 人们提出的问题

### 这会删除我的音乐吗？

是的，内部存储已被删除。 microSD 卡上的文件通常会保留下来，但首先将它们复制到安全的地方。

### 之后我可以返回Rockbox吗？

是的。恢复原始软件不是一扇单向门；而是一扇单向门。您的型号的自定义软件页面可以再次安装。

### 我需要 Type A / Type B 设置吗？

只有 Y1 有这样的选择，并且仅限于原始软件。所有其他模型都使用单个包。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
