---
title: "Orijinal Yazılımı Innioasis G1 Üzerinde Geri Yükleme - adım adım"
description: "Doğrulanmış rom_g1.zip paketini kullanarak Innioasis Updater CE veya SP Flash Tool ile Innioasis G1 cihazındaki resmi Orijinal Yazılım nasıl geri yüklenir."
language: "tr"
source: "https://innioasis.app/guides/restore-original-g1_tr.html"
---

# Orijinal Yazılımı Innioasis G1 Üzerinde Geri Yükleme - adım adım

Geri yükleme kılavuzu · Innioasis G1

# Orijinal Yazılımı Innioasis G1 Üzerinde Geri Yükle

Oynatıcının birlikte gönderdiği yazılıma temiz bir dönüş. Başarısız bir güncellemeden sonra, oynatıcıyı satmadan önce veya özel bir sistemin size uygun olmadığı durumlarda bunu kullanın.[Updater CE edin](../guide_tr.html#platform)[G1 indirme](../firmware_tr.html?model=G1)[G1 kılavuz](../manuals/g1.html)

Bilgisayarınız için kurulum kılavuzu

## Orijinal Yazılımı bilgisayarınızla G1 cihazınıza geri yükleyin

Kullandığınız bilgisayara uygun kılavuzu seçin. Her sürümde platform kurulumu, Updater CE adımları ve stoğa dönüş yolu bulunur.[Windows kılavuzu](/install/original-g1-windows.html)[macOS kılavuzu](/install/original-g1-mac.html)[Linux kılavuzu](/install/original-g1-linux.html)

[Tüm Innioasis G1 kılavuzlar](/install/g1.html) · [Tüm Orijinal Yazılım kılavuzları](/install/original-software.html)

## İhtiyacınız olan şey
  - Windows, macOS veya Linux bilgisayar. Updater CE üçünde de çalışır.
  - Oynatıcıyla birlikte gelen USB veri kablosu. Yalnızca şarj kabloları çalışmayacaktır.
  - Resmi `rom_g1.zip` Güncelleyicinin sizin için indirdiği paket veya [G1 arşiv](../firmware_tr.html?model=G1) Eğer elle flaşlamayı tercih ediyorsanız.
  - Oynatıcıda şarj edin. Gücü kaybeden bir geri yükleme, kötü bir durumu daha da kötüleştirmenin tek yaygın yoludur.

Bu, sistemin yerini alır ve dahili depolamayı siler. Önce müzik, kayıt ve fotoğrafları bir bilgisayara kopyalayın.

## Rota A: Updater CE (önerilir)
  - Düzenlemek [Innioasis Güncelleyici CE](../guide_tr.html#platform) ve aç.
  - Ayarlamak Cihaz modeli ile G1. Modelin oynatıcıyla tam olarak eşleşmesi gerekir.
  - Seçmek Orijinal yazılım Yazılım listesinde.
  - Bir sürüm seçin. En yeni kararlı yapı güvenli varsayılandır.
  - Basmak Yükle / Geri yükle ve paket indirilip çıkartılırken bekleyin.
  - Oynatıcıyı tamamen kapatın, ardından USB kablosunu yalnızca Güncelleyici sorduğunda bağlayın.
  - Başarı mesajı gelene kadar oynatıcıya veya kabloya dokunmayın. Müzikçaların bağlantısını kesin ve başlatın.
Asla "çalışmasını sağlamak" için farklı bir model seçmeyin. Bir G1'ın bir G1 paketine ihtiyacı vardır. Modelleri karıştırmak, oyuncuların manuel kurtarmaya ihtiyaç duymasıyla sonuçlanır.

## Rota B: SP Flash Tool (manuel)

Bir bilgisayar Updater CE'ı çalıştıramadığında veya pakete zaten sahip olduğunuzda ve klasik aracı tercih ettiğinizde bunu kullanın.
  - İndir `rom_g1.zip` itibaren [G1 arşiv](../firmware_tr.html?model=G1) ve zip dosyasını açın.
  - Dağılım dosyasını görsellerin yanında tutun. Görüntüleri yeniden adlandırmayın veya taşımayın.
  - SP Flash Tool'ı açın, seçin Yalnızca İndirve dağılım dosyasını yükleyin.
  - Oynatıcıyı kapatın, tuşuna basın İndir, ardından kabloyu bağlayın.
  - Bağlantıyı kesmeden önce yeşil başarı işaretini bekleyin.

The [SP Flash Tool kılavuz](../sp-flash-tool_tr.html) sürücüleri ve Windows istemlerini daha ayrıntılı olarak kapsar. Linux ve macOS'ta Updater CE daha kolay yoldur çünkü kendi USB işlemesini sağlar.

## Geri yüklemeden sonra
  - Oynatıcının bağlantısını kesin ve kendi kendine başlamasına izin verin.
  - Dilinizi seçin ve saati ayarlayın.
  - Kullanıyorsanız Wi-Fi veya Bluetooth'a yeniden bağlanın.
  - Müziğinizi geri kopyalayın. [aktarım kılavuzu](../manuals/transfer-music.html) klasör adlarına sahiptir.

Oynatıcı başlatılıyor ancak ekran, tekerlek veya düğmeler hâlâ hatalı çalışıyorsa geri yükleme işe yaradı; bu bir donanım veya kurulum sorusudur, yazılım değil. [sorun giderme kılavuzu](../troubleshooting_tr.html) Bir sonraki durak _____ mı.

## Eğer işe yaramazsa

### Güncelleyici oynatıcıyı asla görmez

Kabloyu ve ardından USB bağlantı noktasını değiştirin. Hub'lardan kaçının. Windows'ta MediaTek sürücüsünü şuradan yükleyin: [sürücü sayfası](../drivers_tr.html).

### Flaş erken duruyor

Yeniden bağlayın, oynatıcıyı şarj edin ve yeniden başlayın. Farklı bir modelin paketine geçmeyiniz.

### Oyuncu siyah kalır

Bir saat şarj edin, ardından gücü on saniye basılı tutun. Hala ölüyse, okuyun [kurtarma kılavuzu](../guides/recovery_tr.html) tekrar denemeden önce.

## İnsanların sorduğu sorular

### Bu müziğimi silecek mi?

Evet, dahili depolama birimi silinir. microSD kartındaki dosyalar genellikle hayatta kalır, ancak önce bunları güvenli bir yere kopyalayın.

### Daha sonra Rockbox'a geri dönebilir miyim?

Evet. Orijinal Yazılımın Geri Yüklenmesi tek yönlü bir kapı değildir; modelinize özel yazılım sayfasını tekrar yükleyebilirsiniz.

### Type A / Type B ayarına ihtiyacım var mı?

Yalnızca Y1'in bu seçeneği vardır ve yalnızca Orijinal Yazılım için. Diğer tüm modellerde tek bir paket kullanılır.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
