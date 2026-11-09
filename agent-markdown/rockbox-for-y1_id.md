---
title: "Rockbox untuk Y1 (Rockbox-Y1): ikhtisar, panduan pembuatan dan pemasangan"
description: "Rockbox untuk Y1, Rockbox-Y1 dan rockbox-y1 semuanya mengacu pada firmware komunitas Rockbox untuk Innioasis Y1. Pelajari apa yang ditambahkannya, build mana yang harus dipilih, dan cara menginstalnya dengan Innioasis Updater CE."
language: "id"
source: "https://innioasis.app/rockbox-for-y1_id.html"
---

# Rockbox untuk Y1 (Rockbox-Y1): ikhtisar, panduan pembuatan dan pemasangan

[← Unduhan Firmware](firmware_id.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox untuk Y1 (Rockbox-Y1)

“Rockbox”, “Rockbox-Y1”, dan “Rockbox untuk Y1” semuanya mengacu pada firmware komunitas Rockbox yang sama untuk Innioasis Y1. Inilah yang ditambahkan ke pemutar Anda, build mana yang harus dipilih, dan cara menginstalnya dengan Innioasis Updater CE.[Pasang Rockbox-Y1](rockbox-y1/install.html)[Unduh ROM](rockbox-y1/download.html)[Tutorial tertulis](guides/rockbox-y1.html)[Rockbox-pusat Y1](rockbox-y1/)

## Satu firmware, beberapa nama

Di Innioasis Updater CE, firmware ini muncul sebagai Rockbox saat Anda memilih model perangkat Y1. Panduan, video, dan catatan rilis juga menyebutnya Rockbox-Y1 atau Rockbox untuk Y1 jadi jelas bahwa build tersebut untuk Y1 dan bukan Y2.

Selalu periksa model yang tercetak pada pemutar Anda sebelum menginstal: paket firmware Y1 dan Y2 tidak dapat dipertukarkan.

## Apa yang Rockbox-Y1 tambahkan ke Y1 Anda

Rockbox-Y1 adalah port komunitas dari firmware pemutar musik sumber terbuka Rockbox untuk Innioasis Y1:
  - Perpustakaan musik berbasis tag — telusuri menurut artis, album, genre, dan tahun menggunakan tag audio, atau jelajahi folder secara langsung.
  - Pemutaran audio tingkat lanjut — pemutaran tanpa celah, crossfade, ReplayGain, dan equalizer penuh.
  - Tema khusus — pilih dari ratusan tema komunitas 240p dan 360p, termasuk tata letak bergaya iPod klasik.
  - Radio FM — dukungan radio FM bawaan.
  - Ekstra opsional — pengunduhan podcast melalui Wi-Fi dan Last.fm / ListenBrainz / Maloja melakukan scrobbling pada build yang didukung.
  - Boot ganda — beralih kembali ke Perangkat Lunak Asli pabrik tanpa melakukan flashing pada build yang didukung.

## Versi Y1 mana yang harus saya pilih?
  - 240p vs.360p — Versi 240p berfungsi dengan tema klasik 320×240 Rockbox; Versi 360p menggunakan tema 480×360 Y1 yang lebih tajam. Cocokkan resolusi build dengan tema yang ingin Anda gunakan ([Panduan 240p vs. 360p](rockbox-y1/resolution.html)).
  - Type A vs.Type B — Type A ditujukan untuk pemutar Y1 yang dikirimkan dengan perangkat lunak pabrik 2.0.0 atau lebih baru; Type B adalah untuk unit Y1 sebelumnya. Pilih Type A kecuali Anda tahu Y1 Anda adalah Type B.
  - Stabil vs. Malam hari — Pilih build stabil untuk mendengarkan sehari-hari, atau build malam untuk menguji perubahan terbaru.

## Unduhan langsung dari komunitas pengembang

Innioasis Updater CE selalu mengunduh paket firmware langsung dari komunitas pengembang firmware ([rockbox-y1/rockbox](firmware_id.html?model=Y1&software=rockbox-y1)), dan pengembangnya sendiri bertanggung jawab penuh untuk mencantumkan rilis perangkat lunak mereka di Updater CE.

Anda dapat membiarkan Updater CE mengunduh dan menginstal firmware secara otomatis, atau mengunduh paket ROM dari kami [Rockbox-Y1 halaman unduhan](rockbox-y1/download.html) dan [Rockbox ROM halaman unduh](rockbox-rom-download_id.html).[Rockbox-Y1 unduhan](rockbox-y1/download.html)[Instal dari ZIP lokal](rockbox-y1/portable-zip.html)

## Cara menginstal Rockbox-Y1
  - Buka Innioasis Updater CE dan atur Model perangkat untuk Y1.
  - Pilih Rockbox di Perangkat lunak.
  - Pilih rilis stabil (atau aktifkan nightly build untuk menguji pratinjau).
  - Klik Pasang / Pulihkan jadi Updater CE mengunduh paket langsung dari pengembangnya.
  - Matikan Y1 sepenuhnya dan sambungkan dengan kabel data USB saat Updater CE meminta Anda.
  - Tunggu pesan penyelesaian, lalu putuskan sambungan dan hidupkan pemutar Anda.

Untuk tangkapan layar dan kiat pengaturan mendetail, baca [tutorial lengkap Rockbox-Y1](guides/rockbox-y1.html).

## Memulihkan perangkat lunak Y1 asli

Anda dapat kembali ke perangkat lunak pabrik kapan saja: pilih Y1 dan Perangkat lunak asli di Updater CE, pilih rilis stabil, dan klik Pasang / Pulihkan. Musik Anda di kartu MicroSD dipertahankan. Lihat [panduan pemulihan](rockbox-y1/restore-stock.html) dan [Y1 Halaman Perangkat Lunak Asli](original-software-y1_id.html).

## Pertanyaan yang sering diajukanApakah Rockbox untuk Y1 sama dengan Rockbox-Y1?

Ya. Rockbox, Rockbox-Y1, Rockbox untuk Y1, dan `rockbox-y1` semuanya mengacu pada port komunitas Rockbox yang sama untuk Innioasis Y1.Dari mana Updater CE mengunduh Rockbox-Y1?

Updater CE selalu mengunduh paket firmware langsung dari rilis milik pengembang firmware komunitas (`rockbox-y1/rockbox`). Pengembang sepenuhnya bertanggung jawab untuk mencantumkan rilis perangkat lunak mereka di Updater CE.Bisakah saya menginstal Rockbox-Y1 pada Y2?

Tidak. Y2 memiliki versi firmware tersendiri. Gunakan [Rockbox untuk Y2](rockbox-for-y2_id.html) sebagai gantinya.Apakah menginstal Rockbox-Y1 akan menghapus musik saya?

Tidak. Musik disimpan pada kartu MicroSD dan tidak terpengaruh saat mem-flash firmware internal pemutar.

## Panduan terkait

### [Rockbox-pusat Y1](rockbox-y1/)

Semua panduan Y1: instalasi, pengunduhan, tema, pemulihan, boot ganda, dan pemecahan masalah.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Perbedaan build Y1 dan Y2 Rockbox.

### [Rockbox-Tema Y1](rockbox-y1-themes.html)

Cara mentransfer tema 240p dan 360p dengan Updater CE.

### [Rockbox ikhtisar](rockbox_id.html)

Pengenalan Rockbox pada pemain Innioasis Y1 dan Y2.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
