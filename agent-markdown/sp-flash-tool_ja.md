---
title: "Innioasis および Timmkoo プレイヤーの SP Flash Tool"
description: "Windows および Linux で Innioasis Updater にバンドルされている SP Flash Tool を検索し、rom.zip または rom_y2.zip を抽出し、一致するスキャッタ ファイルで Innioasis Y1 または Y2 をフラッシュします。"
language: "ja"
source: "https://innioasis.app/sp-flash-tool_ja.html"
---

# Innioasis および Timmkoo プレイヤーの SP Flash Tool

手動点滅

# Innioasis および Timmkoo プレーヤー用の Flash ツール

SP Flash Tool は Innioasis Updater の中にあります [Windows](drivers_ja.html#windows) そして [Linux](drivers_ja.html#linux)。すでにお持ちですね。このガイドでは、Innioasis Y1 または Y2 で安全に使用する方法と、Timmkoo プレーヤー向けのアップデーター ルートを示します。[アップデーター ガイドに戻る](guide_ja.html)[ファームウェアのダウンロード](firmware_ja.html)[トラブルシューティング](troubleshooting_ja.html)

Innioasis Updater から始める

## アップデーターは 1 回のパスですべてのジョブを実行します

アップデーターは、ほとんどのインストールを 1 つのパスで実行します。ソフトウェアを選択し、手順に従ってください。これで完了です。また、修正または新しいリリースがいつリリースされるかについても通知されます。 SP Flash Tool は、アップデーターが終了できないまれなケースに備えて、アップデーターのツールキット内にあります。以下の手順は例外です。

## このツールの目的

アップデーターがプレーヤーをフラッシュします。 SP Flash Tool は同じエンジンですが、ガード レールがありません。 Updater が起動しない場合、プレーヤーが接続できない場合、またはスキャッター ファイルの回避方法がわかっている場合に使用してください。まずアップデーターを試してください。 ほとんどのインストールとほとんどのリカバリでは、ガイド付き [アップデーターのルート](guide_ja.html) より安全な選択です。 SP Flash Tool が必要な理由がわかっている場合は SP Flash Tool を使用し、充電済みのバッテリーと USB データ ケーブルを準備しておいてください。

## Innioasis プレーヤー用の Flash ツール

Innioasis Updater は Innioasis プレーヤー用の Flash ツールです。公式ソフトウェアのインストール、モデルに一致するフローを通じてパッケージの更新と復元が行われ、音楽と設定が維持されます。

### Innioasis Y1 フラッシュ ツール

アップデーターで Y1 リリースを選択し、アプリの要求に応じて電源がオフになっているプレーヤーを接続します。手動ルートが必要な場合、同じ Y1 パッケージが SP Flash Tool で機能します。

### Innioasis Y2 フラッシュ ツール

Y2 にリストされているリリースを選択します。 Y2 パッケージは Y1 パッケージと互換性がないため、開始する前にモデルを確認してください。

## Timmkoo プレーヤー用の Flash ツール

Timmkoo プレーヤーは同じアップデーターのインストール フローを使用します。 Timmkoo の ZIP および RAR パッケージを直接読み取るため、別個の Flash ツールやスキャッター ファイルは必要ありません。

### Timmkoo Q5 フラッシュ ツール

アップデーターで Q5 モデルを選択し、Timmkoo パッケージを選択して、インストール/復元を実行し、プロンプトでプレーヤーを接続します。

### Timmkoo Q3 および Q3E フラッシュ ツール

Q3 エントリは、Q3 と Q3E を同様にカバーします。アップデーターは、プロジェクトが公開するパッケージから一致するファイルを選択します。

### Timmkoo A5 フラッシュ ツール

パッケージを選択する前に A5 モデルを選択し、同じインストール プロンプトに従います。

## アップデーターが配置する場所

SP Flash Tool は、個別のダウンロードとしてではなく、アップデーターのインストール フォルダーに同梱されています。必要なときにそこから開きます。

### Windows

アップデーターのインストールフォルダーを開いて実行します。 `flash_tool.exe`。フォルダは通常以下にあります `%LOCALAPPDATA%\Innioasis Updater`。一部のセットアップには、SP Flash Tool ショートカットを持つ Toolkit フォルダーが含まれています。

### Linux

バンドルされたものを実行する `flash_tool` x86 / x86_64 上の Updater アプリ フォルダー内のバイナリ。プロジェクト インストーラーは udev ルールを使用して USB 権限を準備するため、接続時にプレーヤーが表示されるはずです。

### macOS

SP Flash Tool は macOS にはバンドルされていません。アップデーターは代わりに MTKClient ルートを使用します。を使用します。 [ガイド付きインストール](guide_ja.html) Mac では SP Flash Tool を維持し、Windows または Linux マシンでは SP Flash Tool を維持します。

このツールには MediaTek ダウンロード エージェントとモデル固有の構成が付属しているため、DA を収集したり、他の場所からファイルを分散したりする必要はありません。

## ファームウェアを準備する
  - 必要なリリースを取得します [ファームウェアのダウンロード](firmware_ja.html)。選ぶ `rom.zip` Y1 の場合、または `rom_y2.zip` Y2 の場合。
  - ZIP を独自のフォルダーに解凍します。 Windows では [すべて展開] を使用できます。 Linux では、アーカイブ マネージャーを使用するか、 `unzip` 端末内で。
  - 解凍したフォルダー内にスキャッターファイルがあることを確認してください。普通に名前が付けられている `MT6572_Android_scatter.txt` Y1 パッケージの場合と `MT6582_Android_scatter_def.txt` Y2 パッケージの場合、リリースによってはそのプロジェクトにちなんだ名前が付けられる場合があります。
モデルを別々にしておきます。 Y1 スキャッタは MT6572 デバイスを表し、Y2 スキャッタは MT6582 デバイスを表します。間違ったものをフラッシュすると、プレイヤーはレンガになってしまいます。 ZIP 内のスキャッターがモデルと一致しない場合は、停止し、モデル用にリストされているパッケージを代わりに使用してください。

## スキャッターとフラッシュをロードする
  - アップデーターのインストールフォルダーからSP Flash Toolを開きます。
  - [ダウンロード] タブで、 をクリックします。 選択してください [スキャッタロード ファイル] の横にある をクリックし、抽出されたフォルダからスキャッタ ファイルを選択します。パーティションリストが入力されます。
  - フラッシュモードはオンのままにしておきます ダウンロードのみ 意図的に完全なリカバリを行っている場合を除きます。 ファームウェアのアップグレード.
  - クリック ダウンロード。ツールはプレーヤーを待ちます。
  - プレーヤーの電源を完全にオフにしてから、USB データ ケーブルを接続します。プレーヤーを下に置き、動かさないでください。
  - Wait for the green check mark.その後、ケーブルを取り外してプレーヤーを起動してください。

ガイド付きルートと同じ USB ケーブルおよびタイミング ルールを維持します。つまり、データ ケーブルを使用し、ハブは使用せず、ツールの準備ができた場合にのみ接続します。

## 点滅しない場合
  - スキャッタと ZIP がプレーヤーに印刷されているモデルと一致していることを確認します。
  - 接続する前に、プレーヤーの電源が完全にオフになっていることを確認してください。
  - Windows では、アップデーターのセットアップで MediaTek ドライバーがインストールされていることを確認します。 Linux では、プロジェクト インストーラーから udev ルールを確認します。
  - ツールが待機しているときにのみケーブルを再接続してください。港湾競争では、完全なプラグを抜いて新しいものを必要とする場合があります。 ダウンロード クリック。

それ以上のものについては、開いてください [トラブルシューティング](troubleshooting_ja.html)。覚えておいてください: アップデーターは依然として通常のルートであり、 [Y1](guides/restore-original-y1.html) そして [Y2](guides/restore-original-y2.html) 復元ガイドもそれを使用します。

## これは役に立ちましたか?

あなたの回答はこのガイドの改善に役立ちます。はい、便利だと思いましたまだ[改善方法を教えてください](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
