---
title: "開発者 |カスタム ファームウェアを Innioasis Updater CE - Innioasis ファームウェア ダウンロードに追加します"
description: "カスタム Innioasis Y1 または Y2 ファームウェアを Updater CE に追加するための開発者ドキュメント: リポジトリをフォークし、rom.zip アセットを公開し、slidia_manifest.xml を編集し、テストし、プル リクエストを開きます。"
language: "ja"
source: "https://innioasis.app/developers_ja.html"
---

# 開発者 |カスタム ファームウェアを Innioasis Updater CE - Innioasis ファームウェア ダウンロードに追加します

ファームウェア開発者向け

# ファームウェアを Updater CE に追加します。

Updater CE は、カスタム ファームウェアのコミュニティ カタログおよびインストーラーです。ベース ROM からプロジェクトを開発し、正しいリリース アセットを含むパブリック リポジトリとして公開し、モデル エントリを `slidia_manifest.xml`、モデル フィルターをテストし、プル リクエストを開きます。 1 つのリポジトリがサポートするすべてのモデルに対応できます。[Updater CE ソースを表示する](https://github.com/y1-community/Innioasis-Updater)[ソフトウェアのダウンロードを参照する](firmware_ja.html)

## ベース ROM から開始します

ベース ROM は、カスタム ファームウェア開発者に、ワイヤレス無線チップが有効になったクリーンな Android 基盤を提供します。 Y1 では、工場出荷時の Bluetooth と FM に加えて、Wi-Fi と GPS が有効になります。 Y2 では、工場出荷時の Bluetooth に加えて Wi-Fi、GPS、FM が有効になります。カスタム ファームウェア開発用のベース ROM ダウンロード。Android バージョンとそれぞれで有効になるワイヤレス機能が含まれます。[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| ダウンロード | デバイス | Android | ワイヤレス機能 |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Wi-Fi と GPS を工場出荷時の Bluetooth と FM に追加します (FM は工場出荷時に Y1 ですでに動作しています)。 OS 2.0.0 以降で出荷された Y1 プレーヤーの場合。 |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Wi-Fi と GPS を工場出荷時の Bluetooth と FM に追加します (FM は工場出荷時に Y1 ですでに動作しています)。 2.0.0 より前の OS で出荷された Y1 プレーヤーの場合。 |
| rom_y2.zip | Y2 | Android 4.4.2 | 工場出荷時の Bluetooth に Wi-Fi、GPS、FM を追加します。 Y2 無線チップが完全に有効になっているため、ここでも FM が利用可能です。 |

これらのイメージは、デバイスの無線無線が有効になっているストック Android ベース (AOSP) であるため、無線スタックを置き換えるのではなく、カスタム ファームウェアでネットワーク機能を追加できます。これらは、以下の公開手順の実際的な開始点となります。

## これらのリリースアセット名を使用してください

ファイル名は互換性シグナルの一部です。名前を正確に保ち、​​ZIP ファイルをリポジトリ ソース ツリーだけでなくプロジェクトのリリース アセットに配置します。ファームウェア ZIP アセット名とサポートされるデバイス``````

| 資産 | デバイス | ハードウェア | 意味 |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | OS 2.0.0 以降が搭載された Y1 デバイス。 |
| rom_type_b.zip | Y1 | Type B | Y1 デバイスは 2.0.0 より前の OS を搭載して出荷されました。 |
| rom_y2.zip | Y2 | Y2 | Y2 フルインストール パッケージ。 Y1 アセットとは別にしてください。 |
別のモデルに適合させるためにパッケージの名前を変更しないでください。 Y1 と Y2 は、異なる MediaTek プラットフォーム ファイルとフラッシュ構成を使用します。実際にサポートするハードウェアのパッケージを公開します。

## 接続の仕組み

Updater CE はマニフェストをカタログとして読み取ります。それぞれ `<package>` この行は、プロジェクト名、リポジトリ、モデル、およびハンドラーを示します。ユーザーがそのプロジェクトを選択すると、アップデータはリポジトリの公開リリースをチェックし、 `rom*.zip` 資産。

### マニフェスト

プロジェクトに名前を付け、モデルにマップします。 Y1 と Y2 は、リポジトリを共有する場合でも、別々の行が必要です。

### 公開されたリリース

インストール可能な ZIP アセットが含まれています。 1 つのリリースには、Y1、Type A、Y1、Type B、および Y2 のパッケージが一緒に含まれる場合があります。

### Updater CE インストール

選択したモデルを使用して、一致するパッケージとモデル固有のフラッシュ パスを選択します。ユーザーはファイル名を推測する必要はありません。

## 5 つのステップでプロジェクトを公開する
  - Updater CE リポジトリをフォークします。 独自のフォークを作成する [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater)、ローカルでフォークのクローンを作成します。
  - パブリックファームウェアリポジトリを準備します。 リポジトリがパブリックであり、そのリリースに正しい ZIP アセットが含まれていることを確認してください。置くことができます `rom.zip`, `rom_type_b.zip`、そして `rom_y2.zip` 同じバージョンに属している場合は、同じリリース上で実行されます。
  - マニフェストを編集します。 開く `slidia_manifest.xml` Updater CE フォークのルートにあります。リリースがサポートするモデルごとに 1 行を追加します (Y1 と Y2 が共通のペアです)。の `repo` 値はリポジトリの値です `owner/repository`; `url` 公開プロジェクトページです。
  - カタログをテストします。 編集したチェックアウトからアップデーターを実行します。 Y1 を選択し、プロジェクトに Y1 アセットが表示されていることを確認します。 Y2を選択し、Y2のリリースが表示されていることを確認します。 Type AとType Bが両方公開されている場合は個別に確認してください。
  - プルリクエストを開きます。 マニフェストの変更をフォークにプッシュし、上流の Updater CE リポジトリに対してプル リクエストを開きます。プロジェクトのリンク、サポートされているモデル、リリース タグ、アセット名、テストしたデバイスを含めます。

## マニフェスト行を生成する

リポジトリに入力し、リリースがサポートするすべてのモデルにチェックを入れます。ジェネレーターは 1 つを書き込みます `<package>` モデルごとに行に分けられ、設定した属性のみが含まれるため、結果は現在のものと一致します。 `slidia_manifest.xml` 形式。 Updater CE で読み取られるすべての属性は以下で利用可能です。オプションのものは以下にあります。 その他のオプション.リポジトリURLパブリック GitHub リポジトリ。ジェネレーターは抽出します `owner/repository` URLから。ソフトウェア名アプリとサイトのカタログに表示されます。プロジェクトURLプロジェクトまたはそのリリース ノートの人向けページ。ブランドモデルのデフォルトのブランドを使用するには、これをクリアします。 SR1、Q3、Q5、Q3e は Timmkoo モデルです。デバイス (各 1 行)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eその他のモデル上記以外の機種の場合。既知のモデルはカタログの綴りのままです。フラグ`do_not_keep_data` — このファームウェアのデータ保持を決して提供しないでくださいオリジナルのソフトウェアから構築 — 追加 `derivative="y1-community/y1-stock-rom"`

Keep Data は、受信したファームウェアとインストールされたファームウェアが同じであるか、同じファームウェアを共有している場合にのみ提供されます。 `derivative` 根。このフラグは、ユーザーデータが本当に引き継がれない場合にのみ使用してください。その他のオプション: アイコン、アートワーク、リリース アセット、ポストインストール、ミラー

#### アイコンとアートワークアイコンファイルリポジトリにコミットするイメージを選択します。これにより、それがプレビューされ、生の URL が構築されます。何もアップロードしません。リポジトリ内のアイコンのパスリポジトリのルートを基準とした、コミットされたイメージへのパス。アイコンブランチアイコンのURL画像の直接 URL。空の場合、アプリはリリースの `updater.png` または生成されたアイコン。選択したアイコンのプレビュー

ダークモードアイコンのURLオプションのダークテーマアイコン。 `image_dark` は受け入れられるエイリアスです。ライトアート作品URL二次アートワーク、リリース後に試してみた画像と `icon`.ダークアートワークのURL

#### アセットをリリースするリリースアセット名選択したモデルごとに 1 つの名前。空のままにして使用します `rom.zip` Y1 と `rom_<model>.zip` 他の場所で。資産パターンリリースの zip に名前が付けられていない場合に使用される Glob `rom*.zip`.Type A アセットY1 Type A パッケージの名前が記載されていない場合は、そのパッケージをグロブします。Type B アセットY1 Type B パッケージの名前が記載されていない場合は、そのパッケージをグロブします。アプリの最小バージョン古い Updater CE ビルドのエントリを非表示にします。

#### リンク、ミラー、Keep Data ファミリインストール後のページインストールが成功した後に開きます。インストール後の 2 ページ目複数ページのセットアップ ガイドのオプションの 2 番目のステップ。ポータブルジップミラーカンマ区切り `*-mirror` Portable Flashing Zip パッケージを構築するリポジトリ。派生リポジトリこのリリースの構築元となっているファームウェア。関連するファームウェアはデータ パーティションを共有しており、Keep Data はこれをチェックします。情報リポジトリこのファームウェアのアプリを説明するリリースのアプリ リポジトリ。インストール後のページも必要です。APK リポジトリAPK アプリがファームウェアの後にダウンロードしてインストールされるアプリ リポジトリ。

#### カタログ付録ナメクジリンクと保存されたインストール レコードの安定した識別子。複数のモデルを選択すると、モデルは自動的に追加されます。説明`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`行をコピーする

最新のマニフェストをロードしています…行を追加した最新のマニフェストをプレビューする

ジェネレーターが電流を取得しました `slidia_manifest.xml` このリポジトリから取得し、直前に生成された行を挿入しました `</slidia>`.

共有リポジトリには 1 行では不十分です。 Y2 行が欠落している場合、Y2 ユーザーは次のような場合でもモデルに一致するエントリを取得できません。 `rom_y2.zip` プロジェクトのリリースに存在します。リリースがサポートする他のすべてのモデルにも同じことが当てはまります。

### マニフェストが読み取るすべての属性

これらは、現在の Updater CE ビルドが理解する属性です。ジェネレーターは、ユーザーが入力したもののみを書き込みます。アプリは残りの部分について適切なデフォルトに戻ります。slidia_manifest.xml パッケージの属性とその意味``````````````````````````````````````````````````````````````````````````````````````````````

| 属性 | 必要です | 何をするのか |
| --- | --- | --- |
| name | はい | カタログおよびインストールカードに記載されているソフトウェア名。 |
| repo | はい | owner/repo。アプリはそのリポジトリの GitHub リリースを読み取ります。 |
| device | はい | 対象モデル、大文字(Y1, Y2, G1, Q3e、…）。モデルごとに 1 つのエントリを保持します。 |
| url | 推奨 | カタログから開いたプロジェクト ページまたはリリース ノート。 |
| type, handler | はい、実際には | type="img" そして handler="Custom Firmware"。他のタイプおよび非ファームウェア ハンドラーはスキップされます。 |
| brand | オプション | カタログブランド（Innioasis, Timmkoo）。 Empty では、モデルのデフォルトのブランドが使用されます。 |
| package_name | オプション | リリースアセットのファイル名。デフォルトは rom.zip Y1 と rom_<model>.zip 他のモデルでは。 |
| asset_pattern | オプション | ファームウェア zip に名前が付けられていないリリースでは、大文字と小文字を区別しない glob rom*.zip （例えば my-firmware-*.zip). |
| type_a_asset, type_b_asset | オプション | ファイル名に通常のマーカーが含まれていない場合に、Y1 Type A および Type B zip を識別するグロブ。 |
| icon | オプション | ロゴの URL。リリース独自の後に使用される updater.png / updater.jpg、そしてすべてのリリースのフォールバックとして。 |
| icon_dark | オプション | ダークテーマのロゴ。 image_dark は受け入れられるエイリアスです。 |
| image | オプション | 二次的なライト アートワーク、その後に試行 icon. |
| post_install, post_install2 | オプション | インストールが成功した後に開かれたページ。 2 番目のガイドでは、複数のステップのガイドについて説明します。 |
| portable_zips | オプション | カンマ区切り *-mirror すぐに実行できるポータブル パッケージを公開するリポジトリ。 |
| derivative | オプション | ファームウェアの構築元となるリポジトリ。同じ派生ルートを持つファームウェアはユーザー データを保持できます。 |
| info_repo | オプション | リリースには、ファームウェアが展開する内容が記述されているアプリ リポジトリ。必要 post_install または post_install2. |
| apk_repo | オプション | ファームウェアの後にアプリが APK インストールされるアプリ リポジトリ。 |
| min_version | オプション | Updater CE がこのバージョンより古い場合、エントリを非表示にします。 |
| do_not_keep_data | オプション | true （また 1 / yes) このファームウェアのデータ保持を完全にブロックします。 |
| slug | オプション | リンクと保存されたインストール レコードの安定した識別子。空の場合は名前とモデルから生成されます。 |
| description | オプション | カタログの短い説明。属性値または要素のテキストにすることができます。 |

互換性を確保するために、従来の名前も引き続き読み取られます。 `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` そして `image_dark`。新しいエントリには上記の現在の名前を使用する必要があります。

### 行をプルリクエストとして送信します
  - 上記で生成された行をコピーします。 これらはすでに最新のマニフェスト形式と一致しています。
  - 編集 `slidia_manifest.xml` リポジトリ内。 以下の編集リンクを使用してください。リポジトリ ホストはフォークとブランチを自動的に作成します。
  - 直前の行を貼り付けます `</slidia>`, 既存のエントリを変更せずに維持します。
  - 新しいブランチにコミットする （例えば `add-your-firmware`)、Updater CE リポジトリに対してプル リクエストを開きます。
  - PR には次の内容を含めます プロジェクト リンク、サポートされているモデル、リリース タグ、アセット名、テストしたデバイス。
[Updater CE マニフェストを編集する](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[最新のマニフェストを参照してください](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

モデル名は大文字のままにし、パブリック リポジトリの正確な URL を使用し、 `type="img"` そして `handler="Custom Firmware"` ファームウェアエントリの場合。

## リリースを簡単に確認できるようにする

リリースに明確なタグとリリース ノートを付けます。このタグは人々にとって便利ですが、Updater CE がインストール パッケージを識別するために使用するのは ZIP アセット名です。

### リリースチェックリスト
  - リリースを公開します。
  - ZIP ファイルをリリース アセットとして添付します。
  - 備考欄に対応機種とType AまたはType Bを記載してください。
  - 必要な準備や既知の制限を列挙します。

### 1 つのリリース、3 つのアセット

共有リリースには以下を含めることができます `rom.zip`, `rom_type_b.zip`、そして `rom_y2.zip`。アップデーターはそれらを個別に分類し、モデルとハードウェアのフィルターから選択します。

### 推測をまとめないでください

Y2 ファイル名の下に Y1 パッケージを含めたり、アセットを表示するためだけに未テストのスキャッター、プリローダー、またはパーティション データを追加したりしないでください。

## フラッシュ中にモデルのエントリが重要な理由

マニフェストは単なるダウンロード メニューではありません。抽出後、Updater CE は解決されたモデルを使用して、一致するインストール パスを準備します。 Y1 と Y2 には、異なるプラットフォーム ファイル、プリローダー、スキャッター構成、デバイス レイアウトがあります。
  - Y1: アップデーターは Y1 パスを準備し、MTKClient が使用される場合にデバイスの名前付きパーティションを使用します。
  - Y2: アップデーターは Y2 パスを準備し、Y2 MT6582 構成を使用します。完全リカバリでは、モデルが正しい散乱データからの物理アドレスを使用できます。
  - クロスプラットフォームのサポート: Updater CE は、追加のフラッシュ ツールを使用せずに、Windows、Linux、macOS (Intel と Apple Silicon Mac の両方をサポート) 全体でネイティブ フラッシュを直接処理します。
貢献者は、フラッシュ オフセットではなく、正しいファームウェア ファイルを提供する必要があります。 不正なパッケージを回避するためにスキャッタ アドレス、プリローダー、DA ファイル、またはパーティション コマンドを編集しないでください。リリース アセットを修正し、目的のモデルでテストします。

## マージをリクエストする前に
  - XML パーサーを使用して XML を検証します。引用符または締めくくりが欠落している `/>` それ以降のすべてのエントリを非表示にすることができます。
  - チェックアウトからアップデータを起動して、リモート更新の前にローカル マニフェストをロードします。
  - Y1 と Y2 を個別にチェックします。プロジェクトがそのパッケージがサポートされている場合にのみ表示されることを確認します。
  - リリースリストを確認してください `rom.zip`, `rom_type_b.zip`、そして `rom_y2.zip` 該当する限り。
  - 信頼性の高い USB データ ケーブルと元のソフトウェアに戻すためのリカバリ プランを使用して、目的のデバイスで実際のインストールをテストします。
  - プル リクエストでは、テストした内容を説明します。テストされていないモデルをサポートされていると説明しないでください。
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

ローカル チェックの場合は、リポジトリ ルートからコマンドを実行します。 XML 構文のみを検証します。リリースに有効なファームウェアが含まれていること、またはデバイスが安全にフラッシュできることを証明するものではありません。

## 役立つプロジェクトのリンク[フォーク Updater CE](https://github.com/y1-community/Innioasis-Updater/fork)[マニフェストを参照](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[コミュニティ貢献メモ](support_devs_ja.html)[トラブルシューティング](troubleshooting_ja.html)

## AIエージェントのModスキル

リポジトリの `skills/` directory は、Y1 および Y2 のハードウェア、ファームウェア、テーマ、アプリを扱うエージェント向けのソースベースのナレッジ ベースです。各スキルはそのクレームの元となるプロジェクト ファイルに名前を付けるため、エージェントはデバイスを変更する前に事実を確認できます。ここから始めましょう

### [スキルインデックスと安全ルール](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

スキルをロードする方法、ファクトが適用されるモデル、およびパッケージが書き込むべきパーティション。ハードウェア

### [Y1 ハードウェア](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572、キー イベントとしてのホイール、480x360 ディスプレイ、FM/オーディオ パス、ストレージ、および Type A/B パーティション マップ。ハードウェア

### [Y2 ハードウェア](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 ボード、デバイス ツリー、GC9503V/ST7701S パネル、PMIC/DAC レール、パーティション、ブート イメージ。ファームウェア

### [ファームウェアパッケージ](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip の解剖学、スキャッタ ファイル、クラス A 更新契約、およびリリース チェックリスト。テーマ

### [テーマとスキンのオーサリング](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json テーマ、Rockbox WPS/SBS、Reborn スキン、および Y2Player スキン フォーマット v2。すべてのスキル

### [スキルフォルダーを参照する](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2、ストック Android ROM、Y2Linux、Android アプリ、ランチャー、リリース ノート、サイト公開。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
