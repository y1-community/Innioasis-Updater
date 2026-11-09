---
title: "SP Flash Tool untuk Innioasis &amp; Timmkoo Pemain"
description: "Temukan SP Flash Tool yang dibundel dengan Innioasis Updater di Windows dan Linux, ekstrak rom.zip atau rom_y2.zip, dan flash Innioasis Y1 atau Y2 dengan file pencar yang cocok."
language: "id"
source: "https://innioasis.app/sp-flash-tool_id.html"
---

# SP Flash Tool untuk Innioasis &amp; Timmkoo Pemain

Berkedip manual

# Alat Flash untuk Pemain Innioasis dan Timmkoo

SP Flash Tool masuk ke dalam Innioasis Pembaruan aktif [Windows](drivers_id.html#windows) dan [Linux](drivers_id.html#linux). Anda sudah memilikinya. Panduan ini menunjukkan cara aman untuk menggunakannya pada Innioasis Y1 atau Y2, dan rute Updater untuk pemain Timmkoo.[Kembali ke panduan Pembaruan](guide_id.html)[Unduhan Firmware](firmware_id.html)[Pemecahan masalah](troubleshooting_id.html)

Mulailah dengan Innioasis Updater

## Updater melakukan seluruh pekerjaan dalam satu kali jalan

Updater melakukan sebagian besar instalasi dalam sekali jalan. Pilih perangkat lunak, ikuti langkah-langkahnya, dan selesai. Ini juga memberi tahu Anda kapan perbaikan atau rilis baru tersedia. SP Flash Tool ada di dalam Toolkit Updater untuk kasus yang jarang terjadi, Updater tidak dapat menyelesaikannya. Langkah-langkah di bawah ini merupakan pengecualian.

## Untuk apa alat ini

Updater mem-flash pemutar untuk Anda. SP Flash Tool adalah mesin yang sama, tanpa rel pengaman. Gunakan saat Updater tidak dapat dijalankan, saat pemutar tidak dapat terhubung, atau saat Anda mengetahui cara mengatasi file pencar.Coba Pembaruan terlebih dahulu. Untuk sebagian besar instalasi dan sebagian besar pemulihan, panduan ini dipandu [Rute pembaruan](guide_id.html) adalah pilihan yang lebih aman. Gunakan SP Flash Tool bila Anda tahu mengapa Anda memerlukannya, dan siapkan baterai yang terisi daya serta kabel data USB.

## Alat flash untuk pemain Innioasis

Innioasis Updater adalah alat flash untuk pemain Innioasis. Ini menginstal perangkat lunak resmi, memperbarui dan memulihkan paket melalui alur yang sesuai model, dan menyimpan musik dan pengaturan Anda.

### Innioasis Y1 alat flash

Pilih rilis Y1 di Updater, lalu sambungkan pemutar yang dimatikan saat aplikasi memintanya. Paket Y1 yang sama berfungsi dengan SP Flash Tool ketika Anda memerlukan rute manual.

### Innioasis Y2 alat flash

Pilih rilis yang terdaftar untuk Y2. Paket Y2 tidak dapat dipertukarkan dengan paket Y1, jadi periksa modelnya sebelum Anda memulai.

## Alat flash untuk pemain Timmkoo

Pemain Timmkoo menggunakan alur pemasangan Updater yang sama. Bunyinya paket ZIP dan RAR Timmkoo secara langsung, jadi Anda tidak memerlukan alat flash atau file pencar terpisah.

### Timmkoo Q5 alat flash

Pilih model Q5 di Updater, pilih paket Timmkoo, lalu jalankan Install / Restore dan sambungkan pemutar saat diminta.

### Timmkoo Q3 dan Q3E alat flash

Entri Q3 mencakup Q3 dan Q3E. Updater mengambil file yang cocok dari paket yang diterbitkan proyek.

### Timmkoo A5 alat flash

Pilih model A5 sebelum memilih paket, lalu ikuti perintah instalasi yang sama.

## Dimana Updater meletakkannya

SP Flash Tool dikirimkan bersama folder instalasi Updater, bukan sebagai unduhan terpisah. Buka dari sana saat Anda membutuhkannya.

### Windows

Buka folder instalasi Updater dan jalankan `flash_tool.exe`. Foldernya biasanya ada di bawah `%LOCALAPPDATA%\Innioasis Updater`. Folder Toolkit dengan pintasan SP Flash Tool disertakan pada beberapa pengaturan.

### Linux

Jalankan paketnya `flash_tool` biner di dalam folder aplikasi Updater di x86 / x86_64. Penginstal proyek menyiapkan izin USB dengan aturan udev, sehingga pemutar akan muncul saat terhubung.

### macOS

SP Flash Tool tidak dipaketkan di macOS. Updater menggunakan rute MTKClient di sana. Gunakan [instalasi terpandu](guide_id.html) di Mac dan simpan SP Flash Tool untuk mesin Windows atau Linux.

Alat ini dikirimkan bersama agen pengunduhan MediaTek dan konfigurasi khusus model, sehingga Anda tidak perlu mengumpulkan DA atau menyebarkan file dari tempat lain.

## Siapkan firmwarenya
  - Ambil rilis yang Anda inginkan [Unduhan Firmware](firmware_id.html). Pilih `rom.zip` untuk Y1 atau `rom_y2.zip` untuk Y2.
  - Ekstrak ZIP ke dalam foldernya sendiri. Windows dapat menggunakan Ekstrak Semua. Di Linux, gunakan pengelola arsip Anda atau `unzip` di sebuah terminal.
  - Periksa apakah file pencar ada di folder yang diekstraksi. Biasanya diberi nama `MT6572_Android_scatter.txt` untuk paket Y1 dan `MT6582_Android_scatter_def.txt` untuk paket Y2, meskipun rilis mungkin menamainya dengan nama proyeknya.
Pisahkan modelnya. Pencar Y1 mendeskripsikan perangkat MT6572 dan pencar Y2 mendeskripsikan perangkat MT6582. Melakukan flashing dengan yang salah adalah penyebab pemain menjadi brick. Jika sebaran di dalam ZIP tidak cocok dengan model Anda, hentikan dan gunakan paket yang terdaftar untuk model Anda.

## Muat pencar dan flash
  - Buka SP Flash Tool dari folder instalasi Updater.
  - Di tab Unduh, klik Pilih di samping File Pemuatan Sebar dan pilih file pencar dari folder yang diekstraksi. Daftar partisi akan terisi.
  - Biarkan mode lampu kilat menyala Unduh Saja kecuali Anda sengaja melakukan pemulihan penuh, yang diperlukan Peningkatan Firmware.
  - Klik Unduh. Alat tersebut akan menunggu pemain.
  - Matikan player sepenuhnya, lalu sambungkan kabel data USB. Letakkan pemutar dan jangan gerakkan.
  - Tunggu tanda centang hijau. Baru kemudian lepaskan kabel dan nyalakan pemutar.

Pertahankan aturan kabel dan pengaturan waktu USB yang sama seperti rute yang dipandu: kabel data, tanpa hub, dan sambungkan hanya jika alat sudah siap.

## Jika tidak berkedip
  - Periksa apakah pencar dan ZIP cocok dengan model yang tercetak pada pemutar.
  - Konfirmasikan bahwa pemutar telah dimatikan sepenuhnya sebelum menghubungkan.
  - Di Windows, konfirmasikan driver MediaTek yang diinstal dengan pengaturan Updater; di Linux, konfirmasikan aturan udev dari penginstal proyek.
  - Sambungkan kembali kabel hanya ketika alat sudah menunggu. Perlombaan port membutuhkan pencabutan penuh dan segar Unduh klik.

Untuk apa pun selain itu, buka [pemecahan masalah](troubleshooting_id.html). Dan ingat: Updater masih merupakan rute normal, dan [Y1](guides/restore-original-y1.html) dan [Y2](guides/restore-original-y2.html) panduan pemulihan menggunakannya juga.

## Apakah ini berguna?

Jawaban Anda membantu menyempurnakan panduan ini.Ya, menurut saya itu bergunaBelum[Beri tahu kami bagaimana kami dapat meningkatkannya](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
