---
title: "通过全新安装修复 Innioasis 更新程序和 Y1 帮助程序 - Innioasis 更新程序"
description: "Innioasis 更新程序和 Y1 帮助程序的分步全新安装：删除剩余文件，重新安装，然后返回刷新固件。"
language: "zh-CN"
source: "https://innioasis.app/Troubleshooting/clean_install_zh-CN.html"
---

# 通过全新安装修复 Innioasis 更新程序和 Y1 帮助程序 - Innioasis 更新程序

## 确认您需要全新安装

当您看到以下任何症状时，建议手动重新安装：
  - 更新程序需要几分钟时间才能启动，或者在检查更新时停止。
  - 即使存在较新的版本，也会停止更新。
  - 设备固件更新无法下载或应用，即使它们可用。
  - 您跳过了多个版本并且已经很长时间没有使用更新程序了。

## Windows：执行全新重新安装

使用官方 Windows 安装程序在 Windows 10 或 Windows 11（64 位）上刷新更新程序。这完全取代了旧版本并恢复了自我更新通道。

在运行安装程序之前，请打开 设置 › 应用程序 › 已安装的应用程序 （或遗产 添加/删除程序 面板）并卸载 Innioasis 更新程序的任何现有副本。干净启动可以防止文件冲突。[ 下载适用于 Windows 的全新安装程序 ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)步骤1

### 下载最新的安装程序

将安装程序保存到您的下载文件夹中。如果 Innioasis 更新程序当前正在运行，请将其关闭。步骤2

### 删除任何现有安装

打开 设置 › 应用程序 › 已安装的应用程序 （或遗产 控制面板 › 添加/删除程序）并卸载 Innioasis 更新程序，以便重新安装从头开始。步骤3

### 安装并重新启动

运行您下载的安装程序 - Windows 将提示您授予权限。安装完成后，启动 Innioasis 更新程序；它现在应该自动检测 1.8.2.8 并再次获取更新。

 这还修复了启动缓慢的问题，并让更新程序再次直接从开发人员处获取固件版本。 

## macOS：使用 DMG 安装程序进行刷新

macOS 安装程序会清除旧文件并安装 1.8.2.8。[ 下载 Innioasis 更新程序 DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - 打开下载的 DMG 并展开 Finder 窗口，以便您可以看到 重新安装 选项。
  - 运行重新安装命令以刷新更新程序的现有副本。这会删除可能阻止新功能的旧帮助程序文件。
  - 从应用程序中再次启动 Innioasis 更新程序。确认“关于”面板列出的版本 1.8.2.8.
 如果重新安装后看到“Innioasis更新程序无法打开”，请转至 系统设置 › 隐私和安全 并选择 无论如何打开 批准该应用程序。 

## 更新到 1.8.2.8 后

一旦您使用最新版本，您就可以使用以下功能。这些仅适用于当前版本。
  - 一键安装 适用于原始固件、社区版本和直接从开发人员版本下载的 Rockbox 版本。
  - 清晰的引导步骤 告诉您何时连接播放器以及何时可以安全拔掉插头。
  - 两个平台的总体稳定性得到改进，启动时间也显着缩短。

 需要帮助验证您的版本吗？打开Innioasis更新程序，选择 帮助 › 关于，并确认构建显示 1.8.2.8. 

## 仍需要帮助吗？

如果全新安装失败，请捕获所有错误消息并联系 Innioasis 社区支持渠道。包括您的操作系统版本、更新程序版本（如果有）以及您已尝试过的步骤。

保持安装最新可确保您始终收到最新推出的固件包和工具。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
