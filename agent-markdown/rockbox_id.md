---
title: "Cara menginstal Rockbox pada Innioasis Y1 atau Y2 - Innioasis Updater"
description: "Instal Rockbox pada Innioasis Y1 atau Y2 dengan Updater: tema, rilis stabil, catatan Type A dan Type B, dan cara memulihkan Perangkat Lunak Asli setelahnya."
language: "id"
source: "https://innioasis.app/rockbox_id.html"
---

# Cara menginstal Rockbox pada Innioasis Y1 atau Y2 - Innioasis Updater

Rockbox referensi

# Mendapatkan Rockbox di Y1 atau Y2 Anda

Rockbox mengubah perangkat lunak pemutar dan membuka antarmuka pemutar musik yang lebih dalam, kontrol pemutaran, pengurutan, dan opsi tema. Penginstalan dipandu, tetapi Y1 dan Y2 merupakan perjalanan yang terpisah.[Rockbox pada Y1](guides/rockbox-y1.html)[Rockbox pada Y2](guides/rockbox-y2.html)[Mengapa Rockbox?](rockbox-benefits_id.html)

## Apa yang diubah oleh instalasi

Rockbox adalah perangkat lunak khusus. Ini tidak menghilangkan kemampuan Anda untuk kembali ke antarmuka stok ketika paket Perangkat Lunak Asli yang cocok tersedia. Ini dapat meningkatkan penelusuran dan penyesuaian musik, tetapi fitur, resolusi, masa pakai baterai, dan kompatibilitas tema bergantung pada versinya.Jangan mencampur model. Pilih Y1 untuk pemain Y1 dan Y2 untuk pemain Y2. Nama rilis yang tampak serupa tidak cukup untuk membuktikan bahwa suatu paket kompatibel.

## Tonton videonya

Video oleh Frawgeeys. Ini menunjukkan rute pembaru Innioasis; gunakan langkah tertulis khusus model di bawah ini untuk Y1 atau Y2 Anda.

Video oleh [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (Spanyol), menampilkan Rockbox pada Y1. Gunakan langkah khusus model di bawah ini untuk pemutar Anda.

## Rute Updater bersama
  - Instal Updater dan jangan sambungkan apa pun sampai diminta.
  - Pilih model yang tercetak pada pemutar di Model perangkat.
  - Pilih Rockbox di Perangkat lunak.
  - Pilih rilis stabil kecuali Anda sengaja menguji versi malam.
  - Klik Pasang / Pulihkan, lalu ikuti perintah mematikan dan koneksi USB.
  - Putuskan sambungan hanya setelah pesan sukses.

## 240p, 360p, dan tema

Koleksi tema Rockbox yang lebih lama dapat dibuat untuk 240p. Y1 build komunitas juga menggunakan label kompatibilitas 360p. Baca catatan rilis dan sumber tema sebelum memilih build. Tema yang dibuat untuk satu resolusi atau rangkaian perangkat lunak mungkin tidak berfungsi pada resolusi lain.[Jelajahi tema komunitas](https://themes.innioasis.app/?lang=id)[Alat tema](https://themes.innioasis.app/?lang=id)

## Kembali ke Perangkat Lunak Asli

Pilih model yang sama lagi, pilih Perangkat lunak asli, pilih rilis stabil, dan gunakan Pasang / Pulihkan. Jika kegagalan terjadi sebelum prompt USB, periksa komputer dan ekstrak file. Jika pemutar terdeteksi tetapi flash gagal, mulailah dengan [pemecahan masalah](troubleshooting_id.html).[Y1 pulihkan](guides/restore-original-y1.html)[Y2 pulihkan](guides/restore-original-y2.html)

## Pertanyaan umumSaya menginstal ulang Rockbox dan tidak memperbaiki apa pun.

Menginstal ulang Rockbox akan menulis build yang sama pada file yang sama, sehingga tidak dapat mengatur ulang hal-hal yang Rockbox simpan di MicroSD. Jika masalahnya adalah pengaturan, tema, daftar putar, atau basis data yang rusak pada kartu, menginstal ulang tidak akan menghapusnya. Reset yang andal adalah menghapus `.rockbox` folder dari MicroSD — Rockbox membuat yang baru pada boot berikutnya.
  - Matikan pemutar sepenuhnya dan keluarkan kartu MicroSD, atau sambungkan pemutar sebagai drive USB.
  - Tampilkan file tersembunyi di komputer Anda sehingga foldernya terlihat. Cara menampilkan file tersembunyiTampilkan dotfiles di komputer AndaWindows: di File Explorer buka Lihat tab dan centang Barang tersembunyi.macOS: di Penemu tekan Cmd+Shift+. untuk mengaktifkan file tersembunyi.Linux · Berkas GNOME: tekan Ctrl+H, atau buka menu dan pilih Tampilkan File Tersembunyi.Linux · KDE Lumba-lumba: tekan Ctrl+H, atau gunakan Lihat → Tampilkan File Tersembunyi.
  - Hapus itu `.rockbox` folder dari root kartu.
  - Masukkan kembali kartu dan mulai pemutar. Rockbox membuat ulang folder dengan default.
  - Terapkan kembali tema dan pengaturan Anda. Jika masalah hanya muncul kembali setelah tema tertentu, maka tema itulah penyebabnya.

Menghapus `.rockbox` tidak menghapus instalan Rockbox dan tidak menyentuh musik Anda — folder tersebut menyimpan pengaturan, tema, dan cache, dan dibuat ulang secara otomatis. Jika Anda ingin menyimpan tema Anda, salin folder tersebut `.rockbox` sebelum menghapusnya, atau ganti nama folder menjadi `.rockbox-old` pertama.Mengapa saya tidak dapat melihat folder .rockbox di MicroSD saya?

Folder yang namanya dimulai dengan titik disembunyikan secara default di sebagian besar komputer. Anda tidak perlu melihatnya untuk menginstal Rockbox — Updater menangani file. Jika Anda sedang memecahkan masalah dan ingin menghapusnya, aktifkan file tersembunyi terlebih dahulu. Cara menampilkan file tersembunyiTampilkan dotfiles di komputer AndaWindows: di File Explorer buka Lihat tab dan centang Barang tersembunyi.macOS: di Penemu tekan Cmd+Shift+. untuk mengaktifkan file tersembunyi.Linux · Berkas GNOME: tekan Ctrl+H, atau buka menu dan pilih Tampilkan File Tersembunyi.Linux · KDE Lumba-lumba: tekan Ctrl+H, atau gunakan Lihat → Tampilkan File Tersembunyi.Apakah menghapus .rockbox akan mengatur ulang tema dan pengaturan saya?

Ya — `.rockbox` menyimpan pengaturan Rockbox, tema, daftar putar, dan basis data cache. Menghapusnya akan mengembalikan Rockbox ke keadaan default yang bersih. Cadangkan seluruh folder (atau ganti namanya menjadi `.rockbox-old`) jika Anda menginginkannya kembali, jalankan pemutar dan Rockbox buat folder baru.

## Panduan Rockbox-Y1 dan Rockbox-Y2 lainnya

Jelajahi panduan langkah demi langkah untuk menginstal, mengunduh, menentukan tema, memulihkan, dan memecahkan masalah Rockbox pada kedua model:[Rockbox-pusat Y1](rockbox-y1/)[Rockbox-pusat Y2](rockbox-y2/)[Rockbox Unduhan ROM](rockbox-rom-download_id.html)[Rockbox untuk Y1](rockbox-for-y1_id.html)[Rockbox untuk Y2](rockbox-for-y2_id.html)[Rockbox-Y1 vs Y2](rockbox-y1-vs-y2.html)[Rockbox-Tema Y1](rockbox-y1-themes.html)[Rockbox-Tema Y2](rockbox-y2-themes.html)

## Apakah referensi ini bermanfaat?

Jawaban Anda membantu menyempurnakan panduan ini.YaBelum[Beri tahu kami bagaimana kami dapat meningkatkannya](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
