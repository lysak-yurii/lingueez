# Lingueez — Hungarian (hu) translations.
# Keys are English UI strings; values are their Hungarian equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Magyar"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Mégse",
    "OK": "OK",
    "Close": "Bezárás",
    "Save": "Mentés",
    "Delete": "Törlés",
    "Edit": "Szerkesztés",
    "Remove": "Eltávolítás",
    "Add": "Hozzáadás",
    "Refresh": "Frissítés",
    "Import": "Importálás",
    "Export": "Exportálás",
    "Search": "Keresés",
    "Fetch": "Letöltés",
    "Browse…": "Tallózás…",
    "Clear": "Törlés",
    "Pause": "Szünet",
    "Resume": "Folytatás",
    "Language": "Nyelv",
    "Translation": "Fordítás",
    "Word": "Szó",
    "Status": "Állapot",
    "Error": "Hiba",
    "Title": "Cím",
    "Topic": "Téma",
    "Level": "Szint",
    "Generate": "Létrehozás",
    "Generating…": "Létrehozás…",
    "Translating…": "Fordítás…",
    "Format": "Formátum",
    "Style": "Stílus",
    "Model": "Modell",
    "Font": "Betűtípus",
    "Usage": "Használat",
    "Translation language": "Fordítás nyelve",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Menü",
    "Open Excel Table…": "Excel-táblázat megnyitása…",
    "Import Excel to Database…": "Excel importálása az adatbázisba…",
    "Save Import Template…": "Importálási sablon mentése…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Hang (MP3)…",
    "Backups…": "Biztonsági mentések…",
    "Show Source column": "„Forrás” oszlop megjelenítése",
    "Show Created At column": "„Létrehozva” oszlop megjelenítése",
    "Max words…": "Maximális szószám…",
    "View Log": "Napló megtekintése",
    "About": "Névjegy",
    "Quit": "Kilépés",
    "Words": "Szavak",
    "Texts": "Szövegek",
    "Statistics": "Statisztika",
    "Bin (deleted items)": "Lomtár (törölt elemek)",
    "Settings": "Beállítások",
    "Vocabulary": "Szókincs",
    "Search words, translations or tags…": "Keresés szavak, fordítások vagy címkék között…",
    "Search texts by title, content or words…": "Keresés szövegekben cím, tartalom vagy szavak alapján…",
    "Search scope": "Keresési tartomány",
    "Search scope…": "Keresési tartomány…",
    "Nothing to practice yet": "Még nincs mit gyakorolni",
    "Add words to your vocabulary and they show up here.":
        "Vegyen fel szavakat a szótárába, és itt fognak megjelenni.",
    "Come back when cards are due, or practice the newest words now.":
        "Térjen vissza, amikor esedékes kártyák lesznek, vagy gyakorolja most a legújabb szavakat.",
    "Practice newest words": "Legújabb szavak gyakorlása",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Válasszon fent másik paklit, vagy módosítsa a szűrőket a Szavak oldalon.",
    "You're all caught up": "Mindennel végzett",
    "Add word": "Szó hozzáadása",
    "Copy a word in any app, then press:":
        "Másoljon ki egy szót bármelyik alkalmazásban, majd nyomja meg:",
    "Set a shortcut": "Gyorsbillentyű beállítása",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Másoljon ki egy szót bármelyik alkalmazásban, majd a {keys} megnyomásával a fordításával együtt hozzáadhatja.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Állítson be gyorsbillentyűt a Beállításokban, hogy bármelyik alkalmazásból hozzáadhassa a másolt szavakat.",
    " Favorites": " Kedvencek",
    " Filters": " Szűrők",
    "Filters that don't fit the table": "A táblázatba nem illő szűrők",
    "More actions": "További műveletek",
    "Filter by tag": "Szűrés címke alapján",
    "Close file and return to your vocabulary": "Fájl bezárása és visszatérés a szókincshez",
    "Definition": "Meghatározás",
    "Read": "Olvasás",
    "Favorite": "Kedvenc",
    "Tags": "Címkék",
    "Copy": "Másolás",
    "Text": "Szöveg",
    "Delete selected (Del)": "Kijelöltek törlése (Del)",
    "No data": "Nincs adat",
    "No texts yet": "Még nincsenek szövegek",
    "Words: {shown}/{total}": "Szavak: {shown}/{total}",
    "Texts: {total}": "Szövegek: {total}",
    "Texts: {shown}/{total}": "Szövegek: {shown}/{total}",
    "{count} selected": "{count} kijelölve",
    "No selection": "Nincs kijelölés",
    "Please select at least one word.": "Kérjük, jelöljön ki legalább egy szót.",
    "Saved": "Mentve",
    "'{word}' updated.": "„{word}” frissítve.",
    "Database Error": "Adatbázishiba",
    "Delete {count} word(s)?": "Töröl {count} szót?",
    "Deleted": "Törölve",
    "{count} word(s) deleted.": "{count} szó törölve.",
    "Deleted with {n} error(s).": "Törölve {n} hibával.",
    "Favorites": "Kedvencek",
    "{count} word(s) added to favorites.": "{count} szó hozzáadva a kedvencekhez.",
    "{count} word(s) removed from favorites.": "{count} szó eltávolítva a kedvencekből.",
    "Status set to '{status}' for {count} word(s).": "Állapot beállítva erre: „{status}” ({count} szó esetén).",
    "Max Words": "Maximális szószám",
    "Show only the first N words (0 = show all):": "Csak az első N szó megjelenítése (0 = összes):",
    "View Definition": "Meghatározás megtekintése",
    "Copy Word": "Szó másolása",
    "Copy Translation": "Fordítás másolása",
    "Toggle Favorite": "Kedvenc ki/bekapcsolása",
    "Change Status…": "Állapot módosítása…",
    "Add / Remove Tags…": "Címkék hozzáadása / eltávolítása…",
    "Read Aloud": "Felolvasás",
    "Change Status": "Állapot módosítása",
    "New status:": "Új állapot:",
    "Copied": "Másolva",
    "{count} row(s) copied to clipboard.": "{count} sor másolva a vágólapra.",
    "{count} item(s) copied to clipboard.": "{count} elem másolva a vágólapra.",
    "Copy Word(s)": "Szó (szavak) másolása",
    "Copy Translation(s)": "Fordítás(ok) másolása",
    "Copy Both": "Mindkettő másolása",
    "Search in Word": "Keresés a szóban",
    "Search in Translation": "Keresés a fordításban",
    "Search in Tags": "Keresés a címkékben",
    "Promoted": "Léptetve",
    "Google Cloud TTS unavailable": "A Google Cloud TTS nem érhető el",
    "Selection limit": "Kijelölési korlát",
    "Only the first 200 selected words will be read.": "Csak az első 200 kijelölt szó kerül felolvasásra.",
    "Only the first 50 words will be used.": "Csak az első 50 szó kerül felhasználásra.",
    "Select words to save as audio.": "Válasszon ki szavakat a hangfájlként való mentéshez.",
    "Nothing to export.": "Nincs exportálandó adat.",
    "Export Error": "Exportálási hiba",
    "Settings saved.": "Beállítások elmentve.",
    "Generated text saved.": "A generált szöveg elmentve.",
    "Show": "Megjelenítés",
    "Add Word": "Szó hozzáadása",
    "Stop reading": "Olvasás leállítása",
    "Read — Read selected words aloud": "Olvasás — A kijelölt szavak felolvasása",
    "Translation": "Fordítás",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Megjelenés",
    "Audio": "Hang",
    "Learning": "Tanulás",
    "Listening": "Hallgatás",
    "Backups": "Biztonsági mentések",
    "Sync your library?": "Szinkronizálja a könyvtárát?",
    "This will reconcile your device with the cloud:": "Ez összehangolja az eszközét a felhővel:",
    "Sync now": "Szinkronizálás most",
    "Upload": "Feltöltés",
    "Synced — ↑{up} ↓{down}": "Szinkronizálva — ↑{up} ↓{down}",
    "Upload restored library?": "Feltölti a helyreállított könyvtárat?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "A könyvtár helyreállítva. A legközelebbi szinkronizálási szerverhez való csatlakozáskor felajánljuk a feltöltést.",
    "Merging this restored backup with your cloud:": "A helyreállított mentés egyesítése a felhővel:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Ez a mentés {items} elemet tartalmaz. Feltölti és egyesíti most a felhővel, vagy egyelőre érintetlenül hagyja a felhőt?",
    "General": "Általános",
    "Read-aloud": "Felolvasás",
    "Translation & AI": "Fordítás és AI",
    "Data": "Adatok",
    "Behavior": "Viselkedés",
    "Progress": "Haladás",
    "DeepL request failed — using free Google Translate instead.": "A DeepL kérés nem sikerült — az ingyenes Google Fordító kerül felhasználásra.",
    "DeepL key isn't set — using free Google Translate instead.": "A DeepL kulcs nincs beállítva — az ingyenes Google Fordító kerül felhasználásra.",
    "System": "Rendszer",
    "Light": "Világos",
    "Dark": "Sötét",
    "Appearance mode": "Megjelenési mód",
    "Widget scaling": "Elemek méretezése",
    "Table size": "Táblázat mérete",
    "Interface language": "Felület nyelve",
    "Restart the app to apply the language change.": "Indítsa újra az alkalmazást a nyelvváltás alkalmazásához.",
    "The interface language has changed. Restart now to apply it?": "A felület nyelve megváltozott. Újraindítja most az alkalmazást?",
    "TTS provider": "TTS szolgáltató",
    "Google Cloud credentials": "Google Cloud hitelesítő adatok",
    "Voice type": "Hang típusa",
    "Voice name (optional)": "Hang neve (opcionális)",
    "Read Aloud playback": "Felolvasás beállításai",
    "Pause between words (s)": "Szünet a szavak között (mp)",
    "Repeats per word": "Ismétlés szavanként",
    "Repeats per pair": "Ismétlés páronként",
    "Promote status while listening": "Állapot léptetése hallgatás közben",
    "Listens to reach {status}": "Meghallgatások száma a(z) „{status}” állapothoz",
    "Excel import": "Excel importálás",
    "Placeholder values": "Helykitöltő értékek",
    "Skip placeholder rows": "Helykitöltő sorok kihagyása",
    "Skip empty rows": "Üres sorok kihagyása",
    "Normalize language pairs": "Nyelvpárok normalizálása",
    "How to import": "Hogyan importáljunk",
    "Save import template…": "Importálási sablon mentése…",
    "Active provider": "Aktív szolgáltató",
    "API key": "API-kulcs",
    "API URL": "API URL",
    "Check usage": "Használat ellenőrzése",
    "Enable cloud sync": "Felhőalapú szinkronizálás engedélyezése",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase kulcs (.env)",
    "Bin cleanup grace (days)": "Lomtár megőrzési ideje (nap)",
    "Test Connection": "Kapcsolat tesztelése",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "A felhőszinkronizálás az Ön saját Supabase projektjét használja. Hozza létre a szükséges táblákat egyszer, majd adja meg a fenti URL-t és anon kulcsot.",
    "Copy schema SQL": "Séma SQL másolása",
    "Open SQL editor ↗": "SQL szerkesztő megnyitása ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "A séma SQL a vágólapra másolva. Nyissa meg a Supabase projekt SQL szerkesztőjét, illessze be, és nyomja meg a Run gombot a táblák létrehozásához.",
    "Server": "Szerver",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Csatlakoztatva a saját Supabase szerveréhez — személyes mód, fiók nem szükséges.\n{host}",
    "Use your own Supabase server (personal)": "Saját Supabase szerver használata (személyes)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Személyes, egyfelhasználós szinkronizálás az Ön saját Supabase projektjével. Nincs szükség fiókra vagy bejelentkezésre — az alkalmazás a projekt anon kulcsával csatlakozik. Futtassa a séma SQL-t a projektjében, illessze be az URL-t és az anon kulcsot alább, majd kattintson a Kapcsolat tesztelése gombra.\n\nMegjegyzés: bárki, aki rendelkezik ezzel az URL-lel és kulccsal, elolvashatja az adatokat, ezért tartsa a projektet magánjellegűként, és ne ossza meg a kulcsot.",
    "Disconnect — use the built-in server": "Lecsatlakozás — a beépített szerver használata",
    "Disconnect server": "Szerver lecsatlakoztatása",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Leállítja a szinkronizálást a saját Supabase szerverével, és újra a beépítettet használja?\n\nA szavai megmaradnak a saját projektjében és ezen az eszközön. A fiókba való bejelentkezésig csak helyi módban fog működni.",
    "Disconnected — using the built-in server.": "Lecsatlakoztatva — a beépített szerver használatban.",
    "{host} (personal)": "{host} (személyes)",
    "Personal": "Személyes",
    "your server": "az Ön szervere",
    "Account actions": "Fiókműveletek",
    "Add account…": "Fiók hozzáadása…",
    "Sync this device's data to my account…": "Az eszköz adatainak szinkronizálása a fiókomba…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Fiók",
    "Accounts": "Fiókok",
    "No accounts yet. Add one to sync your words across devices.": "Még nincsenek fiókok. Adjon hozzá egyet a szavak eszközök közötti szinkronizálásához.",
    "(active)": "(aktív)",
    "Sign in": "Bejelentkezés",
    "(sign in again)": "(jelentkezzen be újra)",
    "Switch": "Váltás",
    "Remove account": "Fiók eltávolítása",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Eltávolítja a(z) {email} fiókot erről az eszközről? Bármikor újra hozzáadhatja — a szavai a felhőben maradnak, a helyi másolat pedig a lemezen. A felhőben lévő adatai nem törlődnek.",
    "Removed {email} from this device.": "{email} eltávolítva erről az eszközről.",
    "Your data was exported.": "Az adatai exportálva lettek.",
    "Export failed.": "Az exportálás nem sikerült.",
    "Delete account": "Fiók törlése",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Ez véglegesen törli a fiókját és az ÖSSZES szinkronizált szavát, szövegét és címkéjét a felhőből. A helyi másolat archiválásra kerül a biztonsági mentések mappájába. Ez a művelet nem vonható vissza.\n\nTörli a fiókját?",
    "Account deleted.": "Fiók törölve.",
    "Could not delete the account.": "A fiók törlése nem sikerült.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Név",
    "Enter your name.": "Adja meg a nevét.",
    "Email": "E-mail",
    "Password": "Jelszó",
    "New password": "Új jelszó",
    "6-digit code": "6-jegyű kód",
    "or": "vagy",
    "Sign in with Google": "Bejelentkezés Google-fiókkal",
    "Opening your browser to sign in with Google…": "A böngésző megnyitása a Google-bejelentkezéshez…",
    "Forgot password?": "Elfelejtette a jelszót?",
    "Resend code": "Kód újraküldése",
    "Confirm your email": "Erősítse meg az e-mail-címét",
    "Verify code": "Kód ellenőrzése",
    "Use a different email": "Másik e-mail-cím használata",
    "Enter your email and password.": "Adja meg az e-mail-címét és a jelszavát.",
    "Enter the 6-digit code from the email.": "Adja meg az e-mailben kapott 6-jegyű kódot.",
    "Enter the code and a new password.": "Adja meg a kódot és az új jelszót.",
    "Enter your email above first.": "Először adja meg az e-mail-címét fent.",
    "Enter the reset code we emailed you and a new password.": "Adja meg az e-mailben elküldött visszaállítási kódot és egy új jelszót.",
    "Enter the 6-digit code we emailed you.": "Adja meg az e-mailben elküldött 6-jegyű kódot.",
    "Reset password": "Jelszó visszaállítása",
    "Set new password": "Új jelszó beállítása",
    "Back to sign in": "Vissza a bejelentkezéshez",
    "Sign-in failed.": "A bejelentkezés nem sikerült.",
    "Couldn't send the code.": "A kód elküldése nem sikerült.",
    "Done.": "Kész.",
    "Failed.": "Sikertelen.",
    "Create an account": "Fiók létrehozása",
    "Create account": "Fiók létrehozása",
    "I already have an account": "Már van fiókom",
    "Signed in as {email}": "Bejelentkezve mint {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Ezen eszköz adatainak szinkronizálása a fiókjába",
    "your account": "az Ön fiókja",
    "This device has {words} and {texts} not yet in {account}.": "Ezen az eszközön {words} és {texts} található, amelyek még nincsenek a(z) {account} fiókban.",
    "This device has {words} not yet in {account}.": "Ezen az eszközön {words} található, amelyek még nincsenek a(z) {account} fiókban.",
    "This device has {texts} not yet in {account}.": "Ezen az eszközön {texts} található, amelyek még nincsenek a(z) {account} fiókban.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Válassza ki a hozzáadandó elemeket. Ezek átmásolódnak a fiókjába és feltöltődnek a felhőbe, így megjelennek a többi eszközén is. Az ezen az eszközön lévő másolat megmarad.",
    "Don't ask again for this account": "Ne kérdezze meg újra ehhez a fiókhoz",
    "{n} word": "{n} szó",
    "{n} words": "{n} szó",
    "{n} text": "{n} szöveg",
    "{n} texts": "{n} szöveg",
    "Add {n} item": "{n} elem hozzáadása",
    "Add {n} items": "{n} elem hozzáadása",
    # Hungarian does not use special genitive forms for counts; standard forms work
    "words (genitive)": "szó",
    "texts (genitive)": "szöveg",
    "tags (genitive)": "címke",
    "changes (genitive)": "változtatás",
    "deletions (genitive)": "törlés",
    "{n} words (genitive)": "{n} szó",
    "{n} texts (genitive)": "{n} szöveg",
    "Add {n} items (genitive)": "{n} elem hozzáadása",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "{n} elem hozzáadva a fiókjához.",
    "Added {n} items to your account.": "{n} elem hozzáadva a fiókjához.",
    "Added {n} items to your account. (genitive)": "{n} elem hozzáadva a fiókjához.",
    "{n} couldn't be added.": "{n} elemet nem sikerült hozzáadni.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "A munkamenet lejárt — jelentkezzen be újra (Beállítások → Szinkronizálás)",
    "Sign in to sync (Settings → Sync)": "Jelentkezzen be a szinkronizáláshoz (Beállítások → Szinkronizálás)",
    "Sign in again to sync": "Jelentkezzen be újra a szinkronizáláshoz",
    "Sign in again to use this account.": "Jelentkezzen be újra a fiók használatához.",
    "Sync incomplete: {reason}": "A szinkronizálás nem fejeződött be: {reason}",
    "Connect to the internet to add local items to your account.": "Csatlakozzon az internethez a helyi elemek fiókhoz való hozzáadásához.",
    "Everything on this device is already in your account.": "Minden, ami ezen az eszközön van, már megtalálható a fiókjában.",
    "Upload local words?": "Feltölti a helyi szavakat?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Feltölti a jelenlegi helyi szavakat ebbe a fiókba? Egyesülnek a fiók felhőadataival és szinkronizálódnak.\n\nVálassza a Nem lehetőséget a fiók meglévő adatainak megtartásához és a helyi szavak félretenni (a biztonsági mentések mappába archiválva).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "A bejelentkezés nem sikerült. Ellenőrizze e-mail-címét és jelszavát.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Legfeljebb {max} fiókot tarthat ezen az eszközön. Távolítson el egyet egy új hozzáadásához.",
    "Wrong email or password.": "Hibás e-mail-cím vagy jelszó.",
    "That doesn't look like a valid email address.": "Ez nem tűnik érvényes e-mail-címnek.",
    "Confirm password": "Jelszó megerősítése",
    "Passwords don't match.": "A jelszavak nem egyeznek.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Az e-mail-címe még nincs megerősítve. Adja meg az e-mailben elküldött 6-jegyű kódot.",
    "That email is already registered. Try signing in instead.": "Ez az e-mail-cím már regisztrálva van. Próbáljon meg inkább bejelentkezni.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Elküldtünk egy 6-jegyű kódot e-mailben. Adja meg a regisztráció befejezéséhez.",
    "That code didn't work. Check it and try again.": "Ez a kód nem működött. Ellenőrizze és próbálja újra.",
    "If that account exists, a 6-digit reset code is on its way.": "Ha a fiók létezik, a 6-jegyű visszaállító kód úton van.",
    "Confirmation email re-sent.": "A megerősítő e-mail újra elküldve.",
    "Too many attempts. Please wait a minute and try again.": "Túl sok kísérlet. Kérjük, várjon egy percet, és próbálja újra.",
    "Your password is too short — use at least 6 characters.": "A jelszó túl rövid — használjon legalább 6 karaktert.",
    "Sign-ups are disabled on this server.": "A regisztráció le van tiltva ezen a szerveren.",
    "Can't reach the server. Check your internet connection.": "A szerver nem érhető el. Ellenőrizze az internetkapcsolatot.",
    "Something went wrong.": "Valami hiba történt.",
    "Your saved sign-in for this account expired. Sign in again.": "A mentett bejelentkezése ehhez a fiókhoz lejárt. Jelentkezzen be újra.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "A felhőszinkronizálás még nincs beállítva. Először adja meg a Supabase URL-t és kulcsot a Beállítások → Szinkronizálás menüpontban.",
    "Could not start Google sign-in.": "A Google-bejelentkezést nem sikerült elindítani.",
    "Google sign-in was cancelled or timed out.": "A Google-bejelentkezés megszakadt vagy lejárt az időkorlát.",
    "Google sign-in failed.": "A Google-bejelentkezés nem sikerült.",
    "Google sign-in failed: {error}": "A Google-bejelentkezés nem sikerült: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Nem sikerült elindítani a helyi bejelentkezési segédet a(z) {port} porton ({error}). Zárja be az azt használó alkalmazást, és próbálja újra.",
    "Export my data…": "Adataim exportálása…",
    "Delete account…": "Fiók törlése…",
    "Cloud sync is on — your own server ({host})": "Felhőszinkronizálás bekapcsolva — saját szerver ({host})",
    "Cloud sync is on — signed in as {who}": "Felhőszinkronizálás bekapcsolva — bejelentkezve mint {who}",
    "Cloud sync is off — your words are saved on this device only": "Felhőszinkronizálás kikapcsolva — szavai csak ezen az eszközön vannak mentve",
    "(checking…)": "(ellenőrzés…)",
    "(can't connect)": "(nincs kapcsolat)",
    "Turn off cloud sync": "Felhőszinkronizálás kikapcsolása",
    "Cloud sync turned off — this device only.": "Felhőszinkronizálás kikapcsolva — csak ez az eszköz.",
    "Use this server": "Ezen szerver használata",
    "Connecting…": "Csatlakozás…",
    "Testing…": "Tesztelés…",
    "Applying theme…": "Téma alkalmazása…",
    "Now syncing with your own server.": "Most a saját szerverével szinkronizál.",
    "Could not connect to this server:\n{error}": "Nem sikerült csatlakozni ehhez a szerverhez:\n{error}",
    "Could not connect to this server.": "Nem sikerült csatlakozni ehhez a szerverhez.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nEllenőrizze az URL-t és az anon kulcsot, valamint hogy lefuttatta-e ott a séma SQL-t. Ennek ellenére használja ezeket az adatokat?",
    "Enter your server's URL and anon key first, then test.": "Először adja meg a szervere URL-jét és anon kulcsát, majd tesztelje.",
    "Enter your server's URL and anon key first.": "Először adja meg a szervere URL-jét és anon kulcsát.",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase kulcs (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Személyes, egyfelhasználós szinkronizálás az Ön saját Supabase projektjével. Nincs szükség fiókra vagy bejelentkezésre — az alkalmazás a projekt anon kulcsával csatlakozik. Futtassa a séma SQL-t a projektjében, illessze be az URL-t és az anon kulcsot alább, tesztelje, majd nyomja meg a „Ezen szerver használata” gombot.\n\nMegjegyzés: bárki, aki rendelkezik ezzel az URL-lel és kulccsal, elolvashatja az adatokat, ezért tartsa a projektet magánjellegűként, és ne ossza meg a kulcsot.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Leállítja a szinkronizálást a saját Supabase szerverével, és újra a beépítettet használja?\n\nA szavai megmaradnak a saját projektjében és ezen az eszközön. A szerver adatai megőrződnek, így bármikor visszaválthat. A fiókba való bejelentkezésig csak helyi módban fog működzić.",
    "Start automatically on login (minimized to tray)": "Automatikus indítás bejelentkezéskor (a tálcára kicsinyítve)",
    "Add Word hotkey (global)": "„Szó hozzáadása” gyorsbillentyű (globális)",
    "Data format": "Adatformátum",
    "Columns to export": "Exportálandó oszlopok",
    "Sheet name": "Munkalap neve",
    "Start row": "Kezdősor",
    "Start column": "Kezdőoszlop",
    "Shade alternate rows": "Váltakozó sorok árnyékolása",
    "Auto column width": "Automatikus oszlopszélesség",
    "Freeze header row": "Fejléc sornak rögzítése",
    "Delimiter": "Elválasztójel",
    "Delimiter (\\t = tab)": "Elválasztójel (\\t = tab)",
    "Include header lines": "Fejlécsorok belefoglalása",
    "Header lines": "Fejlécsorok",
    "Page size": "Oldalméret",
    "Font size": "Betűméret",
    "Line spacing (pt)": "Sorköz (pt)",
    "Text alignment": "Szöveg igazítása",
    "Margins L/R/T/B (pt)": "Margók B/J/F/A (pt)",
    "Automatic widths (fit page)": "Automatikus szélesség (oldalhoz igazítás)",
    "Columns / width": "Oszlopok / szélesség",
    "Header background": "Fejléc háttér",
    "Header text": "Fejléc szövege",
    "Row background": "Sor háttér",
    "Grid lines": "Rácsvonalak",
    "Background image": "Háttérkép",
    "Concurrent workers": "Párhuzamos folyamatok",
    "Requests per second": "Kérések másodpercenként",
    "Add font…": "Betűtípus hozzáadása…",
    "Page && text": "Oldal és szöveg",
    "Columns": "Oszlopok",
    "Max tokens": "Max tokenek száma",
    "Temperature": "Hőmérséklet (Temperature)",
    "Prompt template": "Prompt sablon",
    "Definitions": "Meghatározások",
    "Generated Texts (from words)": "Generált szövegek (szavakból)",
    "Generated Texts (by topic)": "Generált szövegek (téma alapján)",
    "Text Adaptation (to level)": "Szöveg adaptációja (szinthez)",
    "Thinking budget (0 = off, -1 = auto)": "Gondolkodási keret (0 = ki, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Nyelv felismerése",
    "Type a word or phrase…": "Írjon be egy szót vagy kifejezést…",
    "Translation…": "Fordítás…",
    "Pronounce": "Kiejtés",
    "Swap word and translation": "Szó és fordítás felcserélése",
    "Translate with DeepL (Enter)": "Fordítás DeepL-lel (Enter)",
    "Save Word": "Szó mentése",
    "Enter a word to translate.": "Írjon be egy szót a fordításhoz.",
    "Fill with AI (lemma + best translation)": "Kitöltés AI-val (szótári alak + legjobb fordítás)",
    "Enter a word to fill with AI.": "Írjon be egy szót az AI-val való kitöltéshez.",
    "Source equals target — translated to {lang} instead.": "A forrás- és célnyelv megegyezik — helyette fordítva erre: {lang}.",
    "Both word and translation are required.": "A szó és a fordítás megadása is kötelező.",
    "Please select the source language before saving.": "Kérjük, mentés előtt válassza ki a forrásnyelvet.",
    "'{word}' already exists in your dictionary.": "„{word}” már szerepel a szótárában.",
    "'{word}' is already in your dictionary.": "„{word}” már benne van a szótárában.",
    "Already in your dictionary": "Már a szótárában van",
    "Show existing": "Létező megjelenítése",
    "The text was truncated to the first 100 words.": "A szöveg az első 100 szóra lett lerövidítve.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Generálás AI-val",
    "Regenerate with AI": "Újragenerálás AI-val",
    "Definition 2": "2. meghatározás",
    "No definition yet": "Még nincs meghatározás",
    "Generate one with AI, or write your own with Edit.": "Generáljon egyet AI-val, vagy írja meg a sajátját a Szerkesztés gombbal.",
    "There is no word to define.": "Nincs meghatározandó szó.",
    "Bold": "Félkövér",
    "Italic": "Dőlt",
    "Heading": "Címsor",
    "List": "Lista",
    "API key missing": "Hiányzó API-kulcs",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Először adja meg a {ai} API-kulcsát a Beállítások → Fordítás és AI → AI menüpontban.",
    "Generating definition…": "Meghatározás generálása…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Címkék — {count} szó",
    "New tag name…": "Új címke neve…",
    "Add Tag": "Címke hozzáadása",
    "Apply Selected to All": "Kijelöltek alkalmazása az összesre",
    "Remove Selected": "Kijelöltek eltávolítása",
    "(partial)": "(részleges)",
    "use(s)": "használat",
    "Tags marked ✓ apply to all selected words.": (
        "A ✓ jellel jelölt címkék az összes kijelölt szóra vonatkoznak."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "A ◐ (részleges) azt jelenti, hogy csak néhányuk rendelkezik a címkével."
    ),
    "Select tag(s) in the list first.": "Először válasszon ki címké(ke)t a listából.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Lomtár — Törölt elemek",
    "Delete Permanently": "Végleges törlés",
    "Cleanup Old Items…": "Régi elemek tisztítása…",
    "{n} selected": "{n} kijelölve",
    "The bin is empty. Deleted words will appear here.":
        "A lomtár üres. A törölt szavak itt fognak megjelenni.",
    "The bin is empty. Deleted texts will appear here.":
        "A lomtár üres. A törölt szövegek itt fognak megjelenni.",
    "deleted {when}": "törölve: {when}",
    "(empty)": "(üres)",
    "Untitled": "Cím nélkül",
    "Auto-deletes soon": "Hamarosan automatikusan törlődik",
    "Auto-deletes in {n} day": "Automatikus törlés {n} nap múlva",
    "Auto-deletes in {n} days": "Automatikus törlés {n} nap múlva",
    "Auto-deletes in {n} days (genitive)": "Automatikus törlés {n} nap múlva",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Véglegesen töröl {count} elemet? Ez a művelet nem vonható vissza.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Korábbi verzió helyreállítása",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Az adatbázisról minden változtatás után automatikusan biztonsági mentés készül. "
        "Válasszon ki egy korábbi verziót az alábbiak közül a helyreállításhoz."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Még nincsenek mentett verziók. "
        "Biztonsági mentés automatikusan készül minden változtatás után."
    ),
    "Restore this version": "Ezen verzió helyreállítása",
    "Today": "Ma",
    "Yesterday": "Tegnap",
    "Most recent": "Legújabb",
    "Before your last restore": "A legutóbbi helyreállítás előtt",
    "today": "ma",
    "yesterday": "tegnap",
    "today {time}": "ma {time}",
    "yesterday {time}": "tegnap {time}",
    "the version from {date}": "a(z) {date} dátumú verzió",
    "the version from just before your last restore": "a közvetlenül a legutóbbi helyreállítás előtti verzió",
    "Restore Version": "Verzió helyreállítása",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Helyreállítja ezt: {phrase}?\n\nA jelenlegi adatai először mentésre kerülnek, így ezt visszavonhatja."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Az adatbázisa helyreállítva erre: {phrase}.\n\n"
        "Meggondolta magát? A visszavonáshoz állítsa helyre ezt: „{before}”."
    ),
    "Restore Error": "Helyreállítási hiba",
    "Sorry, that version could not be restored:\n{error}": "Sajnáljuk, ezt a verziót nem sikerült helyreállítani:\n{error}",
    "Remove Version": "Verzió eltávolítása",
    "Remove {phrase}?": "Eltávolítja ezt: {phrase}?",
    "Remove Error": "Eltávolítási hiba",
    "Sorry, that version could not be removed:\n{error}": "Sajnáljuk, ezt a verziót nem sikerült eltávolítani:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Szöveg generálása",
    "Title…": "Cím…",
    "Generated text appears here…": "A generált szöveg itt fog megjelenni…",
    "Save to Texts": "Mentés a Szövegek közé",
    "Save failed": "A mentés nem sikerült",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Mentés hangfájlként",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Egyetlen MP3 fájl generálása {count} szó/fordítás párból."
    ),
    "Generating audio…": "Hang generálása…",
    "Compiling final audio file…": "Végső hangfájl összeállítása…",
    "Processed: {word}": "Feldolgozva: {word}",
    "Choose File && Start": "Fájl kiválasztása és indítás",
    "Cancelled.": "Megszakítva.",
    "Audio saved": "Hang mentve",
    "Audio file saved to:\n{path}": "A hangfájl mentve ide:\n{path}",
    "Audio Error": "Hanghiba",
    "Failed to save audio:\n{error}": "Nem sikerült elmenteni a hangot:\n{error}",
    "Cancelling…": "Megszakítás…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Importálás Excelből",
    "Row": "Sor",
    "Word 1": "1. szó",
    "Language 1": "1. nyelv",
    "Word 2": "2. szó",
    "Language 2": "2. nyelv",
    "Action": "Művelet",
    "Details": "Részletek",
    "Add": "Hozzáadás",
    "Update": "Frissítés",
    "Skip": "Kihagyás",
    "All": "Összes",
    "To add": "Hozzáadandó",
    "To update": "Frissítendő",
    "Skipped": "Kihagyva",
    "Unrecognized": "Felismeretlen",
    "Only recognized languages": "Csak a felismert nyelvek",
    "Exclude rows whose language wasn't recognized.":
        "A nem felismert nyelvű sorok kizárása.",
    "Unrecognized language — will be imported exactly as written.":
        "Felismeretlen nyelv — pontosan a leírtak szerint kerül importálásra.",
    "Select all": "Összes kijelölése",
    "Activity log": "Tevékenységnapló",
    "Export log…": "Napló exportálása…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Exportálás…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Szöveg hozzáadása",
    "Write": "Írás",
    "AI Generate": "AI generálás",
    "Wikipedia": "Wikipédia",
    "From URL": "URL-ről",
    "Language:": "Nyelv:",
    "Level:": "Szint:",
    "Topic:": "Téma:",
    "Topic…": "Téma…",
    "Adapt to my level": "Igazítás a szintemhez",
    "Load entries": "Bejegyzések betöltése",
    "Add feed…": "Hírforrás hozzáadása…",
    "Ideas:": "Ötletek:",
    "Short (~100 words)": "Rövid (~100 szó)",
    "Medium (~250 words)": "Közepes (~250 szó)",
    "Long (~500 words)": "Hosszú (~500 szó)",
    "Travel": "Utazás",
    "Food": "Étel",
    "Daily routine": "Napi rutin",
    "A short story": "Rövid történet",
    "News": "Hírek",
    "Dialogue at a café": "Párbeszéd egy kávézóban",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Írja be vagy illessze be a szöveget ide, vagy töltsön le egyet a fenti fülek segítségével…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Legújabbak elöl",
    "Oldest first": "Légregebbi elöl",
    "Title A–Z": "Cím A–Z",
    "All languages": "Összes nyelv",
    "All levels": "Összes szint",
    "All topics": "Összes téma",
    "No matching texts": "Nincsenek egyező szövegek",
    "Try a different search or language filter.": "Próbáljon meg egy másik keresést vagy nyelvszűrőt.",
    "New text (write or paste)": "Új szöveg (írás vagy beillesztés)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Szöveg beszerzése az internetről (AI / Wikipédia / URL / RSS)"
    ),
    "Import .txt file(s)": ".txt fájl(ok) importálása",
    "Read aloud": "Felolvasás",
    "Translate text": "Szöveg fordítása",
    "Hide translation": "Fordítás elrejtése",
    "Focus mode": "Fókusz mód",
    "Exit focus mode": "Kilépés a fókusz módból",
    "Paper mode: off": "Papír mód: ki",
    "Paper: white (click for sepia)": "Papír: fehér (kattintson a szépiához)",
    "Paper: sepia (click to turn off)": "Papír: szépia (kattintson a kikapcsoláshoz)",
    "Save Changes": "Változtatások mentése",
    "Previous text": "Előző szöveg",
    "Next text": "Következő szöveg",
    "From words: {words}": "Szavakból: {words}",
    "Created {date}": "Létrehozva: {date}",
    "Unsaved changes": "Nem mentett változtatások",
    "Save changes to '{title}'?": "Mentse a változtatásokat ide: „{title}”?",
    "Changes saved.": "A változtatások elmentve.",
    "'{title}' moved to bin.": "„{title}” a lomtárba helyezve.",
    "Reader": "Olvasó",
    'Pronounce "{word}"': '„{word}” kiejtése',
    'Add "{word}" to vocabulary': '„{word}” hozzáadása a szókincshez',
    "Read from here": "Olvasás innentől",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Forrás",
    "Added manually": "Kézzel hozzáadva",
    "From reader": "Az olvasóból",
    "Created at": "Létrehozva",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Hozzáadás AI-val (szótári alak + legjobb fordítás)",
    "Add to vocabulary as is": "Hozzáadás a szókincshez jelenlegi formájában",
    "Thinking…": "Gondolkodás…",
    "'{pair}' is already in your dictionary.": "„{pair}” már benne van a szótárában.",
    "{label} — {translation} · added": "{label} — {translation} · hozzáadva",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Felhőszinkronizálás",
    "Last sync": "Utolsó szinkronizálás",
    "Pending": "Folyamatban",
    "never": "soha",
    "just now": "épp most",
    "{n} min ago": "{n} perce",
    "Connected": "Csatlakoztatva",
    "Not connected": "Nincs csatlakoztatva",
    "change": "változtatás",
    "changes": "változtatás",
    "deletion": "törlés",
    "deletions": "törlés",
    "everything synced": "minden szinkronizálva",
    "Initial sync has not completed yet.": "Kezdeti szinkronizálás még nem fejeződött be.",
    "Sync Now": "Szinkronizálás most",
    "Syncing…": "Szinkronizálás…",
    # Local-only promo state
    "{words} and {texts}": "{words} és {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Itt {items} van elmentve. Jelentkezzen be a biztonságos megőrzésükhöz és tanuláshoz minden eszközén.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Csak helyi — jelentkezzen be a szavak eszközök közötti szinkronizálásához",
    "Sign in to sync across devices": "Bejelentkezés az eszközök közötti szinkronizáláshoz",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Üdvözöljük",
    "Welcome to {app}": "Üdvözöljük a {app} alkalmazásban",
    "Sync across your devices": "Szinkronizálás az eszközei között",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Jelentkezzen be a szókincsének biztonságos megőrzéséhez és tanulásához minden eszközén.",
    "Automatic cloud backup": "Automatikus felhőalapú biztonsági mentés",
    "Your words follow you to every computer.":
        "A szavai elkísérik Önt minden számítógépre.",
    "Never lose your progress.": "Soha ne veszítse el a haladását.",
    "Study anywhere": "Tanuljon bárhol",
    "Pick up right where you left off.":
        "Folytassa pontosan ott, ahol abbahagyta.",
    "Your data is yours — sign in only to sync it.":
        "Az adatai az Önéi — a bejelentkezés csak a szinkronizáláshoz szükséges.",
    "Sign in / Create account": "Bejelentkezés / Fiók létrehozása",
    "Continue on this device": "Folytatás ezen az eszközön",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Lejátszási beállítások",
    "Previous word": "Előző szó",
    "Next word": "Következő szó",
    "Stop playback": "Lejátszás leállítása",
    "Pause between words": "Szünet a szavak között",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Nincs mit olvasni.",
    "Previous sentence": "Előző mondat",
    "Next sentence": "Következő mondat",
    "Reading speed": "Olvasási sebesség",
    "Sentence {n} / {total}": "{n} / {total} mondat",
    "buffering…": "pufferelés…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Áttekintés",
    "Learning status": "Tanulási állapot",
    "Activity": "Tevékenység",
    "Review activity": "Áttekintési tevékenység",
    "Breakdown": "Részletezés",
    "Total words": "Összes szó",
    "Mastered": "Elsajátítva",
    "In progress": "Folyamatban",
    "Languages": "Nyelvek",
    "Current streak": "Jelenlegi sorozat",
    "Added this week": "Ezen a héten hozzáadva",
    "Definitions written": "Megírt meghatározások",
    "Status distribution": "Állapot eloszlása",
    "Words added over time": "Szavak száma az idő múlásával",
    "Activity calendar": "Tevékenységi naptár",
    "Reviews over time": "Áttekintések száma az idő múlásával",
    "Review calendar": "Áttekintési naptár",
    "Most reviewed words": "Legtöbbet áttekintett szavak",
    "Top language pairs": "Legnépszerűbb nyelvpárok",
    "Top tags": "Legnépszerűbb címkék",
    "Reviewed this week": "Ezen a héten áttekintve",
    "Total reviews": "Összes áttekintés",
    "Review streak": "Áttekintési sorozat",
    "{pct}% of all words": "az összes szó {pct}%-a",
    "actively learning": "aktívan tanulva",
    "{n} pairs": "{n} pár",
    "best {n}d": "rekord: {n} nap",
    "{n} today": "{n} ma",
    "listens logged": "meghallgatás rögzítve",
    "keep it going": "csak így tovább!",
    "Day": "Nap",
    "Week": "Hét",
    "Month": "Hónap",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Szövegfájlok importálása",
    "Text files (*.txt);;All files (*)": "Szövegfájlok (*.txt);;Minden fájl (*)",
    "Language of the imported text(s):": "Az importált szöveg(ek) nyelve:",
    "Imported {count} text(s).": "{count} szöveg importálva.",
    "Some files could not be imported:": "Néhány fájlt nem sikerült importálni:",
    "Import failed:\n{error}": "Importálás nem sikerült:\n{error}",
    "Failed to save text:\n{error}": "Nem sikerült elmenteni a szöveget:\n{error}",
    "Failed to delete text:\n{error}": "Nem sikerült törölni a szöveget:\n{error}",
    "Delete Text": "Szöveg törlése",
    "Delete '{title}'?": "Törli ezt: „{title}”?",
    "Unsupported language: {language}": "Nem támogatott nyelv: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Nem támogatott nyelv: {lang}. Válasszon egyet a listából.",
    "(empty)": "(üres)",
    "unsupported language": "nem támogatott nyelv",
    "unreadable text": "olvashatatlan szöveg",
    "Skipped {n} {noun} ({reasons}).": "Kihagyva: {n} {noun} ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Néhány szöveget nem sikerült felolvasni — nem támogatott nyelv "
        "vagy olvashatatlan karakterek.",
    "Edit text": "Szöveg szerkesztése",
    "Done editing": "Szerkesztés kész",
    "Delete text": "Szöveg törlése",
    "Save Changes": "Változtatások mentése",
    "Paper mode": "Papír mód",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Kattintson a „+” gombra szöveg írásához vagy beillesztéséhez, a földgömbre egy szöveg\n"
        "az internetről való letöltéséhez, vagy jelöljön ki szavakat a Szavak nézetben,\n"
        "és használja a „Szöveg” műveletet egy tanulási szöveg generálásához."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Keresés a Wikipédián a kiválasztott nyelven. Kattintson egy eredményre a cikk betöltéséhez; használja az „Igazítás a szintemhez” gombot az egyszerűsítéshez."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Hírcsatornák a kiválasztott nyelvhez. Töltsön be egy csatornát, majd kattintson duplán egy bejegyzésre a teljes szöveg letöltéséhez. Adjon hozzá saját csatornákat a „Hírforrás hozzáadása…” gombbal."
    ),
    "Length:": "Hossz:",
    "Search Wikipedia (in the selected language)…": "Keresés a Wikipédián (a kiválasztott nyelven)…",
    "Double-click an entry to load its full text.": "Kattintson duplán egy bejegyzésre a teljes szöveg betöltéséhez.",
    "Working…": "Feldolgozás…",
    "Show the {count} result(s) again": "A(z) {count} eredmény megjelenítése ismét",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "A(z) {ai} API-kulcs nincs beállítva. Állítsa be a Beállítások → Fordítás és AI → AI menüpontban."
    ),
    "Generating with {ai}…": "Generálás a következõvel: {ai}…",
    'Fetching "{title}"…': '„{title}” letöltése…',
    "(yours)": "(az Önégé)",
    "Fetching the full text…": "A teljes szöveg letöltése…",
    "Add feed": "Hírforrás hozzáadása",
    "Feed name:": "Hírforrás neve:",
    "Feed URL:": "Hírforrás URL-je:",
    "Failed to save the text.": "Nem sikerült elmenteni a szöveget.",
    "Failed to save the text: {error}": "Nem sikerült elmenteni a szöveget: {error}",
    "'{title}' saved.": "„{title}” elmentve.",
    "(untitled)": "(cím nélkül)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Az alábbi szöveg átírása a kiválasztott CEFR szinthez a következõvel: {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Napló exportálása",
    "Activity Log": "Tevékenységnapló",
    "Warnings & errors": "Figyelmeztetések és hibák",
    "Errors only": "Csak hibák",
    "Find…": "Keresés…",
    "Open log folder": "Naplózási mappa megnyitása",
    "Export diagnostics": "Diagnosztika exportálása",
    "Clear the log file? This cannot be undone.":
        "Törli a naplófájlt? Ez a művelet nem vonható vissza.",
    "Could not create the diagnostics file.":
        "Nem sikerült létrehozni a diagnosztikai fájlt.",
    "Diagnostics saved to:\n{path}": "Diagnosztika elmentve ide:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Írja le a problémát**\n\n\n**A reprodukálás lépései**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nKérjük, csatolja a diagnosztikai fájlt:\n{path}\n",
    "Bug report: ": "Hibabejelentés: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Kicsinyítés",
    "Maximize": "Teljes méret",
    "Restore": "Visszaállítás",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Vezérlők megjelenítése",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Nincs szín",
    "None": "Nincs",
    "Choose Color": "Szín kiválasztása",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Felhőszinkronizálás: tétlen",
    "Failed to open table:\n{error}": "Nem sikerült megnyitni a táblázatot:\n{error}",
    "Failed to save template:\n{error}": "Nem sikerült elmenteni a sablont:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Megjelenítés / elrejtés",
    "Excel options": "Excel beállítások",
    "CSV options": "CSV beállítások",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "A fejlécsorok a fájl tetejére íródnak — az importáló eszközök, mint "
        "az Anki beolvassák őket (pl. #separator:tab, #html:true). "
        "Maguk az oszlopnevek nem íródnak ki."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Másoljon egy .ttf fájlt az alkalmazás betűtípus mappájába, és használja azt"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Csak a szavak MP3 fájlba történő exportálásakor használatos. "
        "Maga a hang a Hang fülön állítható be."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "A szavak kiejtéséhez használt hang: az alkalmazáson belüli Felolvasás "
        "és MP3 exportálás során. A gTTS ingyenes, és nem igényel beállítást. A Google Cloud TTS "
        "szolgáltatási fiók JSON kulcsot igényel (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) és engedélyezett számlázást a projekten — "
        "az ingyenes havi kereten belüli használatért nem kell fizetni."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Egy szó teljes meghallgatása a Felolvasásban lépteti azt "
        "az ismerősségi létrán: Új → Áttekintés alatt → Tanulás alatt → Elsajátítva. "
        "Minden szám az adott szint eléréséhez szükséges befejezett meghallgatások száma. "
        "A manuálisan Elsajátítva vagy Figyelmen kívül hagyva állapotúra állított szavak "
        "soha nem változnak meg, és egy szó állapota soha nem lép visszafelé."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Kész .xlsx mentése a megfelelő fejlécekkel és példasorokkal"
    ),
    "Google Translate (free)": "Google Fordító (ingyenes)",
    "Google Translate is free and needs no API key.": (
        "A Google Fordító ingyenes, és nem igényel API-kulcsot."
    ),
    "Usage": "Használat",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Kattintson a mezőre, és nyomja meg a kívánt billentyűkombinációt — ez bárhonnan "
        "megnyitja a 'Szó hozzáadása' ablakot a vágólap tartalmával. "
        "Hagyja üresen a kikapcsoláshoz."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Waylanden ez a gyorsbillentyű a munkakörnyezetben regisztrálódik, "
        "és megjelenik a rendszer billentyűzet-beállításaiban."
    ),
    "Add Word hotkey": "„Szó hozzáadása” gyorsbillentyű",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "A globális „Szó hozzáadása” gyorsbillentyű nem érhető el ebben a "
        "környezetben. Lásd a Beállítások ▸ Rendszer menüpontot a lehetőségekért."
    ),
    "The global Add-Word hotkey isn't available in the "
    "Flatpak sandbox on Wayland.": (
        "A globális „Szó hozzáadása” gyorsbillentyű nem érhető el a "
        "Flatpak homokozóban Wayland alatt."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "A globális „Szó hozzáadása” gyorsbillentyű még nem támogatott ezen "
        "a Wayland munkakörnyezetben."
    ),
    "To enable it, use any one of these:": "Az engedélyezéséhez használja az alábbiak egyikét:",
    "Log in to an X11 session instead of Wayland":
        "jelentkezzen be X11 munkamenetbe Wayland helyett",
    "Use a GNOME session — the global hotkey works there":
        "használjon GNOME munkamenetet — a globális gyorsbillentyű ott működik",
    "Install the AppImage version — it runs outside the sandbox":
        "telepítse az AppImage verziót — az a homokozón kívül fut",
    "Download the AppImage": "AppImage letöltése",
    "Add font…": "Betűtípus hozzáadása…",
    "TrueType fonts (*.ttf)": "TrueType betűtípusok (*.ttf)",
    "Could not copy the font file:\n{error}": "Nem sikerült másolni a betűtípusfájlt:\n{error}",
    "Save import template…": "Importálási sablon mentése…",
    "Excel files (*.xlsx)": "Excel fájlok (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "A sablon elmentve ide:\n{path}\n\n"
        "Töltse ki a szavaival (cserélje ki a példasorokat), "
        "és importálja az alkalmazás menüjén keresztül → Excel importálása az adatbázisba."
    ),
    "Could not save the template:\n{error}": "Nem sikerült elmenteni a sablont:\n{error}",
    "Background image": "Háttérkép",
    "Images (*.png *.jpg *.jpeg)": "Képek (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON fájlok (*.json)",
    "Connection successful! ✅": "Sikeres csatlakozás! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Nem sikerült csatlakozni. Ellenőrizze az URL-t/kulcsot és az internetkapcsolatot."
    ),
    "Connection test failed:\n{error}": "A kapcsolat tesztelése nem sikerült:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} karakter ebben az időszakban",
    "{count} characters used": "{count} karakter felhasználva",
    "Autostart": "Automatikus indítás",
    "Could not update autostart entry:\n{error}": "Nem sikerült frissíteni az automatikus indítási bejegyzést:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "A Google Cloud TTS van kiválasztva, de {problem}\n\n"
        "A hang visszatér a gTTS használatára, amíg ezt nem javítja."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "szó",
    "words": "szó",
    "words (genitive)": "szó",
    "text": "szöveg",
    "texts": "szöveg",
    "texts (genitive)": "szöveg",
    "tag": "címke",
    "tags": "címke",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Fordítás",
    "AI": "AI",
    "Save As": "Mentés másként",
    "Save Audio As": "Hang mentése másként",
    "Save PDF As": "PDF mentése másként",
    "Added": "Hozzáadva",
    "Updated": "Frissítve",
    "Failed": "Sikertelen",
    "Checking…": "Ellenőrzés…",
    "Cleanup": "Tisztítás",
    "Permanent Delete": "Végleges törlés",
    "No word": "Nincs szó",
    "Category": "Kategória",
    "Bin": "Lomtár",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Összes címke",
    "Filter by tag — {tag}": "Szűrés címke alapján — {tag}",
    "(showing first {n})": "(első {n} megjelenítve)",
    "Texts: {total}": "Szövegek: {total}",
    "Deleted with {n} error(s).": "Törölve {n} hibával.",
    "Failed to update: {error}": "Nem sikerült frissíteni: {error}",
    "Failed to export:\n{error}": "Nem sikerült exportálni:\n{error}",
    "Failed to export PDF:\n{error}": "Nem sikerült a PDF exportálása:\n{error}",
    "Failed to export TXT:\n{error}": "Nem sikerült a TXT exportálása:\n{error}",
    "PDF saved to {path}": "PDF elmentve ide: {path}",
    "TXT file saved to {path}": "TXT fájl elmentve ide: {path}",
    "Template saved to {path}": "Sablon elmentve ide: {path}",
    "{format} file saved to {path}": "{format} fájl elmentve ide: {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Helyette gTTS használata — {problem}\nJavítsa ki a Beállítások → Felolvasás → Hang menüpontban."
    ),
    "Failed to load the database:": "Nem sikerült betölteni az adatbázist:",
    "{selected} of {total} selected": "{selected} / {total} kijelölve",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "Oldalsáv összecsukása",
    "Expand sidebar": "Oldalsáv kibontása",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Mentve: {when} · {summary}",
    "the version from {date}": "a(z) {date} dátumú verzió",
    "Sorry, that version could not be restored:\n{error}": (
        "Sajnáljuk, ezt a verziót nem sikerült helyreállítani:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Sajnáljuk, ezt a verziót nem sikerült eltávolítani:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Helyreállít {count} elemet?",
    "Restored {count} item(s).": "{count} elem helyreállítva.",
    "Select item(s) to restore.": "Válassza ki a helyreállítandó eleme(ke)t.",
    "Permanently deleted {count} item(s).": "{count} elem véglegesen törölve.",
    "Select item(s) to delete permanently.": "Válassza ki a véglegesen törlendő eleme(ke)t.",
    "No items older than {n} days found.": "Nem találhatók {n} napnál régebbi elemek.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Véglegesen törli a több mint {days} napja törölt elemeket?\n\n"
        "Ez a művelet nem vonható vissza!"
    ),
    "Permanently deleted {count} old item(s).": "{count} régi elem véglegesen törölve.",
    "Failed to load deleted items:\n{error}": "Nem sikerült betölteni a törölt elemeket:\n{error}",
    "Failed to count old items:\n{error}": "Nem sikerült megszámlálni a régi elemeket:\n{error}",
    "Failed to cleanup:\n{error}": "A tisztítás nem sikerült:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Excel importálása",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Várt oszlopok: Language1, Language2, Word1, Word2 — elnevezve a fejlécsorban, "
        "vagy fejléc nélkül az első négy oszlop ebben a sorrendben. "
        "A kész sablon elérhető az alkalmazás menüjében → Importálási sablon mentése."
    ),
    "All ({n})": "Összes ({n})",
    "To add ({n})": "Hozzáadandó ({n})",
    "To update ({n})": "Frissítendő ({n})",
    "Skipped ({n})": "Kihagyva ({n})",
    "Unrecognized ({n})": "Felismeretlen ({n})",
    " · {n} with unrecognized language": " · {n} felismeretlen nyelvvel",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} sor: {add} új · {update} frissítés · {skip} kihagyva"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Tekintse át a javasolt változtatásokat, majd importálja a kijelölt sorokat."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Nincs mit importálni — nem találhatók új vagy megváltozott bejegyzések."
    ),
    "Analyzing file…": "Fájl elemzése…",
    "Could not read the Excel file — see the activity log.": (
        "Nem sikerült beolvasni az Excel fájlt — lásd a tevékenységnaplót."
    ),
    "Analysis failed — see the activity log.": "Az elemzés nem sikerült — lásd a tevékenységnaplót.",
    "Import failed": "Importálás nem sikerült",
    "Import failed — see the activity log.": "Az importálás nem sikerült — lásd a tevékenységnaplót.",
    "Importing…": "Importálás…",
    "Importing {count} item(s)…": "{count} elem importálása…",
    "Import {count} Item(s)": "{count} elem importálása",
    "Import finished:": "Importálás befejeződött:",
    "Backup failed — see the activity log.": "Biztonsági mentés nem sikerült — lásd a tevékenységnaplót.",
    "{n} added": "{n} hozzáadva",
    "{n} updated": "{n} frissítve",
    "{n} failed": "{n} sikertelen",
    "{n} failed.": "{n} sikertelen.",
    "Export Import Log": "Importálási napló exportálása",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Meghatározás — {word}",
    "Failed to save definition:\n{error}": "Nem sikerült elmenteni a meghatározást:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Szerkesztés — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Nem sikerült elmenteni a szót:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "A kiválasztott címke/címkék hozzárendelése minden kijelölt szóhoz"
    ),
    "Failed to add tag:\n{error}": "Nem sikerült hozzáadni a címkét:\n{error}",
    "Failed to apply tags:\n{error}": "Nem sikerült alkalmazni a címkéket:\n{error}",
    "Failed to remove tags:\n{error}": "Nem sikerült eltávolítani a címkéket:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Szöveget generál AI-val az alábbi Nyelv, Szint és Téma mezők használatával. "
        "Válasszon egy téma zsetont, vagy írja be a sajátját."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "{language} nyelvű szöveg generálása {count} szóból a következõvel: {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Írjon be vagy illesszen be egy szöveget az alábbi szerkesztőbe, adjon neki egy címet, "
        "állítsa be a nyelvet — majd mentse el."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Kinyeri az olvasható cikkszöveget bármely weboldalról. "
        "A bejelentkezés mögötti vagy tisztán JavaScriptre épülő oldalak nem biztos, hogy működnek."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "Meghatározás megtekintése (dupla kattintás)",
    "Read selected words aloud": "Kijelölt szavak felolvasása",
    "Toggle favorite": "Kedvenc ki/bekapcsolása",
    "Add / remove tags": "Címkék hozzáadása / eltávolítása",
    "Edit word": "Szó szerkesztése",
    "Copy words": "Szavak másolása",
    "Generate text from selection": "Szöveg generálása a kijelölésből",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "PDF fájlok (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excel fájlok (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV fájlok (*.csv)",
    "Text files (*.txt)": "Szövegfájlok (*.txt)",
    "MP3 files (*.mp3)": "MP3 fájlok (*.mp3)",
    "Open Excel Table": "Excel táblázat megnyitása",
    "Save Import Template": "Importálási sablon mentése",

    # Cloud sync status
    "Cloud sync": "Felhőszinkronizálás",
    "Not connected. Check internet or credentials": "Nincs csatlakoztatva. Ellenőrizze az internetet vagy a hitelesítő adatokat",
    "Syncing with cloud…": "Szinkronizálás a felhővel…",
    "Sync completed successfully": "A szinkronizálás sikeresen befejeződött",
    "Sync enabled but not connected. Check settings.": "A szinkronizálás engedélyezve van, de nincs csatlakoztatva. Ellenőrizze a beállításokat.",
    "idle": "tétlen",
    "syncing": "szinkronizálás",
    "success": "sikeres",
    "error": "hiba",

    # Chart empty states
    "No data yet": "Még nincsenek adatok",
    "No activity yet": "Még nincs tevékenység",
    "Not enough activity yet": "Még nincs elég tevékenység",

    # Settings tabs
    "APIs": "API-k",
    "Audio (MP3)": "Hang (MP3)",
    "Sync": "Szinkronizálás",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI API-kulcs (.env)",
    "Google API key (.env)": "Google API-kulcs (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Használat alapján számlázva — szerezzen kulcsot itt: <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modellek: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API használat — lásd: <a href="https://platform.openai.com/usage">műszerfal</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Ingyenes csomag elérhető — szerezzen kulcsot itt: <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modellek: gemini-2.5-flash, gemini-2.5-flash-lite… API használat — lásd: <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Szerezzen kulcsot itt: <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Ingyenes kulcsokhoz használja a https://api-free.deepl.com/v2/translate címet.',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Készítsen elő egy Excel fájlt a következő oszlopokkal: <b>Language1, Language2, Word1, Word2</b> — így elnevezve a fejlécsorban (a többletoszlopok figyelmen kívül maradnak), vagy fejléc nélkül az első négy oszlopban pontosan ebben a sorrendben.</li><li>Nyissa meg az alkalmazás menüjét → <i>Excel importálása az adatbázisba…</i> és válassza ki a fájlt.</li><li>Tekintse át a javasolt sorokat, és kattintson az <i>Importálás</i> gombra.</li></ol>",

    # About dialog
    "created by": "készítette:",
    "Version": "Verzió",
    "Build": "Verziószám",
    "Your personal vocabulary companion": "Az Ön személyes szókincstársa",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Építse, tanulja és jegyezze meg szókincsét különböző nyelveken — felhőszinkronizálással, AI-segített meghatározásokkal, fordításokkal, szövegfelolvasással és rugalmas exportálással.",
    "Source code": "Forráskód",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Az Ön személyes szókincstársa felhőszinkronizálással, AI meghatározásokkal, fordításokkal, szövegfelolvasással és exportálási lehetőségekkel.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "A GNU Affero General Public License v3.0 licenc alatt. Ezt a megjelölést meg kell őrizni (AGPL §7).",
    "Found a bug or have an idea?": "Hibát talált vagy van egy ötlete?",
    "Report an issue": "Probléma bejelentése",
    "What would you like to report?": "Mit szeretne bejelenteni?",
    "A bug or technical problem": "Egy hibát vagy technikai problémát",
    "Creates a report with app diagnostics to send to the developers.":
        "Létrehoz egy jelentést az alkalmazás diagnosztikájával, amelyet elküldhet a fejlesztőknek.",
    "Inappropriate AI-generated content": "Nem megfelelő AI által generált tartalom",
    "Report a definition, text, or translation the AI produced.": "Bejelenthet egy AI által készített meghatározást, szöveget vagy fordítást.",
    "Report: inappropriate AI-generated content":
        "Bejelentés: nem megfelelő AI által generált tartalom",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Kérjük, írja le az AI által generált tartalmat, amelyet bejelent.\n\n"
        "Hol jelent meg (meghatározás / generált szöveg / szófordítás):\n"
        "A szó vagy szöveg:\n"
        "Miért nem megfelelő:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "A nem megfelelő AI által generált tartalom bejelentéséhez írjon nekünk a(z) {email} címre.",

    # Support dialog
    "Support": "Támogatás",
    "Support Lingueez": "Lingueez támogatása",
    "Lingueez is free and open-source.": "A Lingueez ingyenes és nyílt forráskódú.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Ha tetszik a Lingueez és hasznosnak találja, egy egyszeri hozzájárulás segít fedezni az opcióként elérhető felhőszinkronizálás mögötti szerverek költségeit, és támogatja a folyamatos fejlesztést. Nincsenek fizetős korlátok — minden funkció ingyenes marad.",
    "Support Lingueez's development": "A Lingueez fejlesztésének támogatása",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "A Stripe opció egyszeri — nincs előfizetés. A fizetéseket a Stripe vagy a GitHub biztonságosan kezeli.",

    # Updates
    "Updates": "Frissítések",
    "Check for updates": "Frissítések keresése",
    "You're up to date.": "A legújabb verziót használja.",
    "Update available": "Frissítés érhető el",
    "Update available — v{version}": "Frissítés érhető el — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "A Lingueez {version} elérhető — Ön a {current} verzióval rendelkezik.",
    "Skip this version": "Verzió kihagyása",
    "Later": "Később",
    "Download": "Letöltés",
    "Check for updates on startup": "Frissítések keresése indításkor",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Naponta egyszer ellenőrzi az újabb verziót, és értesíti Önt; "
        "semmi sem kerül automatikusan letöltésre vagy telepítésre.",

    # Misc units
    "in": "hüvelyk",
    " s": " mp",

    # Word statuses (stored in English; only the displayed label is localized)
    "New": "Új",
    "To Learn": "Megtanulandó",
    "Reviewing": "Áttekintés alatt",
    "Ignored": "Mellőzött",
    # "Learning" and "Mastered" are translated above.

    # Table density (settings → Table size)
    "Compact": "Kompakt",
    "Normal": "Normál",
    "Comfortable": "Kényelmes",
    "Spacious": "Tágas",

    # Language names
    "English": "Angol",
    "German": "Német",
    "Spanish": "Spanyol",
    "Ukrainian": "Ukrán",
    "French": "Francia",
    "Italian": "Olasz",
    "Portuguese": "Portugál",
    "Russian": "Orosz",
    "Greek": "Görög",
    "Arabic": "Arab",
    "Bengali": "Bengáli",
    "Cantonese": "Kantonit",
    "Hindi": "Hindi",
    "Japanese": "Japán",
    "Korean": "Koreai",
    "Mandarin": "Mandarin",
    "Polish": "Lengyel",
    "Turkish": "Török",
    "Vietnamese": "Vietnámi",
    "Afrikaans": "Afrikaans",
    "Albanian": "Albán",
    "Amharic": "Amhara",
    "Armenian": "Örmény",
    "Azerbaijani": "Azeri",
    "Basque": "Baszk",
    "Belarusian": "Fehérorosz",
    "Bosnian": "Bosnyák",
    "Bulgarian": "Bolgár",
    "Catalan": "Katalán",
    "Cebuano": "Szebuano",
    "Chichewa": "Csicseva",
    "Chinese": "Kínai",
    "Croatian": "Horvát",
    "Czech": "Cseh",
    "Danish": "Dán",
    "Dutch": "Holland",
    "Estonian": "Észt",
    "Filipino": "Fülöp-szigeteki",
    "Finnish": "Finn",
    "Galician": "Galíciai",
    "Georgian": "Grúz",
    "Gujarati": "Gudzseráti",
    "Haitian Creole": "Haiti kreol",
    "Hausa": "Hausza",
    "Hawaiian": "Hawaii",
    "Hebrew": "Héber",
    "Hmong": "Hmong",
    "Hungarian": "Magyar",
    "Icelandic": "Izlandi",
    "Igbo": "Igbo",
    "Indonesian": "Indonéz",
    "Irish": "Ír",
    "Javanese": "Jávai",
    "Kannada": "Kannada",
    "Kazakh": "Kazah",
    "Khmer": "Kmer",
    "Kinyarwanda": "Kinyarwanda",
    "Kyrgyz": "Kirgiz",
    "Lao": "Lao",
    "Latin": "Latin",
    "Latvian": "Lett",
    "Lithuanian": "Litván",
    "Luxembourgish": "Luxemburgi",
    "Macedonian": "Macedón",
    "Malagasy": "Malagas",
    "Malay": "Malay",
    "Malayalam": "Malajalam",
    "Maltese": "Máltai",
    "Maori": "Maori",
    "Marathi": "Maráthi",
    "Mongolian": "Mongol",
    "Myanmar (Burmese)": "Mianmari (birmai)",
    "Nepali": "Nepáli",
    "Norwegian": "Norvég",
    "Odia": "Orija",
    "Pashto": "Pasto",
    "Persian": "Perzsa",
    "Punjabi": "Pandzsábi",
    "Romanian": "Román",
    "Samoan": "Szamoai",
    "Scots Gaelic": "Skót gael",
    "Serbian": "Szerb",
    "Sesotho": "Szotó",
    "Shona": "Sona",
    "Sindhi": "Szindhi",
    "Sinhala": "Szingaléz",
    "Slovak": "Szlovák",
    "Slovenian": "Szlovén",
    "Somali": "Szomáli",
    "Sundanese": "Szundanéz",
    "Swahili": "Szuahéli",
    "Swedish": "Svéd",
    "Tajik": "Tadzsik",
    "Tamil": "Tamil",
    "Tatar": "Tatár",
    "Telugu": "Telugu",
    "Thai": "Thaiföldi",
    "Turkmen": "Türkmén",
    "Urdu": "Urdu",
    "Uyghur": "Ujgur",
    "Uzbek": "Üzbég",
    "Welsh": "Walesi",
    "Xhosa": "Xhosza",
    "Yiddish": "Jiddis",
    "Yoruba": "Joruba",
    "Zulu": "Zulu",
    # --- Onboarding tour ---
    "Back": "Vissza",
    "Next": "Tovább",
    "Done": "Kész",
    "Show Tour": "Bemutató megjelenítése",
    "Step {n} of {total}": "{n}. lépés / {total}",
    "Your library": "Az Ön könyvtára",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Váltson a Szavak, Szövegek és Statisztika között ezen az oldalsávon.",
    "Add a word": "Szó hozzáadása",
    "Find anything": "Keressen bármit",
    "Search across your words, translations and tags as you type.":
        "Keresés a szavak, fordítások és címkék között gépelés közben.",
    "Add a new word here — its translation can be fetched automatically.":
        "Adjon hozzá egy új szót itt — a fordítása automatikusan letölthető.",
    "Listen and learn": "Hallgassa és tanulja",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Válasszon ki szavakat, és nyomja meg az Olvasás gombot a felolvasásukhoz. "
        "A többszöri meghallgatás lépteti a szavakat az Új, Áttekintés alatt, Tanulás alatt "
        "és végül az Elsajátítva állapotba.",
    "Generate a text": "Szöveg generálása",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Alakítsa át a kijelölt szavakat egy rövid, AI által írt történetté — "
        "a szókincse kontextusban.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "A szókincse szinkronban marad az eszközei között. Kattintson az "
        "állapot megtekintéséhez vagy az azonnali szinkronizáláshoz.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Engedélyezze a felhőszinkronizálást, váltson nyelvet, módosítsa a megjelenést "
        "és még sok mást a Beállítások menüben.",
    # --- Texts tour ---
    "Add texts": "Szövegek hozzáadása",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Írjon be vagy illesszen be egy szöveget, töltsön le egyet az internetről "
        "(AI / Wikipédia / URL / RSS), vagy importáljon .txt fájlokat.",
    "Your texts": "Az Ön szövegei",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Böngésszen a mentett szövegek között, és szűrje őket nyelv, "
        "szint vagy téma alapján.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Hallgasson meg bármilyen szöveget hangosan — és kattintson egy szóra olvasás közben "
        "a fordításának megtekintéséhez vagy a szókincséhez való hozzáadásához.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Párhuzamos fordítás megjelenítése egymás mellett; válassza ki a nyelvet "
        "a mellette lévő nyíllal.",
    "Reading modes": "Olvasási módok",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "A Fókusz mód elrejti a listát, a Papír mód megváltoztatja a "
        "háttért, a Szerkesztés pedig lehetővé teszi a szöveg módosítását.",
    # --- Flashcards tour ---
    "Choose your deck": "Válasszon paklit",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Válassza ki, mi kerüljön a pakliba — áttekintésre váró kártyák, "
        "szavak a jelenlegi szűrőből, a legújabb hozzáadások, "
        "vagy kézzel kiválasztott elemek.",
    "Shape the session": "Formálja a munkamenetet",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Állítsa be az áttekintendő kártyák számát, keverje meg a sorrendjüket, és "
        "ejtesse ki az egyes kártyákat, amint megjelennek és megfordulnak.",
    "Preview the deck": "Pakli előnézete",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "A pontos kártyák, amelyeket a munkamenete tartalmazni fog. Kattintson egy csempére "
        "a meghatározás elolvasásához vagy szerkesztéséhez, vagy a hangszóróra a "
        "szó meghallgatásához.",
    "Review and grade": "Áttekintés és értékelés",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Fordítsa meg az egyes kártyákat, és értékelje, mennyire tudta az adott szót — Nehéz, "
        "Jó vagy Könnyű. Az időközönkénti ismétlés dönt arról, mikor tér vissza "
        "egyes kártya: a könnyű szavak tovább várnak, a nehezek hamarabb "
        "visszatérnek. A Szóköz megfordítja, az 1–3 billentyűk értékelik a kártyát.",
    "Or just listen": "Vagy csak hallgassa",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "A Pakli lejátszása hanganyaggá alakítja a munkamenetet — a kártyák a hanggal "
        "szinkronban haladnak és fordulnak. Bármikor tartson szünetet a kártyák "
        "saját kezű értékeléséhez.",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "A szókincse egy pillantással — összesítések, elsajátított szavak, "
        "nyelvek és a jelenlegi sorozata.",
    "See how your vocabulary has grown over time.":
        "Nézze meg, hogyan növekedett a szókincse az idő múlásával.",
    "Track how much you've reviewed over time.":
        "Kövesse nyomon, mennyit ismételt az idő múlásával.",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Minta: Séta a városban",
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
        "A reggel ragyogó volt, az utcák pedig csendesek. Egy fiatal nő "
        "lassan sétált a régi úton, nézve a magas házakat és a "
        "éppen nyitó kis boltokat. Megállt friss kenyeret "
        "és egy csésze kávét venni, majd átvágott a téren a park felé. "
        "Gyerekek játszottak a folyó közelében, miközben szüleik a közelben lévő "
        "padokon beszélgettek. Leült egy nagy fa alá, kinyitotta a könyvét, és "
        "olvasni kezdett. A történet egy utazóról szólt, aki átkelt a "
        "hegyeken egy régi barátját keresve, akit sok éve nem látott. "
        "Egy idő után felnézett, nézve a folyón lassan úszó csónakokat "
        "és a háztetők felett magasan köröző madarakat. Egy utcazenész "
        "játszani kezdett valahol a közelben, és a halk hangok követték a "
        "gondolatait. Nyugodt és boldog reggel volt, olyan, amilyet a legjobban szeretett.",
    "Demo": "Demó",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Érvénytelen OpenAI API-kulcs. Ellenőrizze a Beállítások → Fordítás és AI → AI → OpenAI menüpontban.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Az OpenAI-fiókjából kifogyott az egyenleg. Töltsön fel egyenleget a "
        "platform.openai.com/account/billing oldalon, vagy váltson az AI "
        "szolgáltatóra Gemini-re a Beállítások → Fordítás és AI → AI menüpontban.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI kéréskorlát elérve. Várjon egy pillanatot, és próbálja újra.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Ismeretlen OpenAI modell. Ellenőrizze a modell nevét a Beállítások → Fordítás és AI → AI → OpenAI menüpontban.",
    "Could not reach OpenAI. Check your internet connection.":
        "Nem sikerült elérni az OpenAI-t. Ellenőrizze az internetkapcsolatot.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "A Gemini kerete kimerült. Az ingyenes szint naponta nullázódik; várjon, "
        "vagy hozzon létre egy új kulcsot a aistudio.google.com/app/apikey oldalon.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Érvénytelen Google API-kulcs. Ellenőrizze a Beállítások → Fordítás és AI → AI → Gemini menüpontban.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Ismeretlen Gemini modell. Ellenőrizze a modell nevét a Beállítások → Fordítás és AI → AI → Gemini menüpontban.",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "A szókincstúrája itt kezdődik",
    "Add your first word — its translation can be fetched automatically.":
        "Adja hozzá az első szavát — a fordítása automatikusan letölthető.",
    "Add your first word": "Első szó hozzáadása",
    "Take the tour": "Bemutató megtekintése",
    "No matching words": "Nincsenek egyező szavak",
    "Try a different search or filter.": "Próbáljon meg egy másik keresést vagy szűrőt.",
    "Clear filters": "Szűrők törlése",
    # --- Texts empty state ---
    "Your reading library starts here": "Az olvasókönyvtára itt kezdődik",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Adjon hozzá egy szöveget az olvasáshoz — írja meg vagy illessze be a sajátját, töltsön le egyet az "
        "internetrol, vagy importáljon egy .txt fájlt.",
    "Add a text": "Szöveg hozzáadása",
    "Fetch from the Internet": "Letöltés az internetről",
    "Import .txt": ".txt importálása",
    # demo text-list stub titles
    "My first story": "Az első történetem",
    "A news article": "Egy hírcikk",
    "A short poem": "Egy rövid vers",
    "Travel notes": "Utazási jegyzetek",
    # demo text-list stub first sentences (shown as the list snippet)
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Egyszer volt, hol nem volt, egy tengerparti kis faluban "
        "élt egy kíváncsi fiatal róka.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "A kutatók új módot találtak annak tanulmányozására, hogyan "
        "változnak és fejlődnek a nyelvek az évszázadok során.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "A szél halkan jár az őszi fák között, "
        "régi és félig elfeledett dalokat hordozva.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Első nap: késő este érkeztünk a városba, és az "
        "utcák még mindig tele voltak meleg fénnyel.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Másik eszközön törölt elemek",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Amíg ez az eszköz offline volt, {n} elemet töröltek a "
        "többi eszközén. Megtartja őket a felhőben, vagy eltávolítja erről az eszközről?",
    "(untitled)": "(cím nélkül)",
    "[Text] {title}": "[Szöveg] {title}",
    "Remove from this device": "Eltávolítás erről az eszközről",
    "Decide later": "Döntés később",
    "Keep & upload": "Megtartás és feltöltés",
    "Not now": "Nem most",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Adja meg az offline profil nevét.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Legfeljebb {max} offline profilt tarthat. Távolítson el egyet egy új hozzáadásához.",
    "New offline profile": "Új offline profil",
    "Profile name:": "Profil neve:",
    "Offline profile": "Offline profil",
    "Rename offline profile": "Offline profil átnevezése",
    "Offline profiles": "Offline profilok",
    "Add offline profile…": "Offline profil hozzáadása…",
    "Profile actions": "Profilműveletek",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Különálló, csak ezen az eszközön lévő könyvtárak saját adatbázissal. Soha nem szinkronizálódnak, és nem igényelnek bejelentkezést.",
    "Default (local)": "Alapértelmezett (helyi)",
    "Rename": "Átnevezés",
    "Delete offline profile": "Offline profil törlése",
    "Enable cloud sync…": "Felhőszinkronizálás engedélyezése…",
    "Could not create the profile.": "Nem sikerült létrehozni a profilt.",
    "Created and switched to “{name}”.": "Létrehozva és átváltva erre: „{name}”.",
    "Deleted “{name}”.": "„{name}” törölve.",
    "Untitled profile": "Cím nélküli profil",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Véglegesen törli a(z) „{name}” offline profilt? Szavai és szövegei csak ezen az eszközön léteznek — nincs felhőmásolat. Az adatbázis először a biztonsági mentések mappába kerül archiválásra, de ez a művelet az alkalmazásban nem vonható vissza.",
    "this profile": "ez a profil",
    "Connect to the internet to merge this profile into your account.": "Csatlakozzon az internethez a profil fiókjába való egyesítéséhez.",
    "Enable cloud sync for this profile": "Felhőszinkronizálás engedélyezése ehhez a profilhoz",
    "Continue": "Folytatás",
    "Upload words": "Szavak feltöltése",
    "Upload texts": "Szövegek feltöltése",
    "Upload & sync": "Feltöltés és szinkronizálás",
    "Could not upload this profile. Your data is unchanged.": "Nem sikerült feltölteni ezt a profilt. Az adatai nem változtak.",
    "“{name}” is now synced to your account.": "A(z) „{name}” profil most már szinkronizálva van a fiókjával.",
    "Everything in this profile is already in your account.": "Minden, ami ebben a profilban van, már megtalálható a fiókjában.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Jelentkezzen be vagy hozzon létre egy fiókot a(z) „{name}” biztonsági mentéséhez és szinkronizálásához az eszközei között. A profil szavai és szövegei feltöltésre kerülnek, és ez lesz a szinkronizált fiókja ezen az eszközön. A rendszer először egy másolatot archivál a biztonsági mentések mappába.",
    "Upload “{name}” to your account": "„{name}” feltöltése a fiókjába",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "A profilja a(z) „{who}” szinkronizált fiókká válik ezen az eszközön, és feltöltődik a felhőbe.",
    "Merge “{name}” into your account": "„{name}” egyesítése a fiókjával",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Ez a fiók már rendelkezik adatokkal ezen az eszközön. A profilja azon szavai és szövegei, amelyek még nincsenek ott, hozzáadódnak — semmi sem íródik felül. A(z) „{name}” profil ezután a biztonsági mentések mappába kerül archiválásra és eltávolításra kerül.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Ez a profil {items} elemet tartalmaz, amely csak ezen az eszközön van mentve. Engedélyezze a felhőszinkronizálást a biztonsági mentéshez és tanuláshoz minden eszközén.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Válassza ki a hozzáadandó elemeket. Átmásolódnak a fiókjába és feltöltődnek a felhőbe. A(z) „{name}” profil ezután a biztonsági mentések mappába kerül archiválásra és eltávolításra kerül.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Elfogadom a <a href=\"{terms}\">Felhasználási feltételeket</a> és az <a href=\"{privacy}\">Adatvédelmi irányelveket</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Kérjük, fogadja el a Felhasználási feltételeket és az Adatvédelmi irányelveket a folytatáshoz.",
    "Updated Terms & Privacy": "Frissített Feltételek és Adatvédelem",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Frissítettük a Felhasználási feltételeinket és az Adatvédelmi irányelveinket. Kérjük, tekintse át és fogadja el őket a fiókja további használatához.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Elfogadom a frissített <a href=\"{terms}\">Felhasználási feltételeket</a> és <a href=\"{privacy}\">Adatvédelmi irányelveket</a>.",
    "Sign out": "Kijelentkezés",
    "I agree": "Elfogadom",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Adatvédelmi irányelvek</a> · <a href=\"{terms}\">Feltételek</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "A folytatással elfogadja a <a href=\"{terms}\">Felhasználási feltételeket</a> és az <a href=\"{privacy}\">Adatvédelmi irányelveket</a>.",
    "Privacy Policy": "Adatvédelmi irányelvek",
    "Terms": "Feltételek",
    "Website": "Weboldal",
    "Contact": "Kapcsolat",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Tanulókártyák",
    "Practice your vocabulary": "Gyakorolja a szókincsét",
    "Due cards": "Esedékes kártyák",
    "Current filter": "Jelenlegi szűrő",
    "Newest": "Legújabbak",
    "Selected words": "Kijelölt szavak",
    "Deck size": "Pakli mérete",
    "Default deck size": "Alapértelmezett pakliméret",
    "Shuffle": "Keverés",
    "Start session": "Munkamenet indítása",
    "Play deck": "Pakli lejátszása",
    "{n} cards ready to review": "{n} kártya áll készen az áttekintésre",
    "No cards due — great job!": "Nincsenek esedékes kártyák — nagyszerű munka!",
    "{n} selected words": "{n} kijelölt szó",
    "No words to practice.": "Nincsenek gyakorlandó szavak.",
    "End session": "Munkamenet befejezése",
    "Listening — pause to review manually":
        "Hallgatás — tartson szünetet a kézi áttekintéshez",
    "Show answer": "Válasz megjelenítése",
    "Hard": "Nehéz",
    "Good": "Jó",
    "Easy": "Könnyű",
    "Space or click to flip": "Szóköz vagy kattintás a megfordításhoz",
    "Card {current} of {total}": "{current} / {total} kártya",
    "{n} correct": "{n} helyes",
    "Session complete!": "Munkamenet befejeződött!",
    "You listened to {n} of {total} cards.": "Meghallgatott {n} / {total} kártyát.",
    "Correct: {n} of {total}": "Helyes: {n} / {total}",
    "New session": "Új munkamenet",
    "Practice hard words": "Nehéz szavak gyakorlása",
    "Hard words": "Nehéz szavak",
    "Hard words cleared!": "Nehéz szavak feldolgozva!",
    "Open Flashcards when Read Aloud starts":
        "Tanulókártyák megnyitása a Felolvasás indításakor",
    "Stop": "Leállítás",
    "Auto-pronounce": "Automatikus kiejtés",
    "Speak each card as it appears and when it flips":
        "Kiejtés minden kártya megjelenésekor és megfordulásakor",
    "Deck preview": "Pakli előnézete",
    "{n} cards": "{n} kártya",
    "Due": "Esedékes",
    "In {n} d": "{n} nap múlva",
    "{n} d": "{n} nap",
    "{n} mo": "{n} hó",
    "{n} y": "{n} év",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez Androidra…",
    "Android app": "Android alkalmazás",
    "Lingueez on Android": "Lingueez Androidon",
    "Take your vocabulary with you": "Vigye magával a szókincsét",
    "Preview of Lingueez on a phone": "A Lingueez előnézete telefonon",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Jelentkezzen be a Lingueez-fiókjával, és a szókincse már ott van — "
        "semmit sem kell beállítani vagy átmásolni.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Jelentkezzen be egy ingyenes Lingueez-fiókba mindkét eszközön, és a szókincse "
        "szinkronizálódik a telefonra — nem kell fájlokat másolgatni.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Jelentkezzen be egy ingyenes Lingueez-fiókba, és a szavai szinkronizálódnak a telefonjára.",
    "Synced both ways": "Kétirányú szinkronizálás",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "A telefonon hozzáadott szavak várják Önt a számítógépen, és "
        "fordítva.",
    "Listen with the screen off": "Hallgassa kikapcsolt képernyővel",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Zárolási képernyő vezérlők, így az áttekintés a zsebében lévő "
        "telefonnal is folytatódik.",
    "Save a word from any app": "Mentsen el egy szót bármelyik alkalmazásból",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Oszzon meg szöveget a Lingueez alkalmazással, és az megérkezik a szókincsébe, "
        "készen a későbbi kitöltésre.",
    "Point your phone's camera at the code":
        "Irányítsa a telefon kameráját a kódra",
    "Get it on Google Play": "Szerezze be a Google Playen",
    "Copy link": "Hivatkozás másolása",
    "Link copied": "Hivatkozás másolva",
    "Lingueez is now on Android": "A Lingueez már Androidon is elérhető",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Jelentkezzen be a Lingueez-fiókjával — a szókincse már ott van.",
    "Dismiss": "Eltüntetés",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Használja Lingueez-fiókját zökkenőmentesen az asztali és Android eszközök között.",
    "Get the app…": "Alkalmazás beszerzése…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Kvíz",
    "Quiz (recall practice)": "Kvíz (felidézés gyakorlása)",
    "Recall your words, one question at a time":
        "Idézze fel a szavait, kérdésről kérdésre",
    "Questions": "Kérdések",
    "Answer with": "Válasz módja",
    "Choices": "Választás",
    "Typing": "Gépelés",
    "Ask": "Kérdezze",
    "Term": "Kifejezés",
    "Mixed": "Vegyes",
    "Auto-advance": "Automatikus továbblépés",
    "Move on by itself after a correct answer": "Helyes válasz után magától lép tovább",
    "Speak the question, then the answer once it is revealed":
        "Mondja ki a kérdést, majd a választ, amint látszik",
    "Start quiz": "Kvíz indítása",
    "questions ready": "kérdés készen áll",
    "Nothing to quiz": "Nincs mit kérdezni",
    "No words match this deck.": "Egy szó sem illik ehhez a paklihoz.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "A kvízhez legalább két szó kell — a rossz válaszok éppen azokból a szavakból "
        "származnak, amelyekre nem kérdezünk rá.",
    "Not enough words": "Nincs elég szó",
    "Add a few more words, or widen the deck.":
        "Vegyen fel még néhány szót, vagy bővítse a paklit.",
    "Question {n} of {total}": "{n}. kérdés / {total}",
    "Missed words": "Elrontott szavak",
    "End quiz": "Kvíz befejezése",
    "Answer in {language}": "Válasz ezen a nyelven: {language}",
    "Type the answer": "Írja be a választ",
    "Check": "Ellenőrzés",
    "Click to continue": "Kattintson a folytatáshoz",
    "See results": "Eredmények",
    "Almost — it is \"{answer}\"": "Majdnem — a helyes válasz: „{answer}”",
    "It is \"{answer}\"": "A helyes válasz: „{answer}”",
    "Now {status}": "Most {status}",
    "Correct": "Helyes",
    "Missed": "Elrontott",
    "Worth another look": "Érdemes átnézni",
    "Again": "Újra",
    "Missed words cleared!": "Az elrontott szavak megvannak!",
    "Perfect run": "Hibátlan kör",
    "Quiz complete": "Kvíz kész",
    "Practice missed": "Hibák gyakorlása",
    "Default number of questions": "Kérdések alapértelmezett száma",
    "Move on after a correct answer": "Továbblépés helyes válasz után",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Válassza ki, mire kérdezzünk rá",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Ugyanazok a paklik, mint a kártyáknál — ismétlésre váró szavak, a jelenlegi "
        "szűrő, a legújabbak vagy kézzel válogatottak — és hány kérdés legyen.",
    "Choices or typing": "Választás vagy gépelés",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "A „Választás” négy lehetőséget kínál; a „Gépelés” a válasz beírását kéri — "
        "nehezebb, de jobb próba. A gépelés megbocsátja az ékezeteket és az apró "
        "elgépeléseket. A „Kérdezze” dönti el, melyik oldalt látja: a kifejezést, a "
        "fordítást vagy vegyesen.",
    "Start, and it counts": "Kezdje el — és számít",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "A sáv a pakli összetételét mutatja állapot szerint. Minden válasz ugyanabba "
        "az ismétlési ütemtervbe folyik be, mint a kártyáknál: a felidézett szó később "
        "tér vissza, az elrontott hamarabb.",
}

# Date names, read by app.i18n. Months in Hungarian usually use nominative or -i suffix.
# Weekdays start on Monday (datetime.weekday(): 0 = Monday).
MONTHS = ["január", "február", "március", "április", "május", "június",
          "július", "augusztus", "szeptember", "október", "november", "december"]
MONTHS_ABBR = ["jan.", "feb.", "márc.", "ápr.", "máj.", "jún.",
               "júl.", "aug.", "szept.", "okt.", "nov.", "dec."]
WEEKDAYS = ["Hétfő", "Kedd", "Szerda", "Csütörtök",
            "Péntek", "Szombat", "Vasárnap"]
WEEKDAYS_ABBR = ["H", "K", "Sze", "Cs", "P", "Szo", "V"]