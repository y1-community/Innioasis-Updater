---
title: "Geliştiriciler | Innioasis Updater CE'ye özel donanım yazılımı ekleyin - Innioasis Aygıt Yazılımı İndirmeleri"
description: "Güncelleyici CE&#39;ye özel bir Innioasis Y1 veya Y2 donanım yazılımı eklemek için geliştirici belgeleri: depoyu çatallayın, rom.zip varlıkları yayınlayın, slidia_manifest.xml&#39;yi düzenleyin, test edin ve bir çekme isteği açın."
language: "tr"
source: "https://innioasis.app/developers_tr.html"
---

# Geliştiriciler | Innioasis Updater CE'ye özel donanım yazılımı ekleyin - Innioasis Aygıt Yazılımı İndirmeleri

Ürün yazılımı geliştiricileri için

# Firmware'inizi Updater CE'ye ekleyin.

Updater CE, özel ürün yazılımı için topluluk kataloğu ve yükleyicidir. Projenizi bir temelden ROM geliştirin, doğru sürüm varlıklarıyla birlikte genel bir depo olarak yayınlayın, model girişlerini şuraya ekleyin: `slidia_manifest.xml`, model filtrelerini test edin ve bir çekme isteği açın. Bir depo desteklediği her modele hizmet verebilir.[Güncelleyici CE kaynağını görüntüleyin](https://github.com/y1-community/Innioasis-Updater)[Yazılım İndirmelerine Göz Atın](firmware_tr.html)

## Bir tabandan başlayın ROM

Temel ROM'lar, özel ürün yazılımı geliştiricilerine, kablosuz radyo çiplerinin etkin olduğu temiz bir Android temeli sağlar. Y1'da fabrika Bluetooth ve FM'in yanı sıra Wi-Fi ve GPS'i de etkinleştiriyorlar; Y2'de fabrika Bluetooth'unun yanı sıra Wi-Fi, GPS ve FM'i etkinleştiriyorlar.Her birinin etkinleştirdiği Android sürümü ve kablosuz özellikleriyle, özel donanım yazılımı geliştirme için temel ROM indirmeler[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| İndir | Cihaz | Android | Kablosuz özellikler |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Fabrika Bluetooth ve FM'e Wi-Fi ve GPS ekler (FM zaten fabrikadan Y1 üzerinde çalışmaktadır). OS 2.0.0 veya sonraki sürümlerle birlikte gelen Y1 oynatıcılar için. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Fabrika Bluetooth ve FM'e Wi-Fi ve GPS ekler (FM zaten fabrikadan Y1 üzerinde çalışmaktadır). 2.0.0'dan önceki bir işletim sistemiyle birlikte gönderilen Y1 oynatıcılar için. |
| rom_y2.zip | Y2 | Android 4.4.2 | Fabrika Bluetooth'una Wi-Fi, GPS ve FM ekler. Y2 radyo çipi tamamen etkin olduğundan FM burada da mevcuttur. |

Bu görüntüler, cihazın kablosuz radyolarının etkin olduğu stok Android tabanıdır (AOSP), böylece özel bir ürün yazılımı, radyo yığınını değiştirmek yerine ağ özellikleri ekleyebilir. Bunlar aşağıdaki yayınlama adımları için pratik başlangıç ​​noktalarıdır.

## Bu sürüm varlık adlarını kullanın

Dosya adı uyumluluk sinyalinin bir parçasıdır. Adları tam olarak koruyun ve ZIP dosyalarını yalnızca veri havuzu kaynak ağacına değil, projenin sürüm varlıklarına da yerleştirin.Firmware ZIP varlık adları ve desteklenen cihazlar``````

| Varlık | Cihaz | Donanım | Anlam |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | OS 2.0.0 veya sonraki sürümlerle birlikte gönderilen Y1 cihazlar. |
| rom_type_b.zip | Y1 | Type B | 2.0.0'dan önceki bir işletim sistemiyle birlikte gönderilen Y1 aygıt. |
| rom_y2.zip | Y2 | Y2 | Y2 tam kurulum paketi. Bunu Y1 varlıklardan ayrı tutun. |
Bir paketi başka bir modele uyacak şekilde yeniden adlandırmayın. Y1 ve Y2, farklı MediaTek platform dosyalarını ve flash yapılandırmasını kullanır. Paketi gerçekte desteklediği donanıma göre yayınlayın.

## Bağlantı nasıl çalışır?

Güncelleyici CE manifestoyu katalog olarak okur. Her biri `<package>` satırı ona proje adını, depoyu, modeli ve işleyiciyi söyler. Bir kullanıcı bu projeyi seçtiğinde Güncelleyici, veri havuzunun yayınlanan sürümlerini kontrol eder ve bir `rom*.zip` varlık.

### manifest

Projeyi adlandırır ve onu bir modelle eşler. Y1 ve Y2, bir depoyu paylaşsalar bile ayrı satırlara ihtiyaç duyarlar.

### Yayınlanan sürüm

Yüklenebilir ZIP varlıklarını içerir. Tek bir sürüm, Y1 Type A, Y1 Type B ve Y2 paketlerini birlikte içerebilir.

### Güncelleyici CE kurulumu

Eşleşen paketi ve modele özel yanıp sönme yolunu seçmek için seçilen modeli kullanır. Kullanıcının bir dosya adı tahmin etmesi gerekmemelidir.

## Beş adımda bir projeyi yayımlayın
  - Güncelleyici CE deposunu çatallayın. Kendi çatalınızı yaratın [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), ardından çatalınızı yerel olarak klonlayın.
  - Genel bir ürün yazılımı deposu hazırlayın. Havuzun herkese açık olduğundan ve sürümünün doğru ZIP varlıklarını içerdiğinden emin olun. Koyabilirsin `rom.zip`, `rom_type_b.zip`, Ve `rom_y2.zip` aynı sürüme ait olduklarında aynı sürümde.
  - Manifest'i düzenleyin. Açık `slidia_manifest.xml` Updater CE çatalınızın kökünde. Sürümün desteklediği her model için bir satır ekleyin (Y1 ve Y2 ortak çifttir). `repo` değer deponun değeridir `owner/repository`; `url` halka açık proje sayfasıdır.
  - Kataloğu test edin. Güncelleyiciyi düzenlenen ödemeden çalıştırın. Y1 seçeneğini seçin ve projenin Y1 varlıklarını gösterdiğini onaylayın. Y2 seçin ve Y2 yayınını gösterdiğini onaylayın. Her ikisi de yayınlandığında Type A ve Type B'i ayrı ayrı kontrol edin.
  - Bir çekme isteği açın. Bildiri değişikliğini çatalınıza aktarın ve yukarı akış Updater CE deposuna karşı bir çekme isteği açın. Proje bağlantısını, desteklenen modelleri, sürüm etiketini, varlık adlarını ve test ettiğiniz cihazları ekleyin.

## Bildirim satırlarınızı oluşturun

Depoyu doldurun ve sürümün desteklediği her modeli işaretleyin. Jeneratör bir tane yazıyor `<package>` her model için bir satırdır ve yalnızca sizin belirlediğiniz nitelikleri içerir, böylece sonuç geçerli olanla eşleşir `slidia_manifest.xml` biçimi. Güncelleyici CE'nin okuduğu her öznitelik aşağıda mevcuttur; isteğe bağlı olanlar aşağıdadır Daha fazla seçenek.Depo URL'siGenel GitHub deposu. Jeneratör çıkartır `owner/repository` URL'den.Yazılım adıUygulamada ve site kataloğunda gösterilir.Proje URL'siProjenin veya sürüm notlarının insanlara yönelik sayfası.MarkaModelin varsayılan markasını kullanmak için bunu temizleyin. SR1, Q3, Q5 ve Q3e, Timmkoo modelleridir.Cihazlar (her biri bir satır)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eDiğer modellerYukarıda listelenmeyen bir model için. Bilinen modeller katalog yazımlarını korur.Bayraklar`do_not_keep_data` — bu ürün yazılımı için Verileri Sakla'yı asla teklif etmeyinOrijinal Yazılımdan Oluşturuldu — ekler `derivative="y1-community/y1-stock-rom"`

Verileri Sakla, yalnızca gelen ürün yazılımı ile yüklenen ürün yazılımı aynı olduğunda veya bir yazılımı paylaştığında sunulur. `derivative` kök. Bayrağı yalnızca kullanıcı verilerinin gerçekten taşınamadığı durumlarda kullanın.Daha fazla seçenek: simge, çizim, sürüm varlıkları, kurulum sonrası ve aynalar

#### Simge ve sanat eseriSimge dosyasıDepoya göndereceğiniz resmi seçin. Bu, onun ön izlemesini yapar ve ham URL'sini oluşturur; hiçbir şey yüklemiyor.Depodaki simge yoluDepo köküne göre taahhüt edilen görüntünün yolu.Simge dalıSimge URL'siDoğrudan resim URL'si. Boş olduğunda, uygulama sürümün `updater.png` veya oluşturulmuş bir simge.Seçilen simge önizlemesi

Karanlık mod simgesi URL'siİsteğe bağlı koyu tema simgesi. `image_dark` kabul edilen bir takma addır.Işık resmi URL'siYayınlanan görüntüden sonra denenen ikincil çizim ve `icon`.Koyu resim URL'si

#### Varlıkları serbest bırakVarlık adını serbest bırakSeçilen her model için bir ad. Kullanmak için boş bırakın `rom.zip` Y1 üzerinde ve `rom_<model>.zip` başka yerde.Varlık modeliSürümün fermuarları adlandırılmadığında kullanılan Glob `rom*.zip`.Type A varlıkAdı öyle söylemediğinde Y1 Type A paketi için Glob.Type B varlıkAdı öyle söylemediğinde Y1 Type B paketi için Glob.Minimum uygulama sürümüGirişi eski Güncelleyici CE yapılarından gizleyin.

#### Bağlantılar, yansıtmalar ve Keep Data ailesiKurulum sonrası sayfasıBaşarılı bir kurulumun ardından açıldı.Kurulum sonrası ikinci sayfaÇok sayfalı kurulum kılavuzu için isteğe bağlı ikinci adım.Taşınabilir zip aynalarVirgülle ayrılmış `*-mirror` Taşınabilir Yanıp Sönen Zip paketleri oluşturan depolar.Türev deposuBu sürümün oluşturulduğu ürün yazılımı. İlgili donanım yazılımları, Verileri Sakla'nın kontrol ettiği bir veri bölümünü paylaşır.Bilgi deposuSürümleri bu ürün yazılımındaki uygulamaları açıklayan uygulama deposu. Ayrıca bir kurulum sonrası sayfasına da ihtiyacı var.APK deposuUygulamanın bellenimden sonra APK indirilip yüklendiği uygulama deposu.

#### Katalog ekstralarıSümüklüböcekBağlantılar ve kayıtlı yükleme kayıtları için kararlı tanımlayıcı. Birkaç model seçildiğinde model otomatik olarak eklenir.Tanım`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Satırları kopyala

En son manifest yükleniyor…Satırlarınızın eklendiği en son manifestoyu önizleyin

Jeneratör akımı getirdi `slidia_manifest.xml` bu depodan ve oluşturduğunuz satırları hemen önce ekledim `</slidia>`.

Paylaşılan bir depo için bir satır yeterli değildir. Y2 satırı eksikse, Y2 kullanıcıları model uyumlu bir giriş alamayacaklardır. `rom_y2.zip` projenin sürümünde mevcuttur. Aynı durum sürümünüzün desteklediği diğer tüm modeller için de geçerlidir.

### Bildirgenin okuduğu her özellik

Bunlar, güncel Güncelleyici CE'nin anladığı özelliklerdir. Jeneratör yalnızca sizin doldurduklarınızı yazar; geri kalanı için uygulama makul varsayılanlara geri döner.slidia_manifest.xml paketi nitelikleri ve anlamları``````````````````````````````````````````````````````````````````````````````````````````````

| Bağlanmak | Gerekli | Ne işe yarar |
| --- | --- | --- |
| name | Evet | Katalogda ve kurulum kartlarında gösterilen yazılım adı. |
| repo | Evet | owner/repo. Uygulama, deponun GitHub sürümlerini okur. |
| device | Evet | Hedef model, büyük harf (Y1, Y2, G1, Q3e, …). Model başına bir giriş tutun. |
| url | Tavsiye edilen | Katalogdan açılan proje sayfası veya sürüm notları. |
| type, handler | Evet pratikte | type="img" Ve handler="Custom Firmware". Diğer türler ve ürün yazılımı olmayan işleyiciler atlanır. |
| brand | İsteğe bağlı | Katalog markası (Innioasis, Timmkoo). Empty modelin varsayılan markasını kullanır. |
| package_name | İsteğe bağlı | Varlık dosya adını serbest bırakın. Varsayılanlar rom.zip Y1 üzerinde ve rom_<model>.zip diğer modellerde. |
| asset_pattern | İsteğe bağlı | Ürün yazılımı zip'leri adlandırılmayan sürümler için büyük/küçük harfe duyarlı olmayan küre rom*.zip (Örneğin my-firmware-*.zip). |
| type_a_asset, type_b_asset | İsteğe bağlı | Dosya adları olağan işaretçileri içermediğinde Y1 Type A ve Type B zip'lerini tanımlayan küreler. |
| icon | İsteğe bağlı | Logo URL'si. Sürümün kendi sürümünden sonra kullanılır updater.png / updater.jpgve her sürüm için geri dönüş olarak. |
| icon_dark | İsteğe bağlı | Koyu temalı logo. image_dark kabul edilen bir takma addır. |
| image | İsteğe bağlı | İkincil ışık sanat eseri, daha sonra denendi icon. |
| post_install, post_install2 | İsteğe bağlı | Başarılı bir kurulumun ardından sayfalar açıldı. İkincisi çok adımlı bir kılavuzu kapsar. |
| portable_zips | İsteğe bağlı | Virgülle ayrılmış *-mirror Çalıştırılmaya hazır taşınabilir paketler yayınlayan depolar. |
| derivative | İsteğe bağlı | Firmware'in oluşturulduğu depo. Aynı türev köküne sahip ürün yazılımı, kullanıcı verilerini tutabilir. |
| info_repo | İsteğe bağlı | Sürümleri, bellenimin ne dağıttığını açıklayan uygulama deposu. Gereklilikler post_install veya post_install2. |
| apk_repo | İsteğe bağlı | Uygulamanın bellenimden sonra yüklediği APK uygulama deposu. |
| min_version | İsteğe bağlı | Güncelleyici CE bu sürümden daha eski olduğunda girişi gizleyin. |
| do_not_keep_data | İsteğe bağlı | true (Ayrıca 1 / yes) bu ürün yazılımı için Verileri Saklamayı tamamen engeller. |
| slug | İsteğe bağlı | Bağlantılar ve kayıtlı yükleme kayıtları için kararlı tanımlayıcı. Boş olduğunda isim ve modelden oluşturulur. |
| description | İsteğe bağlı | Kısa katalog açıklaması. Bu, nitelik değeri veya öğenin metni olabilir. |

Eski adlar uyumluluk açısından hâlâ okunmaktadır: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` Ve `image_dark`. Yeni girişlerde yukarıdaki mevcut adlar kullanılmalıdır.

### Satırları çekme isteği olarak gönderin
  - Yukarıdaki oluşturulan satırları kopyalayın. Zaten en son manifest formatıyla eşleşiyorlar.
  - Düzenlemek `slidia_manifest.xml` depoda. Aşağıdaki düzenleme bağlantısını kullanın; depo ana bilgisayarı sizin için otomatik olarak bir çatal ve dal oluşturur.
  - Satırları hemen önce yapıştırın `</slidia>`, mevcut girişleri değiştirmeden tutmak.
  - Yeni bir şubeye bağlanın (Örneğin `add-your-firmware`), ardından Güncelleyici CE deposuna yönelik bir çekme isteği açın.
  - PR'a şunları dahil edin: proje bağlantısı, desteklenen modeller, sürüm etiketi, varlık adları ve test ettiğiniz cihazlar.
[Güncelleyici CE bildirimini düzenleyin](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[En son manifestoyu görün](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Model adlarını büyük harfle tutun, genel deponuzun tam URL'sini kullanın ve `type="img"` Ve `handler="Custom Firmware"` Firmware girişi için.

## Sürümün doğrulanmasını kolaylaştırın

Sürüme net bir etiket ve sürüm notu verin. Etiket insanlar için faydalıdır ancak ZIP varlık adları, Updater CE'nin yükleme paketlerini tanımlamak için kullandığı adlardır.

### Kontrol listesini yayınlayın
  - Sürümü herkese açık olarak yayınlayın.
  - ZIP dosyalarını yayın varlıkları olarak ekleyin.
  - Notlarda desteklenen modeli ve Type A veya Type B belirtin.
  - Gerekli hazırlıkları veya bilinen limitleri listeleyin.

### Bir sürüm, üç varlık

Paylaşılan bir sürüm şunları içerebilir: `rom.zip`, `rom_type_b.zip`, Ve `rom_y2.zip`. Güncelleyici bunları ayrı ayrı sınıflandırır ve model ve donanım filtreleri arasından seçim yapar.

### Tahminleri gruplamayın

Bir varlığın görünmesini sağlamak için Y2 dosya adının altına bir Y1 paketi eklemeyin veya test edilmemiş dağılım, ön yükleyici veya bölüm verileri eklemeyin.

## Flashlama sırasında model girişleri neden önemlidir?

Manifest yalnızca bir indirme menüsü değildir. Çıkarma işleminden sonra Güncelleyici CE, eşleşen yükleme yolunu hazırlamak için çözümlenen modeli kullanır. Y1 ve Y2 farklı platform dosyalarına, ön yükleyicilere, dağılım yapılandırmasına ve cihaz düzenlerine sahiptir.
  - Y1: güncelleyici Y1 yolunu hazırlar ve MTKClient kullanıldığında aygıtın adlandırılmış bölümlerini kullanır.
  - Y2: güncelleyici Y2 yolunu hazırlar ve Y2 MT6582 yapılandırmasını kullanır. Tam kurtarma, modele göre doğru dağılım verilerinden fiziksel adresleri kullanabilir.
  - Platformlar Arası Destek: Updater CE, ekstra yükseltme araçlarına gerek kalmadan doğrudan Windows, Linux ve macOS'ta (hem Intel hem de Apple Silicon Mac'leri destekler) yerel flaşlamayı yönetir.
Katkıda bulunanlar flaş ofsetleri değil, doğru ürün yazılımı dosyalarını sağlamalıdır. Kötü bir pakete geçici bir çözüm bulmak için dağıtım adreslerini, ön yükleyicileri, DA dosyalarını veya bölüm komutlarını düzenlemeyin. Sürüm varlığını sabitleyin ve amaçlanan model üzerinde test edin.

## Birleştirme talebinde bulunmadan önce
  - XML'i bir XML ayrıştırıcıyla doğrulayın. Eksik bir alıntı veya kapanış `/>` kendisinden sonraki her girişi gizleyebilir.
  - Güncelleyiciyi ödeme sayfasından başlatın, böylece uzaktan yenilemeden önce yerel bildirimi yükler.
  - Y1 ve Y2'i bağımsız olarak kontrol edin. Projenin yalnızca paketinin desteklendiği yerde göründüğünü doğrulayın.
  - Sürüm listesini kontrol edin `rom.zip`, `rom_type_b.zip`, Ve `rom_y2.zip` uygulanabilir olduğu şekilde.
  - Güvenilir bir USB veri kablosu ve Orijinal Yazılıma geri dönmek için bir kurtarma planı kullanarak amaçlanan cihazdaki gerçek kurulumu test edin.
  - Çekme isteğinde neyi test ettiğinizi açıklayın. Test edilmemiş bir modeli desteklenmiş olarak tanımlamayın.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Yerel bir kontrol için bu komutu depo kökünden çalıştırın. Yalnızca XML sözdizimini doğrular; bir sürümün geçerli bir donanım yazılımı içerdiğini veya bir aygıtın flashlanmasının güvenli olduğunu kanıtlamaz.

## Yararlı proje bağlantıları[Çatal Güncelleyici CE](https://github.com/y1-community/Innioasis-Updater/fork)[Manifestoya bakın](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Topluluk katkı notları](support_devs_tr.html)[Sorun giderme](troubleshooting_tr.html)

## AI ajanları için modlama becerileri

Deponun `skills/` dizin, Y1 ve Y2 donanım, aygıt yazılımı, temalar ve uygulamalar üzerinde çalışan aracılar için kaynak temelli bir bilgi tabanıdır. Her beceri, iddiaların geldiği proje dosyalarını adlandırır, böylece aracı, cihazı değiştirmeden önce bir gerçeği kontrol edebilir.Buradan başlayın

### [Beceri endeksi ve güvenlik kuralları](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Bir becerinin nasıl yükleneceği, bir gerçeğin hangi model için geçerli olduğu ve hiçbir paketin yazmaması gereken bölümler.Donanım

### [Y1 donanım](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, önemli olaylar olarak tekerlek, 480x360 ekran, FM/ses yolları, depolama ve Type A/B bölüm haritası.Donanım

### [Y2 donanım](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

MT6582 kartı, cihaz ağacı, GC9503V/ST7701S panelleri, PMIC/DAC rayları, bölmeler ve önyükleme görüntüsü.Firmware

### [Firmware paketleri](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomi, dağılım dosyaları, A Sınıfı güncelleme sözleşmeleri ve sürüm kontrol listesi.Temalar

### [Tema ve dış görünüş yazma](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 config.json temaları, Rockbox WPS/SBS, Reborn dış görünümler ve Y2Player dış görünüm formatı v2.Tüm beceriler

### [Beceriler klasörüne göz atın](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, hazır Android ROM'lar, Y2Linux, Android uygulamaları, başlatıcılar, sürüm notları ve site yayınlama.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
