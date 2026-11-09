---
title: "Innioasis Y1 - Innioasis ファームウェアのダウンロードに Rockbox をインストールする方法"
description: "デバイス モデル、ソフトウェア、インストール/復元、および実際のアップデータ接続フローを使用して、Rockbox を Innioasis Y1 にインストールします。"
language: "jp"
source: "https://innioasis.app/guides/rockbox-y1_jp.html"
---

# Innioasis Y1 - Innioasis ファームウェアのダウンロードに Rockbox をインストールする方法

Rockbox · Innioasis Y1

# Y1 に Rockbox をインストールします。

これは、ガイド付きアップデーター ルートの Y1 バージョンです。言語をアプリの近くに保ちます。[Updater CE を入手](../guide_jp.html#platform)[Updater CE で入手](../guide_jp.html?model=Y1&software=rockbox-y1)[なぜRockbox?](../rockbox-benefits_jp.html)

お使いのコンピューターのインストールガイド

## コンピュータを使用して Y1 に Rockbox をインストールします

使用しているコンピュータのガイドを選択してください。 すべてのバージョンには、プラットフォームのセットアップ、Updater CE の手順、および在庫に戻る方法が含まれています。[Windowsガイド](/install/rockbox-y1-windows.html)[macOS ガイド](/install/rockbox-y1-mac.html)[Linuxガイド](/install/rockbox-y1-linux.html)

[すべての Innioasis Y1 ガイド](/install/y1.html) · [すべての Rockbox ガイド](/install/rockbox.html)

## 必要なもの

Innioasis Y1、充電済みバッテリー、USB データ ケーブル、および Innioasis Updater CE がインストールされたコンピューター (まだインストールしていない場合は、 [Updater CE を入手](../guide_jp.html#platform) Windows、macOS、または Linux の場合）。 Type A は、オリジナル ソフトウェア バージョン 2.0.0 以降が付属する Y1 プレーヤーに適しています。 Type B は、以前のバージョンに同梱されていたプレーヤーに適しています。 [純正ソフトウェア](../firmware_jp.html?software=original-y1)。プレーヤーに Type B ビルドが必要であることがすでにわかっている場合を除き、Type A から始めてください。

## Rockbox ルートを見る

Frawgeeys によるビデオ。 Y1 と Y2 の両方のモデルで機能します。Innioasis Updater CE で、 Y1 あなたのモデルとして。以下に記載されている手順は、Y1 のインストール シーケンスをカバーしています。

ビデオ: [クリスティアンプラザ](https://www.youtube.com/@CristianPlaza) (スペイン語)、Rockbox インストール段階から開始します。以下に記載されている手順は、Y1 シーケンスをカバーしています。

## アップデーター内
  - Updater CE を開きます (または次のコマンドで起動します) [Updater CE で入手](../guide_jp.html?model=Y1&software=rockbox-y1)) を設定してください デバイスモデル 支援先: Y1.
  - 選択してください Rockbox で ソフトウェア。正確なプロジェクト ラベルは、リリース データでは Rockbox-Y1 として表示される場合があります。
  - 安定したリリースを選択してください。 240p ビルドには、最も幅広い古いテーマの互換性があります。 360p ビルドは Y1 テーマ パスを対象としています。違いが重要な場合は、リリース ノートを確認してください。
  - クリック インストール / 復元。 Updater CE がコミュニティ開発者のリリースからパッケージを直接ダウンロードして準備するまで待ちます。
Y1 に対して Rockbox が選択されたことを示すアップデーターY1 に対して Rockbox が選択されたことを示すアップデーター。Rockbox リリースの選択肢を示すアップデーターモデルとソフトウェアが正しい場合は、リリースを選択してください。

## Y1を接続します
  - Updater がプレーヤーを要求するまで待ちます。
  - Y1 の電源を完全にオフにします。シャットダウンしない場合は、アップデーターが表示する復旧手順をご利用ください。
  - USB データ ケーブルは、アプリが指示した場合にのみ接続してください。プレーヤーを置き、接続を妨げないでください。
  - アップデータが成功を確認した後でのみ切断し、Y1 を開始します。
Updater への接続手順接続の文言はプラットフォームによって異なる場合があります。ライブプロンプトに従ってください。

## 元のソフトウェアに戻る

Rockbox はカスタム ソフトウェアに閉じ込められることはありません。アップデーターをコンピューターにセットアップしたら、Windows、macOS、または Linux で使用します。 Y1、 選ぶ 純正ソフトウェア、実行します インストール / 復元.
  - Updater がストック パッケージの準備を完了するまで待ちます。
  - アプリが尋ねたら、Y1 の電源を切ります。
  - USB データ ケーブルはライブ プロンプトでのみ接続してください。
  - 成功メッセージが表示されるまでプレーヤーを動かさないでください。

Y2 パッケージを使用したり、復元前に Rockbox ファイルを手動で削除したりしないでください。 Type B ホイールの動作については、デバイス タイプを変更する前に、一致するリリース バリアントを確認してください。[Y1 復元ガイド](restore-original-y1_jp.html)[トラブルシューティング](../troubleshooting_jp.html)

## その他の Rockbox-Y1 ガイド

Rockbox-Y1 のインストール、ダウンロード、テーマ設定、復元、トラブルシューティングに関するその他のガイドを参照してください。[Rockbox-Y1 ハブ](../rockbox-y1/)[Rockbox-Y1 ROM ダウンロード](../rockbox-y1/download.html)[ローカル ZIP からインストールする](../rockbox-y1/portable-zip.html)[Y1 の Rockbox](../rockbox-for-y1_jp.html)[Rockbox-Y1 テーマ](../rockbox-y1-themes_jp.html)[Rockbox-Y1 対 Y2](../rockbox-y1-vs-y2_jp.html)[Rockbox-Y2 ハブ](../rockbox-y2/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
