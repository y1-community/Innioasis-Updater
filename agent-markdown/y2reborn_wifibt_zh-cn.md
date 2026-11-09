---
title: "Reborn (Y2Linux) - Innioasis 更新程序的 Wi-Fi、蓝牙和 FM 收音机设置"
description: "Innioasis Y2 上的 Reborn (Y2Linux / Y2Reborn) 的简短安装后指南：复制 system.img，然后设置 Wi-Fi、蓝牙和 FM 收音机。"
language: "zh-cn"
source: "https://innioasis.app/y2reborn_wifibt_zh-cn.html"
---

# Reborn (Y2Linux) - Innioasis 更新程序的 Wi-Fi、蓝牙和 FM 收音机设置

Innioasis Y2 · Reborn 安装后

# 设置 Wi-Fi、蓝牙和 FM 收音机。

将一个文件复制到您的播放器。 Reborn 处理剩下的事情。[下载系统.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[安装指南](guides/reborn-y2linux-y2.html)[为什么是Y2Reborn？](reborn-y2linux-benefits_zh-CN.html)

## 为什么是这个文件？

Wi-Fi、蓝牙和 FM 收音机需要五个 MediaTek 固件模块，Reborn 无法发货。他们在官方内部 Y2 `system.img`。 Reborn 提取它们一次，检查它们，然后删除文件。

## 设置
  - 下载系统.img

下载v3.2.0 FM `system.img` 到您的计算机。[ 下载系统.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - 启动 Reborn 一次

打开播放器。等待 设置存储 完成，然后重新启动一次。
  - 连接到您的计算机

使用 USB 数据线。播放器显示为 内部存储.在 Mac 上？

安装 [开放MTP](https://openmtp.ganeshrvel.com/) 浏览播放器。 Windows 和 Linux 自动挂载它。
  - 将 system.img 复制到固件

创建一个名为的文件夹 `Firmware` 在内部存储的根目录下。复制 `system.img` 进入其中。
  - 等待设置完成

Reborn 自动安装无线电固件并删除 `system.img`。这大约需要 10-20 秒。等待 Wi-Fi 和蓝牙已准备就绪.
  - 连接 Wi-Fi、蓝牙和 FM 收音机
    - 无线上网： 设置→系统→网络→Wi-Fi。选择您的 2.4 GHz 网络。
    - 蓝牙： 将耳机置于配对模式。设置 → 蓝牙 → 选择它们。
    - 调频收音机： 插入有线耳机作为天线，然后打开 FM 收音机。

  - 通过 Wi-Fi 更新

未来的 Reborn 更新从设置 → 系统 → 软件更新安装。您的无线电固件保持不变。

## 本指南有帮助吗？

您觉得这个安装后设置指南有帮助吗？ 是的，有帮助！ [ 需要有关 Discord 的帮助 ](https://discord.gg/zHrT2zrcek) 感谢您的反馈！在 Y2Reborn 上享受无线聆听。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
