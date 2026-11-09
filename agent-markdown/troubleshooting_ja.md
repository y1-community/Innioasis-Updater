---
title: "Innioasis Updater トラブルシューティング | Innioasis と Timmkoo のインストールの問題 - Innioasis Updater"
description: "Innioasis または Timmkoo プレーヤーの Innioasis Updater インストールを修正しました。モデル、ケーブル、ドライバー、電源オフのタイミング、インストールが停止した場所を確認し、再度点滅させます。"
language: "ja"
source: "https://innioasis.app/troubleshooting_ja.html"
---

# Innioasis Updater トラブルシューティング | Innioasis と Timmkoo のインストールの問題 - Innioasis Updater

トラブルシューティング

# インストールが停止したポイントを見つけます。

どこで止まったの？それは何を修正すべきかを示します。[通常のガイドに戻ります](guide_ja.html)[ファームウェアをチェックする](firmware_ja.html)

## USB プロンプトが表示される前に停止しました

これはケーブルの問題ではなく、コンピュータの問題です。モデルを確認してください。ファイルを再度解凍します。それから試してみてください インストール / 復元。リリース リストが空の場合は、 [ファームウェアディレクトリ](firmware_ja.html).

## プレーヤーに接続できません
  - 正しい Y1 または Y2 の電源を完全にオフにします。
  - ケーブルを取り外し、他のフラッシュまたは Android ツールを閉じて、インストールを再度開始します。
  - アップデーターが準備ができたと通知した場合にのみ接続してください。
  - 可能であればハブではなく、短い USB データ ケーブルをコンピュータに直接使用してください。
  - Windows では、MediaTek ドライバーを再インストールして再起動します。 Linux では、USB/serial 権限を確認してください。
アップデータ接続プロンプトライブ アップデーター プロンプトは、現在のモデルとプラットフォームに対して権限を持ちます。

## プレーヤーは検出されましたが、フラッシュは失敗しました

ここで止​​まって。別のモデルを試さないでください。他のツールを閉じ、正しい Y1 または Y2 を選択したことを確認し、プレーヤーが起動しない場合は、一致するオリジナル ソフトウェアを使用してください。 [SP Flash Tool](sp-flash-tool_ja.html) および MTKClient は必要に応じて含まれており、ファイルは [ファームウェアページ](firmware_ja.html).

## Windowsドライバーのメモ

一部の Windows インストールでは、コア分離により MediaTek ドライバーがブロックされます。メモリの整合性を変更する前に現在の Windows セキュリティ ガイダンスに従ってください。システムで許可されている場合は、変更が完了したらオンに戻してください。[ドライバーガイドを開く](drivers_ja.html)[クリーンインストールガイド](Troubleshooting/clean_install.html)

## ホイールが機能しない、またはプレーヤーが起動しない

入力障害と電源障害には、フラッシュの障害とは異なる手順が必要です。これらのガイドでは、一般的な Y1 および Y2 のケースについて説明します。[Y1 スクロールホイール](guides/y1-scroll-wheel-not-working.html)[Y2 スクロールホイール](guides/y2-scroll-wheel-not-working.html)[Y1がオンになりません](guides/y1-wont-turn-on.html)[Y2がオンになりません](guides/y2-wont-turn-on.html)[リカバリガイド](guides/recovery.html)

## まだ行き詰まっていますか?

サポートを求める場合は、モデル、オペレーティング システム、正確なアップデーター メッセージ、プレーヤーが検出されたかどうか、選択したパッケージ/プロジェクトを含めてください。プライベート トークンや無関係なシステム ファイルを投稿しないでください。[助けを求めてください](https://discord.gg/zHrT2zrcek)[サポートメンテナンス](support_devs_ja.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
