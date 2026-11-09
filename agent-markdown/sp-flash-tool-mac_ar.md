---
title: "SP Flash Tool لنظام التشغيل Mac · MediaTek دليل الوميض المبعثر والبدائل"
description: "كيفية استخدام SP Flash Tool على Mac باستخدام Updater CE وتصفح الملفات المتناثرة لفلاش أجهزة MediaTek مثل مشغلات MP3 والهواتف Mechen H1 وInnioasis Y1/Y2 وTimmkoo وMT6580/MT6572."
language: "ar"
source: "https://innioasis.app/sp-flash-tool-mac_ar.html"
---

# SP Flash Tool لنظام التشغيل Mac · MediaTek دليل الوميض المبعثر والبدائل

MediaTek الأدوات والوميض عبر الأنظمة الأساسية

# SP Flash Tool لنظام التشغيل Mac: الدليل الكامل والمتصفح المبعثر

هل يعمل MediaTek SP Flash Tool رسميًا على نظام التشغيل macOS؟ هنا هو الوضع الدقيق، وكيف برنامج التحديث CE يوفر وميضًا أصليًا MediaTek على نظام Mac، وكيفية وميض أي مشغل MP3 MediaTek أو هاتف ذكي يعتمد على التشتت.

## الحقيقة حول SP Flash Tool على نظام التشغيل macOS

MediaTek لم يُصدر مطلقًا إصدارًا رسميًا لنظام التشغيل MacOS أداة فلاش الهاتف الذكي (SP Flash Tool). لم تكن الأداة موجودة إلا كتطبيق Windows 32 بت/64 بت وثنائي Linux x86_64. تفشل محاكاة SP Flash Tool على macOS من خلال Wine أو CrossOver لأن امتدادات macOS kernel USB لا تسمح بـ USB بالمرور التسلسلي بالدقة المطلوبة أثناء مصافحة تمهيد BROM.

الحل:برنامج التحديث CE يسد هذه الفجوة عن طريق تجميع مكتبات Apple Silicon وIntel macOS الوامضة الأصلية (عبر محرك البروتوكول منخفض المستوى MTKclient) جنبًا إلى جنب مع الاكتشاف التلقائي للتشتت!

## تحديث أي جهاز MediaTek به خاصية "التثبيت من ملف" (متصفح Scatter)

لا يقتصر برنامج Updater CE على اللاعبين Innioasis. يمكنك استخدامه بمثابة وميض مبعثر عالمي قوي MediaTek لأي جهاز يتطلب ذلك SP Flash Tool الإصدار 5 أو إصدار سابق:
  - Mechen H1 وH11: مشغلات أندرويد المحمولة HiFi MT6580.
  - Timmkoo Q3, Q5, G1, A5: MediaTek مشغلات صوتية رقمية تعمل باللمس.
  - أويلسكي، فويوت، لوران: MediaTek مشغلات الموسيقى MT6572 / MT6582.
  - الهواتف الذكية القديمة والهواتف المميزة MediaTek: الأجهزة التي تعمل بنظام MT6572 وMT6580 وMT6582 وMT6735 وMT6737 وMT6739 وMT6753 وMT8163.

### كيفية تحميل ملفات مبعثرة مخصصة في Updater CE:
  - قم بتنزيل أرشيف البرامج الثابتة للمصنع (`.zip` أو `.rar`) أو قم باستخراج المجلد الخاص به الذي يحتوي على ملف `*scatter*.txt` ملف.
  - في Updater CE، اختر تصفح الملفات... على شاشة اختيار البرامج الثابتة.
  - حدد الملف النصي المبعثر (على سبيل المثال، `MT6580_Android_scatter.txt`) أو حزمة مضغوطة للبرامج الثابتة.
  - يقوم Updater CE بتوزيع إزاحات الذاكرة، وعناوين الأقسام (أداة التحميل المسبق، والتمهيد، والاسترداد، والنظام، وبيانات المستخدم)، والتحقق من سلامة التشتت.
  - اتبع الموجه المباشر الذي يظهر على الشاشة: قم بإيقاف تشغيل الجهاز وقم بتوصيل كابل USB للوميض.

## عندما تحتاج إلى جهاز كمبيوتر x64 لإلغاء الحظر

بينما يتعامل نظام التشغيل macOS مع الوميض القياسي والتثبيت المخصص ROM بشكل نظيف عبر MTKclient، فإن التعافي من حالات فشل التشغيل العميق (حيث تم مسح قسم أداة التحميل المسبق أو عدم تطابقه) يتطلب إعادة بناء جدول الأقسام بالكامل لـ SP Flash Tool.

إذا واجهت توقفات خطأ على جهاز Mac، فقم بالتبديل إلى جهاز كمبيوتر يعمل بنظام Windows 64 بت أو محطة عمل Linux x86_64، فحدد الإعدادات > إظهار الإعدادات المتقدمة > طريقة الفلاش > SP Flash Tool، وقم بوميض حزمة المصنع المبعثرة.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
