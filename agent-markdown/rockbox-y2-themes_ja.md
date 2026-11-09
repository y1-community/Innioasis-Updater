---
title: "Rockbox-Y2 テーマ: Y2 でのテーマのインストールとリセット"
description: "Innioasis Y2 に Rockbox-Y2 テーマをインストール、管理、リセットする方法: テーマが .rockbox フォルダーに存在する場所と、ビルドの互換性を確認する方法。"
language: "ja"
source: "https://innioasis.app/rockbox-y2-themes_ja.html"
---

# Rockbox-Y2 テーマ: Y2 でのテーマのインストールとリセット

[← Rockbox-Y2 ハブ](rockbox-y2/)

Rockbox-Y2 · テーマ

# Rockbox-Y2 テーマ

Rockbox-Y2 にテーマをインストールする方法、インストールされているビルドとテーマの互換性を確認する方法、およびテーマが正しく表示されない場合にテーマをリセットする方法。[Rockbox-Y2 リリースノート](release-notes/rockbox-y2/index.html)[コミュニティのテーマを参照する](https://themes.innioasis.app/)[Rockbox-Y2 をインストールします](rockbox-y2/install.html)

## ビルドのテーマの互換性を確認する

Rockbox-Y2 は Y1 ポートとは別に開発されているため、テーマの互換性はインストールされている Y2 ビルド バージョンに従います。チェックしてください [Rockbox-Y2 リリースノート](release-notes/rockbox-y2/index.html) テーマ パックをインストールする前に、お使いのバージョンを確認してください。

見る [Rockbox-Y1 対 Rockbox-Y2](rockbox-y1-vs-y2_ja.html) 2 つのポートの完全な比較については、こちらをご覧ください。

## Y2 にテーマをインストールする方法

テーマは MicroSD カードの隠しファイルに保存されます。 `.rockbox` フォルダ。
  - Rockbox-Y2 を少なくとも 1 回開始して、 `.rockbox` MicroSD カードのフォルダーに移動します。
  - テーマ ファイルを抽出またはコピーします。 `.rockbox/` （それで `themes`, `wps`, `fonts`、そして `backdrops` にマージする `.rockbox/`).
  - プレーヤーで、開きます 設定 → テーマ設定 → テーマファイルの参照 テーマを選択します。

コンピュータ上の隠しフォルダを表示するには: を押します。 Cmd+Shift+. macOS では有効にします 表示 → 隠しアイテム Windows の場合、または を押します Ctrl+H Linux 上で。

## 壊れたテーマをリセットする方法

テーマのせいで画面が読みにくくなっている場合は、テーマの名前を変更するか削除してください。 `.rockbox` MicroSD カードのフォルダーを選択し、プレーヤーを再起動します。 Rockbox-Y2 は新しいものを作成します `.rockbox` 音楽をそのまま維持しながら、デフォルトのテーマでフォルダーを作成します。[.rockbox フォルダー](rockbox-y2/sd-card.html)[Rockbox-Y2 を更新しています](rockbox-y2/update.html)[Rockbox-Y2 ビルドノート](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
