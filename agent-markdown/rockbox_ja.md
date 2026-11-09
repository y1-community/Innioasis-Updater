---
title: "Innioasis Y1 または Y2 - Innioasis Updater に Rockbox をインストールする方法"
description: "アップデーターを使用して Innioasis Y1 または Y2 に Rockbox をインストールします: テーマ、安定版リリース、Type A および Type B のメモ、および後で元のソフトウェアを復元する方法。"
language: "ja"
source: "https://innioasis.app/rockbox_ja.html"
---

# Innioasis Y1 または Y2 - Innioasis Updater に Rockbox をインストールする方法

Rockbox 参照

# Y1 または Y2 で Rockbox を取得しています

Rockbox はプレーヤー ソフトウェアを変更し、より深い音楽プレーヤー インターフェイス、再生コントロール、並べ替え、およびテーマのオプションを開きます。インストールはガイドに従って行われますが、Y1 と Y2 は別の手順になります。[Y1 の Rockbox](guides/rockbox-y1.html)[Y2 の Rockbox](guides/rockbox-y2.html)[なぜRockbox?](rockbox-benefits_ja.html)

## インストールによって何が変わるのか

Rockbox はカスタム ソフトウェアです。対応するオリジナル ソフトウェア パッケージが利用可能な場合、ストック インターフェイスに戻る機能が失われるわけではありません。音楽のブラウジングとカスタマイズを改善できますが、機能、解像度、バッテリー寿命、テーマの互換性はビルドによって異なります。モデルを混合しないでください。 Y1 プレーヤーの場合は Y1、Y2 プレーヤーの場合は Y2 を選択します。リリース名が似ているだけでは、パッケージに互換性があるという十分な証拠にはなりません。

## ビデオを見る

Frawgeeys によるビデオ。 Innioasis Updater ルートが表示されます。 Y1 または Y2 については、以下に記載されているモデル固有の手順を使用してください。

ビデオ: [クリスティアンプラザ](https://www.youtube.com/@CristianPlaza) (スペイン語)、Y1 に Rockbox を表示します。お使いのプレーヤーについては、以下のモデル固有の手順を使用してください。

## 共有アップデータ ルート
  - Updater をインストールし、要求されるまで何も接続しません。
  - プレーヤーに印刷されているモデルを選択してください デバイスモデル.
  - 選択してください Rockbox で ソフトウェア.
  - 意図的に夜間ビルドをテストする場合を除き、安定したリリースを選択してください。
  - クリック インストール / 復元をクリックし、電源をオフにして USB 接続を求めるプロンプトに従います。
  - 成功メッセージが表示された後でのみ切断してください。

## 240p、360p、およびテーマ

古い Rockbox テーマ コレクションは 240p で作成できます。 Y1 コミュニティ ビルドでも 360p 互換性ラベルが使用されます。ビルドを選択する前に、リリース ノートとテーマ ソースをお読みください。ある解像度またはソフトウェア ファミリ用に作成されたテーマは、別の解像度またはソフトウェア ファミリでは動作しない場合があります。[コミュニティのテーマを参照する](https://themes.innioasis.app/?lang=ja)[テーマツール](https://themes.innioasis.app/?lang=ja)

## 元のソフトウェアに戻す

同じモデルを再度選択し、 純正ソフトウェア、安定したリリースを選択し、使用します インストール / 復元。 USB プロンプトが表示される前にエラーが発生した場合は、コンピュータと抽出されたファイルを確認してください。プレーヤーは検出されたがフラッシュに失敗した場合は、次のことから始めてください。 [トラブルシューティング](troubleshooting_ja.html).[Y1 復元](guides/restore-original-y1.html)[Y2 復元](guides/restore-original-y2.html)

## よくある質問Rockbox を再インストールしましたが、何も修正されませんでした。

Rockbox を再インストールすると、同じビルドが同じファイルに書き込まれるため、Rockbox が MicroSD に保持しているものをリセットできません。問題が、カード上に存在する壊れた設定、テーマ、プレイリスト、またはデータベースである場合、再インストールしても問題は解決されません。確実なリセットとは、 `.rockbox` MicroSD — Rockbox のフォルダーは、次回の起動時に新しいフォルダーを構築します。
  - プレーヤーの電源を完全にオフにして MicroSD カードを取り外すか、プレーヤーを USB ドライブとして接続します。
  - コンピュータ上の隠しファイルを表示して、フォルダが見えるようにします。 隠しファイルを表示する方法コンピュータ上のドットファイルを表示するWindows: ファイルエクスプローラーで開きます ビュー タブとチェックマーク 隠しアイテム.macOS: ファインダープレスで Cmd+Shift+. 隠しファイルを切り替えます。Linux · GNOME ファイル: 押す Ctrl+H、またはメニューを開いて選択します 隠しファイルを表示.Linux · KDE ドルフィン: 押す Ctrl+H、または使用します 「表示」→「隠しファイルを表示」.
  - を削除します `.rockbox` カードルートからのフォルダー。
  - カードを再度挿入し、プレーヤーを起動します。 Rockbox はデフォルトでフォルダーを再作成します。
  - テーマと設定を再適用します。特定のテーマの後でのみ問題が再発する場合は、そのテーマが原因です。

削除中 `.rockbox` Rockbox はアンインストールされず、音楽にも影響しません。フォルダーには設定、テーマ、キャッシュが保持され、自動的に再構築されます。テーマを保持したい場合は、フォルダーをコピーしてください。 `.rockbox` 削除する前に、またはフォルダーの名前を `.rockbox-old` まず。MicroSD に .rockbox フォルダーが表示されないのはなぜですか?

名前がドットで始まるフォルダーは、ほとんどのコンピューターではデフォルトで非表示になります。 Rockbox をインストールするためにこれを参照する必要はありません — アップデーターがファイルを処理します。トラブルシューティング中にそれを削除したい場合は、最初に隠しファイルを有効にしてください。 隠しファイルを表示する方法コンピュータ上のドットファイルを表示するWindows: ファイルエクスプローラーで開きます ビュー タブとチェックマーク 隠しアイテム.macOS: ファインダープレスで Cmd+Shift+. 隠しファイルを切り替えます。Linux · GNOME ファイル: 押す Ctrl+H、またはメニューを開いて選択します 隠しファイルを表示.Linux · KDE ドルフィン: 押す Ctrl+H、または使用します 「表示」→「隠しファイルを表示」..rockbox を削除するとテーマと設定がリセットされますか?

はい - `.rockbox` Rockbox の設定、テーマ、プレイリスト、キャッシュされたデータベースを保持します。これを削除すると、Rockbox はクリーンなデフォルト状態に戻ります。フォルダー全体をバックアップします (またはフォルダーの名前を次のように変更します) `.rockbox-old`) いずれかを戻したい場合は、プレーヤーを起動すると、Rockbox によって新しいフォルダーが作成されます。

## その他の Rockbox-Y1 および Rockbox-Y2 ガイド

両方のモデルで Rockbox のインストール、ダウンロード、テーマ設定、復元、トラブルシューティングを行うためのステップバイステップのガイドをご覧ください。[Rockbox-Y1 ハブ](rockbox-y1/)[Rockbox-Y2 ハブ](rockbox-y2/)[Rockbox ROMのダウンロード](rockbox-rom-download_ja.html)[Y1 の Rockbox](rockbox-for-y1_ja.html)[Y2 の Rockbox](rockbox-for-y2_ja.html)[Rockbox-Y1 対 Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 テーマ](rockbox-y1-themes.html)[Rockbox-Y2 テーマ](rockbox-y2-themes.html)

## この参考資料は役に立ちましたか?

あなたの回答はこのガイドの改善に役立ちます。はいまだ[改善方法を教えてください](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
