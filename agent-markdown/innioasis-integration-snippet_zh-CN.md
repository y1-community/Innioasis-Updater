---
title: "嵌入 Innioasis 更新程序安装指南 - Innioasis 更新程序"
description: "将 Innioasis 更新程序安装指南添加到另一个具有响应式 iframe 嵌入和复制就绪示例的网站。"
language: "zh-CN"
source: "https://innioasis.app/innioasis-integration-snippet_zh-CN.html"
---

# 嵌入 Innioasis 更新程序安装指南 - Innioasis 更新程序

# 🚀 Innioasis 更新程序 - 可嵌入安装指南

这是一个完整的、可嵌入的安装指南小部件，可以轻松集成到任何网站中。它具有一个很酷的右下角弹出式 CTA，可以为 Windows、macOS 和 Linux 用户打开全面的安装指南。

### 🎨 美丽的设计

现代、响应式设计，适用于所有支持深色模式的设备

### 📱 跨平台

适用于 Windows、macOS 和 Linux 的完整安装指南以及分步说明

### 🔧 轻松集成

只需复制并粘贴代码片段 - 无需依赖项或复杂的设置

### 💾 智能存储

记住用户是否关闭了横幅以避免打扰

## 📋 集成说明

要将 Innioasis 更新程序安装指南添加到您的网站，只需将此代码片段复制并粘贴到您的 HTML 中： <!-- Innioasis 更新程序安装指南小部件 --> <script> (function() { // 创建并注入小部件 const script = document.createElement('script'); script.src = 'https://your-domain.com/innioasis-embed.html'; script.async = true; // 替代方案：从本地文件加载 // script.src = './innoasis-embed.html'; document.head.appendChild(script); // 创建 iframe 容器 const iframe = document.createElement('iframe'); iframe.style.cssText = ` 位置: 20px; 宽度: 400px; 边框: 无; 999999; // 使 iframe 交互 iframe.onload = function() { iframe.style.pointerEvents = 'auto'; }; </脚本> 📋复制集成代码

## 🎯替代方案：直接嵌入方法

为了更简单的集成，您可以使用 iframe 直接嵌入小部件： <!-- 直接 iframe 嵌入 --> <iframe src="https://your-domain.com/innioasis-embed.html" width="400" height="200" frameborder="0" style="position: 固定; 底部: 20px; 右: 20px; z-index: 999999; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.3);"允许透明度=“true”> </iframe> 📋 复制 iframe 代码

## 🔧 定制选项

您可以通过修改以下参数来自定义小部件： // 自定义 CTA 横幅 window.InnioasisUpdater = { // 更改横幅文本 ctaTitle: "🚀 Get Innioasis Updater", ctaDescription: "下载适合您平台的桌面应用程序", ctaButtonText: "Get Started", // 更改位置position: "bottom-right", // 或 "bottom-left", "top-right", "top-left" // 自动显示延迟（以毫秒为单位） showDelay: 3000, // 3 秒后显示 // 自定义样式 customCSS: ` .cta-banner { background: Linear-gradient(135deg, #your-color1, #your-color2); } ` }; 

## 📱 演示

单击下面的按钮查看正在运行的小部件：🎯 显示演示小部件

## 📚 包含的功能
  - 智能 CTA 横幅： 以流畅的动画显示在右下角
  - 平台检测： 自动检测用户的操作系统
  - 分步指南： 适用于 Windows、macOS 和 Linux 的完整安装说明
  - 进度跟踪： 多步骤安装的可视进度条
  - 下载集成： 所有必需文件的直接下载链接
  - 响应式设计： 在台式机、平板电脑和移动设备上完美运行
  - 深色模式支持： 自动适应用户的系统偏好
  - 用户偏好： 记住用户是否关闭了横幅
  - 辅助功能： 键盘导航和屏幕阅读器友好

## 🌐 托管要求

要在您的网站上使用此小部件，您需要：
  - 上传 `innioasis-embed.html` 文件到您的网络服务器
  - 更新集成代码段中的 URL 以指向您的服务器
  - 确保您的服务器支持 HTTPS（现代浏览器必需）
  - 在您的网站上测试小部件以确保其正常工作

## 🆘 支持

如果您需要集成此小部件的帮助或有疑问，请：
  - 检查浏览器控制台是否有任何错误消息
  - 确保所有文件都正确上传到您的服务器
  - 验证集成代码中的 URL 是否正确
  - 在不同浏览器和设备上测试

 由 Innioasis 团队使用 ❤️ 制作

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
