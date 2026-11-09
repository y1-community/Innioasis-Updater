---
title: "driver Innioasis Y1 dan Y2 USB | Izin driver Windows dan Linux - Innioasis Pembaruan"
description: "Siapkan komputer Anda untuk Innioasis Updater: driver Windows MediaTek dan izin Linux USB — ditambah perbaikan kabel dan pengaturan waktu."
language: "id"
source: "https://innioasis.app/drivers_id.html"
---

# driver Innioasis Y1 dan Y2 USB | Izin driver Windows dan Linux - Innioasis Pembaruan

Pengaturan komputer

# Siapkan komputer sebelum pemutar.

Sebagian besar masalah koneksi berasal dari driver, izin, kabel, atau pengaturan waktu. Windows memerlukan driver MediaTek yang diinstal. Linux memerlukan izin USB yang tepat. Temukan platform Anda di bawah.[Dapatkan Updater CE](guide_id.html#platform)[Pemecahan masalah](troubleshooting_id.html)

## Windows
  - Unduh penginstal driver MediaTek di bawah.
  - Jalankan penginstal dan izinkan Windows menginstal driver.
  - Nyalakan kembali komputer.
  - Buka Updater CE dan tunggu perintah koneksi sebelum Anda mencolokkan pemutar yang dimatikan.

Beberapa sistem Windows memblokir driver melalui isolasi Inti (Integritas memori). Jika Updater CE masih tidak dapat melihat pemutar setelah dimulai ulang, matikan Integritas memori di Keamanan Windows, mulai ulang, dan instal ulang driver. Aktifkan kembali pengaturan setelah Anda selesai jika sistem Anda mengizinkannya.

Windows tidak meluncurkan aplikasi? Jika Keamanan Windows atau Kontrol Aplikasi Cerdas menghentikan pembukaan Updater CE, buka Pengaturan (tekan Win + I) → Privasi & keamanan → Windows Security → Kontrol aplikasi & browser → Pengaturan Kontrol Aplikasi Cerdas dan atur ke Mati. Kontrol Aplikasi Cerdas saat ini memengaruhi aplikasi populer seperti Epic Overlay Service (digunakan oleh Fortnite) — Updater CE aman dan terverifikasi untuk digunakan. Untuk mengaktifkan kembali nanti, setel `VerifiedAndReputablePolicyState` untuk `1` (Aktif) atau `2` (Mode Evaluasi) di bawah `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` di Penyunting Registri.[Unduh driver Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Kembali ke panduan utama](guide_id.html#windows) · [Unduhan Perangkat Lunak](firmware_id.html)

## Izin Linux USB

Linux memerlukan akun pengguna Anda untuk diizinkan berkomunikasi dengan chip MediaTek USB di dalam pemutar. Updater CE biasanya menyelesaikan masalah ini selama instalasi, dan izin yang sama mencakup SP Flash Tool, jadi perlakukan ini sebagai langkah perbaikan daripada tahap normal.
  - Jalankan Updater CE sebagai pengguna biasa, bukan sebagai root. Pemasang meminta akses administrator hanya jika diperlukan.
  - Periksa apakah pemain terlihat sama sekali. Matikan pemutar, sambungkan kabel, dan jalankan perintah lsusb di terminal. Pemutar yang terhubung muncul sebagai perangkat MediaTek dengan ID vendor 0e8d.
`lsusb`
  - Jika muncul di lsusb tetapi Innioasis Updater CE atau SP Flash Tool mengatakan izin ditolak atau tidak dapat membuka port, pengguna Anda kehilangan akses ke perangkat USB. Aturan udev yang sama mencakup kedua alat tersebut, jadi tambahkan satu yang memungkinkan kelompok pengguna membacanya.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Simpan baris tersebut ke file baru bernama /etc/udev/rules.d/51-innioasis.rules, lalu jalankan:`sudo udevadm control --reload && sudo udevadm trigger`
  - Cabut pemutar sepenuhnya, sambungkan kembali, dan coba instal lagi.
  - Jika SP Flash Tool melaporkan izin serial atau port race, cabut sepenuhnya dan sambungkan kembali hanya jika diminta.
Jangan berimprovisasi pada offset flash.Jika Anda berpindah ke alat pemulihan manual, gunakan file dan konfigurasi khusus model yang dikirimkan bersama proyek.

[Kembali ke panduan utama](guide_id.html#linux) · [Unduhan Perangkat Lunak](firmware_id.html) · [SP Flash Tool panduan](sp-flash-tool_id.html)

## Kabel dan waktu
  - Gunakan kabel data USB yang dikenal.
  - Hindari hub saat memecahkan masalah.
  - Matikan model yang benar sepenuhnya.
  - Hubungkan hanya jika diminta.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
