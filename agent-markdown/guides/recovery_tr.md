---
title: "Innioasis Y1 ve Y2 Kurtarma Kılavuzu | Innioasis Aygıt Yazılımı Arşivi - Innioasis Aygıt Yazılımı İndirmeleri"
description: "Açılmayan veya güncelleme sonrasında çalışmayı durduran kaydırma tekerleğine sahip olan Innioasis Y1 ve Y2 oyuncular için kurtarma kılavuzu. Sıfırlama ve ürün yazılımı adımları."
language: "tr"
source: "https://innioasis.app/guides/recovery_tr.html"
---

# Innioasis Y1 ve Y2 Kurtarma Kılavuzu | Innioasis Aygıt Yazılımı Arşivi - Innioasis Aygıt Yazılımı İndirmeleri

Oyuncu kurtarma · Y1 ve Y2

# Innioasis Y1 ve Y2 kurtarma kılavuzu

Açılmıyor, tekerlek çalışmıyor veya kurulum yarı yolda duruyor. Belirtiyle başlayın ve ardından doğrudan manuel flaşa geçmek yerine adımları sırayla izleyin.[Updater CE edin](../guide_tr.html#platform)[Aygıt Yazılımı İndirmeleri](../firmware_tr.html)[Sorun giderme](../troubleshooting_tr.html)

Innioasis Updater ile başlayın

## Kılavuzlu kurulum bunların çoğunu düzeltir

Güncelleyici bunu tek geçişte yapar. Yazılımı seçin, ekrandaki adımları izleyin ve işiniz bitti. Ayrıca bir düzeltmenin veya yeni bir sürümün ne zaman yayınlanacağını da size bildirir.

## Semptomla başlayın

Bu kılavuzlar, insanların bir güncelleme veya flaş sonrasında en sık karşılaştıkları iki arızayı kapsar. Gördüğünüzle eşleşeni seçin ve ardından sırayla çalışın.

### Kaydırma tekerleği çalışmıyor

Çark dönüyor ancak oynatıcı bunu görmezden geliyor veya güncellemeden hemen sonra duruyor.

[Y1 kaydırma tekerleği kılavuzu](y1-scroll-wheel-not-working_tr.html) · [Y2 kaydırma tekerleği kılavuzu](y2-scroll-wheel-not-working_tr.html)

### Oynatıcı açılmıyor

Siyah bir ekran, şarj ışığı yok veya görünüp kaybolan bir logo.

[Y1 güç kılavuzu](y1-wont-turn-on_tr.html) · [Y2 güç kılavuzu](y2-wont-turn-on_tr.html)

### Kurulum yarı yolda durduruldu

Güncelleyici USB isteminden önce veya sonra başarısız oldu ya da sürüm listesi yanlış görünüyor.

[Sorun giderme kılavuzu](../troubleshooting_tr.html)

### Dosyalara ihtiyacım var

Orijinal Yazılım ve her modele özel paketler.

[Aygıt Yazılımı İndirmeleri](../firmware_tr.html)

## Y1 ve Y2 paketleri birbirinin yerine kullanılamazBir modele asla çapraz flaş uygulamayın. bir Y1 `rom.zip` bir Y2 paketi değil ve bir Y2 `rom_y2.zip` Y1 üzerinde çalışmayacak. Yanlış modelin yanıp sönmesi, bir oyuncunun ölü kontrollerle veya önyükleme döngüsüyle sonuçlanmasının en yaygın nedenlerinden biridir.

Oynatıcının üzerinde yazılı olan modeli kontrol edin ve bir sürüm seçmeden önce bunu Güncelleyici CE'de eşleştirin.

## Önce eşleşen Orijinal Yazılımı geri yükleyin

Herhangi bir manuel araçtan önce, doğru modelin stok donanım yazılımını oynatıcıya geri koyun. Bu, güncellemeyle ilgili tekerlek ve önyükleme hatalarının çoğunu giderir.

Y1: Y1'ı seçin, Orijinal Yazılım'ı seçin, kararlı bir Y1 sürümü seçin ve ardından Yükle / Geri Yükle'yi çalıştırın. [Tam Y1 geri yükleme kılavuzu](restore-original-y1_tr.html).

Y2: Y2'ı seçin, Orijinal Yazılım'ı seçin, kararlı bir Y2 sürümü seçin ve ardından Yükle / Geri Yükle'yi çalıştırın. [Tam Y2 geri yükleme kılavuzu](restore-original-y2_tr.html).

Oynatıcıyı kapatın ve USB veri kablosunu yalnızca Güncelleyici istediğinde bağlayın. Başarı mesajına kadar bağlı bırakın.

## Güncelleyici CE ile birlikte gelen manuel kurtarma

Güncelleyici işi bitiremediğinde, aynı kurulum manuel araçları da içerir. [SP Flash Tool](../sp-flash-tool_tr.html) Windows ve Linux x86 makinelerinde paketlenmiştir ve MTKClient rotası macOS'u kapsar. Her ikisinin de modelle eşleşen bir ürün yazılımı paketine ihtiyacı vardır; [Aygıt Yazılımı İndirmeleri](../firmware_tr.html) sayfa.

Platformunuza uygun kılavuzu kullanın ve oynatıcının şarjını koruyun. Hiçbir araç oynatıcıyı algılayamazsa, hata büyük ihtimalle ürün yazılımından ziyade donanımdadır.

## Yardım istediğinizde neleri dahil etmelisiniz?
  - Oynatıcının üzerinde basılı olan model — Y1 veya Y2 —.
  - Ekran ne yapar: hiçbir şey, logo, önyükleme döngüsü veya ana ekran.
  - Bir bilgisayarın oynatıcıyı MediaTek cihazı olarak algılayıp algılamadığı.
  - Tam Güncelleyici mesajı ve seçtiğiniz paket.
  - Herhangi bir manuel araç dahil, daha önce denediğiniz şeyler.

Özel belirteçleri veya ilgisiz sistem dosyalarını göndermeyin. [topluluk Discord](https://discord.gg/zHrT2zrcek) Ve [r/innioasis](https://reddit.com/r/innioasis) notları karşılaştırmak için en hızlı yerlerdir.

## Innioasis kurtarma SSS

### Açılmayan bir Innioasis oynatıcıyı nasıl düzeltirim?

Bilinen bir veri kablosuyla 30 dakika şarj edin, gücü 15 saniye basılı tutarak yeniden başlatmaya zorlayın, ardından bilgisayarın bunu algılayıp algılamadığını kontrol edin. Eğer öyleyse, modelle eşleşen Orijinal Yazılımı geri yükleyin; değilse Updater CE'de bulunan manuel kurtarma araçlarını kullanın.

### Y1 veya Y2 kaydırma tekerleğim neden çalışmıyor?

Tekerlek bir güncellemeden sonra durursa, bu genellikle bir ürün yazılımı uyumsuzluğundan kaynaklanır. Model uyumlu Orijinal Yazılımı yeniden yükleyin ve tekrar test edin. Her ürün yazılımında tekerlek ölüyse, bunu bir donanım hatası olarak değerlendirin.

### Kurtarma için ürün yazılımını nereden indirebilirim?

İnnioasis.app/firmware.html adresindeki Firmware İndirmeleri sayfası, her model için orijinal ve özel paketleri barındırır. Her zaman oynatıcıyla eşleşen Y1 veya Y2 paketini seçin.

### Updater CE'ye hangi kurtarma araçları dahildir?

Güncelleyici CE, normal yükleme tamamlanamadığında manuel kurtarma için Windows ve Linux'ta SP Flash Tool ve macOS dahil MTKClient rotasını içerir.

## İlgili düzeltmeler
  - [Y1 kaydırma tekerleği çalışmıyor](y1-scroll-wheel-not-working_tr.html) — güncellemeden sonra tıklama tekerleği yanıt vermiyor
  - [Y2 kaydırma tekerleği çalışmıyor](y2-scroll-wheel-not-working_tr.html) — Y2 için aynı kontroller
  - [Y1 açılmıyor](y1-wont-turn-on_tr.html) — şarj etme, yeniden başlatma ve manuel kurtarma
  - [Y2 açılmıyor](y2-wont-turn-on_tr.html) — Y2 için aynı kontroller
  - [SP Flash Tool kılavuz](../sp-flash-tool_tr.html) — Windows ve Linux'ta manuel yanıp sönme

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
