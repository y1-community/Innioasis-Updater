---
title: "כיצד לשחזר נגן MediaTek שאינו מאתחול לאחר כשל ב-MTKclient · קהילה Innioasis"
description: "מדריך שלב אחר שלב לביטול הברקה ושחזור נגני Innioasis Y1, Y2, G1, Timmkoo ו-MediaTek ללא אתחול לאחר קטעי הבזקים של MTKclient ב-Linux או macOS."
language: "he"
source: "https://innioasis.app/recover-non-booting-device_he.html"
---

# כיצד לשחזר נגן MediaTek שאינו מאתחול לאחר כשל ב-MTKclient · קהילה Innioasis

פתרון בעיות ושחזור מכשירים

# שחזור מכשיר שאינו מאתחול לאחר הבהוב של MTKclient

אם מכשיר ה-Innioasis Y1, Y2, או MediaTek לא מצליח להידלק או מציג מסך שחור לאחר מהבהב עם MTKclient ב-macOS או Linux, אל תיבהל. ה-BootROM של החומרה (BROM) הוא קבוע ולא ניתן להרוס אותו.

## מדוע MTKclient עשוי להיתקע או להשאיר מסך שחור

MTKclient מסתמך על עומסי ניצול תוכנה (kamakiri / amonet) כדי לעקוף אימות DA ותקשורת גולמית USB באמצעות libusb. במערכות macOS ו-Linux ARM64:
  - USB חביון לחיצת יד או פסק זמן של יציאה ב-macOS יכולים לעכב את הזרקת מטען DA באמצע ההעברה.
  - כותרות מחיצות חסרות או לא שלמות משאירות את טוען האתחול (preloader / lk) במצב לא מגיב.
  - הנגן נראה מת לחלוטין - ללא LED, ללא סמל טעינה, ללא תאורה אחורית של המסך.

אפילו במצב זה, ערכת השבבים MediaTek צונחת חזרה מצב BROM (USB VID 0e8d, PID 0003), מוכן לשחזור רשמי ברמה נמוכה.

## שיטת השחזור הסופי: SP Flash Tool מנוע בעדכון CE

הדרך הבטוחה והאמינה ביותר לשחזר את השחקן הלבנים שלך היא שימוש עדכון CE מוגדר עם הפקיד SP Flash Tool אחורי.

### שלבים מדויקים בעדכון CE:
  - פתוח עדכון CE.
  - לחץ הגדרות בסרגל הצד השמאלי של הניווט.
  - גלול מטה לקטע מתקדם והפעל הצג הגדרות מתקדמות.
  - מתחת שיטת ההתקנה (או מנוע מהבהב עבור מתקין MediaTek), אתר את שיטת פלאש תפריט נפתח.
  - שנה את הבחירה מ אוטומטי (מומלץ) או MTKClient ל SP Flash Tool.
  - אשר את ההנחיה וחזור לזרימת ההתקנה הראשית.

## ארכיטקטורת פלטפורמה ודרישות מערכת הפעלה עבור SP Flash Tool

הרשמי של MediaTek `SP Flash Tool` בינארי מורכב באופן מקורי בתור an x86_64 ELF בינארי עבור לינוקס וכן א קובץ הפעלה PE32+ עבור Windows x64.הערת חומרה חשובה למשתמשי macOS ו-ARM64 Linux:
 מכיוון שMediaTek אינו מקמפל SP Flash Tool עבור macOS (Darwin) או Linux ARM64 (aarch64), משתמשי macOS ומשתמשי ARM64 Linux (כגון Raspberry Pi או Apple Silicon עם Asahi Linux) שחווים לבנה חייבים לחבר את הנגן שלהם ל: 
  - א x64 Windows PC (Windows 10 / 11 64 סיביות), או
  - א x86_64 מחשב לינוקס (אובונטו, דביאן, פדורה, Arch 64-bit).

## תהליך שחרור חומרה שלב אחר שלב
  - נתק את הנגן: נתק את הכבל USB מהנגן והמחשב לחלוטין.
  - כיבוי קשה: החזק את כפתור ההפעלה (או הפעלה + עוצמת הקול) למשך 15 שניות כדי להבטיח שערכת השבבים כבויה לחלוטין ואינה תקועה בלולאה נמוכה USB.
  - הפעל את Updater CE עם מצב SP Flash Tool: בחר את דגם המכשיר שלך (למשל. Innioasis Y1 או Innioasis Y2) ובחר תוכנה מקורית כדי לשחזר מחיצות מלאי.
  - התחל התקנה / שחזור: לחץ התקנה / שחזור בעדכון CE. המתן עד שהודעת הסטטוס תאמר מחכה לשחקן...
  - הכנס כבל USB להפעלת BROM: כשהמכשיר כבוי, חבר את הכבל USB ישירות ליציאת לוח אם במהירות גבוהה USB (הימנע מרכזות USB ללא חשמל.
  - המערכת תזהה את יציאת ה-VCOM MediaTek, תדחוף את סוכן ההורדה (DA), תכתוב מחדש טבלאות מחיצות ותשחזר את כל תמונות הקושחה בצורה נקייה.

## תמורות לפי דגם ומערכת הפעלה

| דגם | פלטפורמה נכשלה | הגדרת שחזור מומלצת | מנוע ומצב |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 מלאי ROM |
| Innioasis Y1 | לינוקס ARM64 / x86_64 | Linux x86_64 או Windows x64 PC | SP Flash Tool + DA קהילה |
| Innioasis Y2 | macOS (MTKclient נתקע) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 שחזור פיזור |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC עם מנהלי התקנים של VCOM | SP Flash Tool + קושחה של היצרן |
| Mechen H1 / Timmkoo A5 | כל פלטפורמה | Windows x64 או Linux x86_64 PC | SP Flash Tool + קובץ פיזור |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
