---
title: "開發商|將自訂韌體新增至 Innioasis 更新程式 CE - Innioasis 韌體下載"
description: "用於將自訂 Innioasis Y1 或 Y2 韌體新增至 Updater CE 的開發人員文件：分叉儲存庫、發布 rom.zip 資產、編輯 slidia_manifest.xml、測試並開啟拉取請求。"
language: "zh-TW"
source: "https://innioasis.app/developers_zh-TW.html"
---

# 開發商|將自訂韌體新增至 Innioasis 更新程式 CE - Innioasis 韌體下載

對於韌體開發人員

# 將您的韌體新增至 Updater CE。

Updater CE 是自訂韌體的社群目錄和安裝程式。從基礎 ROM 開發您的項目，將其發佈為具有正確發布資產的公共儲存庫，將模型條目新增至 `slidia_manifest.xml`，測試模型過濾器，並開啟拉取請求。一個儲存庫可以為其支援的每種模型提供服務。[查看Updater CE源](https://github.com/y1-community/Innioasis-Updater)[瀏覽軟體下載](firmware_zh-TW.html)

## 從基礎開始 ROM

基礎 ROM 為定制韌體開發人員提供了一個乾淨的 Android 基礎，並啟用了無線射頻晶片。在 Y1 上，它們支援 Wi-Fi 和 GPS 以及工廠藍牙和 FM；在 Y2 上，它們支援 Wi-Fi、GPS 和 FM 以及工廠藍牙。用於自訂韌體開發的基礎 ROM 下載，其中每一項都支援 Android 版本和無線功能[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| 下載 | 裝置 | Android | 無線功能 |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | 將 Wi-Fi 和 GPS 新增至出廠藍牙和 FM（出廠時 FM 已在 Y1 上運作）。適用於搭載 OS 2.0.0 或更高版本的 Y1 播放器。 |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | 將 Wi-Fi 和 GPS 新增至出廠藍牙和 FM（出廠時 FM 已在 Y1 上運作）。適用於作業系統早於 2.0.0 的 Y1 玩家。 |
| rom_y2.zip | Y2 | Android 4.4.2 | 為工廠藍牙添加 Wi-Fi、GPS 和 FM。 Y2 無線電晶片已完全啟用，因此 FM 也可在此處使用。 |

這些圖像是啟用了設備無線無線電的庫存 Android 基礎 (AOSP)，因此自訂韌體可以添加網路功能，而不是替換無線電堆疊。它們是以下發布步驟的實際起點。

## 使用這些發布資產名稱

檔案名稱是相容性訊號的一部分。保持名稱準確，並將 ZIP 檔案放入專案的發布資產中，而不僅僅是儲存庫來源樹中。韌體 ZIP 資產名稱和支援的設備``````

| 資產 | 裝置 | 硬體 | 意義 |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 隨附作業系統 2.0.0 或更高版本的裝置。 |
| rom_type_b.zip | Y1 | Type B | Y1 隨附 2.0.0 之前作業系統的設備。 |
| rom_y2.zip | Y2 | Y2 | Y2 完整安裝包。將其與 Y1 資產分開。 |
不要重命名包以使其適合另一個模型。 Y1 和 Y2 使用不同的 MediaTek 平台檔案和刷新配置。发布其实际支持的硬件的包。

## 連結如何運作

更新程式 CE 讀取清單作為其目錄。每個 `<package>` 該行告訴它項目名稱、儲存庫、模型和處理程序。當使用者選擇該項目時，更新程式會檢查儲存庫的已發布版本並查找 `rom*.zip` 資產。

### 顯現

命名項目並將其映射到模型。 Y1 和 Y2 需要單獨的行，即使它們共用儲存庫。

### 已發布版本

包含可安裝的 ZIP 資產。單一版本可能包含 Y1 Type A、Y1 Type B 和 Y2 套件。

### 更新程式CE安裝

使用選定的型號來選擇相符的封裝和特定於型號的快閃記憶體路徑。用户不必猜测文件名。

## 發布項目只需五步
  - 分叉 Updater CE 儲存庫。 創建您自己的分叉 [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)，然後在本地克隆您的分叉。
  - 準備公共韌體儲存庫。 確保儲存庫是公共的並且其版本包含正確的 ZIP 資產。你可以把 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip` 當它們屬於同一版本時在同一版本上。
  - 編輯清單。 打開 `slidia_manifest.xml` 在 Updater CE 分支的根目錄中。為該版本支援的每個模型新增一行（Y1 和 Y2 是公共對）。這 `repo` 值是儲存庫的 `owner/repository`; `url` 是公共項目頁面。
  - 測試目錄。 从编辑后的结账中运行更新程序。選擇 Y1 並確認項目顯示 Y1 資產。选择 Y2 并确认其显示 Y2 版本。当Type A和Type B都发布时，分别检查。
  - 打開拉取請求。 將清單變更推送到您的分支，並針對上游 Updater CE 儲存庫開啟拉取請求。包括項目連結、支援的型號、發布標籤、資產名稱和您測試的設備。

## 產生您的清單行

填寫儲存庫並勾選該版本支援的每個模型。生成器寫一個 `<package>` 每個模型行，僅包含您設定的屬性，因此結果與目前相符 `slidia_manifest.xml` 格式。下面提供了 Updater CE 讀取的每個屬性 - 可選屬性位於 更多選擇.儲存庫網址公共 GitHub 儲存庫。生成器提取 `owner/repository` 從網址。軟體名稱顯示在應用程式和網站目錄中。專案網址項目或其發行說明的面向人的頁面。品牌清除此項可使用模型的預設品牌。 SR1、Q3、Q5 和 Q3e 是 Timmkoo 模型。設備（每條線）Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3e其他型號對於上面未列出的型號。已知型號保留其目錄拼字。旗幟`do_not_keep_data` — 切勿為此韌體提供保留數據由原始軟體建構 - 補充 `derivative="y1-community/y1-stock-rom"`

僅當傳入韌體與已安裝韌體相同或共享一個韌體時才提供保留數據 `derivative` 根。僅當用戶資料確實無法保留時才使用該標誌。更多選項：圖標、藝術品、發布資源、安裝後和鏡像

#### 圖標和藝術品圖示文件選擇您將提交到儲存庫的圖像。這將預覽它並建立其原始 URL；它不上傳任何東西。儲存庫中的圖示路徑已提交映像的路徑，相對於儲存庫根目錄。圖示分支圖示網址直接圖像 URL。當為空時，應用程式使用版本的 `updater.png` 或生成的圖示。選定的圖標預覽

深色模式圖示 URL可選的深色主題圖示。 `image_dark` 是一個可接受的別名。燈光藝術作品網址二次藝術作品，在發布圖像後嘗試過 `icon`.深色藝術作品網址

#### 釋放資產發布資產名稱每個選定型號都有一個名稱。留空即可使用 `rom.zip` 在 Y1 上和 `rom_<model>.zip` 別處。資產格局當發行版的 zip 未命名時使用 Glob `rom*.zip`.Type A 資產當 Y1 Type A 套件的名稱沒有說明時，使用 Glob 表示。Type B 資產當 Y1 Type B 套件的名稱沒有說明時，使用 Glob 表示。最低應用版本隱藏舊版 Updater CE 版本中的條目。

#### 連結、鏡像和 Keep Data 系列安裝後頁面安裝成功後開啟。第二個安裝後頁面多頁設定指南的可選第二步驟。便攜式拉鍊鏡子逗號分隔 `*-mirror` 建置 Portable Flashing Zip 套件的儲存庫。衍生性商品儲存庫此版本所基於的韌體。相關韌體共享一個資料分區，這就是Keep Data檢查的內容。資訊庫應用程式儲存庫，其版本描述了此韌體中的應用程式。它還需要一個安裝後頁面。APK 儲存庫應用程式儲存庫，其 APK 應用程式在韌體之後下載並安裝。

#### 目錄附加內容蛞蝓連結和保存的安裝記錄的穩定標識符。當選擇多個模型時，模型會自動附加。描述`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`複製行

正在加載最新的清單...預覽添加了您的行的最新清單

發電機獲取電流 `slidia_manifest.xml` 來自此存儲庫並在之前插入您生成的行 `</slidia>`.

對於共享儲存庫來說，一行是不夠的。 如果缺少 Y2 行，Y2 使用者即使在 `rom_y2.zip` 存在於專案的發布中。對於您的版本支援的所有其他模型也是如此。

### 清單讀取的每個屬性

這些是目前 Updater CE 版本所理解的屬性。生成器僅寫入您填寫的內容；該應用程式將在其餘部分回退到合理的預設值。slidia_manifest.xml包屬性及其意義``````````````````````````````````````````````````````````````````````````````````````````````

| 屬性 | 需要 | 它的作用 |
| --- | --- | --- |
| name | 是的 | 軟體名稱顯示在目錄和安裝卡上。 |
| repo | 是的 | owner/repo。該應用程式讀取該儲存庫的 GitHub 版本。 |
| device | 是的 | 目標型號，大寫（Y1, Y2, G1, Q3e，……）。每個模型保留一個條目。 |
| url | 受到推崇的 | 從目錄中開啟的項目頁面或發行說明。 |
| type, handler | 實踐中是的 | type="img" 和 handler="Custom Firmware"。其他類型和非韌體處理程序將被跳過。 |
| brand | 可選 | 目錄品牌（Innioasis, Timmkoo）。空使用模型的預設品牌。 |
| package_name | 可選 | 发布资产文件名。預設為 rom.zip 在 Y1 上和 rom_<model>.zip 在其他型號上。 |
| asset_pattern | 可選 | 對於韌體 zip 未命名的版本，不區分大小寫的 glob rom*.zip （例如 my-firmware-*.zip). |
| type_a_asset, type_b_asset | 可選 | 當檔案名稱不包含常用標記時，識別 Y1 Type A 和 Type B zip 的 Glob。 |
| icon | 可選 | 徽標網址。自己發布後使用 updater.png / updater.jpg，並作為每個版本的後備。 |
| icon_dark | 可選 | 深色主題標誌。 image_dark 是一個可接受的別名。 |
| image | 可選 | 二次光藝術作品，嘗試後 icon. |
| post_install, post_install2 | 可選 | 成功安裝後開啟的頁面。第二個包含多步驟指南。 |
| portable_zips | 可選 | 逗號分隔 *-mirror 發布可立即運行的可移植套件的儲存庫。 |
| derivative | 可選 | 建置韌體的儲存庫。具有相同衍生根的韌體可以保留用戶資料。 |
| info_repo | 可選 | 應用程式儲存庫，其版本描述了韌體的部署內容。需要 post_install 或 post_install2. |
| apk_repo | 可選 | 應用程式儲存庫，其 APK 應用程式在韌體之後安裝。 |
| min_version | 可選 | 當 Updater CE 早於此版本時隱藏該條目。 |
| do_not_keep_data | 可選 | true (也 1 / yes）阻止此韌體完全保留資料。 |
| slug | 可選 | 連結和保存的安裝記錄的穩定標識符。空時根據名稱和型號產生。 |
| description | 可選 | 簡短的目錄描述。它可以是屬性值或元素的文字。 |

為了相容性，仍會讀取舊名稱： `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` 和 `image_dark`。新条目应使用上面的当前名称。

### 將這些行作為拉取請求提交
  - 複製上面產生的行。 它們已經符合最新的清單格式。
  - 編輯 `slidia_manifest.xml` 在儲存庫中。 使用下面的編輯連結；儲存庫主機會自動為您建立一個分叉和一個分支。
  - 貼上之前的行 `</slidia>`, 保持現有條目不變。
  - 提交到新分支 （例如 `add-your-firmware`），然後針對 Updater CE 儲存庫開啟拉取請求。
  - 在 PR 中，包括 項目連結、支援的型號、發布標籤、資產名稱和您測試的設備。
[編輯更新程式 CE 清單](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[查看最新的清單](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

保持模型名稱大寫，使用公共儲存庫的確切 URL，並保留 `type="img"` 和 `handler="Custom Firmware"` 用於韌體條目。

## 使發布易於驗證

為發布提供清晰的標籤和發布說明。該標籤對人們很有用，但 Updater CE 使用 ZIP 資產名稱來識別安裝包。

### 發布清單
  - 公開發布該版本。
  - 附加 ZIP 檔案作為發布資產。
  - 在註記中註明支援的型號和Type A或Type B。
  - 列出任何所需的準備工作或已知的限制。

### 一個版本，三項資產

共享版本可以包含 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip`。更新程式將它們分開分類，並從模型和硬體過濾器中進行選擇。

### 不要捆綁猜測

請勿在 Y2 檔案名稱下包含 Y1 包，或新增未經測試的分散、預先載入器或分割資料只是為了使資產出現。

## 為什麼模型條目在閃爍期間很重要

清單不僅僅是一個下載選單。提取後，Updater CE 使用解析的模型來準備匹配的安裝路徑。 Y1 和 Y2 具有不同的平台檔案、預先載入器、分散式配置和裝置佈局。
  - Y1: 更新程式準備 Y1 路徑，並在使用 MTKClient 時使用裝置的命名分割區。
  - Y2: 更新程式準備 Y2 路徑並使用 Y2 MT6582 配置。完全恢復可以使用來自模型正確的分散資料的實體位址。
  - 跨平台支援： Updater CE 可以直接跨 Windows、Linux 和 macOS（支援 Intel 和 Apple Silicon Mac）處理本機刷新，無需額外的刷新工具。
貢獻者應提供正確的韌體文件，而不是快閃記憶體偏移量。 不要編輯分散位址、預先載入器、DA 檔案或分區命令來解決損壞的套件。修復發布資產並在預期模型上進行測試。

## 在請求合併之前
  - 使用 XML 解析器驗證 XML。缺少報價或結束語 `/>` 可以隱藏其後的每個條目。
  - 從結帳啟動更新程序，以便它在遠端刷新之前載入本機清單。
  - 獨立檢查Y1和Y2。確認該項目僅出現在其包受支援的地方。
  - 檢查發布列表 `rom.zip`, `rom_type_b.zip`, 和 `rom_y2.zip` 如適用。
  - 使用可靠的 USB 數據線和恢復原始軟體的恢復計劃來測試目標設備上的實際安裝。
  - 在拉取請求中，解釋您測試的內容。不要將未經測試的模型描述為受支援。
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

對於本機檢查，請從儲存庫根執行該命令。它僅驗證 XML 語法；它不能證明版本包含有效的韌體或裝置可以安全地刷新。

## 有用的項目鏈接[分叉更新器 CE](https://github.com/y1-community/Innioasis-Updater/fork)[查看清單](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[社區貢獻說明](support_devs_zh-TW.html)[疑難排解](troubleshooting_zh-TW.html)

## AI 代理的改裝技能

儲存庫的 `skills/` 目錄是一個基於原始程式碼的知識庫，適用於處理 Y1 和 Y2 硬體、韌體、主題和應用程式的代理程式。每個技能都會為其聲明來源命名專案文件，因此代理可以在更改設備之前檢查事實。從這裡開始

### [技能指標及安全規則](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

如何載入技能，事實適用於哪個模型，以及套件不應該寫入的分區。硬體

### [Y1 硬體](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572，滾輪作為按鍵事件，480x360顯示，FM/音訊路徑，儲存和Type A/B分區圖。硬體

### [Y2 硬體](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 板、設備樹、GC9503V/ST7701S 面板、PMIC/DAC 導軌、分區和啟動映像。韌體

### [韌體包](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip 剖析、分散文件、A 級更新合約和發布清單。主題

### [主題和皮膚創作](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json 主題、Rockbox WPS/SBS、Reborn 皮膚和 Y2Player 皮膚格式 v2。所有技能

### [瀏覽技能資料夾](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2、庫存 Android ROM、Y2Linux、Android 應用程式、啟動器、發行說明和網站發布。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
