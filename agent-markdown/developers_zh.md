---
title: "开发商|将自定义固件添加到 Innioasis 更新程序 CE - Innioasis 固件下载"
description: "用于将自定义 Innioasis Y1 或 Y2 固件添加到 Updater CE 的开发人员文档：分叉存储库、发布 rom.zip 资产、编辑 slidia_manifest.xml、测试并打开拉取请求。"
language: "zh"
source: "https://innioasis.app/developers_zh.html"
---

# 开发商|将自定义固件添加到 Innioasis 更新程序 CE - Innioasis 固件下载

对于固件开发人员

# 将您的固件添加到 Updater CE。

Updater CE 是自定义固件的社区目录和安装程序。从基础 ROM 开发您的项目，将其发布为具有正确发布资产的公共存储库，将模型条目添加到 `slidia_manifest.xml`，测试模型过滤器，并打开拉取请求。一个存储库可以为其支持的每种模型提供服务。[查看Updater CE源](https://github.com/y1-community/Innioasis-Updater)[浏览软件下载](firmware_zh-CN.html)

## 从基础开始 ROM

基础 ROM 为定制固件开发人员提供了一个干净的 Android 基础，并启用了无线射频芯片。在 Y1 上，它们支持 Wi-Fi 和 GPS 以及工厂蓝牙和 FM；在 Y2 上，它们支持 Wi-Fi、GPS 和 FM 以及工厂蓝牙。用于自定义固件开发的基础 ROM 下载，其中每一项都支持 Android 版本和无线功能[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| 下载 | 设备 | Android | 无线功能 |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | 将 Wi-Fi 和 GPS 添加到出厂蓝牙和 FM（出厂时 FM 已在 Y1 上运行）。适用于搭载 OS 2.0.0 或更高版本的 Y1 播放器。 |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | 将 Wi-Fi 和 GPS 添加到出厂蓝牙和 FM（出厂时 FM 已在 Y1 上运行）。适用于操作系统早于 2.0.0 的 Y1 玩家。 |
| rom_y2.zip | Y2 | Android 4.4.2 | 为工厂蓝牙添加 Wi-Fi、GPS 和 FM。 Y2 无线电芯片已完全启用，因此 FM 也可在此处使用。 |

这些图像是启用了设备无线无线电的库存 Android 基础 (AOSP)，因此自定义固件可以添加网络功能，而不是替换无线电堆栈。它们是以下发布步骤的实际起点。

## 使用这些发布资产名称

文件名是兼容性信号的一部分。保持名称准确，并将 ZIP 文件放入项目的发布资产中，而不仅仅是存储库源树中。固件 ZIP 资产名称和支持的设备``````

| 资产 | 设备 | 硬件 | 意义 |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 附带操作系统 2.0.0 或更高版本的设备。 |
| rom_type_b.zip | Y1 | Type B | Y1 附带 2.0.0 之前操作系统的设备。 |
| rom_y2.zip | Y2 | Y2 | Y2 完整安装包。将其与 Y1 资产分开。 |
不要重命名包以使其适合另一个模型。 Y1 和 Y2 使用不同的 MediaTek 平台文件和刷新配置。发布其实际支持的硬件的包。

## 连接如何运作

更新程序 CE 读取清单作为其目录。每个 `<package>` 该行告诉它项目名称、存储库、模型和处理程序。当用户选择该项目时，更新程序会检查存储库的已发布版本并查找 `rom*.zip` 资产。

### 显现

命名项目并将其映射到模型。 Y1 和 Y2 需要单独的行，即使它们共享存储库。

### 已发布版本

包含可安装的 ZIP 资产。单个版本可能包含 Y1 Type A、Y1 Type B 和 Y2 包。

### 更新程序CE安装

使用选定的型号来选择匹配的封装和特定于型号的闪存路径。用户不必猜测文件名。

## 发布项目只需五步
  - 分叉 Updater CE 存储库。 创建您自己的分叉 [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)，然后在本地克隆您的分叉。
  - 准备公共固件存储库。 确保存储库是公共的并且其版本包含正确的 ZIP 资产。你可以把 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip` 当它们属于同一版本时在同一版本上。
  - 编辑清单。 打开 `slidia_manifest.xml` 在 Updater CE 分支的根目录中。为该版本支持的每个模型添加一行（Y1 和 Y2 是公共对）。这 `repo` 值是存储库的 `owner/repository`; `url` 是公共项目页面。
  - 测试目录。 从编辑后的结账中运行更新程序。选择 Y1 并确认项目显示 Y1 资产。选择 Y2 并确认其显示 Y2 版本。当Type A和Type B都发布时，分别检查。
  - 打开拉取请求。 将清单更改推送到您的分支，并针对上游 Updater CE 存储库打开拉取请求。包括项目链接、支持的型号、发布标签、资产名称和您测试的设备。

## 生成您的清单行

填写存储库并勾选该版本支持的每个模型。生成器写一个 `<package>` 每个模型行，仅包含您设置的属性，因此结果与当前匹配 `slidia_manifest.xml` 格式。下面提供了 Updater CE 读取的每个属性 - 可选属性位于 更多选择.存储库网址公共 GitHub 存储库。生成器提取 `owner/repository` 从网址。软件名称显示在应用程序和网站目录中。项目网址项目或其发行说明的面向人的页面。品牌清除此项可使用模型的默认品牌。 SR1、Q3、Q5 和 Q3e 是 Timmkoo 模型。设备（每条线）Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3e其他型号对于上面未列出的型号。已知型号保留其目录拼写。旗帜`do_not_keep_data` — 切勿为此固件提供保留数据由原始软件构建 - 补充 `derivative="y1-community/y1-stock-rom"`

仅当传入固件与已安装固件相同或共享一个固件时才提供保留数据 `derivative` 根。仅当用户数据确实无法保留时才使用该标志。更多选项：图标、艺术品、发布资源、安装后和镜像

#### 图标和艺术品图标文件选择您将提交到存储库的图像。这将预览它并构建其原始 URL；它不上传任何东西。存储库中的图标路径已提交映像的路径，相对于存储库根目录。图标分支图标网址直接图像 URL。当为空时，应用程序使用版本的 `updater.png` 或生成的图标。选定的图标预览

深色模式图标 URL可选的深色主题图标。 `image_dark` 是一个可接受的别名。灯光艺术作品网址二次艺术作品，在发布图像后尝试过 `icon`.深色艺术作品网址

#### 释放资产发布资产名称每个选定型号都有一个名称。留空即可使用 `rom.zip` 在 Y1 上和 `rom_<model>.zip` 别处。资产格局当发行版的 zip 未命名时使用 Glob `rom*.zip`.Type A 资产当 Y1 Type A 包的名称没有说明时，使用 Glob 表示。Type B 资产当 Y1 Type B 包的名称没有说明时，使用 Glob 表示。最低应用版本隐藏旧版 Updater CE 版本中的条目。

#### 链接、镜像和 Keep Data 系列安装后页面安装成功后打开。第二个安装后页面多页设置指南的可选第二步。便携式拉链镜子逗号分隔 `*-mirror` 构建 Portable Flashing Zip 包的存储库。衍生品存储库此版本所基于的固件。相关固件共享一个数据分区，这就是Keep Data检查的内容。信息库应用程序存储库，其版本描述了此固件中的应用程序。它还需要一个安装后页面。APK 存储库应用程序存储库，其 APK 应用程序在固件之后下载并安装。

#### 目录附加内容蛞蝓链接和保存的安装记录的稳定标识符。当选择多个模型时，模型会自动附加。描述`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`复制行

正在加载最新的清单...预览添加了您的行的最新清单

发电机获取电流 `slidia_manifest.xml` 来自此存储库并在之前插入您生成的行 `</slidia>`.

对于共享存储库来说，一行是不够的。 如果缺少 Y2 行，Y2 用户即使在 `rom_y2.zip` 存在于项目的发布中。对于您的版本支持的所有其他模型也是如此。

### 清单读取的每个属性

这些是当前 Updater CE 版本理解的属性。生成器仅写入您填写的内容；该应用程序对于其余部分将回退到合理的默认值。slidia_manifest.xml包属性及其含义``````````````````````````````````````````````````````````````````````````````````````````````

| 属性 | 需要 | 它的作用 |
| --- | --- | --- |
| name | 是的 | 软件名称显示在目录和安装卡上。 |
| repo | 是的 | owner/repo。该应用程序读取该存储库的 GitHub 版本。 |
| device | 是的 | 目标型号，大写（Y1, Y2, G1, Q3e，……）。每个模型保留一个条目。 |
| url | 受到推崇的 | 从目录中打开的项目页面或发行说明。 |
| type, handler | 实践中是的 | type="img" 和 handler="Custom Firmware"。其他类型和非固件处理程序将被跳过。 |
| brand | 可选 | 目录品牌（Innioasis, Timmkoo）。空使用模型的默认品牌。 |
| package_name | 可选 | 发布资产文件名。默认为 rom.zip 在 Y1 上和 rom_<model>.zip 在其他型号上。 |
| asset_pattern | 可选 | 对于固件 zip 未命名的版本，不区分大小写的 glob rom*.zip （例如 my-firmware-*.zip). |
| type_a_asset, type_b_asset | 可选 | 当文件名不包含常用标记时，识别 Y1 Type A 和 Type B zip 的 Glob。 |
| icon | 可选 | 徽标网址。自己发布后使用 updater.png / updater.jpg，并作为每个版本的后备。 |
| icon_dark | 可选 | 深色主题标志。 image_dark 是一个可接受的别名。 |
| image | 可选 | 二次光艺术作品，尝试后 icon. |
| post_install, post_install2 | 可选 | 成功安装后打开的页面。第二个包含多步骤指南。 |
| portable_zips | 可选 | 逗号分隔 *-mirror 发布可立即运行的可移植包的存储库。 |
| derivative | 可选 | 构建固件的存储库。具有相同衍生根的固件可以保留用户数据。 |
| info_repo | 可选 | 应用程序存储库，其版本描述了固件的部署内容。需要 post_install 或 post_install2. |
| apk_repo | 可选 | 应用程序存储库，其 APK 应用程序在固件之后安装。 |
| min_version | 可选 | 当 Updater CE 早于此版本时隐藏该条目。 |
| do_not_keep_data | 可选 | true （还 1 / yes）阻止此固件完全保留数据。 |
| slug | 可选 | 链接和保存的安装记录的稳定标识符。空时根据名称和型号生成。 |
| description | 可选 | 简短的目录描述。它可以是属性值或元素的文本。 |

为了兼容性，仍会读取旧名称： `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` 和 `image_dark`。新条目应使用上面的当前名称。

### 将这些行作为拉取请求提交
  - 复制上面生成的行。 它们已经匹配最新的清单格式。
  - 编辑 `slidia_manifest.xml` 在存储库中。 使用下面的编辑链接；存储库主机会自动为您创建一个分叉和一个分支。
  - 粘贴之前的行 `</slidia>`, 保持现有条目不变。
  - 提交到新分支 （例如 `add-your-firmware`），然后针对 Updater CE 存储库打开拉取请求。
  - 在 PR 中，包括 项目链接、支持的型号、发布标签、资产名称和您测试的设备。
[编辑更新程序 CE 清单](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[查看最新的清单](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

保持模型名称大写，使用公共存储库的确切 URL，并保留 `type="img"` 和 `handler="Custom Firmware"` 用于固件条目。

## 使发布易于验证

为发布提供清晰的标签和发布说明。该标签对人们很有用，但 Updater CE 使用 ZIP 资产名称来识别安装包。

### 发布清单
  - 公开发布该版本。
  - 附加 ZIP 文件作为发布资产。
  - 在注释中注明支持的型号和Type A或Type B。
  - 列出任何所需的准备工作或已知的限制。

### 一个版本，三项资产

共享版本可以包含 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip`。更新程序将它们分开分类，并从模型和硬件过滤器中进行选择。

### 不要捆绑猜测

请勿在 Y2 文件名下包含 Y1 包，或添加未经测试的分散、预加载器或分区数据只是为了使资产出现。

## 为什么模型条目在闪烁期间很重要

清单不仅仅是一个下载菜单。提取后，Updater CE 使用解析的模型来准备匹配的安装路径。 Y1 和 Y2 具有不同的平台文件、预加载器、分散配置和设备布局。
  - Y1: 更新程序准备 Y1 路径，并在使用 MTKClient 时使用设备的命名分区。
  - Y2: 更新程序准备 Y2 路径并使用 Y2 MT6582 配置。完全恢复可以使用来自模型正确的分散数据的物理地址。
  - 跨平台支持： Updater CE 可以直接跨 Windows、Linux 和 macOS（支持 Intel 和 Apple Silicon Mac）处理本机刷新，无需额外的刷新工具。
贡献者应提供正确的固件文件，而不是闪存偏移量。 不要编辑分散地址、预加载器、DA 文件或分区命令来解决损坏的包。修复发布资产并在预期模型上进行测试。

## 在请求合并之前
  - 使用 XML 解析器验证 XML。缺少报价或结束语 `/>` 可以隐藏其后的每个条目。
  - 从结帐启动更新程序，以便它在远程刷新之前加载本地清单。
  - 独立检查Y1和Y2。确认该项目仅出现在其包受支持的地方。
  - 检查发布列表 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip` 如适用。
  - 使用可靠的 USB 数据线和恢复原始软件的恢复计划来测试目标设备上的实际安装。
  - 在拉取请求中，解释您测试的内容。不要将未经测试的模型描述为受支持。
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

对于本地检查，请从存储库根运行该命令。它仅验证 XML 语法；它不能证明版本包含有效的固件或设备可以安全地刷新。

## 有用的项目链接[分叉更新器 CE](https://github.com/y1-community/Innioasis-Updater/fork)[查看清单](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[社区贡献说明](support_devs_zh-CN.html)[故障排除](troubleshooting_zh-CN.html)

## AI 代理的改装技能

存储库的 `skills/` 目录是一个基于源代码的知识库，适用于处理 Y1 和 Y2 硬件、固件、主题和应用程序的代理。每个技能都会为其声明来源命名项目文件，因此代理可以在更改设备之前检查事实。从这里开始

### [技能指标及安全规则](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

如何加载技能，事实适用于哪个模型，以及包不应该写入的分区。硬件

### [Y1 硬件](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572，滚轮作为按键事件，480x360显示，FM/音频路径，存储和Type A/B分区图。硬件

### [Y2 硬件](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 板、设备树、GC9503V/ST7701S 面板、PMIC/DAC 导轨、分区和启动映像。固件

### [固件包](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip 剖析、分散文件、A 级更新合同和发布清单。主题

### [主题和皮肤创作](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json 主题、Rockbox WPS/SBS、Reborn 皮肤和 Y2Player 皮肤格式 v2。所有技能

### [浏览技能文件夹](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2、库存 Android ROM、Y2Linux、Android 应用程序、启动器、发行说明和网站发布。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
