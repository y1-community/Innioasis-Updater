---
title: "Innioasis Y1 Açılmıyor | Innioasis Aygıt Yazılımı Arşivi - Innioasis Aygıt Yazılımı İndirmeleri"
description: "Innioasis Y1 açılmıyor veya şarj olmuyor mu? Yeniden başlatmaya zorlayın, bilgisayarın bunu görüp görmediğini kontrol edin, ardından Y1 donanım yazılımını geri yükleyin veya manuel SP Flash Tool kurtarmayı kullanın."
language: "tr"
source: "https://innioasis.app/guides/y1-wont-turn-on_tr.html"
---

# Innioasis Y1 Açılmıyor | Innioasis Aygıt Yazılımı Arşivi - Innioasis Aygıt Yazılımı İndirmeleri

Oyuncu kurtarma · Innioasis Y1

# Innioasis Y1 açılmıyor

Siyah ekran her zaman oyuncunun öldüğü anlamına gelmez. Manuel flaşı denemeden önce bilgisayarda şarj etme, zorla yeniden başlatma ve algılama işlemlerini gerçekleştirin.[Updater CE edin](../guide_tr.html#platform)[Aygıt Yazılımı İndirmeleri](../firmware_tr.html)[Kurtarma kılavuzu](recovery_tr.html)

## Her şeyden önce Y1 cihazını uygun şekilde şarj edin

"Y1 açılmıyor" raporlarının çoğu boşalmış pil, yalnızca şarj kablosu veya yeterli akımı sağlayamayan şarj cihazıdır. Derinden boşalmış bir Y1, ekranda herhangi bir şey görünmeden önce 20 ila 30 dakika kadar güç alabilir, bu yüzden ona ölü demeden önce biraz zaman tanıyın.
  - Bilinen bir USB kullanın veri kablo, yalnızca şarj kablosu değil.
  - Duvar şarj cihazını, ardından hub yerine doğrudan bilgisayar USB bağlantı noktasını deneyin.
  - 30 ila 60 dakika kadar bağlı bırakın ve şarj simgesinin veya arka ışığın görünüp görünmediğini izleyin.
  - Devam etmeden önce ikinci bir kabloyu ve şarj cihazını deneyin.

## Yeniden başlatmayı zorla

Güç düğmesini yaklaşık 15 saniye basılı tutun, bırakın, beş saniye bekleyin ve ardından güce bir kez basın. Bu, askıdaki önyüklemeyi temizler ve tekrarlanması güvenlidir.

Ekranda logo görüntüleniyor ve ardından kararıyorsa oynatıcı başlatılıyor ve hata veriyor demektir; aşağıdaki ürün yazılımı geri yükleme adımına geçin. Hiçbir şey olmazsa şarjda tutun ve yarım saat sonra tekrar deneyin.

## Bir bilgisayarın oynatıcıyı görüp göremediğini kontrol edin

Kapalı olan Y1 cihazını bir veri kablosuyla bağlayın ve Windows'ta Aygıt Yöneticisi'ni açın, `lsusb` Linux'ta veya macOS'ta MTKClient. Çalışan bir oynatıcı, satıcı kimliğine sahip bir MediaTek cihaz olarak görünüyor `0e8d`. Görünürse donanım, ekran karanlık kalsa bile yeniden yanıp sönecek kadar canlı demektir.

Hiçbir şey görünmezse, önce Windows'a MediaTek sürücüsünü yükleyin; [sürücü rehberi](../drivers_tr.html) Windows ve Linux izinlerini kapsar.

## Y1 stok donanım yazılımını geri yükleyin

Oynatıcı algılanır ancak önyükleme yapmazsa Y1 Orijinal Yazılımı yeniden yükleyin. Yalnızca Y1 paketini kullanın; Y2 yapısı Y1 donanımında başlamayacaktır.
  - Açık [Güncelleyici CE](../guide_tr.html#platform) Bilgisayarınızda.
  - Ayarlamak Cihaz modeli ile Y1.
  - Seçmek Orijinal yazılım içinde Yazılım ve kararlı bir Y1 sürümü seçin; manuel paket `rom.zip`.
  - Tıklamak Yükle / Geri yükle ve paketin çıkmasına izin verin.
  - Y1'ı tamamen kapatın, USB veri kablosunu yalnızca Güncelleyici istediğinde bağlayın ve başarı mesajına kadar bırakın.
Gücü sabit tutun. Gücünü kaybeden bir flaş, oynatıcıyı kullanılamaz hale getirebilir. Önce şarj edin ve doğrudan bilgisayara bağlayın.

## Güncelleyici oynatıcıyı göremediğinde manuel kurtarma

Updater CE, yönlendirmeli kurulumun tamamlanamadığı durumlar için manuel kurtarma araçları içerir. [SP Flash Tool](../sp-flash-tool_tr.html) Windows ve Linux x86'da paketlenmiştir ve MTKClient rotası macOS'u kapsar. Her ikisinin de model uyumlu bir ürün yazılımı paketine ihtiyacı var [Aygıt Yazılımı İndirmeleri](../firmware_tr.html) sayfa.

Dağılım dosyalarını veya ofsetleri doğaçlama yapmak yerine platformunuza uygun araç kılavuzunu takip edin. Oynatıcı herhangi bir araç tarafından algılanmazsa arıza muhtemelen pil, şarj portu veya karttadır.

## Eğer hala başlamıyorsa

Yanıp sönmeyi bırakın ve donanım olarak değerlendirin. Kutuyu açmayın veya pile basmayın. Topluluğa modeli, ekranın ne yaptığını, bilgisayarın onu algılayıp algılamadığını ve hangi paketleri denediğinizi sorun. [Discord topluluk](https://discord.gg/zHrT2zrcek) bir servis yolunun belirlenmesine yardımcı olabilir.

Stok geri yüklemesi sistemin yerini alır; bu nedenle, flash'ı yüklemeden önce oynatıcının dahili belleğinde saklanan her şeyi yedekleyin. MicroSD kartındaki müziğe geri yükleme işlemi etkilenmez.

## Innioasis Y1 güç SSS

### Neden Innioasis Y1 cihazım açılmıyor?

Genel nedenler; tamamen boşalmış bir pil, yalnızca şarj kablosu veya zayıf şarj cihazı, önyüklemeyi durduran bir ürün yazılımı çökmesi veya bir donanım arızasıdır. Müzikçaların öldüğünü varsaymadan önce bilinen bir veri kablosuyla 30 dakika boyunca şarj edin.

### Bir Innioasis Y1'ı nasıl yeniden başlatmaya zorlarım?

Güç düğmesini yaklaşık 15 saniye basılı tutun, bırakın, beş saniye bekleyin ve ardından güce bir kez basın. Hiçbir şey görünmezse şarjda bırakın ve 30 dakika sonra tekrar deneyin.

### Açılmayan bir Y1 cihazını kurtarabilir miyim?

Çoğu zaman evet. Bilgisayar hala MediaTek aygıtını algılıyorsa, Y1 Orijinal Yazılım paketini Updater CE ile yeniden yükleyin. Algılanmazsa Güncelleyici CE'de bulunan SP Flash Tool veya MTKClient kurtarmayı ve model uyumlu bir Y1 ürün yazılımı dosyasını kullanın.

### Y1'ın yanıp sönmeden önce şarj edilmesi gerekiyor mu?

Evet. Gücünü kaybeden bir flaş, oynatıcıyı kullanılamaz hale getirebilir. Önce şarj edin ve hub yerine doğrudan bilgisayara bağlayın.

## İlgili düzeltmeler
  - [Y2 açılmıyor](y2-wont-turn-on_tr.html) — Y2 için aynı kontroller
  - [Y1 kaydırma tekerleği çalışmıyor](y1-scroll-wheel-not-working_tr.html) — önyükleme yapıyor ancak tekerlek çalışmıyorsa
  - [Innioasis kurtarma kılavuzu](recovery_tr.html) — tüm semptom kılavuzları tek bir yerde
  - [SP Flash Tool kılavuz](../sp-flash-tool_tr.html) — Windows ve Linux'ta manuel yanıp sönme
  - [Bir yüklemede sorun giderme](../troubleshooting_tr.html) — başarısız bir flaş neye benziyor

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
