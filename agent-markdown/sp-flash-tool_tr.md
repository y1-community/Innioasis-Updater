---
title: "Innioasis ve Timmkoo Oyuncular için SP Flash Tool"
description: "Windows ve Linux&#39;ta Innioasis Güncelleyici ile birlikte verilen SP Flash Tool&#39;ı bulun, rom.zip veya rom_y2.zip&#39;ü çıkarın ve eşleşen dağılım dosyasıyla birlikte bir Innioasis Y1 veya Y2&#39;i flaşlayın."
language: "tr"
source: "https://innioasis.app/sp-flash-tool_tr.html"
---

# Innioasis ve Timmkoo Oyuncular için SP Flash Tool

Manuel yanıp sönme

# Innioasis ve Timmkoo Oyuncular için Flash Aracı

SP Flash Tool, Innioasis Güncelleyicinin içine gelir [Windows](drivers_tr.html#windows) Ve [Linux](drivers_tr.html#linux). Zaten ona sahipsin. Bu kılavuz, onu Innioasis Y1 veya Y2 üzerinde kullanmanın güvenli yolunu ve Timmkoo oyuncular için Güncelleyici rotasını gösterir.[Güncelleyici kılavuzuna dön](guide_tr.html)[Aygıt Yazılımı İndirmeleri](firmware_tr.html)[Sorun giderme](troubleshooting_tr.html)

Innioasis Updater ile başlayın

## Güncelleyici tüm işi tek geçişte yapar

Güncelleyici çoğu yüklemeyi tek geçişte gerçekleştirir. Yazılımı seçin, adımları izleyin ve işiniz bitti. Ayrıca bir düzeltmenin veya yeni bir sürümün ne zaman yayınlanacağını da size bildirir. SP Flash Tool, Güncelleyicinin tamamlayamadığı nadir durumlar için Güncelleyicinin Araç Takımının içindedir. Aşağıdaki adımlar istisnadır.

## Bu araç ne işe yarar?

Güncelleyici oynatıcıyı sizin için yanıp söner. SP Flash Tool, koruma rayları olmayan aynı motordur. Güncelleyici başlamadığında, oynatıcı bağlanmadığında veya bir dağılım dosyasında yolunuzu bildiğinizde bunu kullanın.Önce Güncelleyiciyi deneyin. Çoğu yükleme ve çoğu kurtarma için kılavuzlu [Güncelleyici rotası](guide_tr.html) daha güvenli bir seçimdir. Neden ihtiyacınız olduğunu bildiğinizde SP Flash Tool kullanın ve şarj edilmiş bir pil ile bir USB veri kablosunu hazır bulundurun.

## Innioasis oyuncu için Flash aracı

Innioasis Güncelleyici, Innioasis oyuncuya yönelik flash araçtır. Model uyumlu akış aracılığıyla resmi yazılımı yükler, paketleri günceller ve geri yükler ve müziğinizi ve ayarlarınızı korur.

### Innioasis Y1 flaş aracı

Güncelleyici'de Y1 sürümünü seçin, ardından uygulama sorduğunda kapalı oynatıcıyı bağlayın. Aynı Y1 paketleri, manuel yönlendirmeye ihtiyaç duyduğunuzda SP Flash Tool ile çalışır.

### Innioasis Y2 flaş aracı

Y2 için listelenen bir sürümü seçin. Y2 paketleri, Y1 paketleriyle değiştirilemez, bu nedenle başlamadan önce modeli kontrol edin.

## Timmkoo oyuncu için Flash aracı

Timmkoo oyuncu aynı Güncelleyici yükleme akışını kullanıyor. Timmkoo'in ZIP ve RAR paketlerini doğrudan okur, dolayısıyla ayrı bir flash aracına veya dağılım dosyasına ihtiyacınız yoktur.

### Timmkoo Q5 flaş aracı

Güncelleyici'de Q5 modelini seçin, Timmkoo paketini seçin, ardından Yükle / Geri Yükle'yi çalıştırın ve komut isteminde oynatıcıyı bağlayın.

### Timmkoo Q3 ve Q3E flash aracı

Q3 girişi, Q3 ve Q3E'yi benzer şekilde kapsar. Güncelleyici, eşleşen dosyaları projenin yayınladığı paketten seçer.

### Timmkoo A5 flaş aracı

Bir paket seçmeden önce A5 modelini seçin, ardından aynı kurulum istemini takip edin.

## Güncelleyicinin onu koyduğu yer

SP Flash Tool, ayrı bir indirme olarak değil, Güncelleyici yükleme klasörüyle birlikte gelir. İhtiyacınız olduğunda oradan açın.

### Windows

Güncelleyici yükleme klasörünü açın ve çalıştırın `flash_tool.exe`. Klasör genellikle altındadır `%LOCALAPPDATA%\Innioasis Updater`. Bazı kurulumlarda SP Flash Tool kısayoluna sahip bir Araç Seti klasörü bulunur.

### Linux

Paketlenmiş olanı çalıştır `flash_tool` x86 / x86_64'teki Güncelleyici uygulama klasöründeki ikili dosya. Proje yükleyicisi USB izinlerini udev kurallarıyla hazırlar, böylece oynatıcı bağlandığında görünmelidir.

### macOS

SP Flash Tool macOS'ta paketlenmemiştir. Güncelleyici bunun yerine MTKClient rotasını kullanıyor. Şunu kullanın: [rehberli kurulum](guide_tr.html) Mac'te ve Windows veya Linux makinesinde SP Flash Tool'ı saklayın.

Araç, MediaTek indirme aracısı ve modele özgü yapılandırmayla birlikte gelir, dolayısıyla DA veya dosyaları başka yerden toplamanıza gerek kalmaz.

## Ürün yazılımını hazırlayın
  - İstediğiniz yayını alın [Aygıt Yazılımı İndirmeleri](firmware_tr.html). Seçmek `rom.zip` Y1 için veya `rom_y2.zip` Y2 için.
  - ZIP'i kendi klasörüne çıkartın. Windows Tümünü Ayıkla'yı kullanabilir. Linux'ta arşiv yöneticinizi kullanın veya `unzip` bir terminalde.
  - Dağılım dosyasının çıkartılan klasörde olup olmadığını kontrol edin. Genellikle adı verilir `MT6572_Android_scatter.txt` Y1 paketleri için ve `MT6582_Android_scatter_def.txt` Y2 paketleri için, ancak bir sürüm ona projesinin adını verebilir.
Modelleri ayrı tutun. Y1 dağılımı bir MT6572 cihazını tanımlar ve Y2 dağılımı bir MT6582 cihazını tanımlar. Yanlış olanla yanıp sönmek, oyuncuların nasıl tuğlalandığıdır. ZIP içindeki dağılım modelinizle eşleşmiyorsa durun ve onun yerine modeliniz için listelenen bir paketi kullanın.

## Scatter'ı yükleyin ve flaşlayın
  - Güncelleyici yükleme klasöründen SP Flash Tool dosyasını açın.
  - İndirme sekmesinde, Seçmek Dağılım Yükleme Dosyası'nın yanındaki simgesini seçin ve çıkarılan klasörden dağılım dosyasını seçin. Bölüm listesi doldurulacaktır.
  - Flaş modunu açık bırakın Yalnızca İndir kasıtlı olarak tam bir iyileşme yapmadığınız sürece, ki bu da Aygıt Yazılımı Yükseltmesi.
  - Tıklamak İndir. Araç oynatıcıyı bekleyecektir.
  - Oynatıcıyı tamamen kapatın, ardından USB veri kablosunu bağlayın. Oynatıcıyı yere bırakın ve hareket ettirmeyin.
  - Yeşil onay işaretini bekleyin. Ancak bundan sonra kabloyu çıkarın ve oynatıcıyı başlatın.

Kılavuzlu rotayla aynı USB kablo ve zamanlama kurallarını koruyun: bir veri kablosu, hub yok ve yalnızca araç hazır olduğunda bağlanın.

## Eğer yanıp sönmüyorsa
  - Dağılımın ve ZIP'in oynatıcının üzerinde yazılı olan modelle eşleştiğini kontrol edin.
  - Bağlamadan önce oynatıcının tamamen kapalı olduğundan emin olun.
  - Windows'ta Güncelleyici kurulumuyla yüklenen MediaTek sürücüsünü doğrulayın; Linux'ta proje yükleyicisinden udev kurallarını onaylayın.
  - Kabloyu yalnızca alet beklerken yeniden bağlayın. Bir liman yarışının tamamen fişten çekilmesi ve yeni bir deneyime ihtiyacı olabilir İndir tıklamak.

Bunun ötesinde herhangi bir şey için açık [sorun giderme](troubleshooting_tr.html). Ve unutmayın: Güncelleyici hala normal yoldur ve [Y1](guides/restore-original-y1.html) Ve [Y2](guides/restore-original-y2.html) geri yükleme kılavuzları da bunu kullanır.

## Bu yararlı mıydı?

Cevabınız bu kılavuzun geliştirilmesine yardımcı olacaktır.Evet faydalı buldumHenüz değil[Nasıl geliştirebileceğimizi bize bildirin](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
