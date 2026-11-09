---
title: "Rockbox עבור Y2 (Rockbox-Y2): סקירה כללית, מדריך בנייה והתקנה"
description: "Rockbox עבור Y2, Rockbox-Y2 ו-rockbox-y2 מתייחסים ליציאת הקושחה Rockbox של הקהילה עבור Innioasis Y2. למד מה זה כולל וכיצד להתקין אותו עם Innioasis Updater CE."
language: "he"
source: "https://innioasis.app/rockbox-for-y2_he.html"
---

# Rockbox עבור Y2 (Rockbox-Y2): סקירה כללית, מדריך בנייה והתקנה

[← הורדות קושחה](firmware_he.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox עבור Y2 (Rockbox-Y2)

Rockbox-Y2 (נקראת גם "Rockbox עבור Y2") היא יציאת הקושחה הייעודית של הקהילה Rockbox עבור Innioasis Y2. הוא משתמש בחבילה ROM משלו (`rom_y2.zip`) ומותקן ישירות דרך Innioasis Updater CE.[התקן את Rockbox-Y2](rockbox-y2/install.html)[הורד את ROM](rockbox-y2/download.html)[הדרכה כתובה](guides/rockbox-y2.html)[Rockbox-רכזת Y2](rockbox-y2/)

## נבנה במיוחד עבור Innioasis Y2

ב-Innioasis Updater CE, קושחה זו מופיעה בתור Rockbox מתי Y2 נבחר. המהדורות שלה מתפרסמות על ידי [spycemagic/y2-rockbox](firmware_he.html?model=Y2&software=rockbox-y2) פרויקט עם שם החבילה `rom_y2.zip`.

לעולם אל תתקין חבילת קושחה Y1 על Y2. בחירה Y2 ב-Updater CE מסנן אוטומטית את רשימת ההפצות ל-Y2-builds תואמות בלבד.

## מה Rockbox-Y2 מציע
  - ספריית מוזיקה מבוססת תגים - דפדף באלבומים, אמנים וז'אנרים מתגי קבצי השמע שלך, או עיין בתיקיות ישירות.
  - בקרות השמעה - הגדרות השמעה ללא פערים, Crossfade, ReplayGain ואקולייזר.
  - ערכות נושא מותאמות אישית - התקן ערכות נושא התואמות למבנה Rockbox-Y2 שלך ([Y2 מדריך נושא](rockbox-y2-themes.html)).
  - 100% לא מקוון - מנגן קבצים מקומיים מהכרטיס MicroSD שלך ללא חשבונות או מנויים.
  - שחזור מפעל קל — חזור לתוכנה המקורית Y2 בכל עת ב-Updater CE.

## בחירת גרסה Rockbox-Y2
  - בחר תמיד Y2 ב דגם המכשיר תחילה.
  - בחר את המהדורה האחרונה אלא אם כן אתה בודק גרסה ספציפית.
  - קרא את [Rockbox-Y2 הערות שחרור](release-notes/rockbox-y2/index_he.html) לראות מה השתנה בכל מבנה.

## הורדות ישירות ממפתחי הקהילה

Innioasis Updater CE תמיד מוריד חבילות קושחה ישירות ממפתחי הקושחה של הקהילה ([spycemagic/y2-rockbox](firmware_he.html?model=Y2&software=rockbox-y2)), והמפתחים הללו הם האחראים הבלעדיים לרישום מהדורות התוכנה שלהם ב-Updater CE.

אתה יכול לתת ל-Updater CE להוריד ולהבזק `rom_y2.zip` אוטומטית, או הורד את החבילה שלנו [Rockbox-Y2 דף הורדות](rockbox-y2/download.html) ו [Rockbox ROM דף הורדה](rockbox-rom-download_he.html).[Rockbox-Y2 הורדות](rockbox-y2/download.html)[התקן מ-ZIP מקומי](rockbox-y2/portable-zip.html)

## כיצד להתקין Rockbox-Y2
  - פתח את Innioasis Updater CE והגדר דגם המכשיר ל Y2.
  - בחר Rockbox ב תוכנה.
  - בחר גרסה Y2 מהרשימה.
  - לחץ התקנה / שחזור אז Updater CE מוריד את החבילה ישירות מהמפתח.
  - כבה לחלוטין את Y2 וחבר אותו עם כבל נתונים USB כאשר Updater CE מבקש.
  - המתן להודעת ההשלמה, ואז נתק והפעל את Y2.

להדרכה המלאה שלב אחר שלב, קרא את [Rockbox-Y2 הדרכה](guides/rockbox-y2.html).

## שחזור התוכנה המקורית Y2

כדי לחזור לקושחה של היצרן, בחר Y2 ו תוכנה מקורית ב- Updater CE, בחר מהדורה יציבה ולחץ התקנה / שחזור. ראה את [מדריך לשחזור](rockbox-y2/restore-stock.html) ו [Y2 דף תוכנה מקורי](original-software-y2_he.html).

## שאלות נפוצותמאיפה Updater CE מוריד את Rockbox-Y2?

Updater CE תמיד מוריד חבילות קושחה ישירות מהגרסאות של מפתחי הקושחה בקהילה (`spycemagic/y2-rockbox`). המפתחים הם האחראים הבלעדיים לרישום מהדורות התוכנה שלהם ב-Updater CE.מדוע החבילה נקראת rom_y2.zip?

המפתח נותן שם לארכיון הקושחה Y2 `rom_y2.zip` כך שלא ניתן לבלבל אותו עם ה-Y1 `rom.zip`.האם Y1 ערכות נושא פועלות על Y2?

לא תמיד. בדוק את הערות הגרסה עבור המבנה Y2 שלך וראה את [Rockbox-Y2 מדריך נושא](rockbox-y2-themes.html).

## מדריכים קשורים

### [Rockbox-רכזת Y2](rockbox-y2/)

כל המדריכים Y2: התקנה, הורדות, ערכות נושא, שחזור, אתחול כפול ופתרון בעיות.

### [Rockbox-Y1 לעומת Rockbox-Y2](rockbox-y1-vs-y2.html)

ההבדל בין המבנה Y1 ו-Y2 Rockbox.

### [Rockbox-Y2 ערכות נושא](rockbox-y2-themes.html)

התקנה ואיפוס ערכות נושא ב-Rockbox-Y2.

### [Rockbox עבור Y1](rockbox-for-y1_he.html)

סקירה כללית ומדריך התקנה עבור היציאה Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
