# Lingueez — Danish (da) translations.
# Keys are English UI strings; values are their Danish equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Dansk"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Annuller",
    "OK": "OK",
    "Close": "Luk",
    "Save": "Gem",
    "Delete": "Slet",
    "Edit": "Rediger",
    "Remove": "Fjern",
    "Add": "Tilføj",
    "Refresh": "Opdater",
    "Import": "Importer",
    "Export": "Eksporter",
    "Search": "Søg",
    "Fetch": "Hent",
    "Browse…": "Gennemse…",
    "Clear": "Ryd",
    "Pause": "Pause",
    "Resume": "Genoptag",
    "Language": "Sprog",
    "Translation": "Oversættelse",
    "Word": "Ord",
    "Status": "Status",
    "Error": "Fejl",
    "Title": "Titel",
    "Topic": "Emne",
    "Level": "Niveau",
    "Generate": "Generer",
    "Generating…": "Genererer…",
    "Translating…": "Oversætter…",
    "Format": "Format",
    "Style": "Stil",
    "Model": "Model",
    "Font": "Skrifttype",
    "Usage": "Forbrug",
    "Translation language": "Oversættelsessprog",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Menu",
    "Open Excel Table…": "Åbn Excel-tabel…",
    "Import Excel to Database…": "Importer Excel til database…",
    "Save Import Template…": "Gem importskabelon…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Lyd (MP3)…",
    "Backups…": "Sikkerhedskopier…",
    "Show Source column": "Vis kolonnen «Kilde»",
    "Show Created At column": "Vis kolonnen «Oprettelsesdato»",
    "Max words…": "Maks. antal ord…",
    "View Log": "Vis log",
    "About": "Om programmet",
    "Quit": "Afslut",
    "Words": "Ord",
    "Texts": "Tekster",
    "Statistics": "Statistik",
    "Bin (deleted items)": "Papirkurv (slettede elementer)",
    "Settings": "Indstillinger",
    "Vocabulary": "Ordbog",
    "Search words, translations or tags…": "Søg efter ord, oversættelser eller tags…",
    "Search texts by title, content or words…": "Søg i tekster efter titel, indhold eller ord…",
    "Search scope": "Søgeområde",
    "Search scope…": "Søgeområde…",
    "Nothing to practice yet": "Der er endnu intet at øve",
    "Add words to your vocabulary and they show up here.":
        "Tilføj ord til dit ordforråd, så dukker de op her.",
    "Come back when cards are due, or practice the newest words now.":
        "Kom tilbage, når der er kort til gennemgang, eller øv de nyeste ord nu.",
    "Practice newest words": "Øv de nyeste ord",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Vælg et andet sæt ovenfor, eller justér dine filtre på Ord-siden.",
    "You're all caught up": "Du er helt ajour",
    "Add word": "Tilføj ord",
    "Copy a word in any app, then press:":
        "Kopiér et ord i en app, og tryk:",
    "Set a shortcut": "Vælg en genvej",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Kopiér et ord i en app, og tryk {keys} for at tilføje det med oversættelsen.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Vælg en genvej i Indstillinger for at tilføje kopierede ord fra alle apps.",
    " Favorites": " Favoritter",
    " Filters": " Filtre",
    "Filters that don't fit the table": "Filtre der ikke passer i tabellen",
    "More actions": "Flere handlinger",
    "Filter by tag": "Filtrer efter tag",
    "Close file and return to your vocabulary": "Luk fil og vend tilbage til din ordbog",
    "Definition": "Definition",
    "Read": "Læs",
    "Favorite": "Favorit",
    "Tags": "Tags",
    "Copy": "Kopier",
    "Text": "Tekst",
    "Delete selected (Del)": "Slet markerede (Slet)",
    "No data": "Ingen data",
    "No texts yet": "Ingen tekster endnu",
    "Words: {shown}/{total}": "Ord: {shown}/{total}",
    "Texts: {total}": "Tekster: {total}",
    "Texts: {shown}/{total}": "Tekster: {shown}/{total}",
    "{count} selected": "{count} valgt",
    "No selection": "Intet valgt",
    "Please select at least one word.": "Vælg venligst mindst ét ord.",
    "Saved": "Gemt",
    "'{word}' updated.": "«{word}» opdateret.",
    "Database Error": "Databasefejl",
    "Delete {count} word(s)?": "Slet {count} ord?",
    "Deleted": "Slettet",
    "{count} word(s) deleted.": "{count} ord slettet.",
    "Deleted with {n} error(s).": "Slettet med {n} fejl.",
    "Favorites": "Favoritter",
    "{count} word(s) added to favorites.": "{count} ord tilføjet til favoritter.",
    "{count} word(s) removed from favorites.": "{count} ord fjernet fra favoritter.",
    "Status set to '{status}' for {count} word(s).": "Status sat til «{status}» for {count} ord.",
    "Max Words": "Maks. antal ord",
    "Show only the first N words (0 = show all):": "Vis kun de første N ord (0 = vis alle):",
    "View Definition": "Vis definition",
    "Copy Word": "Kopier ord",
    "Copy Translation": "Kopier oversættelse",
    "Toggle Favorite": "Skift favoritstatus",
    "Change Status…": "Skift status…",
    "Add / Remove Tags…": "Tilføj / fjern tags…",
    "Read Aloud": "Læs op",
    "Change Status": "Skift status",
    "New status:": "Ny status:",
    "Copied": "Kopieret",
    "{count} row(s) copied to clipboard.": "{count} række(r) kopieret til udklipsholder.",
    "{count} item(s) copied to clipboard.": "{count} element(er) kopieret til udklipsholder.",
    "Copy Word(s)": "Kopier ord",
    "Copy Translation(s)": "Kopier oversættelse(r)",
    "Copy Both": "Kopier begge",
    "Search in Word": "Søg i Ord",
    "Search in Translation": "Søg i Oversættelse",
    "Search in Tags": "Søg i Tags",
    "Promoted": "Opgraderet",
    "Google Cloud TTS unavailable": "Google Cloud TTS er utilgængelig",
    "Selection limit": "Grænse for markering",
    "Only the first 200 selected words will be read.": "Kun de første 200 markerede ord vil blive læst op.",
    "Only the first 50 words will be used.": "Kun de første 50 ord vil blive brugt.",
    "Select words to save as audio.": "Vælg ord, der skal gemmes som lyd.",
    "Nothing to export.": "Intet at eksportere.",
    "Export Error": "Eksportfejl",
    "Settings saved.": "Indstillinger gemt.",
    "Generated text saved.": "Genereret tekst gemt.",
    "Show": "Vis",
    "Add Word": "Tilføj ord",
    "Stop reading": "Stop oplæsning",
    "Read — Read selected words aloud": "Læs — Læs markerede ord op",
    "Translation": "Oversættelse",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Udseende",
    "Audio": "Lyd",
    "Learning": "Lærer",
    "Listening": "Lytter",
    "Backups": "Sikkerhedskopier",
    "Sync your library?": "Synkroniser dit bibliotek?",
    "This will reconcile your device with the cloud:": "Dette vil afstemme din enhed med skyen:",
    "Sync now": "Synkroniser nu",
    "Upload": "Upload",
    "Synced — ↑{up} ↓{down}": "Synkroniseret — ↑{up} ↓{down}",
    "Upload restored library?": "Upload genoprettet bibliotek?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Biblioteket er genoprettet. Du vil blive bedt om at uploade det næste gang, du opretter forbindelse til en synkroniseringsserver.",
    "Merging this restored backup with your cloud:": "Fletter denne genoprettede sikkerhedskopi med din sky:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Denne sikkerhedskopi indeholder {items}. Vil du uploade og flette den med din sky nu, eller lade skyen være uændret indtil videre?",
    "General": "Generelt",
    "Read-aloud": "Oplæsning",
    "Translation & AI": "Oversættelse og AI",
    "Data": "Data",
    "Behavior": "Adfærd",
    "Progress": "Fremskridt",
    "DeepL request failed — using free Google Translate instead.": "DeepL-anmodning mislykkedes — bruger gratis Google Oversæt i stedet.",
    "DeepL key isn't set — using free Google Translate instead.": "DeepL-nøgle er ikke angivet — bruger gratis Google Oversæt i stedet.",
    "System": "System",
    "Light": "Lys",
    "Dark": "Mørk",
    "Appearance mode": "Udseendetilstand",
    "Widget scaling": "Elementskalering",
    "Table size": "Tabelstørrelse",
    "Interface language": "Grænsefladesprog",
    "Restart the app to apply the language change.": "Genstart appen for at anvende ændringen af sprog.",
    "The interface language has changed. Restart now to apply it?": "Grænsefladesproget er ændret. Genstart nu for at anvende?",
    "TTS provider": "TTS-udbyder",
    "Google Cloud credentials": "Google Cloud-legitimationsoplysninger",
    "Voice type": "Stemmetype",
    "Voice name (optional)": "Stemmenavn (valgfrit)",
    "Read Aloud playback": "Indstillinger for oplæsning",
    "Pause between words (s)": "Pause mellem ord (sek)",
    "Repeats per word": "Gentagelser pr. ord",
    "Repeats per pair": "Gentagelser pr. par",
    "Promote status while listening": "Forbedr status under lytning",
    "Listens to reach {status}": "Antal lytninger for at nå «{status}»",
    "Excel import": "Excel-import",
    "Placeholder values": "Pladsholderværdier",
    "Skip placeholder rows": "Spring pladsholderrækker over",
    "Skip empty rows": "Spring tomme rækker over",
    "Normalize language pairs": "Normaliser sprogpar",
    "How to import": "Sådan importerer du",
    "Save import template…": "Gem importskabelon…",
    "Active provider": "Aktiv udbyder",
    "API key": "API-nøgle",
    "API URL": "API-URL",
    "Check usage": "Tjek forbrug",
    "Enable cloud sync": "Aktiver skysynkronisering",
    "Supabase URL (.env)": "Supabase-URL (.env)",
    "Supabase key (.env)": "Supabase-nøgle (.env)",
    "Bin cleanup grace (days)": "Dage før sletning i papirkurv",
    "Test Connection": "Test forbindelse",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "Skysynkronisering bruger dit eget Supabase-projekt. Opret de nødvendige tabeller én gang, og indtast derefter URL og anon-nøgle ovenfor.",
    "Copy schema SQL": "Kopier schema-SQL",
    "Open SQL editor ↗": "Åbn SQL-editor ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "Schema-SQL er kopieret til udklipsholderen. Åbn SQL-editoren i dit Supabase-projekt, indsæt koden, og tryk på Run for at oprette tabellerne.",
    "Server": "Server",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Forbundet til din egen Supabase-server — personlig tilstand, ingen konto nødvendig.\n{host}",
    "Use your own Supabase server (personal)": "Brug din egen Supabase-server (personlig)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Personlig, enkeltbruger-synkronisering til et Supabase-projekt, du ejer. Ingen konto eller login — appen opretter forbindelse med projektets anon-nøgle. Kør schema-SQL i dit projekt, indsæt URL og anon-nøgle nedenfor, og klik derefter på Test forbindelse.\n\nBemærk: Alle med denne URL og nøgle kan læse dataene, så hold projektet privat og del ikke nøglen.",
    "Disconnect — use the built-in server": "Afbryd — brug den indbyggede server",
    "Disconnect server": "Afbryd server",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Vil du stoppe synkronisering med din egen Supabase-server og bruge den indbyggede igen?\n\nDine ord forbliver i dit eget projekt og på denne enhed. Du vil kun køre lokalt, indtil du logger ind på en konto.",
    "Disconnected — using the built-in server.": "Afbrudt — bruger den indbyggede server.",
    "{host} (personal)": "{host} (personlig)",
    "Personal": "Personlig",
    "your server": "din server",
    "Account actions": "Konto-handlinger",
    "Add account…": "Tilføj konto…",
    "Sync this device's data to my account…": "Synkroniser data fra denne enhed til min konto…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Konto",
    "Accounts": "Konti",
    "No accounts yet. Add one to sync your words across devices.": "Ingen konti endnu. Tilføj en for at synkronisere dine ord på tværs af enheder.",
    "(active)": "(aktiv)",
    "Sign in": "Log ind",
    "(sign in again)": "(log ind igen)",
    "Switch": "Skift",
    "Remove account": "Fjern konto",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Fjern {email} fra denne enhed? Du kan tilføje den igen når som helst — dine ord forbliver i skyen, og den lokale kopi forbliver på disken. Dine skydata slettes ikke.",
    "Removed {email} from this device.": "Fjernede {email} fra denne enhed.",
    "Your data was exported.": "Dine data blev eksporteret.",
    "Export failed.": "Eksport mislykkedes.",
    "Delete account": "Slet konto",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Dette sletter permanent din konto og ALLE dine synkroniserede ord, tekster og tags fra skyen. Din lokale kopi arkiveres i mappen for sikkerhedskopier. Dette kan ikke fortrydes.\n\nVil du slette din konto?",
    "Account deleted.": "Konto slettet.",
    "Could not delete the account.": "Kunne ikke slette kontoen.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Navn",
    "Enter your name.": "Indtast dit navn.",
    "Email": "E-mail",
    "Password": "Adgangskode",
    "New password": "Ny adgangskode",
    "6-digit code": "6-cifret kode",
    "or": "eller",
    "Sign in with Google": "Log ind med Google",
    "Opening your browser to sign in with Google…": "Åbner din browser for at logge ind med Google…",
    "Forgot password?": "Glemt adgangskode?",
    "Resend code": "Send kode igen",
    "Confirm your email": "Bekræft din e-mail",
    "Verify code": "Bekræft kode",
    "Use a different email": "Brug en anden e-mail",
    "Enter your email and password.": "Indtast din e-mail og adgangskode.",
    "Enter the 6-digit code from the email.": "Indtast den 6-cifrede kode fra e-mailen.",
    "Enter the code and a new password.": "Indtast koden og en ny adgangskode.",
    "Enter your email above first.": "Indtast din e-mail ovenfor først.",
    "Enter the reset code we emailed you and a new password.": "Indtast nulstillingskoden, vi sendte til dig, og en ny adgangskode.",
    "Enter the 6-digit code we emailed you.": "Indtast den 6-cifrede kode, vi sendte på e-mail.",
    "Reset password": "Nulstil adgangskode",
    "Set new password": "Angiv ny adgangskode",
    "Back to sign in": "Tilbage til login",
    "Sign-in failed.": "Login mislykkedes.",
    "Couldn't send the code.": "Kunne ikke sende koden.",
    "Done.": "Færdig.",
    "Failed.": "Mislykkedes.",
    "Create an account": "Opret en konto",
    "Create account": "Opret konto",
    "I already have an account": "Jeg har allerede en konto",
    "Signed in as {email}": "Logget ind som {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Synkroniser data fra denne enhed til din konto",
    "your account": "din konto",
    "This device has {words} and {texts} not yet in {account}.": "Denne enhed har {words} og {texts}, som endnu ikke er i {account}.",
    "This device has {words} not yet in {account}.": "Denne enhed har {words}, som endnu ikke er i {account}.",
    "This device has {texts} not yet in {account}.": "Denne enhed har {texts}, som endnu ikke er i {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Vælg de elementer, der skal tilføjes. De kopieres til din konto og uploades til skyen, så de vises på dine andre enheder. Kopien på denne enhed bevares.",
    "Don't ask again for this account": "Spørg ikke igen for denne konto",
    "{n} word": "{n} ord",
    "{n} words": "{n} ord",
    "{n} text": "{n} tekst",
    "{n} texts": "{n} tekster",
    "Add {n} item": "Tilføj {n} element",
    "Add {n} items": "Tilføj {n} elementer",
    # Genitive/plural placeholder compatibility
    "words (genitive)": "ord",
    "texts (genitive)": "tekster",
    "tags (genitive)": "tags",
    "changes (genitive)": "ændringer",
    "deletions (genitive)": "sletninger",
    "{n} words (genitive)": "{n} ord",
    "{n} texts (genitive)": "{n} tekster",
    "Add {n} items (genitive)": "Tilføj {n} elementer",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "Tilføjede {n} element til din konto.",
    "Added {n} items to your account.": "Tilføjede {n} elementer til din konto.",
    "Added {n} items to your account. (genitive)": "Tilføjede {n} elementer til din konto.",
    "{n} couldn't be added.": "{n} kunne ikke tilføjes.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Din session er udløbet — log ind igen (Indstillinger → Synkronisering)",
    "Sign in to sync (Settings → Sync)": "Log ind for at synkronisere (Indstillinger → Synkronisering)",
    "Sign in again to sync": "Log ind igen for at synkronisere",
    "Sign in again to use this account.": "Log ind igen for at bruge denne konto.",
    "Sync incomplete: {reason}": "Synkronisering ufuldstændig: {reason}",
    "Connect to the internet to add local items to your account.": "Opret forbindelse til internettet for at tilføje lokale elementer til din konto.",
    "Everything on this device is already in your account.": "Alt på denne enhed er allerede på din konto.",
    "Upload local words?": "Upload lokale ord?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Vil du uploade dine nuværende lokale ord til denne konto? De flettes sammen med kontens skydata og synkroniseres.\n\nVælg Nej for at beholde denne kontos eksisterende data og lægge dine lokale ord til side (arkiveres i sikkerhedskopimappen).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Login mislykkedes. Tjek din e-mail og adgangskode.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Du kan have op til {max} konti på denne enhed. Fjern en for at tilføje en anden.",
    "Wrong email or password.": "Forkert e-mail eller adgangskode.",
    "That doesn't look like a valid email address.": "Det ligner ikke en gyldig e-mailadresse.",
    "Confirm password": "Bekræft adgangskode",
    "Passwords don't match.": "Adgangskoderne matcher ikke.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Din e-mail er ikke bekræftet endnu. Indtast den 6-cifrede kode, vi sendte på e-mail.",
    "That email is already registered. Try signing in instead.": "Denne e-mail er allerede registreret. Prøv at logge ind i stedet.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Vi har sendt dig en 6-cifret kode på e-mail. Indtast den for at fuldføre tilmeldingen.",
    "That code didn't work. Check it and try again.": "Koden virkede ikke. Tjek den, og prøv igen.",
    "If that account exists, a 6-digit reset code is on its way.": "Hvis kontoen eksisterer, er en 6-cifret nulstillingskode på vej.",
    "Confirmation email re-sent.": "Bekræftelses-e-mail sendt igen.",
    "Too many attempts. Please wait a minute and try again.": "For mange forsøg. Vent venligst et minut og prøv igen.",
    "Your password is too short — use at least 6 characters.": "Din adgangskode er for kort — brug mindst 6 tegn.",
    "Sign-ups are disabled on this server.": "Oprettelse af nye konti er deaktiveret på denne server.",
    "Can't reach the server. Check your internet connection.": "Kan ikke nå serveren. Tjek din internetforbindelse.",
    "Something went wrong.": "Noget gik galt.",
    "Your saved sign-in for this account expired. Sign in again.": "Dit gemte login for denne konto er udløbet. Log ind igen.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "Skysynkronisering er ikke konfigureret endnu. Tilføj Supabase URL og nøgle under Indstillinger → Synkronisering først.",
    "Could not start Google sign-in.": "Kunne ikke starte Google-login.",
    "Google sign-in was cancelled or timed out.": "Google-login blev annulleret eller fik timeout.",
    "Google sign-in failed.": "Google-login mislykkedes.",
    "Google sign-in failed: {error}": "Google-login mislykkedes: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Kunne ikke starte den lokale login-hjælper på port {port} ({error}). Luk det program, der bruger den, og prøv igen.",
    "Export my data…": "Eksporter mine data…",
    "Delete account…": "Slet konto…",
    "Cloud sync is on — your own server ({host})": "Skysynkronisering er slået til — din egen server ({host})",
    "Cloud sync is on — signed in as {who}": "Skysynkronisering er slået til — logget ind som {who}",
    "Cloud sync is off — your words are saved on this device only": "Skysynkronisering er slået fra — dine ord gemmes kun på denne enhed",
    "(checking…)": "(kontrollerer…)",
    "(can't connect)": "(kan ikke forbinde)",
    "Turn off cloud sync": "Slå skysynkronisering fra",
    "Cloud sync turned off — this device only.": "Skysynkronisering slået fra — kun denne enhed.",
    "Use this server": "Brug denne server",
    "Connecting…": "Forbinder…",
    "Testing…": "Tester…",
    "Applying theme…": "Anvender tema…",
    "Now syncing with your own server.": "Synkroniserer nu med din egen server.",
    "Could not connect to this server:\n{error}": "Kunne ikke forbinde til denne server:\n{error}",
    "Could not connect to this server.": "Kunne ikke forbinde til denne server.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nTjek URL'en og anon-nøglen, samt om du har kørt schema-SQL der. Vil du bruge disse oplysninger alligevel?",
    "Enter your server's URL and anon key first, then test.": "Indtast din servers URL og anon-nøgle først, og test derefter.",
    "Enter your server's URL and anon key first.": "Indtast din servers URL og anon-nøgle først.",
    "Supabase URL": "Supabase-URL",
    "Supabase key (anon)": "Supabase-nøgle (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Personlig, enkeltbruger-synkronisering til et Supabase-projekt, du ejer. Ingen konto eller login — appen opretter forbindelse med projektets anon-nøgle. Kør schema-SQL i dit projekt, indsæt URL og anon-nøgle nedenfor, test den, og tryk derefter på “Brug denne server”.\n\nBemærk: Alle med denne URL og nøgle kan læse dataene, så hold projektet privat og del ikke nøglen.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Vil du stoppe synkroniseringen med din egen Supabase-server og bruge den indbyggede igen?\n\nDine ord forbliver i dit eget projekt og på denne enhed. Serveroplysningerne gemmes, så du altid kan skifte tilbage. Du vil køre lokalt, indtil du logger ind på en konto.",
    "Start automatically on login (minimized to tray)": "Start automatisk ved login (minimeret til proceslinjen)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "Start ved logon er slået fra for Lingueez i Windows-indstillinger, så det kan ikke slås til her.",
    "Open Windows startup settings": "Åbn Windows' startindstillinger",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows anvendte ikke denne ændring. Du kan selv slå Lingueez til eller fra under Indstillinger > Apps > Start.",
    "Add Word hotkey (global)": "Genvejstast til «Tilføj ord» (global)",
    "Data format": "Dataformat",
    "Columns to export": "Kolonner, der skal eksporteres",
    "Sheet name": "Arknavn",
    "Start row": "Startrække",
    "Start column": "Startkolonne",
    "Shade alternate rows": "Nuancer hver anden række",
    "Auto column width": "Automatisk kolonnebredde",
    "Freeze header row": "Lås overskriftsrække",
    "Delimiter": "Afgrænsning",
    "Delimiter (\\t = tab)": "Afgrænsning (\\t = tabulator)",
    "Include header lines": "Inkluder overskriftslinjer",
    "Header lines": "Overskriftslinjer",
    "Page size": "Sidestørrelse",
    "Font size": "Skriftstørrelse",
    "Line spacing (pt)": "Linjeafstand (pt)",
    "Text alignment": "Tekstjustering",
    "Margins L/R/T/B (pt)": "Marginer V/H/T/B (pt)",
    "Automatic widths (fit page)": "Automatiske bredder (tilpas til side)",
    "Columns / width": "Kolonner / bredde",
    "Header background": "Overskrift baggrund",
    "Header text": "Overskrift tekst",
    "Row background": "Række baggrund",
    "Grid lines": "Gitterlinjer",
    "Background image": "Baggrundsbillede",
    "Concurrent workers": "Samtidige processer",
    "Requests per second": "Anmodninger pr. sekund",
    "Add font…": "Tilføj skrifttype…",
    "Page && text": "Side && tekst",
    "Columns": "Kolonner",
    "Max tokens": "Maks. tokens",
    "Temperature": "Temperatur",
    "Prompt template": "Prompt-skabelon",
    "Definitions": "Definitioner",
    "Generated Texts (from words)": "Genererede tekster (ud fra ord)",
    "Generated Texts (by topic)": "Genererede tekster (efter emne)",
    "Text Adaptation (to level)": "Teksttilpasning (til niveau)",
    "Thinking budget (0 = off, -1 = auto)": "Tænkebudget (0 = fra, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Registrer sprog",
    "Type a word or phrase…": "Skriv et ord eller en sætning…",
    "Translation…": "Oversættelse…",
    "Pronounce": "Udtal",
    "Swap word and translation": "Byt om på ord og oversættelse",
    "Translate with DeepL (Enter)": "Oversæt med DeepL (Enter)",
    "Save Word": "Gem ord",
    "Enter a word to translate.": "Indtast et ord for at oversætte.",
    "Fill with AI (lemma + best translation)": "Udfyld med AI (lemma + bedste oversættelse)",
    "Enter a word to fill with AI.": "Indtast et ord for at udfylde med AI.",
    "Source equals target — translated to {lang} instead.": "Kildesprog er det samme som målsprog — oversat til {lang} i stedet.",
    "Both word and translation are required.": "Både ord og oversættelse er påkrævet.",
    "Please select the source language before saving.": "Vælg kildesproget, før du gemmer.",
    "'{word}' already exists in your dictionary.": "«{word}» findes allerede i din ordbog.",
    "'{word}' is already in your dictionary.": "«{word}» findes allerede i din ordbog.",
    "Already in your dictionary": "Allerede i din ordbog",
    "Show existing": "Vis eksisterende",
    "The text was truncated to the first 100 words.": "Teksten blev afskåret til de første 100 ord.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Generer med AI",
    "Regenerate with AI": "Generer igen med AI",
    "Definition 2": "Definition 2",
    "No definition yet": "Ingen definition endnu",
    "Generate one with AI, or write your own with Edit.": "Generer en med AI, eller skriv din egen via Rediger.",
    "There is no word to define.": "Der er intet ord at definere.",
    "Bold": "Fed",
    "Italic": "Kursiv",
    "Heading": "Overskrift",
    "List": "Liste",
    "API key missing": "API-nøgle mangler",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Angiv din {ai} API-nøgle i Indstillinger → Oversættelse og AI → AI først.",
    "Generating definition…": "Genererer definition…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Tags — {count} ord",
    "New tag name…": "Nyt tag-navn…",
    "Add Tag": "Tilføj tag",
    "Apply Selected to All": "Anvend valgte på alle",
    "Remove Selected": "Fjern valgte",
    "(partial)": "(delvis)",
    "use(s)": "anvendelse(r)",
    "Tags marked ✓ apply to all selected words.": (
        "Tags markeret med ✓ gælder for alle markerede ord."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (delvis) betyder, at kun nogle af ordene har tagget."
    ),
    "Select tag(s) in the list first.": "Vælg tag(s) på listen først.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Papirkurv — Slettede elementer",
    "Delete Permanently": "Slet permanent",
    "Cleanup Old Items…": "Ryd op i gamle elementer…",
    "{n} selected": "{n} valgt",
    "The bin is empty. Deleted words will appear here.":
        "Papirkurven er tom. Slettede ord vil blive vist her.",
    "The bin is empty. Deleted texts will appear here.":
        "Papirkurven er tom. Slettede tekster vil blive vist her.",
    "deleted {when}": "slettet {when}",
    "(empty)": "(tom)",
    "Untitled": "Uden titel",
    "Auto-deletes soon": "Slettes automatisk snart",
    "Auto-deletes in {n} day": "Slettes automatisk om {n} dag",
    "Auto-deletes in {n} days": "Slettes automatisk om {n} dage",
    "Auto-deletes in {n} days (genitive)": "Slettes automatisk om {n} dage",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Vil du slette {count} element(er) permanent? Dette kan ikke fortrydes.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Gendan en tidligere version",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Din database sikkerhedskopieres automatisk efter enhver ændring. "
        "Vælg en tidligere version nedenfor for at gendanne den."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Ingen gemte versioner endnu. "
        "En sikkerhedskopi oprettes automatisk efter enhver ændring."
    ),
    "Restore this version": "Gendan denne version",
    "Today": "I dag",
    "Yesterday": "I går",
    "Most recent": "Seneste",
    "Before your last restore": "Før din sidste gendannelse",
    "today": "i dag",
    "yesterday": "i går",
    "today {time}": "i dag {time}",
    "yesterday {time}": "i går {time}",
    "the version from {date}": "versionen fra {date}",
    "the version from just before your last restore": "versionen fra lige før din sidste gendannelse",
    "Restore Version": "Gendan version",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Vil du gendanne {phrase}?\n\nDine nuværende data gemmes først, så du kan fortryde dette."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Din database er blevet gendannet til {phrase}.\n\n"
        "Har du ombestemt dig? Gendan \"{before}\" for at fortryde."
    ),
    "Restore Error": "Gendannelsesfejl",
    "Sorry, that version could not be restored:\n{error}": "Beklager, den version kunne ikke gendannes:\n{error}",
    "Remove Version": "Fjern version",
    "Remove {phrase}?": "Slet {phrase}?",
    "Remove Error": "Fejl ved fjernelse",
    "Sorry, that version could not be removed:\n{error}": "Beklager, den version kunne ikke fjernes:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Generer tekst",
    "Title…": "Titel…",
    "Generated text appears here…": "Genereret tekst vises her…",
    "Save to Texts": "Gem under tekster",
    "Save failed": "Gem mislykkedes",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Gem som lyd",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Generer én MP3-fil ud fra {count} ord/oversættelsespar."
    ),
    "Generating audio…": "Genererer lyd…",
    "Compiling final audio file…": "Kompilerer den endelige lydfil…",
    "Processed: {word}": "Behandlet: {word}",
    "Choose File && Start": "Vælg fil && start",
    "Cancelled.": "Annulleret.",
    "Audio saved": "Lyd gemt",
    "Audio file saved to:\n{path}": "Lydfil gemt i:\n{path}",
    "Audio Error": "Lydfejl",
    "Failed to save audio:\n{error}": "Kunne ikke gemme lyd:\n{error}",
    "Cancelling…": "Annullerer…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Importer fra Excel",
    "Row": "Række",
    "Word 1": "Ord 1",
    "Language 1": "Sprog 1",
    "Word 2": "Ord 2",
    "Language 2": "Sprog 2",
    "Action": "Handling",
    "Details": "Detaljer",
    "Add": "Tilføj",
    "Update": "Opdater",
    "Skip": "Spring over",
    "All": "Alle",
    "To add": "Der skal tilføjes",
    "To update": "Der skal opdateres",
    "Skipped": "Paspringede",
    "Unrecognized": "Ikke genkendt",
    "Only recognized languages": "Kun genkendte sprog",
    "Exclude rows whose language wasn't recognized.":
        "Ekskluder rækker med uigenkendte sprog.",
    "Unrecognized language — will be imported exactly as written.":
        "Uigenkendt sprog — vil blive importeret nøjagtigt som skrevet.",
    "Select all": "Vælg alle",
    "Activity log": "Aktivitetslog",
    "Export log…": "Eksporter log…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Eksporter…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Tilføj tekst",
    "Write": "Skriv",
    "AI Generate": "AI-generering",
    "Wikipedia": "Wikipedia",
    "From URL": "Fra URL",
    "Language:": "Sprog:",
    "Level:": "Niveau:",
    "Topic:": "Emne:",
    "Topic…": "Emne…",
    "Adapt to my level": "Tilpas til mit niveau",
    "Load entries": "Indlæs indlæg",
    "Add feed…": "Tilføj feed…",
    "Ideas:": "Idéer:",
    "Short (~100 words)": "Kort (~100 ord)",
    "Medium (~250 words)": "Mellem (~250 ord)",
    "Long (~500 words)": "Lang (~500 ord)",
    "Travel": "Rejser",
    "Food": "Mad",
    "Daily routine": "Hverdag",
    "A short story": "En kort historie",
    "News": "Nyheder",
    "Dialogue at a café": "Dialog på en café",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Skriv eller indsæt din tekst her, eller hent en med fanerne ovenfor…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Nyeste først",
    "Oldest first": "Ældste først",
    "Title A–Z": "Titel A–Å",
    "All languages": "Alle sprog",
    "All levels": "Alle niveauer",
    "All topics": "Alle emner",
    "No matching texts": "Ingen matchende tekster",
    "Try a different search or language filter.": "Prøv en anden søgning eller sprogfilter.",
    "New text (write or paste)": "Ny tekst (skriv eller indsæt)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Hent tekst fra internettet (AI / Wikipedia / URL / RSS)"
    ),
    "Import .txt file(s)": "Importer .txt-fil(er)",
    "Read aloud": "Læs op",
    "Translate text": "Oversæt tekst",
    "Hide translation": "Skjul oversættelse",
    "Focus mode": "Fokustilstand",
    "Exit focus mode": "Afslut fokustilstand",
    "Paper mode: off": "Papirtilstand: fra",
    "Paper: white (click for sepia)": "Papir: hvidt (klik for sepia)",
    "Paper: sepia (click to turn off)": "Papir: sepia (klik for at slå fra)",
    "Save Changes": "Gem ændringer",
    "Previous text": "Forrige tekst",
    "Next text": "Næste tekst",
    "From words: {words}": "Fra ord: {words}",
    "Created {date}": "Oprettet {date}",
    "Unsaved changes": "Ugemte ændringer",
    "Save changes to '{title}'?": "Gem ændringer i «{title}»?",
    "Changes saved.": "Ændringer gemt.",
    "'{title}' moved to bin.": "«{title}» flyttet til papirkurven.",
    "Reader": "Læser",
    'Pronounce "{word}"': 'Udtal «{word}»',
    'Add "{word}" to vocabulary': 'Tilføj «{word}» til ordbog',
    "Read from here": "Læs herfra",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Kilde",
    "Added manually": "Tilføjet manuelt",
    "From reader": "Fra læseren",
    "Created at": "Oprettelsesdato",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Tilføj med AI (lemma + bedste oversættelse)",
    "Add to vocabulary as is": "Tilføj til ordbog som den er",
    "Thinking…": "Tænker…",
    "'{pair}' is already in your dictionary.": "«{pair}» er allerede i din ordbog.",
    "{label} — {translation} · added": "{label} — {translation} · tilføjet",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Skysynkronisering",
    "Last sync": "Sidste synkronisering",
    "Pending": "Afventer",
    "never": "aldrig",
    "just now": "lige nu",
    "{n} min ago": "for {n} min siden",
    "Connected": "Forbundet",
    "Not connected": "Ikke forbundet",
    "change": "ændring",
    "changes": "ændringer",
    "deletion": "sletning",
    "deletions": "sletninger",
    "everything synced": "alt er synkroniseret",
    "Initial sync has not completed yet.": "Første synkronisering er endnu ikke fuldført.",
    "Sync Now": "Synkroniser nu",
    "Syncing…": "Synkroniserer…",
    # Local-only promo state
    "{words} and {texts}": "{words} og {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Du har gemt {items} her. Log ind for at beskytte dem og læse på alle dine enheder.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Kun lokalt — log ind for at synkronisere dine ord på tværs af enheder",
    "Sign in to sync across devices": "Log ind for at synkronisere",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Velkommen",
    "Welcome to {app}": "Velkommen til {app}",
    "Sync across your devices": "Synkroniser på tværs af enheder",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Log ind for at opbevare din ordbog sikkert og studere den på enhver enhed.",
    "Automatic cloud backup": "Automatisk sikkerhedskopiering i skyen",
    "Your words follow you to every computer.":
        "Dine ord følger dig til enhver computer.",
    "Never lose your progress.": "Mist aldrig dine fremskridt.",
    "Study anywhere": "Lær hvor som helst",
    "Pick up right where you left off.":
        "Fortsæt præcis, hvor du slap.",
    "Your data is yours — sign in only to sync it.":
        "Dine data er dine — log kun ind for at synkronisere.",
    "Sign in / Create account": "Log ind / Opret konto",
    "Continue on this device": "Fortsæt på denne enhed",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Afspilningsindstillinger",
    "Previous word": "Forrige ord",
    "Next word": "Næste ord",
    "Stop playback": "Stop afspilning",
    "Pause between words": "Pause mellem ord",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Intet at læse.",
    "Previous sentence": "Forrige sætning",
    "Next sentence": "Næste sætning",
    "Reading speed": "Læsehastighed",
    "Sentence {n} / {total}": "Sætning {n} / {total}",
    "buffering…": "buffer…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Oversigt",
    "Learning status": "Læringsstatus",
    "Activity": "Aktivitet",
    "Review activity": "Repetitionssaktivitet",
    "Breakdown": "Opdeling",
    "Total words": "Ord i alt",
    "Mastered": "Mestret",
    "In progress": "I gang",
    "Languages": "Sprog",
    "Current streak": "Nuværende stime",
    "Added this week": "Tilføjet i denne uge",
    "Definitions written": "Skrevne definitioner",
    "Status distribution": "Statusfordeling",
    "Words added over time": "Ord tilføjet over tid",
    "Activity calendar": "Aktivitetskalender",
    "Reviews over time": "Repetitioner over tid",
    "Review calendar": "Repetitionskalender",
    "Most reviewed words": "Mest repeterede ord",
    "Top language pairs": "Top sprogpar",
    "Top tags": "Mest brugte tags",
    "Reviewed this week": "Repeteret i denne uge",
    "Total reviews": "Repetitioner i alt",
    "Review streak": "Repetitionsstime",
    "{pct}% of all words": "{pct}% af alle ord",
    "actively learning": "aktivt i gang med at lære",
    "{n} pairs": "{n} par",
    "best {n}d": "rekord {n} d.",
    "{n} today": "{n} i dag",
    "listens logged": "lytninger registreret",
    "keep it going": "bliv ved!",
    "Day": "Dag",
    "Week": "Uge",
    "Month": "Måned",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Importer tekstfiler",
    "Text files (*.txt);;All files (*)": "Tekstfiler (*.txt);;Alle filer (*)",
    "Language of the imported text(s):": "Sprog for importeret tekst(er):",
    "Imported {count} text(s).": "Importeret {count} tekst(er).",
    "Some files could not be imported:": "Nogle filer kunne ikke importeres:",
    "Import failed:\n{error}": "Import mislykkedes:\n{error}",
    "Failed to save text:\n{error}": "Kunne ikke gemme tekst:\n{error}",
    "Failed to delete text:\n{error}": "Kunne ikke slette tekst:\n{error}",
    "Delete Text": "Slet tekst",
    "Delete '{title}'?": "Slet «{title}»?",
    "Unsupported language: {language}": "Ikke-understøttet sprog: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Ikke-understøttet sprog: {lang}. Vælg et fra listen.",
    "(empty)": "(tom)",
    "unsupported language": "ikke-understøttet sprog",
    "unreadable text": "ulæselig tekst",
    "Skipped {n} {noun} ({reasons}).": "Sprang {n} {noun} over ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Noget tekst kunne ikke læses op — ikke-understøttet sprog "
        "eller ulæselige tegn.",
    "Edit text": "Rediger tekst",
    "Done editing": "Færdig med at redigere",
    "Delete text": "Slet tekst",
    "Save Changes": "Gem ændringer",
    "Paper mode": "Papirtilstand",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Klik på «+» for at skrive eller indsætte en tekst, «globussen» for at hente en\n"
        "fra internettet, eller vælg ord i visningen «Ord»\n"
        "og brug handlingen «Tekst» til at generere en studietekst."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Søger på Wikipedia på det valgte sprog. Klik på et resultat for at indlæse artiklen; brug «Tilpas til mit niveau» for at forenkle den."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Nyhedsfeeds for det valgte sprog. Indlæs et feed, og dobbeltklik derefter på et indlæg for at hente den fulde tekst. Tilføj dine egne feeds med «Tilføj feed…»."
    ),
    "Length:": "Længde:",
    "Search Wikipedia (in the selected language)…": "Søg på Wikipedia (på det valgte sprog)…",
    "Double-click an entry to load its full text.": "Dobbeltklik på et indlæg for at indlæse den fulde tekst.",
    "Working…": "Arbejder…",
    "Show the {count} result(s) again": "Vis de {count} resultat(er) igen",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "{ai} API-nøgle er ikke angivet. Konfigurer den i Indstillinger → Oversættelse og AI → AI."
    ),
    "Generating with {ai}…": "Genererer med {ai}…",
    'Fetching "{title}"…': 'Henter «{title}»…',
    "(yours)": "(din)",
    "Fetching the full text…": "Henter den fulde tekst…",
    "Add feed": "Tilføj feed",
    "Feed name:": "Feed-navn:",
    "Feed URL:": "Feed-URL:",
    "Failed to save the text.": "Kunne ikke gemme teksten.",
    "Failed to save the text: {error}": "Kunne ikke gemme teksten: {error}",
    "'{title}' saved.": "«{title}» gemt.",
    "(untitled)": "(uden titel)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Omskriv teksten nedenfor til det valgte CEFR-niveau med {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Eksporter log",
    "Activity Log": "Aktivitetslog",
    "Warnings & errors": "Advarsler og fejl",
    "Errors only": "Kun fejl",
    "Find…": "Find…",
    "Open log folder": "Åbn logmappe",
    "Export diagnostics": "Eksporter diagnostik",
    "Clear the log file? This cannot be undone.":
        "Vil du rydde logfilen? Dette kan ikke fortrydes.",
    "Could not create the diagnostics file.":
        "Kunne ikke oprette diagnostikfilen.",
    "Diagnostics saved to:\n{path}": "Diagnostik gemt i:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Beskriv problemet**\n\n\n**Trin til at genskabe**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nVedhæft venligst diagnostikfilen:\n{path}\n",
    "Bug report: ": "Fejlrapport: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Minimer",
    "Maximize": "Maksimer",
    "Restore": "Gendan",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Vis styring",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Ingen farve",
    "None": "Ingen",
    "Choose Color": "Vælg farve",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Skysynkronisering: inaktiv",
    "Failed to open table:\n{error}": "Kunne ikke åbne tabel:\n{error}",
    "Failed to save template:\n{error}": "Kunne ikke gemme skabelon:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Vis / skjul",
    "Excel options": "Excel-indstillinger",
    "CSV options": "CSV-indstillinger",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Overskriftslinjer skrives øverst i filen — importværktøjer som "
        "Anki læser dem (f.eks. #separator:tab, #html:true). "
        "Selve kolonnenavnene skrives ikke."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Kopier en .ttf-fil til appens skrifttypemappe og brug den"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Bruges kun ved eksport af ord til en MP3-fil. "
        "Selve stemmen konfigureres i fanen Lyd."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "Stemmen bruges overalt, hvor ord læses op: i appens Oplæsning "
        "og MP3-eksport. gTTS er gratis og kræver ingen opsætning. Google Cloud TTS "
        "kræver en JSON-nøgle fra en servicekonto (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) samt aktiveret fakturering i projektet — "
        "forbrug inden for den gratis månedlige kvote er omkostningsfrit."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "At lytte helt til et ord i Oplæsning forfremmer det langs "
        "kendthedsstigen Ny → Repeteres → Lærer → Mestret. Hvert "
        "tal er det samlede antal fuldførte lytninger, der kræves for at nå niveauet. Ord "
        "du selv sætter til Mestret eller Ignoreret ændres aldrig, og et "
        "ord nedgraderes aldrig."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Gem en færdig .xlsx med de rigtige overskrifter og eksempelrækker"
    ),
    "Google Translate (free)": "Google Oversæt (gratis)",
    "Google Translate is free and needs no API key.": (
        "Google Oversæt er gratis og kræver ingen API-nøgle."
    ),
    "Usage": "Forbrug",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Klik i feltet og tryk på den ønskede tastekombination — det åbner "
        "«Tilføj ord» med udklipsholderens indhold uanset hvor du er. "
        "Lad være tom for at deaktivere."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "På Wayland registreres denne genvej hos dit "
        "skrivebord og vises i systemets tastaturindstillinger."
    ),
    "Add Word hotkey": "Genvejstast til «Tilføj ord»",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Den globale genvejstast «Tilføj ord» er ikke tilgængelig i dette "
        "miljø. Se Indstillinger ▸ System for valgmuligheder."
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "Den globale genvejstast «Tilføj ord» er ikke tilgængelig i "
        "{sandbox}-sandkassen på Wayland."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Den globale genvejstast «Tilføj ord» understøttes endnu ikke "
        "på dette Wayland-skrivebord."
    ),
    "To enable it, use any one of these:": "For at aktivere den, brug en af følgende metoder:",
    "Log in to an X11 session instead of Wayland":
        "log ind i en X11-session i stedet for Wayland",
    "Use a GNOME session — the global hotkey works there":
        "brug en GNOME-session — der virker den globale genvejstast",
    "Install the AppImage version — it runs outside the sandbox":
        "installer AppImage-versionen — den kører uden for sandkassen",
    "Download the AppImage": "Download AppImage",
    "Add font…": "Tilføj skrifttype…",
    "TrueType fonts (*.ttf)": "TrueType-skrifttyper (*.ttf)",
    "Could not copy the font file:\n{error}": "Kunne ikke kopiere skrifttypefilen:\n{error}",
    "Save import template…": "Gem importskabelon…",
    "Excel files (*.xlsx)": "Excel-filer (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Skabelon gemt i:\n{path}\n\n"
        "Udfyld den med dine ord (erstat eksempelrækkerne) "
        "og importer den via appmenuen → Importer Excel til database."
    ),
    "Could not save the template:\n{error}": "Kunne ikke gemme skabelonen:\n{error}",
    "Background image": "Baggrundsbillede",
    "Images (*.png *.jpg *.jpeg)": "Billeder (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON-filer (*.json)",
    "Connection successful! ✅": "Forbindelse lykkedes! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Kunne ikke forbinde. Tjek URL/nøgle og din internetforbindelse."
    ),
    "Connection test failed:\n{error}": "Forbindelsestest mislykkedes:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} tegn i denne periode",
    "{count} characters used": "{count} tegn brugt",
    "Autostart": "Autostart",
    "Could not update autostart entry:\n{error}": "Kunne ikke opdatere autostart-post:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS er valgt, men {problem}\n\n"
        "Lyd vil falde tilbage til gTTS, indtil dette er rettet."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "ord",
    "words": "ord",
    "words (genitive)": "ord",
    "text": "tekst",
    "texts": "tekster",
    "texts (genitive)": "tekster",
    "tag": "tag",
    "tags": "tags",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Oversæt",
    "AI": "AI",
    "Save As": "Gem som",
    "Save Audio As": "Gem lyd som",
    "Save PDF As": "Gem PDF som",
    "Added": "Tilføjet",
    "Updated": "Opdateret",
    "Failed": "Mislykkedes",
    "Checking…": "Kontrollerer…",
    "Cleanup": "Oprydning",
    "Permanent Delete": "Permanent sletning",
    "No word": "Intet ord",
    "Category": "Kategori",
    "Bin": "Papirkurv",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Alle tags",
    "Filter by tag — {tag}": "Filtrer efter tag — {tag}",
    "(showing first {n})": "(viser de første {n})",
    "Texts: {total}": "Tekster: {total}",
    "Deleted with {n} error(s).": "Slettet med {n} fejl.",
    "Failed to update: {error}": "Kunne ikke opdatere: {error}",
    "Failed to export:\n{error}": "Kunne ikke eksportere:\n{error}",
    "Failed to export PDF:\n{error}": "Kunne ikke eksportere PDF:\n{error}",
    "Failed to export TXT:\n{error}": "Kunne ikke eksportere TXT:\n{error}",
    "PDF saved to {path}": "PDF gemt i {path}",
    "TXT file saved to {path}": "TXT-fil gemt i {path}",
    "Template saved to {path}": "Skabelon gemt i {path}",
    "{format} file saved to {path}": "{format}-fil gemt i {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Bruger gTTS i stedet — {problem}\nRet det i Indstillinger → Oplæsning → Lyd."
    ),
    "Failed to load the database:": "Kunne ikke indlæse databasen:",
    "{selected} of {total} selected": "{selected} af {total} valgt",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "Skjul sidepanel",
    "Expand sidebar": "Udvid sidepanel",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Gemt {when} · {summary}",
    "the version from {date}": "versionen fra {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Beklager, den version kunne ikke gendannes:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Beklager, den version kunne ikke fjernes:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Gendan {count} element(er)?",
    "Restored {count} item(s).": "Gendannede {count} element(er).",
    "Select item(s) to restore.": "Vælg element(er), der skal gendannes.",
    "Permanently deleted {count} item(s).": "Slettede {count} element(er) permanent.",
    "Select item(s) to delete permanently.": "Vælg element(er), der skal slettes permanent.",
    "No items older than {n} days found.": "Ingen elementer ældre end {n} dage fundet.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Vil du slette elementer permanent, der er slettet for mere end {days} dage siden?\n\n"
        "Dette kan ikke fortrydes!"
    ),
    "Permanently deleted {count} old item(s).": "Slettede permanent {count} gamle element(er).",
    "Failed to load deleted items:\n{error}": "Kunne ikke indlæse slettede elementer:\n{error}",
    "Failed to count old items:\n{error}": "Kunne ikke optælle gamle elementer:\n{error}",
    "Failed to cleanup:\n{error}": "Kunne ikke rydde op:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Import Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Forventede kolonner: Language1, Language2, Word1, Word2 — angivet i en overskriftsrække "
        "eller uden overskrifter med de første fire kolonner i den rækkefølge. "
        "En færdig skabelon findes i appmenuen → Gem importskabelon."
    ),
    "All ({n})": "Alle ({n})",
    "To add ({n})": "Tilføjes ({n})",
    "To update ({n})": "Opdateres ({n})",
    "Skipped ({n})": "Sprunget over ({n})",
    "Unrecognized ({n})": "Uigenkendt ({n})",
    " · {n} with unrecognized language": " · {n} med uigenkendt sprog",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} rækker: {add} nye · {update} opdateringer · {skip} sprunget over"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Gennemse de foreslåede ændringer, og importer derefter de markerede rækker."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Intet at importere — ingen nye eller ændrede poster fundet."
    ),
    "Analyzing file…": "Analyserer fil…",
    "Could not read the Excel file — see the activity log.": (
        "Kunne ikke læse Excel-filen — se aktivitetsloggen."
    ),
    "Analysis failed — see the activity log.": "Analyse mislykkedes — se aktivitetsloggen.",
    "Import failed": "Import mislykkedes",
    "Import failed — see the activity log.": "Import mislykkedes — se aktivitetsloggen.",
    "Importing…": "Importerer…",
    "Importing {count} item(s)…": "Importerer {count} element(er)…",
    "Import {count} Item(s)": "Importer {count} element(er)",
    "Import finished:": "Import fuldført:",
    "Backup failed — see the activity log.": "Sikkerhedskopiering mislykkedes — se aktivitetsloggen.",
    "{n} added": "{n} tilføjet",
    "{n} updated": "{n} opdateret",
    "{n} failed": "{n} mislykkedes",
    "{n} failed.": "{n} mislykkedes.",
    "Export Import Log": "Eksporter importlog",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Definition — {word}",
    "Failed to save definition:\n{error}": "Kunne ikke gemme definition:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Rediger — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Kunne ikke gemme ord:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Tilknyt valgte tag(s) til hvert markeret ord"
    ),
    "Failed to add tag:\n{error}": "Kunne ikke tilføje tag:\n{error}",
    "Failed to apply tags:\n{error}": "Kunne ikke anvende tags:\n{error}",
    "Failed to remove tags:\n{error}": "Kunne ikke fjerne tags:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Genererer en tekst med AI ved hjælp af felterne Sprog, Niveau og Emne nedenfor. "
        "Vælg et emne eller skriv dit eget."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Genererer en {language} tekst ud fra {count} ord med {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Skriv eller indsæt en tekst i editoren nedenfor, giv den en titel, "
        "angiv sproget — og gem."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Udtrækker den læsbare artikeltekst fra enhver webside. "
        "Sider bag login eller opbygget udelukkende med JavaScript virker muligvis ikke."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "Vis definition (dobbeltklik)",
    "Read selected words aloud": "Læs markerede ord op",
    "Toggle favorite": "Tilføj/fjern fra favoritter",
    "Add / remove tags": "Tilføj / fjern tags",
    "Edit word": "Rediger ord",
    "Copy words": "Kopier ord",
    "Generate text from selection": "Generer tekst fra markering",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "PDF-filer (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excel-filer (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV-filer (*.csv)",
    "Text files (*.txt)": "Tekstfiler (*.txt)",
    "MP3 files (*.mp3)": "MP3-filer (*.mp3)",
    "Open Excel Table": "Åbn Excel-tabel",
    "Save Import Template": "Gem importskabelon",

    # Cloud sync status
    "Cloud sync": "Skysynkronisering",
    "Not connected. Check internet or credentials": "Ikke forbundet. Tjek internet eller legitimationsoplysninger",
    "Syncing with cloud…": "Synkroniserer med skyen…",
    "Sync completed successfully": "Synkronisering fuldført med succes",
    "Sync enabled but not connected. Check settings.": "Synkronisering aktiveret, men ikke forbundet. Tjek indstillinger.",
    "idle": "inaktiv",
    "syncing": "synkroniserer",
    "success": "succes",
    "error": "fejl",

    # Chart empty states
    "No data yet": "Ingen data endnu",
    "No activity yet": "Ingen aktivitet endnu",
    "Not enough activity yet": "Ikke nok aktivitet endnu",

    # Settings tabs
    "APIs": "API'er",
    "Audio (MP3)": "Lyd (MP3)",
    "Sync": "Synkronisering",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI API-nøgle (.env)",
    "Google API key (.env)": "Google API-nøgle (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Faktureres pr. forbrug — hent en nøgle på <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modeller: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API-forbrug — se <a href="https://platform.openai.com/usage">kontrolpanel</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Gratis niveau tilgængeligt — hent en nøgle på <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modeller: gemini-2.5-flash, gemini-2.5-flash-lite… API-forbrug — se <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Hent en nøgle på <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Brug https://api-free.deepl.com/v2/translate til nøgler på det gratis niveau.',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Klargør en Excel-fil med kolonnerne <b>Language1, Language2, Word1, Word2</b> — navngivet sådan i en overskriftsrække (ekstra kolonner ignoreres), eller uden overskrifter med de første fire kolonner i præcis den rækkefølge.</li><li>Åbn appmenuen → <i>Importer Excel til database…</i> og vælg filen.</li><li>Gennemse de foreslåede rækker, og klik på <i>Importer</i>.</li></ol>",

    # About dialog
    "created by": "oprettet af",
    "Version": "Version",
    "Build": "Build",
    "Your personal vocabulary companion": "Din personlige ordbogshjælper",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Opbyg, studer og husk ordforråd på tværs af sprog — med skysynkronisering, AI-assisterede definitioner, oversættelser, tekst-til-tale og fleksibel eksport.",
    "Source code": "Kildekode",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Din personlige ordbogshjælper med skysynkronisering, AI-definitioner, oversættelser, tekst-til-tale og eksportmuligheder.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Liceret under GNU Affero General Public License v3.0. Denne kreditering skal bevares (AGPL §7).",
    "Found a bug or have an idea?": "Fundet en fejl eller har du en idé?",
    "Report an issue": "Rapporter et problem",
    "What would you like to report?": "Hvad vil du rapportere?",
    "A bug or technical problem": "En fejl eller et teknisk problem",
    "Creates a report with app diagnostics to send to the developers.":
        "Opretter en rapport med appdiagnostik, der sendes til udviklerne.",
    "Inappropriate AI-generated content": "Upassende AI-genereret indhold",
    "Report a definition, text, or translation the AI produced.":
        "Rapporter en definition, tekst eller oversættelse skabt af AI.",
    "Report: inappropriate AI-generated content":
        "Rapport: upassende AI-genereret indhold",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Beskriv venligst det AI-genererede indhold, du rapporterer.\n\n"
        "Hvor det viste sig (definition / genereret tekst / ordoversættelse):\n"
        "Det gældende ord eller tekst:\n"
        "Hvorfor det er upassende:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "For at rapportere upassende AI-genereret indhold bedes du sende en e-mail til {email}.",

    # Support dialog
    "Support": "Støt",
    "Support Lingueez": "Støt Lingueez",
    "Lingueez is free and open-source.": "Lingueez er gratis og open source.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Hvis du kan lide Lingueez og finder det nyttigt, hjælper et engangsbidrag med at dække serverne til den valgfrie skysynkronisering og støtter den videre udvikling. Der er ingen betalingsmur — alle funktioner forbliver gratis under alle omstændigheder.",
    "Support Lingueez's development": "Støt udviklingen af Lingueez",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Stripe-valgmuligheden er et engangsbeløb — intet abonnement. Betalinger håndteres sikkert af Stripe eller GitHub.",

    # Updates
    "Updates": "Opdateringer",
    "Check for updates": "Søg efter opdateringer",
    "You're up to date.": "Du har den nyeste version.",
    "Update available": "Opdatering tilgængelig",
    "Update available — v{version}": "Opdatering tilgængelig — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} er tilgængelig — du har {current}.",
    "Skip this version": "Spring denne version over",
    "Later": "Senere",
    "Download": "Download",
    "Check for updates on startup": "Søg efter opdateringer ved opstart",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Søger én gang om dagen efter en nyere version og giver dig besked; "
        "intet downloades eller installeres automatisk.",

    # Misc units
    "in": "tomme",
    " s": " sek",

    # Word statuses (stored in English; only the displayed label is localized)
    "New": "Ny",
    "To Learn": "Skal læres",
    "Reviewing": "Repeteres",
    "Ignored": "Ignoreret",
    "Undo": "Fortryd",
    "Restored": "Gendannet",
    "Ignore word": "Ignorér ord",
    "Ignore this word": "Ignorér dette ord",
    "Already ignored.": "Allerede ignoreret.",
    "{count} word(s) won't come up in practice.": "{count} ord vises ikke længere i øvelser.",
    "'{word}' is back in rotation": "«{word}» er tilbage i rotation",
    "'{word}' won't come up again": "«{word}» dukker ikke op igen",
    "Mark for relearning": "Markér til at lære igen",
    "Forgot this word — move it to To Learn": "Glemt dette ord — flyt til «Skal læres»",
    "'{word}' is queued to learn again": "«{word}» er sat til at læres igen",
    "{count} word(s) queued to learn again.": "{count} ord sat til at læres igen.",
    "Nothing here to relearn yet.": "Der er ikke noget at lære igen endnu.",
    # "Learning" and "Mastered" translated in main blocks

    # Table density (settings → Table size)
    "Compact": "Kompakt",
    "Normal": "Normal",
    "Comfortable": "Komfortabel",
    "Spacious": "Rummelig",

    # Language names
    "English": "Engelsk",
    "German": "Tysk",
    "Spanish": "Spansk",
    "Ukrainian": "Ukrainsk",
    "French": "Fransk",
    "Italian": "Italiensk",
    "Portuguese": "Portugisisk",
    "Russian": "Russisk",
    "Greek": "Græsk",
    "Arabic": "Arabisk",
    "Bengali": "Bengali",
    "Cantonese": "Kantonesisk",
    "Hindi": "Hindi",
    "Japanese": "Japansk",
    "Korean": "Koreansk",
    "Mandarin": "Mandarin",
    "Polish": "Polsk",
    "Turkish": "Tyrkisk",
    "Vietnamese": "Vietnamesisk",
    "Afrikaans": "Afrikaans",
    "Albanian": "Albansk",
    "Amharic": "Amharisk",
    "Armenian": "Armensk",
    "Azerbaijani": "Aserbajdsjansk",
    "Basque": "Baskisk",
    "Belarusian": "Hviderussisk",
    "Bosnian": "Bosnisk",
    "Bulgarian": "Bulgarsk",
    "Catalan": "Katalansk",
    "Cebuano": "Cebuano",
    "Chichewa": "Chichewa",
    "Chinese": "Kinesisk",
    "Croatian": "Kroatisk",
    "Czech": "Tjekkisk",
    "Danish": "Dansk",
    "Dutch": "Nederlandsk",
    "Estonian": "Estisk",
    "Filipino": "Filippinsk",
    "Finnish": "Finsk",
    "Galician": "Galicisk",
    "Georgian": "Georgisk",
    "Gujarati": "Gujarati",
    "Haitian Creole": "Haitisk kreol",
    "Hausa": "Hausa",
    "Hawaiian": "Hawaiiansk",
    "Hebrew": "Hebraisk",
    "Hmong": "Hmong",
    "Hungarian": "Ungarsk",
    "Icelandic": "Islandsk",
    "Igbo": "Igbo",
    "Indonesian": "Indonesisk",
    "Irish": "Irsk",
    "Javanese": "Javansk",
    "Kannada": "Kannada",
    "Kazakh": "Kasakhisk",
    "Khmer": "Khmer",
    "Kinyarwanda": "Kinyarwanda",
    "Kyrgyz": "Kirgisisk",
    "Lao": "Laotisk",
    "Latin": "Latin",
    "Latvian": "Lettisk",
    "Lithuanian": "Litauisk",
    "Luxembourgish": "Luxembourgsk",
    "Macedonian": "Makedonsk",
    "Malagasy": "Madagaskisk",
    "Malay": "Malajisk",
    "Malayalam": "Malayalam",
    "Maltese": "Maltesisk",
    "Maori": "Maori",
    "Marathi": "Marathi",
    "Mongolian": "Mongolsk",
    "Myanmar (Burmese)": "Myanmar (burmesisk)",
    "Nepali": "Nepalesisk",
    "Norwegian": "Norsk",
    "Odia": "Odia",
    "Pashto": "Pashto",
    "Persian": "Persisk",
    "Punjabi": "Punjabi",
    "Romanian": "Rumænsk",
    "Samoan": "Samoansk",
    "Scots Gaelic": "Skotsk gælisk",
    "Serbian": "Serbisk",
    "Sesotho": "Sesotho",
    "Shona": "Shona",
    "Sindhi": "Sindhi",
    "Sinhala": "Singalesisk",
    "Slovak": "Slovakisk",
    "Slovenian": "Slovensk",
    "Somali": "Somali",
    "Sundanese": "Sundanesisk",
    "Swahili": "Swahili",
    "Swedish": "Svensk",
    "Tajik": "Tadsjikisk",
    "Tamil": "Tamil",
    "Tatar": "Tatarisk",
    "Telugu": "Telugu",
    "Thai": "Thai",
    "Turkmen": "Turkmensk",
    "Urdu": "Urdu",
    "Uyghur": "Uigurisk",
    "Uzbek": "Usbekisk",
    "Welsh": "Walisisk",
    "Xhosa": "Xhosa",
    "Yiddish": "Jiddisch",
    "Yoruba": "Yoruba",
    "Zulu": "Zulu",
    # --- Onboarding tour ---
    "Back": "Tilbage",
    "Next": "Næste",
    "Done": "Færdig",
    "Show Tour": "Vis rundvisning",
    "Step {n} of {total}": "Trin {n} af {total}",
    "Your library": "Dit bibliotek",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Skift mellem dine Ord, Tekster og Statistikker fra dette sidepanel.",
    "Add a word": "Tilføj et ord",
    "Find anything": "Find hvad som helst",
    "Search across your words, translations and tags as you type.":
        "Søg på tværs af dine ord, oversættelser og tags, mens du skriver.",
    "Add a new word here — its translation can be fetched automatically.":
        "Tilføj et nyt ord her — dets oversættelse kan hentes automatisk.",
    "Listen and learn": "Lyt og lær",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Vælg ord og tryk på Læs for at høre dem læst op. Gentagen "
        "lytning forfremmer hvert ord fra Ny til Repeteres, Lærer "
        "og til sidst Mestret.",
    "Generate a text": "Generer en tekst",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Forvandl valgte ord til en kort AI-skrevet historie — "
        "dit ordforråd i kontekst.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Dit ordforråd holdes synkroniseret på tværs af enheder. Klik for "
        "status eller for at synkronisere nu.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Aktiver skysynkronisering, skift sprog, ændr udseende og "
        "mere under Indstillinger.",
    # --- Texts tour ---
    "Add texts": "Tilføj tekster",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Skriv eller indsæt en tekst, hent en fra internettet "
        "(AI / Wikipedia / URL / RSS), eller importer .txt-filer.",
    "Your texts": "Dine tekster",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Gennemse dine gemte tekster, og filtrer dem efter sprog, "
        "niveau eller emne.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Lyt til enhver tekst oplæst — og klik på et ord under læsning "
        "for at se dets oversættelse eller tilføje det til din ordbog.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Vis en parallel oversættelse side om side; vælg sproget "
        "med pilen ved siden af.",
    "Reading modes": "Læsetilstande",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Fokustilstand skjuler listen, Papirtilstand ændrer "
        "baggrunden, og Rediger lader dig tilpasse teksten.",
    # --- Flashcards tour ---
    "Choose your deck": "Vælg dit kortsæt",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Vælg hvad der skal i kortsættet — kort klar til repetition, "
        "ord fra dit nuværende filter, de nyeste tilføjelser "
        "eller et håndplukket udvalg.",
    "Shape the session": "Tilpas sessionen",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Angiv hvor mange kort du vil gennemgå, bland deres rækkefølge, og "
        "få hvert kort udtalt, når det vises og vendes.",
    "Preview the deck": "Forhåndsvis kortsæt",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "De præcise kort, din session vil indeholde. Klik på et felt for at "
        "læse eller redigere dets definition, eller højttaleren for at høre "
        "ordet.",
    "Review and grade": "Repeter og bedøm",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Vend hvert kort, og bedøm hvor godt du kendte det — Svært, "
        "Godt eller Nemt. Spredt repetition afgør, hvornår hvert kort "
        "vender tilbage: nemme ord venter længere, svære kommer hurtigere "
        "tilbage. Mellemrum vendes med, 1–3 giver bedømmelse.",
    "Or just listen": "Eller bare lyt",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "«Afspil kortsæt» forvandler sessionen til lyd — kortene skifter "
        "og vendes i takt med stemmen. Sæt på pause når som helst for selv at bedømme "
        "et kort.",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Dit ordforråd med et øjekast — samlede tal, mestrede ord, "
        "sprog og din nuværende stime.",
    "See how your vocabulary has grown over time.":
        "Se hvordan dit ordforråd er vokset over tid.",
    "Track how much you've reviewed over time.":
        "Spor hvor meget du har repeteret over tid.",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Eksempel: En gåtur i byen",
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
        "Morgenen var lys, og gaderne var stille. En ung kvinde "
        "gik langsomt langs den gamle vej, mens hun kiggede på de høje huse og de "
        "små butikker, der lige var ved at åbne. Hun stoppede for at købe noget frisk "
        "brød og en kop kaffe og gik derefter over pladsen mod parken. "
        "Børn legede nær floden, mens deres forældre talte sammen på "
        "bænkene i nærheden. Hun satte sig under et stort træ, åbnede sin bog og "
        "begyndte at læse. Historien handlede om en rejsende, der krydsede "
        "bjergene for at lede efter en gammel ven, han ikke havde set i mange år. "
        "Efter et stykke tid kiggede hun op og så bådene drive langsomt ned ad "
        "floden og fuglene cirkle højt over tagryggene. En gademusiker "
        "begyndte at spille et sted i nærheden, og de bløde toner fulgte hendes "
        "tanker. Det var en rolig og lykkelig morgen, den slags hun bedst kunne lide.",
    "Demo": "Demo",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Ugyldig OpenAI API-nøgle. Tjek den i Indstillinger → Oversættelse og AI → AI → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Din OpenAI-konto er løbet tør for kredit. Tilføj kredit på "
        "platform.openai.com/account/billing, eller skift AI-udbyder "
        "til Gemini i Indstillinger → Oversættelse og AI → AI.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI-forbrugsgrænse nået. Vent et øjeblik, og prøv igen.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Ukendt OpenAI-model. Tjek modelnavnet i Indstillinger → Oversættelse og AI → AI → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "Kunne ikke oprette forbindelse til OpenAI. Tjek din internetforbindelse.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Gemini-kvote opbrugt. Det gratis niveau nulstilles dagligt; vent, "
        "eller opret en ny nøgle på aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Ugyldig Google API-nøgle. Tjek den i Indstillinger → Oversættelse og AI → AI → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Ukendt Gemini-model. Tjek modelnavnet i Indstillinger → Oversættelse og AI → AI → Gemini.",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "Din rejse med ordforråd starter her",
    "Add your first word — its translation can be fetched automatically.":
        "Tilføj dit første ord — dets oversættelse kan hentes automatisk.",
    "Add your first word": "Tilføj dit første ord",
    "Take the tour": "Tag rundvisningen",
    "No matching words": "Ingen matchende ord",
    "Try a different search or filter.": "Prøv en anden søgning eller et andet filter.",
    "Clear filters": "Ryd filtre",
    # --- Texts empty state ---
    "Your reading library starts here": "Dit læsebibliotek starter her",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Tilføj en tekst til læsning — skriv eller indsæt din egen, hent en fra "
        "internettet, eller importer en .txt-fil.",
    "Add a text": "Tilføj en tekst",
    "Fetch from the Internet": "Hent fra internettet",
    "Import .txt": "Importer .txt",
    # demo text-list stub titles
    "My first story": "Min første historie",
    "A news article": "En nyhedsartikel",
    "A short poem": "Et kort digt",
    "Travel notes": "Rejsenoter",
    # demo text-list stub first sentences
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Der var engang en nysgerrig ung ræv, der boede i en lille landsby ved havet.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Forskere har fundet en ny måde at undersøge, hvordan "
        "sprog ændrer sig og udvikler sig gennem århundrederne.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Vinden går blidt gennem efterårstræerne "
        "og bærer på gamle og halvt glemte sange.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Dag ét: vi ankom til byen sent om natten, og "
        "gaderne var stadig fyldt med varmt lys.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Elementer slettet på en anden enhed",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Mens denne enhed var offline, blev {n} element(er) slettet på dine "
        "andre enheder. Vil du beholde dem i skyen eller fjerne dem fra denne enhed?",
    "(untitled)": "(uden titel)",
    "[Text] {title}": "[Tekst] {title}",
    "Remove from this device": "Fjern fra denne enhed",
    "Decide later": "Beslut senere",
    "Keep & upload": "Behold og upload",
    "Not now": "Ikke nu",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Indtast et navn til offline-profilen.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Du kan have op til {max} offline-profiler. Fjern en for at tilføje en anden.",
    "New offline profile": "Ny offline-profil",
    "Profile name:": "Profilnavn:",
    "Offline profile": "Offline-profil",
    "Rename offline profile": "Omdøb offline-profil",
    "Offline profiles": "Offline-profiler",
    "Add offline profile…": "Tilføj offline-profil…",
    "Profile actions": "Profilhandlinger",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Adskilte biblioteker kun til denne enhed med deres egen database. De synkroniseres aldrig og kræver intet login.",
    "Default (local)": "Standard (lokal)",
    "Rename": "Omdøb",
    "Delete offline profile": "Slet offline-profil",
    "Enable cloud sync…": "Aktiver skysynkronisering…",
    "Could not create the profile.": "Kunne ikke oprette profilen.",
    "Created and switched to “{name}”.": "Oprettet og skiftet til “{name}”.",
    "Deleted “{name}”.": "Slettede “{name}”.",
    "Untitled profile": "Profil uden titel",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Vil du slette offline-profilen “{name}” permanent? Dets ord og tekster findes kun på denne enhed — der er ingen kopi i skyen. Databasen arkiveres i sikkerhedskopimappen først, men dette kan ikke fortrydes i appen.",
    "this profile": "denne profil",
    "Connect to the internet to merge this profile into your account.": "Opret forbindelse til internettet for at flette denne profil sammen med din konto.",
    "Enable cloud sync for this profile": "Aktiver skysynkronisering for denne profil",
    "Continue": "Fortsæt",
    "Upload words": "Upload ord",
    "Upload texts": "Upload tekster",
    "Upload & sync": "Upload og synkroniser",
    "Could not upload this profile. Your data is unchanged.": "Kunne ikke uploade denne profil. Dine data er uændrede.",
    "“{name}” is now synced to your account.": "“{name}” er nu synkroniseret med din konto.",
    "Everything in this profile is already in your account.": "Alt i denne profil er allerede på din konto.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Log ind eller opret en konto for at sikkerhedskopiere “{name}” og synkronisere den på tværs af dine enheder. Denne profils ord og tekster uploades, og den bliver din synkroniserede konto på denne enhed. En kopi arkiveres i mappen for sikkerhedskopier først.",
    "Upload “{name}” to your account": "Upload “{name}” til din konto",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Din profil bliver til den synkroniserede konto “{who}” på denne enhed og uploades til skyen.",
    "Merge “{name}” into your account": "Flet “{name}” ind i din konto",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Denne konto har allerede data på denne enhed. Ord og tekster fra din profil, som ikke findes der i forvejen, vil blive tilføjet — intet overskrives. “{name}” arkiveres derefter i sikkerhedskopimappen og fjernes.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Denne profil indeholder {items}, som kun er gemt på denne enhed. Aktiver skysynkronisering for at sikkerhedskopiere dem og studere på alle dine enheder.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Vælg de elementer, der skal tilføjes. De kopieres til din konto og uploades til skyen. “{name}” arkiveres derefter i sikkerhedskopimappen og fjernes.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Jeg accepterer <a href=\"{terms}\">servicevilkårene</a> og <a href=\"{privacy}\">privatlivspolitikken</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Accepter venligst servicevilkårene og privatlivspolitikken for at fortsætte.",
    "Updated Terms & Privacy": "Opdaterede vilkår og privatlivspolitik",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Vi har opdateret vores servicevilkår og privatlivspolitik. Gennemse og accepter dem venligst for at fortsætte med at bruge din konto.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Jeg accepterer de opdaterede <a href=\"{terms}\">servicevilkår</a> og <a href=\"{privacy}\">privatlivspolitikken</a>.",
    "Sign out": "Log ud",
    "I agree": "Jeg accepterer",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Privatlivspolitik</a> · <a href=\"{terms}\">Vilkår</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Ved at fortsætte accepterer du <a href=\"{terms}\">servicevilkårene</a> og <a href=\"{privacy}\">privatlivspolitikken</a>.",
    "Privacy Policy": "Privatlivspolitik",
    "Terms": "Vilkår",
    "Website": "Hjemmeside",
    "Contact": "Kontakt",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Flashcards",
    "Practice your vocabulary": "Øv dit ordforråd",
    "Due cards": "Kort til repetition",
    "Current filter": "Nuværende filter",
    "Newest": "Nyeste",
    "Selected words": "Valgte ord",
    "Deck size": "Kortsættets størrelse",
    "Default deck size": "Standardstørrelse på kortsæt",
    "Shuffle": "Bland",
    "Start session": "Start session",
    "Play deck": "Afspil kortsæt",
    "{n} cards ready to review": "{n} kort klar til repetition",
    "No cards due — great job!": "Ingen kort til repetition — godt gået!",
    "{n} selected words": "{n} valgte ord",
    "No words to practice.": "Ingen ord at øve.",
    "End session": "Afslut session",
    "Listening — pause to review manually":
        "Lytter — sæt på pause for at gennemgå manuelt",
    "Show answer": "Vis svar",
    "Hard": "Svært",
    "Good": "Godt",
    "Easy": "Nemt",
    "Space or click to flip": "Mellemrum eller klik for at vende",
    "Card {current} of {total}": "Kort {current} af {total}",
    "{n} correct": "{n} korrekte",
    "Session complete!": "Session fuldført!",
    "You listened to {n} of {total} cards.": "Du lyttede til {n} af {total} kort.",
    "Correct: {n} of {total}": "Korrekt: {n} af {total}",
    "New session": "Ny session",
    "Practice hard words": "Øv svære ord",
    "Hard words": "Svære ord",
    "Hard words cleared!": "Svære ord klaret!",
    "Open Flashcards when Read Aloud starts":
        "Åbn Flashcards når Oplæsning starter",
    "Stop": "Stop",
    "Auto-pronounce": "Automatisk udtale",
    "Speak each card as it appears and when it flips":
        "Udtal hvert kort, når det vises og når det vendes",
    "Deck preview": "Forhåndsvisning af kortsæt",
    "{n} cards": "{n} kort",
    "Due": "Tid til repetition",
    "In {n} d": "Om {n} d",
    "{n} d": "{n} d",
    "{n} mo": "{n} md",
    "{n} y": "{n} år",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez til Android…",
    "Android app": "Android-app",
    "Lingueez on Android": "Lingueez på Android",
    "Take your vocabulary with you": "Tag dit ordforråd med dig",
    "Preview of Lingueez on a phone": "Forhåndsvisning af Lingueez på en telefon",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Log ind med din Lingueez-konto, så er dit ordforråd der allerede — "
        "intet at opsætte, intet at flytte over.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Log ind med en gratis Lingueez-konto på begge, så synkroniseres dit ordforråd "
        "til telefonen — ingen filer skal kopieres over.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Log ind med en gratis Lingueez-konto, så synkroniseres dine ord til din telefon.",
    "Synced both ways": "Synkroniseret begge veje",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Ord, du tilføjer på telefonen, venter på computeren, og "
        "omvendt.",
    "Listen with the screen off": "Lyt med skærmen slukket",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Styring på låseskærmen, så en repetition fortsætter med telefonen "
        "i lommen.",
    "Save a word from any app": "Gem et ord fra en vilkårlig app",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Del tekst med Lingueez, så lander det i dit ordforråd, klar til "
        "at blive udfyldt senere.",
    "Point your phone's camera at the code":
        "Peg telefonens kamera mod koden",
    "Get it on Google Play": "Hent den i Google Play",
    "Copy link": "Kopier link",
    "Link copied": "Link kopieret",
    "Lingueez is now on Android": "Lingueez er nu på Android",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Log ind med din Lingueez-konto — dit ordforråd er der allerede.",
    "Dismiss": "Afvis",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Brug din Lingueez-konto problemfrit på tværs af computer og Android-enheder.",
    "Get the app…": "Hent appen…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Quiz",
    "Quiz (recall practice)": "Quiz (genkaldelsesøvelse)",
    "Recall your words, one question at a time":
        "Genkald dine ord, ét spørgsmål ad gangen",
    "Questions": "Spørgsmål",
    "Answer with": "Svar med",
    "Choices": "Valg",
    "Typing": "Indtastning",
    "Ask": "Spørg om",
    "Term": "Term",
    "Mixed": "Blandet",
    "Auto-advance": "Gå automatisk videre",
    "Move on by itself after a correct answer":
        "Gå videre af sig selv efter et rigtigt svar",
    "Speak the question, then the answer once it is revealed":
        "Læs spørgsmålet op, og svaret så snart det vises",
    "Start quiz": "Start quiz",
    "questions ready": "spørgsmål klar",
    "Nothing to quiz": "Intet at spørge om",
    "No words match this deck.": "Ingen ord passer til dette bundt.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "En quiz kræver mindst to ord — de forkerte svar kommer netop fra de ord, du "
        "ikke bliver spurgt om.",
    "Not enough words": "Ikke nok ord",
    "Add a few more words, or widen the deck.":
        "Tilføj et par ord, eller udvid bundtet.",
    "Question {n} of {total}": "Spørgsmål {n} af {total}",
    "Missed words": "Forkerte ord",
    "End quiz": "Afslut quiz",
    "Answer in {language}": "Svar på {language}",
    "Type the answer": "Skriv svaret",
    "Check": "Tjek",
    "Click to continue": "Klik for at fortsætte",
    "See results": "Se resultater",
    "Almost — it is \"{answer}\"": "Næsten — det er „{answer}“",
    "It is \"{answer}\"": "Det er „{answer}“",
    "Now {status}": "Nu {status}",
    "Correct": "Rigtige",
    "Missed": "Forkerte",
    "Worth another look": "Værd at se på igen",
    "Again": "Igen",
    "Missed words cleared!": "De forkerte ord er klaret!",
    "Perfect run": "Fejlfri runde",
    "Quiz complete": "Quiz gennemført",
    "Practice missed": "Øv fejlene",
    "Default number of questions": "Standardantal spørgsmål",
    "Move on after a correct answer": "Gå videre efter et rigtigt svar",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Vælg, hvad du bliver spurgt om",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "De samme bundter som ved kortene — ord til gentagelse, dit nuværende filter, "
        "de nyeste eller et selvvalgt udvalg — og hvor mange spørgsmål.",
    "Choices or typing": "Valg eller indtastning",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "„Valg“ giver fire svar at vælge imellem; „Indtastning“ beder dig skrive "
        "svaret — sværere, men den bedre prøve. Indtastning tilgiver accenter og små "
        "tastefejl. „Spørg om“ afgør, hvilken side du ser: termen, oversættelsen eller "
        "blandet.",
    "Start, and it counts": "Gå i gang — og det tæller",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "Bjælken viser bundtets sammensætning efter status. Hvert svar føder den samme "
        "gentagelsesplan som kortene: et ord, du husker, vender tilbage senere, et "
        "forkert tidligere.",
}

# Date names read by app.i18n.
MONTHS = ["januar", "februar", "marts", "april", "maj", "juni",
          "juli", "august", "september", "oktober", "november", "december"]
MONTHS_ABBR = ["jan.", "feb.", "mar.", "apr.", "maj", "jun.",
               "jul.", "aug.", "sep.", "okt.", "nov.", "dec."]
WEEKDAYS = ["Mandag", "Tirsdag", "Onsdag", "Torsdag",
            "Fredag", "Lørdag", "Søndag"]
WEEKDAYS_ABBR = ["Man", "Tir", "Ons", "Tor", "Fre", "Lør", "Søn"]