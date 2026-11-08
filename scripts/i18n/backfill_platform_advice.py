#!/usr/bin/env python3
"""
Backfill macOS Gatekeeper ('Open Anyway') and Windows Smart App Control
tokenized text nodes across translation catalogs in Innioasis-Updater and InnioasisY1Themes.
"""

import json
import os
from pathlib import Path

TRANSLATIONS = {
    "If your Mac stops you from running the app for the first time, please open System Settings, click Privacy & Security, scroll down to Security and click": {
        "de": "Wenn Ihr Mac Sie daran hindert, die App zum ersten Mal auszuführen, öffnen Sie bitte die Systemeinstellungen, klicken Sie auf Datenschutz und Sicherheit, scrollen Sie nach unten zu Sicherheit und klicken Sie auf",
        "fr": "Si votre Mac vous empêche d'exécuter l'application pour la première fois, ouvrez Réglages Système, cliquez sur Confidentialité et sécurité, faites défiler jusqu'à Sécurité et cliquez sur",
        "es": "Si tu Mac te impide ejecutar la app por primera vez, abre Ajustes del Sistema, haz clic en Privacidad y seguridad, baja hasta Seguridad y haz clic en",
        "it": "Se il tuo Mac ti impedisce di eseguire l'app per la prima volta, apri Impostazioni di Sistema, fai clic su Privacy e sicurezza, scorri verso il basso fino a Sicurezza e fai clic su",
        "ja": "初めてアプリを実行する際にMacでブロックされた場合は、「システム設定」を開き、「プライバシーとセキュリティ」をクリックして、「セキュリティ」まで下にスクロールし、",
        "ko": "Mac에서 앱을 처음 실행할 때 차단되면 시스템 설정을 열고 개인정보 보호 및 보안을 클릭한 다음 보안까지 아래로 스크롤하여",
        "zh": "如果您的 Mac 首次运行该应用程序时将其阻止，请打开“系统设置”，点击“隐私与安全性”，向下滚动至“安全性”，然后点击",
        "zh-CN": "如果您的 Mac 首次运行该应用程序时将其阻止，请打开“系统设置”，点击“隐私与安全性”，向下滚动至“安全性”，然后点击",
        "zh-TW": "如果您的 Mac 首次執行該應用程式時將其阻止，請打開「系統設定」，點擊「隱私與安全性」，向下滾動至「安全性」，然後點擊",
        "pt": "Se o seu Mac o impedir de executar a aplicação pela primeira vez, abra as Definições do Sistema, clique em Privacidade e Segurança, desloque-se para baixo até Segurança e clique em",
        "pt-BR": "Se o seu Mac impedir você de executar o aplicativo pela primeira vez, abra Ajustes do Sistema, clique em Privacidade e Segurança, role para baixo até Segurança e clique em",
        "ru": "Если Mac блокирует первый запуск приложения, откройте «Системные настройки», выберите «Конфиденциальность и безопасность», прокрутите вниз до раздела «Безопасность» и нажмите",
        "pl": "Jeśli Twój Mac blokuje uruchomienie aplikacji po raz pierwszy, otwórz Ustawienia systemowe, kliknij Prywatność i ochrona, przewiń w dół do sekcji Ochrona i kliknij",
        "nl": "Als uw Mac voorkomt dat u de app voor het eerst uitvoert, open dan Systeeminstellingen, klik op Privacy en beveiliging, scrol omlaag naar Beveiliging en klik op",
        "tr": "Mac'iniz uygulamayı ilk kez çalıştırmanızı engelliyorsa lütfen Sistem Ayarları'nı açın, Gizlilik ve Güvenlik'e tıklayın, Güvenlik'e kadar aşağı kaydırın ve",
        "ar": "إذا منعك جهاز Mac من تشغيل التطبيق لأول مرة، يرجى فتح إعدادات النظام، والنقر على الخصوصية والأمان، ثم التمرير لأسفل إلى الأمان والنقر على",
        "uk": "Якщо ваш Mac блокує запуск програми вперше, відкрийте Системні параметри, клацніть Приватність і безпека, прокрутіть униз до розділу Безпека та натисніть",
    },
    ". You can also Control-click (or right-click) the app in Finder and choose Open.": {
        "de": ". Sie können auch im Finder bei gedrückter Ctrl-Taste (oder mit der rechten Maustaste) auf die App klicken und „Öffnen“ wählen.",
        "fr": ". Vous pouvez également faire un Contrôle-clic (ou un clic droit) sur l'application dans le Finder et choisir Ouvrir.",
        "es": ". También puedes hacer Control-clic (o clic derecho) en la aplicación en el Finder y seleccionar Abrir.",
        "it": ". Puoi anche fare clic tenendo premuto il tasto Ctrl (o fare clic con il tasto destro) sull'app nel Finder e scegliere Apri.",
        "ja": "をクリックしてください。FinderでアプリをControlキーを押しながらクリック（または右クリック）して「開く」を選択することもできます。",
        "ko": "을(를) 클릭하세요. Finder에서 앱을 Control-클릭(또는 마우스 우클릭)한 후 '열기'를 선택할 수도 있습니다.",
        "zh": "。您也可以在访达中按住 Control 键点按（或右键点按）该应用程序并选择“打开”。",
        "zh-CN": "。您也可以在访达中按住 Control 键点按（或右键点按）该应用程序并选择“打开”。",
        "zh-TW": "。您也可以在訪達（Finder）中按住 Control 鍵點按（或右鍵點按）該應用程式並選擇「打開」。",
        "pt": ". Também pode premir a tecla Control (ou clicar com o botão direito) na aplicação no Finder e escolher Abrir.",
        "pt-BR": ". Você também pode clicar com a tecla Control pressionada (ou clicar com o botão direito) no aplicativo no Finder e escolher Abrir.",
        "ru": ". Вы также можете нажать на приложение в Finder удерживая клавишу Control (или правой кнопкой мыши) и выбрать «Открыть».",
        "pl": ". Możesz także kliknąć aplikację w Finderze z wciśniętym klawiszem Control (lub prawym przyciskiem myszy) i wybrać Otwórz.",
        "nl": ". U kunt ook met Control ingedrukt (of met de rechtermuisknop) op de app in de Finder klikken en Openen kiezen.",
        "tr": ". Ayrıca Finder'da uygulamayı Control tuşuna basarak tıklatabilir (veya sağ tıklayıp) Aç'ı seçebilirsiniz.",
        "ar": ". يمكنك أيضًا النقر مع الضغط على مفتاح Control (أو النقر بزر الماوس الأيمن) على التطبيق في Finder واختيار فتح.",
        "uk": ". Ви також можете клацнути програму у Finder, утримуючи клавішу Control (або правою кнопкою миші), і вибрати Відкрити.",
    },
    "You can also Control-click (or right-click) the app in Finder and choose Open.": {
        "de": "Sie können auch im Finder bei gedrückter Ctrl-Taste (oder mit der rechten Maustaste) auf die App klicken und „Öffnen“ wählen.",
        "fr": "Vous pouvez également faire un Contrôle-clic (ou un clic droit) sur l'application dans le Finder et choisir Ouvrir.",
        "es": "También puedes hacer Control-clic (o clic derecho) en la aplicación en el Finder y seleccionar Abrir.",
        "it": "Puoi anche fare clic tenendo premuto il tasto Ctrl (o fare clic con il tasto destro) sull'app nel Finder e scegliere Apri.",
        "ja": "FinderでアプリをControlキーを押しながらクリック（または右クリック）して「開く」を選択することもできます。",
        "ko": "Finder에서 앱을 Control-클릭(또는 마우스 우클릭)한 후 '열기'를 선택할 수도 있습니다.",
        "zh": "您也可以在访达中按住 Control 键点按（或右键点按）该应用程序并选择“打开”。",
        "zh-CN": "您也可以在访达中按住 Control 键点按（或右键点按）该应用程序并选择“打开”。",
        "zh-TW": "您也可以在訪達（Finder）中按住 Control 鍵點按（或右鍵點按）該應用程式並選擇「打開」。",
        "pt": "Também pode premir a tecla Control (ou clicar com o botão direito) na aplicação no Finder e escolher Abrir.",
        "pt-BR": "Você também pode clicar com a tecla Control pressionada (ou clicar com o botão direito) no aplicativo no Finder e escolher Abrir.",
        "ru": "Вы также можете нажать на приложение в Finder удерживая клавишу Control (или правой кнопкой мыши) и выбрать «Открыть».",
        "pl": "Możesz także kliknąć aplikację w Finderze z wciśniętym klawiszem Control (lub prawym przyciskiem myszy) i wybrać Otwórz.",
        "nl": "U kunt ook met Control ingedrukt (of met de rechtermuisknop) op de app in de Finder klikken en Openen kiezen.",
        "tr": "Ayrıca Finder'da uygulamayı Control tuşuna basarak tıklatabilir (veya sağ tıklayıp) Aç'ı seçebilirsiniz.",
        "ar": "يمكنك أيضًا النقر مع الضغط على مفتاح Control (أو النقر بزر الماوس الأيمن) على التطبيق في Finder واختيار فتح.",
        "uk": "Ви також можете клацнути програму у Finder, утримуючи клавішу Control (або правою кнопкою миші), і вибрати Відкрити.",
    },
    "Works on Intel and Apple Silicon Macs with macOS Monterey and later.": {
        "de": "Funktioniert auf Intel- und Apple-Silicon-Macs mit macOS Monterey und höher.",
        "fr": "Fonctionne sur les Mac Intel et Apple Silicon avec macOS Monterey et versions ultérieures.",
        "es": "Funciona en Mac Intel y Apple Silicon con macOS Monterey y posterior.",
        "it": "Funziona su Mac Intel e Apple Silicon con macOS Monterey e versioni successive.",
        "ja": "macOS Monterey以降を搭載したIntelおよびAppleシリコンMacで動作します。",
        "ko": "macOS Monterey 이상의 Intel 및 Apple Silicon Mac에서 작동합니다.",
        "zh": "适用于运行 macOS Monterey 及更高版本的 Intel 和 Apple 芯片 Mac。",
        "zh-CN": "适用于运行 macOS Monterey 及更高版本的 Intel 和 Apple 芯片 Mac。",
        "zh-TW": "適用於運行 macOS Monterey 及更高版本的 Intel 和 Apple 晶片 Mac。",
        "pt": "Funciona em Macs Intel e Apple Silicon com o macOS Monterey e posterior.",
        "pt-BR": "Funciona em Macs Intel e Apple Silicon com o macOS Monterey e posterior.",
        "ru": "Работает на компьютерах Mac с процессорами Intel и Apple Silicon под управлением macOS Monterey и новее.",
        "pl": "Działa na komputerach Mac z procesorami Intel i Apple Silicon z systemem macOS Monterey i nowszymi.",
        "nl": "Werkt op Intel- en Apple Silicon-Macs met macOS Monterey en later.",
        "tr": "macOS Monterey ve sonraki sürümlere sahip Intel ve Apple Silicon Mac'lerde çalışır.",
        "ar": "يعمل على أجهزة Mac المزودة بمعالجات Intel وApple Silicon بنظام macOS Monterey والإصدارات الأحدث.",
        "uk": "Працює на комп'ютерах Mac з процесорами Intel та Apple Silicon під керуванням macOS Monterey та новіших версій.",
    },
    "If Windows Security or Smart App Control stops Updater CE from opening, open": {
        "de": "Wenn die Windows-Sicherheit oder die intelligente App-Steuerung das Öffnen von Updater CE verhindert, öffnen Sie",
        "fr": "Si la Sécurité Windows ou le Contrôle intelligent des applications empêche l'ouverture d'Updater CE, ouvrez",
        "es": "Si Seguridad de Windows o el Control inteligente de aplicaciones impide abrir Updater CE, abre",
        "it": "Se Sicurezza di Windows o Controllo app intelligente impedisce l'apertura di Updater CE, apri",
        "ja": "Windows セキュリティまたはスマート アプリ コントロールによって Updater CE を開くことができない場合は、",
        "ko": "Windows 보안 또는 스마트 앱 제어로 인해 Updater CE를 열 수 없는 경우",
        "zh": "如果 Windows 安全中心或智能应用程序控制阻止 Updater CE 打开，请打开",
        "zh-CN": "如果 Windows 安全中心或智能应用程序控制阻止 Updater CE 打开，请打开",
        "zh-TW": "如果 Windows 安全中心或智慧型應用程式控制阻止 Updater CE 打開，請開啟",
        "pt": "Se a Segurança do Windows ou o Controlo de Aplicações Inteligente impedir a abertura do Updater CE, abra",
        "pt-BR": "Se a Segurança do Windows ou o Controle Inteligente de Aplicativos impedir a abertura do Updater CE, abra",
        "ru": "Если «Безопасность Windows» или функция «Умное управление приложениями» блокируют запуск Updater CE, откройте",
        "pl": "Jeśli zabezpieczenia systemu Windows lub funkcja Inteligentna kontrola aplikacji uniemożliwiają otwarcie Updater CE, otwórz",
        "nl": "Als Windows-beveiliging of Smart App Control verhindert dat Updater CE wordt geopend, open dan",
        "tr": "Windows Güvenliği veya Akıllı Uygulama Denetimi, Updater CE'nin açılmasını engelliyorsa şurayı açın:",
        "ar": "إذا منع أمان Windows أو التحكم الذكي في التطبيقات فتح Updater CE، فافتح",
        "uk": "Якщо Безпека Windows або функція розумного керування програмами блокує відкриття Updater CE, відкрийте",
    },
    ". Smart App Control is currently impacting popular applications like the Epic Overlay Service (used by Fortnite) — Updater CE is safe and verified to use. To re-enable later, set": {
        "de": ". Smart App Control wirkt sich derzeit auf beliebte Anwendungen wie den Epic Overlay Service (von Fortnite verwendet) aus – Updater CE ist sicher und für die Verwendung verifiziert. Um sie später wieder zu aktivieren, setzen Sie",
        "fr": ". Le Contrôle intelligent des applications affecte actuellement des applications populaires comme Epic Overlay Service (utilisé par Fortnite) — Updater CE est sûr et vérifié. Pour le réactiver ultérieurement, définissez",
        "es": ". El Control inteligente de aplicaciones afecta actualmente a aplicaciones conocidas como Epic Overlay Service (utilizado por Fortnite) — Updater CE es seguro y verificado. Para volver a activarlo más tarde, establece",
        "it": ". Controllo app intelligente sta attualmente influenzando applicazioni diffuse come Epic Overlay Service (utilizzato da Fortnite) — Updater CE è sicuro e verificato. Per riattivarlo in seguito, imposta",
        "ja": "に設定してください。スマート アプリ コントロールは現在、Epic Overlay Service (Fortnite で使用) などの一般的なアプリケーションに影響を与えています。Updater CE は安全で検証済みです。後で再度有効にするには、",
        "ko": "（으）로 설정하세요. 스마트 앱 제어는 현재 Fortnite에서 사용하는 Epic Overlay Service와 같은 인기 애플리케이션에 영향을 미치고 있습니다. Updater CE는 안전하며 검증되었습니다. 나중에 다시 활성화하려면",
        "zh": "。智能应用程序控制目前正在影响流行的应用程序，例如 Epic Overlay Service（Fortnite 所用）——Updater CE 安全且经验证。如需日后重新启用，请将",
        "zh-CN": "。智能应用程序控制目前正在影响流行的应用程序，例如 Epic Overlay Service（Fortnite 所用）——Updater CE 安全且经验证。如需日后重新启用，请将",
        "zh-TW": "。智慧型應用程式控制目前正在影響熱門應用程式，例如 Epic Overlay Service（Fortnite 所用）——Updater CE 安全且經驗證。如需日後重新啟用，請將",
        "pt": ". O Controlo de Aplicações Inteligente está atualmente a afetar aplicações populares como o Epic Overlay Service (usado pelo Fortnite) — o Updater CE é seguro e verificado. Para reativar mais tarde, defina",
        "pt-BR": ". O Controle Inteligente de Aplicativos está atualmente afetando aplicativos populares como o Epic Overlay Service (usado pelo Fortnite) — o Updater CE é seguro e verificado. Para reativar mais tarde, defina",
        "ru": ". Функция «Умное управление приложениями» в настоящее время влияет на популярные приложения, такие как Epic Overlay Service (используется Fortnite) — Updater CE безопасен и проверен. Чтобы повторно включить позже, установите",
        "pl": ". Inteligentna kontrola aplikacji ma obecnie wpływ na popularne aplikacje, takie jak Epic Overlay Service (używana przez Fortnite) — Updater CE jest bezpieczny i zweryfikowany. Aby włączyć ponownie później, ustaw",
        "nl": ". Smart App Control heeft momenteel invloed op populaire applicaties zoals de Epic Overlay Service (gebruikt door Fortnite) — Updater CE is veilig en geverifieerd. Om later weer in te schakelen, stelt u",
        "tr": ". Akıllı Uygulama Denetimi şu anda Epic Overlay Service (Fortnite tarafından kullanılan) gibi popüler uygulamaları etkilemektedir — Updater CE güvenlidir ve kullanımı doğrulanmıştır. Daha sonra tekrar etkinleştirmek için",
        "ar": ". يؤثر التحكم الذكي في التطبيقات حاليًا على التطبيقات الشائعة مثل Epic Overlay Service (المستخدم في Fortnite) - تطبيق Updater CE آمن وموثوق للاستخدام. لإعادة التمكين لاحقًا، اضبط",
        "uk": ". Функція розумного керування програмами наразі впливає на популярні програми, такі як Epic Overlay Service (використовується Fortnite) — Updater CE безпечний і перевірений. Щоб увімкнути знову пізніше, установіть",
    },
    "in Registry Editor.": {
        "de": "im Registrierungs-Editor.",
        "fr": "dans l'Éditeur du Registre.",
        "es": "en el Editor del Registro.",
        "it": "nell'Editor del Registro di sistema.",
        "ja": "（レジストリ エディター内）に設定します。",
        "ko": "（레지스트리 편집기）에서 설정하세요.",
        "zh": "（在注册表编辑器中）。",
        "zh-CN": "（在注册表编辑器中）。",
        "zh-TW": "（在登錄編輯程式中）。",
        "pt": "no Editor de Registo.",
        "pt-BR": "no Editor do Registro.",
        "ru": "в редакторе реестра.",
        "pl": "w Edytorze rejestru.",
        "nl": "in de Register-editor.",
        "tr": "Kayıt Defteri Düzenleyicisi'nde.",
        "ar": "في محرر التسجيل.",
        "uk": "у Редакторі реєстру.",
    }
}


def backfill_catalogs(catalog_dir: Path):
    if not catalog_dir.is_dir():
        return
    updated_files = 0
    for path in sorted(catalog_dir.glob("*.json")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        loc = path.stem
        lang = loc.split("-")[0]

        is_wrapped = isinstance(data, dict) and "strings" in data and isinstance(data["strings"], dict)
        strings_dict = data["strings"] if is_wrapped else data

        modified = False
        for eng_key, by_lang in TRANSLATIONS.items():
            trans = by_lang.get(loc) or by_lang.get(lang)
            if trans and eng_key not in strings_dict:
                strings_dict[eng_key] = trans
                modified = True

        if modified:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write("\n")
            updated_files += 1

    print(f"Updated {updated_files} catalogs in {catalog_dir}")


def main():
    root = Path(__file__).resolve().parents[2]
    backfill_catalogs(root / "i18n" / "catalogs")

    themes_root = root.parent / "InnioasisY1Themes"
    if themes_root.is_dir():
        backfill_catalogs(themes_root / "i18n" / "catalogs")


if __name__ == "__main__":
    main()
