---
title: "Windows 10/11 uygulama başlatma sorunları ve Akıllı Uygulama Denetimi geçici çözümü - Innioasis Güncelleyici"
description: "Windows 10/11 veya Akıllı Uygulama Kontrolü uygulamayı başlatmanızı engelliyorsa buradaki geçici çözümü uygulayın."
language: "tr"
source: "https://innioasis.app/notices/2026-11-07-codesigning_tr.html"
---

# Windows 10/11 uygulama başlatma sorunları ve Akıllı Uygulama Denetimi geçici çözümü - Innioasis Güncelleyici

2026-10-25'ten 31-2026'ya kadar · Modeller: Y1,Y2

# Windows 10/11 uygulama başlatma sorunları ve Akıllı Uygulama Denetimi geçici çözümü

Windows 10/11 veya Akıllı Uygulama Kontrolü uygulamayı başlatmanızı engelliyorsa buradaki geçici çözümü uygulayın.

2026-10-25'ten 31-2026'ya kadar · Modeller: Y1,Y2

Yanlış pozitif raporlar Microsoft'a gönderildi `installer.exe` Ve `InnioasisUpdater.exe` ve işlem yapıldı ancak Windows Uç Nokta Koruması veya Akıllı Uygulama Denetimi hala bilgisayarınızdaki uygulamayı engelliyorsa şu geçici çözümü kullanın:

### Geçici Çözüm: Akıllı Uygulama Denetimini Kapatın
  - Windows'u aç Ayarlar (basmak `Win + I`).
  - Git Gizlilik ve güvenlik > Windows Güvenliği > Uygulama ve tarayıcı kontrolü.
  - Altında Akıllı Uygulama Kontrolü, tıklamak Akıllı Uygulama Kontrolü ayarları.
  - Akıllı Uygulama Kontrolünü şu şekilde ayarlayın: Kapalı. Bu, uygulamanın hemen açılıp çalıştırılmasına olanak tanır.

Windows veya Edge, Güncelleyici CE'yi indirmenizi engelliyorsa daha fazla seçeneğe tıklayın (…) Daha sonra Kale > Daha fazlasını göster > Yine de kal.

### Akıllı Uygulama Denetimini Yeniden Etkinleştirme

Yanlış pozitif tanımların bilgisayarınızda güncellenmesi bittiğinde, Akıllı Uygulama Denetimini Windows Kayıt Defteri aracılığıyla yeniden etkinleştirebilirsiniz:
  - Basmak Windows Tuşu + R, tip `regedit`Kayıt Defteri Düzenleyicisi'ni yönetici olarak açmak için Enter tuşuna basın.
  - Şuraya gidin: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (veya `Policies`).
  - Bul `VerifiedAndReputablePolicyState` sağdaki bölmede.
  - Çift tıklama `VerifiedAndReputablePolicyState` ve Değer verilerini şu şekilde değiştirin:

  - `1` = Açık (Zorunlu)
  - `2` = Değerlendirme Modu

  - Tamam'ı tıklayın, Kayıt Defteri Düzenleyicisi'ni kapatın ve bilgisayarınızı yeniden başlatın.

[Microsoft'a gönderilen installer.exe raporuna bakın](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Microsoft'a gönderilen InnioasisUpdater.exe raporuna bakın](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Bağlantılı sayfayı aç](https://innioasis.app/notices.html)

[← Tüm bildirimler](index_tr.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
