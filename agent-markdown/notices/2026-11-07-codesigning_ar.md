---
title: "مشكلات تشغيل تطبيق Windows 10/11 والحل البديل للتحكم في التطبيقات الذكية - Innioasis محدث"
description: "إذا منعك Windows 10/11 أو Smart App Control من تشغيل التطبيق، فاتبع الحل البديل هنا."
language: "ar"
source: "https://innioasis.app/notices/2026-11-07-codesigning_ar.html"
---

# مشكلات تشغيل تطبيق Windows 10/11 والحل البديل للتحكم في التطبيقات الذكية - Innioasis محدث

من 25-10-2026 · حتى 31-12-2026 · الموديلات: Y1,Y2

# مشكلات تشغيل تطبيق Windows 10/11 والحل البديل للتحكم في التطبيقات الذكية

إذا منعك Windows 10/11 أو Smart App Control من تشغيل التطبيق، فاتبع الحل البديل هنا.

من 25-10-2026 · حتى 31-12-2026 · الموديلات: Y1,Y2

تم إرسال تقارير إيجابية كاذبة إلى Microsoft لـ `installer.exe` و `InnioasisUpdater.exe` وتم اتخاذ إجراء بشأنه، ولكن إذا كان Windows Endpoint Protection أو Smart App Control لا يزال يحظر التطبيق على جهاز الكمبيوتر الخاص بك، فاستخدم هذا الحل البديل:

### الحل المؤقت: قم بإيقاف تشغيل التحكم في التطبيقات الذكية
  - افتح ويندوز الإعدادات (يضعط `Win + I`).
  - اذهب الى الخصوصية والأمان > أمن ويندوز > التحكم في التطبيق والمتصفح.
  - تحت التحكم الذكي في التطبيقات، انقر إعدادات التحكم في التطبيقات الذكية.
  - اضبط التحكم الذكي في التطبيقات على عن. وهذا يسمح للتطبيق بالفتح والتشغيل على الفور.

إذا منعك Windows أو Edge من تنزيل Updater CE، فانقر فوق المزيد من الخيارات (…) ثم يحفظ > عرض المزيد > احتفظ به على أية حال.

### إعادة تمكين التحكم في التطبيقات الذكية

عند انتهاء تحديث التعريفات الإيجابية الخاطئة على جهاز الكمبيوتر الخاص بك، يمكنك إعادة تمكين التحكم الذكي في التطبيقات عبر سجل Windows:
  - اضغط مفتاح ويندوز + ر، يكتب `regedit`، ثم اضغط على Enter لفتح محرر التسجيل كمسؤول.
  - انتقل إلى: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (أو `Policies`).
  - تحديد موقع `VerifiedAndReputablePolicyState` في الجزء الأيمن.
  - انقر نقرا مزدوجا `VerifiedAndReputablePolicyState` وتغيير بيانات القيمة الخاصة به إلى:

  - `1` = تشغيل (قسري)
  - `2` = وضع التقييم

  - انقر فوق موافق، وأغلق محرر التسجيل، وأعد تشغيل الكمبيوتر.

[راجع تقرير installer.exe إلى Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[راجع تقرير InnioasisUpdater.exe المقدم إلى Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[افتح الصفحة المرتبطة](https://innioasis.app/notices.html)

[← جميع الإشعارات](index_ar.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
