---
title: "Innioasis PR1 で元のソフトウェアを復元する - ステップバイステップ"
description: "検証済みの rom_pr1.zip パッケージを使用して、Innioasis Updater CE または SP Flash Tool を含む Innioasis PR1 上の公式のオリジナル ソフトウェアを復元する方法。"
language: "ja"
source: "https://innioasis.app/guides/restore-original-pr1_ja.html"
---

# Innioasis PR1 で元のソフトウェアを復元する - ステップバイステップ

復元ガイド · Innioasis PR1

# Innioasis PR1 で元のソフトウェアを復元します

プレーヤーに同梱されていたソフトウェアに完全に戻りました。アップデートに失敗した後、プレーヤーを販売する前、またはカスタム システムが自分に合わないときはいつでも、これを使用してください。[Updater CE を入手](../guide_ja.html#platform)[PR1 ダウンロード数](../firmware_ja.html?model=PR1)[PR1 マニュアル](../manuals/pr1.html)

お使いのコンピューターのインストールガイド

## コンピュータを使用して PR1 上の元のソフトウェアを復元します

使用しているコンピュータのガイドを選択してください。 すべてのバージョンには、プラットフォームのセットアップ、Updater CE の手順、および在庫に戻る方法が含まれています。[Windowsガイド](/install/original-pr1-windows.html)[macOS ガイド](/install/original-pr1-mac.html)[Linuxガイド](/install/original-pr1-linux.html)

[すべての Innioasis PR1 ガイド](/install/pr1.html) · [すべてのオリジナル ソフトウェア ガイド](/install/original-software.html)

## 必要なもの
  - Windows、macOS、または Linux コンピューター。 Updater CE は 3 つすべてで実行されます。
  - プレーヤーに付属の USB データ ケーブル。充電専用ケーブルは動作しません。
  - 役人 `rom_pr1.zip` アップデータがダウンロードするパッケージ、または [PR1 アーカイブ](../firmware_ja.html?model=PR1) 手動でフラッシュしたい場合。
  - プレーヤーに充電します。電源を失った状態での復元は、悪い状況をさらに悪化させる唯一の一般的な方法です。

これにより、システムが置き換えられ、内部ストレージが消去されます。 まず音楽、録音、写真をコンピュータにコピーします。

## ルートA: Updater CE (推奨)
  - インストール [Innioasis アップデーター CE](../guide_ja.html#platform) そしてそれを開きます。
  - セット デバイスモデル 支援先: PR1。モデルはプレーヤーと正確に一致する必要があります。
  - 選択してください 純正ソフトウェア ソフトウェアリストにある。
  - リリースを選択します。最新の安定したビルドが安全なデフォルトです。
  - プレス インストール / 復元 パッケージがダウンロードされて解凍されるまで待ちます。
  - プレーヤーの電源を完全にオフにし、アップデーターが要求した場合にのみ USB ケーブルを接続します。
  - 成功メッセージが表示されるまで、プレーヤーやケーブルに触れないでください。接続を外してプレーヤーを起動します。
「動作させる」ために別のモデルを選択しないでください。 PR1 には PR1 パッケージが必要です。モデルを混合すると、プレイヤーは手動での回復が必要になります。

## ルートB: SP Flash Tool (手動)

コンピューターで Updater CE を実行できない場合、または既にパッケージを持っていて従来のツールを使用したい場合に、これを使用します。
  - ダウンロード `rom_pr1.zip` からの [PR1 アーカイブ](../firmware_ja.html?model=PR1) そしてそれを解凍します。
  - スキャッタファイルを画像の隣に置いてください。画像の名前を変更したり、移動したりしないでください。
  - SP Flash Tool を開き、選択します ダウンロードのみをクリックして、スキャッタ ファイルをロードします。
  - プレーヤーの電源を切り、 を押します ダウンロードを選択し、ケーブルを接続します。
  - 切断する前に、緑色の成功マークが点灯するまで待ちます。

の [SP Flash Tool ガイド](../sp-flash-tool_ja.html) ドライバーと Windows プロンプトについて詳しく説明します。 Linux および macOS では、Updater CE が独自の USB 処理を行うため、より簡単なルートです。

## 復元後
  - プレーヤーを切断し、自動的に起動できるようにします。
  - 言語を選択し、時計を設定します。
  - Wi-Fi または Bluetooth を使用している場合は、それらに再接続します。
  - 音楽をコピーして戻します。の [乗換案内](../manuals/transfer-music.html) フォルダ名が付いています。

プレーヤーは起動しても、画面、ホイール、またはボタンの動作がまだ正しくない場合は、復元は機能しています。それはハードウェアまたはセットアップの問題であり、ソフトウェアの問題ではありません。の [トラブルシューティングガイド](../troubleshooting_ja.html) 次の停留所です。

## うまくいかない場合

### アップデーターはプレーヤーを決して認識しません

ケーブルを変更し、次に USB ポートを変更します。ハブは避けてください。 Windows では、MediaTek ドライバーを次の場所からインストールします。 [ドライバーページ](../drivers_ja.html).

### フラッシュが早く止まる

再接続し、プレーヤーを充電して、もう一度開始してください。別のモデルのパッケージに切り替えないでください。

### プレイヤーは黒のままです

1 時間充電してから、10 秒間電源を保持します。まだ死んでいる場合は、以下をお読みください。 [リカバリーガイド](../guides/recovery_ja.html) もう一度試す前に。

## 人々が尋ねる質問

### これにより私の音楽は削除されますか?

はい、内部ストレージは消去されます。通常、microSD カード上のファイルは残りますが、最初に安全な場所にコピーしてください。

### その後 Rockbox に戻ることはできますか?

はい。元のソフトウェアの復元は一方通行ではありません。ご使用のモデルのカスタム ソフトウェア ページから再度インストールできます。

### Type A / Type B の設定は必要ですか?

その選択肢があるのは Y1 だけであり、オリジナル ソフトウェアのみです。他のすべてのモデルは単一のパッケージを使用します。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
