---
title: "Reborn (Y2Linux) - Innioasis Updater の Wi-Fi、Bluetooth、FM ラジオのセットアップ"
description: "Innioasis Y2 の Reborn (Y2Linux / Y2Reborn) の短いインストール後のガイド: system.img をコピーし、Wi-Fi、Bluetooth、FM ラジオをセットアップします。"
language: "ja"
source: "https://innioasis.app/y2reborn_wifibt_ja.html"
---

# Reborn (Y2Linux) - Innioasis Updater の Wi-Fi、Bluetooth、FM ラジオのセットアップ

Innioasis Y2 · Reborn ポストインストール

# Wi-Fi、Bluetooth、FM ラジオをセットアップします。

1 つのファイルをプレーヤーにコピーします。 Reborn が残りを処理します。[system.img をダウンロード (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[インストールガイド](guides/reborn-y2linux-y2.html)[なぜY2Reborn?](reborn-y2linux-benefits_ja.html)

## なぜこのファイルなのか?

Wi-Fi、Bluetooth、および FM ラジオには、Reborn が出荷できない 5 つの MediaTek ファームウェア モジュールが必要です。それらは公式 Y2 内にあります。 `system.img`。 Reborn はそれらを一度抽出して確認し、ファイルを削除します。

## 設定
  - system.img をダウンロード

v3.2.0 FM をダウンロードする `system.img` あなたのコンピュータに。[ system.img をダウンロード ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Reborn を 1 回起動します

プレーヤーの電源を入れます。待ってください ストレージのセットアップ 完了してから、一度再起動します。
  - コンピュータに接続する

USB データ ケーブルを使用します。プレイヤーは次のように表示されます 内部ストレージ.Mac で?

インストール [OpenMTP](https://openmtp.ganeshrvel.com/) プレーヤーを参照します。 Windows と Linux では自動的にマウントされます。
  - system.imgをファームウェアにコピー

という名前のフォルダーを作成します `Firmware` 内部ストレージのルートにあります。コピー `system.img` そこに。
  - セットアップが完了するまで待ちます

Reborn は無線ファームウェアを自動的にインストールし、削除します `system.img`。これには約 10 ～ 20 秒かかります。待ってください Wi-FiとBluetoothが準備されています.
  - Wi-Fi、Bluetooth、FMラジオを接続する
    - Wi-Fi： 「設定」→「システム」→「ネットワーク」→「Wi-Fi」。 2.4 GHz ネットワークを選択します。
    - ブルートゥース： ヘッドフォンをペアリングモードにします。 「設定」→「Bluetooth」→それらを選択します。
    - FMラジオ: 有線ヘッドフォンをアンテナとして接続し、FM ラジオを開きます。

  - Wi-Fi経由でアップデートする

今後の Reborn アップデートは、[設定] → [システム] → [ソフトウェア アップデート] からインストールされます。無線ファームウェアはそのまま残ります。

## このガイドは役に立ちましたか?

このインストール後のセットアップ ガイドは役に立ちましたか? はい、助かりました！ [ Discord について助けが必要です ](https://discord.gg/zHrT2zrcek) フィードバックをいただきありがとうございます。 Y2Reborn でワイヤレスリスニングをお楽しみください。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
