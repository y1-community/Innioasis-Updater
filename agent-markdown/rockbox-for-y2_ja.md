---
title: "Y2 (Rockbox-Y2) の Rockbox: 概要、ビルド、インストール ガイド"
description: "Y2、Rockbox-Y2、および Rockbox-y2 の Rockbox は、Innioasis Y2 のコミュニティ Rockbox ファームウェア ポートを参照します。これに含まれるものと、Innioasis Updater CE を使用してインストールする方法を学びます。"
language: "ja"
source: "https://innioasis.app/rockbox-for-y2_ja.html"
---

# Y2 (Rockbox-Y2) の Rockbox: 概要、ビルド、インストール ガイド

[← ファームウェアのダウンロード](firmware_ja.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Y2 の Rockbox (Rockbox-Y2)

Rockbox-Y2 (Y2 の Rockbox とも呼ばれます) は、Innioasis Y2 の専用コミュニティ Rockbox ファームウェア ポートです。独自の ROM パッケージを使用します (`rom_y2.zip`) であり、Innioasis Updater CE を通じて直接インストールされます。[Rockbox-Y2 をインストールします](rockbox-y2/install.html)[ROM をダウンロードします](rockbox-y2/download.html)[書かれたチュートリアル](guides/rockbox-y2.html)[Rockbox-Y2 ハブ](rockbox-y2/)

## Innioasis Y2 専用に構築

Innioasis Updater CE では、このファームウェアは次のようにリストされます。 Rockbox いつ Y2 が選択されます。そのリリースは、 [spycemagic/y2-rockbox](firmware_ja.html?model=Y2&software=rockbox-y2) パッケージ名のプロジェクト `rom_y2.zip`.

Y1 ファームウェア パッケージを Y2 にインストールしないでください。選択中 Y2 Updater CE では、リリース リストが Y2 と互換性のあるビルドのみに自動的にフィルターされます。

## Rockbox-Y2 が提供するもの
  - タグベースの音楽ライブラリ — オーディオ ファイルのタグからアルバム、アーティスト、ジャンルを参照するか、フォルダーを直接参照します。
  - 再生コントロール — ギャップレス再生、クロスフェード、リプレイゲイン、イコライザー設定。
  - カスタムテーマ — Rockbox-Y2 ビルドと互換性のあるテーマをインストールします ([Y2 テーマ ガイド](rockbox-y2-themes.html)).
  - 100%オフライン — アカウントやサブスクリプションなしで MicroSD カードからローカル ファイルを再生します。
  - 簡単な工場出荷時の復元 — Updater CEでいつでもY2の元のソフトウェアに戻ります。

## Rockbox-Y2 リリースの選択
  - 常に選択する Y2 で デバイスモデル まず。
  - 特定のバージョンをテストする場合を除き、最新のリリースを選択してください。
  - 読んでください [Rockbox-Y2 リリースノート](release-notes/rockbox-y2/index_ja.html) 各ビルドで何が変更されたかを確認します。

## コミュニティ開発者からの直接ダウンロード

Innioasis Updater CE は常にコミュニティ ファームウェア開発者からファームウェア パッケージを直接ダウンロードします ([spycemagic/y2-rockbox](firmware_ja.html?model=Y2&software=rockbox-y2))、これらの開発者はソフトウェア リリースを Updater CE にリストする責任を単独で負います。

Updater CE をダウンロードしてフラッシュすることができます `rom_y2.zip` 自動的にパッケージをダウンロードするか、弊社からパッケージをダウンロードします。 [Rockbox-Y2 ダウンロード ページ](rockbox-y2/download.html) そして [Rockbox ROM ダウンロード ページ](rockbox-rom-download_ja.html).[Rockbox-Y2 ダウンロード数](rockbox-y2/download.html)[ローカル ZIP からインストールする](rockbox-y2/portable-zip.html)

## Rockbox-Y2 のインストール方法
  - Innioasis Updater CEを開いて設定します デバイスモデル 支援先: Y2.
  - 選択 Rockbox で ソフトウェア.
  - リストから Y2 リリースを選択します。
  - クリック インストール / 復元 したがって、Updater CE は開発者からパッケージを直接ダウンロードします。
  - Updater CE の要求に応じて、Y2 の電源を完全にオフにし、USB データ ケーブルで接続します。
  - 完了メッセージが表示されるまで待ってから、プラグを抜き、Y2 の電源を入れます。

完全なステップバイステップのチュートリアルについては、「 [Rockbox-Y2 チュートリアル](guides/rockbox-y2.html).

## 元の Y2 ソフトウェアの復元

工場出荷時のファームウェアに戻すには、次を選択します。 Y2 そして 純正ソフトウェア Updater CE で安定したリリースを選択し、 インストール / 復元。を参照してください。 [復元ガイド](rockbox-y2/restore-stock.html) そして [Y2 オリジナル ソフトウェア ページ](original-software-y2_ja.html).

## よくある質問Updater CE は Rockbox-Y2 をどこからダウンロードしますか?

Updater CE は常に、コミュニティ ファームウェア開発者自身のリリースからファームウェア パッケージを直接ダウンロードします (`spycemagic/y2-rockbox`）。開発者は、ソフトウェア リリースを Updater CE にリストすることに単独で責任を負います。パッケージの名前が rom_y2.zip なのはなぜですか?

開発者は Y2 ファームウェア アーカイブに名前を付けます `rom_y2.zip` したがって、Y1 と混同することはできません `rom.zip`.Y1 テーマは Y2 で動作しますか?

いつもではありません。 Y2 ビルドのリリース ノートを確認し、 [Rockbox-Y2 テーマ ガイド](rockbox-y2-themes.html).

## 関連ガイド

### [Rockbox-Y2 ハブ](rockbox-y2/)

すべての Y2 ガイド: インストール、ダウンロード、テーマ、復元、デュアル ブート、トラブルシューティング。

### [Rockbox-Y1 対 Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 ビルドと Y2 Rockbox ビルドの違い。

### [Rockbox-Y2 テーマ](rockbox-y2-themes.html)

Rockbox-Y2 にテーマをインストールしてリセットしています。

### [Y1 の Rockbox](rockbox-for-y1_ja.html)

Innioasis Y1 ポートの概要とインストール ガイド。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
