---
title: "MTKClient &amp; 低レベルリカバリガイド - Innioasis &amp; Timmkoo - Innioasis ファームウェアのダウンロード"
description: "MTKClient と SP Flash Tool を使用する Innioasis と Timmkoo プレーヤーの低レベルの MediaTek リカバリ、ブートローダーのブリック解除命令、およびドライバー診断。"
language: "ja"
source: "https://innioasis.app/mtkclient_ja.html"
---

# MTKClient &amp; 低レベルリカバリガイド - Innioasis &amp; Timmkoo - Innioasis ファームウェアのダウンロード

高度な診断 · MediaTek

# MTKClient & アンブリック診断

MTKClient は、Innioasis Updater CE によって使用される基礎となるオープンソース MediaTek フラッシュ エンジンです。プレーヤーが応答しなくなったり、標準のフラッシュに失敗したりした場合は、これらの回復診断を使用してください。[一般的なトラブルシューティング](troubleshooting_ja.html)[ドライバーセットアップに関する注意事項](drivers_ja.html)

Innioasis Updater から始める

## 低レベルのルートの前にガイド付きルートを試してください

アップデーターはこれを 1 パスで実行します。ソフトウェアを選択し、画面上の手順に従ってください。これで完了です。また、修正または新しいリリースがいつリリースされるかについても通知されます。

## BootROM (BROM) モードについて

電源が完全にオフになると、MediaTek MT6572 / MT6580 プロセッサは、プライマリ ブートローダーをロードする前に、USB バスでハンドシェイク パケットをリッスンします。フラッシュの破損が発生した場合、BROM モードでは完全なリカバリの再書き込みが可能です。

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
