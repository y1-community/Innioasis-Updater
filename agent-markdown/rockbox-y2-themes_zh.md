---
title: "Rockbox-Y2 主题：在 Y2 上安装和重置主题"
description: "如何在 Innioasis Y2 上安装、管理和重置 Rockbox-Y2 主题：主题位于 .rockbox 文件夹中的位置以及如何检查构建兼容性。"
language: "zh"
source: "https://innioasis.app/rockbox-y2-themes_zh.html"
---

# Rockbox-Y2 主题：在 Y2 上安装和重置主题

[← Rockbox-Y2 中心](rockbox-y2/)

Rockbox-Y2 · 主题

# Rockbox-Y2 主题

如何在 Rockbox-Y2 上安装主题，检查主题与已安装版本的兼容性，并在主题无法正常显示时重置主题。[Rockbox-Y2 发行说明](release-notes/rockbox-y2/index.html)[浏览社区主题](https://themes.innioasis.app/)[安装Rockbox-Y2](rockbox-y2/install.html)

## 检查您的构建的主题兼容性

Rockbox-Y2 与 Y1 端口分开开发，因此主题兼容性遵循您安装的 Y2 构建版本。检查 [Rockbox-Y2 发行说明](release-notes/rockbox-y2/index.html) 在安装主题包之前先选择您的版本。

看 [Rockbox-Y1 与 Rockbox-Y2](rockbox-y1-vs-y2_zh-CN.html) 对两个端口进行全面比较。

## 如何在 Y2 上安装主题

主题存储在隐藏的 MicroSD 卡上 `.rockbox` 文件夹。
  - 至少启动 Rockbox-Y2 一次，以便创建 `.rockbox` 您的 MicroSD 卡上的文件夹。
  - 将主题文件提取或复制到 `.rockbox/` （所以 `themes`, `wps`, `fonts`, 和 `backdrops` 合并到 `.rockbox/`).
  - 在播放器上，打开 设置 → 主题设置 → 浏览主题文件 并选择您的主题。

要查看计算机上的隐藏文件夹：按 Cmd+Shift+. 在 macOS 上，启用 查看 → 隐藏项目 在 Windows 上，或按 Ctrl+H 在 Linux 上。

## 如何重置损坏的主题

如果主题使屏幕难以阅读，请重命名或删除该主题 `.rockbox` 您的 MicroSD 卡上的文件夹并重新启动播放器。 Rockbox-Y2将创造一个新的 `.rockbox` 具有默认主题的文件夹，同时保持音乐完好无损。[.rockbox 文件夹](rockbox-y2/sd-card.html)[正在更新 Rockbox-Y2](rockbox-y2/update.html)[Rockbox-Y2 构建注释](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
