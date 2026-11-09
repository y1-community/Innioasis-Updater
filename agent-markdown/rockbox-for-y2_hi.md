---
title: "Rockbox के लिए Y2 (Rockbox-Y2): अवलोकन, निर्माण और इंस्टॉल गाइड"
description: "Rockbox के लिए Y2, Rockbox-Y2 और रॉकबॉक्स-वाई2 Innioasis Y2 के लिए समुदाय Rockbox फर्मवेयर पोर्ट को संदर्भित करता है। जानें कि इसमें क्या शामिल है और इसे Innioasis अपडेटर सीई के साथ कैसे स्थापित किया जाए।"
language: "hi"
source: "https://innioasis.app/rockbox-for-y2_hi.html"
---

# Rockbox के लिए Y2 (Rockbox-Y2): अवलोकन, निर्माण और इंस्टॉल गाइड

[← फ़र्मवेयर डाउनलोड](firmware_hi.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox के लिए Y2 (Rockbox-Y2)

Rockbox-Y2 (जिसे Y2 के लिए "Rockbox भी कहा जाता है) Innioasis Y2 के लिए समर्पित समुदाय Rockbox फर्मवेयर पोर्ट है। यह अपने स्वयं के ROM पैकेज का उपयोग करता है (`rom_y2.zip`) और सीधे Innioasis अपडेटर सीई के माध्यम से स्थापित किया गया है।[Rockbox-Y2 स्थापित करें](rockbox-y2/install.html)[ROM डाउनलोड करें](rockbox-y2/download.html)[लिखित ट्यूटोरियल](guides/rockbox-y2.html)[Rockbox-Y2 हब](rockbox-y2/)

## Innioasis Y2 के लिए विशेष रूप से निर्मित

Innioasis अपडेटर सीई में, इस फर्मवेयर को इस प्रकार सूचीबद्ध किया गया है Rockbox कब Y2 चयनित है। इसकी विज्ञप्तियाँ द्वारा प्रकाशित की जाती हैं [spycemagic/y2-rockbox](firmware_hi.html?model=Y2&software=rockbox-y2) पैकेज नाम के साथ प्रोजेक्ट `rom_y2.zip`.

Y2 पर कभी भी Y1 फर्मवेयर पैकेज स्थापित न करें। चयन Y2 अपडेटर सीई में स्वचालित रूप से रिलीज़ सूची को Y2-केवल संगत बिल्ड में फ़िल्टर किया जाता है।

## Rockbox-Y2 क्या ऑफर करता है
  - टैग-आधारित संगीत लाइब्रेरी — अपने ऑडियो फ़ाइल टैग से एल्बम, कलाकार और शैलियाँ ब्राउज़ करें, या सीधे फ़ोल्डर ब्राउज़ करें।
  - प्लेबैक नियंत्रण - गैपलेस प्लेबैक, क्रॉसफ़ेड, रिप्लेगेन और इक्वलाइज़र सेटिंग्स।
  - कस्टम थीम - अपने Rockbox-Y2 बिल्ड के साथ संगत थीम इंस्टॉल करें ([Y2 थीम गाइड](rockbox-y2-themes.html)).
  - 100% ऑफ़लाइन - आपके MicroSD कार्ड से बिना किसी खाते या सदस्यता के स्थानीय फ़ाइलें चलाता है।
  - आसान फ़ैक्टरी पुनर्स्थापना - अपडेटर सीई में किसी भी समय Y2 मूल सॉफ़्टवेयर पर वापस लौटें।

## Rockbox-Y2 रिलीज़ चुनना
  - हमेशा चयन करें Y2 में डिवाइस मॉडल प्रथम.
  - जब तक आप किसी विशिष्ट संस्करण का परीक्षण नहीं कर रहे हों, नवीनतम रिलीज़ चुनें।
  - पढ़ें [Rockbox-Y2 रिलीज़ नोट्स](release-notes/rockbox-y2/index_hi.html) यह देखने के लिए कि प्रत्येक निर्माण में क्या परिवर्तन हुआ।

## सामुदायिक डेवलपर्स से सीधे डाउनलोड

Innioasis अपडेटर सीई हमेशा फर्मवेयर पैकेज सीधे सामुदायिक फर्मवेयर डेवलपर्स से डाउनलोड करता है ([spycemagic/y2-rockbox](firmware_hi.html?model=Y2&software=rockbox-y2)), और वे डेवलपर्स अपडेटर सीई में अपने सॉफ़्टवेयर रिलीज़ को सूचीबद्ध करने के लिए पूरी तरह से ज़िम्मेदार हैं।

आप अपडेटर सीई को डाउनलोड और फ्लैश करने दे सकते हैं `rom_y2.zip` स्वचालित रूप से, या हमारे से पैकेज डाउनलोड करें [Rockbox-Y2 डाउनलोड पेज](rockbox-y2/download.html) और [Rockbox ROM डाउनलोड पेज](rockbox-rom-download_hi.html).[Rockbox-Y2 डाउनलोड](rockbox-y2/download.html)[स्थानीय ज़िप से इंस्टॉल करें](rockbox-y2/portable-zip.html)

## कैसे स्थापित करें Rockbox-Y2
  - Innioasis अपडेटर सीई खोलें और सेट करें डिवाइस मॉडल को Y2.
  - चयन करें Rockbox में सॉफ़्टवेयर.
  - सूची से Y2 रिलीज़ चुनें।
  - क्लिक करें इंस्टॉल / पुनर्स्थापित इसलिए अपडेटर सीई सीधे डेवलपर से पैकेज डाउनलोड करता है।
  - Y2 को पूरी तरह से बंद कर दें और अपडेटर सीई के कहने पर इसे USB डेटा केबल से कनेक्ट करें।
  - पूरा होने के संदेश की प्रतीक्षा करें, फिर अनप्लग करें और अपना Y2 चालू करें।

संपूर्ण चरण-दर-चरण पूर्वाभ्यास के लिए, पढ़ें [Rockbox-Y2 ट्यूटोरियल](guides/rockbox-y2.html).

## मूल Y2 सॉफ़्टवेयर को पुनर्स्थापित करना

फ़ैक्टरी फ़र्मवेयर पर वापस जाने के लिए, चुनें Y2 और मूल सॉफ़्टवेयर अपडेटर सीई में, एक स्थिर रिलीज़ चुनें और क्लिक करें इंस्टॉल / पुनर्स्थापित. देखें [पुनर्स्थापना मार्गदर्शिका](rockbox-y2/restore-stock.html) और [Y2 मूल सॉफ़्टवेयर पृष्ठ](original-software-y2_hi.html).

## अक्सर पूछे जाने वाले प्रश्नअपडेटर सीई Rockbox-Y2 कहां से डाउनलोड करता है?

अपडेटर सीई हमेशा समुदाय फर्मवेयर डेवलपर्स के स्वयं के रिलीज से सीधे फर्मवेयर पैकेज डाउनलोड करता है (`spycemagic/y2-rockbox`). अपडेटर सीई में अपने सॉफ़्टवेयर रिलीज़ को सूचीबद्ध करने के लिए डेवलपर्स पूरी तरह से जिम्मेदार हैं।पैकेज का नाम rom_y2.zip क्यों है?

डेवलपर ने Y2 फ़र्मवेयर संग्रह को नाम दिया है `rom_y2.zip` इसलिए इसे Y1 के साथ भ्रमित नहीं किया जा सकता `rom.zip`.क्या Y1 थीम Y2 पर काम करती हैं?

हमेशा नहीं. अपने Y2 बिल्ड के लिए रिलीज़ नोट्स देखें और देखें [Rockbox-Y2 थीम गाइड](rockbox-y2-themes.html).

## संबंधित मार्गदर्शिकाएँ

### [Rockbox-Y2 हब](rockbox-y2/)

सभी Y2 गाइड: इंस्टॉल, डाउनलोड, थीम, रीस्टोर, डुअल बूट और समस्या निवारण।

### [Rockbox-Y1 बनाम Rockbox-Y2](rockbox-y1-vs-y2.html)

Y1 और Y2 Rockbox बिल्ड किस प्रकार भिन्न हैं।

### [Rockbox-Y2 थीम](rockbox-y2-themes.html)

Rockbox-Y2 पर थीम इंस्टॉल और रीसेट करना।

### [Rockbox Y1 के लिए](rockbox-for-y1_hi.html)

Innioasis Y1 पोर्ट के लिए अवलोकन और इंस्टॉल गाइड।

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
