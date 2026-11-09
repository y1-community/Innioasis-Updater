---
title: "Innioasis Updater インストール ガイドを埋め込みます - Innioasis Updater"
description: "応答性の高い iframe 埋め込みとコピー可能なサンプルを備えた Innioasis Updater インストール ガイドを別の Web サイトに追加します。"
language: "ja"
source: "https://innioasis.app/innioasis-integration-snippet_ja.html"
---

# Innioasis Updater インストール ガイドを埋め込みます - Innioasis Updater

# 🚀 Innioasis Updater - 埋め込み可能インストールガイド

これは、あらゆる Web サイトに簡単に統合できる、完全な埋め込み可能なインストール ガイド ウィジェットです。 Windows、macOS、Linux ユーザー向けの包括的なインストール ガイドを開くクールな右下隅のポップアップ CTA が特徴です。

### 🎨 美しいデザイン

ダークモードをサポートするすべてのデバイスで動作する最新の応答性の高いデザイン

### 📱 クロスプラットフォーム

Windows、macOS、Linux 用の完全なインストール ガイド (ステップバイステップの説明付き)

### 🔧 簡単な統合

スニペットをコピーして貼り付けるだけです。依存関係や複雑な設定は必要ありません。

### 💾 スマートストレージ

ユーザーが邪魔を避けるためにバナーを閉じたかどうかを記憶します

## 📋 統合手順

Innioasis Updater インストール ガイドを Web サイトに追加するには、次のコード スニペットをコピーして HTML に貼り付けるだけです。 <!-- Innioasis Updater インストール ガイド ウィジェット --> <script> (function() { // ウィジェットを作成して挿入します const script = document.createElement('script'); script.src = 'https://your-domain.com/innioasis-embed.html'; script.async = true; // 代替: ローカル ファイルからロード // script.src = './innioasis-embed.html'; document.head.appendChild(script); // iframe コンテナを作成します const iframe = document.createElement('iframe'); iframe.src = 'position: 固定; right: 20px;高さ: 200px; z-index: 999999; ポインタイベント: なし; // iframe.onload = 'auto' }; </script> 📋 統合コードをコピー

## 🎯 代替案: 直接埋め込み方法

さらに簡単に統合するには、iframe を使用してウィジェットを直接埋め込むことができます。 <!-- iframe の直接埋め込み --> <iframe src="https://your-domain.com/innioasis-embed.html" width="400" height="200" Frameborder="0" style="position:fixed;bottom:20px;right:20px;z-index:999999;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,0.3);" allowtransparency="true"> </iframe> 📋 Iframe コードをコピー

## 🔧 カスタマイズオプション

次のパラメータを変更することでウィジェットをカスタマイズできます。 // CTA バナーをカスタマイズします window.InnioasisUpdater = { // バナー テキストを変更します ctaTitle: "🚀 Get Innioasis Updater", ctaDescription: "お使いのプラットフォーム用のデスクトップ アプリをダウンロードします", ctaButtonText: "Get Started", // 位置を変更します: "bottom-right"、// または "bottom-left"、"top-right"、"top-left" // 自動表示遅延 (ミリ秒単位) showDelay: 3000, // 3 秒後に表示 // カスタム スタイル CustomCSS: ` .cta-banner { background: Linear-gradient(135deg, #your-color1, #your-color2); } ` }; 

## 📱 デモ

ウィジェットの動作を確認するには、下のボタンをクリックしてください。🎯 デモウィジェットを表示

## 📚 含まれる機能
  - スマート CTA バナー: スムーズなアニメーションで右下隅に表示されます
  - プラットフォームの検出: ユーザーのオペレーティング システムを自動的に検出します
  - ステップバイステップのガイド: Windows、macOS、Linux の完全なインストール手順
  - 進捗状況の追跡: 複数ステップのインストールのための視覚的な進行状況バー
  - ダウンロード統合: 必要なすべてのファイルの直接ダウンロード リンク
  - レスポンシブデザイン: デスクトップ、タブレット、モバイルで完璧に動作します
  - ダークモードのサポート: ユーザーのシステム設定に自動的に適応します
  - ユーザー設定: ユーザーがバナーを閉じたかどうかを記憶します
  - アクセシビリティ: キーボードナビゲーションとスクリーンリーダーフレンドリー

## 🌐 ホスティング要件

Web サイトでこのウィジェットを使用するには、次のことを行う必要があります。
  - アップロードする `innioasis-embed.html` Web サーバーにファイルを保存する
  - サーバーを指すように統合スニペット内の URL を更新します。
  - サーバーが HTTPS をサポートしていることを確認します (最新のブラウザに必要)
  - Web サイト上のウィジェットをテストして、正しく動作することを確認します。

## 🆘 サポート

このウィジェットの統合についてサポートが必要な場合、または質問がある場合は、次のことを行ってください。
  - ブラウザのコンソールでエラー メッセージがないか確認してください
  - すべてのファイルがサーバーに適切にアップロードされていることを確認してください
  - 統合コード内の URL が正しいことを確認します。
  - さまざまなブラウザとデバイスでテストする

 Innioasis チームによる ❤️ で作成されました

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
