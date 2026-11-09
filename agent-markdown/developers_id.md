---
title: "Pengembang | Tambahkan firmware khusus ke Innioasis Updater CE - Innioasis Unduhan Firmware"
description: "Dokumentasi pengembang untuk menambahkan firmware khusus Innioasis Y1 atau Y2 ke Updater CE: membagi repositori, menerbitkan aset rom.zip, mengedit slidia_manifest.xml, menguji, dan membuka permintaan tarik."
language: "id"
source: "https://innioasis.app/developers_id.html"
---

# Pengembang | Tambahkan firmware khusus ke Innioasis Updater CE - Innioasis Unduhan Firmware

Untuk pengembang firmware

# Tambahkan firmware Anda ke Updater CE.

Updater CE adalah katalog komunitas dan penginstal untuk firmware khusus. Kembangkan proyek Anda dari basis ROM, publikasikan sebagai repositori publik dengan aset rilis yang benar, tambahkan entri model ke `slidia_manifest.xml`, uji filter model, dan buka permintaan tarik. Satu repositori dapat melayani setiap model yang didukungnya.[Lihat sumber Updater CE](https://github.com/y1-community/Innioasis-Updater)[Telusuri Unduhan Perangkat Lunak](firmware_id.html)

## Mulai dari basis ROM

ROM Dasar memberi pengembang firmware khusus fondasi Android yang bersih dengan chip radio nirkabel diaktifkan. Pada Y1 mereka mengaktifkan Wi-Fi dan GPS bersama dengan Bluetooth dan FM pabrik; pada Y2 mereka mengaktifkan Wi-Fi, GPS, dan FM bersama dengan Bluetooth pabrik.Unduhan dasar ROM untuk pengembangan firmware khusus, dengan versi Android dan fitur nirkabel yang diaktifkan masing-masing[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Unduh | Perangkat | Android | Fitur nirkabel |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Menambahkan Wi-Fi dan GPS ke Bluetooth dan FM pabrik (FM sudah berfungsi di Y1 dari pabrik). Untuk pemutar Y1 yang dikirimkan dengan OS 2.0.0 atau lebih baru. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Menambahkan Wi-Fi dan GPS ke Bluetooth dan FM pabrik (FM sudah berfungsi di Y1 dari pabrik). Untuk Y1 pemain yang dikirimkan dengan OS lebih awal dari 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Menambahkan Wi-Fi, GPS, dan FM ke Bluetooth pabrik. Chip radio Y2 diaktifkan sepenuhnya, jadi FM juga tersedia di sini. |

Gambar-gambar ini adalah stok basis Android (AOSP) dengan radio nirkabel perangkat diaktifkan, sehingga firmware khusus dapat menambahkan fitur jaringan alih-alih mengganti tumpukan radio. Ini adalah titik awal praktis untuk langkah-langkah penerbitan di bawah ini.

## Gunakan nama aset rilis ini

Nama file adalah bagian dari sinyal kompatibilitas. Pertahankan nama yang tepat dan letakkan file ZIP di aset rilis proyek, tidak hanya di pohon sumber repositori.Nama aset ZIP firmware dan perangkat yang didukung``````

| Aset | Perangkat | Perangkat keras | Artinya |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 perangkat yang dikirimkan dengan OS 2.0.0 atau lebih baru. |
| rom_type_b.zip | Y1 | Type B | Y1 perangkat yang dikirimkan dengan OS lebih awal dari 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Paket instalasi lengkap Y2. Pisahkan dari aset Y1 . |
Jangan mengganti nama paket agar sesuai dengan model lain. Y1 dan Y2 menggunakan file platform MediaTek dan konfigurasi flashing yang berbeda. Publikasikan paket untuk perangkat keras yang didukungnya.

## Cara kerja koneksi

Updater CE membaca manifes sebagai katalognya. Masing-masing `<package>` baris memberitahukannya nama proyek, repositori, model, dan penangan. Saat pengguna memilih proyek tersebut, Updater memeriksa rilis repositori yang diterbitkan dan mencari a `rom*.zip` aset.

### nyata

Beri nama proyek dan petakan ke model. Y1 dan Y2 memerlukan baris terpisah, meskipun keduanya berbagi repositori.

### Rilis yang diterbitkan

Berisi aset ZIP yang dapat diinstal. Sebuah rilis tunggal mungkin berisi paket Y1 Type A, Y1 Type B, dan Y2 secara bersamaan.

### Pemasangan pembaruan CE

Menggunakan model yang dipilih untuk memilih paket yang cocok dan jalur flashing khusus model. Pengguna tidak perlu menebak nama file.

## Publikasikan proyek dalam lima langkah
  - Cabangkan repositori Updater CE. Buat garpu Anda sendiri [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), lalu kloning garpu Anda secara lokal.
  - Siapkan repositori firmware publik. Pastikan repositori bersifat publik dan rilisnya berisi aset ZIP yang benar. Anda bisa menempatkan `rom.zip`, `rom_type_b.zip`, dan `rom_y2.zip` pada rilis yang sama padahal keduanya berasal dari versi yang sama.
  - Edit manifes. Buka `slidia_manifest.xml` di root garpu Updater CE Anda. Tambahkan satu baris untuk setiap model yang didukung rilis (Y1 dan Y2 adalah pasangan yang umum). Itu `repo` nilainya adalah milik repositori `owner/repository`; `url` adalah halaman proyek publik.
  - Uji katalognya. Jalankan Updater dari checkout yang diedit. Pilih Y1 dan konfirmasikan bahwa proyek menampilkan aset Y1. Pilih Y2 dan konfirmasikan bahwa rilis Y2 ditampilkan. Centang Type A dan Type B secara terpisah ketika keduanya dipublikasikan.
  - Buka permintaan tarik. Dorong perubahan manifes ke fork Anda dan buka permintaan tarik terhadap repositori Updater CE upstream. Sertakan tautan proyek, model yang didukung, tag rilis, nama aset, dan perangkat yang Anda uji.

## Hasilkan garis manifes Anda

Isi repositori dan centang setiap model yang didukung rilis. Generator menulis satu `<package>` baris per model dan hanya menyertakan atribut yang Anda tetapkan, sehingga hasilnya sesuai dengan yang sekarang `slidia_manifest.xml` format. Setiap atribut yang dibaca Updater CE tersedia di bawah — atribut opsional ada di bawah Opsi lainnya.URL repositoriRepositori publik GitHub. Ekstrak generator `owner/repository` dari URL.Nama perangkat lunakDitampilkan di aplikasi dan katalog situs.URL proyekHalaman yang dapat dilihat manusia untuk proyek atau catatan rilisnya.MerekHapus ini untuk menggunakan merek default model. SR1, Q3, Q5 dan Q3e adalah model Timmkoo.Perangkat (masing-masing satu baris)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eModel lainnyaUntuk model yang tidak tercantum di atas. Model terkenal menjaga ejaan katalognya.Bendera`do_not_keep_data` — jangan pernah menawarkan Simpan Data untuk firmware iniDibangun dari Perangkat Lunak Asli — menambahkan `derivative="y1-community/y1-stock-rom"`

Keep Data hanya ditawarkan ketika firmware yang masuk dan firmware yang diinstal sama atau berbagi a `derivative` akar. Gunakan tanda ini hanya jika data pengguna benar-benar tidak dapat dipindahkan.Opsi lainnya: ikon, karya seni, aset rilis, pasca-instalasi, dan mirror

#### Ikon dan karya seniBerkas ikonPilih gambar yang akan Anda komit ke repositori. Ini mempratinjaunya dan membuat URL mentahnya; itu tidak mengunggah apa pun.Jalur ikon di repositoriJalur ke gambar yang dikomit, relatif terhadap akar repositori.Cabang ikonURL IkonURL gambar langsung. Jika kosong, aplikasi akan menggunakan rilis tersebut `updater.png` atau ikon yang dihasilkan.Pratinjau ikon yang dipilih

URL ikon mode gelapIkon tema gelap opsional. `image_dark` adalah alias yang diterima.URL karya seni ringanKarya seni sekunder, dicoba setelah gambar rilis dan `icon`.URL karya seni gelap

#### Lepaskan asetRilis nama asetSatu nama untuk setiap model yang dipilih. Biarkan kosong untuk digunakan `rom.zip` pada Y1 dan `rom_<model>.zip` di tempat lain.Pola asetGlob digunakan ketika ritsleting rilis tidak diberi nama `rom*.zip`.Type A asetGlob untuk paket Y1 Type A ketika namanya tidak disebutkan.Type B asetGlob untuk paket Y1 Type B ketika namanya tidak disebutkan.Versi aplikasi minimumSembunyikan entri dari versi Updater CE yang lebih lama.

#### Tautan, cermin, dan keluarga Keep DataHalaman pasca-instalDibuka setelah instalasi berhasil.Halaman kedua pasca pemasanganLangkah kedua opsional untuk panduan pengaturan multi-halaman.Cermin zip portabelDipisahkan koma `*-mirror` repositori yang membuat paket Portable Flashing Zip.Repositori turunanFirmware yang digunakan untuk membuat rilis ini. Firmware terkait berbagi partisi data, yang merupakan pemeriksaan Keep Data.Gudang informasiRepo aplikasi yang rilisnya menjelaskan aplikasi dalam firmware ini. Itu juga memerlukan halaman pasca-instalasi.APK repositoriRepo aplikasi yang APK aplikasinya diunduh dan diinstal setelah firmware.

#### Ekstra katalogSiputPengidentifikasi stabil untuk tautan dan catatan pemasangan yang disimpan. Model ditambahkan secara otomatis ketika beberapa model dipilih.Deskripsi`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Salin garis

Memuat manifes terbaru…Pratinjau manifes terbaru dengan baris Anda yang ditambahkan

Generator mengambil arus `slidia_manifest.xml` dari repositori ini dan masukkan baris yang Anda buat sebelumnya `</slidia>`.

Satu baris saja tidak cukup untuk repositori bersama. Jika baris Y2 tidak ada, pengguna Y2 tidak akan mendapatkan entri yang cocok dengan model meskipun `rom_y2.zip` ada dalam rilis proyek. Hal yang sama juga berlaku untuk setiap model lain yang didukung rilis Anda.

### Setiap atribut yang dibaca manifes

Ini adalah atribut yang dipahami oleh Updater CE build saat ini. Generator hanya menulis yang Anda isi; aplikasi lainnya kembali ke default yang masuk akal.atribut paket slidia_manifest.xml dan artinya``````````````````````````````````````````````````````````````````````````````````````````````

| Atribut | Dibutuhkan | Apa fungsinya |
| --- | --- | --- |
| name | Ya | Nama perangkat lunak ditampilkan di katalog dan di kartu instalasi. |
| repo | Ya | owner/repo. Aplikasi membaca rilis GitHub repositori tersebut. |
| device | Ya | Model target, huruf besar (Y1, Y2, G1, Q3e, …). Simpan satu entri per model. |
| url | Direkomendasikan | Halaman proyek atau catatan rilis dibuka dari katalog. |
| type, handler | Ya dalam praktiknya | type="img" dan handler="Custom Firmware". Tipe lain dan penangan non-firmware dilewati. |
| brand | Opsional | Merek katalog (Innioasis, Timmkoo). Kosong menggunakan merek default model. |
| package_name | Opsional | Rilis nama file aset. Defaultnya adalah rom.zip pada Y1 dan rom_<model>.zip pada model lain. |
| asset_pattern | Opsional | Gumpalan yang tidak peka huruf besar-kecil untuk rilis yang ritsleting firmwarenya tidak diberi nama rom*.zip (misalnya my-firmware-*.zip). |
| type_a_asset, type_b_asset | Opsional | Glob yang mengidentifikasi zip Y1 Type A dan Type B ketika nama filenya tidak berisi penanda biasa. |
| icon | Opsional | URL logo. Digunakan setelah rilisnya sendiri updater.png / updater.jpg, dan sebagai pengganti untuk setiap rilis. |
| icon_dark | Opsional | Logo bertema gelap. image_dark adalah alias yang diterima. |
| image | Opsional | Karya seni ringan sekunder, dicoba setelahnya icon. |
| post_install, post_install2 | Opsional | Halaman dibuka setelah instalasi berhasil. Yang kedua mencakup panduan multi-langkah. |
| portable_zips | Opsional | Dipisahkan koma *-mirror repo yang menerbitkan paket portabel yang siap dijalankan. |
| derivative | Opsional | Repositori tempat firmware dibuat. Firmware dengan root turunan yang sama dapat menyimpan data pengguna. |
| info_repo | Opsional | Repositori aplikasi yang rilisnya menjelaskan apa yang disebarkan firmware. Membutuhkan post_install atau post_install2. |
| apk_repo | Opsional | Repositori aplikasi yang APK aplikasinya diinstal setelah firmware. |
| min_version | Opsional | Sembunyikan entri ketika Updater CE lebih tua dari versi ini. |
| do_not_keep_data | Opsional | true (juga 1 / yes) memblokir Simpan Data sepenuhnya untuk firmware ini. |
| slug | Opsional | Pengidentifikasi stabil untuk tautan dan catatan pemasangan yang disimpan. Dihasilkan dari nama dan model saat kosong. |
| description | Opsional | Deskripsi katalog singkat. Ini bisa berupa nilai atribut atau teks elemen. |

Nama lama masih dibaca untuk kompatibilitas: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` dan `image_dark`. Entri baru harus menggunakan nama saat ini di atas.

### Kirimkan baris sebagai permintaan tarik
  - Salin baris yang dihasilkan di atas. Mereka sudah cocok dengan format manifes terbaru.
  - Sunting `slidia_manifest.xml` di repositori. Gunakan tautan edit di bawah; host repositori membuat fork dan cabang untuk Anda secara otomatis.
  - Tempelkan baris sebelumnya `</slidia>`, menjaga entri yang ada tidak berubah.
  - Berkomitmen pada cabang baru (misalnya `add-your-firmware`), lalu buka permintaan tarik terhadap repositori Updater CE.
  - Dalam PR, sertakan tautan proyek, model yang didukung, tag rilis, nama aset, dan perangkat yang Anda uji.
[Edit manifes Updater CE](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Lihat manifes terbaru](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Pertahankan nama model dalam huruf besar, gunakan URL persis dari repositori publik Anda, dan simpan `type="img"` dan `handler="Custom Firmware"` untuk entri firmware.

## Jadikan rilisnya mudah untuk diverifikasi

Berikan label rilis dan catatan rilis yang jelas pada rilis tersebut. Tag ini berguna bagi orang-orang, tetapi nama aset ZIP adalah apa yang digunakan Updater CE untuk mengidentifikasi paket instalasi.

### Daftar periksa rilis
  - Publikasikan rilis tersebut secara publik.
  - Lampirkan file ZIP sebagai aset rilis.
  - Nyatakan model yang didukung dan Type A atau Type B dalam catatan.
  - Buat daftar persiapan yang diperlukan atau batasan yang diketahui.

### Satu rilis, tiga aset

Rilis bersama dapat berisi `rom.zip`, `rom_type_b.zip`, dan `rom_y2.zip`. Updater mengklasifikasikannya secara terpisah dan memilih dari model dan filter perangkat keras.

### Jangan menggabungkan tebakan

Jangan menyertakan paket Y1 di bawah nama file Y2, atau menambahkan data sebar, prapemuat, atau partisi yang belum teruji hanya untuk memunculkan aset.

## Mengapa entri model penting selama flashing

Manifes bukan sekedar menu download. Setelah ekstraksi, Updater CE menggunakan model yang diselesaikan untuk menyiapkan jalur instalasi yang cocok. Y1 dan Y2 memiliki file platform, prapemuat, konfigurasi sebar, dan tata letak perangkat yang berbeda.
  - Y1: pembaru menyiapkan jalur Y1 dan menggunakan partisi bernama perangkat saat MTKClient digunakan.
  - Y2: pembaru menyiapkan jalur Y2 dan menggunakan konfigurasi Y2 MT6582. Pemulihan penuh dapat menggunakan alamat fisik dari data sebar yang modelnya benar.
  - Dukungan Lintas Platform: Updater CE menangani flashing asli langsung di Windows, Linux, dan macOS (mendukung Intel dan Apple Silicon Mac) tanpa alat flashing tambahan.
Kontributor harus memberikan file firmware yang benar, bukan offset flash. Jangan mengedit alamat pencar, prapemuat, file DA, atau perintah partisi untuk mengatasi paket yang buruk. Perbaiki aset rilis dan uji pada model yang diinginkan.

## Sebelum Anda meminta penggabungan
  - Validasi XML dengan parser XML. Kutipan atau penutup hilang `/>` dapat menyembunyikan setiap entri setelahnya.
  - Luncurkan pembaru dari checkout Anda sehingga memuat manifes lokal sebelum penyegaran jarak jauh.
  - Periksa Y1 dan Y2 secara terpisah. Konfirmasikan bahwa proyek hanya muncul jika paketnya didukung.
  - Periksa daftar rilis untuk `rom.zip`, `rom_type_b.zip`, dan `rom_y2.zip` sebagaimana berlaku.
  - Uji penginstalan sebenarnya pada perangkat yang dimaksud, dengan kabel data USB yang andal dan rencana pemulihan untuk kembali ke Perangkat Lunak Asli.
  - Dalam permintaan tarik, jelaskan apa yang Anda uji. Jangan mendeskripsikan model yang belum diuji sebagai model yang didukung.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Untuk pemeriksaan lokal, jalankan perintah itu dari root repositori. Ini memverifikasi sintaks XML saja; itu tidak membuktikan bahwa rilis berisi firmware yang valid atau perangkat aman untuk di-flash.

## Tautan proyek yang berguna[Pembaruan Garpu CE](https://github.com/y1-community/Innioasis-Updater/fork)[Lihat manifesnya](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Catatan kontribusi komunitas](support_devs_id.html)[Pemecahan masalah](troubleshooting_id.html)

## Memodifikasi keterampilan untuk agen AI

Repositori itu `skills/` direktori adalah basis pengetahuan berbasis sumber untuk agen yang mengerjakan Y1 dan Y2 perangkat keras, firmware, tema, dan aplikasi. Setiap keterampilan memberi nama pada file proyek asal klaimnya, sehingga agen dapat memeriksa fakta sebelum mengganti perangkat.Mulai di sini

### [Indeks keterampilan dan aturan keselamatan](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Cara memuat keterampilan, model mana yang berlaku, dan partisi yang tidak boleh ditulis oleh paket mana pun.Perangkat keras

### [Y1 perangkat keras](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, roda sebagai peristiwa penting, tampilan 480x360, jalur FM/audio, penyimpanan dan peta partisi Type A/B.Perangkat keras

### [Y2 perangkat keras](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Papan MT6582, pohon perangkat, panel GC9503V/ST7701S, rel PMIC/DAC, partisi dan image boot.Firmware

### [Paket firmware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomi, file sebar, kontrak pembaruan Kelas A, dan daftar periksa rilis.Tema

### [Penulisan tema dan kulit](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 tema config.json, Rockbox WPS/SBS, Reborn skin dan Y2Player format skin v2.Semua keterampilan

### [Jelajahi folder keterampilan](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, stok ROM Android, Y2Linux, aplikasi Android, peluncur, catatan rilis, dan penerbitan situs.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
