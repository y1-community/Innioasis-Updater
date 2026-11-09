---
title: "クリーン インストールで Innioasis Updater および Y1 ヘルパーを修正 - Innioasis Updater"
description: "Innioasis Updater と Y1 ヘルパーの段階的なクリーン インストール: 残ったファイルを削除し、再インストールして、ファームウェアのフラッシュに戻ります。"
language: "ja"
source: "https://innioasis.app/Troubleshooting/clean_install_ja.html"
---

# クリーン インストールで Innioasis Updater および Y1 ヘルパーを修正 - Innioasis Updater

## クリーン インストールが必要であることを確認する

次のいずれかの症状が発生した場合は、手動で再インストールすることをお勧めします。
  - アップデーターの起動に数分かかるか、アップデートの確認中に停止します。
  - 新しいリリースが存在する場合でも、アップデートは受信されなくなります。
  - デバイスのファームウェアのアップデートが利用可能であっても、ダウンロードまたは適用に失敗します。
  - 複数のリリースをスキップし、長い間アップデーターを使用していませんでした。

## Windows: クリーン再インストールを実行する

Windows 10 または Windows 11 (64 ビット) でアップデータを更新するには、公式 Windows インストーラーを使用します。これにより、古いビルドが完全に置き換えられ、自己更新チャネルが復元されます。

インストーラーを実行する前に、 設定 › アプリ › インストールされているアプリ (または遺産 プログラムの追加と削除 パネル))、Innioasis Updater の既存のコピーをアンインストールします。クリーンを開始すると、ファイルの競合が防止されます。[ Windows 用クリーン インストーラーをダウンロード ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)ステップ1

### 最新のインストーラーをダウンロードする

インストーラーをダウンロード フォルダーに保存します。現在実行中の場合は Innioasis Updater を閉じます。ステップ2

### 既存のインストールを削除する

開く 設定 › アプリ › インストールされているアプリ (または遺産 コントロール パネル › プログラムの追加と削除) し、Innioasis Updater をアンインストールして、再インストールが白紙の状態から開始されるようにします。ステップ3

### インストールして再起動する

ダウンロードしたインストーラーを実行します。Windows は許可を求めるプロンプトを表示します。セットアップが完了したら、Innioasis Updater を起動します。これで、1.8.2.8 が自動的に検出され、アップデートが再度取得されるはずです。

 これにより、起動の遅さも修正され、アップデーターが開発者から直接ファームウェア リリースを取得できるようになります。 

## macOS: DMG インストーラーを使用して更新する

macOS インストーラーは古いファイルを削除し、1.8.2.8 をインストールします。[ Innioasis Updater DMG をダウンロード ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - ダウンロードした DMG を開き、Finder ウィンドウを展開して、 再インストール オプション。
  - 再インストール コマンドを実行して、アップデーターの既存のコピーを更新します。これにより、新機能をブロックする可能性のある古いヘルパー ファイルが削除されます。
  - アプリケーションからInnioasis Updaterを再度起動します。バージョン情報パネルリストのバージョンを確認する 1.8.2.8.
 再インストール後に「Innioasis Updater を開けません」と表示される場合は、次の手順に進みます。 システム設定 › プライバシーとセキュリティ そして選択してください とにかく開く アプリを承認します。 

## 1.8.2.8 にアップデートした後

最新バージョンを使用すると、以下の機能にアクセスできるようになります。これらは現在のビルドでのみ利用可能です。
  - ワンクリックでインストール オリジナルのファームウェア、コミュニティ リリース、および開発者のリリースから直接ダウンロードされた Rockbox ビルドの場合。
  - ガイド付きの手順を明確にする これにより、プレーヤーを接続するタイミングと、プラグを抜いても安全なタイミングがわかります。
  - 両方のプラットフォームで全体的な安定性が向上し、起動時間が大幅に短縮されました。

 バージョンを確認するためにサポートが必要ですか? Innioasis Updater を開き、選択します ヘルプ › 概要、ビルドが表示されることを確認します 1.8.2.8. 

## まだサポートが必要ですか?

クリーン インストールが失敗した場合は、エラー メッセージをキャプチャし、Innioasis コミュニティ サポート チャネルに連絡してください。 OS のバージョン、アップデーターのビルド (利用可能な場合)、およびすでに試した手順を含めてください。

インストールを最新の状態に保つことで、展開時に常に最新のファームウェア パッケージとツールを受け取ることができます。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
