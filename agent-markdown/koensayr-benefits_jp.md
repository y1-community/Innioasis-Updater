---
title: "なぜ Koensayr が Innioasis Y1 なのか | Koensayr の特典 - Innioasis ファームウェアのダウンロード"
description: "Koensayr は、インターフェイスを変更せずに、ストックの Y1 ファームウェアにパッチを適用します。アーティストからアルバムへのナビゲーションと AVRCP 1.3 Bluetooth メタデータおよびカー ステレオのコントロールです。"
language: "jp"
source: "https://innioasis.app/koensayr-benefits_jp.html"
---

# なぜ Koensayr が Innioasis Y1 なのか | Koensayr の特典 - Innioasis ファームウェアのダウンロード

カスタム ソフトウェア · Koensayr

# Innioasis Y1 に Koensayr を選択する理由

Koensayr は使い慣れたインターフェイスを維持し、気になる点を修正します。音楽はアーティストごとに閲覧でき、Bluetooth はトラック名を表示し、車のコントロールと連動します。[アップデーターで Koensayr を取得](guide_ja.html?model=Y1&software=koensayr-y1)[Y1 インストールページ](koensayr-y1-software_ja.html)

## モデルの入手可能性

どの Innioasis モデルで実行されますか?[Y1 · 利用可能](koensayr-y1-software_ja.html)Y2 · 利用できません

Y1 ビルドと Y2 ビルドは別個であるため、ソフトウェア ダウンロードでプレーヤー用に作成されたビルドを入手してください。一方をもう一方と交換しないでください。

## 人々がそれを選ぶ理由

ストックプレーヤーはそのままにしておきます。気になる部分を修正します。
  - アーティスト→アルバムナビゲーション — ストック ミュージック アプリには、これまで欠けていたアーティストからアルバムへのフローが得られ、フォルダーを探す必要がなくなりました。
  - 車の中で使えるBluetooth — 仕様に準拠した AVRCP 1.3 メタデータとコントロール: ヘッドユニットはトラック タイトル、再生ヘッド、リピート/シャッフル状態を認識します。
  - 実際にペアリングするペアリング — 自動ペアリングの修正を含む、カーステレオとヘッドセット用に調整されたオーディオとペアリング構成。
  - 必要なときにroot化する — adb エスカレーション用に最小限の setuid su がインストールされます。診断やいじくりに役立ちます。
  - むくみが少なくなる — 使用されていないシステム アプリは削除され、RAM が解放され、バックグラウンド作業が軽減されます。
  - 学習曲線が不要 — インターフェイスは Y1 インターフェイスです。 Koensayr は見た目ではなく動作を変更します。

## コミュニティ

コミュニティの意見

Koensayr は、標準の Y1 インターフェースが好きで、単にイライラする部分を修正したい人のためのソフトウェアです。その名前はスター・ウォーズのディープカットです。Koensayr が Y ウイングを構築し、Y ウイングは Y1 につながります。

コミュニティで最も話題になっている勝利は Bluetooth です。カー ステレオとヘッドセット (AVRCP 1.3) の適切なトラック メタデータとコントロールですが、標準ソフトウェアが間違っていることは有名です。車の中に住んでいるなら、これが人々に勧められるソフトウェアです。
  - [r/innioasis · Koensayr と車の Bluetooth](https://www.reddit.com/r/innioasis/)

## プロジェクトが提供するもの
  - アーティスト → アルバム ナビゲーションがシステム ミュージック APK にパッチされました
  - AVRCP 1.3 メタデータとコントロール: フルトラックメタデータ、ミリ秒精度の再生ヘッド、トラックとバッテリーの通知、双方向リピート/シャッフル
  - Bluetooth ペアリングの修正: audio.conf、auto_pairing.conf、blacklist.conf、および build.prop の車とヘッドセットのペアリングの編集
  - adb エスカレーションのための最小限の setuid su を介した root アクセス。在庫のadbdはそのまま残ります
  - システムのデブロート — プリインストールされたブロートウェアが削除されました
  - build.prop でのオプションの ADB の有効化
  - 実際のハードウェアでの Bluetooth の動作を調査するための診断ツール

## 最初に知っておくべきこと
  - 現在は Y1 のみであり、ストック インターフェイスが維持されます。これはランチャーではなくパッチャーです。
  - これは最も技術的なルートです。パッチャーは Linux ホスト上で実行され、MTKClient 経由でフラッシュされるため、自信のあるユーザーに適しています。
  - このプロジェクトは既知のストック ソフトウェアのみにパッチを当てます - ソフトウェアのバージョンが一致していることを確認してください
  - 気が変わったら、モデルの元のソフトウェアを復元することはまだ後戻りできません

## 始めましょう

Updater で Y1 を選択し、Koensayr を選択して、リリース ノートに従います。このチュートリアルでは、パッチャー フローを順番に説明します。[Koensayr のリリースを参照する](firmware_ja.html?model=Y1&software=koensayr-y1)[Y1 チュートリアル](guides/koensayr-y1.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
