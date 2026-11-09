---
title: "Innioasis Y1 veya Y2 - Innioasis Güncelleyicinize Rockbox nasıl yüklenir"
description: "Güncelleyici ile Innioasis Y1 veya Y2 cihazına Rockbox yükleyin: temalar, kararlı sürümler, Type A ve Type B notları ve sonrasında Orijinal Yazılımın nasıl geri yükleneceği."
language: "tr"
source: "https://innioasis.app/rockbox_tr.html"
---

# Innioasis Y1 veya Y2 - Innioasis Güncelleyicinize Rockbox nasıl yüklenir

Rockbox referans

# Y1 veya Y2 cihazınızda Rockbox alınıyor

Rockbox oynatıcı yazılımını değiştirir ve daha derin bir müzik oynatıcı arayüzü, oynatma kontrolleri, sıralama ve tema seçenekleri açar. Kurulum yönlendirilir, ancak Y1 ve Y2 ayrı yolculuklardır.[Rockbox üzerinde Y1](guides/rockbox-y1.html)[Rockbox üzerinde Y2](guides/rockbox-y2.html)[Neden Rockbox?](rockbox-benefits_tr.html)

## Yükleme neleri değiştirir?

Rockbox özel bir yazılımdır. Eşleşen Orijinal Yazılım paketi mevcut olduğunda stok arayüzüne dönme yeteneğinizi ortadan kaldırmaz. Müzik taramayı ve kişiselleştirmeyi iyileştirebilir ancak özellikler, çözünürlük, pil ömrü ve tema uyumluluğu yapıya bağlıdır.Modelleri karıştırmayın. Y1 oynatıcı için Y1'ı ve Y2 oynatıcı için Y2'yi seçin. Benzer görünen sürüm adı, bir paketin uyumlu olduğuna dair yeterli kanıt değildir.

## Videoyu izle

Frawgeeys'in videosu. Innioasis Güncelleyici rotasını gösterir; Y1 veya Y2 cihazınız için aşağıdaki modele özel yazılı adımları kullanın.

Videoyu yazan: [Cristian Meydanı](https://www.youtube.com/@CristianPlaza) (İspanyolca), Y1 üzerinde Rockbox gösteriliyor. Oynatıcınız için aşağıdaki modele özel adımları kullanın.

## Paylaşılan Güncelleyici rotası
  - Güncelleyiciyi yükleyin ve sorulana kadar hiçbir şeyi bağlamayın.
  - Oynatıcının üzerinde yazılı olan modeli seçin. Cihaz modeli.
  - Seçmek Rockbox içinde Yazılım.
  - Gecelik bir yapıyı kasıtlı olarak test etmediğiniz sürece kararlı bir sürüm seçin.
  - Tıklamak Yükle / Geri yükle, ardından kapatma ve USB bağlantı istemini izleyin.
  - Yalnızca başarı mesajından sonra bağlantıyı kesin.

## 240p, 360p ve temalar

Daha eski Rockbox tema koleksiyonları 240p için oluşturulabilir. Y1 topluluk yapıları da 360p uyumluluk etiketleri kullanır. Bir yapı seçmeden önce sürüm notlarını ve tema kaynağını okuyun. Bir çözünürlük veya yazılım ailesi için oluşturulan tema, diğerinde çalışmayabilir.[Topluluk temalarına göz atın](https://themes.innioasis.app/?lang=tr)[Tema araçları](https://themes.innioasis.app/?lang=tr)

## Orijinal Yazılıma Dönüş

Aynı modeli tekrar seçin, Orijinal yazılım, kararlı bir sürüm seçin ve kullanın Yükle / Geri yükle. Hata USB isteminden önce meydana geldiyse bilgisayarı ve çıkartılan dosyaları kontrol edin. Oynatıcı algılandıysa ancak flaş başarısız olduysa şununla başlayın: [sorun giderme](troubleshooting_tr.html).[Y1 geri yükleme](guides/restore-original-y1.html)[Y2 geri yükleme](guides/restore-original-y2.html)

## SSSRockbox'ı yeniden yükledim ve hiçbir şeyi düzeltmedi.

Rockbox'ı yeniden yüklemek aynı yapıyı aynı dosyalar üzerine yazar, dolayısıyla Rockbox'in MicroSD üzerinde sakladığı şeyleri sıfırlayamaz. Sorun, kartta bulunan bozuk bir ayar, tema, çalma listesi veya veri tabanından kaynaklanıyorsa, yeniden yüklemek sorunu gidermez. Güvenilir sıfırlama, `.rockbox` MicroSD içindeki klasör — Rockbox bir sonraki önyüklemede yeni bir tane oluşturur.
  - Oynatıcıyı tamamen kapatın ve MicroSD kartını çıkarın veya oynatıcıyı USB sürücüsü olarak bağlayın.
  - Klasörün görünür olması için bilgisayarınızdaki gizli dosyaları gösterin. Gizli dosyalar nasıl gösterilir?Bilgisayarınızda nokta dosyalarını gösterinWindows: Dosya Gezgini'nde açın Görüş sekme ve onay işareti Gizli öğeler.macOS: Finder tuşuna basın Cmd+Shift+. gizli dosyaları değiştirmek için.Linux · GNOME Dosyaları: basmak Ctrl+Hveya menüyü açın ve Gizli Dosyaları Göster.Linux · KDE Dolphin: basmak Ctrl+Hveya kullanın Görünüm → Gizli Dosyaları Göster.
  - Sil `.rockbox` kartın kökündeki klasör.
  - Kartı tekrar takın ve oynatıcıyı başlatın. Rockbox klasörü varsayılanlarla yeniden oluşturur.
  - Temanızı ve ayarlarınızı yeniden uygulayın. Sorun yalnızca belirli bir temadan sonra tekrar ortaya çıkıyorsa, sorunun nedeni o temadır.

Silme `.rockbox` Rockbox dosyasını kaldırmaz ve müziğinize dokunmaz; klasör; ayarları, temaları ve önbellekleri barındırır ve otomatik olarak yeniden oluşturulur. Temalarınızı korumak istiyorsanız klasörü kopyalayın. `.rockbox` silmeden önce veya klasörü yeniden adlandırın `.rockbox-old` Birinci.Neden MicroSD cihazımda .rockbox klasörünü göremiyorum?

Adı noktayla başlayan klasörler çoğu bilgisayarda varsayılan olarak gizlenir. Rockbox yüklemek için onu görmenize gerek yok — Güncelleyici dosyaları yönetir. Sorun gidermeye çalışıyorsanız ve silmek istiyorsanız önce gizli dosyaları açın. Gizli dosyalar nasıl gösterilir?Bilgisayarınızda nokta dosyalarını gösterinWindows: Dosya Gezgini'nde açın Görüş sekme ve onay işareti Gizli öğeler.macOS: Finder tuşuna basın Cmd+Shift+. gizli dosyaları değiştirmek için.Linux · GNOME Dosyaları: basmak Ctrl+Hveya menüyü açın ve Gizli Dosyaları Göster.Linux · KDE Dolphin: basmak Ctrl+Hveya kullanın Görünüm → Gizli Dosyaları Göster..rockbox'ı silmek temamı ve ayarlarımı sıfırlar mı?

Evet - `.rockbox` Rockbox'ın ayarlarını, temasını, çalma listelerini ve önbelleğe alınmış veritabanını içerir. Bunu silmek, Rockbox'i temiz bir varsayılan duruma döndürür. Tüm klasörü yedekleyin (veya yeniden adlandırın) `.rockbox-old`) herhangi birini geri istiyorsanız oynatıcıyı başlatın ve Rockbox yeni bir klasör oluşturur.

## Daha fazla Rockbox-Y1 ve Rockbox-Y2 kılavuz

Her iki modelde Rockbox yükleme, indirme, tema oluşturma, geri yükleme ve sorun gidermeye yönelik adım adım kılavuzları keşfedin:[Rockbox-Y1 merkezi](rockbox-y1/)[Rockbox-Y2 merkezi](rockbox-y2/)[Rockbox ROM indirme](rockbox-rom-download_tr.html)[Y1 için Rockbox](rockbox-for-y1_tr.html)[Y2 için Rockbox](rockbox-for-y2_tr.html)[Rockbox-Y1 ve Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 temalar](rockbox-y1-themes.html)[Rockbox-Y2 temalar](rockbox-y2-themes.html)

## Bu referans faydalı oldu mu?

Cevabınız bu kılavuzun geliştirilmesine yardımcı olacaktır.EvetHenüz değil[Nasıl geliştirebileceğimizi bize bildirin](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
