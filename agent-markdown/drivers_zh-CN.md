---
title: "Innioasis Y1 和 Y2 USB 驱动程序 | Windows 驱动程序和 Linux 权限 - Innioasis 更新程序"
description: "设置您的计算机的 Innioasis 更新程序：Windows MediaTek 驱动程序和 Linux USB 权限 - 以及电缆和计时修复。"
language: "zh-CN"
source: "https://innioasis.app/drivers_zh-CN.html"
---

# Innioasis Y1 和 Y2 USB 驱动程序 | Windows 驱动程序和 Linux 权限 - Innioasis 更新程序

电脑设置

# 在播放器之前先准备好计算机。

大多数连接问题来自驱动程序、权限、电缆或计时。 Windows 需要安装 MediaTek 驱动程序。 Linux 需要正确的 USB 权限。在下面找到您的平台。[获取 Updater CE](guide_zh-CN.html#platform)[故障排除](troubleshooting_zh-CN.html)

## Windows
  - 下载下面的 MediaTek 驱动程序安装程序。
  - 运行安装程序并允许 Windows 安装驱动程序。
  - 重新启动计算机。
  - 打开 Updater CE 并等待连接提示，然后再插入已关闭的播放器。

某些 Windows 系统通过核心隔离（内存完整性）来阻止驱动程序。如果重新启动后 Updater CE 仍然无法看到播放器，请在 Windows 安全性中关闭内存完整性，重新启动并重新安装驱动程序。如果系统允许，完成后请重新打开该设置。

Windows 无法启动该应用程序？ 如果 Windows 安全或智能应用程序控制阻止 Updater CE 打开，请打开 设置 （按 Win + I) → 隐私与安全 → Windows Security → 应用程序和浏览器控制 → 智能应用程序控制设置 并将其设置为 离开。智能应用程序控制目前正在影响流行的应用程序，例如 Epic Overlay Service（Fortnite 所用）——Updater CE 安全且经验证。如需日后重新启用，请将 `VerifiedAndReputablePolicyState` 至 `1` （开）或 `2` （评估模式）下 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 在注册表编辑器中。[下载 Windows 驱动程序](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[返回主要指南](guide_zh-CN.html#windows) · [软件下载](firmware_zh-CN.html)

## Linux USB 权限

Linux 需要允许您的用户帐户与播放器内的 MediaTek USB 芯片对话。更新程序 CE 通常会在安装过程中解决此问题，并且相同的权限涵盖 SP Flash Tool，因此请将其视为修复步骤而不是正常阶段。
  - 以普通用户身份（而不是 root 用户）运行 Updater CE。安装程序仅在需要时才请求管理员访问权限。
  - 检查玩家是否被看见。关闭播放器电源，连接电缆，然后在终端中运行 lsusb 命令。连接的播放器显示为 MediaTek 设备，供应商 ID 为 0e8d。
`lsusb`
  - 如果它出现在 lsusb 中，但 Innioasis 更新程序 CE 或 SP Flash Tool 表示权限被拒绝或无法打开端口，则您的用户无法访问 USB 设备。相同的 udev 规则涵盖这两种工具，因此请添加一个让用户组读取它的规则。
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

将该行保存到名为 /etc/udev/rules.d/51-innioasis.rules 的新文件，然后运行：`sudo udevadm control --reload && sudo udevadm trigger`
  - 完全拔掉播放器的插头，重新插入，然后再次尝试安装。
  - 如果 SP Flash Tool 报告串行权限或端口争用，请完全拔出插头并仅在出现提示时重新连接。
不要临时调整闪光偏移。如果您转向手动恢复工具，请使用项目附带的文件和特定于模型的配置。

[返回主要指南](guide_zh-CN.html#linux) · [软件下载](firmware_zh-CN.html) · [SP Flash Tool 指南](sp-flash-tool_zh-CN.html)

## 电缆和时序
  - 使用已知的 USB 数据线。
  - 故障排除时避免使用集线器。
  - 完全关闭正确型号的电源。
  - 仅在出现提示时连接。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
