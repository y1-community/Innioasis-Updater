---
title: "Innioasis Y1 ve Y2 USB sürücüler | Windows sürücüsü ve Linux izinleri - Innioasis Güncelleyici"
description: "Bilgisayarınızı Innioasis Güncelleyici için ayarlayın: Windows MediaTek sürücüsü ve Linux USB izinleri — artı kablo ve zamanlama düzeltmeleri."
language: "tr"
source: "https://innioasis.app/drivers_tr.html"
---

# Innioasis Y1 ve Y2 USB sürücüler | Windows sürücüsü ve Linux izinleri - Innioasis Güncelleyici

Bilgisayar kurulumu

# Bilgisayarı oynatıcıdan önce hazırlayın.

Bağlantı sorunlarının çoğu sürücüden, izinlerden, kablodan veya zamanlamadan kaynaklanır. Windows'un MediaTek sürücüsünün yüklü olması gerekiyor. Linux'un doğru USB izinlere ihtiyacı var. Aşağıda platformunuzu bulun.[Updater CE edin](guide_tr.html#platform)[Sorun giderme](troubleshooting_tr.html)

## Windows
  - Aşağıdaki MediaTek sürücü yükleyicisini indirin.
  - Yükleyiciyi çalıştırın ve Windows'un sürücüyü yüklemesine izin verin.
  - Bilgisayarı yeniden başlatın.
  - Updater CE'yi açın ve kapalı oynatıcıyı fişe takmadan önce bağlantı istemini bekleyin.

Bazı Windows sistemleri sürücüyü Çekirdek izolasyonu (Bellek bütünlüğü) yoluyla engeller. Güncelleyici CE, yeniden başlatmanın ardından oynatıcıyı hala göremiyorsa, Windows Güvenliği'nde Bellek bütünlüğünü kapatın, yeniden başlatın ve sürücüyü yeniden yükleyin. Sisteminiz izin veriyorsa, işiniz bittiğinde ayarı tekrar açın.

Windows uygulamayı başlatmıyor mu? Windows Güvenliği veya Akıllı Uygulama Denetimi, Güncelleyici CE'nin açılmasını durdurursa, Ayarlar (basmak Win + I) → Gizlilik ve güvenlik → Windows Security → Uygulama ve tarayıcı kontrolü → Akıllı Uygulama Kontrolü ayarları ve bunu şu şekilde ayarlayın: Kapalı. Akıllı Uygulama Denetimi şu anda Epic Overlay Service (Fortnite tarafından kullanılan) gibi popüler uygulamaları etkilemektedir — Updater CE güvenlidir ve kullanımı doğrulanmıştır. Daha sonra tekrar etkinleştirmek için `VerifiedAndReputablePolicyState` ile `1` (Açık) veya `2` (Değerlendirme Modu) altında `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` Kayıt Defteri Düzenleyicisi'nde.[Windows sürücüsünü indirin](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Ana kılavuza geri dön](guide_tr.html#windows) · [Yazılım İndirmeleri](firmware_tr.html)

## Linux USB izinleri

Linux, kullanıcı hesabınızın oynatıcının içindeki MediaTek USB çipiyle konuşmasına izin verilmesine ihtiyaç duyar. Güncelleyici CE bunu genellikle kurulum sırasında çözer ve aynı izin SP Flash Tool için de geçerlidir, dolayısıyla bunu normal bir aşama yerine bir düzeltme adımı olarak değerlendirin.
  - Updater CE'yi root olarak değil, normal kullanıcınız olarak çalıştırın. Yükleyici yalnızca ihtiyaç duyduğunda yönetici erişimi ister.
  - Oynatıcının hiç görülüp görülmediğini kontrol edin. Oynatıcıyı kapatın, kabloyu bağlayın ve bir terminalde lsusb komutunu çalıştırın. Bağlı bir oynatıcı, satıcı kimliği 0e8d olan bir MediaTek cihazı olarak görünür.
`lsusb`
  - lsusb'de görünüyor ancak Innioasis Güncelleyici CE veya SP Flash Tool iznin reddedildiğini söylüyorsa veya bağlantı noktasını açamıyorsa, kullanıcınızın USB aygıtına erişimi yoktur. Aynı udev kuralı her iki aracı da kapsar; bu nedenle kullanıcı grubunun onu okumasına olanak tanıyan bir tane ekleyin.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Bu satırı /etc/udev/rules.d/51-innioasis.rules adlı yeni bir dosyaya kaydedin ve ardından şunu çalıştırın:`sudo udevadm control --reload && sudo udevadm trigger`
  - Oynatıcının fişini tamamen çekin, tekrar takın ve yüklemeyi yeniden deneyin.
  - SP Flash Tool bir seri izin veya bağlantı noktası yarışı bildirirse, fişi tamamen çıkarın ve yalnızca istendiğinde yeniden bağlayın.
Flaş ofsetlerini doğaçlama yapmayın.Manuel kurtarma aracına geçerseniz projeyle birlikte gönderilen dosyaları ve modele özel yapılandırmayı kullanın.

[Ana kılavuza geri dön](guide_tr.html#linux) · [Yazılım İndirmeleri](firmware_tr.html) · [SP Flash Tool kılavuz](sp-flash-tool_tr.html)

## Kablo ve zamanlama
  - Bilinen bir USB veri kablosu kullanın.
  - Sorun giderme sırasında hub'lardan kaçının.
  - Doğru modeli tamamen kapatın.
  - Yalnızca istemde bağlanın.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
