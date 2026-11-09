---
title: "Innioasis Y1 و Y2 USB السائقين | برنامج تشغيل Windows وأذونات Linux - Innioasis محدث"
description: "قم بإعداد جهاز الكمبيوتر الخاص بك للحصول على تحديث Innioasis: برنامج تشغيل Windows MediaTek وأذونات Linux USB - بالإضافة إلى إصلاحات الكابلات والتوقيت."
language: "ar"
source: "https://innioasis.app/drivers_ar.html"
---

# Innioasis Y1 و Y2 USB السائقين | برنامج تشغيل Windows وأذونات Linux - Innioasis محدث

إعداد الكمبيوتر

# اجعل الكمبيوتر جاهزًا قبل اللاعب.

تأتي معظم مشكلات الاتصال من برنامج التشغيل أو الأذونات أو الكابل أو التوقيت. يحتاج Windows إلى تثبيت برنامج التشغيل MediaTek. يحتاج Linux إلى أذونات USB الصحيحة. ابحث عن النظام الأساسي الخاص بك أدناه.[احصل على Updater CE](guide_ar.html#platform)[استكشاف الأخطاء وإصلاحها](troubleshooting_ar.html)

## Windows
  - قم بتنزيل مثبت برنامج التشغيل MediaTek أدناه.
  - قم بتشغيل برنامج التثبيت واسمح لـ Windows بتثبيت برنامج التشغيل.
  - أعد تشغيل الكمبيوتر.
  - افتح Updater CE وانتظر حتى تظهر رسالة الاتصال قبل توصيل المشغل الذي تم إيقاف تشغيله.

تقوم بعض أنظمة Windows بحظر برنامج التشغيل من خلال العزل الأساسي (تكامل الذاكرة). إذا ظل Updater CE غير قادر على رؤية المشغل بعد إعادة التشغيل، فقم بإيقاف تشغيل تكامل الذاكرة في Windows Security، وأعد تشغيل برنامج التشغيل وأعد تثبيته. قم بإعادة تشغيل الإعداد عند الانتهاء إذا كان نظامك يسمح بذلك.

لن يقوم Windows بتشغيل التطبيق؟ إذا أدى أمان Windows أو التحكم الذكي في التطبيقات إلى إيقاف فتح Updater CE، فافتحه الإعدادات (يضعط Win + I) → الخصوصية والأمان → Windows Security → التحكم في التطبيق والمتصفح → إعدادات التحكم في التطبيقات الذكية وتعيينه على عن. يؤثر التحكم الذكي في التطبيقات حاليًا على التطبيقات الشائعة مثل Epic Overlay Service (المستخدم في Fortnite) - تطبيق Updater CE آمن وموثوق للاستخدام. لإعادة التمكين لاحقًا، اضبط `VerifiedAndReputablePolicyState` ل `1` (على) أو `2` (وضع التقييم) تحت `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` في محرر التسجيل.[تحميل برنامج تشغيل ويندوز](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[العودة إلى الدليل الرئيسي](guide_ar.html#windows) · [تنزيلات البرامج](firmware_ar.html)

## أذونات لينكس USB

يحتاج Linux إلى السماح لحساب المستخدم الخاص بك بالتحدث إلى الشريحة MediaTek USB الموجودة داخل المشغل. عادةً ما يقوم Updater CE بفرز هذا الأمر أثناء التثبيت، ويغطي نفس الإذن SP Flash Tool، لذا تعامل مع هذا كخطوة إصلاح بدلاً من مرحلة عادية.
  - قم بتشغيل Updater CE كمستخدم عادي، وليس كجذر. يطلب المثبت وصول المسؤول فقط عندما يحتاج إليه.
  - تحقق وينظر إلى لاعب على الإطلاق. قم بإيقاف تشغيل المشغل، وقم بتوصيل الكابل، وقم بتشغيل الأمر lsusb في الجهاز الطرفي. يظهر المشغل المتصل كجهاز MediaTek بمعرف البائع 0e8d.
`lsusb`
  - إذا ظهر في lsusb ولكن يقول Innioasis Updater CE أو SP Flash Tool أن الإذن مرفوض أو لا يمكنه فتح المنفذ، فهذا يعني أن المستخدم الخاص بك يفقد الوصول إلى جهاز USB. تغطي نفس قاعدة udev كلتا الأداتين، لذا أضف واحدة تسمح للمستخدمين بقراءتها.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

احفظ هذا السطر في ملف جديد باسم /etc/udev/rules.d/51-innioasis.rules، ثم قم بتشغيل:`sudo udevadm control --reload && sudo udevadm trigger`
  - افصل المشغل بالكامل، ثم قم بتوصيله مرة أخرى، ثم حاول التثبيت مرة أخرى.
  - إذا أبلغ SP Flash Tool عن إذن تسلسلي أو سباق منفذ، فافصل القابس بالكامل وأعد الاتصال فقط عند المطالبة بذلك.
لا ترتجل تعويضات الفلاش.إذا انتقلت إلى أداة الاسترداد اليدوية، فاستخدم الملفات والتكوين الخاص بالطراز المرفق مع المشروع.

[العودة إلى الدليل الرئيسي](guide_ar.html#linux) · [تنزيلات البرامج](firmware_ar.html) · [SP Flash Tool الدليل](sp-flash-tool_ar.html)

## الكابل والتوقيت
  - استخدم كبل بيانات USB معروفًا.
  - تجنب المحاور أثناء استكشاف الأخطاء وإصلاحها.
  - قم بإيقاف تشغيل الطراز الصحيح بالكامل.
  - الاتصال فقط في الموجه.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
