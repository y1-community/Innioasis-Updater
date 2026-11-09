---
title: "MTKclient Arızasından Sonra Önyükleme Yapamayan MediaTek Oyuncu Nasıl Kurtarılır · Innioasis Topluluk"
description: "Linux veya macOS&#39;ta MTKclient kesintiye uğrayan flaşlardan sonra önyükleme yapmayan Innioasis Y1, Y2, G1, Timmkoo ve MediaTek oynatıcıların engellemesini kaldırmak ve kurtarmak için adım adım kılavuz."
language: "tr"
source: "https://innioasis.app/recover-non-booting-device_tr.html"
---

# MTKclient Arızasından Sonra Önyükleme Yapamayan MediaTek Oyuncu Nasıl Kurtarılır · Innioasis Topluluk

Sorun Giderme ve Cihaz Kurtarma

# MTKclient Flashlamasından Sonra Önyüklemeyen Bir Aygıtın Kurtarılması

Innioasis Y1, Y2 veya MediaTek cihazınız açılmıyorsa veya macOS veya Linux'ta MTKclient ile yanıp söndükten sonra siyah ekran gösteriyorsa paniğe kapılmayın. Donanım BootROM'u (BROM) kalıcıdır ve yok edilemez.

## MTKclient Neden Durabilir veya Siyah Ekran Bırakabilir?

MTKclient, DA kimlik doğrulamasını ve libusb aracılığıyla ham USB iletişimi atlamak için yazılımdan yararlanma yüklerine (kamakiri / amonet) güvenir. MacOS ve Linux ARM64 sistemlerinde:
  - MacOS'ta USB el sıkışma gecikmesi veya bağlantı noktası zaman aşımları, aktarım sırasında DA verisi enjeksiyonunu durdurabilir.
  - Eksik veya tamamlanmamış bölüm başlıkları, önyükleyiciyi (önyükleyici / lk) yanıt vermeyen bir durumda bırakır.
  - Oynatıcı tamamen ölü görünüyor; LED yok, şarj simgesi yok, ekran arka ışığı yok.

Bu durumda bile, MediaTek yonga seti tekrar BROM Modu (USB VID 0e8d, PID 0003), resmi düşük seviyeli kurtarma için hazır.

## Kesin Kurtarma Yöntemi: Güncelleyici CE'deki SP Flash Tool Motor

Tuğlalanmış oynatıcınızı kurtarmanın en güvenli, en güvenilir yolu kullanmaktır. Güncelleyici CE yetkili ile yapılandırılmış SP Flash Tool arka uç.

### Güncelleyici CE'deki Tam Adımlar:
  - Açık Güncelleyici CE.
  - Tıklamak Ayarlar sol gezinme kenar çubuğunda.
  - Gelişmiş bölümüne ilerleyin ve etkinleştirin Gelişmiş Ayarları Göster.
  - Altında Kurulum Yöntemi (veya MediaTek yükleyici için Yanıp Sönen Motor), yerini bulun Flaş Yöntemi yıkılmak.
  - Seçimi şu şekilde değiştir: Otomatik (önerilen) veya MTKClient ile SP Flash Tool.
  - İstemi onaylayın ve ana yükleme akışına dönün.

## SP Flash Tool İçin Platform Mimarisi ve İşletim Sistemi Gereksinimleri

MediaTek'ın yetkilisi `SP Flash Tool` ikili dosya yerel olarak derlenir Linux için x86_64 ELF ikili dosyası ve bir Windows x64 için PE32+ yürütülebilir dosyası.macOS ve ARM64 Linux Kullanıcıları için Önemli Donanım Notu:
 MediaTek, SP Flash Tool'i macOS (Darwin) veya Linux ARM64 (aarch64) için derlemediğinden, tuğla sorunu yaşayan macOS kullanıcıları ve ARM64 Linux kullanıcılarının (Asahi Linux çalıştıran Raspberry Pi veya Apple Silicon gibi) oynatıcılarını aşağıdakilere bağlaması gerekir: 
  - Bir x64 Windows PC (Windows 10/11 64 bit) veya
  - Bir x86_64 Linux bilgisayarı (Ubuntu, Debian, Fedora, Arch 64 bit).

## Adım Adım Donanım Engelleme İşlemi
  - Oynatıcının bağlantısını kesin: USB kablosunu oynatıcıdan ve bilgisayardan tamamen çıkarın.
  - Sert Güç Kapatma: Yonga setinin tamamen kapatıldığından ve düşük güç USB döngüsünde sıkışıp kalmadığından emin olmak için Güç düğmesini (veya Güç + Sesi Kısma) 15 saniye basılı tutun.
  - Güncelleyici CE'yi SP Flash Tool Moduyla başlatın: Cihazınızın modelini seçin (ör. Innioasis Y1 veya Innioasis Y2) ve seçin Orijinal yazılım stok bölümlerini geri yüklemek için.
  - Kurulumu / Geri Yüklemeyi başlatın: Tıklamak Yükle / Geri yükle Güncelleyici CE'de. Durum istemi şunu söyleyene kadar bekleyin Oyuncu bekleniyor...
  - BROM'u Tetiklemek için USB Kabloyu Takın: Cihaz KAPALI iken, USB kablosunu doğrudan yüksek hızlı anakart USB bağlantı noktasına takın (güçsüz USB hub'lardan kaçının).
  - Sistem MediaTek VCOM bağlantı noktasını algılayacak, İndirme Aracısını (DA) gönderecek, bölüm tablolarını yeniden yazacak ve tüm ürün yazılımı görüntülerini temiz bir şekilde geri yükleyecektir.

## Modele ve İşletim Sistemine Göre Permütasyonlar

| Modeli | Başarısız Platform | Önerilen Kurtarma Kurulumu | Motor ve Mod |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silikon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Hisse senedi ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 veya Windows x64 PC | SP Flash Tool + Topluluk DA'sı |
| Innioasis Y2 | macOS (MTKclient durdu) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Dağılım Kurtarma |
| Innioasis G1 / G3 / G5 | macOS / Linux MTK istemcisi | VCOM Sürücülerine sahip Windows x64 PC | SP Flash Tool + Fabrika Aygıt Yazılımı |
| Mechen H1 / Timmkoo A5 | Herhangi bir platform | Windows x64 veya Linux x86_64 PC | SP Flash Tool + Dağılım dosyası |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
