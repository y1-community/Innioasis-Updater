---
title: "Windows 10/11 アプリの起動の問題と Smart App Control の回避策 - Innioasis アップデーター"
description: "Windows 10/11 または Smart App Control によってアプリの起動が停止された場合は、こちらの回避策に従ってください。"
language: "ja"
source: "https://innioasis.app/notices/2026-11-07-codesigning_ja.html"
---

# Windows 10/11 アプリの起動の問題と Smart App Control の回避策 - Innioasis アップデーター

2026-10-25 · 2026-12-31 まで · モデル: Y1、Y2

# Windows 10/11 アプリの起動の問題と Smart App Control の回避策

Windows 10/11 または Smart App Control によってアプリの起動が停止された場合は、こちらの回避策に従ってください。

2026-10-25 · 2026-12-31 まで · モデル: Y1、Y2

誤検知レポートは次の目的で Microsoft に提出されました。 `installer.exe` そして `InnioasisUpdater.exe` 対処しましたが、Windows Endpoint Protection または Smart App Control が依然としてコンピューター上のアプリケーションをブロックしている場合は、次の回避策を使用してください。

### 一時的な回避策: スマート アプリ コントロールをオフにする
  - ウィンドウを開く 設定 （プレス `Win + I`).
  - に行く プライバシーとセキュリティ > Windows セキュリティ > アプリとブラウザの制御.
  - 下 スマートアプリコントロール、 クリック スマートアプリコントロールの設定.
  - スマート アプリ コントロールを次のように設定します オフ。これにより、アプリがすぐに開いて実行できるようになります。

Windows または Edge によって Updater CE をダウンロードできない場合は、その他のオプション (…） それから 保つ > もっと見る > とにかく保管してください.

### スマート アプリ コントロールを再度有効にする

コンピューター上で誤検知の定義の更新が完了したら、Windows レジストリを使用して Smart App Control を再度有効にすることができます。
  - プレス Windowsキー+R、 タイプ `regedit`をクリックし、Enter キーを押して、管理者としてレジストリ エディタを開きます。
  - 次の場所に移動します: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` （または `Policies`).
  - 位置を特定する `VerifiedAndReputablePolicyState` 右側のペインで。
  - ダブルクリック `VerifiedAndReputablePolicyState` そして、その値データを次のように変更します。

  - `1` = オン (強制)
  - `2` = 評価モード

  - [OK] をクリックし、レジストリ エディタを閉じて、コンピュータを再起動します。

[Microsoft への installer.exe レポートを参照してください。](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Microsoft への InnioasisUpdater.exe レポートを参照してください。](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[リンクされたページを開く](https://innioasis.app/notices.html)

[← すべてのお知らせ](index_ja.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
