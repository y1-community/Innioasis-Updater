---
title: "SP Flash Tool for Mac · MediaTek スキャッター フラッシュ ガイドと代替案"
description: "Mac で Updater CE を使用して SP Flash Tool を使用し、Mechen H1、Innioasis Y1/Y2、Timmkoo、MT6580/MT6572 MP3 プレーヤーや電話などの MediaTek デバイスをフラッシュするスキャッタ ファイルを参照する方法。"
language: "jp"
source: "https://innioasis.app/sp-flash-tool-mac_jp.html"
---

# SP Flash Tool for Mac · MediaTek スキャッター フラッシュ ガイドと代替案

MediaTek ツールとクロスプラットフォーム フラッシュ

# SP Flash Tool for Mac: 完全ガイドとスキャッター ブラウザ

公式 MediaTek SP Flash Tool は macOS 上で実行できますか?正確なステータスは次のとおりです。 アップデーター CE Mac でのネイティブ MediaTek フラッシュ、およびスキャッターベースの MediaTek MP3 プレーヤーまたはスマートフォンをフラッシュする方法を提供します。

## macOS 上の SP Flash Tool の真実

MediaTek の公式 macOS ビルドはリリースされていません スマートフォンフラッシュツール (SP Flash Tool)。このツールは、これまで 32 ビット/64 ビット Windows アプリケーションおよび x86_64 Linux バイナリとしてのみ存在していました。 macOS カーネル USB 拡張機能では、BROM ブート ハンドシェイク中に必要な精度で USB シリアル パススルーが許可されていないため、Wine または CrossOver を介して macOS 上で SP Flash Tool をエミュレートすることは失敗します。

解決策:アップデーター CE は、ネイティブの Apple Silicon および Intel macOS フラッシュ ライブラリ (MTKclient 低レベル プロトコル エンジン経由) を自動化されたスキャター検出とバンドルすることで、このギャップを埋めます。

## 「ファイルからインストール」を使用して任意の MediaTek デバイスをフラッシュする (Scatter Browser)

Updater CE は Innioasis 人のプレイヤーに限定されません。必要なあらゆるデバイスの強力なユニバーサル MediaTek スキャッター フラッシャーとして使用できます。 SP Flash Tool v5 以前:
  - Mechen H1 & H11: MT6580 ポータブル HiFi Android プレーヤー。
  - Timmkoo Q3, Q5, G1, A5: MediaTek タッチスクリーン デジタル オーディオ プレーヤー。
  - オイルスキー、プフー、ルオラン: MediaTek MT6572 / MT6582 音楽プレーヤー。
  - 従来の MediaTek スマートフォンおよびフィーチャーフォン: MT6572、MT6580、MT6582、MT6735、MT6737、MT6739、MT6753、および MT8163 を実行しているデバイス。

### Updater CE にカスタム スキャッタ ファイルをロードする方法:
  - 工場出荷時のファームウェア アーカイブをダウンロードします (`.zip` または `.rar`) を含むフォルダーを抽出するか、 `*scatter*.txt` ファイル。
  - Updater CEで選択します ファイルを参照… ファームウェア選択画面で
  - スキャッター テキスト ファイル (例: `MT6580_Android_scatter.txt`) またはファームウェア zip パッケージ。
  - Updater CE はメモリ オフセット、パーティション アドレス (プリローダー、ブート、リカバリ、システム、ユーザーデータ) を解析し、分散整合性を検証します。
  - 画面上のライブ プロンプトに従ってください。デバイスの電源を切り、USB ケーブルをフラッシュに接続します。

## アンブリックのために x64 コンピューターが必要な場合

macOS は標準のフラッシュとカスタム ROM のインストールを MTKclient 経由でクリーンに処理しますが、深いブートループ障害 (プリローダー パーティションがワイプまたは不一致になった場合) から回復するには、SP Flash Tool の完全なパーティション テーブルの再構築が必要です。

Mac でエラー ストールが発生した場合は、64 ビット Windows PC または x86_64 Linux ワークステーションに切り替えて、 設定 > 詳細設定を表示 > フラッシュ方式 > SP Flash Tool、工場出荷時の分散パッケージをフラッシュします。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
