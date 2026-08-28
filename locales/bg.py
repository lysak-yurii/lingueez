# Lingueez — Bulgarian (bg) translations.
# Keys are English UI strings; values are their Bulgarian equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Български"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Отказ",
    "OK": "OK",
    "Close": "Затвори",
    "Save": "Запази",
    "Delete": "Изтрий",
    "Edit": "Редактирай",
    "Remove": "Премахни",
    "Add": "Добави",
    "Refresh": "Обнови",
    "Import": "Импортиране",
    "Export": "Експортиране",
    "Search": "Търсене",
    "Fetch": "Изтегли",
    "Browse…": "Преглед…",
    "Clear": "Изчисти",
    "Pause": "Пауза",
    "Resume": "Продължи",
    "Language": "Език",
    "Translation": "Превод",
    "Word": "Дума",
    "Status": "Статус",
    "Error": "Грешка",
    "Title": "Заглавие",
    "Topic": "Тема",
    "Level": "Ниво",
    "Generate": "Генерирай",
    "Generating…": "Генериране…",
    "Translating…": "Превеждане…",
    "Format": "Формат",
    "Style": "Стил",
    "Model": "Модел",
    "Font": "Шрифт",
    "Usage": "Употреба",
    "Translation language": "Език на превода",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Меню",
    "Open Excel Table…": "Отваряне на Excel таблица…",
    "Import Excel to Database…": "Импортиране на Excel в база данни…",
    "Save Import Template…": "Запазване на шаблон за импортиране…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Аудио (MP3)…",
    "Backups…": "Резервни копия…",
    "Show Source column": "Показване на колона „Източник“",
    "Show Created At column": "Показване на колона „Създадено на“",
    "Max words…": "Максимум думи…",
    "View Log": "Преглед на дневника",
    "About": "Относно",
    "Quit": "Изход",
    "Words": "Думи",
    "Texts": "Текстове",
    "Statistics": "Статистика",
    "Bin (deleted items)": "Кошче (изтрити елементи)",
    "Settings": "Настройки",
    "Vocabulary": "Речник",
    "Search words, translations or tags…": "Търсене на думи, преводи или етикети…",
    "Search texts by title, content or words…": "Търсене на текстове по заглавие, съдържание или думи…",
    "Search scope": "Обхват на търсенето",
    "Search scope…": "Обхват на търсенето…",
    "Nothing to practice yet": "Още няма какво да упражнявате",
    "Add words to your vocabulary and they show up here.":
        "Добавете думи в речника си и те ще се появят тук.",
    "Come back when cards are due, or practice the newest words now.":
        "Върнете се, когато има карти за преговор, или упражнявайте най-новите думи сега.",
    "Practice newest words": "Упражнявай най-новите думи",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Изберете друго тесте по-горе или променете филтрите в страницата Думи.",
    "You're all caught up": "Всичко е наваксано",
    "Add word": "Добавяне на дума",
    "Copy a word in any app, then press:":
        "Копирайте дума в друго приложение и натиснете:",
    "Set a shortcut": "Задаване на пряк път",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Копирайте дума в друго приложение и натиснете {keys}, за да я добавите с превода ѝ.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Задайте пряк път в Настройки, за да добавяте копирани думи от всяко приложение.",
    " Favorites": " Любими",
    " Filters": " Филтри",
    "Filters that don't fit the table": "Филтри, които не се побират в таблицата",
    "More actions": "Още действия",
    "Filter by tag": "Филтриране по етикет",
    "Close file and return to your vocabulary": "Затваряне на файла и връщане към речника",
    "Definition": "Дефиниция",
    "Read": "Четене",
    "Favorite": "Любими",
    "Tags": "Етикети",
    "Copy": "Копиране",
    "Text": "Текст",
    "Delete selected (Del)": "Изтриване на избраните (Del)",
    "No data": "Няма данни",
    "No texts yet": "Все още няма текстове",
    "Words: {shown}/{total}": "Думи: {shown}/{total}",
    "Texts: {total}": "Текстове: {total}",
    "Texts: {shown}/{total}": "Текстове: {shown}/{total}",
    "{count} selected": "{count} избрани",
    "No selection": "Няма избрани",
    "Please select at least one word.": "Моля, изберете поне една дума.",
    "Saved": "Запазено",
    "'{word}' updated.": "„{word}“ е обновена.",
    "Database Error": "Грешка в базата данни",
    "Delete {count} word(s)?": "Изтриване на {count} дума/думи?",
    "Deleted": "Изтрито",
    "{count} word(s) deleted.": "Изтрити са {count} дума/думи.",
    "Deleted with {n} error(s).": "Изтрито с {n} грешка/грешки.",
    "Favorites": "Любими",
    "{count} word(s) added to favorites.": "Добавени са {count} дума/думи в любими.",
    "{count} word(s) removed from favorites.": "Премахнати са {count} дума/думи от любими.",
    "Status set to '{status}' for {count} word(s).": "Статусът е зададен на „{status}“ за {count} дума/думи.",
    "Max Words": "Максимум думи",
    "Show only the first N words (0 = show all):": "Показване само на първите N думи (0 = показване на всички):",
    "View Definition": "Преглед на дефиницията",
    "Copy Word": "Копиране на думата",
    "Copy Translation": "Копиране на превода",
    "Toggle Favorite": "Превключване на любими",
    "Change Status…": "Промяна на статус…",
    "Add / Remove Tags…": "Добавяне / премахване на етикети…",
    "Read Aloud": "Четене на глас",
    "Change Status": "Промяна на статус",
    "New status:": "Нов статус:",
    "Copied": "Копирано",
    "{count} row(s) copied to clipboard.": "Копирани са {count} ред/реда в клипборда.",
    "{count} item(s) copied to clipboard.": "Копирани са {count} елемент/елемента в клипборда.",
    "Copy Word(s)": "Копиране на дума/думи",
    "Copy Translation(s)": "Копиране на превод/преводи",
    "Copy Both": "Копиране на двете",
    "Search in Word": "Търсене в думата",
    "Search in Translation": "Търсене в превода",
    "Search in Tags": "Търсене в етикетите",
    "Promoted": "Повишени",
    "Google Cloud TTS unavailable": "Google Cloud TTS е недостъпен",
    "Selection limit": "Лимит на селекцията",
    "Only the first 200 selected words will be read.": "Ще бъдат прочетени само първите 200 избрани думи.",
    "Only the first 50 words will be used.": "Ще бъдат използвани само първите 50 думи.",
    "Select words to save as audio.": "Изберете думи за запазване като аудио.",
    "Nothing to export.": "Няма нищо за експортиране.",
    "Export Error": "Грешка при експортиране",
    "Settings saved.": "Настройките са запазени.",
    "Generated text saved.": "Генерираният текст е запазен.",
    "Show": "Покажи",
    "Add Word": "Добавяне на дума",
    "Stop reading": "Спиране на четенето",
    "Read — Read selected words aloud": "Четене — Прочитане на избраните думи на глас",
    "Translation": "Превод",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Външен вид",
    "Audio": "Аудио",
    "Learning": "Учене",
    "Listening": "Слушане",
    "Backups": "Резервни копия",
    "Sync your library?": "Синхронизиране на библиотеката?",
    "This will reconcile your device with the cloud:": "Това ще синхронизира устройството ви с облака:",
    "Sync now": "Синхронизирай сега",
    "Upload": "Качване",
    "Synced — ↑{up} ↓{down}": "Синхронизирано — ↑{up} ↓{down}",
    "Upload restored library?": "Качване на възстановената библиотека?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Библиотеката е възстановена. Ще бъдете попитани дали да я качите следващия път, когато свържете сървър за синхронизация.",
    "Merging this restored backup with your cloud:": "Сливане на това възстановено резервно копие с вашия облак:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Това резервно копие съдържа {items}. Да го качите и слеете в облака си сега, или да оставите облака си непроменен засега?",
    "General": "Общи",
    "Read-aloud": "Четене на глас",
    "Translation & AI": "Превод и ИИ",
    "Data": "Данни",
    "Behavior": "Поведение",
    "Progress": "Прогрес",
    "DeepL request failed — using free Google Translate instead.": "Заявката към DeepL неуспешна — вместо това се използва безплатният Google Преводач.",
    "DeepL key isn't set — using free Google Translate instead.": "Ключът за DeepL не е зададен — вместо това се използва безплатният Google Преводач.",
    "System": "Система",
    "Light": "Светла",
    "Dark": "Тъмна",
    "Appearance mode": "Режим на външния вид",
    "Widget scaling": "Мащабиране на елементите",
    "Table size": "Размер на таблицата",
    "Interface language": "Език на интерфейса",
    "Restart the app to apply the language change.": "Рестартирайте приложението, за да приложите езиковата промяна.",
    "The interface language has changed. Restart now to apply it?": "Езикът на интерфейса е променен. Да рестартирате ли сега, за да го приложите?",
    "TTS provider": "Доставчик на TTS",
    "Google Cloud credentials": "Уводни данни за Google Cloud",
    "Voice type": "Тип глас",
    "Voice name (optional)": "Име на гласа (по избор)",
    "Read Aloud playback": "Възпроизвеждане при четене на глас",
    "Pause between words (s)": "Пауза между думите (сек)",
    "Repeats per word": "Повторения на дума",
    "Repeats per pair": "Повторения на двойка",
    "Promote status while listening": "Повишаване на статуса при слушане",
    "Listens to reach {status}": "Слушания за достигане на „{status}“",
    "Excel import": "Импортиране на Excel",
    "Placeholder values": "Стойности за запълване",
    "Skip placeholder rows": "Пропускане на редовете с пълнежи",
    "Skip empty rows": "Пропускане на празни редове",
    "Normalize language pairs": "Нормализиране на езиковите двойки",
    "How to import": "Как се импортира",
    "Save import template…": "Запазване на шаблон за импортиране…",
    "Active provider": "Активен доставчик",
    "API key": "API ключ",
    "API URL": "API URL",
    "Check usage": "Проверка на употребата",
    "Enable cloud sync": "Активиране на облачна синхронизация",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase ключ (.env)",
    "Bin cleanup grace (days)": "Срок за пазени в кошчето (дни)",
    "Test Connection": "Тестване на връзката",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "Облачната синхронизация използва ваш собствен Supabase проект. Създайте необходимите таблици веднъж, след което въведете URL адреса и анонимния ключ по-горе.",
    "Copy schema SQL": "Копиране на SQL схемата",
    "Open SQL editor ↗": "Отваряне на SQL редактор ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "SQL схемата е копирана в клипборда. Отворете SQL редактора на вашия Supabase проект, поставете я и натиснете Run, за да създадете таблиците.",
    "Server": "Сървър",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Свързан към вашия собствен Supabase сървър — личен режим, не се изисква акаунт.\n{host}",
    "Use your own Supabase server (personal)": "Използване на ваш собствен Supabase сървър (личен)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Лична синхронизация за един потребител към ваш собствен Supabase проект. Без акаунт или влизане — приложението се свързва с анонимния ключ на проекта. Изпълнете SQL схемата във вашия проект, поставете нейния URL и анонимен ключ по-горе, след което тествайте връзката.\n\nЗабележка: всеки с този URL и ключ може да чете данните, затова пазете проекта поверителен и не споделяйте ключа.",
    "Disconnect — use the built-in server": "Изключване — използване на вградения сървър",
    "Disconnect server": "Изключване на сървъра",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Спиране на синхронизацията с вашия собствен Supabase сървър и връщане към вградения?\n\nВашите думи остават във вашия проект и на това устройство. Ще работите само локално, докато не влезете в акаунт.",
    "Disconnected — using the built-in server.": "Изключено — използва се вграденият сървър.",
    "{host} (personal)": "{host} (личен)",
    "Personal": "Личен",
    "your server": "вашият сървър",
    "Account actions": "Действия с акаунта",
    "Add account…": "Добавяне на акаунт…",
    "Sync this device's data to my account…": "Синхронизиране на данните от това устройство с моя акаунт…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Акаунт",
    "Accounts": "Акаунти",
    "No accounts yet. Add one to sync your words across devices.": "Все още няма акаунти. Добавете такъв, за да синхронизирате думите си между устройствата.",
    "(active)": "(активен)",
    "Sign in": "Вход",
    "(sign in again)": "(влезте отново)",
    "Switch": "Превключване",
    "Remove account": "Премахване на акаунта",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Да се премахне ли {email} от това устройство? Можете да го добавите отново по всяко време — вашите думи остават в облака, а локалното копие остава на диска. Данните ви в облака не се изтриват.",
    "Removed {email} from this device.": "Премахнат е {email} от това устройство.",
    "Your data was exported.": "Данните ви бяха експортирани.",
    "Export failed.": "Експортирането беше неуспешно.",
    "Delete account": "Изтриване на акаунта",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Това ще изтрие завинаги вашия акаунт и ВСИЧКИ ваши синхронизирани думи, текстове и етикети от облака. Вашето локално копие се архивира в папката с резервни копия. Това действие е необратимо.\n\nИскате ли да изтриете акаунта си?",
    "Account deleted.": "Акаунтът е изтрит.",
    "Could not delete the account.": "Акаунтът не можа да бъде изтрит.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Име",
    "Enter your name.": "Въведете вашето име.",
    "Email": "Имейл",
    "Password": "Парола",
    "New password": "Нова парола",
    "6-digit code": "6-цифрен код",
    "or": "или",
    "Sign in with Google": "Вход с Google",
    "Opening your browser to sign in with Google…": "Отваряне на браузъра за влизане с Google…",
    "Forgot password?": "Забравена парола?",
    "Resend code": "Изпращане на кода отново",
    "Confirm your email": "Потвърдете имейла си",
    "Verify code": "Потвърждаване на код",
    "Use a different email": "Използване на друг имейл",
    "Enter your email and password.": "Въведете вашия имейл и парола.",
    "Enter the 6-digit code from the email.": "Въведете 6-цифрения код от имейла.",
    "Enter the code and a new password.": "Въведете кода и нова парола.",
    "Enter your email above first.": "Първо въведете имейла си по-горе.",
    "Enter the reset code we emailed you and a new password.": "Въведете кода за нулиране, който ви изпратихме по имейл, и нова парола.",
    "Enter the 6-digit code we emailed you.": "Въведете 6-цифрения код, който ви изпратихме по имейл.",
    "Reset password": "Нулиране на паролата",
    "Set new password": "Задаване на нова парола",
    "Back to sign in": "Обратно към входа",
    "Sign-in failed.": "Влизането беше неуспешно.",
    "Couldn't send the code.": "Кодът не можа да бъде изпратен.",
    "Done.": "Готово.",
    "Failed.": "Неуспешно.",
    "Create an account": "Създаване на акаунт",
    "Create account": "Създаване на акаунт",
    "I already have an account": "Вече имам акаунт",
    "Signed in as {email}": "Влезли сте като {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Синхронизиране на данните от това устройство с вашия акаунт",
    "your account": "вашия акаунт",
    "This device has {words} and {texts} not yet in {account}.": "Това устройство има {words} и {texts}, които все още не са в {account}.",
    "This device has {words} not yet in {account}.": "Това устройство има {words}, които все още не са в {account}.",
    "This device has {texts} not yet in {account}.": "Това устройство има {texts}, които все още не са в {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Изберете елементите за добавяне. Те се копират във вашия акаунт и се качват в облака, така че да се появят на другите ви устройства. Копието на това устройство се запазва.",
    "Don't ask again for this account": "Не питай повече за този акаунт",
    "{n} word": "{n} дума",
    "{n} words": "{n} думи",
    "{n} text": "{n} текст",
    "{n} texts": "{n} текста",
    "Add {n} item": "Добавяне на {n} елемент",
    "Add {n} items": "Добавяне на {n} елемента",
    # Third plural slot (uk "many"/genitive). ntr() only reads it for Ukrainian,
    # so these are never shown in Bulgarian — kept so the key set stays complete.
    "tags (genitive)": "етикета",
    "changes (genitive)": "промени",
    "deletions (genitive)": "изтривания",
    "{n} words (genitive)": "{n} думи",
    "{n} texts (genitive)": "{n} текста",
    "Add {n} items (genitive)": "Добавяне на {n} елемента",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "Добавен е {n} елемент към вашия акаунт.",
    "Added {n} items to your account.": "Добавени са {n} елемента към вашия акаунт.",
    "Added {n} items to your account. (genitive)": "Добавени са {n} елемента към вашия акаунт.",
    "{n} couldn't be added.": "{n} не можа да бъде добавен.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Сесията ви изтече — влезте отново (Настройки → Синхронизация)",
    "Sign in to sync (Settings → Sync)": "Влезте, за да синхронизирате (Настройки → Синхронизация)",
    "Sign in again to sync": "Влезте отново, за да синхронизирате",
    "Sign in again to use this account.": "Влезте отново, за да използвате този акаунт.",
    "Sync incomplete: {reason}": "Непълна синхронизация: {reason}",
    "Connect to the internet to add local items to your account.": "Свържете се с интернет, за да добавите локални елементи към вашия акаунт.",
    "Everything on this device is already in your account.": "Всичко на това устройство вече е във вашия акаунт.",
    "Upload local words?": "Качване на локалните думи?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Да качите ли текущите си локални думи в този акаунт? Те ще се слеят с данните в облака на този акаунт и ще се синхронизират.\n\nИзберете „Не“, за да запазите съществуващите данни на този акаунт и да отложите локалните си думи (архивирани в папката с резервни копия).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Влизането беше неуспешно. Проверете имейла и паролата си.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Можете да съхранявате до {max} акаунта на това устройство. Премахнете единия, за да добавите друг.",
    "Wrong email or password.": "Грешен имейл или парола.",
    "That doesn't look like a valid email address.": "Това не изглежда като валиден имейл адрес.",
    "Confirm password": "Потвърждение на паролата",
    "Passwords don't match.": "Паролите не съвпадат.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Имейлът ви все още не е потвърден. Въведете 6-цифрения код, който ви изпратихме.",
    "That email is already registered. Try signing in instead.": "Този имейл вече е регистриран. Опитайте да влезете вместо това.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Изпратихме ви 6-цифрен код по имейла. Въведете го, за да завършите регистрацията.",
    "That code didn't work. Check it and try again.": "Този код не проработи. Проверете го и опитайте отново.",
    "If that account exists, a 6-digit reset code is on its way.": "Ако този акаунт съществува, 6-цифрен код за нулиране е на път.",
    "Confirmation email re-sent.": "Имейлът за потвърждение е изпратен отново.",
    "Too many attempts. Please wait a minute and try again.": "Прекалено много опити. Моля, изчакайте минута и опитайте отново.",
    "Your password is too short — use at least 6 characters.": "Паролата ви е твърде кратка — използвайте поне 6 символа.",
    "Sign-ups are disabled on this server.": "Регистрациите са изключени на този сървър.",
    "Can't reach the server. Check your internet connection.": "Няма връзка със сървъра. Проверете интернет връзката си.",
    "Something went wrong.": "Нещо се обърка.",
    "Your saved sign-in for this account expired. Sign in again.": "Запазеното влизане за този акаунт е изтекло. Влезте отново.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "Облачната синхронизация все още не е конфигурирана. Първо добавете Supabase URL и ключ в Настройки → Синхронизация.",
    "Could not start Google sign-in.": "Влизането с Google не можа да бъде стартирано.",
    "Google sign-in was cancelled or timed out.": "Влизането с Google беше отменено или времето му изтече.",
    "Google sign-in failed.": "Влизането с Google беше неуспешно.",
    "Google sign-in failed: {error}": "Влизането с Google беше неуспешно: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Помощникът за локално влизане не можа да се стартира на порт {port} ({error}). Затворете приложението, което го използва, и опитайте отново.",
    "Export my data…": "Експортиране на моите данни…",
    "Delete account…": "Изтриване на акаунта…",
    "Cloud sync is on — your own server ({host})": "Облачната синхронизация е включена — вашият собствен сървър ({host})",
    "Cloud sync is on — signed in as {who}": "Облачната синхронизация е включена — влезли сте като {who}",
    "Cloud sync is off — your words are saved on this device only": "Облачната синхронизация е изключена — думите ви се запазват само на това устройство",
    "(checking…)": "(проверява се…)",
    "(can't connect)": "(няма връзка)",
    "Turn off cloud sync": "Изключване на облачната синхронизация",
    "Cloud sync turned off — this device only.": "Облачната синхронизация е изключена — само това устройство.",
    "Use this server": "Използване на този сървър",
    "Connecting…": "Свързване…",
    "Testing…": "Тестване…",
    "Applying theme…": "Прилагане на тема…",
    "Now syncing with your own server.": "Вече се синхронизира с вашия собствен сървър.",
    "Could not connect to this server:\n{error}": "Свързването с този сървър беше неуспешно:\n{error}",
    "Could not connect to this server.": "Свързването с този сървър беше неуспешно.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nПроверете URL адреса и анонимния ключ, както и дали сте изпълнили SQL схемата там. Да се използват ли тези данни все пак?",
    "Enter your server's URL and anon key first, then test.": "Първо въведете URL адреса и анонимния ключ на сървъра си, след което тествайте.",
    "Enter your server's URL and anon key first.": "Първо въведете URL адреса и анонимния ключ на сървъра си.",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase ключ (анонимен)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Лична синхронизация за един потребител към ваш собствен Supabase проект. Без акаунт или влизане — приложението се свързва с анонимния ключ на проекта. Изпълнете SQL схемата във вашия проект, поставете нейния URL и анонимен ключ по-долу, тествайте го, след което натиснете „Използване на този сървър“.\n\nЗабележка: всеки с този URL и ключ може да чете данните, затова пазете проекта поверителен и не споделяйте ключа.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Спиране на синхронизацията с вашия собствен Supabase сървър и връщане към вградения?\n\nВашите думи остават във вашия проект и на това устройство. Данните за сървъра са запазени, така че можете да се върнете към тях по всяко време. Ще работите само локално, докато не влезете в акаунт.",
    "Start automatically on login (minimized to tray)": "Автоматично стартиране при влизане (минимизирано в системния трей)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "Стартирането при влизане е изключено за Lingueez в настройките на Windows, затова не може да се включи оттук.",
    "Open Windows startup settings": "Отваряне на настройките за стартиране в Windows",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows не приложи тази промяна. Можете сами да включите или изключите Lingueez в Настройки > Приложения > Стартиране.",
    "Add Word hotkey (global)": "Глобален клавишен стил за „Добавяне на дума“",
    "Data format": "Формат на данните",
    "Columns to export": "Колони за експортиране",
    "Sheet name": "Име на лист",
    "Start row": "Начален ред",
    "Start column": "Начална колона",
    "Shade alternate rows": "Засенчване на редуващите се редове",
    "Auto column width": "Автоматична ширина на колоните",
    "Freeze header row": "Фиксиране на реда сa заглавия",
    "Delimiter": "Разделител",
    "Delimiter (\\t = tab)": "Разделител (\\t = табулация)",
    "Include header lines": "Включване на заглавните редове",
    "Header lines": "Заглавни редове",
    "Page size": "Размер на страницата",
    "Font size": "Размер на шрифта",
    "Line spacing (pt)": "Междуредно разстояние (pt)",
    "Text alignment": "Подравняване на текста",
    "Margins L/R/T/B (pt)": "Полета Л/Д/Г/Д (pt)",
    "Automatic widths (fit page)": "Автоматични широчини (побиране в страницата)",
    "Columns / width": "Колони / ширина",
    "Header background": "Фон на заглавната част",
    "Header text": "Текст на заглавната част",
    "Row background": "Фон на реда",
    "Grid lines": "Мрежови линии",
    "Background image": "Фоново изображение",
    "Concurrent workers": "Едновременни работни процеси",
    "Requests per second": "Заявки в секунда",
    "Add font…": "Добавяне на шрифт…",
    "Page && text": "Страница && текст",
    "Columns": "Колони",
    "Max tokens": "Максимум токени",
    "Temperature": "Температура",
    "Prompt template": "Шаблон на подкана",
    "Definitions": "Дефиниции",
    "Generated Texts (from words)": "Генерирани текстове (от думи)",
    "Generated Texts (by topic)": "Генерирани текстове (по тема)",
    "Text Adaptation (to level)": "Адаптация на текст (към ниво)",
    "Thinking budget (0 = off, -1 = auto)": "Бюджет за мислене (0 = изключено, -1 = авто)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Откриване на език",
    "Type a word or phrase…": "Въведете дума или фраза…",
    "Translation…": "Превод…",
    "Pronounce": "Произнеси",
    "Swap word and translation": "Размяна на думата и превода",
    "Translate with DeepL (Enter)": "Превод с DeepL (Enter)",
    "Save Word": "Запазване на думата",
    "Enter a word to translate.": "Въведете дума за превод.",
    "Fill with AI (lemma + best translation)": "Запълване с ИИ (лема + най-добър превод)",
    "Enter a word to fill with AI.": "Въведете дума за запълване с ИИ.",
    "Source equals target — translated to {lang} instead.": "Източникът е равен на целта — вместо това е преведено на {lang}.",
    "Both word and translation are required.": "И думата, и преводът са задължителни.",
    "Please select the source language before saving.": "Моля, изберете езика източник преди запазване.",
    "'{word}' already exists in your dictionary.": "„{word}“ вече съществува в речника ви.",
    "'{word}' is already in your dictionary.": "„{word}“ вече е в речника ви.",
    "Already in your dictionary": "Вече е в речника ви",
    "Show existing": "Показване на съществуващите",
    "The text was truncated to the first 100 words.": "Текстът беше съкратен до първите 100 думи.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Генериране с ИИ",
    "Regenerate with AI": "Генериране отново с ИИ",
    "Definition 2": "Дефиниция 2",
    "No definition yet": "Все още няма дефиниция",
    "Generate one with AI, or write your own with Edit.": "Генерирайте я с ИИ или напишете собствена чрез Редактиране.",
    "There is no word to define.": "Няма дума за дефиниране.",
    "Bold": "Удебелен",
    "Italic": "Курсив",
    "Heading": "Заглавие",
    "List": "Списък",
    "API key missing": "Липсва API ключ",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Първо задайте своя {ai} API ключ в Настройки → Превод и ИИ → ИИ.",
    "Generating definition…": "Генериране на дефиниция…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Етикети — {count} дума/думи",
    "New tag name…": "Име на нов етикет…",
    "Add Tag": "Добавяне на етикет",
    "Apply Selected to All": "Прилагане на избраните за всички",
    "Remove Selected": "Премахване на избраните",
    "(partial)": "(частично)",
    "use(s)": "употреби",
    "Tags marked ✓ apply to all selected words.": (
        "Етикетите, отбелязани с ✓, се прилагат за всички избрани думи."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (частично) означава, че само някои от тях имат етикета."
    ),
    "Select tag(s) in the list first.": "Първо изберете етикет/и в списъка.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Кошче — Изтрити елементи",
    "Delete Permanently": "Изтриване завинаги",
    "Cleanup Old Items…": "Изчистване на стари елементи…",
    "{n} selected": "{n} избрани",
    "The bin is empty. Deleted words will appear here.":
        "Кошчето е празно. Тук ще се появяват изтритите думи.",
    "The bin is empty. Deleted texts will appear here.":
        "Кошчето е празно. Тук ще се появяват изтритите текстове.",
    "deleted {when}": "изтрито {when}",
    "(empty)": "(празно)",
    "Untitled": "Без заглавие",
    "Auto-deletes soon": "Ще се изтрие автоматично скоро",
    "Auto-deletes in {n} day": "Автоматично изтриване след {n} ден",
    "Auto-deletes in {n} days": "Автоматично изтриване след {n} дни",
    "Auto-deletes in {n} days (genitive)": "Автоматично изтриване след {n} дни",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Наистина ли искате да изтриете завинаги {count} елемент/елемента? Това действие е необратимо.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Възстановяване на по-ранна версия",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Базата ви данни се архивира автоматично след всяка промяна. "
        "Изберете по-ранна версия по-долу, за да я възстановите."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Все още няма запазени версии. "
        "Резервно копие се създава автоматично след всяка промяна."
    ),
    "Restore this version": "Възстановяване на тази версия",
    "Today": "Днес",
    "Yesterday": "Вчера",
    "Most recent": "Най-нова",
    "Before your last restore": "Преди последното възстановяване",
    "today": "днес",
    "yesterday": "вчера",
    "today {time}": "днес в {time}",
    "yesterday {time}": "вчера в {time}",
    "the version from {date}": "версията от {date}",
    "the version from just before your last restore": "версията отпреди последното ви възстановяване",
    "Restore Version": "Възстановяване на версия",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Възстановяване на {phrase}?\n\nТекущите ви данни се запазват предварително, така че можете да отмените това."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo." : (
        "Базата ви данни беше възстановена до {phrase}.\n\n"
        "Разколебахте ли се? Възстановете „{before}“, за да отмените."
    ),
    "Restore Error": "Грешка при възстановяване",
    "Sorry, that version could not be restored:\n{error}": "За съжаление тази версия не можа да бъде възстановена:\n{error}",
    "Remove Version": "Премахване на версия",
    "Remove {phrase}?": "Премахване на {phrase}?",
    "Remove Error": "Грешка при премахване",
    "Sorry, that version could not be removed:\n{error}": "За съжаление тази версия не можа да бъде премахната:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Генериране на текст",
    "Title…": "Заглавие…",
    "Generated text appears here…": "Генерираният текст се появява тук…",
    "Save to Texts": "Запазване в текстове",
    "Save failed": "Запазването беше неуспешно",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Запазване като аудио",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Генериране на един MP3 файл от {count} двойка/двойки дума/превод."
    ),
    "Generating audio…": "Генериране на аудио…",
    "Compiling final audio file…": "Компилиране на крайния аудио файл…",
    "Processed: {word}": "Обработено: {word}",
    "Choose File && Start": "Избор на файл && Старт",
    "Cancelled.": "Отменено.",
    "Audio saved": "Аудиото е запазено",
    "Audio file saved to:\n{path}": "Аудио файлът е запазен в:\n{path}",
    "Audio Error": "Аудио грешка",
    "Failed to save audio:\n{error}": "Неуспешно запазване на аудиото:\n{error}",
    "Cancelling…": "Отмяна…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Импортиране от Excel",
    "Row": "Ред",
    "Word 1": "Дума 1",
    "Language 1": "Език 1",
    "Word 2": "Дума 2",
    "Language 2": "Език 2",
    "Action": "Действие",
    "Details": "Подробности",
    "Add": "Добавяне",
    "Update": "Обновяване",
    "Skip": "Пропускане",
    "All": "Всички",
    "To add": "За добавяне",
    "To update": "За обновяване",
    "Skipped": "Пропуснати",
    "Unrecognized": "Неразпознати",
    "Only recognized languages": "Само разпознати езици",
    "Exclude rows whose language wasn't recognized.":
        "Изключване на редовете, чийто език не е бил разпознат.",
    "Unrecognized language — will be imported exactly as written.":
        "Неразпознат език — ще бъде импортиран точно както е написан.",
    "Select all": "Избор на всички",
    "Activity log": "Дневник на активността",
    "Export log…": "Експортиране на дневника…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Експортиране…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Добавяне на текст",
    "Write": "Писане",
    "AI Generate": "ИИ генериране",
    "Wikipedia": "Уикипедия",
    "From URL": "От URL адрес",
    "Language:": "Език:",
    "Level:": "Ниво:",
    "Topic:": "Тема:",
    "Topic…": "Тема…",
    "Adapt to my level": "Адаптиране към моето ниво",
    "Load entries": "Зареждане на записи",
    "Add feed…": "Добавяне на емисия…",
    "Ideas:": "Идеи:",
    "Short (~100 words)": "Кратък (~100 думи)",
    "Medium (~250 words)": "Среден (~250 думи)",
    "Long (~500 words)": "Дълъг (~500 думи)",
    "Travel": "Пътувания",
    "Food": "Храна",
    "Daily routine": "Ежедневие",
    "A short story": "Кратък разказ",
    "News": "Новини",
    "Dialogue at a café": "Диалог в кафене",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Въведете или поставете текста си тук, или изтеглете такъв от табовете по-горе…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Най-новите първи",
    "Oldest first": "Най-старите първи",
    "Title A–Z": "Заглавие А–Я",
    "All languages": "Всички езици",
    "All levels": "Всички нива",
    "All topics": "Всички теми",
    "No matching texts": "Няма съвпадащи текстове",
    "Try a different search or language filter.": "Опитайте друго търсене или езиков филтър.",
    "New text (write or paste)": "Нов текст (напишете или поставете)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Изтегляне на текст от интернет (ИИ / Уикипедия / URL / RSS)"
    ),
    "Import .txt file(s)": "Импортиране на .txt файл/файлове",
    "Read aloud": "Четене на глас",
    "Translate text": "Превод на текст",
    "Hide translation": "Скриване на превода",
    "Focus mode": "Режим на фокус",
    "Exit focus mode": "Изход от режим на фокус",
    "Paper mode: off": "Хартиен режим: изключен",
    "Paper: white (click for sepia)": "Хартия: бяла (кликнете за сепия)",
    "Paper: sepia (click to turn off)": "Хартия: сепия (кликнете за изключване)",
    "Save Changes": "Запазване на промените",
    "Previous text": "Предишен текст",
    "Next text": "Следващ текст",
    "From words: {words}": "От думи: {words}",
    "Created {date}": "Създадено {date}",
    "Unsaved changes": "Незапазени промени",
    "Save changes to '{title}'?": "Да запазя ли промените в „{title}“?",
    "Changes saved.": "Промените са запазени.",
    "'{title}' moved to bin.": "„{title}“ е преместен в кошчето.",
    "Reader": "Четец",
    'Pronounce "{word}"': 'Произнеси „{word}“',
    'Add "{word}" to vocabulary': 'Добави „{word}“ към речника',
    "Read from here": "Четене оттук",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Източник",
    "Added manually": "Добавено ръчно",
    "From reader": "От четеца",
    "Created at": "Създадено на",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Добавяне с ИИ (лема + най-добър превод)",
    "Add to vocabulary as is": "Добавяне към речника както е",
    "Thinking…": "Мислене…",
    "'{pair}' is already in your dictionary.": "„{pair}“ вече е в речника ви.",
    "{label} — {translation} · added": "{label} — {translation} · добавено",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Облачна синхронизация",
    "Last sync": "Последна синхронизация",
    "Pending": "Чакащи",
    "never": "никога",
    "just now": "току-що",
    "{n} min ago": "преди {n} мин",
    "Connected": "Свързан",
    "Not connected": "Няма връзка",
    "change": "промяна",
    "changes": "промени",
    "deletion": "изтриване",
    "deletions": "изтривания",
    "everything synced": "всичко е синхронизирано",
    "Initial sync has not completed yet.": "Първоначалната синхронизация все още не е завършила.",
    "Sync Now": "Синхронизирай сега",
    "Syncing…": "Синхронизиране…",
    # Local-only promo state
    "{words} and {texts}": "{words} и {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Тук сте запазили {items}. Влезте, за да ги пазите сигурни и да учите на всичките си устройства.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Само локално — влезте, за да синхронизирате думите си между устройствата",
    "Sign in to sync across devices": "Влезте за синхронизация между устройства",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Добре дошли",
    "Welcome to {app}": "Добре дошли в {app}",
    "Sync across your devices": "Синхронизиране между вашите устройства",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Влезте, за да пазите речника си в безопасност и да го учите на всяко устройство.",
    "Automatic cloud backup": "Автоматично архивиране в облака",
    "Your words follow you to every computer.":
        "Вашите думи ви следват на всеки компютър.",
    "Never lose your progress.": "Никога не губете своя напредък.",
    "Study anywhere": "Учете навсякъде",
    "Pick up right where you left off.":
        "Продължете точно откъдето спрете.",
    "Your data is yours — sign in only to sync it.":
        "Вашите данни са си ваши — влезте само за да ги синхронизирате.",
    "Sign in / Create account": "Вход / Създаване на акаунт",
    "Continue on this device": "Продължаване на това устройство",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Настройки за възпроизвеждане",
    "Previous word": "Предишна дума",
    "Next word": "Следваща дума",
    "Stop playback": "Спиране на възпроизвеждането",
    "Pause between words": "Пауза между думите",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Няма нищо за четене.",
    "Previous sentence": "Предишно изречение",
    "Next sentence": "Следващо изречение",
    "Reading speed": "Скорост на четене",
    "Sentence {n} / {total}": "Изречение {n} / {total}",
    "buffering…": "буфериране…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Преглед",
    "Learning status": "Статус на учене",
    "Activity": "Активност",
    "Review activity": "Активност при преговор",
    "Breakdown": "Разпределение",
    "Total words": "Общо думи",
    "Mastered": "Овладени",
    "In progress": "В процес",
    "Languages": "Езици",
    "Current streak": "Текуща серия",
    "Added this week": "Добавени тази седмица",
    "Definitions written": "Написани дефиниции",
    "Status distribution": "Разпределение по статус",
    "Words added over time": "Добавени думи във времето",
    "Activity calendar": "Календар на активността",
    "Reviews over time": "Преговори във времето",
    "Review calendar": "Календар на преговорите",
    "Most reviewed words": "Най-преговаряни думи",
    "Top language pairs": "Топ езикови двойки",
    "Top tags": "Топ етикети",
    "Reviewed this week": "Преговорени тази седмица",
    "Total reviews": "Общо преговори",
    "Review streak": "Серия от преговори",
    "{pct}% of all words": "{pct}% от всички думи",
    "actively learning": "активно учене",
    "{n} pairs": "{n} двойки",
    "best {n}d": "най-добра серия {n} дни",
    "{n} today": "{n} днес",
    "listens logged": "записани слушания",
    "keep it going": "продължавайте в същия дух",
    "Day": "Ден",
    "Week": "Седмица",
    "Month": "Месец",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Импортиране на текстови файлове",
    "Text files (*.txt);;All files (*)": "Текстови файлове (*.txt);;Всички файлове (*)",
    "Language of the imported text(s):": "Език на импортирания текст/текстове:",
    "Imported {count} text(s).": "Импортирани са {count} текст/текстове.",
    "Some files could not be imported:": "Някои файлове не можаха да бъдат импортирани:",
    "Import failed:\n{error}": "Неуспешно импортиране:\n{error}",
    "Failed to save text:\n{error}": "Неуспешно запазване на текста:\n{error}",
    "Failed to delete text:\n{error}": "Неуспешно изтриване на текста:\n{error}",
    "Delete Text": "Изтриване на текст",
    "Delete '{title}'?": "Изтриване на „{title}“?",
    "Unsupported language: {language}": "Неподдържан език: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Неподдържан език: {lang}. Изберете такъв от списъка.",
    "(empty)": "(празно)",
    "unsupported language": "неподдържан език",
    "unreadable text": "нечетлив текст",
    "Skipped {n} {noun} ({reasons}).": "Пропуснати {n} {noun} ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Част от текста не можа да бъде прочетена на глас — неподдържан език "
        "или нечетливи символи.",
    "Edit text": "Редактиране на текст",
    "Done editing": "Готово с редактирането",
    "Delete text": "Изтриване на текст",
    "Save Changes": "Запазване на промените",
    "Paper mode": "Хартиен режим",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Кликнете „+“, за да напишете или поставите текст, земното кълбо за изтегляне\n"
        "от интернет, или изберете думи в изгледа Думи\n"
        "и използвайте действието „Текст“, за да генерирате учебен текст."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Търси в Уикипедия на избрания език. Кликнете върху резултат, за да заредите статията; използвайте „Адаптиране към моето ниво“, за да я опростите."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Новинарски емисии за избрания език. Заредете емисия, след това кликнете два пъти върху запис, за да изтеглите пълния му текст. Добавете свои собствени емисии с „Добавяне на емисия…“."
    ),
    "Length:": "Дължина:",
    "Search Wikipedia (in the selected language)…": "Търсене в Уикипедия (на избрания език)…",
    "Double-click an entry to load its full text.": "Кликнете два пъти върху запис, за да заредите пълния му текст.",
    "Working…": "Работа…",
    "Show the {count} result(s) again": "Показване на {count} резултат/резултата отново",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "{ai} API ключът не е зададен. Конфигурирайте го в Настройки → Превод и ИИ → ИИ."
    ),
    "Generating with {ai}…": "Генериране с {ai}…",
    'Fetching "{title}"…': "Изтегляне на „{title}“…",
    "(yours)": "(вашият)",
    "Fetching the full text…": "Изтегляне на пълния текст…",
    "Add feed": "Добавяне на емисия",
    "Feed name:": "Име на емисията:",
    "Feed URL:": "URL на емисията:",
    "Failed to save the text.": "Неуспешно запазване на текста.",
    "Failed to save the text: {error}": "Неуспешно запазване на текста: {error}",
    "'{title}' saved.": "„{title}“ е запазен.",
    "(untitled)": "(без заглавие)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Пренапишете текста по-долу за избраното CEFR ниво с {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Експортиране на дневника",
    "Activity Log": "Дневник на активността",
    "Warnings & errors": "Предупреждения и грешки",
    "Errors only": "Само грешки",
    "Find…": "Търсене…",
    "Open log folder": "Отваряне на папката с дневници",
    "Export diagnostics": "Експортиране на диагностиката",
    "Clear the log file? This cannot be undone.":
        "Изчистване на файла с дневника? Това действие е необратимо.",
    "Could not create the diagnostics file.":
        "Диагностичният файл не можа да бъде създаден.",
    "Diagnostics saved to:\n{path}": "Диагностиката е запазена в:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Опишете проблема**\n\n\n**Стъпки за възпроизвеждане**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nМоля, прикачете диагностичния файл:\n{path}\n",
    "Bug report: ": "Доклад за грешка: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Минимизиране",
    "Maximize": "Максимизиране",
    "Restore": "Възстановяване",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Показване на контролите",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Без цвят",
    "None": "Няма",
    "Choose Color": "Избор на цвят",

    # ── main_window.py (additions) ─────────────────────────────────────────
    "Cloud sync: idle": "Облачна синхронизация: в изчакване",
    "Failed to open table:\n{error}": "Таблицата не можа да бъде отворена:\n{error}",
    "Failed to save template:\n{error}": "Шаблонът не можа да бъде запазен:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Показване / скриване",
    "Excel options": "Опции за Excel",
    "CSV options": "Опции за CSV",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Заглавните редове се записват в горната част на файла — инструменти за импортиране като "
        "Anki ги четат (напр. #separator:tab, #html:true). "
        "Самите имена на колони не се записват."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Копирайте .ttf файл в папката с шрифтове на приложението и го използвайте"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Използва се само при експортиране на думи в MP3 файл. "
        "Самѝят глас се конфигурира в раздела Аудио."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "Гласът, използван навсякъде, където се изговарят думи: Четене на глас в приложението "
        "и MP3 експортиране. gTTS е безплатен и не изисква настройка. Google Cloud TTS "
        "изисква JSON ключ за сервизен акаунт (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) и активирано таксуване за проекта — "
        "използването в рамките на безплатната месечна квота не се таксува."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Пълното изслушване на дума при Четене на глас я изкачва по стълбата на "
        "познаваемостта: Ново → Преговаряне → Учене → Овладено. Всяко "
        "число е общият брой завършени слушания, необходими за достигане на това ниво — "
        "пасивното аудио излагане е слабо, така че високите стойности са нормални. "
        "Думите, които сами сте задали като Овладени или Игнорирани, никога не се променят, "
        "и една дума никога не се понижава в статус."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Запазване на готов .xlsx файл с правилните заглавия и примерни редове"
    ),
    "Google Translate (free)": "Google Translate (безплатно)",
    "Google Translate is free and needs no API key.": (
        "Google Translate е безплатен и не изисква API ключ."
    ),
    "Usage": "Употреба",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Кликнете в полето и натиснете желаната клавишна комбинация — тя отваря "
        "„Добавяне на дума“ със съдържанието на клипборда отвсякъде. "
        "Оставете празно за изключване."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "В Wayland този клавишен стил се регистрира от вашата "
        "обработваща среда и се появява в системните настройки на клавиатурата."
    ),
    "Add Word hotkey": "Клавишна комбинация за „Добавяне на дума“",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Глобалната клавишна комбинация за добавяне на дума не е налична в тази "
        "среда. Вижте Настройки ▸ Система за опции."
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "Глобалната клавишна комбинация за добавяне на дума не е налична в пясъчника "
        "на {sandbox} под Wayland."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Глобалната клавишна комбинация за добавяне на дума все още не се поддържа "
        "в тази Wayland среда."
    ),
    "To enable it, use any one of these:": "За да я активирате, използвайте едно от следните:",
    "Log in to an X11 session instead of Wayland":
        "влезте в X11 сесия вместо Wayland",
    "Use a GNOME session — the global hotkey works there":
        "използвайте GNOME сесия — там глобалната клавишна комбинация работи",
    "Install the AppImage version — it runs outside the sandbox":
        "инсталирайте AppImage версията — тя работи извън пясъчника",
    "Download the AppImage": "Изтегляне на AppImage",
    "Add font…": "Добавяне на шрифт…",
    "TrueType fonts (*.ttf)": "TrueType шрифтове (*.ttf)",
    "Could not copy the font file:\n{error}": "Файлът с шрифта не можа да бъде копиран:\n{error}",
    "Save import template…": "Запазване на шаблон за импортиране…",
    "Excel files (*.xlsx)": "Excel файлове (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Шаблонът е запазен в:\n{path}\n\n"
        "Напълнете го с вашите думи (заменете примерните редове) "
        "и го импортирайте през менюто на приложението → Импортиране на Excel в база данни."
    ),
    "Could not save the template:\n{error}": "Шаблонът не можа да бъде запазен:\n{error}",
    "Background image": "Фоново изображение",
    "Images (*.png *.jpg *.jpeg)": "Изображения (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON файлове (*.json)",
    "Connection successful! ✅": "Успешна връзка! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Свързването не успя. Проверете URL адреса/ключа и интернет връзката си."
    ),
    "Connection test failed:\n{error}": "Тестът на връзката беше неуспешен:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} знака за този период",
    "{count} characters used": "Използвани знаци: {count}",
    "Autostart": "Автостартиране",
    "Could not update autostart entry:\n{error}": "Записът за автостартиране не можа да бъде обновен:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Избран е Google Cloud TTS, но {problem}\n\n"
        "Аудиото ще премине към gTTS, докато това не бъде оправено."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "дума",
    "words": "думи",
    "words (genitive)": "думи",
    "text": "текст",
    "texts": "текстове",
    "texts (genitive)": "текста",
    "tag": "етикет",
    "tags": "етикети",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Превод",
    "AI": "ИИ",
    "Save As": "Запази като",
    "Save Audio As": "Запази аудио като",
    "Save PDF As": "Запази PDF като",
    "Added": "Добавено",
    "Updated": "Обновено",
    "Failed": "Неуспешно",
    "Checking…": "Проверка…",
    "Cleanup": "Почистване",
    "Permanent Delete": "Заобиколено изтриване",
    "No word": "Няма дума",
    "Category": "Категория",
    "Bin": "Кошче",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Всички етикети",
    "Filter by tag — {tag}": "Филтър по етикет — {tag}",
    "(showing first {n})": "(показване на първите {n})",
    "Texts: {total}": "Текстове: {total}",
    "Deleted with {n} error(s).": "Изтрито с {n} грешка/грешки.",
    "Failed to update: {error}": "Неуспешно обновяване: {error}",
    "Failed to export:\n{error}": "Неуспешно експортиране:\n{error}",
    "Failed to export PDF:\n{error}": "Неуспешно експортиране на PDF:\n{error}",
    "Failed to export TXT:\n{error}": "Неуспешно експортиране на TXT:\n{error}",
    "PDF saved to {path}": "PDF файлът е запазен в {path}",
    "TXT file saved to {path}": "TXT файлът е запазен в {path}",
    "Template saved to {path}": "Шаблонът е запазен в {path}",
    "{format} file saved to {path}": "{format} файлът е запазен в {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Използва се gTTS вместо това — {problem}\nОправете го в Настройки → Четене на глас → Аудио."
    ),
    "Failed to load the database:": "Базата данни не можа да бъде заредена:",
    "{selected} of {total} selected": "Избрани {selected} от {total}",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "Свиване на страничната лента",
    "Expand sidebar": "Разширяване на страничната лента",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Запазено {when} · {summary}",
    "the version from {date}": "версията от {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "За съжаление тази версия не можа да бъде възстановена:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "За съжаление тази версия не можа да бъде премахната:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Възстановяване на {count} елемент/елемента?",
    "Restored {count} item(s).": "Възстановени са {count} елемент/елемента.",
    "Select item(s) to restore.": "Изберете елемент/елементи за възстановяване.",
    "Permanently deleted {count} item(s).": "Изтрити завинаги {count} елемент/елемента.",
    "Select item(s) to delete permanently.": "Изберете елемент/елементи за завинаги изтриване.",
    "No items older than {n} days found.": "Няма намерени елементи, по-стари от {n} дни.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Наистина ли да се изтрият завинаги елементите, изтрити преди повече от {days} дни?\n\n"
        "Това действие е необратимо!"
    ),
    "Permanently deleted {count} old item(s).": "Изтрити завинаги {count} стари елемента.",
    "Failed to load deleted items:\n{error}": "Изтритите елементи не можаха да бъдат заредени:\n{error}",
    "Failed to count old items:\n{error}": "Старите елементи не можаха да бъдат преброени:\n{error}",
    "Failed to cleanup:\n{error}": "Почистването беше неуспешно:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Импортиране на Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Очаквани колони: Language1, Language2, Word1, Word2 — наименувани в заглавен ред "
        "или без заглавие с първите четири колони в същия ред. "
        "Готов шаблон е наличен в менюто на приложението → Запазване на шаблон за импортиране."
    ),
    "All ({n})": "Всички ({n})",
    "To add ({n})": "За добавяне ({n})",
    "To update ({n})": "За обновяване ({n})",
    "Skipped ({n})": "Пропуснати ({n})",
    "Unrecognized ({n})": "Неразпознати ({n})",
    " · {n} with unrecognized language": " · {n} с неразпознат език",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} реда: {add} нови · {update} обновления · {skip} пропуснати"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Прегледайте предложените промени, след което импортирайте избраните редове."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Няма нищо за импортиране — няма намерени нови или променени записи."
    ),
    "Analyzing file…": "Анализиране на файла…",
    "Could not read the Excel file — see the activity log.": (
        "Excel файлът не можа да бъде прочетен — вижте дневника на активността."
    ),
    "Analysis failed — see the activity log.": "Анализът беше неуспешен — вижте дневника на активността.",
    "Import failed": "Импортирането неуспешно",
    "Import failed — see the activity log.": "Импортирането беше неуспешно — вижте дневника на активността.",
    "Importing…": "Импортиране…",
    "Importing {count} item(s)…": "Импортиране на {count} елемент/елемента…",
    "Import {count} Item(s)": "Импортиране на {count} елемент/елемента",
    "Import finished:": "Импортирането завърши:",
    "Backup failed — see the activity log.": "Архивирането беше неуспешно — вижте дневника на активността.",
    "{n} added": "добавени: {n}",
    "{n} updated": "обновени: {n}",
    "{n} failed": "неуспешни: {n}",
    "{n} failed.": "{n} неуспешни.",
    "Export Import Log": "Експортиране на дневника за импортиране",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Дефиниция — {word}",
    "Failed to save definition:\n{error}": "Дефиницията не можа да бъде запазена:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Редактиране — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Думата не можа да бъде запазена:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Прикачване на избрания/те етикет/и към всяка избрана дума"
    ),
    "Failed to add tag:\n{error}": "Етикетът не можа да бъде добавен:\n{error}",
    "Failed to apply tags:\n{error}": "Етикетите не можаха да бъдат приложени:\n{error}",
    "Failed to remove tags:\n{error}": "Етикетите не можаха да бъдат премахнати:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Генерира текст с ИИ, използвайки полетата Език, Ниво и Тема по-долу. "
        "Изберете тема или въведете своя собствена."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Генериране на текст на език {language} от {count} дума/думи с {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Въведете или поставете текст в редактора по-долу, дайте му заглавие, "
        "задайте езика — след което запазете."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Извлича четимия текст на статията от всяка уеб страница. "
        "Страници зад вход или изградени изцяло с JavaScript може да не работят."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "Преглед на дефиницията (двоен клик)",
    "Read selected words aloud": "Прочитане на избраните думи на глас",
    "Toggle favorite": "Превключване на любими",
    "Add / remove tags": "Добавяне / премахване на етикети",
    "Edit word": "Редактиране на дума",
    "Copy words": "Копиране на думи",
    "Generate text from selection": "Генериране на текст от селекцията",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "PDF файлове (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excel файлове (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV файлове (*.csv)",
    "Text files (*.txt)": "Текстови файлове (*.txt)",
    "MP3 files (*.mp3)": "MP3 файлове (*.mp3)",
    "Open Excel Table": "Отваряне на Excel таблица",
    "Save Import Template": "Запазване на шаблон за импортиране",

    # Cloud sync status
    "Cloud sync": "Облачна синхронизация",
    "Not connected. Check internet or credentials": "Няма връзка. Проверете интернета или идентификационните данни",
    "Syncing with cloud…": "Синхронизиране с облака…",
    "Sync completed successfully": "Синхронизацията завърши успешно",
    "Sync enabled but not connected. Check settings.": "Синхронизацията е активирана, но няма връзка. Проверете настройките.",
    "idle": "в изчакване",
    "syncing": "синхронизиране",
    "success": "успех",
    "error": "грешка",

    # Chart empty states
    "No data yet": "Все още няма данни",
    "No activity yet": "Все още няма активност",
    "Not enough activity yet": "Все още няма достатъчно активност",

    # Settings tabs
    "APIs": "API-та",
    "Audio (MP3)": "Аудио (MP3)",
    "Sync": "Синхронизация",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI API ключ (.env)",
    "Google API key (.env)": "Google API ключ (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Таксуване на употреба — вземете ключ от <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Модели: gpt-4o-mini, gpt-4o, gpt-4.1-mini… Използване на API — вижте < таблото <a href="https://platform.openai.com/usage">dashboard</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Наличен е безплатен план — вземете ключ от <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Модели: gemini-2.5-flash, gemini-2.5-flash-lite… Използване на API — вижте <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Вземете ключ от <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Използвайте https://api-free.deepl.com/v2/translate за безплатни ключове.',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Подгответе Excel файл с колоните <b>Language1, Language2, Word1, Word2</b> — наименувани така в заглавен ред (излишните колони се игнорират) или без заглавия, като първите четири колони са точно в този ред.</li><li>Отворете менюто на приложението → <i>Импортиране на Excel в база данни…</i> и изберете файла.</li><li>Прегледайте предложените редове и кликнете <i>Импортиране</i>.</li></ol>",

    # About dialog
    "created by": "създадено от",
    "Version": "Версия",
    "Build": "Компилация",
    "Your personal vocabulary companion": "Вашият личен спътник за речник",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Изграждайте, изучавайте и помнете речник на различни езици — с облачна синхронизация, подпомогнати от ИИ дефиниции, преводи, преобразуване на текст в говор и гъвкаво експортиране.",
    "Source code": "Изходен код",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Вашият личен спътник за речник с облачна синхронизация, ИИ дефиниции, преводи, текст към говор и опции за експортиране.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Лицензирано под GNU Affero General Public License v3.0. Тази атрибюция трябва да бъде запазена (AGPL §7).",
    "Found a bug or have an idea?": "Намерихте грешка или имате идея?",
    "Report an issue": "Докладване на проблем",
    "What would you like to report?": "Какво бихте искали да докладвате?",
    "A bug or technical problem": "Грешка или технически проблем",
    "Creates a report with app diagnostics to send to the developers.":
        "Създава доклад с диагностика на приложението за изпращане до разработчиците.",
    "Inappropriate AI-generated content": "Неподходящо съдържание, генерирано от ИИ",
    "Report a definition, text, or translation the AI produced.":
        "Докладвайте дефиниция, текст или превод, генерирани от ИИ.",
    "Report: inappropriate AI-generated content":
        "Доклад: неподходящо съдържание, генерирано от ИИ",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Моля, опишете генерираното от ИИ съдържание, което докладвате.\n\n"
        "Къде се появи (дефиниция / генериран текст / превод на дума):\n"
        "Въпросната дума или текст:\n"
        "Защо е неподходящо:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "За да докладвате неподходящо генерирано от ИИ съдържание, моля, пишете ни на {email}.",

    # Support dialog
    "Support": "Поддръжка",
    "Support Lingueez": "Подкрепете Lingueez",
    "Lingueez is free and open-source.": "Lingueez е безплатно приложение с отворен код.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Ако харесвате Lingueez и ви е полезно, еднократният принос помага за покриване на разходите за сървърите зад незадължителната облачна синхронизация и поддържа по-нататъшното развитие. Няма платена стена — всяка функция остава безплатна във всеки случай.",
    "Support Lingueez's development": "Подкрепете развитието на Lingueez",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Опцията със Stripe е еднократна — без абонамент. Плащанията се обработват сигурно от Stripe или GitHub.",

    # Updates
    "Updates": "Обновявания",
    "Check for updates": "Проверка за обновления",
    "You're up to date.": "Използвате последната версия.",
    "Update available": "Налично е обновление",
    "Update available — v{version}": "Налично е обновление — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Налична е версия Lingueez {version} — вие имате {current}.",
    "Skip this version": "Пропускане на тази версия",
    "Later": "По-късно",
    "Download": "Изтегляне",
    "Check for updates on startup": "Проверка за обновления при стартиране",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Проверява веднъж дневно за по-нова версия и ви уведомява; "
        "нищо никога не се изтегля или инсталира автоматично.",

    # Misc units
    "in": "инч",
    " s": " сек",

    # Word statuses (stored in English; only the displayed label is localized)
    "New": "Ново",
    "To Learn": "За учене",
    "Reviewing": "Преговаряне",
    "Ignored": "Игнорирано",
    "Undo": "Отмени",
    "Restored": "Възстановено",
    "Ignore word": "Игнориране на дума",
    "Ignore this word": "Игнориране на тази дума",
    "Already ignored.": "Вече е игнорирана.",
    "{count} word(s) won't come up in practice.": "{count} дума(и) няма да се появява(т) в упражненията.",
    "'{word}' is back in rotation": "„{word}“ отново участва в упражненията",
    "'{word}' won't come up again": "„{word}“ повече няма да се появява",
    "Mark for relearning": "Отбелязване за повторно учене",
    "Forgot this word — move it to To Learn": "Забравих тази дума — премести в „За учене“",
    "'{word}' is queued to learn again": "„{word}“ е в списъка за повторно учене",
    "{count} word(s) queued to learn again.": "{count} дума(и) за повторно учене.",
    "Nothing here to relearn yet.": "Тук още няма какво да се учи отново.",
    # "Learning" and "Mastered" are translated above.

    # Table density (settings → Table size)
    "Compact": "Компактна",
    "Normal": "Нормална",
    "Comfortable": "Удобна",
    "Spacious": "Просторна",

    # Language names (stored in English as the canonical DeepL/gTTS key;
    # only the displayed label is localized — see app/i18n.py lang_label).
    "English": "Английски",
    "German": "Немски",
    "Spanish": "Испански",
    "Ukrainian": "Украински",
    "French": "Френски",
    "Italian": "Италиански",
    "Portuguese": "Португалски",
    "Russian": "Руски",
    "Greek": "Гръцки",
    "Arabic": "Арабски",
    "Bengali": "Бенгалски",
    "Cantonese": "Кантонски",
    "Hindi": "Хинди",
    "Japanese": "Японски",
    "Korean": "Корейски",
    "Mandarin": "Мандарин",
    "Polish": "Полски",
    "Turkish": "Турски",
    "Vietnamese": "Виетнамски",
    "Afrikaans": "Африкаанс",
    "Albanian": "Албански",
    "Amharic": "Амхарски",
    "Armenian": "Арменски",
    "Azerbaijani": "Азербайджански",
    "Basque": "Баски",
    "Belarusian": "Беларуски",
    "Bosnian": "Босненски",
    "Bulgarian": "Български",
    "Catalan": "Каталонски",
    "Cebuano": "Себуано",
    "Chichewa": "Чичева",
    "Chinese": "Китайски",
    "Croatian": "Хърватски",
    "Czech": "Чешки",
    "Danish": "Датски",
    "Dutch": "Нидерландски",
    "Estonian": "Естонски",
    "Filipino": "Филипински",
    "Finnish": "Финландски",
    "Galician": "Галисийски",
    "Georgian": "Грузински",
    "Gujarati": "Гуджарати",
    "Haitian Creole": "Хаитянски креолски",
    "Hausa": "Хауса",
    "Hawaiian": "Хавайски",
    "Hebrew": "Иврит",
    "Hmong": "Хмонг",
    "Hungarian": "Унгарски",
    "Icelandic": "Исландски",
    "Igbo": "Игбо",
    "Indonesian": "Индонезийски",
    "Irish": "Ирландски",
    "Javanese": "Явански",
    "Kannada": "Каннада",
    "Kazakh": "Казахски",
    "Khmer": "Кхмерски",
    "Kinyarwanda": "Киняруанда",
    "Kyrgyz": "Киргизки",
    "Lao": "Лаоски",
    "Latin": "Латински",
    "Latvian": "Латвийски",
    "Lithuanian": "Литовски",
    "Luxembourgish": "Люксембургски",
    "Macedonian": "Македонски",
    "Malagasy": "Малгашки",
    "Malay": "Малайски",
    "Malayalam": "Малаялам",
    "Maltese": "Малтийски",
    "Maori": "Маорски",
    "Marathi": "Маратхи",
    "Mongolian": "Монголски",
    "Myanmar (Burmese)": "Мианмарски (бирмански)",
    "Nepali": "Непалски",
    "Norwegian": "Норвежки",
    "Odia": "Одия",
    "Pashto": "Пущу",
    "Persian": "Персийски",
    "Punjabi": "Пенджабски",
    "Romanian": "Румънски",
    "Samoan": "Самоански",
    "Scots Gaelic": "Шотландски келтски",
    "Serbian": "Сръбски",
    "Sesotho": "Сесото",
    "Shona": "Шона",
    "Sindhi": "Синдхи",
    "Sinhala": "Синхалски",
    "Slovak": "Словашки",
    "Slovenian": "Словенски",
    "Somali": "Сомалийски",
    "Sundanese": "Сундански",
    "Swahili": "Суахили",
    "Swedish": "Шведски",
    "Tajik": "Таджикски",
    "Tamil": "Тамилски",
    "Tatar": "Татарски",
    "Telugu": "Телугу",
    "Thai": "Тайландски",
    "Turkmen": "Туркменски",
    "Urdu": "Урду",
    "Uyghur": "Уйгурски",
    "Uzbek": "Узбекски",
    "Welsh": "Уелски",
    "Xhosa": "Коса",
    "Yiddish": "Идиш",
    "Yoruba": "Йоруба",
    "Zulu": "Зулуски",
    # --- Onboarding tour ---
    "Back": "Назад",
    "Next": "Напред",
    "Done": "Готово",
    "Show Tour": "Показване на тур",
    "Step {n} of {total}": "Стъпка {n} от {total}",
    "Your library": "Вашата библиотека",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Превключвайте между думи, текстове и статистика от тази странична лента.",
    "Add a word": "Добавяне на дума",
    "Find anything": "Намерете всичко",
    "Search across your words, translations and tags as you type.":
        "Търсете сред думите, преводите и етикетите си докато пишете.",
    "Add a new word here — its translation can be fetched automatically.":
        "Добавете нова дума тук — нейният превод може да бъде изтеглен автоматично.",
    "Listen and learn": "Слушайте и учате",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Изберете думи и натиснете Четене, за да ги чуете на глас. Повтарящото се "
        "слушане изкачва всяка дума от Ново до Преговаряне, Учене "
        "и накрая Овладено.",
    "Generate a text": "Генериране на текст",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Превърнете избраните думи в кратък разказ, написан от ИИ — "
        "вашият речник в контекст.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Речникът ви се синхронизира между устройствата. Кликнете за "
        "статус или за синхронизиране веднага.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Активирайте облачната синхронизация, сменете езика, променете външния вид и "
        "още от Настройки.",
    # --- Texts tour ---
    "Add texts": "Добавяне на текстове",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Напишете или поставете текст, изтеглете такъв от интернет "
        "(ИИ / Уикипедия / URL / RSS) или импортирайте .txt файлове.",
    "Your texts": "Вашите текстове",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Разглеждайте запазените си текстове и ги филтрирайте по език, "
        "ниво или тема.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Слушайте всеки текст на глас — и кликнете върху дума по време на четене, "
        "за да видите нейния превод или да я добавите към речника си.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Показване на паралелен превод едно до друго; изберете езика "
        "със стрелката до него.",
    "Reading modes": "Режими на четене",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Режимът на фокус скрива списъка, хартиеният режим променя "
        "фона, а редактирането ви позволява да промените текста.",
    # --- Flashcards tour ---
    "Choose your deck": "Изберете колода",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Изберете какво да влезе в колодата — карти за преговор, "
        "думи от текущия филтър, най-новите добавки "
        "или ръчно подбрана селекция.",
    "Shape the session": "Оформете сесията",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Задайте колко карти да преговорите, разбъркайте реда им и "
        "направете така, че всяка карта да се произнася при поява и обръщане.",
    "Preview the deck": "Преглед на колодата",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Точно картите, които сесията ви ще съдържа. Кликнете върху плочка, за да "
        "прочетете или редактирате нейната дефиниция, или върху високоговорителя, за да чуете думата.",
    "Review and grade": "Преговор и оценка",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Обърнете всяка карта и оценете колко добре я знаете — Трудно, "
        "Добре или Лесно. Интервалното повтаряне определя кога всяка карта "
        "се връща: лесните думи чакат по-дълго, трудните се връщат "
        "по-скоро. Интервал обръща, 1–3 е оценка.",
    "Or just listen": "Или просто слушайте",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "Изпълнението на колода превръща сесията в аудио — картите напредват "
        "и се обръщат в синхрон с гласа. Паузирайте по всяко време, за да оцените "
        "карта сами.",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Вашият речник с един поглед — общо, овладени думи, "
        "езици и текущата ви серия.",
    "See how your vocabulary has grown over time.":
        "Вижте как речникът ви е нараснал с течение на времето.",
    "Track how much you've reviewed over time.":
        "Проследявайте колко сте преговаряли с течение на времето.",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Пример: Разходка из града",
    "The morning was bright and the streets were quiet. A young woman "
    "walked slowly along the old road, looking at the tall houses and the "
    "small shops that were just opening. She stopped to buy some fresh "
    "bread and a cup of coffee, then crossed the square toward the park. "
    "Children were playing near the river while their parents talked on the "
    "benches nearby. She sat down under a large tree, opened her book, and "
    "began to read. The story was about a traveller who crossed the "
    "mountains in search of an old friend he had not seen for many years. "
    "After a while she looked up, watching the boats drift slowly down the "
    "river and the birds circle high above the rooftops. A street musician "
    "began to play somewhere nearby, and the soft notes followed her "
    "thoughts. It was a calm and happy morning, the kind she liked best.":
        "Сутринта беше ясна, а улиците бяха тихи. Една млада жена "
        "вървеше бавно по стария път, разглеждайки високите къщи и "
        "малките магазини, които току-що отваряха. Тя спря да купи малко прясен "
        "хляб и чаша кафе, след което пресече площада към парка. "
        "Деца играеха близо до реката, докато родителите им разговаряха на "
        "пейките наблизо. Тя седна под голямо дърво, отвори книгата си и "
        "започна да чете. Историята беше за пътешественик, който пресече "
        "планините в търсене на стар приятел, когото не беше виждал от много години. "
        "След малко тя вдигна поглед, наблюдаваща как лодките се носят бавно надолу "
        "по реката и птиците се въртят високо над покривите. Уличен музикант "
        "започна да свири някъде наблизо и меките нотки следваха нейните "
        "мисли. Беше спокойна и щастлива сутрин, каквато тя харесваше най-много.",
    "Demo": "Демо",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Невалиден OpenAI API ключ. Проверете го в Настройки → Превод и ИИ → ИИ → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Във вашия акаунт в OpenAI няма кредити. Добавете кредити в "
        "platform.openai.com/account/billing или превключете ИИ доставчика "
        "на Gemini в Настройки → Превод и ИИ → ИИ.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "Достигнат е лимитът на заявките за OpenAI. Изчакайте малко и опитайте отново.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Непознат OpenAI модел. Проверете името на модела в Настройки → Превод и ИИ → ИИ → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "Не може да се осъществи връзка с OpenAI. Проверете интернет връзката си.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Квотата на Gemini е изчерпана. Безплатният план се нулира ежедневно; изчакайте "
        "или създайте нов ключ на aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Невалиден Google API ключ. Проверете го в Настройки → Превод и ИИ → ИИ → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Непознат модел на Gemini. Проверете името на модела в Настройки → Превод и ИИ → ИИ → Gemini.",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "Вашето пътешествие с речника започва тук",
    "Add your first word — its translation can be fetched automatically.":
        "Добавете първата си дума — нейният превод може да бъде изтеглен автоматично.",
    "Add your first word": "Добавяне на първата дума",
    "Take the tour": "Разгледайте обиколката",
    "No matching words": "Няма съвпадащи думи",
    "Try a different search or filter.": "Опитайте друго търсене или филтър.",
    "Clear filters": "Изчистване на филтрите",
    # --- Texts empty state ---
    "Your reading library starts here": "Вашата библиотека за четене започва тук",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Добавете текст за четене — напишете или поставете ваш собствен, изтеглете от "
        "интернет или импортирайте .txt файл.",
    "Add a text": "Добавяне на текст",
    "Fetch from the Internet": "Изтегляне от интернет",
    "Import .txt": "Импортиране на .txt",
    # demo text-list stub titles
    "My first story": "Моята първа история",
    "A news article": "Новинарска статия",
    "A short poem": "Кратко стихотворение",
    "Travel notes": "Бележки от пътуване",
    # demo text-list stub first sentences (shown as the list snippet)
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Имало едно време в едно малко селце край морето, "
        "живяло любопитно младо лисиче.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Изследователите намериха нов начин да изучават как "
        "езиците се променят и развиват през вековете.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Вятърът върви тихо из есенните дървета, "
        "носещ стари и наполовина забравени песни.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Първи ден: пристигнахме в града късно през нощта и "
        "улиците все още бяха пълни с топла светлина.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Елементи, изтрити на друго устройство",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Докато това устройство беше офлайн, {n} елемент/елемента тук бяха изтрити на вашите "
        "други устройства. Да ги запазите ли в облака, или да ги премахнете от това устройство?",
    "(untitled)": "(без заглавие)",
    "[Text] {title}": "[Текст] {title}",
    "Remove from this device": "Премахване от това устройство",
    "Decide later": "Решаване по-късно",
    "Keep & upload": "Запазване и качване",
    "Not now": "Не сега",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Въведете име за офлайн профила.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Можете да съхранявате до {max} офлайн профила. Премахнете един, за да добавите друг.",
    "New offline profile": "Нов офлайн профил",
    "Profile name:": "Име на профила:",
    "Offline profile": "Офлайн профил",
    "Rename offline profile": "Преименуване на офлайн профила",
    "Offline profiles": "Офлайн профили",
    "Add offline profile…": "Добавяне на офлайн профил…",
    "Profile actions": "Действия с профила",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Отделни библиотеки само за устройството със собствена база данни. Те никога не се синхронизират и не изискват влизане.",
    "Default (local)": "По подразбиране (локален)",
    "Rename": "Преименуване",
    "Delete offline profile": "Изтриване на офлайн профила",
    "Enable cloud sync…": "Активиране на облачна синхронизация…",
    "Could not create the profile.": "Профилът не можа да бъде създаден.",
    "Created and switched to “{name}”.": "Създаден и превключен към „{name}“.",
    "Deleted “{name}”.": "Изтрит „{name}“.",
    "Untitled profile": "Профил без заглавие",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Наистина ли искате да изтриете завинаги офлайн профила „{name}“? Неговите думи и текстове съществуват само на това устройство — няма облачно копие. Базата данни първо се архивира в папката с резервни копия, но това не може да бъде отменено в приложението.",
    "this profile": "този профил",
    "Connect to the internet to merge this profile into your account.": "Свържете се с интернет, за да слеете този профил в акаунта си.",
    "Enable cloud sync for this profile": "Активиране на облачна синхронизация за този профил",
    "Continue": "Продължи",
    "Upload words": "Качване на думи",
    "Upload texts": "Качване на текстове",
    "Upload & sync": "Качване и синхронизиране",
    "Could not upload this profile. Your data is unchanged.": "Този профил не можа да бъде качен. Данните ви са непроменени.",
    "“{name}” is now synced to your account.": "„{name}“ вече е синхронизиран с вашия акаунт.",
    "Everything in this profile is already in your account.": "Всичко в този профил вече е във вашия акаунт.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Влезте или създайте акаунт, за да направите резервно копие на „{name}“ и да го синхронизирате между устройствата си. Думите и текстовете на този профил се качват и той се превръща във вашия синхронизиран акаунт на това устройство. Копие първо се архивира в папката с резервни копия.",
    "Upload “{name}” to your account": "Качване на „{name}“ във вашия акаунт",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Вашият профил става синхронизираният акаунт „{who}“ на това устройство и се качва в облака.",
    "Merge “{name}” into your account": "Сливане на „{name}“ във вашия акаунт",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Този акаунт вече има данни на това устройство. Думите и текстовете от вашия профил, които все още не са там, ще бъдат добавени към него — нищо не се презаписва. След това „{name}“ се архивира в папката с резервни копия и се премахва.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Този профил има {items}, запазени само на това устройство. Активирайте облачната синхронизация, за да направите резервно копие и да учите на всичките си устройства.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Изберете елементите за добавяне. Те се копират във вашия акаунт и се качват в облака. След това „{name}“ се архивира в папката с резервни копия и се премахва.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Съгласен съм с <a href=\"{terms}\">Условията за ползване</a> и <a href=\"{privacy}\">Политиката за поверителност</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Моля, приемете Условията за ползване и Политиката за поверителност, за да продължите.",
    "Updated Terms & Privacy": "Обновени Условия и поверителност",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Обновихме нашите Условия за ползване и Политика за поверителност. Моля, прегледайте ги и ги приемете, за да продължите да използвате акаунта си.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Съгласен съм с обновените <a href=\"{terms}\">Условия за ползване</a> и <a href=\"{privacy}\">Политика за поверителност</a>.",
    "Sign out": "Изход",
    "I agree": "Съгласен съм",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Политика за поверителност</a> · <a href=\"{terms}\">Условия</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Продължавайки, вие се съгласявате с <a href=\"{terms}\">Условията за ползване</a> и <a href=\"{privacy}\">Политиката за поверителност</a>.",
    "Privacy Policy": "Политика за поверителност",
    "Terms": "Условия",
    "Website": "Уебсайт",
    "Contact": "Контакти",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Флаш карти",
    "Practice your vocabulary": "Упражнявайте речника си",
    "Due cards": "Карти за преговор",
    "Current filter": "Текущ филтър",
    "Newest": "Най-нови",
    "Selected words": "Избрани думи",
    "Deck size": "Размер на колодата",
    "Default deck size": "Стандартен размер на колодата",
    "Shuffle": "Разбъркване",
    "Start session": "Начало на сесията",
    "Play deck": "Възпроизвеждане на колодата",
    "{n} cards ready to review": "Карти за преговор: {n}",
    "No cards due — great job!": "Няма карти за преговор — страхотна работа!",
    "{n} selected words": "Избрани думи: {n}",
    "No words to practice.": "Няма думи за упражнение.",
    "End session": "Край на сесията",
    "Listening — pause to review manually":
        "Слушане — пауза за ръчен преговор",
    "Show answer": "Покажи отговора",
    "Hard": "Трудно",
    "Good": "Добре",
    "Easy": "Лесно",
    "Space or click to flip": "Интервал или клик за обръщане",
    "Card {current} of {total}": "Карта {current} от {total}",
    "{n} correct": "Верни: {n}",
    "Session complete!": "Сесията завърши!",
    "You listened to {n} of {total} cards.": "Изслушахте {n} от {total} карти.",
    "Correct: {n} of {total}": "Верни: {n} от {total}",
    "New session": "Нова сесия",
    "Practice hard words": "Упражняване на трудните думи",
    "Hard words": "Трудни думи",
    "Hard words cleared!": "Трудните думи са изчистени!",
    "Open Flashcards when Read Aloud starts":
        "Отваряне на флаш картите при стартиране на четене на глас",
    "Stop": "Стоп",
    "Auto-pronounce": "Автоматично произнасяне",
    "Speak each card as it appears and when it flips":
        "Изговаряне на всяка карта при появата ѝ и при обръщане",
    "Deck preview": "Преглед на колодата",
    "{n} cards": "Карти: {n}",
    "Due": "За преговор",
    "In {n} d": "След {n} д",
    "{n} d": "{n} д",
    "{n} mo": "{n} мес",
    "{n} y": "{n} г",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez за Android…",
    "Android app": "Приложение за Android",
    "Lingueez on Android": "Lingueez на Android",
    "Take your vocabulary with you": "Вземете речника си със себе си",
    "Preview of Lingueez on a phone": "Преглед на Lingueez на телефон",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Влезте с вашия Lingueez акаунт и речникът ви вече е там — "
        "нищо за настройване, нищо за преместване.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Влезте с безплатен Lingueez акаунт и на двете места и речникът ви "
        "се синхронизира с телефона — без файлове за копиране.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Влезте с безплатен Lingueez акаунт и думите ви се синхронизират с телефона.",
    "Synced both ways": "Синхронизирано в двете посоки",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Думите, добавени на телефона, ви чакат на компютъра, и "
        "обратното.",
    "Listen with the screen off": "Слушане при изключен екран",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Контроли на заключения екран, така че преговорът да продължава с телефона "
        "в джоба ви.",
    "Save a word from any app": "Запазване на дума от всяко приложение",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Споделете текст към Lingueez и той попада в речника ви, готов за "
        "попълване по-късно.",
    "Point your phone's camera at the code":
        "Насочете камерата на телефона си към кода",
    "Get it on Google Play": "Изтеглете от Google Play",
    "Copy link": "Копиране на връзката",
    "Link copied": "Връзката е копирана",
    "Lingueez is now on Android": "Lingueez вече е за Android",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Влезте с вашия Lingueez акаунт — речникът ви вече е там.",
    "Dismiss": "Отхвърляне",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Използвайте своя Lingueez акаунт безпроблемно на настолни и Android устройства.",
    "Get the app…": "Вземете приложението…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Тест",
    "Quiz (recall practice)": "Тест (упражнение за припомняне)",
    "Recall your words, one question at a time":
        "Припомнете си думите, въпрос по въпрос",
    "Questions": "Въпроси",
    "Answer with": "Отговаряй с",
    "Choices": "Избор",
    "Typing": "Писане",
    "Ask": "Питай за",
    "Term": "Термин",
    "Mixed": "Смесено",
    "Auto-advance": "Автоматично напред",
    "Move on by itself after a correct answer": "Продължаване само след верен отговор",
    "Speak the question, then the answer once it is revealed":
        "Прочитане на въпроса, а после и на отговора след разкриването му",
    "Start quiz": "Започни теста",
    "questions ready": "въпроса готови",
    "Nothing to quiz": "Няма какво да се пита",
    "No words match this deck.": "Няма думи за това тесте.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Тестът се нуждае от поне две думи — грешните отговори идват точно от думите, "
        "за които не ви питаме.",
    "Not enough words": "Няма достатъчно думи",
    "Add a few more words, or widen the deck.":
        "Добавете още няколко думи или разширете тестето.",
    "Question {n} of {total}": "Въпрос {n} от {total}",
    "Missed words": "Сгрешени думи",
    "End quiz": "Край на теста",
    "Answer in {language}": "Отговорете на език: {language}",
    "Type the answer": "Напишете отговора",
    "Check": "Провери",
    "Click to continue": "Щракнете, за да продължите",
    "See results": "Виж резултатите",
    "Almost — it is \"{answer}\"": "Почти — вярното е „{answer}“",
    "It is \"{answer}\"": "Вярното е „{answer}“",
    "Now {status}": "Сега {status}",
    "Correct": "Верни",
    "Missed": "Сгрешени",
    "Worth another look": "Струва си да се повтори",
    "Again": "Отново",
    "Missed words cleared!": "Сгрешените думи са усвоени!",
    "Perfect run": "Безупречен кръг",
    "Quiz complete": "Тестът е завършен",
    "Practice missed": "Упражни грешките",
    "Default number of questions": "Брой въпроси по подразбиране",
    "Move on after a correct answer": "Продължаване след верен отговор",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Изберете за какво да ви питаме",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Същите тестета като при картите — думи за повторение, текущият ви филтър, "
        "най-новите или ръчно избрани — и колко въпроса.",
    "Choices or typing": "Избор или писане",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "„Избор“ предлага четири отговора; „Писане“ иска да напишете отговора — "
        "по-трудно е, но е по-добрата проверка. Писането прощава ударения и дребни "
        "печатни грешки. „Питай за“ решава коя страна виждате: термина, превода или "
        "смесено.",
    "Start, and it counts": "Започнете — и се брои",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "Лентата показва състава на тестето по статуси. Всеки отговор захранва същия "
        "график за разредено повторение като картите: дума, която сте си спомнили, се "
        "връща по-късно, а сгрешена — по-рано.",
}

# Date names, read by app.i18n. Months are in the genitive case because they
# only appear in formatted dates ("13 юни 2026"). Weekdays start on Monday
# (datetime.weekday(): 0 = Monday).
MONTHS = ["януари", "февруари", "март", "април", "май", "юни",
          "юли", "август", "септември", "октомври", "ноември", "декември"]
MONTHS_ABBR = ["яну", "фев", "мар", "апр", "май", "юни",
               "юли", "авг", "сеп", "окт", "ное", "дек"]
WEEKDAYS = ["Понеделник", "Вторник", "Сряда", "Четвъртък",
            "Петък", "Събота", "Неделя"]
WEEKDAYS_ABBR = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
