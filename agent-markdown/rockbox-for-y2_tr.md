---
title: "Y2 (Rockbox-Y2 için Rockbox: genel bakış, yapımlar ve kurulum kılavuzu"
description: "Y2 için Rockbox, Rockbox-Y2 ve rockbox-y2, Innioasis Y2 için topluluk Rockbox donanım yazılımı bağlantı noktasına atıfta bulunur. Neleri içerdiğini ve Innioasis Updater CE ile nasıl kurulacağını öğrenin."
language: "tr"
source: "https://innioasis.app/rockbox-for-y2_tr.html"
---

# Y2 (Rockbox-Y2 için Rockbox: genel bakış, yapımlar ve kurulum kılavuzu

[← Ürün Yazılımı İndirmeleri](firmware_tr.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Y2 için Rockbox (Rockbox-Y2)

Rockbox-Y2 (Y2 için “Rockbox olarak da adlandırılır”), Innioasis Y2 için özel topluluk Rockbox donanım yazılımı bağlantı noktasıdır. Kendi ROM paketini kullanır (`rom_y2.zip`) ve doğrudan Innioasis Güncelleyici CE aracılığıyla yüklenir.[Rockbox-Y2 yükleyin](rockbox-y2/install.html)[ROM dosyasını indirin](rockbox-y2/download.html)[Yazılı eğitim](guides/rockbox-y2.html)[Rockbox-Y2 merkezi](rockbox-y2/)

## Innioasis Y2 için özel olarak tasarlandı

Innioasis Updater CE'de bu ürün yazılımı şu şekilde listelenir: Rockbox Ne zaman Y2 seçilir. Yayınları tarafından yayınlanmaktadır. [spycemagic/y2-rockbox](firmware_tr.html?model=Y2&software=rockbox-y2) paket adı ile proje `rom_y2.zip`.

Y2 cihazına asla Y1 ürün yazılımı paketi yüklemeyin. Seçme Y2 Güncelleyici CE'de sürüm listesini yalnızca Y2 uyumlu sürümlere göre otomatik olarak filtreler.

## Rockbox-Y2 neler sunuyor?
  - Etiket tabanlı müzik kitaplığı — ses dosyası etiketlerinizden albümlere, sanatçılara ve türlere göz atın veya klasörlere doğrudan göz atın.
  - Oynatma kontrolleri — boşluksuz oynatma, çapraz geçiş, ReplayGain ve ekolayzır ayarları.
  - Özel temalar — Rockbox-Y2 yapınızla uyumlu temalar yükleyin ([Y2 tema kılavuzu](rockbox-y2-themes.html)).
  - %100 çevrimdışı — hesap veya abonelik olmadan MicroSD kartınızdaki yerel dosyaları oynatır.
  - Kolay fabrika geri yüklemesi — Güncelleyici CE'de istediğiniz zaman Y2 Orijinal Yazılıma geri dönün.

## Bir Rockbox-Y2 sürümü seçme
  - Her zaman seç Y2 içinde Cihaz modeli Birinci.
  - Belirli bir sürümü test etmediğiniz sürece en son sürümü seçin.
  - Okuyun [Rockbox-Y2 sürüm notları](release-notes/rockbox-y2/index_tr.html) her yapıda nelerin değiştiğini görmek için.

## Topluluk geliştiricilerinden doğrudan indirmeler

Innioasis Güncelleyici CE, donanım yazılımı paketlerini her zaman doğrudan topluluk donanım yazılımı geliştiricilerinden indirir ([spycemagic/y2-rockbox](firmware_tr.html?model=Y2&software=rockbox-y2)) ve bu geliştiriciler, yazılım sürümlerinin Güncelleyici CE'de listelenmesinden yalnızca sorumludur.

Updater CE'nin indirilmesine ve flashlanmasına izin verebilirsiniz `rom_y2.zip` otomatik olarak veya paketimizden indirin. [Rockbox-Y2 indirme sayfası](rockbox-y2/download.html) Ve [Rockbox ROM indirme sayfası](rockbox-rom-download_tr.html).[Rockbox-Y2 indirme](rockbox-y2/download.html)[Yerel bir ZIP'ten yükleyin](rockbox-y2/portable-zip.html)

## Rockbox-Y2 nasıl yüklenir
  - Innioasis Güncelleyici CE'yi açın ve ayarlayın Cihaz modeli ile Y2.
  - Seçme Rockbox içinde Yazılım.
  - Listeden bir Y2 yayın seçin.
  - Tıklamak Yükle / Geri yükle bu nedenle Güncelleyici CE, paketi doğrudan geliştiriciden indirir.
  - Güncelleyici CE sorduğunda Y2'ı tamamen kapatın ve bir USB veri kablosuyla bağlayın.
  - Tamamlanma mesajını bekleyin, ardından Y2 cihazınızın fişini çekin ve açın.

Adım adım açıklamalı kılavuzun tamamını okuyun [Rockbox-Y2 öğretici](guides/rockbox-y2.html).

## Orijinal Y2 yazılımı geri yükleme

Fabrika ürün yazılımına geri dönmek için öğesini seçin. Y2 Ve Orijinal yazılım Güncelleyici CE'de kararlı bir sürüm seçin ve Yükle / Geri yükle. Bkz. [geri yükleme kılavuzu](rockbox-y2/restore-stock.html) Ve [Y2 Orijinal Yazılım sayfası](original-software-y2_tr.html).

## Sık sorulan sorularGüncelleyici CE Rockbox-Y2 dosyasını nereden indiriyor?

Updater CE, bellenim paketlerini her zaman doğrudan topluluk bellenim geliştiricilerinin kendi sürümlerinden indirir (`spycemagic/y2-rockbox`). Geliştiriciler, yazılım sürümlerinin Güncelleyici CE'de listelenmesinden yalnızca sorumludur.Paket neden rom_y2.zip olarak adlandırılıyor?

Geliştirici Y2 donanım yazılımı arşivini adlandırır `rom_y2.zip` bu yüzden Y1'larla karıştırılamaz `rom.zip`.Y1 temaları Y2 üzerinde çalışıyor mu?

Her zaman değil. Y2 yapınızın sürüm notlarına bakın ve [Rockbox-Y2 tema kılavuzu](rockbox-y2-themes.html).

## İlgili kılavuzlar

### [Rockbox-Y2 merkezi](rockbox-y2/)

Tüm Y2 kılavuzlar: yükleme, indirmeler, temalar, geri yükleme, çift önyükleme ve sorun giderme.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 ve Y2 Rockbox yapılarının farklılıkları.

### [Rockbox-Y2 temalar](rockbox-y2-themes.html)

Rockbox-Y2 üzerinde temaların yüklenmesi ve sıfırlanması.

### [Y1 için Rockbox](rockbox-for-y1_tr.html)

Innioasis Y1 bağlantı noktası için genel bakış ve kurulum kılavuzu.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
