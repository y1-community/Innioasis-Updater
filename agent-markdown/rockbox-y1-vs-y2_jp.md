---
title: "Rockbox-Y1 vs Rockbox-Y2: どちらのビルドがプレイヤーに属しているか"
description: "Innioasis Y1 と Y2 の Rockbox-Y1 と Rockbox-Y2 を比較します: 開発者リポジトリ、ROM パッケージ名、ビルド オプション、テーマ、および工場出荷時の復元パス。"
language: "jp"
source: "https://innioasis.app/rockbox-y1-vs-y2_jp.html"
---

# Rockbox-Y1 vs Rockbox-Y2: どちらのビルドがプレイヤーに属しているか

[← ファームウェアのダウンロード](firmware_ja.html?software=rockbox-y1)

Rockbox-Y1 · Rockbox-Y2

# Rockbox-Y1 対 Rockbox-Y2

Rockbox-Y1 と Rockbox-Y2 は、異なるプレーヤー用に作成された個別のファームウェア ビルドです。ビルドはプレーヤーに印刷されているモデルと常に一致させてください。[Rockbox-Y1 インストール](rockbox-y1/install.html)[Rockbox-Y2 インストール](rockbox-y2/install.html)[両方の ROM ダウンロード](rockbox-rom-download_ja.html)

## 並べて比較````[``](firmware_ja.html?model=Y1&software=rockbox-y1)[``](firmware_ja.html?model=Y2&software=rockbox-y2)``````

| 詳細 | Rockbox-Y1 | Rockbox-Y2 |
| --- | --- | --- |
| 選手モデル | Innioasis Y1 | Innioasis Y2 |
| 開発者プロジェクト | rockbox-y1/rockbox | spycemagic/y2-rockbox |
| 開発者 ROM パッケージ | rom.zip （そして rom_type_b.zip) | rom_y2.zip |
| Updater CE ダウンロードソース | 開発者のリリースから直接 | 開発者のリリースから直接 |
| ビルドオプション | 240p / 360p、Type A / Type B、安定した夜間 | バージョン付きのベータ版リリース |
| テーマ | 240p および 360p のテーマ コレクション | インストールされている Y2 ビルドに一致するテーマ |
| 工場出荷時の復元 | Y1 オリジナル ソフトウェア (Updater CE) | Y2 オリジナル ソフトウェア (Updater CE) |

## 最初にモデルを選択することが重要な理由

どちらのビルドも Rockbox を実行しますが、Innioasis Y1 と Y2 はハードウェアとパーティションのレイアウトが異なります。 Y2 で Y1 ROM を点滅させたり、Y1 で Y2 ROM を点滅させたりしないでください。

Innioasis Updater CE は、選択するとすぐに利用可能なソフトウェアをフィルタリングすることで不一致を防ぎます Y1 または Y2 で デバイスモデル。 Updater CE は常に、選択したパッケージをコミュニティ ファームウェア開発者のリリースから直接ダウンロードします (Updater CE にリリースをリストする責任は開発者にあります)。

## どのガイドが必要ですか?
  - Innioasis Y1 — に行きます [Rockbox-Y1 ハブ](rockbox-y1/)。 Type A (2.0.0 以降に同梱されたプレイヤーの場合) または Type B (古いユニットの場合) を選択し、240p または 360p ビルドを選択します。
  - Innioasis Y2 — に行きます [Rockbox-Y2 ハブ](rockbox-y2/)。 Updater CE で Y2 を選択し、最新の Y2 リリースを選択します。

## 両方のポートが共有するもの

どちらも Rockbox のタグベースの音楽データベース、ギャップレス再生、イコライザー、カスタム テーマ、プレーヤーでの 100% オフライン再生を実現します。読む [なぜ Rockbox](rockbox-benefits_ja.html) Rockbox が工場出荷時のソフトウェアに何を追加するかを確認します。[Y1 の Rockbox](rockbox-for-y1_ja.html)[Y2 の Rockbox](rockbox-for-y2_ja.html)[Rockbox の概要](rockbox_ja.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
