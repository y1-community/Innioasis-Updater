---
title: "ファームウェアのインストールとストック復元ガイド | Innioasis Updater CE - Innioasis ファームウェアのダウンロード"
description: "Innioasis Y1、Y2、G1、G3、G5、R1、PR1、および Timmkoo、Q5、Q3 に Innioasis Updater CE を使用してカスタム ファームウェアをインストールするか、公式の工場出荷時のストック ファームウェアを復元します。"
language: "jp"
source: "https://innioasis.app/firmware-guide_jp.html"
---

# ファームウェアのインストールとストック復元ガイド | Innioasis Updater CE - Innioasis ファームウェアのダウンロード

ファームウェアのインストールおよびストック復元ガイド

# デバイスにファームウェアをインストールまたは復元する

プレーヤーに印刷されているモデルを選択してください。次に、Updater CE の手順に従います。残りはそれが処理します。[Updater CE を入手](guide_ja.html#platform)[ファームウェアアーカイブを参照](firmware_ja.html)[トラブルシューティング](troubleshooting_ja.html)

プレーヤーに印刷されているモデルと必要なソフトウェアを選択して、このガイドを開きます。 [モデルごとにソフトウェアとストックファームウェアを参照](firmware_ja.html).

## 

[Updater CE を入手](guide_ja.html#download-updater)[完全な書面によるチュートリアル](guide_ja.html)

## Innioasis Updater CEを取得

Updater CE をまだ入手していない場合は、ここから始めてください。Updater CE で入手ガイド付きインストールあり

### Windows

インストーラーをダウンロードして開き、セットアップのプロンプトに従います。[ドライバーのダウンロードとインストール](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[アプリとドライバーをダウンロードする](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[エッジによってブロックされましたか?](#)

Windows によってアプリの実行が停止されたり、起動されない場合は、[設定] を開き、[プライバシーとセキュリティ] → [Windows セキュリティ] → [アプリとブラウザー コントロール] をクリックして、スマート アプリ コントロールをオフにしてください。 [Windows ではアプリが起動しませんか?ヘルプ](#smart-app-control)

動作させるには、インストール後に PC を再起動する必要があります。

### macOS

アプリをダウンロードし、「アプリケーション」に移動します。 macOS がブロックする場合は、[システム設定]、[プライバシーとセキュリティ] の順に開き、[とにかく開く] をクリックします。 [仕組み](https://support.apple.com/en-gb/102445#openanyway)[ダウンロード Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Intel および AMD システム用の AppImage をダウンロードし、実行可能にして実行します。[Intel/AMD 用の AppImage をダウンロード](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linux セットアップに関するメモ](drivers_ja.html#linux)別のプラットフォームですか？

コンピューターのセットアップに関する詳細なメモが必要ですか?を開きます [Windows](drivers_ja.html#windows) または [Linux](drivers_ja.html#linux) セットアップガイド。

## 元のソフトウェアに戻る

戻るには、モデルを選択し、 純正ソフトウェア、実行します インストール / 復元。以上です。アップデーターはシステム ソフトウェアを置き換えます。[Y1 復元ガイド](guides/restore-original-y1.html)[Y2 復元ガイド](guides/restore-original-y2.html)

## モデル別ソフトウェアガイド

モデルを選択して、ソフトウェアのガイドを開きます。

### Innioasis Y1

Y1 用のソフトウェア:

### Innioasis Y2

Y2 用のソフトウェア:

2 つのツールに関するメモ

## どのツールを使用すればよいですか?

Innioasis アップデータ CE プレーヤーを更新する最も安全な方法です。音楽、ビデオ、Bluetooth のペアリングを維持します。アップデートの準備が完了すると通知されます。 Windows、macOS、Linux 上で動作します。 Innioasis Universal Flash Tool はプレーヤーをワイプし、より少ないコンピューターで動作します。[完全な比較を開く](updater-comparison_ja.html)

### Windows ではアプリが起動しませんか?スマートアプリコントロールをオフにする方法

Windows Defender SmartScreen または Smart App Control は、署名の評価が伝播する前に、新しくダウンロードされたコミュニティ アプリケーションをブロックできます。 Smart App Control は現在、Epic Overlay Service (Fortnite で使用) などの人気のあるアプリケーションに影響を与えています。Updater CE は安全で、使用が検証されています。 Smart App Control をオフにすると、Updater CE が正常に開いて実行できるようになります。
  - 開く 設定 Windows PC 上で ( Win + I).
  - クリック プライバシーとセキュリティ 左側のサイドバーで をクリックし、 Windows Security.
  - クリック アプリとブラウザの制御.
  - 下 スマートアプリコントロール、 クリック スマートアプリコントロールの設定.
  - トグルを次のように設定します オフ Updater CE の起動を許可します。

エッジによってブロックされましたか? Microsoft Edge がダウンロード自体をブロックする場合は、[その他のオプション] ボタン (…) → 保つ → もっと見る → とにかく保管してください.

後でスマート アプリ コントロールを再度有効にします。 スマート アプリ コントロールをオンに戻したい場合は、次の Windows レジストリから再度有効にすることができます。 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` 設定により `VerifiedAndReputablePolicyState` 支援先: `1` (オン) または `2` （評価モード）して再起動します。ヘルプを閉じる

## これは役に立ちましたか?

あなたの回答はこのガイドの改善に役立ちます。はい、便利だと思いましたまだ[改善方法を教えてください](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
