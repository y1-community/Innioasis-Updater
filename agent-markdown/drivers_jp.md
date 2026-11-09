---
title: "Innioasis Y1 および Y2 USB ドライバー | Windows ドライバーと Linux の権限 - Innioasis Updater"
description: "Innioasis Updater 用にコンピュータをセットアップします。Windows MediaTek ドライバと Linux USB 権限、さらにケーブルとタイミングの修正を行います。"
language: "jp"
source: "https://innioasis.app/drivers_jp.html"
---

# Innioasis Y1 および Y2 USB ドライバー | Windows ドライバーと Linux の権限 - Innioasis Updater

コンピュータのセットアップ

# プレーヤーの前にコンピューターを準備します。

接続の問題のほとんどは、ドライバー、権限、ケーブル、またはタイミングが原因で発生します。 Windows には MediaTek ドライバーがインストールされている必要があります。 Linux には適切な USB 権限が必要です。以下でプラットフォームを見つけてください。[Updater CE を入手](guide_ja.html#platform)[トラブルシューティング](troubleshooting_ja.html)

## Windows
  - 以下の MediaTek ドライバー インストーラーをダウンロードします。
  - インストーラーを実行し、Windows がドライバーをインストールできるようにします。
  - コンピュータを再起動します。
  - Updater CE を開き、接続プロンプトが表示されるまで待ってから、電源がオフになっているプレーヤーを接続します。

一部の Windows システムでは、コア分離 (メモリ整合性) によってドライバーがブロックされます。再起動後も Updater CE がプレーヤーを認識できない場合は、Windows セキュリティでメモリの整合性をオフにし、再起動してドライバーを再インストールします。システムで許可されている場合は、終了後に設定をオンに戻します。

Windows ではアプリが起動しませんか? Windows セキュリティまたは Smart App Control によって Updater CE が開かない場合は、開いてください。 設定 （プレス Win + I) → プライバシーとセキュリティ → Windows Security → アプリとブラウザの制御 → スマートアプリコントロールの設定 そしてそれを次のように設定します オフに設定してください。スマート アプリ コントロールは現在、Epic Overlay Service (Fortnite で使用) などの一般的なアプリケーションに影響を与えています。Updater CE は安全で検証済みです。後で再度有効にするには、 `VerifiedAndReputablePolicyState` 支援先: `1` (オン) または `2` (評価モード) `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` レジストリエディターで。[Windowsドライバーをダウンロードする](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[メインガイドに戻る](guide_ja.html#windows) · [ソフトウェアのダウンロード](firmware_ja.html)

## Linux USB 権限

Linux では、プレーヤー内の MediaTek USB チップとの通信を許可するには、ユーザー アカウントが必要です。 Updater CE は通常、インストール中にこれを解決し、同じ権限が SP Flash Tool にも適用されるため、これを通常の段階ではなく修正ステップとして扱います。
  - root としてではなく、通常のユーザーとして Updater CE を実行します。インストーラーは、必要な場合にのみ管理者アクセスを要求します。
  - プレーヤーがすべて見られることを確認してください。プレーヤーの電源をオフにし、ケーブルを接続し、ターミナルで lsusb コマンドを実行します。接続されたプレーヤーは、ベンダー ID 0e8d を持つ MediaTek デバイスとして表示されます。
`lsusb`
  - lsusb には表示されるが、Innioasis Updater CE または SP Flash Tool でアクセス許可が拒否された、またはポートを開けないというメッセージが表示される場合、ユーザーは USB デバイスにアクセスできません。同じ udev ルールが両方のツールに適用されるため、ユーザー グループがそれを読み取れるようにするルールを追加します。
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

その行を /etc/udev/rules.d/51-innioasis.rules という名前の新しいファイルに保存し、次を実行します。`sudo udevadm control --reload && sudo udevadm trigger`
  - プレーヤーを完全に取り外し、再度接続して、インストールを再試行してください。
  - SP Flash Tool がシリアル許可またはポート競合を報告した場合は、プラグを完全に取り外し、プロンプトが表示された場合にのみ再接続してください。
フラッシュのオフセットを即興で調整しないでください。手動回復ツールに移行する場合は、プロジェクトに付属のファイルとモデル固有の構成を使用してください。

[メインガイドに戻る](guide_ja.html#linux) · [ソフトウェアのダウンロード](firmware_ja.html) · [SP Flash Tool ガイド](sp-flash-tool_ja.html)

## ケーブルとタイミング
  - 既知の USB データ ケーブルを使用してください。
  - トラブルシューティング中はハブを避けてください。
  - 正しいモデルの電源を完全にオフにします。
  - プロンプトでのみ接続します。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
