# Lingueez — Czech (cs) translations.
# Keys are English UI strings; values are their Czech equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Čeština"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Zrušit",
    "OK": "OK",
    "Close": "Zavřít",
    "Save": "Uložit",
    "Delete": "Smazat",
    "Edit": "Upravit",
    "Remove": "Odebrat",
    "Add": "Přidat",
    "Refresh": "Obnovit",
    "Import": "Importovat",
    "Export": "Exportovat",
    "Search": "Hledat",
    "Fetch": "Načíst",
    "Browse…": "Procházet…",
    "Clear": "Vyčistit",
    "Pause": "Pozastavit",
    "Resume": "Pokračovat",
    "Language": "Jazyk",
    "Translation": "Překlad",
    "Word": "Slovo",
    "Status": "Stav",
    "Error": "Chyba",
    "Title": "Název",
    "Topic": "Téma",
    "Level": "Úroveň",
    "Generate": "Generovat",
    "Generating…": "Generování…",
    "Translating…": "Překládání…",
    "Format": "Formát",
    "Style": "Styl",
    "Model": "Model",
    "Font": "Písmo",
    "Usage": "Využití",
    "Translation language": "Jazyk překladu",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Nabídka",
    "Open Excel Table…": "Otevřít tabulku Excel…",
    "Import Excel to Database…": "Importovat Excel do databáze…",
    "Save Import Template…": "Uložit šablonu importu…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Zvuk (MP3)…",
    "Backups…": "Zálohy…",
    "Show Source column": "Zobrazit sloupec Zdroj",
    "Show Created At column": "Zobrazit sloupec Vytvořeno",
    "Max words…": "Množství slov…",
    "View Log": "Zobrazit protokol",
    "About": "O aplikaci",
    "Quit": "Ukončit",
    "Words": "Slova",
    "Texts": "Texty",
    "Statistics": "Statistika",
    "Bin (deleted items)": "Koš (smazané položky)",
    "Settings": "Nastavení",
    "Vocabulary": "Slovník",
    "Search words, translations or tags…": "Hledat slova, překlady nebo značky…",
    "Search texts by title, content or words…": "Hledat texty podle názvu, obsahu nebo slov…",
    "Search scope": "Rozsah hledání",
    "Search scope…": "Rozsah hledání…",
    "Nothing to practice yet": "Zatím není co procvičovat",
    "Add words to your vocabulary and they show up here.":
        "Přidejte slova do slovníku a objeví se tady.",
    "Come back when cards are due, or practice the newest words now.":
        "Vraťte se, až budou karty na řadě, nebo si teď procvičte nejnovější slova.",
    "Practice newest words": "Procvičit nejnovější slova",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Zvolte výše jiný balíček nebo upravte filtry na stránce Slova.",
    "You're all caught up": "Máte vše hotovo",
    "Add word": "Přidat slovo",
    "Copy a word in any app, then press:":
        "Zkopírujte slovo v jakékoli aplikaci a stiskněte:",
    "Set a shortcut": "Nastavit zkratku",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Zkopírujte slovo v jakékoli aplikaci a stisknutím {keys} ho přidáte i s překladem.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Nastavte zkratku v Nastavení a přidávejte zkopírovaná slova z jakékoli aplikace.",
    " Favorites": " Oblíbené",
    " Filters": " Filtry",
    "Filters that don't fit the table": "Filtry, které se nevejdou do tabulky",
    "More actions": "Další akce",
    "Filter by tag": "Filtrovat podle značky",
    "Close file and return to your vocabulary": "Zavřít soubor a vrátit se do slovníku",
    "Definition": "Definice",
    "Read": "Číst",
    "Favorite": "Oblíbené",
    "Tags": "Značky",
    "Copy": "Kopírovat",
    "Text": "Text",
    "Delete selected (Del)": "Smazat vybrané (Del)",
    "No data": "Žádná data",
    "No texts yet": "Zatím žádné texty",
    "Words: {shown}/{total}": "Slova: {shown}/{total}",
    "Texts: {total}": "Texty: {total}",
    "Texts: {shown}/{total}": "Texty: {shown}/{total}",
    "{count} selected": "{count} vybráno",
    "No selection": "Nic nevybráno",
    "Please select at least one word.": "Vyberte prosím alespoň jedno slovo.",
    "Saved": "Uloženo",
    "'{word}' updated.": "„{word}“ aktualizováno.",
    "Database Error": "Chyba databáze",
    "Delete {count} word(s)?": "Smazat {count} slov(o/a)?",
    "Deleted": "Smazáno",
    "{count} word(s) deleted.": "{count} slov(o/a) smazáno.",
    "Deleted with {n} error(s).": "Smazáno s {n} chybou/chybami.",
    "Favorites": "Oblíbené",
    "{count} word(s) added to favorites.": "{count} slov(o/a) přidáno do oblíbených.",
    "{count} word(s) removed from favorites.": "{count} slov(o/a) odebráno z oblíbených.",
    "Status set to '{status}' for {count} word(s).": "Stav nastaven na „{status}“ pro {count} slov(o/a).",
    "Max Words": "Maximum slov",
    "Show only the first N words (0 = show all):": "Zobrazit pouze prvních N slov (0 = zobrazit vše):",
    "View Definition": "Zobrazit definici",
    "Copy Word": "Kopírovat slovo",
    "Copy Translation": "Kopírovat překlad",
    "Toggle Favorite": "Přepnout oblíbené",
    "Add to favorites": "Přidat k oblíbeným",
    "Remove from favorites": "Odebrat z oblíbených",
    "Tag these words…": "Označit tato slova…",
    "Show less": "Sbalit",
    "Show all {count}": "Zobrazit všech {count}",
    "Change Status…": "Změnit stav…",
    "Add / Remove Tags…": "Přidat / Odebrat značky…",
    "Read Aloud": "Předčítat",
    "Change Status": "Změnit stav",
    "New status:": "Nový stav:",
    "Copied": "Zkopírováno",
    "{count} row(s) copied to clipboard.": "{count} řádek/řádky/řádků zkopírováno do schránky.",
    "{count} item(s) copied to clipboard.": "{count} položka/položky/položek zkopírováno do schránky.",
    "Copy Word(s)": "Kopírovat slovo/slova",
    "Copy Translation(s)": "Kopírovat překlad(y)",
    "Copy Both": "Kopírovat obojí",
    "Search in Word": "Hledat ve slově",
    "Search in Translation": "Hledat v překladu",
    "Search in Tags": "Hledat ve značkách",
    "Promoted": "Povýšeno",
    "Google Cloud TTS unavailable": "Služba Google Cloud TTS není dostupná",
    "Selection limit": "Limit výběru",
    "Only the first 200 selected words will be read.": "Přečteno bude pouze prvních 200 vybraných slov.",
    "Only the first 50 words will be used.": "Použije se pouze prvních 50 slov.",
    "Select words to save as audio.": "Vyberte slova pro uložení jako zvuk.",
    "Nothing to export.": "Nic k exportu.",
    "Export Error": "Chyba exportu",
    "Settings saved.": "Nastavení uloženo.",
    "Generated text saved.": "Vygenerovaný text uložen.",
    "Show": "Zobrazit",
    "Add Word": "Přidat slovo",
    "Stop reading": "Zastavit čtení",
    "Read — Read selected words aloud": "Číst — Přečíst vybraná slova nahlas",
    "Translation": "Překlad",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Vzhled",
    "Audio": "Zvuk",
    "Learning": "Učení",
    "Listening": "Poslech",
    "Backups": "Zálohy",
    "Sync your library?": "Synchronizovat vaši knihovnu?",
    "This will reconcile your device with the cloud:": "Tímto se sladí vaše zařízení s cloudem:",
    "Sync now": "Synchronizovat nyní",
    "Upload": "Nahrát",
    "Synced — ↑{up} ↓{down}": "Synchronizováno — ↑{up} ↓{down}",
    "Upload restored library?": "Nahrát obnovenou knihovnu?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Knihovna obnovena. Při příštím připojení k synchronizačnímu serveru budete požádáni o její nahrání.",
    "Merging this restored backup with your cloud:": "Sloučení této obnovené zálohy s cloudem:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Tato záloha obsahuje {items}. Nahrát a sloučit ji s cloudem nyní, nebo nechat cloud zatím beze změn?",
    "General": "Obecné",
    "Read-aloud": "Předčítání",
    "Translation & AI": "Překlad a AI",
    "Data": "Data",
    "Behavior": "Chování",
    "Progress": "Pokrok",
    "DeepL request failed — using free Google Translate instead.": "Požadavek na DeepL selhal — místo toho se používá bezplatný Google Překladač.",
    "DeepL key isn't set — using free Google Translate instead.": "Klíč DeepL není nastaven — místo toho se používá bezplatný Google Překladač.",
    "System": "Systém",
    "Light": "Světlý",
    "Dark": "Tmavý",
    "Appearance mode": "Režim vzhledu",
    "Widget scaling": "Měřítko prvků",
    "Table size": "Velikost tabulky",
    "Interface language": "Jazyk rozhraní",
    "Restart the app to apply the language change.": "Restartujte aplikaci pro použití změny jazyka.",
    "The interface language has changed. Restart now to apply it?": "Jazyk rozhraní se změnil. Restartovat nyní pro použití změn?",
    "TTS provider": "Poskytovatel TTS",
    "Google Cloud credentials": "Přihlašovací údaje Google Cloud",
    "Voice type": "Typ hlasu",
    "Voice name (optional)": "Název hlasu (volitelné)",
    "Read Aloud playback": "Přehrávání předčítání",
    "Pause between words (s)": "Pauza mezi slovy (s)",
    "Repeats per word": "Opakování na slovo",
    "Repeats per pair": "Opakování na pár",
    "Promote status while listening": "Zvýšit stav při poslechu",
    "Listens to reach {status}": "Počet poslechů pro dosažení stavu „{status}“",
    "Excel import": "Import z Excelu",
    "Placeholder values": "Zástupné hodnoty",
    "Skip placeholder rows": "Přeskočit řádky se zástupnými hodnotami",
    "Skip empty rows": "Přeskočit prázdné řádky",
    "Normalize language pairs": "Normalizovat jazykové páry",
    "How to import": "Jak importovat",
    "Save import template…": "Uložit šablonu importu…",
    "Active provider": "Aktivní poskytovatel",
    "API key": "Klíč API",
    "API URL": "URL rozhraní API",
    "Check usage": "Zkontrolovat využití",
    "Enable cloud sync": "Povolit cloudovou synchronizaci",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase klíč (.env)",
    "Bin cleanup grace (days)": "Lhůta pro vyčištění koše (dny)",
    "Test Connection": "Testovat připojení",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "Cloudová synchronizace používá váš vlastní projekt Supabase. Vytvořte jednou požadované tabulky a poté zadejte URL a anon klíč výše.",
    "Copy schema SQL": "Kopírovat SQL schématu",
    "Open SQL editor ↗": "Otevřít SQL editor ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "SQL schématu zkopírováno do schránky. Otevřete SQL editor vašeho projektu Supabase, vložte kód a klikněte na Run pro vytvoření tabulek.",
    "Server": "Server",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Připojeno k vašemu vlastnímu Supabase serveru — osobní režim, účet není potřeba.\n{host}",
    "Use your own Supabase server (personal)": "Použít vlastní Supabase server (osobní)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Osobní synchronizace pro jednoho uživatele do projektu Supabase, který vlastníte. Není potřeba žádný účet ani přihlášení — aplikace se připojuje pomocí anon klíče projektu. Spusťte SQL schéma ve svém projektu, vložte níže jeho URL a anon klíč a poté klikněte na Testovat připojení.\n\nPoznámka: Kdo má toto URL a klíč, může číst vaše data, proto udržujte projekt soukromý a klíč nesdílejte.",
    "Disconnect — use the built-in server": "Odpojit — použít vestavěný server",
    "Disconnect server": "Odpojit server",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Zastavit synchronizaci s vaším vlastním Supabase serverem a znova použít vestavěný?\n\nVaše slova zůstanou ve vašem projektu a na tomto zařízení. Než se přihlásíte k účtu, budete pracovat pouze lokálně.",
    "Disconnected — using the built-in server.": "Odpojeno — používá se vestavěný server.",
    "{host} (personal)": "{host} (osobní)",
    "Personal": "Osobní",
    "your server": "váš server",
    "Account actions": "Akce účtu",
    "Add account…": "Přidat účet…",
    "Sync this device's data to my account…": "Synchronizovat data tohoto zařízení s mým účtem…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Účet",
    "Accounts": "Účty",
    "No accounts yet. Add one to sync your words across devices.": "Zatím žádné účty. Přidejte jeden pro synchronizaci slov mezi zařízeními.",
    "(active)": "(aktivní)",
    "Sign in": "Přihlásit se",
    "(sign in again)": "(přihlaste se znovu)",
    "Switch": "Přepnout",
    "Remove account": "Odebrat účet",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Odebrat {email} z tohoto zařízení? Můžete jej kdykoli znova přidat — vaše slova zůstanou v cloudu a lokální kopie zůstane na disku. Vaše cloudová data nebudou smazána.",
    "Removed {email} from this device.": "Účet {email} byl odebrán z tohoto zařízení.",
    "Your data was exported.": "Vaše data byla exportována.",
    "Export failed.": "Export selhal.",
    "Delete account": "Smazat účet",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Tímto trvale smažete svůj účet a VŠECHNA vaše synchronizovaná slova, texty a značky z cloudu. Vaše lokální kopie bude zaarchivována do složky záloh. Tuto akci nelze vzít zpět.\n\nSmazat účet?",
    "Account deleted.": "Účet smažen.",
    "Could not delete the account.": "Účet nelze smazat.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Jméno",
    "Enter your name.": "Zadejte své jméno.",
    "Email": "E-mail",
    "Password": "Heslo",
    "New password": "Nové heslo",
    "6-digit code": "6místný kód",
    "or": "nebo",
    "Sign in with Google": "Přihlásit se přes Google",
    "Opening your browser to sign in with Google…": "Otevírá se prohlížeč pro přihlášení přes Google…",
    "Forgot password?": "Zapomněli jste heslo?",
    "Resend code": "Znovu poslat kód",
    "Confirm your email": "Potvrďte svůj e-mail",
    "Verify code": "Ověřit kód",
    "Use a different email": "Použít jiný e-mail",
    "Enter your email and password.": "Zadejte svůj e-mail a heslo.",
    "Enter the 6-digit code from the email.": "Zadejte 6místný kód z e-mailu.",
    "Enter the code and a new password.": "Zadejte kód a nové heslo.",
    "Enter your email above first.": "Nejprve zadejte svůj e-mail výše.",
    "Enter the reset code we emailed you and a new password.": "Zadejte kód pro obnovení z e-mailu a nové heslo.",
    "Enter the 6-digit code we emailed you.": "Zadejte 6místný kód, který jsme vám poslali e-mailem.",
    "Reset password": "Obnovit heslo",
    "Set new password": "Nastavit nové heslo",
    "Back to sign in": "Zpět k přihlášení",
    "Sign-in failed.": "Přihlášení selhalo.",
    "Couldn't send the code.": "Kód nelze odeslat.",
    "Done.": "Hotovo.",
    "Failed.": "Selhalo.",
    "Create an account": "Vytvořit účet",
    "Create account": "Vytvořit účet",
    "I already have an account": "Již mám účet",
    "Signed in as {email}": "Přihlášen jako {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Synchronizovat data tohoto zařízení s vaším účtem",
    "your account": "vůj účet",
    "This device has {words} and {texts} not yet in {account}.": "Toto zařízení obsahuje {words} a {texts}, které ještě nejsou v účtu {account}.",
    "This device has {words} not yet in {account}.": "Toto zařízení obsahuje {words}, které ještě nejsou v účtu {account}.",
    "This device has {texts} not yet in {account}.": "Toto zařízení obsahuje {texts}, které ještě nejsou v účtu {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Vyberte položky, které chcete přidat. Budou zkopírovány do vašeho účtu a nahrány do cloudu, takže se zobrazí na ostatních zařízeních. Kopie na tomto zařízení bude zachována.",
    "Don't ask again for this account": "Příště se u tohoto účtu neptat",
    "{n} word": "{n} slovo",
    "{n} words": "{n} slov(a)",
    "{n} text": "{n} text",
    "{n} texts": "{n} textů",
    "Add {n} item": "Přidat {n} položku",
    "Add {n} items": "Přidat {n} položek",
    "words (genitive)": "slov",
    "texts (genitive)": "textů",
    "tags (genitive)": "značek",
    "changes (genitive)": "změn",
    "deletions (genitive)": "smazání",
    "{n} words (genitive)": "{n} slov",
    "{n} texts (genitive)": "{n} textů",
    "Add {n} items (genitive)": "Přidat {n} položek",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "Přidána {n} položka do vašeho účtu.",
    "Added {n} items to your account.": "Přidáno {n} položek do vašeho účtu.",
    "Added {n} items to your account. (genitive)": "Přidáno {n} položek do vašeho účtu.",
    "{n} couldn't be added.": "Položky ({n}) nebylo možné přidat.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Vaše relace vypršela — přihlaste se znovu (Nastavení → Synchronizace)",
    "Sign in to sync (Settings → Sync)": "Přihlaste se pro synchronizaci (Nastavení → Synchronizace)",
    "Sign in again to sync": "Přihlaste se znovu pro synchronizaci",
    "Sign in again to use this account.": "Přihlaste se znovu pro používání tohoto účtu.",
    "Sync incomplete: {reason}": "Synchronizace nedokončena: {reason}",
    "Connect to the internet to add local items to your account.": "Připojte se k internetu pro přidání lokálních položek do vašeho účtu.",
    "Everything on this device is already in your account.": "Vše na tomto zařízení již ve vašem účtu je.",
    "Upload local words?": "Nahrát lokální slova?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Nahrát vaše aktuální lokální slova do tohoto účtu? Sloučí se s cloudovými daty účtu a synchronizují se.\n\nZvolte Ne, pokud chcete ponechat stávající data účtu a lokální slova odložit (zaarchivují se do složky záloh).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Přihlášení selhalo. Zkontrolujte e-mail a heslo.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Na tomto zařízení můžete mít maximálně {max} účtů. Pro přidání dalšího jeden odeberte.",
    "Wrong email or password.": "Nesprávný e-mail nebo heslo.",
    "That doesn't look like a valid email address.": "Toto nevypadá jako platná e-mailová adresa.",
    "Confirm password": "Potvrďte heslo",
    "Passwords don't match.": "Hesla se neshodují.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Váš e-mail ještě nebyl potvrzen. Zadejte 6místný kód, který jsme vám poslali.",
    "That email is already registered. Try signing in instead.": "Tento e-mail je již zaregistrován. Zkuste se místo toho přihlásit.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Poslali jsme vám e-mailem 6místný kód. Zadejte jej pro dokončení registrace.",
    "That code didn't work. Check it and try again.": "Tento kód nefungoval. Zkontrolujte jej a zkuste to znovu.",
    "If that account exists, a 6-digit reset code is on its way.": "Pokud tento účet existuje, 6místný kód pro obnovení je na cestě.",
    "Confirmation email re-sent.": "Potvrzovací e-mail byl znovu odeslán.",
    "Too many attempts. Please wait a minute and try again.": "Příliš mnoho pokusů. Počkejte prosím minutu a zkuste to znovu.",
    "Your password is too short — use at least 6 characters.": "Vaše heslo je příliš krátké — použijte alespoň 6 znaků.",
    "Sign-ups are disabled on this server.": "Registrace jsou na tomto serveru zakázány.",
    "Can't reach the server. Check your internet connection.": "Nelze se spojit se serverem. Zkontrolujte své připojení k internetu.",
    "Something went wrong.": "Něco se nepovedlo.",
    "Your saved sign-in for this account expired. Sign in again.": "Vaše uložené přihlášení pro tento účet vypršelo. Přihlaste se znovu.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "Cloudová synchronizace ještě není nakonfigurována. Nejprve přidejte URL a klíč Supabase v Nastavení → Synchronizace.",
    "Could not start Google sign-in.": "Přihlášení přes Google nelze spustit.",
    "Google sign-in was cancelled or timed out.": "Přihlášení přes Google bylo zrušeno nebo vypršel jeho časový limit.",
    "Google sign-in failed.": "Přihlášení přes Google selhalo.",
    "Google sign-in failed: {error}": "Přihlášení přes Google selhalo: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Nelze spustit lokálního pomocníka přihlášení na portu {port} ({error}). Zavřete aplikaci, která ho používá, a zkuste to znovu.",
    "Export my data…": "Exportovat moje data…",
    "Delete account…": "Smazat účet…",
    "Cloud sync is on — your own server ({host})": "Cloudová synchronizace je zapnuta — váš vlastní server ({host})",
    "Cloud sync is on — signed in as {who}": "Cloudová synchronizace je zapnuta — přihlášen jako {who}",
    "Cloud sync is off — your words are saved on this device only": "Cloudová synchronizace je vypnuta — vaše slova jsou uložena pouze na tomto zařízení",
    "(checking…)": "(kontrola…)",
    "(can't connect)": "(nelze se připojit)",
    "Turn off cloud sync": "Vypnout cloudovou synchronizaci",
    "Cloud sync turned off — this device only.": "Cloudová synchronizace vypnuta — pouze toto zařízení.",
    "Use this server": "Použít tento server",
    "Connecting…": "Připojování…",
    "Testing…": "Testování…",
    "Applying theme…": "Aplikování motivu…",
    "Now syncing with your own server.": "Nyní se synchronizuje s vaším vlastním serverem.",
    "Could not connect to this server:\n{error}": "Nelze se připojit k tomuto serveru:\n{error}",
    "Could not connect to this server.": "Nelze se připojit k tomuto serveru.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nZkontrolujte URL a anon klíč a ujistěte se, že jste tam spustili SQL schéma. Použít tyto údaje i tak?",
    "Enter your server's URL and anon key first, then test.": "Nejprve zadejte URL svého serveru a anon klíč, poté otestujte.",
    "Enter your server's URL and anon key first.": "Nejprve zadejte URL svého serveru a anon klíč.",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase klíč (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Osobní synchronizace pro jednoho uživatele do projektu Supabase, který vlastníte. Není potřeba účet ani přihlášení — aplikace se připojuje pomocí anon klíče projektu. Spusťte SQL schéma ve svém projektu, vložte níže jeho URL a anon klíč, otestujte ho a poté klikněte na „Použít tento server“.\n\nPoznámka: Kdo má toto URL a klíč, může číst vaše data, proto udržujte projekt soukromý a klíč nesdílejte.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Zastavit synchronizaci s vaším vlastním Supabase serverem a znova použít vestavěný?\n\nVaše slova zůstanou ve vašem projektu a na tomto zařízení. Údaje o serveru budou zapamatovány, takže se můžete kdykoli vrátit. Dokud se nepřihlásíte k účtu, budete pracovat pouze lokálně.",
    "Start automatically on login (minimized to tray)": "Spustit automaticky při přihlášení (při startu zobrazit v liště)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "Spouštění při přihlášení je pro Lingueez vypnuté v Nastavení Windows, takže ho zde nelze zapnout.",
    "Open Windows startup settings": "Otevřít nastavení spouštění ve Windows",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows tuto změnu nepoužil. Lingueez můžete zapnout nebo vypnout sami v Nastavení > Aplikace > Po spuštění.",
    "Add Word hotkey (global)": "Klávesová zkratka „Přidat slovo“ (globální)",
    "Data format": "Formát dat",
    "Columns to export": "Sloupce k exportu",
    "Sheet name": "Název listu",
    "Start row": "Počáteční řádek",
    "Start column": "Počáteční sloupec",
    "Shade alternate rows": "Stínovat střídavě řádky",
    "Auto column width": "Automatická šířka sloupců",
    "Freeze header row": "Ukotvit řádek záhlaví",
    "Delimiter": "Oddělovač",
    "Delimiter (\\t = tab)": "Oddělovač (\\t = tabulátor)",
    "Include header lines": "Zahrnout řádky záhlaví",
    "Header lines": "Řádky záhlaví",
    "Page size": "Velikost stránky",
    "Font size": "Velikost písma",
    "Line spacing (pt)": "Řádkování (pt)",
    "Text alignment": "Zarovnání textu",
    "Margins L/R/T/B (pt)": "Okraje L/P/H/D (pt)",
    "Automatic widths (fit page)": "Automatické šířky (přizpůsobit stránce)",
    "Columns / width": "Sloupce / šířka",
    "Header background": "Pozadí záhlaví",
    "Header text": "Text záhlaví",
    "Row background": "Pozadí řádku",
    "Grid lines": "Mřížka",
    "Background image": "Obrázek na pozadí",
    "Concurrent workers": "Souběžné procesy",
    "Requests per second": "Požadavky za sekundu",
    "Add font…": "Přidat písmo…",
    "Page && text": "Stránka a text",
    "Columns": "Sloupce",
    "Max tokens": "Maximum tokenů",
    "Temperature": "Teplota",
    "Prompt template": "Šablona výzvy",
    "Definitions": "Definice",
    "Generated Texts (from words)": "Vygenerované texty (ze slov)",
    "Generated Texts (by topic)": "Vygenerované texty (podle tématu)",
    "Text Adaptation (to level)": "Adaptace textu (na úroveň)",
    "Thinking budget (0 = off, -1 = auto)": "Rozpočet přemýšlení (0 = vypnuto, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Detekovat jazyk",
    "Type a word or phrase…": "Napište slovo nebo frázi…",
    "Translation…": "Překlad…",
    "Pronounce": "Vyslovit",
    "Swap word and translation": "Prohodit slovo a překlad",
    "Translate with DeepL (Enter)": "Přeložit pomocí DeepL (Enter)",
    "Save Word": "Uložit slovo",
    "Enter a word to translate.": "Zadejte slovo k překladu.",
    "Fill with AI (lemma + best translation)": "Doplnit pomocí AI (lemma + nejlepší překlad)",
    "Enter a word to fill with AI.": "Zadejte slovo k doplnění pomocí AI.",
    "Source equals target — translated to {lang} instead.": "Zdrojový jazyk se shoduje s cílovým — přeloženo místo toho do {lang}.",
    "Both word and translation are required.": "Vyžaduje se slovo i překlad.",
    "Please select the source language before saving.": "Před uložením vyberte zdrojový jazyk.",
    "'{word}' already exists in your dictionary.": "„{word}“ již existuje ve vašem slovníku.",
    "'{word}' is already in your dictionary.": "„{word}“ již ve vašem slovníku je.",
    "Already in your dictionary": "Již ve vašem slovníku",
    "Show existing": "Zobrazit stávající",
    "The text was truncated to the first 100 words.": "Text byl zkrácen na prvních 100 slov.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Vygenerovat pomocí AI",
    "Regenerate with AI": "Znovu vygenerovat pomocí AI",
    "Definition 2": "Definice 2",
    "No definition yet": "Zatím bez definice",
    "Generate one with AI, or write your own with Edit.": "Vygenerujte definici pomocí AI, nebo napište vlastní pomocí Upravit.",
    "There is no word to define.": "Není k dispozici žádné slovo k definování.",
    "Bold": "Tučné",
    "Italic": "Kurzíva",
    "Heading": "Nadpis",
    "List": "Seznam",
    "API key missing": "Chybí klíč API",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Nejprve nastavte svůj klíč API pro {ai} v Nastavení → Překlad a AI → AI.",
    "Generating definition…": "Generování definice…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Značky — {count} slov(o/a)",
    "New tag name…": "Název nové značky…",
    "Add Tag": "Přidat značku",
    "Apply Selected to All": "Použít vybrané na vše",
    "Remove Selected": "Odebrat vybrané",
    "(partial)": "(částečné)",
    "use(s)": "použití",
    "Tags marked ✓ apply to all selected words.": (
        "Značky označené ✓ se použijí na všechna vybraná slova."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (částečné) znamená, že značku mají pouze některá ze slov."
    ),
    "Select tag(s) in the list first.": "Nejprve vyberte značku/značky ze seznamu.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Koš — Smazané položky",
    "Delete Permanently": "Trvale smazat",
    "Cleanup Old Items…": "Vyčistit staré položky…",
    "{n} selected": "{n} vybráno",
    "The bin is empty. Deleted words will appear here.":
        "Koš je prázdný. Zde se zobrazí smazaná slova.",
    "The bin is empty. Deleted texts will appear here.":
        "Koš je prázdný. Zde se zobrazí smazané texty.",
    "deleted {when}": "smazáno {when}",
    "(empty)": "(prázdné)",
    "Untitled": "Bez názvu",
    "Auto-deletes soon": "Brzy bude automaticky smazáno",
    "Auto-deletes in {n} day": "Automatické smazání za {n} den",
    "Auto-deletes in {n} days": "Automatické smazání za {n} dny/dní",
    "Auto-deletes in {n} days (genitive)": "Automatické smazání za {n} dní",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Trvale smazat {count} položku/položky/položek? Tuto akci nelze vzít zpět.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Obnovit starší verzi",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Záloha vaší databáze se vytváří automaticky po každé změně. "
        "Vyberte nižší/starší verzi pro obnovení."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Zatím žádné uložené verze. "
        "Záloha se vytvoří automaticky po každé změně."
    ),
    "Restore this version": "Obnovit tuto verzi",
    "Today": "Dnes",
    "Yesterday": "Včera",
    "Most recent": "Nejnovější",
    "Before your last restore": "Před posledním obnovením",
    "today": "dnes",
    "yesterday": "včera",
    "today {time}": "dnes v {time}",
    "yesterday {time}": "včera v {time}",
    "the version from {date}": "verzi z {date}",
    "the version from just before your last restore": "verzi z doby těsně před posledním obnovením",
    "Restore Version": "Obnovit verzi",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Obnovit {phrase}?\n\nVaše aktuální data budou nejprve uložena, takže tuto akci můžete vrátit zpět."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Vaše databáze byla obnovena na {phrase}.\n\n"
        "Změnili jste názor? Obnovte „{before}“ pro vrácení změn."
    ),
    "Restore Error": "Chyba obnovení",
    "Sorry, that version could not be restored:\n{error}": "Litujeme, tuto verzi nelze obnovit:\n{error}",
    "Remove Version": "Odebrat verzi",
    "Remove {phrase}?": "Odebrat {phrase}?",
    "Remove Error": "Chyba odebrání",
    "Sorry, that version could not be removed:\n{error}": "Litujeme, tuto verzi nelze odebrat:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Generovat text",
    "Title…": "Název…",
    "Generated text appears here…": "Zde se zobrazí vygenerovaný text…",
    "Save to Texts": "Uložit do textů",
    "Save failed": "Uložení selhalo",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Uložit jako zvuk",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Vygenerovat jeden soubor MP3 z {count} páru/párů slovo/překlad."
    ),
    "Generating audio…": "Generování zvuku…",
    "Compiling final audio file…": "Sestavování finálního zvukového souboru…",
    "Processed: {word}": "Zpracováno: {word}",
    "Choose File && Start": "Vybrat soubor a začít",
    "Cancelled.": "Zrušeno.",
    "Audio saved": "Zvuk uložen",
    "Audio file saved to:\n{path}": "Zvukový soubor uložen do:\n{path}",
    "Audio Error": "Chyba zvuku",
    "Failed to save audio:\n{error}": "Zvuk nelze uložit:\n{error}",
    "Cancelling…": "Rušení…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Importovat z Excelu",
    "Row": "Řádek",
    "Word 1": "Slovo 1",
    "Language 1": "Jazyk 1",
    "Word 2": "Slovo 2",
    "Language 2": "Jazyk 2",
    "Action": "Akce",
    "Details": "Podrobnosti",
    "Add": "Přidat",
    "Update": "Aktualizovat",
    "Skip": "Přeskočit",
    "All": "Vše",
    "To add": "K přidání",
    "To update": "K aktualizaci",
    "Skipped": "Přeskočeno",
    "Unrecognized": "Nerozpoznáno",
    "Only recognized languages": "Pouze rozpoznané jazyky",
    "Exclude rows whose language wasn't recognized.":
        "Vyloučit řádky, jejichž jazyk nebyl rozpoznán.",
    "Unrecognized language — will be imported exactly as written.":
        "Nerozpoznaný jazyk — bude importováno přesně tak, jak je napsáno.",
    "Select all": "Vybrat vše",
    "Activity log": "Protokol aktivit",
    "Export log…": "Exportovat protokol…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Exportovat…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Přidat text",
    "Write": "Napsat",
    "AI Generate": "Generovat pomocí AI",
    "Wikipedia": "Wikipedie",
    "From URL": "Z adresy URL",
    "Language:": "Jazyk:",
    "Level:": "Úroveň:",
    "Topic:": "Téma:",
    "Topic…": "Téma…",
    "Adapt to my level": "Přizpůsobit mé úrovni",
    "Load entries": "Načíst položky",
    "Add feed…": "Přidat kanál…",
    "Ideas:": "Nápady:",
    "Short (~100 words)": "Krátký (~100 slov)",
    "Medium (~250 words)": "Střední (~250 slov)",
    "Long (~500 words)": "Dlouhý (~500 slov)",
    "Travel": "Cestování",
    "Food": "Jídlo",
    "Daily routine": "Denní rutina",
    "A short story": "Krátký příběh",
    "News": "Zprávy",
    "Dialogue at a café": "Rozhovor v kavárně",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Zadejte nebo vložte text sem, nebo jej načtěte pomocí záložek výše…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Nejnovější nejdříve",
    "Oldest first": "Nejstarší nejdříve",
    "Title A–Z": "Název A–Z",
    "All languages": "Všechny jazyky",
    "All levels": "Všechny úrovně",
    "All topics": "Všechna témata",
    "No matching texts": "Žádné odpovídající texty",
    "Try a different search or language filter.": "Zkuste jiné vyhledávání nebo filtr jazyka.",
    "New text (write or paste)": "Nový text (napsat nebo vložit)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Získat text z internetu (AI / Wikipedie / URL / RSS)"
    ),
    "Import .txt file(s)": "Importovat soubor(y) .txt",
    "Read aloud": "Předčítat",
    "Translate text": "Přeložit text",
    "Hide translation": "Skrýt překlad",
    "Focus mode": "Režim soustředění",
    "Exit focus mode": "Odejít z režimu soustředění",
    "Paper mode: off": "Režim papíru: vypnuto",
    "Paper: white (click for sepia)": "Papír: bílý (klikněte pro sepiový)",
    "Paper: sepia (click to turn off)": "Papír: sepiový (klikněte pro vypnutí)",
    "Save Changes": "Uložit změny",
    "Previous text": "Předchozí text",
    "Next text": "Následující text",
    "From words: {words}": "Ze slov: {words}",
    "Created {date}": "Vytvořeno {date}",
    "Unsaved changes": "Neuložené změny",
    "Save changes to '{title}'?": "Uložit změny do „{title}“?",
    "Changes saved.": "Změny uloženy.",
    "'{title}' moved to bin.": "„{title}“ přesunuto do koše.",
    "Reader": "Čtečka",
    'Pronounce "{word}"': 'Vyslovit „{word}“',
    'Add "{word}" to vocabulary': 'Přidat „{word}“ do slovníku',
    "Read from here": "Číst odsud",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Zdroj",
    "Added manually": "Přidáno ručně",
    "From reader": "Z čtečky",
    "Created at": "Datum vytvoření",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Přidat pomocí AI (lemma + nejlepší překlad)",
    "Add to vocabulary as is": "Přidat do slovníku tak, jak je",
    "Thinking…": "Přemýšlím…",
    "'{pair}' is already in your dictionary.": "„{pair}“ již ve vašem slovníku je.",
    "{label} — {translation} · added": "{label} — {translation} · přidáno",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Cloudová synchronizace",
    "Last sync": "Poslední synchronizace",
    "Pending": "Čekající",
    "never": "nikdy",
    "just now": "právě teď",
    "{n} min ago": "před {n} min",
    "Connected": "Připojeno",
    "Not connected": "Nepřipojeno",
    "change": "změna",
    "changes": "změny",
    "deletion": "smazání",
    "deletions": "smazání",
    "everything synced": "vše synchronizováno",
    "Initial sync has not completed yet.": "Páteřní/Počáteční synchronizace ještě nebyla dokončena.",
    "Sync Now": "Synchronizovat nyní",
    "Syncing…": "Synchronizace…",
    # Local-only promo state
    "{words} and {texts}": "{words} a {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Uložili jste zde {items}. Přihlaste se, abyste je udrželi v bezpečí a mohli studovat na všech zařízeních.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Pouze lokálně — přihlaste se pro synchronizaci slov mezi zařízeními",
    "Sign in to sync across devices": "Přihlaste se pro synchronizaci napříč zařízeními",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Vítejte",
    "Welcome to {app}": "Vítejte v {app}",
    "Sync across your devices": "Synchronizace napříč zařízeními",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Přihlaste se, abyste uchovali svůj slovník v bezpečí a mohli jej procvičovat na každém zařízení.",
    "Automatic cloud backup": "Automatická cloudová záloha",
    "Your words follow you to every computer.":
        "Vaše slova vás provázejí na každý počítač.",
    "Never lose your progress.": "Nikdy neztrácejte svůj pokrok.",
    "Study anywhere": "Učte se kdekoli",
    "Pick up right where you left off.":
        "Pokračujte přesně tam, kde jste přestali.",
    "Your data is yours — sign in only to sync it.":
        "Vaše data jsou vaše — přihlaste se pouze pro jejich synchronizaci.",
    "Sign in / Create account": "Přihlásit se / Vytvořit účet",
    "Continue on this device": "Pokračovat na tomto zařízení",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Nastavení přehrávání",
    "Previous word": "Předchozí slovo",
    "Next word": "Následující slovo",
    "Stop playback": "Zastavit přehrávání",
    "Pause between words": "Pauza mezi slovy",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Nic k čtení.",
    "Previous sentence": "Předchozí věta",
    "Next sentence": "Následující věta",
    "Reading speed": "Rychlost čtení",
    "Sentence {n} / {total}": "Věta {n} / {total}",
    "buffering…": "načítání paměti…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Přehled",
    "Learning status": "Stav učení",
    "Activity": "Aktivita",
    "Review activity": "Aktivita opakování",
    "Breakdown": "Rozpad",
    "Total words": "Celkem slov",
    "Mastered": "Zvládnuto",
    "In progress": "V procesu",
    "Languages": "Jazyky",
    "Current streak": "Aktuální série",
    "Added this week": "Přidáno tento týden",
    "Definitions written": "Napsané definice",
    "Status distribution": "Rozdělení podle stavu",
    "Words added over time": "Slova přidaná v průběhu času",
    "Activity calendar": "Kalendář aktivit",
    "Reviews over time": "Opakování v průběhu času",
    "Review calendar": "Kalendář opakování",
    "Most reviewed words": "Nejvíce opakovaná slova",
    "Top language pairs": "Nejčastější jazykové páry",
    "Top tags": "Nejčastější značky",
    "Reviewed this week": "Opakováno tento týden",
    "Total reviews": "Celkem opakování",
    "Review streak": "Série opakování",
    "{pct}% of all words": "{pct}% všech slov",
    "actively learning": "aktivně se učím",
    "{n} pairs": "{n} párů",
    "best {n}d": "rekord {n} d.",
    "{n} today": "{n} dnes",
    "listens logged": "zaznamenaných poslechů",
    "keep it going": "jen tak dál!",
    "Day": "Den",
    "Week": "Týden",
    "Month": "Měsíc",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Importovat textové soubory",
    "Text files (*.txt);;All files (*)": "Textové soubory (*.txt);;Všechny soubory (*)",
    "Language of the imported text(s):": "Jazyk importovaného textu/textů:",
    "Imported {count} text(s).": "Importováno {count} textů.",
    "Some files could not be imported:": "Některé soubory se nepodařilo importovat:",
    "Import failed:\n{error}": "Import selhal:\n{error}",
    "Failed to save text:\n{error}": "Text se nepodařilo uložit:\n{error}",
    "Failed to delete text:\n{error}": "Text se nepodařilo smazat:\n{error}",
    "Delete Text": "Smazat text",
    "Delete '{title}'?": "Smazat „{title}“?",
    "Unsupported language: {language}": "Nepodporovaný jazyk: {language}",
    "Unsupported language: {lang}. Pick one from the list.": (
        "Nepodporovaný jazyk: {lang}. Vyberte jeden ze seznamu."
    ),
    "(empty)": "(prázdné)",
    "unsupported language": "nepodporovaný jazyk",
    "unreadable text": "nečitelný text",
    "Skipped {n} {noun} ({reasons}).": "Přeskočeno {n} {noun} ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.": (
        "Některý text nebylo možné přečíst nahlas — nepodporovaný jazyk "
        "nebo nečitelné znaky."
    ),
    "Edit text": "Upravit text",
    "Done editing": "Dokončit úpravy",
    "Delete text": "Smazat text",
    "Save Changes": "Uložit změny",
    "Paper mode": "Režim papíru",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Klikněte na „+“ pro napsání nebo vložení textu, na glóbus pro načtení\n"
        "z internetu, nebo vyberte slova v pohledu Slova a\n"
        "použijte akci „Text“ pro vygenerování studijního textu."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Vyhledává na Wikipedii ve vybraném jazyce. Klikněte na výsledek pro načtení článku; použijte „Přizpůsobit mé úrovni“ pro jeho zjednodušení."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Zpravodajské kanály pro vybraný jazyk. Načtěte kanál a poté poklepáním na položku načtěte její celý text. Přidejte vlastní kanály pomocí „Přidat kanál…“."
    ),
    "Length:": "Délka:",
    "Search Wikipedia (in the selected language)…": "Hledat na Wikipedii (ve vybraném jazyce)…",
    "Double-click an entry to load its full text.": "Dvakrát klikněte na položku pro načtení celého textu.",
    "Working…": "Zpracování…",
    "Show the {count} result(s) again": "Zobrazit znovu {count} výsledků",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "Klíč API pro {ai} není nastaven. Nakonfigurujte jej v Nastavení → Překlad a AI → AI."
    ),
    "Generating with {ai}…": "Generování pomocí {ai}…",
    'Fetching "{title}"…': "Načítání „{title}“…",
    "(yours)": "(vaše)",
    "Fetching the full text…": "Načítání celého textu…",
    "Add feed": "Přidat kanál",
    "Feed name:": "Název kanálu:",
    "Feed URL:": "URL kanálu:",
    "Failed to save the text.": "Text se nepodařilo uložit.",
    "Failed to save the text: {error}": "Text se nepodařilo uložit: {error}",
    "'{title}' saved.": "„{title}“ uloženo.",
    "(untitled)": "(bez názvu)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Přepsat text níže pro vybranou úroveň CEFR pomocí {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Exportovat protokol",
    "Activity Log": "Protokol aktivit",
    "Warnings & errors": "Varování a chyby",
    "Errors only": "Pouze chyby",
    "Find…": "Hledat…",
    "Open log folder": "Otevřít složku protokolu",
    "Export diagnostics": "Exportovat diagnostiku",
    "Clear the log file? This cannot be undone.": (
        "Vyčistit soubor protokolu? Tuto akci nelze vzít zpět."
    ),
    "Could not create the diagnostics file.": (
        "Diagnostický soubor se nepodařilo vytvořit."
    ),
    "Diagnostics saved to:\n{path}": "Diagnostika uložena do:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n": (
        "**Popište problém**\n\n\n**Kroky k reprodukci**\n\n\n---\n"
    ),
    "\nPlease attach the diagnostics file:\n{path}\n": (
        "\nPřipojte prosím diagnostický soubor:\n{path}\n"
    ),
    "Bug report: ": "Hlášení chyby: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Minimalizovat",
    "Maximize": "Maximalizovat",
    "Restore": "Obnovit",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Zobrazit ovládací prvky",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Bez barvy",
    "None": "Žádný",
    "Choose Color": "Vybrat barvu",

    # ── main_window.py (additions) ─────────────────────────────────────────
    "Cloud sync: idle": "Cloudová synchronizace: neaktivní",
    "Failed to open table:\n{error}": "Tabulku se nepodařilo otevřít:\n{error}",
    "Failed to save template:\n{error}": "Šablonu se nepodařilo uložit:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Zobrazit / skrýt",
    "Excel options": "Možnosti Excelu",
    "CSV options": "Možnosti CSV",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Řádky záhlaví se zapisují na začátek souboru — importní nástroje jako "
        "Anki je čtou (např. #separator:tab, #html:true). "
        "Sami názvy sloupců se nezapisují."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Zkopírujte soubor .ttf do složky písem aplikace a použijte jej"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Používá se pouze při exportu slov do souboru MP3. "
        "Samotný hlas se konfiguroval na kartě Zvuk."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "Hlas používaný všude, kde se mluví slova: Předčítání v aplikaci "
        "a export do MP3. gTTS je zdarma a nevyžaduje nastavení. Google Cloud TTS "
        "vyžaduje JSON klíč účtu služby (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) a povolené fakturování u projektu — "
        "využití v rámci bezplatné měsíční kvóty není účtováno."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Úplný poslech slova v Předčítání jej posouvá po žebříčku znalostí "
        "Nové → Opakované → Učení → Zvládnuto. Každé číslo udává celkový počet "
        "dokončených poslechů potřebných k dosažení dané úrovně. Slova, "
        "kterým jste sami nastavili stav Zvládnuto nebo Ignorováno, se nikdy nemění "
        "a slovo se nikdy neposune na nižší úroveň."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Uložit hotový soubor .xlsx se správnými záhlavími a vzorovými řádky"
    ),
    "Google Translate (free)": "Google Translate (zdarma)",
    "Google Translate is free and needs no API key.": (
        "Google Translate je zdarma a nevyžaduje klíč API."
    ),
    "Usage": "Využití",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Klikněte do pole a stiskněte požadovanou kombinaci kláves — otevře "
        "„Přidat slovo“ s obsahem schránky odkudkoli. "
        "Ponechte prázdné pro deaktivaci."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Na Waylandu je tato zkratka registrována ve vašem prostředí "
        "a zobrazuje se v systémovém nastavení klávesnice."
    ),
    "Add Word hotkey": "Klávesová zkratka Přidat slovo",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Globální klávesová zkratka Přidat slovo není v tomto prostředí dostupná. "
        "Možnosti naleznete v Nastavení ▸ Systém."
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "Globální klávesová zkratka Přidat slovo není k dispozici ve {sandbox} "
        "sandboxu na Waylandu."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Globální klávesová zkratka Přidat slovo zatím není v tomto prostředí "
        "Wayland podporována."
    ),
    "To enable it, use any one of these:": "Chcete-li ji povolit, použijte kteroukoli z těchto možností:",
    "Log in to an X11 session instead of Wayland": (
        "Přihlaste se do relace X11 místo Waylandu"
    ),
    "Use a GNOME session — the global hotkey works there": (
        "Použijte relaci GNOME — globální zkratka tam funguje"
    ),
    "Install the AppImage version — it runs outside the sandbox": (
        "Nainstalujte verzi AppImage — běží mimo sandbox"
    ),
    "Download the AppImage": "Stáhnout AppImage",
    "Add font…": "Přidat písmo…",
    "TrueType fonts (*.ttf)": "Písma TrueType (*.ttf)",
    "Could not copy the font file:\n{error}": "Soubor písma nelze zkopírovat:\n{error}",
    "Save import template…": "Uložit šablonu importu…",
    "Excel files (*.xlsx)": "Soubory Excel (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Šablona uložena do:\n{path}\n\n"
        "Vyplňte ji svými slovy (nahraďte vzorové řádky) "
        "a importujte ji přes nabídku aplikace → Importovat Excel do databáze."
    ),
    "Could not save the template:\n{error}": "Šablonu se nepodařilo uložit:\n{error}",
    "Background image": "Obrázek na pozadí",
    "Images (*.png *.jpg *.jpeg)": "Obrázky (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "Soubory JSON (*.json)",
    "Connection successful! ✅": "Připojení úspěšné! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Nelze se připojit. Zkontrolujte URL/klíč a vaše internetové připojení."
    ),
    "Connection test failed:\n{error}": "Test připojení selhal:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} znaků za toto období",
    "{count} characters used": "{count} znaků použito",
    "Autostart": "Automatické spuštění",
    "Could not update autostart entry:\n{error}": "Položku automatického spuštění nelze aktualizovat:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Je vybrána služba Google Cloud TTS, ale {problem}\n\n"
        "Zvuk bude zálohován pomocí gTTS, dokud to nebude opraveno."
    ),

    # ── Count nouns ────────────────────────────────────────────────────────
    "word": "slovo",
    "words": "slova",
    "words (genitive)": "slov",
    "text": "text",
    "texts": "texty",
    "texts (genitive)": "textů",
    "tag": "značka",
    "tags": "značky",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Přeložit",
    "AI": "AI",
    "Save As": "Uložit jako",
    "Save Audio As": "Uložit zvuk jako",
    "Save PDF As": "Uložit PDF jako",
    "Added": "Přidáno",
    "Updated": "Aktualizováno",
    "Failed": "Selhalo",
    "Checking…": "Kontrola…",
    "Cleanup": "Vyčištění",
    "Permanent Delete": "Trvalé smazání",
    "No word": "Žádné slovo",
    "Category": "Kategorie",
    "Bin": "Koš",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Všechny značky",
    "Filter by tag — {tag}": "Filtrovat podle značky — {tag}",
    "(showing first {n})": "(zobrazeno prvních {n})",
    "Texts: {total}": "Texty: {total}",
    "Deleted with {n} error(s).": "Smazáno s {n} chybou/chybami.",
    "Failed to update: {error}": "Nelze aktualizovat: {error}",
    "Failed to export:\n{error}": "Nelze exportovat:\n{error}",
    "Failed to export PDF:\n{error}": "Nelze exportovat PDF:\n{error}",
    "Failed to export TXT:\n{error}": "Nelze exportovat TXT:\n{error}",
    "PDF saved to {path}": "PDF uloženo do {path}",
    "TXT file saved to {path}": "TXT soubor uložen do {path}",
    "Template saved to {path}": "Šablona uložena do {path}",
    "{format} file saved to {path}": "Soubor {format} uložen do {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Místo toho se používá gTTS — {problem}\nOpravte to v Nastavení → Předčítání → Zvuk."
    ),
    "Failed to load the database:": "Databázi se nepodařilo načíst:",
    "{selected} of {total} selected": "{selected} z {total} vybráno",
    "Collapse sidebar": "Sbalit postranní panel",
    "Expand sidebar": "Rozbalit postranní panel",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Uloženo {when} · {summary}",
    "the version from {date}": "verzi z {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Litujeme, tuto verzi nelze obnovit:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Litujeme, tuto verzi nelze odebrat:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Obnovit {count} položku/položky/položek?",
    "Restored {count} item(s).": "Obnoveno {count} položek.",
    "Select item(s) to restore.": "Vyberte položku/položky k obnovení.",
    "Permanently deleted {count} item(s).": "Trvale smazáno {count} položek.",
    "Select item(s) to delete permanently.": "Vyberte položku/položky k trvalému smazání.",
    "No items older than {n} days found.": "Nebyly nalezeny žádné položky starší než {n} dní.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Trvale smazat položky smazané před více než {days} dny?\n\n"
        "Tuto akci nelze vzít zpět!"
    ),
    "Permanently deleted {count} old item(s).": "Trvale smazáno {count} starých položek.",
    "Failed to load deleted items:\n{error}": "Smazané položky se nepodařilo načíst:\n{error}",
    "Failed to count old items:\n{error}": "Staré položky se nepodařilo spočítat:\n{error}",
    "Failed to cleanup:\n{error}": "Vyčištění selhalo:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Importovat Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Očekávané sloupce: Language1, Language2, Word1, Word2 — pojmenované v řádku záhlaví, "
        "nebo bez záhlaví s prvními čtyřmi sloupci v tomto pořadí. "
        "Hotová šablona je k dispozici v nabídce aplikace → Uložit šablonu importu."
    ),
    "All ({n})": "Vše ({n})",
    "To add ({n})": "K přidání ({n})",
    "To update ({n})": "K aktualizaci ({n})",
    "Skipped ({n})": "Přeskočeno ({n})",
    "Unrecognized ({n})": "Nerozpoznáno ({n})",
    " · {n} with unrecognized language": " · {n} s nerozpoznaným jazykem",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} řádků: {add} nových · {update} aktualizací · {skip} přeskočeno"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Zkontrolujte navržené změny a poté importujte vybrané řádky."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Nic k importu — nebyly nalezeny žádné nové nebo změněné záznamy."
    ),
    "Analyzing file…": "Analýza souboru…",
    "Could not read the Excel file — see the activity log.": (
        "Soubor Excel nelze přečíst — viz protokol aktivit."
    ),
    "Analysis failed — see the activity log.": "Analýza selhala — viz protokol aktivit.",
    "Import failed": "Import selhal",
    "Import failed — see the activity log.": "Import selhal — viz protokol aktivit.",
    "Importing…": "Importování…",
    "Importing {count} item(s)…": "Importování {count} položek…",
    "Import {count} Item(s)": "Importovat {count} položek",
    "Import finished:": "Import dokončen:",
    "Backup failed — see the activity log.": "Zálohování selhalo — viz protokol aktivit.",
    "{n} added": "{n} přidáno",
    "{n} updated": "{n} aktualizováno",
    "{n} failed": "{n} selhalo",
    "{n} failed.": "{n} selhalo.",
    "Export Import Log": "Exportovat protokol importu",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Definice — {word}",
    "Failed to save definition:\n{error}": "Definici se nepodařilo uložit:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Upravit — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Slovo se nepodařilo uložit:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Připojit vybrané značky ke všem vybraným slovům"
    ),
    "Failed to add tag:\n{error}": "Značku se nepodařilo přidat:\n{error}",
    "Failed to apply tags:\n{error}": "Značky se nepodařilo použít:\n{error}",
    "Failed to remove tags:\n{error}": "Značky se nepodařilo odebrat:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Generuje text pomocí AI na základě polí Jazyk, Úroveň a Téma níže. "
        "Vyberte tématickou značku nebo napište vlastní."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Generování textu v jazyce {language} z {count} slov(a) pomocí {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Napište nebo vložte text do editoru níže, přidejte název, "
        "nastavte jazyk — a uložte."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Extrahujeme čitelný text článku z jakékoli webové stránky. "
        "Stránky chráněné přihlášením nebo vytvořené pouze pomocí JavaScriptu nemusí fungovat."
    ),

    # ── Tooltips & Filters ─────────────────────────────────────────────────
    "View definition (double-click)": "Zobrazit definici (poklepáním)",
    "Read selected words aloud": "Přečíst vybraná slova nahlas",
    "Toggle favorite": "Přepnout oblíbené",
    "Add / remove tags": "Přidat / odebrat značky",
    "Edit word": "Upravit slovo",
    "Copy words": "Kopírovat slova",
    "Generate text from selection": "Vygenerovat text z výběru",
    "PDF files (*.pdf)": "Soubory PDF (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Soubory Excel (*.xlsx *.xls)",
    "CSV files (*.csv)": "Soubory CSV (*.csv)",
    "Text files (*.txt)": "Textové soubory (*.txt)",
    "MP3 files (*.mp3)": "Soubory MP3 (*.mp3)",
    "Open Excel Table": "Otevřít tabulku Excel",
    "Save Import Template": "Uložit šablonu importu",

    # Cloud sync status
    "Cloud sync": "Cloudová synchronizace",
    "Not connected. Check internet or credentials": "Nepřipojeno. Zkontrolujte internet nebo přihlašovací údaje",
    "Syncing with cloud…": "Synchronizace s cloudem…",
    "Sync completed successfully": "Synchronizace byla úspěšně dokončena",
    "Sync enabled but not connected. Check settings.": "Synchronizace povolena, ale není připojeno. Zkontrolujte nastavení.",
    "idle": "neaktivní",
    "syncing": "synchronizuje se",
    "success": "úspěch",
    "error": "chyba",

    # Chart empty states
    "No data yet": "Zatím žádná data",
    "No activity yet": "Zatím žádná aktivita",
    "Not enough activity yet": "Zatím nedostatek aktivity",

    # Settings tabs
    "APIs": "API",
    "Audio (MP3)": "Zvuk (MP3)",
    "Sync": "Synchronizace",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI API klíč (.env)",
    "Google API key (.env)": "Google API klíč (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Účtováno dle použití — získejte klíč na <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modely: gpt-4o-mini, gpt-4o, gpt-4.1-mini… Využití API — viz <a href="https://platform.openai.com/usage">přehled</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'K dispozici je bezplatná verze — získejte klíč na <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modely: gemini-2.5-flash, gemini-2.5-flash-lite… Využití API — viz <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Získejte klíč na <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Pro bezplatné klíče použijte https://api-free.deepl.com/v2/translate.',

    # Excel import help
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Připravte soubor Excel se sloupci <b>Language1, Language2, Word1, Word2</b> — pojmenovanými v řádku záhlaví (další sloupce se ignorují), nebo bez záhlaví s prvními čtyřmi sloupci přesně v tomto pořadí.</li><li>Otevřete nabídku aplikace → <i>Importovat Excel do databáze…</i> a vyberte soubor.</li><li>Zkontrolujte navržené řádky a klikněte na <i>Importovat</i>.</li></ol>",

    # About dialog
    "created by": "vytvořil",
    "Version": "Verze",
    "Build": "Sestavení",
    "Your personal vocabulary companion": "Váš osobní slovníkový společník",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Budujte, studujte a pamatujte si slovní zásobu napříč jazyky — s cloudovou synchronizací, definicemi pomocí AI, překlady, převodem textu na řeč a flexibilním exportem.",
    "Source code": "Zdrojový kód",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Váš osobní slovníkový společník s cloudovou synchronizací, AI definicemi, překlady, převodem textu na řeč a možnostmi exportu.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Licencováno pod GNU Affero General Public License v3.0. Toto uvedení autora musí být zachováno (AGPL §7).",
    "Found a bug or have an idea?": "Našli jste chybu nebo máte nápad?",
    "Report an issue": "Nahlásit problém",
    "What would you like to report?": "Co chcete nahlásit?",
    "A bug or technical problem": "Chybu nebo technický problém",
    "Creates a report with app diagnostics to send to the developers.":
        "Vytvoří hlášení s diagnostikou aplikace pro odeslání vývojářům.",
    "Inappropriate AI-generated content": "Nevhodný obsah vygenerovaný AI",
    "Report a definition, text, or translation the AI produced.":
        "Nahlásit definici, text nebo překlad vygenerovaný AI.",
    "Report: inappropriate AI-generated content":
        "Hlášení: nevhodný obsah vygenerovaný AI",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Popište prosím obsah vygenerovaný AI, který hlásíte.\n\n"
        "Kde se objevil (definice / vygenerovaný text / překlad slova):\n"
        "Dotyčné slovo nebo text:\n"
        "Proč je nevhodný:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "Chcete-li nahlásit nevhodný obsah vygenerovaný AI, napište nám na e-mail {email}.",

    # Support dialog
    "Support": "Podpora",
    "Support Lingueez": "Podpořit Lingueez",
    "Lingueez is free and open-source.": "Lingueez je zdarma a je open-source.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Pokud se vám Lingueez líbí a je pro vás užitečný, jednorázový příspěvek pomůže pokrýt náklady na servery pro volitelnou cloudovou synchronizaci a podpoří další vývoj. Neexistuje žádný placený obsah — každá funkce zůstává v každém případě zdarma.",
    "Support Lingueez's development": "Podpořit vývoj aplikace Lingueez",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Možnost Stripe je jednorázová — žádné předplatné. Platby jsou bezpečně zpracovány přes Stripe nebo GitHub.",

    # Updates
    "Updates": "Aktualizace",
    "Check for updates": "Zkontrolovat aktualizace",
    "You're up to date.": "Aplikace je aktuální.",
    "Update available": "Dostupná aktualizace",
    "Update available — v{version}": "Dostupná aktualizace — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Je k dispozici verze Lingueez {version} — vy máte {current}.",
    "Skip this version": "Přeskočit tuto verzi",
    "Later": "Později",
    "Download": "Stáhnout",
    "Check for updates on startup": "Zkontrolovat aktualizace při spuštění",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Jednou denně zkontroluje novější verzi a dá vám vědět; "
        "nic se automaticky nestahuje ani neinstaluje.",

    # Misc units
    "in": "palec",
    " s": " s",

    # Word statuses
    "New": "Nové",
    "To Learn": "K učení",
    "Reviewing": "Opakované",
    "Ignored": "Ignorováno",
    "Undo": "Zpět",
    "Restored": "Obnoveno",
    "Ignore word": "Ignorovat slovo",
    "Ignore this word": "Ignorovat toto slovo",
    "Already ignored.": "Již ignorováno.",
    "{count} word(s) won't come up in practice.": "{count} slovo/slova se už neobjeví v procvičování.",
    "'{word}' is back in rotation": "„{word}“ se vrací do procvičování",
    "'{word}' won't come up again": "„{word}“ se už neobjeví",
    "Mark for relearning": "Označit k opětovnému učení",
    "Forgot this word — move it to To Learn": "Zapomenuté slovo — přesunout do „K učení“",
    "'{word}' is queued to learn again": "„{word}“ je zařazeno k opětovnému učení",
    "{count} word(s) queued to learn again.": "{count} slovo/slova zařazeno k opětovnému učení.",
    "Nothing here to relearn yet.": "Zatím tu není co se učit znovu.",

    # Table density
    "Compact": "Kompaktní",
    "Normal": "Normální",
    "Comfortable": "Pohodlné",
    "Spacious": "Prostorné",

    # Language names
    "English": "Angličtina",
    "German": "Němčina",
    "Spanish": "Španělština",
    "Ukrainian": "Ukrajinština",
    "French": "Francouzština",
    "Italian": "Italština",
    "Portuguese": "Portugalština",
    "Russian": "Ruština",
    "Greek": "Řečtina",
    "Arabic": "Arabština",
    "Bengali": "Bengálština",
    "Cantonese": "Kantonština",
    "Hindi": "Hindština",
    "Japanese": "Japonština",
    "Korean": "Korejština",
    "Mandarin": "Mandarínština",
    "Polish": "Polština",
    "Turkish": "Turečtina",
    "Vietnamese": "Vietnamština",
    "Afrikaans": "Afrikánština",
    "Albanian": "Albánština",
    "Amharic": "Amharština",
    "Armenian": "Arménština",
    "Azerbaijani": "Ázerbájdžánština",
    "Basque": "Baskičtina",
    "Belarusian": "Běloruština",
    "Bosnian": "Bosensko",
    "Bulgarian": "Bulharština",
    "Catalan": "Katalánština",
    "Cebuano": "Cebuanština",
    "Chichewa": "Čičevština",
    "Chinese": "Čínština",
    "Croatian": "Chorvatština",
    "Czech": "Čeština",
    "Danish": "Dánština",
    "Dutch": "Nizozemština",
    "Estonian": "Estonština",
    "Filipino": "Filipínština",
    "Finnish": "Finština",
    "Galician": "Galicijština",
    "Georgian": "Gruzínština",
    "Gujarati": "Gudžarátština",
    "Haitian Creole": "Haitská kreolština",
    "Hausa": "Hausština",
    "Hawaiian": "Havajština",
    "Hebrew": "Hebrejština",
    "Hmong": "Hmongština",
    "Hungarian": "Maďarština",
    "Icelandic": "Islandština",
    "Igbo": "Igboština",
    "Indonesian": "Indonéština",
    "Irish": "Irština",
    "Javanese": "Jávština",
    "Kannada": "Kannadština",
    "Kazakh": "Kazaština",
    "Khmer": "Khmérština",
    "Kinyarwanda": "Rwandština",
    "Kyrgyz": "Kyrgyzština",
    "Lao": "Laoština",
    "Latin": "Latina",
    "Latvian": "Lotyština",
    "Lithuanian": "Litovština",
    "Luxembourgish": "Lucemburština",
    "Macedonian": "Makedonština",
    "Malagasy": "Malagsaština",
    "Malay": "Malajština",
    "Malayalam": "Malajálamština",
    "Maltese": "Maltština",
    "Maori": "Maorština",
    "Marathi": "Maráthština",
    "Mongolian": "Mongolština",
    "Myanmar (Burmese)": "Barmanština",
    "Nepali": "Nepálština",
    "Norwegian": "Norština",
    "Odia": "Orijština",
    "Pashto": "Paštština",
    "Persian": "Persko",
    "Punjabi": "Pandžábština",
    "Romanian": "Rumunština",
    "Samoan": "Samojština",
    "Scots Gaelic": "Skotská gaelština",
    "Serbian": "Srbština",
    "Sesotho": "Sesothština",
    "Shona": "Shonština",
    "Sindhi": "Sindhština",
    "Sinhala": "Sinhálština",
    "Slovak": "Slovenština",
    "Slovenian": "Slovinština",
    "Somali": "Somálština",
    "Sundanese": "Sundština",
    "Swahili": "Svahilština",
    "Swedish": "Švédština",
    "Tajik": "Tádžičtina",
    "Tamil": "Tamilština",
    "Tatar": "Tatarština",
    "Telugu": "Telugština",
    "Thai": "Thajština",
    "Turkmen": "Turkmenština",
    "Urdu": "Urdština",
    "Uyghur": "Ujgurština",
    "Uzbek": "Uzbečtina",
    "Welsh": "Velština",
    "Xhosa": "Xhoština",
    "Yiddish": "Jidiš",
    "Yoruba": "Jorubština",
    "Zulu": "Zuluština",

    # --- Onboarding tour ---
    "Back": "Zpět",
    "Next": "Dále",
    "Done": "Hotovo",
    "Show Tour": "Zobrazit prohlídku",
    "Step {n} of {total}": "Krok {n} z {total}",
    "Your library": "Vaše knihovna",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Přepínejte mezi Slovy, Texty a Statistikami z tohoto postranního panelu.",
    "Add a word": "Přidat slovo",
    "Find anything": "Najděte cokoli",
    "Search across your words, translations and tags as you type.":
        "Vyhledávejte ve svých slovech, překladech a značkách během psaní.",
    "Add a new word here — its translation can be fetched automatically.":
        "Zde přidejte nové slovo — jeho překlad lze načíst automaticky.",
    "Listen and learn": "Poslouchejte a učte se",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Vyberte slova a stiskněte Číst pro jejich předčítání. Opakovaný "
        "poslech posouvá každé slovo z Nového na Opakované, Učení "
        "a nakonec Zvládnuté.",
    "Generate a text": "Vygenerovat text",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Proměňte vybraná slova v krátký příběh napsaný pomocí AI — "
        "vaše slovní zásoba v kontextu.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Vaše slovní zásoba zůstává synchronizována napříč zařízeními. Klikněte pro "
        "zobrazení stavu nebo okamžitou synchronizaci.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Povolte cloudovou synchronizaci, změňte jazyk, upravte vzhled a "
        "další v Nastavení.",

    # --- Texts tour ---
    "Add texts": "Přidat texty",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Napište nebo vložte text, načtěte ho z internetu "
        "(AI / Wikipedie / URL / RSS) nebo importujte soubory .txt.",
    "Your texts": "Vaše texty",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Procházejte své uložené texty a filtrujte je podle jazyka, "
        "úrovně nebo tématu.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Poslouchejte jakýkoli text nahlas — a kliknutím na slovo během čtení "
        "zobrazte jeho překlad nebo ho přidejte do svého slovníku.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Zobrazte paralelní překlad vedle sebe; vyberte jazyk "
        "šipkou vedle něj.",
    "Reading modes": "Režimy čtení",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Režim soustředění skryje seznam, Režim papíru změní "
        "pozadí a Upravit vám umožní upravit text.",

    # --- Flashcards tour ---
    "Choose your deck": "Vyberte si balíček",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Vyberte, co bude v balíčku — kartičky k opakování, "
        "slova z vašeho aktuálního filtru, nejnovější přírůstky "
        "nebo ručně vybrané slova.",
    "Shape the session": "Přizpůsobte relaci",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Nastavte, kolik kartiček chcete opakovat, zamíchejte jejich pořadí a "
        "nechte každou kartičku vyslovit, jakmile se objeví a otočí.",
    "Preview the deck": "Náhled balíčku",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Přesné kartičky, které vaše relace obsahuje. Klikněte na dlaždici pro "
        "přečtení nebo úpravu její definice, nebo na reproduktor pro poslech "
        "slova.",
    "Review and grade": "Opakovat a hodnotit",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Otočte každou kartičku a ohodnoťte, jak dobře jste ji znali — Těžké, "
        "Dobré nebo Snadné. Intervalové opakování rozhodne, kdy se kartička "
        "vrátí: snadná slova počkají déle, těžká se vrátí "
        "dříve. Mezerník otáčí, klávesy 1–3 hodnotí.",
    "Or just listen": "Nebo jen poslouchejte",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "Přehrajte balíček a proměňte relaci v zvuk — kartičky postupují "
        "a otáčejí se v synchronizaci s hlasem. Kdykoli pozastavte pro "
        "vlastní ohodnocení kartičky.",

    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Vaše slovní zásoba na první pohled — celkový počet, zvládaná slova, "
        "jazyky a vaše aktuální série.",
    "See how your vocabulary has grown over time.":
        "Podívejte se, jak vaše slovní zásoba v průběhu času rostla.",
    "Track how much you've reviewed over time.":
        "Sledujte, kolikrát jste si v průběhu času slova opakovali.",

    # --- Demo text ---
    "Sample: A walk in the city": "Ukázka: Procházka městem",
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
        "Ráno bylo jasné a ulice tiché. Mladá žena pomalu kráčela po staré "
        "cestě, dívala se na vysoké domy a malé obchůdky, které se právě "
        "otevíraly. Zastavila se, aby si koupila čerstvý chléb a šálek kávy, a "
        "pak přešla náměstí směrem k parku. Děti si hrály u řeky, zatímco jejich "
        "rodiče si povídali na lavičkách opodál. Posadila se pod velký strom, "
        "otevřela knihu a začala číst. Příběh vyprávěl o cestovateli, který "
        "přešel hory a hledal starého přítele, kterého neviděl mnoho let. "
        "Po chvíli vzhlédla a pozorovala lodě pomalu plující po řece a "
        "ptáky kroužící vysoko nad střechami. Kdeosi blízko začal hrát "
        "pouliční muzikant a jemné tóny doprovázely její myšlenky. Bylo "
        "to klidné a šťastné ráno, přesně takové, jaké měla nejraději.",
    "Demo": "Ukázka",

    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Neplatný klíč OpenAI API. Zkontrolujte jej v Nastavení → Překlad a AI → AI → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Na vašem účtu OpenAI došel kredit. Přidejte kredit na "
        "platform.openai.com/account/billing, nebo přepněte poskytovatele AI "
        "na Gemini v Nastavení → Překlad a AI → AI.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "Dosaženo limitu požadavků OpenAI. Počkejte chvíli a zkuste to znovu.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Neznámý model OpenAI. Zkontrolujte název modelu v Nastavení → Překlad a AI → AI → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "Nelze se spojit s OpenAI. Zkontrolujte připojení k internetu.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Kvóta Gemini byla vyčerpána. Bezplatná úroveň se obnovuje denně; počkejte, "
        "nebo vytvořte nový klíč na aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Neplatný klíč Google API. Zkontrolujte jej v Nastavení → Překlad a AI → AI → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Neznámý model Gemini. Zkontrolujte název modelu v Nastavení → Překlad a AI → AI → Gemini.",

    # --- Words empty state ---
    "Your vocabulary journey starts here": "Vaše cesta za slovní zásobou začíná zde",
    "Add your first word — its translation can be fetched automatically.":
        "Přidejte své první slovo — jeho překlad lze načíst automaticky.",
    "Add your first word": "Přidat první slovo",
    "Take the tour": "Spustit prohlídku",
    "No matching words": "Žádná odpovídající slova",
    "Try a different search or filter.": "Zkuste jiné vyhledávání nebo filtr.",
    "Clear filters": "Vyčistit filtry",

    # --- Texts empty state ---
    "Your reading library starts here": "Vaše čtenářská knihovna začíná zde",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Přidejte text k čtení — napište nebo vložte vlastní, načtěte ho z "
        "internetů nebo importujte soubor .txt.",
    "Add a text": "Přidat text",
    "Fetch from the Internet": "Získat z internetu",
    "Import .txt": "Importovat .txt",
    "My first story": "Můj první příběh",
    "A news article": "Zpravodajský článek",
    "A short poem": "Krátká báseň",
    "Travel notes": "Cestovní poznámky",
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Byl jednou jeden zvědavý mladý lišák, který žil v malé vesničce u moře.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Vědci našli nový způsob, jak zkoumat, jak se jazyky v průběhu století mění a vyvíjejí.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Vítr se tiše prochází podzimními stromy a přináší staré a polozapomenuté písně.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "První den: do města jsme dorazili pozdě v noci a ulice byly stále plné teplého světla.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Položky smazané na jiném zařízení",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Zatímco bylo toto zařízení offline, {n} položka/položky/položek zde bylo smazáno na vašich "
        "ostatních zařízeních. Ponechat je v cloudu, nebo je odebrat z tohoto zařízení?",
    "(untitled)": "(bez názvu)",
    "[Text] {title}": "[Text] {title}",
    "Remove from this device": "Odebrat z tohoto zařízení",
    "Decide later": "Rozhodnout se později",
    "Keep & upload": "Ponechat a nahrát",
    "Not now": "Nyní ne",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Zadejte název offline profilu.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Můžete mít až {max} offline profilů. Pro přidání dalšího jeden odeberte.",
    "New offline profile": "Nový offline profil",
    "Profile name:": "Název profilu:",
    "Offline profile": "Offline profil",
    "Rename offline profile": "Přejmenovat offline profil",
    "Offline profiles": "Offline profily",
    "Add offline profile…": "Přidat offline profil…",
    "Profile actions": "Akce profilu",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Samostatné knihovny pouze pro toto zařízení s vlastní databází. Nikdy se nesynchronizují a nevyžadují přihlášení.",
    "Default (local)": "Výchozí (lokální)",
    "Rename": "Přejmenovat",
    "Delete offline profile": "Smazat offline profil",
    "Enable cloud sync…": "Povolit cloudovou synchronizaci…",
    "Could not create the profile.": "Profil se nepodařilo vytvořit.",
    "Created and switched to “{name}”.": "Vytvořeno a přepnuto na „{name}“.",
    "Deleted “{name}”.": "Profil „{name}“ smažen.",
    "Untitled profile": "Profil bez názvu",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Trvale smazat offline profil „{name}“? Jeho slova a texty existují pouze na tomto zařízení — v cloudu není žádná kopie. Databáze se nejprve zaarchivuje do složky záloh, ale tuto akci nelze v aplikaci vrátit zpět.",
    "this profile": "tento profil",
    "Connect to the internet to merge this profile into your account.": "Připojte se k internetu a sloučte tento profil se svým účtem.",
    "Enable cloud sync for this profile": "Povolit cloudovou synchronizaci pro tento profil",
    "Continue": "Pokračovat",
    "Upload words": "Nahrát slova",
    "Upload texts": "Nahrát texty",
    "Upload & sync": "Nahrát a synchronizovat",
    "Could not upload this profile. Your data is unchanged.": "Tento profil se nepodařilo nahrát. Vaše data jsou beze změny.",
    "“{name}” is now synced to your account.": "Profil „{name}“ je nyní synchronizován s vaším účtem.",
    "Everything in this profile is already in your account.": "Vše z tohoto profilu již ve vašem účtu je.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Přihlaste se nebo vytvořte účet pro zálohování profilu „{name}“ a jeho synchronizaci napříč zařízeními. Slova a texty tohoto profilu se nahrají a ten se stane vaším synchronizovaným účtem na tomto zařízení. Kopie se nejprve zaarchivuje do složky záloh.",
    "Upload “{name}” to your account": "Nahrát profil „{name}“ do vašeho účtu",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Váš profil se na tomto zařízení stane synchronizovaným účtem „{who}“ a nahraje se do cloudu.",
    "Merge “{name}” into your account": "Sloučit profil „{name}“ do vašeho účtu",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Tento účet již má data na tomto zařízení. Slova a texty vašeho profilu, které tam ještě nejsou, se k němu přidají — nic se nepřebíjí. Profil „{name}“ se poté zaarchivuje do složky záloh a odebere.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Tento profil obsahuje {items}, uloženo pouze na tomto zařízení. Povolte cloudovou synchronizaci pro jejich zálohování a studium na všech zařízeních.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Vyberte položky k přidání. Zkopírují se do vašeho účtu a nahrají do cloudu. Profil „{name}“ se poté zaarchivuje do složky záloh a odebere.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Souhlasím s <a href=\"{terms}\">Smluvními podmínkami</a> a <a href=\"{privacy}\">Zásadami ochrany osobních údajů</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Pro pokračování prosím přijměte Smluvní podmínky a Zásady ochrany osobních údajů.",
    "Updated Terms & Privacy": "Aktualizované Podmínky a Ochrana soukromí",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Aktualizovali jsme naše Smluvní podmínky a Zásady ochrany osobních údajů. Pro pokračování v používání účtu si je prosím přečtěte a přijměte je.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Souhlasím s aktualizovanými <a href=\"{terms}\">Smluvními podmínkami</a> a <a href=\"{privacy}\">Zásadami ochrany osobních údajů</a>.",
    "Sign out": "Odhlásit se",
    "I agree": "Souhlasím",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Zásady ochrany osobních údajů</a> · <a href=\"{terms}\">Podmínky</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Pokračováním souhlasíte se <a href=\"{terms}\">Smluvními podmínkami</a> a <a href=\"{privacy}\">Zásadami ochrany osobních údajů</a>.",
    "Privacy Policy": "Zásady ochrany osobních údajů",
    "Terms": "Podmínky",
    "Website": "Webová stránka",
    "Contact": "Kontakt",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Kartičky",
    "Practice your vocabulary": "Procvičujte si svou slovní zásobu",
    "Due cards": "Kartičky k opakování",
    "Current filter": "Aktuální filtr",
    "Newest": "Nejnovější",
    "Selected words": "Vybraná slova",
    "Deck size": "Velikost balíčku",
    "Default deck size": "Výchozí velikost balíčku",
    "Shuffle": "Zamíchat",
    "Start session": "Spustit relaci",
    "Play deck": "Přehrát balíček",
    "{n} cards ready to review": "Připraveno k opakování kartiček: {n}",
    "No cards due — great job!": "Žádné kartičky k opakování — skvělá práce!",
    "{n} selected words": "Vybraných slov: {n}",
    "No words to practice.": "Žádná slova k procvičování.",
    "End session": "Ukončit relaci",
    "Listening — pause to review manually":
        "Poslech — pozastavte pro ruční opakování",
    "Show answer": "Zobrazit odpověď",
    "Hard": "Těžké",
    "Good": "Dobré",
    "Easy": "Snadné",
    "Space or click to flip": "Mezerník nebo kliknutí pro otočení",
    "Card {current} of {total}": "Kartička {current} z {total}",
    "{n} correct": "Správně: {n}",
    "Session complete!": "Relace dokončena!",
    "You listened to {n} of {total} cards.": "Poslechli jste si {n} z {total} kartiček.",
    "Correct: {n} of {total}": "Správně: {n} z {total}",
    "New session": "Nová relace",
    "Practice hard words": "Procvičovat těžká slova",
    "Hard words": "Těžká slova",
    "Hard words cleared!": "Těžká slova zvládnutá!",
    "Open Flashcards when Read Aloud starts":
        "Otevřít Kartičky při spuštění předčítání",
    "Stop": "Zastavit",
    "Auto-pronounce": "Automatická výslovnost",
    "Speak each card as it appears and when it flips":
        "Vyslovit každou kartičku, když se objeví a když se otočí",
    "Deck preview": "Náhled balíčku",
    "{n} cards": "Kartiček: {n}",
    "Due": "K opakování",
    "In {n} d": "Za {n} d.",
    "{n} d": "{n} d.",
    "{n} mo": "{n} měs.",
    "{n} y": "{n} r.",

    # ── Android companion app ──────────────────────────────────────────────
    "Lingueez for Android…": "Lingueez pro Android…",
    "Android app": "Aplikace pro Android",
    "Lingueez on Android": "Lingueez v Androidu",
    "Take your vocabulary with you": "Vezměte si svou slovní zásobu s sebou",
    "Preview of Lingueez on a phone": "Náhled Lingueez v telefonu",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Přihlaste se pod svým účtem Lingueez a vaše slovní zásoba už tam bude — "
        "nic nemusíte nastavovat ani přenášet.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Přihlaste se k bezplatnému účtu Lingueez na obou zařízeních a vaše slovní zásoba "
        "se synchronizuje do telefonu — žádné soubory k ručnímu kopírování.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Přihlaste se k bezplatnému účtu Lingueez a vaše slova se synchronizují do telefonu.",
    "Synced both ways": "Obousměrná synchronizace",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Slova, která přidáte v telefonu, na vás čekají v počítači a naopak.",
    "Listen with the screen off": "Poslouchejte s vypnutou obrazovkou",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Ovládání na zamčené obrazovce vám umožní pokračovat v opakování, i když máte telefon v kapse.",
    "Save a word from any app": "Uložte slovo z jakékoli aplikace",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Sdílejte text do aplikace Lingueez a ten se uloží do vašeho slovníku, připravený k pozdějšímu doplnění.",
    "Point your phone's camera at the code":
        "Naměřte fotoaparát telefonu na kód",
    "Get it on Google Play": "Získat na Google Play",
    "Copy link": "Kopírovat odkaz",
    "Link copied": "Odkaz zkopírován",
    "Lingueez is now on Android": "Lingueez je nyní i na Androidu",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Přihlaste se pod svým účtem Lingueez — vaše slovní zásoba už tam bude.",
    "Dismiss": "Skrýt",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Používejte svůj účet Lingueez plynule mezi počítačem a zařízeními Android.",
    "Get the app…": "Získat aplikaci…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Kvíz",
    "Quiz (recall practice)": "Kvíz (procvičování vybavování)",
    "Recall your words, one question at a time":
        "Vybavte si svá slova, otázku po otázce",
    "Questions": "Otázek",
    "Answer with": "Odpovídat",
    "Choices": "Výběr",
    "Typing": "Psaní",
    "Ask": "Ptát se na",
    "Term": "Termín",
    "Mixed": "Smíšeně",
    "Auto-advance": "Automatický přechod",
    "Move on by itself after a correct answer": "Po správné odpovědi pokračovat samo",
    "Speak the question, then the answer once it is revealed":
        "Přečíst otázku a po odhalení i odpověď",
    "Start quiz": "Spustit kvíz",
    "questions ready": "otázek připraveno",
    "Nothing to quiz": "Není na co se ptát",
    "No words match this deck.": "Tomuto balíčku neodpovídají žádná slova.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Kvíz potřebuje alespoň dvě slova — špatné odpovědi pocházejí právě ze slov, "
        "na která se právě neptáme.",
    "Not enough words": "Málo slov",
    "Add a few more words, or widen the deck.":
        "Přidejte několik slov nebo rozšiřte balíček.",
    "Question {n} of {total}": "Otázka {n} z {total}",
    "Missed words": "Chybná slova",
    "End quiz": "Ukončit kvíz",
    "Answer in {language}": "Odpovězte v jazyce: {language}",
    "Type the answer": "Napište odpověď",
    "Check": "Zkontrolovat",
    "Click to continue": "Klepnutím pokračujte",
    "See results": "Zobrazit výsledky",
    "Almost — it is \"{answer}\"": "Skoro — správně je „{answer}“",
    "It is \"{answer}\"": "Správně je „{answer}“",
    "Now {status}": "Nyní {status}",
    "Correct": "Správně",
    "Missed": "Chyby",
    "Worth another look": "Stojí za zopakování",
    "Again": "Znovu",
    "Missed words cleared!": "Chybná slova zvládnuta!",
    "Perfect run": "Bezchybné kolo",
    "Quiz complete": "Kvíz dokončen",
    "Practice missed": "Procvičit chyby",
    "Default number of questions": "Výchozí počet otázek",
    "Move on after a correct answer": "Po správné odpovědi pokračovat",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Vyberte, na co se budeme ptát",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Stejné balíčky jako u kartiček — slova k opakování, aktuální filtr, "
        "nejnovější nebo ručně vybraná — a kolik otázek.",
    "Choices or typing": "Výběr nebo psaní",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "„Výběr“ nabídne čtyři možnosti; „Psaní“ vyžaduje odpověď napsat — je to "
        "těžší, ale lepší zkouška. Psaní odpouští diakritiku i drobné překlepy. „Ptát "
        "se na“ určuje, kterou stranu vidíte: termín, překlad, nebo obojí střídavě.",
    "Start, and it counts": "Začněte — a počítá se to",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "Pruh ukazuje složení balíčku podle stavů. Každá odpověď plní stejný plán "
        "opakování jako kartičky: slovo, které si vybavíte, se vrátí později, chybné "
        "dříve.",

    # ── import_excel.py (definitions & tags) ──────────────────────────────
    "Definition 1": "Definice 1",
    "Definitions and tags": "Definice a značky",
    "Definitions and tags ({n})": "Definice a značky ({n})",
    " · {n} gaining definitions or tags": " · {n} získá definice nebo značky",
    "Already in the database — kept as is.": "Již v databázi — zůstane beze změny.",
    "New tags: {tags}": "Nové značky: {tags}",
    "\n\nEntry ID: {id}": "\n\nID záznamu: {id}",
    "Optional columns: Definition, Definition2 and Tags "
    "(comma-separated) — merged into words you already have, "
    "never overwriting them.": (
        "Volitelné sloupce: Definition, Definition2 a Tags (oddělené čárkami) — doplní se ke slovům, která už máte, aniž by je přepsaly."
    ),
}

# Date names, read by app.i18n.
MONTHS = ["ledna", "února", "března", "dubna", "května", "června",
          "července", "srpna", "září", "října", "listopadu", "prosince"]
MONTHS_ABBR = ["led", "úno", "bře", "dub", "kvě", "čvn",
               "čvc", "srp", "zář", "říj", "lis", "pro"]
WEEKDAYS = ["Pondělí", "Úterý", "Středa", "Čtvrtek",
            "Pátek", "Sobota", "Neděle"]
WEEKDAYS_ABBR = ["Po", "Út", "St", "Čt", "Pá", "So", "Ne"]