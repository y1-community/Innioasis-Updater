---
title: "Cara Memulihkan Pemain yang Non-Booting MediaTek Setelah Kegagalan Klien MTK · Innioasis Komunitas"
description: "Panduan langkah demi langkah untuk membatalkan pemasangan dan memulihkan pemutar Innioasis Y1, Y2, G1, Timmkoo, dan MediaTek yang tidak melakukan booting setelah klien MTK menghentikan flash di Linux atau macOS."
language: "id"
source: "https://innioasis.app/recover-non-booting-device_id.html"
---

# Cara Memulihkan Pemain yang Non-Booting MediaTek Setelah Kegagalan Klien MTK · Innioasis Komunitas

Pemecahan Masalah & Pemulihan Perangkat

# Memulihkan Perangkat Non-Boot Setelah Klien MTK Berkedip

Jika perangkat Innioasis Y1, Y2, atau MediaTek Anda gagal menyala atau menampilkan layar hitam setelah melakukan flashing dengan klien MTK di macOS atau Linux, jangan panik. BootROM perangkat keras (BROM) bersifat permanen dan tidak dapat dimusnahkan.

## Mengapa Klien MTK Mungkin Menghentikan atau Meninggalkan Layar Hitam

Klien MTK mengandalkan muatan eksploitasi perangkat lunak (kamakiri / amonet) untuk melewati otentikasi DA dan komunikasi mentah USB melalui libusb. Pada sistem macOS dan Linux ARM64:
  - USB latensi jabat tangan atau batas waktu port pada macOS dapat menghentikan injeksi muatan DA di tengah transfer.
  - Header partisi yang hilang atau tidak lengkap membuat bootloader (preloader/lk) dalam keadaan tidak responsif.
  - Pemutar tampak mati total—tidak ada LED, tidak ada ikon pengisian daya, tidak ada lampu latar layar.

Bahkan dalam keadaan ini, chipset MediaTek turun kembali Modus BROM (USB VID 0e8d, PID 0003), siap untuk pemulihan resmi tingkat rendah.

## Metode Pemulihan Definitif: SP Flash Tool Mesin di Updater CE

Cara teraman dan paling andal untuk memulihkan pemain Anda yang terkena brick adalah dengan menggunakan Pembaruan CE dikonfigurasi dengan resmi SP Flash Tool bagian belakang.

### Langkah Tepat di Updater CE:
  - Buka Pembaruan CE.
  - Klik Pengaturan di sidebar navigasi kiri.
  - Gulir ke bawah ke bagian Lanjutan dan aktifkan Tampilkan Pengaturan Lanjutan.
  - Di bawah Metode Instalasi (atau Mesin Berkedip untuk penginstal MediaTek), temukan Metode Flash tarik-turun.
  - Ubah pilihan dari Otomatis (disarankan) atau MTKClient untuk SP Flash Tool.
  - Konfirmasikan perintah tersebut dan kembali ke alur instalasi utama.

## Arsitektur Platform & Persyaratan OS untuk SP Flash Tool

MediaTek resmi `SP Flash Tool` biner dikompilasi secara asli sebagai x86_64 biner ELF untuk Linux dan sebuah PE32+ dapat dieksekusi untuk Windows x64.Catatan Perangkat Keras Penting untuk Pengguna macOS dan ARM64 Linux:
 Karena MediaTek tidak mengkompilasi SP Flash Tool untuk macOS (Darwin) atau Linux ARM64 (aarch64), pengguna macOS dan pengguna Linux ARM64 (seperti Raspberry Pi atau Apple Silicon yang menjalankan Asahi Linux) yang mengalami brick harus menghubungkan pemutar mereka ke: 
  - Sebuah x64 PC Windows (Windows 10/11 64-bit), atau
  - Sebuah x86_64 PC Linux (Ubuntu, Debian, Fedora, Lengkungan 64-bit).

## Proses Pembongkaran Perangkat Keras Langkah-demi-Langkah
  - Putuskan Sambungan Pemutar: Cabut sepenuhnya kabel USB dari player dan PC.
  - Matikan Keras: Tahan tombol Daya (atau Daya + Volume Turun) selama 15 detik untuk memastikan chipset dimatikan sepenuhnya dan tidak terjebak dalam loop USB berdaya rendah.
  - Luncurkan Updater CE dengan Mode SP Flash Tool: Pilih model perangkat Anda (mis. Innioasis Y1 atau Innioasis Y2) dan pilih Perangkat lunak asli untuk memulihkan partisi stok.
  - Memulai Instal/Pulihkan: Klik Pasang / Pulihkan di Pembaruan CE. Tunggu hingga pesan status berbunyi Menunggu pemain...
  - Masukkan Kabel USB untuk Memicu BROM: Saat perangkat MATI, colokkan kabel USB langsung ke port USB motherboard berkecepatan tinggi (hindari hub USB yang tidak memiliki daya).
  - Sistem akan mendeteksi port VCOM MediaTek, mendorong Download Agent (DA), menulis ulang tabel partisi, dan memulihkan semua image firmware dengan bersih.

## Permutasi berdasarkan Model dan Sistem Operasi

| Model | Platform Gagal | Pengaturan Pemulihan yang Direkomendasikan | Mesin & Mode |
| --- | --- | --- | --- |
| Innioasis Y1 | MacOS (Apple Silicon/Intel) | Windows x64/Linux x86_64 PC | SP Flash Tool + Y1 Stok ROM |
| Innioasis Y1 | Linux ARM64/x86_64 | Linux x86_64 atau PC Windows x64 | SP Flash Tool + DA Komunitas |
| Innioasis Y2 | macOS (klien MTK terhenti) | Windows x64/Linux x86_64 PC | SP Flash Tool + Y2 Pemulihan Sebaran |
| Innioasis G1 / G3 / G5 | klien macOS / Linux MTK | PC Windows x64 dengan Driver VCOM | SP Flash Tool + Firmware Pabrik |
| Mechen H1 / Timmkoo A5 | Platform apa pun | PC Windows x64 atau Linux x86_64 | SP Flash Tool + File sebar |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
