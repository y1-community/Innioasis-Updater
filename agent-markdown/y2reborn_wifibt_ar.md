---
title: "إعداد Wi-Fi وBluetooth وراديو FM لـ Reborn (Y2Linux) - Innioasis محدث"
description: "دليل قصير بعد التثبيت لـ Reborn (Y2Linux / Y2Reborn) على Innioasis Y2: انسخ system.img، ثم قم بإعداد Wi-Fi وBluetooth وراديو FM."
language: "ar"
source: "https://innioasis.app/y2reborn_wifibt_ar.html"
---

# إعداد Wi-Fi وBluetooth وراديو FM لـ Reborn (Y2Linux) - Innioasis محدث

Innioasis Y2 · Reborn ما بعد التثبيت

# قم بإعداد Wi-Fi وBluetooth وراديو FM.

انسخ ملفًا واحدًا إلى المشغل الخاص بك. Reborn يتولى الباقي.[تنزيل system.img (860 ميجابايت)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[دليل التثبيت](guides/reborn-y2linux-y2.html)[لماذا Y2Reborn؟](reborn-y2linux-benefits_ar.html)

## لماذا هذا الملف؟

تحتاج شبكة Wi-Fi وBluetooth وراديو FM إلى خمس وحدات برامج ثابتة MediaTek لا يمكن لـ Reborn شحنها. وهم داخل الرسمي Y2 `system.img`. Reborn يستخرجها مرة واحدة ويفحصها ويحذف الملف.

## يثبت
  - تحميل system.img

تحميل v3.2.0 FM `system.img` إلى جهاز الكمبيوتر الخاص بك.[ تحميل system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - التمهيد Reborn مرة واحدة

قم بتشغيل المشغل. انتظر إعداد التخزين للانتهاء، ثم أعد تشغيله مرة واحدة.
  - الاتصال بجهاز الكمبيوتر الخاص بك

استخدم كابل بيانات USB. يظهر اللاعب ك التخزين الداخلي.على ماك؟

تثبيت [OpenMTP](https://openmtp.ganeshrvel.com/) لتصفح المشغل. يقوم Windows وLinux بتثبيته تلقائيًا.
  - انسخ system.img إلى البرامج الثابتة

قم بإنشاء مجلد يسمى `Firmware` في جذر التخزين الداخلي. ينسخ `system.img` فيه.
  - انتظر حتى ينتهي الإعداد

Reborn يقوم بتثبيت البرنامج الثابت للراديو تلقائيًا ويحذفه `system.img`. يستغرق هذا حوالي 10-20 ثانية. انتظر شبكة Wi-Fi وBluetooth جاهزة.
  - قم بتوصيل Wi-Fi وBluetooth وراديو FM
    - واي فاي: الإعدادات ← النظام ← الشبكة ← Wi-Fi. اختر شبكة 2.4 جيجا هرتز.
    - بلوتوث: ضع سماعات الرأس في وضع الاقتران. الإعدادات ← بلوتوث ← حددها.
    - راديو اف ام: قم بتوصيل سماعات الرأس السلكية كهوائي، ثم افتح راديو FM.

  - التحديث عبر شبكة Wi-Fi

يتم تثبيت التحديثات المستقبلية Reborn من الإعدادات → النظام → تحديث البرنامج. تبقى البرامج الثابتة للراديو في مكانها.

## هل كان هذا الدليل مفيدًا؟

هل وجدت دليل الإعداد بعد التثبيت هذا مفيدًا؟ نعم، لقد ساعد! [ بحاجة إلى مساعدة بشأن Discord ](https://discord.gg/zHrT2zrcek) شكرا لتعليقاتك! استمتع بالاستماع اللاسلكي على Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
