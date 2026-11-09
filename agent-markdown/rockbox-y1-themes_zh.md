---
title: "Rockbox-Y1 主题：使用 Updater CE 传输主题、240p 与 360p 并应用主题"
description: "如何使用 Updater CE 将主题传输到 Innioasis Y1（可用时自动推送，或在 macOS 和 Linux 上 MTKClient 刷新后引导逐步传输），以及 240p 与 360p 兼容性和应用主题。"
language: "zh"
source: "https://innioasis.app/rockbox-y1-themes_zh.html"
---

# Rockbox-Y1 主题：使用 Updater CE 传输主题、240p 与 360p 并应用主题

[← Rockbox-Y1 中心](rockbox-y1/)

Rockbox-Y1 · 主题和更新程序 CE

# Rockbox-Y1 主题：使用 Updater CE 传输，选择构建，然后选择外观

更新程序 CE 会为您处理 Rockbox-Y1 主题和字体 - 只要有可能，就会自动将它们传输到 Y1，并在无法无人值守的情况下逐步指导您完成传输（例如，在 macOS 或 Linux 上安装 MTKClient 固件后）。[获取 Rockbox 和更新程序 CE](guides/rockbox-y1.html)[浏览社区主题](https://themes.innioasis.app/)[240p 与 360p](rockbox-y1/resolution.html)

## 使用 Updater CE 将主题传输到 Y1

Rockbox 将其固件存储在 Y1 的内部闪存中，而主题、字体和用户设置则存储在隐藏的闪存中 `.rockbox` 播放器存储器（MicroSD 卡）上的文件夹。因为刷新 ROM 和将文件复制到存储使用两个不同的连接， 更新程序 CE 自动适应您的操作系统和安装方法：
  - 当Updater CE可以到达玩家时自动传输： 当您安装 360p Rockbox-Y1 版本（或在“设置”中启用自动主题同步）时，Updater CE 会在后台下载并合并精选的 360p 主题和字体包。一旦 Y1 可以到达 亚洲开发银行 （Android 调试桥）或安装为 USB驱动器 与一个 `.rockbox` 文件夹中，Updater CE 会将主题和字体直接推送到播放器，无需手动解压缩。
  - 当无法在无人值守的情况下进行引导式逐步传输时（例如 macOS 和 Linux 上的 MTKClient）： 当您使用 Rockbox 闪烁时 MTKClient 在 macOS 或 Linux 上安装方法时，当 Y1 在低级预加载器/BROM 模式下关闭电源时，会发生刷新 — 在 Rockbox 首次启动以创建之前 `.rockbox` 并且在将播放器的存储安装到您的计算机上之前。每当 Updater CE 在刷新期间无法在无人值守的情况下完成传输时，它会自动打开 安装后主题和字体助手 并引导您完成它： 
    - 首先启动 Rockbox： 如果需要，更新程序 CE 会提示您断开 USB 电缆并打开 Y1 电源，以便 Rockbox 启动一次并初始化 `.rockbox` 卡上的文件夹。
    - 通过 USB 重新连接： 将 Y1 插回您的 Mac 或 Linux PC。如果 ADB 可用，Updater CE 会检测启动的播放器并自动推送主题和字体包。
    - 或者使用 USB 存储模式和引导文件夹选择器： 如果 ADB 未激活或者您更喜欢直接存储传输，Updater CE 会引导您进入 Y1 上的 USB 存储模式，单击 选择 .rockbox 文件夹，显示隐藏文件夹（Cmd+Shift+. 在 macOS 文件对话框中或 Ctrl+H 在 Linux 上），然后选择 `.rockbox` 在 Y1 驱动器上 — 然后 Updater CE 会将所有主题和字体合并到位。

  - 按需随时添加或刷新主题： 您可以随时运行相同的自动或引导传输，而无需重新刷新固件 - 打开 Updater CE 并选择 设置 → 安装 Rockbox 360p 主题 (Cmd+T 在 macOS 上， Ctrl+T 在 Windows 和 Linux 上），或拖动单个主题 `.zip` 打包到 Updater CE 上 智能投放 窗户。

## 240p、360p，以及为何标签位于机身上

Y1 社区版本发布时带有分辨率标签，主题集合也带有相同的标签。 240p 版本与较旧的主题包具有最广泛的兼容性； 360p 版本是为较新的 Y1 主题路径制作的。安装一个并应用另一个并不危险——它只是看起来不对，有剪切的文本、丢失的元素或无法阅读的界面。

如果您还没有主题首选项，请采用较新的稳定版本及其默认主题，然后选择与其标签匹配的主题。这 [分辨率页](rockbox-y1/resolution.html) 更深入；经验法则很简单：构建标签和主题标签必须一致。

## 主题所在

主题是 MicroSD 卡上的文件，位于 `.rockbox` 文件夹 — 保存设置和缓存的同一文件夹。固件本身位于内部闪存上，因此添加、更改或删除主题不需要重新刷新。
  - 将主题自己的文件夹复制到 `.rockbox/themes` 在卡上。
  - 然后在播放器的主题设置中选择它并重新启动以查看它是否已应用。
  - 在更新版本之前保留您喜欢的主题的副本 - 它是一个文件，而不是安装。

如果看不到文件夹，请先打开隐藏文件：macOS Cmd+Shift+.、Windows 视图 → 隐藏项目、Linux Ctrl+H.

## 按顺序应用主题
  - 首先安装并启动Rockbox-Y1；主题需要运行构建。
  - 将主题文件夹复制到 `.rockbox/themes` 在卡上。
  - 打开主题设置并选择主题。
  - 重新启动，以便整个界面（而不仅仅是菜单）都能拾取它。
  - 如果它看起来坏了，请选择另一个主题；如果您想稍后重试，这些文件仍然存在。

## 撤消破坏界面的主题

如果播放器启动后出现无法使用的情况，您无需重新安装固件。重命名或删除 `.rockbox` 卡上的文件夹并启动播放器：构建使用默认设置和默认主题重新创建文件夹。您的音乐不会受到影响，您可以稍后将您想要的主题复制回来。[.rockbox 文件夹](rockbox-y1/sd-card.html)[第一次开始](rockbox-y1/first-start.html)[更新构建](rockbox-y1/update.html)

## 人们提出的问题为什么 Updater CE 在 macOS 或 Linux 上安装 MTKClient 后会引导我传输主题？

当您的 Y1 在低级预加载器/BROM 模式下断电时，Rockbox 启动以初始化之前，MTKClient 将 Rockbox ROM 闪存到内部存储器 `.rockbox` 文件夹并在 MicroSD 卡安装到您的计算机上之前。只要 Updater CE 可以直接到达启动的播放器（通过 ADB 或安装的 USB 驱动器），它就会自动传输主题；如果在刷新过程中无法在无人值守的情况下执行此操作，它会在刷新后立即打开引导主题和字体步骤，以帮助您打开 Y1 电源并通过 ADB 或 USB 存储模式完成传输。Y2 主题适用于 Y1 吗？

不。端口是独立的，Y2 上的主题支持遵循其测试版本。看 [Rockbox-Y2 主题](rockbox-y2-themes_zh-CN.html).主题在更新后还能继续存在吗？

通常是的，因为它们位于卡上并且闪存写入 ROM。如果新版本更改了主题路径，请重新应用与其标签匹配的主题。为什么主题只应用了一半？

重新启动通常可以解决该问题。如果不是，则主题的文件不完整 - 重新复制其文件夹而不是编辑单个文件。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
