---
title: "Y1 (Rockbox-Y1) の Rockbox: 概要、ビルド、インストール ガイド"
description: "Y1、Rockbox-Y1、および Rockbox-y1 の Rockbox はすべて、Innioasis Y1 のコミュニティ Rockbox ファームウェアを参照します。何が追加されるのか、どのビルドを選択すればよいのか、Innioasis Updater CE を使用してインストールする方法を学びましょう。"
language: "jp"
source: "https://innioasis.app/rockbox-for-y1_jp.html"
---

# Y1 (Rockbox-Y1) の Rockbox: 概要、ビルド、インストール ガイド

[← ファームウェアのダウンロード](firmware_ja.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Y1 の Rockbox (Rockbox-Y1)

「Rockbox」、「Rockbox-Y1」、および「Y1 の Rockbox」はすべて、Innioasis Y1 の同じコミュニティ Rockbox ファームウェアを参照します。プレーヤーに何を追加するか、どのビルドを選択するか、Innioasis Updater CE を使用してインストールする方法は次のとおりです。[Rockbox-Y1 をインストールします](rockbox-y1/install.html)[ROM をダウンロードします](rockbox-y1/download.html)[書かれたチュートリアル](guides/rockbox-y1.html)[Rockbox-Y1 ハブ](rockbox-y1/)

## 1 つのファームウェアに複数の名前

Innioasis Updater CE では、このファームウェアは次のように表示されます Rockbox デバイスモデルを選択するとき Y1。ガイド、ビデオ、リリース ノートでもこのように呼ばれています。 Rockbox-Y1 または Y1 の Rockbox したがって、ビルドは Y1 用であり、Y2 用ではないことは明らかです。

インストールする前に、プレーヤーに印刷されているモデルを必ず確認してください。 Y1 および Y2 ファームウェア パッケージには互換性がありません。

## Rockbox-Y1 が Y1 に追加するもの

Rockbox-Y1 は、Innioasis Y1 用のオープンソース Rockbox 音楽プレーヤー ファームウェアのコミュニティ ポートです。
  - タグベースの音楽ライブラリ — オーディオタグを使用してアーティスト、アルバム、ジャンル、年ごとに参照するか、フォルダーを直接参照します。
  - 高度なオーディオ再生 — ギャップレス再生、クロスフェード、リプレイゲイン、フルイコライザー。
  - カスタムテーマ — クラシックな iPod スタイルのレイアウトを含む、数百もの 240p および 360p コミュニティ テーマから選択します。
  - FMラジオ — 内蔵 FM ラジオのサポート。
  - オプションの追加物 — Wi-Fi 経由でポッドキャストをダウンロードし、サポートされているビルドで Last.fm / ListenBrainz / Maloja をスクロブルします。
  - デュアルブート — サポートされているビルドを再フラッシュせずに、工場出荷時のオリジナル ソフトウェアに切り替えます。

## どの Y1 ビルドを選択すればよいですか?
  - 240p 対 360p — 240p ビルドは、クラシックな 320×240 Rockbox テーマで動作します。 360p ビルドでは、より鮮明な 480×360 Y1 テーマが使用されます。ビルド解像度を使用するテーマに合わせます ([240p 対 360p ガイド](rockbox-y1/resolution.html)).
  - Type A 対 Type B — Type A は、工場出荷時のソフトウェア 2.0.0 以降が付属している Y1 プレーヤー用です。 Type B は以前の Y1 ユニット用です。 Y1 が Type B であることがわかっていない限り、Type A を選択してください。
  - 安定版と夜間版 — 毎日のリスニング用に安定したビルドを選択するか、最新の変更をテストするために夜間ビルドを選択します。

## コミュニティ開発者からの直接ダウンロード

Innioasis Updater CE は常にコミュニティ ファームウェア開発者からファームウェア パッケージを直接ダウンロードします ([rockbox-y1/rockbox](firmware_ja.html?model=Y1&software=rockbox-y1))、開発者自身がソフトウェア リリースを Updater CE にリストすることに単独で責任を負います。

Updater CE にファームウェアを自動的にダウンロードしてインストールさせることも、弊社から ROM パッケージをダウンロードさせることもできます。 [Rockbox-Y1 ダウンロード ページ](rockbox-y1/download.html) そして [Rockbox ROM ダウンロード ページ](rockbox-rom-download_ja.html).[Rockbox-Y1 ダウンロード数](rockbox-y1/download.html)[ローカル ZIP からインストールする](rockbox-y1/portable-zip.html)

## Rockbox-Y1 のインストール方法
  - Innioasis Updater CEを開いて設定します デバイスモデル 支援先: Y1.
  - 選択 Rockbox で ソフトウェア.
  - 安定したリリースを選択します (または、夜間ビルドを有効にしてプレビューをテストします)。
  - クリック インストール / 復元 したがって、Updater CE は開発者からパッケージを直接ダウンロードします。
  - Updater CE のプロンプトが表示されたら、Y1 の電源を完全にオフにし、USB データ ケーブルで接続します。
  - 完了メッセージが表示されるまで待ってから、プレーヤーを切断して電源を入れます。

スクリーンショットと詳細なセットアップのヒントについては、「 [完全な Rockbox-Y1 チュートリアル](guides/rockbox-y1.html).

## 元の Y1 ソフトウェアの復元

いつでも工場出荷時のソフトウェアに戻ることができます: を選択してください Y1 そして 純正ソフトウェア Updater CE で安定したリリースを選択し、 インストール / 復元。 MicroSD カードの音楽は保存されます。を参照してください。 [復元ガイド](rockbox-y1/restore-stock.html) そして [Y1 オリジナル ソフトウェア ページ](original-software-y1_ja.html).

## よくある質問Y1 の Rockbox は Rockbox-Y1 と同じですか?

はい。 Y1 の Rockbox、Rockbox-Y1、Rockbox、および `rockbox-y1` すべては Innioasis Y1 の同じコミュニティ Rockbox ポートを参照します。Updater CE は Rockbox-Y1 をどこからダウンロードしますか?

Updater CE は常に、コミュニティ ファームウェア開発者自身のリリースからファームウェア パッケージを直接ダウンロードします (`rockbox-y1/rockbox`）。開発者は、ソフトウェア リリースを Updater CE にリストすることに単独で責任を負います。Rockbox-Y1 を Y2 にインストールできますか?

いいえ。Y2 には独自の個別のファームウェア ビルドがあります。使用 [Y2 の Rockbox](rockbox-for-y2_ja.html) その代わり。Rockbox-Y1 をインストールすると音楽は消去されますか?

いいえ。音楽は MicroSD カードに保存されており、プレーヤーの内部ファームウェアをフラッシュしても影響を受けません。

## 関連ガイド

### [Rockbox-Y1 ハブ](rockbox-y1/)

すべての Y1 ガイド: インストール、ダウンロード、テーマ、復元、デュアル ブート、トラブルシューティング。

### [Rockbox-Y1 対 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 ビルドと Y2 Rockbox ビルドの違い。

### [Rockbox-Y1 テーマ](rockbox-y1-themes.html)

Updater CE を使用して 240p および 360p テーマを転送する方法。

### [Rockbox の概要](rockbox_ja.html)

Innioasis Y1 プレーヤーと Y2 プレーヤーの Rockbox の紹介。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
