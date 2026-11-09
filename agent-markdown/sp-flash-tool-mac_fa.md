---
title: "SP Flash Tool برای مک · MediaTek راهنمای چشمک زن پراکنده و گزینه های جایگزین"
description: "نحوه استفاده از SP Flash Tool در مک با استفاده از Updater CE و مرور فایل‌های scatter برای فلش کردن دستگاه‌های MediaTek مانند Mechen H1، Innioasis Y1/Y2، Timmkoo، و پخش‌کننده‌های MP3 و تلفن‌های MT6580/MT6572."
language: "fa"
source: "https://innioasis.app/sp-flash-tool-mac_fa.html"
---

# SP Flash Tool برای مک · MediaTek راهنمای چشمک زن پراکنده و گزینه های جایگزین

MediaTek ابزارها و چشمک زن بین پلتفرم

# SP Flash Tool for Mac: The Complete Guide & Scatter Browser

آیا MediaTek SP Flash Tool رسمی روی macOS اجرا می‌شود؟ در اینجا وضعیت دقیق، چگونه است به‌روزرسان CE فلش بومی MediaTek را در مک و نحوه فلش کردن هر پخش کننده MP3 مبتنی بر MediaTek یا گوشی هوشمند را ارائه می دهد.

## حقیقت درباره SP Flash Tool در macOS

MediaTek هرگز نسخه رسمی macOS را منتشر نکرد ابزار فلش تلفن هوشمند (SP Flash Tool). این ابزار تنها به عنوان یک برنامه ویندوز 32 بیتی/64 بیتی و یک باینری لینوکس x86_64 وجود داشته است. شبیه‌سازی SP Flash Tool در macOS از طریق Wine یا CrossOver انجام نمی‌شود زیرا برنامه‌های افزودنی هسته macOS USB اجازه عبور سریال USB را با دقت لازم در هنگام دست دادن بوت BROM نمی‌دهد.

راه حل:به‌روزرسان CE این شکاف را با جمع کردن کتابخانه‌های چشمک زن بومی Apple Silicon و macOS اینتل (از طریق موتور پروتکل سطح پایین MTKclient) در کنار کشف خودکار پراکندگی پر می‌کند!

## فلش کردن هر دستگاه MediaTek با «نصب از فایل» (مرورگر پراکنده)

به روز رسانی CE محدود به Innioasis بازیکن نیست. می توانید از آن به عنوان یک فلاشر پراکنده جهانی MediaTek قدرتمند برای هر دستگاهی که نیاز دارید استفاده کنید SP Flash Tool نسخه 5 یا قبل از آن:
  - Mechen H1 و H11: پخش کننده های اندروید قابل حمل HiFi MT6580.
  - Timmkoo Q3, Q5, G1, A5: MediaTek پخش کننده صوتی دیجیتال صفحه لمسی.
  - Oilsky، Phueut، Luoran: MediaTek پخش کننده موسیقی MT6572 / MT6582.
  - Legacy MediaTek تلفن‌های هوشمند و تلفن‌های ویژه: دستگاه‌هایی که دارای MT6572، MT6580، MT6582، MT6735، MT6737، MT6739، MT6753 و MT8163 هستند.

### نحوه بارگذاری فایل های Scatter سفارشی در Updater CE:
  - دانلود آرشیو سیستم عامل کارخانه (`.zip` یا `.rar`) یا پوشه آن حاوی `*scatter*.txt` فایل
  - در Updater CE را انتخاب کنید مرور فایل ها… در صفحه انتخاب سیستم عامل
  - فایل متنی پراکنده را انتخاب کنید (به عنوان مثال، `MT6580_Android_scatter.txt`) یا بسته زیپ سیستم عامل.
  - به روز رسانی CE، آفست های حافظه، آدرس های پارتیشن (پیش بارگذاری، بوت، بازیابی، سیستم، داده های کاربر) را تجزیه می کند و یکپارچگی پراکندگی را تأیید می کند.
  - فرمان زنده روی صفحه را دنبال کنید: دستگاه را خاموش کنید و کابل USB را به فلاش متصل کنید.

## وقتی برای Unbricking به یک کامپیوتر x64 نیاز دارید

در حالی که macOS فلش استاندارد و نصب های سفارشی ROM را از طریق MTKclient انجام می دهد، بازیابی از خرابی های بوت لوپ عمیق (جایی که پارتیشن پیش بارگذاری پاک شد یا با هم مطابقت نداشت) نیاز به بازسازی کامل جدول پارتیشن SP Flash Tool دارد.

اگر در Mac با خطاهای stall مواجه شدید، به یک رایانه ویندوزی 64 بیتی یا ایستگاه کاری لینوکس x86_64 بروید، را انتخاب کنید Settings > Show Advanced Settings > Flash Method > SP Flash Toolو پکیج اسکتر کارخانه را فلش کنید.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
