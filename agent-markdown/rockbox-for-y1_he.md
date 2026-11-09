---
title: "Rockbox עבור Y1 (Rockbox-Y1): סקירה כללית, מדריך בנייה והתקנה"
description: "Rockbox עבור Y1, Rockbox-Y1 ו-rockbox-y1 מתייחסים כולם לקושחה Rockbox של הקהילה עבור Innioasis Y1. למד מה הוא מוסיף, איזה מבנה לבחור וכיצד להתקין אותו עם Innioasis Updater CE."
language: "he"
source: "https://innioasis.app/rockbox-for-y1_he.html"
---

# Rockbox עבור Y1 (Rockbox-Y1): סקירה כללית, מדריך בנייה והתקנה

[← הורדות קושחה](firmware_he.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox עבור Y1 (Rockbox-Y1)

"Rockbox", "Rockbox-Y1", ו-"Rockbox עבור Y1" כולם מתייחסים לאותה קהילה Rockbox קושחה עבור Innioasis Y1. הנה מה זה מוסיף לנגן שלך, איזה מבנה לבחור, וכיצד להתקין אותו עם Innioasis Updater CE.[התקן את Rockbox-Y1](rockbox-y1/install.html)[הורד את ROM](rockbox-y1/download.html)[הדרכה כתובה](guides/rockbox-y1.html)[Rockbox-רכזת Y1](rockbox-y1/)

## קושחה אחת, מספר שמות

ב-Innioasis Updater CE, קושחה זו מופיעה בתור Rockbox בעת בחירת דגם המכשיר Y1. מדריכים, סרטונים והערות שחרור קוראים לזה גם Rockbox-Y1 או Rockbox עבור Y1 כך שברור שהמבנה מיועד ל-Y1 ולא ל-Y2.

בדוק תמיד את הדגם המודפס על הנגן שלך לפני ההתקנה: חבילות הקושחה Y1 ו-Y2 אינן ניתנות להחלפה.

## מה Rockbox-Y1 מוסיף ל-Y1 שלך

Rockbox-Y1 היא יציאה קהילתית של קושחת נגן המוזיקה Rockbox בקוד פתוח עבור Innioasis Y1:
  - ספריית מוזיקה מבוססת תגים - דפדף לפי אמן, אלבום, ז'אנר ושנה באמצעות תגי שמע, או עיין בתיקיות ישירות.
  - השמעת אודיו מתקדמת - השמעה ללא פערים, Crossfade, ReplayGain ואקולייזר מלא.
  - ערכות נושא מותאמות אישית - בחר מתוך מאות ערכות נושא קהילתיות של 240p ו-360p, כולל פריסות קלאסיות בסגנון iPod.
  - רדיו FM - תמיכה מובנית ברדיו FM.
  - תוספות אופציונליות - הורדות פודקאסטים דרך Wi-Fi ו- Last.fm / ListenBrainz / Maloja סרבול ב-builds נתמכים.
  - מגף כפול — עבור חזרה לתוכנה המקורית של היצרן מבלי לבצע חידושים מחדש ב-builds נתמכים.

## באיזה Y1 build עלי לבחור?
  - 240p לעומת 360p — עבודה בבניית 240p עם ערכות נושא קלאסיות של 320×240 Rockbox; בניית 360p משתמשת בערכות נושא חדות יותר ב-480×360 Y1. התאם את רזולוציית הבנייה לנושאים שבהם תרצה להשתמש ([מדריך 240p לעומת 360p](rockbox-y1/resolution.html)).
  - Type A לעומת Type B — Type A מיועד לשחקנים Y1 שנשלחו עם תוכנת היצרן 2.0.0 ומעלה; Type B מיועד ליחידות Y1 מוקדמות יותר. בחר Type A אלא אם כן אתה יודע שה-Y1 שלך הוא Type B.
  - יציב מול לילי - בחר מבנה יציב להאזנה יומיומית, או מבנה לילי כדי לבדוק את השינויים החדשים ביותר.

## הורדות ישירות ממפתחי הקהילה

Innioasis Updater CE תמיד מוריד חבילות קושחה ישירות ממפתחי הקושחה של הקהילה ([rockbox-y1/rockbox](firmware_he.html?model=Y1&software=rockbox-y1)), והמפתחים עצמם הם האחראים הבלעדיים לרישום מהדורות התוכנה שלהם ב-Updater CE.

אתה יכול לאפשר ל-Update CE להוריד ולהתקין את הקושחה באופן אוטומטי, או להוריד את החבילות ROM מהאתר שלנו [Rockbox-Y1 דף הורדות](rockbox-y1/download.html) ו [Rockbox ROM דף הורדה](rockbox-rom-download_he.html).[Rockbox-Y1 הורדות](rockbox-y1/download.html)[התקן מ-ZIP מקומי](rockbox-y1/portable-zip.html)

## כיצד להתקין Rockbox-Y1
  - פתח את Innioasis Updater CE והגדר דגם המכשיר ל Y1.
  - בחר Rockbox ב תוכנה.
  - בחר מהדורה יציבה (או הפעל בנייה לילית כדי לבדוק תצוגה מקדימה).
  - לחץ התקנה / שחזור אז Updater CE מוריד את החבילה ישירות מהמפתח.
  - כבה לחלוטין את Y1 וחבר אותו עם כבל נתונים USB כאשר Updater CE יבקש ממך.
  - המתן להודעת ההשלמה, ואז נתק והפעל את הנגן שלך.

לצילומי מסך וטיפים מפורטים להגדרה, קרא את ה [הדרכה מלאה Rockbox-Y1](guides/rockbox-y1.html).

## שחזור התוכנה המקורית Y1

אתה יכול לחזור לתוכנת היצרן בכל עת: בחר Y1 ו תוכנה מקורית ב- Updater CE, בחר מהדורה יציבה ולחץ התקנה / שחזור. המוזיקה שלך בכרטיס MicroSD נשמרת. ראה את [מדריך לשחזור](rockbox-y1/restore-stock.html) ו [Y1 דף תוכנה מקורי](original-software-y1_he.html).

## שאלות נפוצותהאם Rockbox עבור Y1 זהה ל-Rockbox-Y1?

כן. Rockbox, Rockbox-Y1, Rockbox עבור Y1, ו `rockbox-y1` כולם מתייחסים לאותה יציאת קהילה Rockbox עבור Innioasis Y1.מאיפה Updater CE מוריד את Rockbox-Y1?

Updater CE תמיד מוריד חבילות קושחה ישירות מהגרסאות של מפתחי הקושחה בקהילה (`rockbox-y1/rockbox`). המפתחים הם האחראים הבלעדיים לרישום מהדורות התוכנה שלהם ב-Updater CE.האם אני יכול להתקין את Rockbox-Y1 על Y2?

לא. ל-Y2 יש מבנה קושחה נפרד משלו. השתמש [Rockbox עבור Y2](rockbox-for-y2_he.html) במקום זאת.האם התקנת Rockbox-Y1 תמחק את המוזיקה שלי?

לא. מוזיקה מאוחסנת בכרטיס MicroSD ואינה מושפעת בעת מהבהבת הקושחה הפנימית של הנגן.

## מדריכים קשורים

### [Rockbox-רכזת Y1](rockbox-y1/)

כל המדריכים Y1: התקנה, הורדות, ערכות נושא, שחזור, אתחול כפול ופתרון בעיות.

### [Rockbox-Y1 לעומת Rockbox-Y2](rockbox-y1-vs-y2.html)

ההבדל בין המבנה Y1 ו-Y2 Rockbox.

### [Rockbox-Y1 ערכות נושא](rockbox-y1-themes.html)

כיצד להעביר ערכות נושא של 240p ו-360p עם Updater CE.

### [Rockbox סקירה כללית](rockbox_he.html)

היכרות עם Rockbox על שחקנים Innioasis Y1 ו-Y2.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
