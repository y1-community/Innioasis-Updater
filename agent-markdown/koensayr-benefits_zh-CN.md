---
title: "为什么 Koensayr 适合您的 Innioasis Y1 | Koensayr 优点 - Innioasis 固件下载"
description: "Koensayr 修补库存 Y1 固件：艺术家到专辑导航和 AVRCP 1.3 蓝牙元数据以及汽车音响的控件，无需更改界面。"
language: "zh-CN"
source: "https://innioasis.app/koensayr-benefits_zh-CN.html"
---

# 为什么 Koensayr 适合您的 Innioasis Y1 | Koensayr 优点 - Innioasis 固件下载

定制软件·Koensayr

# 为什么 Koensayr 适合您的 Innioasis Y1

Koensayr 保留您熟悉的界面并修复令您烦恼的问题。按艺术家浏览音乐，蓝牙显示曲目名称并与您的汽车控件配合使用。[在更新程序中获取 Koensayr](guide_zh-CN.html?model=Y1&software=koensayr-y1)[Y1安装页面](koensayr-y1-software_zh-CN.html)

## 型号可用性

哪些 Innioasis 型号运行它？[Y1 · 可用](koensayr-y1-software_zh-CN.html)Y2 · 不可用

Y1 和 Y2 版本是分开的，因此请在软件下载中获取为您的播放器制作的版本 - 切勿将其中一个替换为另一个。

## 为什么人们选择它

保留库存玩家。修复烦人的部分。
  - 艺术家 → 专辑导航 - 库存音乐应用程序获得了它所缺少的艺术家到专辑的流程 - 不再需要挖掘文件夹。
  - 可在车内使用的蓝牙 — 符合规范的 AVRCP 1.3 元数据和控件：您的主机可以看到曲目标题、播放头和重复/随机播放状态。
  - 真正配对的配对 - 针对汽车音响和耳机调整的音频和配对配置，包括自动配对修复。
  - 当你需要的时候root — 安装了最小的 setuid su 用于 adb 升级 — 对于诊断和修补很有用。
  - 减少臃肿 — 从未使用的系统应用程序被删除以释放 RAM 并减少后台工作。
  - 无学习曲线 — 该接口是Y1接口。 Koensayr 改变的是行为，而不是外表。

## 社区

社区怎么说

Koensayr 是为那些喜欢现有的 Y1 界面并且只是希望修复令人沮丧的地方的人而设计的软件。它的名字是《星球大战》的深切——Koensayr建造了Y翼，Y翼通向Y1。

社区中最受关注的胜利是蓝牙：汽车音响和耳机上的正确轨道元数据和控制（AVRCP 1.3），这是众所周知的库存软件错误。如果您住在车里，人们就会向您推荐这款软件。
  - [r/innioasis · Koensayr 和车载蓝牙](https://www.reddit.com/r/innioasis/)

## 该项目提供什么
  - 艺术家 → 专辑导航已修补到系统音乐中 APK
  - AVRCP 1.3 元数据和控制：完整曲目元数据、毫秒精度播放头、曲目和电池通知以及双向重复/随机播放
  - 蓝牙配对修复：针对汽车和耳机配对的audio.conf、auto_pairing.conf、blacklist.conf 和 build.prop 编辑
  - 通过最小的 setuid su 进行 root 访问以进行 adb 升级；库存 adbd 保持不变
  - 系统 debloat — 删除了预装的臃肿软件
  - build.prop 中可选的 ADB 支持
  - 用于调查真实硬件上蓝牙行为的诊断工具

## 首先要知道的事情
  - 目前仅 Y1，并且它保留了库存界面 - 它是一个修补程序，而不是启动器
  - 这是最具技术性的路线：补丁程序在Linux主机上运行并通过MTKClient刷新，因此它适合有信心的用户
  - 该项目仅修补已知的库存软件 - 检查您的软件版本是否匹配
  - 如果您改变主意，恢复模型的原始软件仍然是可行的方法

## 开始使用

在更新程序中选择 Y1，选择 Koensayr，然后按照发行说明进行操作。本教程按顺序介绍修补程序流程。[浏览 Koensayr 版本](firmware_zh-CN.html?model=Y1&software=koensayr-y1)[Y1教程](guides/koensayr-y1.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
