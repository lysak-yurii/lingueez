# Lingueez — German (de) translations.
# Keys are English UI strings; values are their German equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Deutsch"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Abbrechen",
    "OK": "OK",
    "Close": "Schließen",
    "Save": "Speichern",
    "Delete": "Löschen",
    "Edit": "Bearbeiten",
    "Remove": "Entfernen",
    "Add": "Hinzufügen",
    "Refresh": "Aktualisieren",
    "Import": "Importieren",
    "Export": "Exportieren",
    "Search": "Suchen",
    "Fetch": "Abrufen",
    "Browse…": "Durchsuchen…",
    "Clear": "Löschen",
    "Pause": "Pause",
    "Resume": "Fortsetzen",
    "Language": "Sprache",
    "Translation": "Übersetzung",
    "Word": "Wort",
    "Status": "Status",
    "Error": "Fehler",
    "Title": "Titel",
    "Topic": "Thema",
    "Level": "Niveau",
    "Generate": "Generieren",
    "Generating…": "Generieren…",
    "Translating…": "Übersetzen…",
    "Format": "Format",
    "Style": "Stil",
    "Model": "Modell",
    "Font": "Schriftart",
    "Usage": "Nutzung",
    "Translation language": "Übersetzungssprache",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Menü",
    "Open Excel Table…": "Excel-Tabelle öffnen…",
    "Import Excel to Database…": "Excel in Datenbank importieren…",
    "Save Import Template…": "Importvorlage speichern…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Audio (MP3)…",
    "Backups…": "Sicherungen…",
    "Show Source column": "Spalte „Quelle“ anzeigen",
    "Show Created At column": "Spalte „Erstellt am“ anzeigen",
    "Max words…": "Max. Wörter…",
    "View Log": "Protokoll anzeigen",
    "About": "Über",
    "Quit": "Beenden",
    "Words": "Wörter",
    "Texts": "Texte",
    "Statistics": "Statistiken",
    "Bin (deleted items)": "Papierkorb (gelöschte Elemente)",
    "Settings": "Einstellungen",
    "Vocabulary": "Wortschatz",
    "Search words, translations or tags…": "Wörter, Übersetzungen oder Tags suchen…",
    "Search texts by title, content or words…": "Texte nach Titel, Inhalt oder Wörtern suchen…",
    "Search scope": "Suchbereich",
    "Search scope…": "Suchbereich…",
    "Add word": "Wort hinzufügen",
    "Copy a word in any app, then press:":
        "Kopieren Sie ein Wort in einer App und drücken Sie:",
    "Set a shortcut": "Kürzel festlegen",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Kopieren Sie ein Wort in einer App und drücken Sie {keys} — es wird samt Übersetzung hinzugefügt.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Legen Sie in den Einstellungen ein Kürzel fest, um kopierte Wörter aus jeder App hinzuzufügen.",
    " Favorites": " Favoriten",
    " Filters": " Filter",
    "Filters that don't fit the table": "Filter, die nicht in die Tabelle passen",
    "More actions": "Weitere Aktionen",
    "Filter by tag": "Nach Tag filtern",
    "Close file and return to your vocabulary": "Datei schließen und zum Wortschatz zurückkehren",
    "Definition": "Definition",
    "Read": "Vorlesen",
    "Favorite": "Favorit",
    "Tags": "Tags",
    "Copy": "Kopieren",
    "Text": "Text",
    "Delete selected (Del)": "Ausgewählte löschen (Entf)",
    "No data": "Keine Daten",
    "No texts yet": "Noch keine Texte",
    "Words: {shown}/{total}": "Wörter: {shown}/{total}",
    "Texts: {total}": "Texte: {total}",
    "Texts: {shown}/{total}": "Texte: {shown}/{total}",
    "{count} selected": "{count} ausgewählt",
    "No selection": "Keine Auswahl",
    "Please select at least one word.": "Bitte wählen Sie mindestens ein Wort aus.",
    "Saved": "Gespeichert",
    "'{word}' updated.": "„{word}“ aktualisiert.",
    "Database Error": "Datenbankfehler",
    "Delete {count} word(s)?": "{count} Wort/Wörter löschen?",
    "Deleted": "Gelöscht",
    "{count} word(s) deleted.": "{count} Wort/Wörter gelöscht.",
    "Deleted with {n} error(s).": "Mit {n} Fehler(n) gelöscht.",
    "Favorites": "Favoriten",
    "{count} word(s) added to favorites.": "{count} Wort/Wörter zu Favoriten hinzugefügt.",
    "{count} word(s) removed from favorites.": "{count} Wort/Wörter aus Favoriten entfernt.",
    "Status set to '{status}' for {count} word(s).": "Status für {count} Wort/Wörter auf „{status}“ gesetzt.",
    "Max Words": "Maximale Wortanzahl",
    "Show only the first N words (0 = show all):": "Nur die ersten N Wörter anzeigen (0 = alle anzeigen):",
    "View Definition": "Definition anzeigen",
    "Copy Word": "Wort kopieren",
    "Copy Translation": "Übersetzung kopieren",
    "Toggle Favorite": "Favorit umschalten",
    "Change Status…": "Status ändern…",
    "Add / Remove Tags…": "Tags hinzufügen / entfernen…",
    "Read Aloud": "Laut vorlesen",
    "Change Status": "Status ändern",
    "New status:": "Neuer Status:",
    "Copied": "Kopiert",
    "{count} row(s) copied to clipboard.": "{count} Zeile(n) in die Zwischenablage kopiert.",
    "{count} item(s) copied to clipboard.": "{count} Element(e) in die Zwischenablage kopiert.",
    "Copy Word(s)": "Wort/Wörter kopieren",
    "Copy Translation(s)": "Übersetzung(en) kopieren",
    "Copy Both": "Beides kopieren",
    "Search in Word": "In Wort suchen",
    "Search in Translation": "In Übersetzung suchen",
    "Search in Tags": "In Tags suchen",
    "Promoted": "Befördert",
    "Google Cloud TTS unavailable": "Google Cloud TTS nicht verfügbar",
    "Selection limit": "Auswahllimit",
    "Only the first 200 selected words will be read.": "Nur die ersten 200 ausgewählten Wörter werden vorgelesen.",
    "Only the first 50 words will be used.": "Nur die ersten 50 Wörter werden verwendet.",
    "Select words to save as audio.": "Wählen Sie Wörter aus, die als Audio gespeichert werden sollen.",
    "Nothing to export.": "Nichts zum Exportieren vorhanden.",
    "Export Error": "Exportfehler",
    "Settings saved.": "Einstellungen gespeichert.",
    "Generated text saved.": "Generierter Text gespeichert.",
    "Show": "Anzeigen",
    "Add Word": "Wort hinzufügen",
    "Stop reading": "Vorlesen beenden",
    "Read — Read selected words aloud": "Vorlesen — Ausgewählte Wörter laut vorlesen",
    "Translation": "Übersetzung",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Erscheinungsbild",
    "Audio": "Audio",
    "Learning": "Lernen",
    "Listening": "Hören",
    "Backups": "Sicherungen",
    "Sync your library?": "Bibliothek synchronisieren?",
    "This will reconcile your device with the cloud:": "Dadurch wird Ihr Gerät mit der Cloud abgeglichen:",
    "Sync now": "Jetzt synchronisieren",
    "Upload": "Hochladen",
    "Synced — ↑{up} ↓{down}": "Synchronisiert — ↑{up} ↓{down}",
    "Upload restored library?": "Wiederhergestellte Bibliothek hochladen?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Bibliothek wiederhergestellt. Sie werden beim nächsten Verbinden mit einem Sync-Server aufgefordert, sie hochzuladen.",
    "Merging this restored backup with your cloud:": "Zusammenführen dieser wiederhergestellten Sicherung mit Ihrer Cloud:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Diese Sicherung enthält {items}. Jetzt hochladen und mit der Cloud zusammenführen oder die Cloud vorerst unverändert lassen?",
    "General": "Allgemein",
    "Read-aloud": "Vorlesefunktion",
    "Translation & AI": "Übersetzung & KI",
    "Data": "Daten",
    "Behavior": "Verhalten",
    "Progress": "Fortschritt",
    "DeepL request failed — using free Google Translate instead.": "DeepL-Anfrage fehlgeschlagen — stattdessen wird das kostenlose Google Translate verwendet.",
    "DeepL key isn't set — using free Google Translate instead.": "DeepL-Schlüssel nicht festgelegt — stattdessen wird das kostenlose Google Translate verwendet.",
    "System": "System",
    "Light": "Hell",
    "Dark": "Dunkel",
    "Appearance mode": "Erscheinungsbild-Modus",
    "Widget scaling": "Element-Skalierung",
    "Table size": "Tabellengröße",
    "Interface language": "Benutzeroberflächensprache",
    "Restart the app to apply the language change.": "Starten Sie die App neu, um die Sprachänderung anzuwenden.",
    "The interface language has changed. Restart now to apply it?": "Die Sprache der Benutzeroberfläche hat sich geändert. Jetzt neu starten, um sie anzuwenden?",
    "TTS provider": "TTS-Anbieter",
    "Google Cloud credentials": "Google Cloud-Anmeldedaten",
    "Voice type": "Stimmtyp",
    "Voice name (optional)": "Stimmenname (optional)",
    "Read Aloud playback": "Vorlese-Wiedergabe",
    "Pause between words (s)": "Pause zwischen Wörtern (s)",
    "Repeats per word": "Wiederholungen pro Wort",
    "Repeats per pair": "Wiederholungen pro Paar",
    "Promote status while listening": "Status beim Hören erhöhen",
    "Listens to reach {status}": "Anzahl Hördurchgänge für „{status}“",
    "Excel import": "Excel-Import",
    "Placeholder values": "Platzhalterwerte",
    "Skip placeholder rows": "Platzhalterzeilen überspringen",
    "Skip empty rows": "Leere Zeilen überspringen",
    "Normalize language pairs": "Sprachpaare normalisieren",
    "How to import": "Importanleitung",
    "Save import template…": "Importvorlage speichern…",
    "Active provider": "Aktiver Anbieter",
    "API key": "API-Schlüssel",
    "API URL": "API-URL",
    "Check usage": "Nutzung prüfen",
    "Enable cloud sync": "Cloud-Synchronisierung aktivieren",
    "Supabase URL (.env)": "Supabase-URL (.env)",
    "Supabase key (.env)": "Supabase-Schlüssel (.env)",
    "Bin cleanup grace (days)": "Aufbewahrungsfrist im Papierkorb (Tage)",
    "Test Connection": "Verbindung testen",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "Die Cloud-Synchronisierung nutzt Ihr eigenes Supabase-Projekt. Erstellen Sie die erforderlichen Tabellen einmalig und geben Sie oben die URL und den anon-Schlüssel ein.",
    "Copy schema SQL": "Schema-SQL kopieren",
    "Open SQL editor ↗": "SQL-Editor öffnen ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "Schema-SQL in die Zwischenablage kopiert. Öffnen Sie den SQL-Editor Ihres Supabase-Projekts, fügen Sie es ein und klicken Sie auf „Run“, um die Tabellen zu erstellen.",
    "Server": "Server",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Mit Ihrem eigenen Supabase-Server verbunden — persönlicher Modus, kein Konto erforderlich.\n{host}",
    "Use your own Supabase server (personal)": "Eigenen Supabase-Server verwenden (persönlich)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Persönliche Einzelbenutzer-Synchronisierung mit einem eigenen Supabase-Projekt. Kein Konto oder Login erforderlich — die App verbindet sich über den anon-Schlüssel des Projekts. Führen Sie das Schema-SQL in Ihrem Projekt aus, fügen Sie URL und anon-Schlüssel unten ein und klicken Sie auf „Verbindung testen“.\n\nHinweis: Jeder mit dieser URL und diesem Schlüssel kann die Daten lesen. Halten Sie das Projekt daher privat und teilen Sie den Schlüssel nicht.",
    "Disconnect — use the built-in server": "Trennen — integrierten Server verwenden",
    "Disconnect server": "Server trennen",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Synchronisierung mit Ihrem Supabase-Server beenden und wieder den integrierten Server nutzen?\n\nIhre Wörter bleiben in Ihrem Projekt und auf diesem Gerät gespeichert. Sie arbeiten rein lokal, bis Sie sich in einem Konto anmelden.",
    "Disconnected — using the built-in server.": "Getrennt — integrierter Server wird verwendet.",
    "{host} (personal)": "{host} (persönlich)",
    "Personal": "Persönlich",
    "your server": "Ihr Server",
    "Account actions": "Kontoaktionen",
    "Add account…": "Konto hinzufügen…",
    "Sync this device's data to my account…": "Daten dieses Geräts mit meinem Konto synchronisieren…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Konto",
    "Accounts": "Konten",
    "No accounts yet. Add one to sync your words across devices.": "Noch keine Konten vorhanden. Fügen Sie eines hinzu, um Ihre Wörter geräteübergreifend zu synchronisieren.",
    "(active)": "(aktiv)",
    "Sign in": "Anmelden",
    "(sign in again)": "(erneut anmelden)",
    "Switch": "Wechseln",
    "Remove account": "Konto entfernen",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "{email} von diesem Gerät entfernen? Sie können es jederzeit wieder hinzufügen — Ihre Wörter bleiben in der Cloud und die lokale Kopie auf der Festplatte erhalten. Ihre Cloud-Daten werden nicht gelöscht.",
    "Removed {email} from this device.": "{email} wurde von diesem Gerät entfernt.",
    "Your data was exported.": "Ihre Daten wurden exportiert.",
    "Export failed.": "Export fehlgeschlagen.",
    "Delete account": "Konto löschen",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Dadurch werden Ihr Konto und ALLE Ihre synchronisierten Wörter, Texte und Tags dauerhaft aus der Cloud gelöscht. Ihre lokale Kopie wird im Sicherungsordner archiviert. Dies kann nicht rückgängig gemacht werden.\n\nKonto wirklich löschen?",
    "Account deleted.": "Konto gelöscht.",
    "Could not delete the account.": "Das Konto konnte nicht gelöscht werden.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Name",
    "Enter your name.": "Geben Sie Ihren Namen ein.",
    "Email": "E-Mail",
    "Password": "Passwort",
    "New password": "Neues Passwort",
    "6-digit code": "6-stelliger Code",
    "or": "oder",
    "Sign in with Google": "Mit Google anmelden",
    "Opening your browser to sign in with Google…": "Browser wird geöffnet, um sich mit Google anzumelden…",
    "Forgot password?": "Passwort vergessen?",
    "Resend code": "Code erneut senden",
    "Confirm your email": "E-Mail-Adresse bestätigen",
    "Verify code": "Code bestätigen",
    "Use a different email": "Andere E-Mail verwenden",
    "Enter your email and password.": "Geben Sie Ihre E-Mail-Adresse und Ihr Passwort ein.",
    "Enter the 6-digit code from the email.": "Geben Sie den 6-stelligen Code aus der E-Mail ein.",
    "Enter the code and a new password.": "Geben Sie den Code und ein neues Passwort ein.",
    "Enter your email above first.": "Geben Sie zuerst oben Ihre E-Mail-Adresse ein.",
    "Enter the reset code we emailed you and a new password.": "Geben Sie den per E-Mail zugesandten Wiederherstellungscode und ein neues Passwort ein.",
    "Enter the 6-digit code we emailed you.": "Geben Sie den 6-stelligen Code ein, den wir Ihnen per E-Mail geschickt haben.",
    "Reset password": "Passwort zurücksetzen",
    "Set new password": "Neues Passwort festlegen",
    "Back to sign in": "Zurück zur Anmeldung",
    "Sign-in failed.": "Anmeldung fehlgeschlagen.",
    "Couldn't send the code.": "Code konnte nicht gesendet werden.",
    "Done.": "Fertig.",
    "Failed.": "Fehlgeschlagen.",
    "Create an account": "Konto erstellen",
    "Create account": "Konto erstellen",
    "I already have an account": "Ich habe bereits ein Konto",
    "Signed in as {email}": "Angemeldet als {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Daten dieses Geräts mit Ihrem Konto synchronisieren",
    "your account": "Ihr Konto",
    "This device has {words} and {texts} not yet in {account}.": "Dieses Gerät enthält {words} und {texts}, die noch nicht in {account} vorhanden sind.",
    "This device has {words} not yet in {account}.": "Dieses Gerät enthält {words}, die noch nicht in {account} vorhanden sind.",
    "This device has {texts} not yet in {account}.": "Dieses Gerät enthält {texts}, die noch nicht in {account} vorhanden sind.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Wählen Sie die hinzuzufügenden Elemente aus. Sie werden in Ihr Konto kopiert und in die Cloud hochgeladen, sodass sie auf Ihren anderen Geräten erscheinen. Die Kopie auf diesem Gerät bleibt erhalten.",
    "Don't ask again for this account": "Für dieses Konto nicht mehr fragen",
    "{n} word": "{n} Wort",
    "{n} words": "{n} Wörter",
    "{n} text": "{n} Text",
    "{n} texts": "{n} Texte",
    "Add {n} item": "{n} Element hinzufügen",
    "Add {n} items": "{n} Elemente hinzufügen",
    # Genitive/plural forms (reused/mapped for consistency in German)
    "words (genitive)": "Wörter",
    "texts (genitive)": "Texte",
    "tags (genitive)": "Tags",
    "changes (genitive)": "Änderungen",
    "deletions (genitive)": "Löschungen",
    "{n} words (genitive)": "{n} Wörter",
    "{n} texts (genitive)": "{n} Texte",
    "Add {n} items (genitive)": "{n} Elemente hinzufügen",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "{n} Element zu Ihrem Konto hinzugefügt.",
    "Added {n} items to your account.": "{n} Elemente zu Ihrem Konto hinzugefügt.",
    "Added {n} items to your account. (genitive)": "{n} Elemente zu Ihrem Konto hinzugefügt.",
    "{n} couldn't be added.": "{n} konnte(n) nicht hinzugefügt werden.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Sitzung abgelaufen — bitte erneut anmelden (Einstellungen → Synch)",
    "Sign in to sync (Settings → Sync)": "Anmelden zum Synchronisieren (Einstellungen → Synch)",
    "Sign in again to sync": "Erneut anmelden zum Synchronisieren",
    "Sign in again to use this account.": "Melden Sie sich erneut an, um dieses Konto zu nutzen.",
    "Sync incomplete: {reason}": "Synchronisierung unvollständig: {reason}",
    "Connect to the internet to add local items to your account.": "Mit dem Internet verbinden, um lokale Elemente zu Ihrem Konto hinzuzufügen.",
    "Everything on this device is already in your account.": "Alles auf diesem Gerät befindet sich bereits in Ihrem Konto.",
    "Upload local words?": "Lokale Wörter hochladen?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Ihre aktuellen lokalen Wörter in dieses Konto hochladen? Sie werden mit den Cloud-Daten zusammengeführt und synchronisiert.\n\nWählen Sie „Nein“, um vorhandene Daten zu behalten und die lokalen Wörter im Sicherungsordner zu archivieren.",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Anmeldung fehlgeschlagen. Überprüfen Sie E-Mail und Passwort.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Sie können maximal {max} Konten auf diesem Gerät speichern. Entfernen Sie eines, um ein neues hinzuzufügen.",
    "Wrong email or password.": "Falsche E-Mail-Adresse oder Passwort.",
    "That doesn't look like a valid email address.": "Das ist keine gültige E-Mail-Adresse.",
    "Confirm password": "Passwort bestätigen",
    "Passwords don't match.": "Passwörter stimmen nicht überein.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Ihre E-Mail ist noch nicht bestätigt. Geben Sie den 6-stelligen Code aus der E-Mail ein.",
    "That email is already registered. Try signing in instead.": "Diese E-Mail ist bereits registriert. Versuchen Sie stattdessen, sich anzumelden.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Wir haben Ihnen einen 6-stelligen Code per E-Mail gesendet. Geben Sie ihn ein, um die Registrierung abzuschließen.",
    "That code didn't work. Check it and try again.": "Dieser Code hat nicht funktioniert. Überprüfen Sie ihn und versuchen Sie es erneut.",
    "If that account exists, a 6-digit reset code is on its way.": "Falls das Konto existiert, wurde ein 6-stelliger Rücksetzcode gesendet.",
    "Confirmation email re-sent.": "Bestätigungs-E-Mail erneut gesendet.",
    "Too many attempts. Please wait a minute and try again.": "Zu viele Versuche. Bitte warten Sie eine Minute und versuchen Sie es erneut.",
    "Your password is too short — use at least 6 characters.": "Ihr Passwort ist zu kurz — verwenden Sie mindestens 6 Zeichen.",
    "Sign-ups are disabled on this server.": "Registrierungen sind auf diesem Server deaktiviert.",
    "Can't reach the server. Check your internet connection.": "Server nicht erreichbar. Überprüfen Sie Ihre Internetverbindung.",
    "Something went wrong.": "Etwas ist schiefgelaufen.",
    "Your saved sign-in for this account expired. Sign in again.": "Ihre gespeicherte Anmeldung ist abgelaufen. Bitte melden Sie sich erneut an.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "Cloud-Synch ist noch nicht konfiguriert. Fügen Sie zuerst URL und Schlüssel unter Einstellungen → Synch hinzu.",
    "Could not start Google sign-in.": "Google-Anmeldung konnte nicht gestartet werden.",
    "Google sign-in was cancelled or timed out.": "Google-Anmeldung wurde abgebrochen oder hat das Zeitlimit überschritten.",
    "Google sign-in failed.": "Google-Anmeldung fehlgeschlagen.",
    "Google sign-in failed: {error}": "Google-Anmeldung fehlgeschlagen: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Lokaler Anmelde-Helfer konnte nicht auf Port {port} gestartet werden ({error}). Schließen Sie die blockierende Anwendung und versuchen Sie es erneut.",
    "Export my data…": "Meine Daten exportieren…",
    "Delete account…": "Konto löschen…",
    "Cloud sync is on — your own server ({host})": "Cloud-Synch ist aktiv — eigener Server ({host})",
    "Cloud sync is on — signed in as {who}": "Cloud-Synch ist aktiv — angemeldet als {who}",
    "Cloud sync is off — your words are saved on this device only": "Cloud-Synch ist aus — Wörter werden nur auf diesem Gerät gespeichert",
    "(checking…)": "(prüfen…)",
    "(can't connect)": "(keine Verbindung)",
    "Turn off cloud sync": "Cloud-Synchronisierung ausschalten",
    "Cloud sync turned off — this device only.": "Cloud-Synch ausgeschaltet — nur dieses Gerät.",
    "Use this server": "Diesen Server verwenden",
    "Connecting…": "Verbinden…",
    "Testing…": "Testen…",
    "Applying theme…": "Design anwenden…",
    "Now syncing with your own server.": "Synchronisiert nun mit Ihrem eigenen Server.",
    "Could not connect to this server:\n{error}": "Verbindung zu diesem Server fehlgeschlagen:\n{error}",
    "Could not connect to this server.": "Verbindung zu diesem Server fehlgeschlagen.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nPrüfen Sie URL, anon-Schlüssel und das Schema-SQL. Diese Daten trotzdem verwenden?",
    "Enter your server's URL and anon key first, then test.": "Geben Sie zuerst Server-URL und anon-Schlüssel ein, dann testen.",
    "Enter your server's URL and anon key first.": "Geben Sie zuerst Server-URL und anon-Schlüssel ein.",
    "Supabase URL": "Supabase-URL",
    "Supabase key (anon)": "Supabase-Schlüssel (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Persönliche Synchronisierung mit einem eigenen Supabase-Projekt. Kein Konto notwendig — Verbindung erfolgt per anon-Schlüssel. Führen Sie das Schema-SQL aus, fügen Sie URL/Schlüssel ein, testen Sie und klicken Sie auf „Diesen Server verwenden“.\n\nHinweis: Halten Sie das Projekt privat und teilen Sie den Schlüssel nicht.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Synchronisierung beenden und wieder den integrierten Server nutzen?\n\nIhre Daten bleiben erhalten. Die Serverdetails werden gespeichert, sodass Sie jederzeit zurückwechseln können.",
    "Start automatically on login (minimized to tray)": "Automatisch bei der Anmeldung starten (im System-Tray minimieren)",
    "Add Word hotkey (global)": "Tastenkombination „Wort hinzufügen“ (global)",
    "Data format": "Datenformat",
    "Columns to export": "Zu exportierende Spalten",
    "Sheet name": "Tabellenblattname",
    "Start row": "Startzeile",
    "Start column": "Startspalte",
    "Shade alternate rows": "Abwechselnde Zeilen schattieren",
    "Auto column width": "Automatische Spaltenbreite",
    "Freeze header row": "Kopfzeile fixieren",
    "Delimiter": "Trennzeichen",
    "Delimiter (\\t = tab)": "Trennzeichen (\\t = Tab)",
    "Include header lines": "Kopfzeilen einschließen",
    "Header lines": "Kopfzeilen",
    "Page size": "Seitengröße",
    "Font size": "Schriftgröße",
    "Line spacing (pt)": "Zeilenabstand (pt)",
    "Text alignment": "Textausrichtung",
    "Margins L/R/T/B (pt)": "Ränder L/R/O/U (pt)",
    "Automatic widths (fit page)": "Automatische Breite (An Seite anpassen)",
    "Columns / width": "Spalten / Breite",
    "Header background": "Kopfzeilen-Hintergrund",
    "Header text": "Kopfzeilen-Text",
    "Row background": "Zeilen-Hintergrund",
    "Grid lines": "Gitterlinien",
    "Background image": "Hintergrundbild",
    "Concurrent workers": "Parallele Worker",
    "Requests per second": "Anfragen pro Sekunde",
    "Add font…": "Schriftart hinzufügen…",
    "Page && text": "Seite && Text",
    "Columns": "Spalten",
    "Max tokens": "Max. Token",
    "Temperature": "Temperatur",
    "Prompt template": "Prompt-Vorlage",
    "Definitions": "Definitionen",
    "Generated Texts (from words)": "Generierte Texte (aus Wörtern)",
    "Generated Texts (by topic)": "Generierte Texte (nach Thema)",
    "Text Adaptation (to level)": "Textanpassung (an Niveau)",
    "Thinking budget (0 = off, -1 = auto)": "Denk-Budget (0 = aus, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Sprache erkennen",
    "Type a word or phrase…": "Wort oder Phrase eingeben…",
    "Translation…": "Übersetzung…",
    "Pronounce": "Aussprechen",
    "Swap word and translation": "Wort und Übersetzung tauschen",
    "Translate with DeepL (Enter)": "Mit DeepL übersetzen (Eingabe)",
    "Save Word": "Wort speichern",
    "Enter a word to translate.": "Geben Sie ein Wort zum Übersetzen ein.",
    "Fill with AI (lemma + best translation)": "Mit KI ausfüllen (Lemma + beste Übersetzung)",
    "Enter a word to fill with AI.": "Geben Sie ein Wort ein, das per KI ausgefüllt werden soll.",
    "Source equals target — translated to {lang} instead.": "Quelle entspricht Ziel — stattdessen nach {lang} übersetzt.",
    "Both word and translation are required.": "Sowohl Wort als auch Übersetzung sind erforderlich.",
    "Please select the source language before saving.": "Bitte wählen Sie vor dem Speichern die Quellsprache aus.",
    "'{word}' already exists in your dictionary.": "„{word}“ existiert bereits in Ihrem Wörterbuch.",
    "'{word}' is already in your dictionary.": "„{word}“ ist bereits in Ihrem Wörterbuch.",
    "Already in your dictionary": "Bereits in Ihrem Wörterbuch",
    "Show existing": "Vorhandenes anzeigen",
    "The text was truncated to the first 100 words.": "Der Text wurde auf die ersten 100 Wörter gekürzt.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Mit KI generieren",
    "Regenerate with AI": "Neu generieren mit KI",
    "Definition 2": "Definition 2",
    "No definition yet": "Noch keine Definition vorhanden",
    "Generate one with AI, or write your own with Edit.": "Generieren Sie eine mit KI oder schreiben Sie eine eigene über „Bearbeiten“.",
    "There is no word to define.": "Es gibt kein Wort zu definieren.",
    "Bold": "Fett",
    "Italic": "Kursiv",
    "Heading": "Überschrift",
    "List": "Liste",
    "API key missing": "API-Schlüssel fehlt",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Legen Sie zuerst Ihren {ai}-API-Schlüssel unter Einstellungen → Übersetzung & KI → KI fest.",
    "Generating definition…": "Definition wird generiert…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Tags — {count} Wort/Wörter",
    "New tag name…": "Neuer Tag-Name…",
    "Add Tag": "Tag hinzufügen",
    "Apply Selected to All": "Ausgewählte auf alle anwenden",
    "Remove Selected": "Ausgewählte entfernen",
    "(partial)": "(teilweise)",
    "use(s)": "Verwendung(en)",
    "Tags marked ✓ apply to all selected words.": (
        "Mit ✓ markierte Tags gelten für alle ausgewählten Wörter."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (teilweise) bedeutet, dass nur einige Wörter den Tag haben."
    ),
    "Select tag(s) in the list first.": "Wählen Sie zuerst Tag(s) in der Liste aus.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Papierkorb — Gelöschte Elemente",
    "Delete Permanently": "Endgültig löschen",
    "Cleanup Old Items…": "Alte Elemente bereinigen…",
    "{n} selected": "{n} ausgewählt",
    "The bin is empty. Deleted words will appear here.":
        "Der Papierkorb ist leer. Gelöschte Wörter erscheinen hier.",
    "The bin is empty. Deleted texts will appear here.":
        "Der Papierkorb ist leer. Gelöschte Texte erscheinen hier.",
    "deleted {when}": "gelöscht {when}",
    "(empty)": "(leer)",
    "Untitled": "Ohne Titel",
    "Auto-deletes soon": "Wird bald automatisch gelöscht",
    "Auto-deletes in {n} day": "Automatische Löschung in {n} Tag",
    "Auto-deletes in {n} days": "Automatische Löschung in {n} Tagen",
    "Auto-deletes in {n} days (genitive)": "Automatische Löschung in {n} Tagen",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "{count} Element(e) endgültig löschen? Dies kann nicht rückgängig gemacht werden.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Frühere Version wiederherstellen",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Ihre Datenbank wird nach jeder Änderung automatisch gesichert. "
        "Wählen Sie unten eine frühere Version aus, um sie wiederherzustellen."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Noch keine gespeicherten Versionen. "
        "Nach jeder Änderung wird automatisch eine Sicherung erstellt."
    ),
    "Restore this version": "Diese Version wiederherstellen",
    "Today": "Heute",
    "Yesterday": "Gestern",
    "Most recent": "Neueste",
    "Before your last restore": "Vor Ihrer letzten Wiederherstellung",
    "today": "heute",
    "yesterday": "gestern",
    "today {time}": "heute um {time}",
    "yesterday {time}": "gestern um {time}",
    "the version from {date}": "die Version vom {date}",
    "the version from just before your last restore": "die Version direkt vor der letzten Wiederherstellung",
    "Restore Version": "Version wiederherstellen",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "{phrase} wiederherstellen?\n\nIhre aktuellen Daten werden zuerst gesichert, sodass Sie dies rückgängig machen können."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Ihre Datenbank wurde auf {phrase} wiederhergestellt.\n\n"
        "Meinung geändert? Stellen Sie „{before}“ wieder her, um die Aktion rückgängig zu machen."
    ),
    "Restore Error": "Wiederherstellungsfehler",
    "Sorry, that version could not be restored:\n{error}": "Diese Version konnte leider nicht wiederhergestellt werden:\n{error}",
    "Remove Version": "Version entfernen",
    "Remove {phrase}?": "{phrase} entfernen?",
    "Remove Error": "Fehler beim Entfernen",
    "Sorry, that version could not be removed:\n{error}": "Diese Version konnte leider nicht entfernt werden:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Text generieren",
    "Title…": "Titel…",
    "Generated text appears here…": "Generierter Text erscheint hier…",
    "Save to Texts": "In Texte speichern",
    "Save failed": "Speichern fehlgeschlagen",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Als Audio speichern",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Eine MP3-Datei aus {count} Wort/Übersetzungs-Paar(en) generieren."
    ),
    "Generating audio…": "Audio wird generiert…",
    "Compiling final audio file…": "Finale Audiodatei wird zusammengestellt…",
    "Processed: {word}": "Verarbeitet: {word}",
    "Choose File && Start": "Datei auswählen && Starten",
    "Cancelled.": "Abgebrochen.",
    "Audio saved": "Audio gespeichert",
    "Audio file saved to:\n{path}": "Audiodatei gespeichert unter:\n{path}",
    "Audio Error": "Audiofehler",
    "Failed to save audio:\n{error}": "Audio konnte nicht gespeichert werden:\n{error}",
    "Cancelling…": "Abbrechen…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Aus Excel importieren",
    "Row": "Zeile",
    "Word 1": "Wort 1",
    "Language 1": "Sprache 1",
    "Word 2": "Wort 2",
    "Language 2": "Sprache 2",
    "Action": "Aktion",
    "Details": "Details",
    "Add": "Hinzufügen",
    "Update": "Aktualisieren",
    "Skip": "Überspringen",
    "All": "Alle",
    "To add": "Hinzuzufügen",
    "To update": "Zu aktualisieren",
    "Skipped": "Übersprungen",
    "Unrecognized": "Nicht erkannt",
    "Only recognized languages": "Nur erkannte Sprachen",
    "Exclude rows whose language wasn't recognized.":
        "Zeilen ausschließen, deren Sprache nicht erkannt wurde.",
    "Unrecognized language — will be imported exactly as written.":
        "Nicht erkannte Sprache — wird exakt wie geschrieben importiert.",
    "Select all": "Alle auswählen",
    "Activity log": "Aktivitätsprotokoll",
    "Export log…": "Protokoll exportieren…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Exportieren…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Text hinzufügen",
    "Write": "Schreiben",
    "AI Generate": "KI-Generierung",
    "Wikipedia": "Wikipedia",
    "From URL": "Von URL",
    "Language:": "Sprache:",
    "Level:": "Niveau:",
    "Topic:": "Thema:",
    "Topic…": "Thema…",
    "Adapt to my level": "An mein Niveau anpassen",
    "Load entries": "Einträge laden",
    "Add feed…": "Feed hinzufügen…",
    "Ideas:": "Ideen:",
    "Short (~100 words)": "Kurz (~100 Wörter)",
    "Medium (~250 words)": "Mittel (~250 Wörter)",
    "Long (~500 words)": "Lang (~500 Wörter)",
    "Travel": "Reisen",
    "Food": "Essen",
    "Daily routine": "Alltag",
    "A short story": "Eine Kurzgeschichte",
    "News": "Nachrichten",
    "Dialogue at a café": "Dialog im Café",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Geben Sie Ihren Text ein oder fügen Sie ihn hier ein, oder rufen Sie einen über die Reiter oben ab…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Neueste zuerst",
    "Oldest first": "Älteste zuerst",
    "Title A–Z": "Titel A–Z",
    "All languages": "Alle Sprachen",
    "All levels": "Alle Niveaus",
    "All topics": "Alle Themen",
    "No matching texts": "Keine passenden Texte",
    "Try a different search or language filter.": "Versuchen Sie eine andere Suche oder einen anderen Sprachfilter.",
    "New text (write or paste)": "Neuer Text (schreiben oder einfügen)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Text aus dem Internet abrufen (KI / Wikipedia / URL / RSS)"
    ),
    "Import .txt file(s)": ".txt-Datei(en) importieren",
    "Read aloud": "Laut vorlesen",
    "Translate text": "Text übersetzen",
    "Hide translation": "Übersetzung ausblenden",
    "Focus mode": "Fokusmodus",
    "Exit focus mode": "Fokusmodus verlassen",
    "Paper mode: off": "Papiermodus: Aus",
    "Paper: white (click for sepia)": "Papier: Weiß (Klicken für Sepia)",
    "Paper: sepia (click to turn off)": "Papier: Sepia (Klicken zum Ausschalten)",
    "Save Changes": "Änderungen speichern",
    "Previous text": "Vorheriger Text",
    "Next text": "Nächster Text",
    "From words: {words}": "Aus Wörtern: {words}",
    "Created {date}": "Erstellt am {date}",
    "Unsaved changes": "Ungespeicherte Änderungen",
    "Save changes to '{title}'?": "Änderungen an „{title}“ speichern?",
    "Changes saved.": "Änderungen gespeichert.",
    "'{title}' moved to bin.": "„{title}“ in den Papierkorb verschoben.",
    "Reader": "Leser",
    'Pronounce "{word}"': '„{word}“ aussprechen',
    'Add "{word}" to vocabulary': '„{word}“ zum Wortschatz hinzufügen',
    "Read from here": "Ab hier lesen",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Quelle",
    "Added manually": "Manuell hinzugefügt",
    "From reader": "Aus dem Reader",
    "Created at": "Erstellt am",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Mit KI hinzufügen (Lemma + beste Übersetzung)",
    "Add to vocabulary as is": "So wie es ist zum Wortschatz hinzufügen",
    "Thinking…": "Nachdenken…",
    "'{pair}' is already in your dictionary.": "„{pair}“ ist bereits in Ihrem Wörterbuch.",
    "{label} — {translation} · added": "{label} — {translation} · hinzugefügt",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Cloud-Synchronisierung",
    "Last sync": "Letzte Synch.",
    "Pending": "Ausstehend",
    "never": "nie",
    "just now": "gerade eben",
    "{n} min ago": "vor {n} Min.",
    "Connected": "Verbunden",
    "Not connected": "Nicht verbunden",
    "change": "Änderung",
    "changes": "Änderungen",
    "deletion": "Löschung",
    "deletions": "Löschungen",
    "everything synced": "alles synchronisiert",
    "Initial sync has not completed yet.": "Die Erstsynchronisierung ist noch nicht abgeschlossen.",
    "Sync Now": "Jetzt synchronisieren",
    "Syncing…": "Synchronisieren…",
    # Local-only promo state
    "{words} and {texts}": "{words} und {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Sie haben hier {items} gespeichert. Melden Sie sich an, um sie zu sichern und auf all Ihren Geräten zu lernen.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Nur lokal — anmelden, um Ihre Wörter geräteübergreifend zu synchronisieren",
    "Sign in to sync across devices": "Anmelden zur geräteübergreifenden Synchronisierung",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Willkommen",
    "Welcome to {app}": "Willkommen bei {app}",
    "Sync across your devices": "Geräteübergreifend synchronisieren",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Melden Sie sich an, um Ihren Wortschatz zu sichern und auf jedem Gerät zu lernen.",
    "Automatic cloud backup": "Automatische Cloud-Sicherung",
    "Your words follow you to every computer.":
        "Ihre Wörter begleiten Sie auf jeden Computer.",
    "Never lose your progress.": "Verlieren Sie nie wieder Ihren Fortschritt.",
    "Study anywhere": "Überall lernen",
    "Pick up right where you left off.":
        "Machen Sie genau dort weiter, wo Sie aufgehört haben.",
    "Your data is yours — sign in only to sync it.":
        "Ihre Daten gehören Ihnen — eine Anmeldung ist nur zur Synchronisierung erforderlich.",
    "Sign in / Create account": "Anmelden / Konto erstellen",
    "Continue on this device": "Auf diesem Gerät fortfahren",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Wiedergabeeinstellungen",
    "Previous word": "Vorheriges Wort",
    "Next word": "Nächstes Wort",
    "Stop playback": "Wiedergabe stoppen",
    "Pause between words": "Pause zwischen Wörtern",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Nichts zum Lesen vorhanden.",
    "Previous sentence": "Vorheriger Satz",
    "Next sentence": "Nächster Satz",
    "Reading speed": "Lesegeschwindigkeit",
    "Sentence {n} / {total}": "Satz {n} / {total}",
    "buffering…": "pufferung…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Übersicht",
    "Learning status": "Lernstatus",
    "Activity": "Aktivität",
    "Review activity": "Wiederholungsaktivität",
    "Breakdown": "Aufschlüsselung",
    "Total words": "Wörter insgesamt",
    "Mastered": "Gemeistert",
    "In progress": "In Bearbeitung",
    "Languages": "Sprachen",
    "Current streak": "Aktuelle Serie",
    "Added this week": "Diese Woche hinzugefügt",
    "Definitions written": "Geschriebene Definitionen",
    "Status distribution": "Statusverteilung",
    "Words added over time": "Hinzugefügte Wörter im Zeitverlauf",
    "Activity calendar": "Aktivitätskalender",
    "Reviews over time": "Wiederholungen im Zeitverlauf",
    "Review calendar": "Wiederholungskalender",
    "Most reviewed words": "Am häufigsten wiederholte Wörter",
    "Top language pairs": "Top-Sprachpaare",
    "Top tags": "Top-Tags",
    "Reviewed this week": "Diese Woche wiederholt",
    "Total reviews": "Wiederholungen insgesamt",
    "Review streak": "Wiederholungsserie",
    "{pct}% of all words": "{pct}% aller Wörter",
    "actively learning": "aktiv am Lernen",
    "{n} pairs": "{n} Paar(e)",
    "best {n}d": "Rekord {n} T.",
    "{n} today": "{n} heute",
    "listens logged": "Hördurchgänge erfasst",
    "keep it going": "weiter so!",
    "Day": "Tag",
    "Week": "Woche",
    "Month": "Monat",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Textdateien importieren",
    "Text files (*.txt);;All files (*)": "Textdateien (*.txt);;Alle Dateien (*)",
    "Language of the imported text(s):": "Sprache der importierten Texte:",
    "Imported {count} text(s).": "{count} Text(e) importiert.",
    "Some files could not be imported:": "Einige Dateien konnten nicht importiert werden:",
    "Import failed:\n{error}": "Import fehlgeschlagen:\n{error}",
    "Failed to save text:\n{error}": "Text konnte nicht gespeichert werden:\n{error}",
    "Failed to delete text:\n{error}": "Text konnte nicht gelöscht werden:\n{error}",
    "Delete Text": "Text löschen",
    "Delete '{title}'?": "„{title}“ löschen?",
    "Unsupported language: {language}": "Nicht unterstützte Sprache: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Nicht unterstützte Sprache: {lang}. Wählen Sie eine aus der Liste.",
    "(empty)": "(leer)",
    "unsupported language": "nicht unterstützte Sprache",
    "unreadable text": "unlesbarer Text",
    "Skipped {n} {noun} ({reasons}).": "{n} {noun} übersprungen ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Einige Texte konnten nicht laut vorgelesen werden — nicht unterstützte Sprache "
        "oder unlesbare Zeichen.",
    "Edit text": "Text bearbeiten",
    "Done editing": "Bearbeitung beenden",
    "Delete text": "Text löschen",
    "Save Changes": "Änderungen speichern",
    "Paper mode": "Papiermodus",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Klicken Sie auf „+“, um einen Text zu schreiben/einzufügen, auf den Globus, um einen aus dem\n"
        "Internet abzurufen, oder wählen Sie Wörter in der Wörter-Ansicht aus und nutzen\n"
        "Sie die Aktion „Text“, um einen Lerntext zu generieren."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Durchsucht Wikipedia in der ausgewählten Sprache. Klicken Sie auf ein Ergebnis, um den Artikel zu laden; nutzen Sie „An mein Niveau anpassen“, um ihn zu vereinfachen."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Nachrichten-Feeds für die ausgewählte Sprache. Laden Sie einen Feed und doppelklicken Sie auf einen Eintrag, um den Volltext abzurufen. Fügen Sie eigene Feeds über „Feed hinzufügen…“ hinzu."
    ),
    "Length:": "Länge:",
    "Search Wikipedia (in the selected language)…": "Wikipedia durchsuchen (in ausgewählter Sprache)…",
    "Double-click an entry to load its full text.": "Doppelklicken Sie auf einen Eintrag, um dessen Volltext zu laden.",
    "Working…": "Wird verarbeitet…",
    "Show the {count} result(s) again": "Die {count} Ergebnis(se) erneut anzeigen",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "API-Schlüssel für {ai} ist nicht gesetzt. Konfigurieren Sie ihn unter Einstellungen → Übersetzung & KI → KI."
    ),
    "Generating with {ai}…": "Generieren mit {ai}…",
    'Fetching "{title}"…': "„{title}“ wird abgerufen…",
    "(yours)": "(Ihre)",
    "Fetching the full text…": "Volltext wird abgerufen…",
    "Add feed": "Feed hinzufügen",
    "Feed name:": "Feed-Name:",
    "Feed URL:": "Feed-URL:",
    "Failed to save the text.": "Text konnte nicht gespeichert werden.",
    "Failed to save the text: {error}": "Text konnte nicht gespeichert werden: {error}",
    "'{title}' saved.": "„{title}“ gespeichert.",
    "(untitled)": "(ohne Titel)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Schreiben Sie den Text unten für das ausgewählte GER-Niveau mit {ai} um"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Protokoll exportieren",
    "Activity Log": "Aktivitätsprotokoll",
    "Warnings & errors": "Warnungen & Fehler",
    "Errors only": "Nur Fehler",
    "Find…": "Suchen…",
    "Open log folder": "Protokollordner öffnen",
    "Export diagnostics": "Diagnose exportieren",
    "Clear the log file? This cannot be undone.":
        "Protokolldatei löschen? Dies kann nicht rückgängig gemacht werden.",
    "Could not create the diagnostics file.":
        "Diagnosedatei konnte nicht erstellt werden.",
    "Diagnostics saved to:\n{path}": "Diagnose gespeichert unter:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Beschreiben Sie das Problem**\n\n\n**Schritte zur Reproduktion**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nBitte fügen Sie die Diagnosedatei an:\n{path}\n",
    "Bug report: ": "Fehlerbericht: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Minimieren",
    "Maximize": "Maximieren",
    "Restore": "Wiederherstellen",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Steuerung anzeigen",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Keine Farbe",
    "None": "Keine",
    "Choose Color": "Farbe wählen",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Cloud-Synch: Inaktiv",
    "Failed to open table:\n{error}": "Tabelle konnte nicht geöffnet werden:\n{error}",
    "Failed to save template:\n{error}": "Vorlage konnte nicht gespeichert werden:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Anzeigen / verbergen",
    "Excel options": "Excel-Optionen",
    "CSV options": "CSV-Optionen",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Kopfzeilen werden ganz oben in der Datei geschrieben — Import-Tools wie "
        "Anki lesen diese aus (z. B. #separator:tab, #html:true). "
        "Die Spaltennamen selbst werden nicht geschrieben."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Kopieren Sie eine .ttf-Datei in den Schriftarten-Ordner der App und verwenden Sie sie"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Wird nur beim Exportieren von Wörtern in eine MP3-Datei verwendet. "
        "Die Stimme selbst wird auf dem Reiter „Audio“ konfiguriert."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "Die Stimme, die überall genutzt wird, wo Wörter gesprochen werden: beim Vorlesen "
        "in der App und beim MP3-Export. gTTS ist kostenlos und erfordert keine Einrichtung. Google Cloud TTS "
        "benötigt einen Dienstkonto-JSON-Schlüssel (Cloud Console → IAM & Admin → "
        "Service Accounts → Schlüssel) sowie aktiviertes Abrechnungskonto — "
        "die Nutzung innerhalb des kostenlosen monatlichen Kontingents bleibt gebührenfrei."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Das vollständige Anhören eines Wortes beim Vorlesen befördert es stufenweise: "
        "Neu → Wiedeholen → Lernen → Gemeistert. Jede Zahl ist die Gesamtzahl "
        "vollständiger Hördurchgänge, die zum Erreichen dieser Stufe erforderlich ist. Worte, "
        "die Sie manuell auf „Gemeistert“ oder „Ignoriert“ gesetzt haben, werden nie geändert, "
        "und ein Wort wird niemals herabgestuft."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Eine fertige .xlsx-Datei mit den passenden Kopfzeilen und Beispielzeilen speichern"
    ),
    "Google Translate (free)": "Google Translate (kostenlos)",
    "Google Translate is free and needs no API key.": (
        "Google Translate ist kostenlos und benötigt keinen API-Schlüssel."
    ),
    "Usage": "Nutzung",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Klicken Sie auf das Feld und drücken Sie die gewünschte Tastenkombination — sie öffnet "
        "„Wort hinzufügen“ mit dem Inhalt der Zwischenablage von überall aus. "
        "Lassen Sie es leer, um die Funktion zu deaktivieren."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Unter Wayland wird dieses Tastenkürzel bei Ihrem Desktop "
        "registriert und erscheint in den Tastatureinstellungen des Systems."
    ),
    "Add Word hotkey": "Tastenkürzel „Wort hinzufügen“",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Das globale Tastenkürzel „Wort hinzufügen“ ist in dieser "
        "Umgebung nicht verfügbar. Siehe Einstellungen ▸ System für Optionen."
    ),
    "The global Add-Word hotkey isn't available in the "
    "Flatpak sandbox on Wayland.": (
        "Das globale Tastenkürzel „Wort hinzufügen“ ist in der "
        "Flatpak-Sandbox unter Wayland nicht verfügbar."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Das globale Tastenkürzel „Wort hinzufügen“ wird auf diesem "
        "Wayland-Desktop noch nicht unterstützt."
    ),
    "To enable it, use any one of these:": "Um es zu aktivieren, nutzen Sie eine dieser Möglichkeiten:",
    "Log in to an X11 session instead of Wayland":
        "Melden Sie sich in einer X11-Sitzung anstelle von Wayland an",
    "Use a GNOME session — the global hotkey works there":
        "Nutzen Sie eine GNOME-Sitzung — dort funktioniert das globale Tastenkürzel",
    "Install the AppImage version — it runs outside the sandbox":
        "Installieren Sie die AppImage-Version — sie läuft außerhalb der Sandbox",
    "Download the AppImage": "AppImage herunterladen",
    "Add font…": "Schriftart hinzufügen…",
    "TrueType fonts (*.ttf)": "TrueType-Schriftarten (*.ttf)",
    "Could not copy the font file:\n{error}": "Schriftdatei konnte nicht kopiert werden:\n{error}",
    "Save import template…": "Importvorlage speichern…",
    "Excel files (*.xlsx)": "Excel-Dateien (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Vorlage gespeichert unter:\n{path}\n\n"
        "Füllen Sie sie mit Ihren Wörtern (ersetzen Sie die Beispielzeilen) "
        "und importieren Sie sie über das App-Menü → Excel in Datenbank importieren."
    ),
    "Could not save the template:\n{error}": "Vorlage konnte nicht gespeichert werden:\n{error}",
    "Background image": "Hintergrundbild",
    "Images (*.png *.jpg *.jpeg)": "Bilder (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON-Dateien (*.json)",
    "Connection successful! ✅": "Verbindung erfolgreich! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Keine Verbindung. Überprüfen Sie URL/Schlüssel und Ihre Internetverbindung."
    ),
    "Connection test failed:\n{error}": "Verbindungstest fehlgeschlagen:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} Zeichen in diesem Zeitraum",
    "{count} characters used": "{count} Zeichen verwendet",
    "Autostart": "Autostart",
    "Could not update autostart entry:\n{error}": "Autostart-Eintrag konnte nicht aktualisiert werden:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS ist ausgewählt, aber {problem}\n\n"
        "Audio wird auf gTTS zurückgreifen, bis dies behoben ist."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "Wort",
    "words": "Wörter",
    "words (genitive)": "Wörter",
    "text": "Text",
    "texts": "Texte",
    "texts (genitive)": "Texte",
    "tag": "Tag",
    "tags": "Tags",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Übersetzen",
    "AI": "KI",
    "Save As": "Speichern unter",
    "Save Audio As": "Audio speichern unter",
    "Save PDF As": "PDF speichern unter",
    "Added": "Hinzugefügt",
    "Updated": "Aktualisiert",
    "Failed": "Fehlgeschlagen",
    "Checking…": "Prüfen…",
    "Cleanup": "Bereinigung",
    "Permanent Delete": "Endgültig löschen",
    "No word": "Kein Wort",
    "Category": "Kategorie",
    "Bin": "Papierkorb",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Alle Tags",
    "Filter by tag — {tag}": "Nach Tag filtern — {tag}",
    "(showing first {n})": "(erste {n} werden angezeigt)",
    "Texts: {total}": "Texte: {total}",
    "Deleted with {n} error(s).": "Mit {n} Fehler(n) gelöscht.",
    "Failed to update: {error}": "Aktualisierung fehlgeschlagen: {error}",
    "Failed to export:\n{error}": "Export fehlgeschlagen:\n{error}",
    "Failed to export PDF:\n{error}": "PDF-Export fehlgeschlagen:\n{error}",
    "Failed to export TXT:\n{error}": "TXT-Export fehlgeschlagen:\n{error}",
    "PDF saved to {path}": "PDF gespeichert unter: {path}",
    "TXT file saved to {path}": "TXT-Datei gespeichert unter: {path}",
    "Template saved to {path}": "Vorlage gespeichert unter: {path}",
    "{format} file saved to {path}": "{format}-Datei gespeichert unter: {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Stattdessen wird gTTS verwendet — {problem}\nBeheben Sie dies unter Einstellungen → Vorlesen → Audio."
    ),
    "Failed to load the database:": "Datenbank konnte nicht geladen werden:",
    "{selected} of {total} selected": "{selected} von {total} ausgewählt",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "Seitenleiste einklappen",
    "Expand sidebar": "Seitenleiste ausklappen",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Gespeichert {when} · {summary}",
    "the version from {date}": "die Version vom {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Entschuldigung, diese Version konnte nicht wiederhergestellt werden:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Entschuldigung, diese Version konnte nicht entfernt werden:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "{count} Element(e) wiederherstellen?",
    "Restored {count} item(s).": "{count} Element(e) wiederhergestellt.",
    "Select item(s) to restore.": "Wählen Sie Element(e) zum Wiederherstellen aus.",
    "Permanently deleted {count} item(s).": "{count} Element(e) endgültig gelöscht.",
    "Select item(s) to delete permanently.": "Wählen Sie Element(e) zum endgültigen Löschen aus.",
    "No items older than {n} days found.": "Keine Elemente gefunden, die älter als {n} Tage sind.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Elemente endgültig löschen, die vor mehr als {days} Tagen gelöscht wurden?\n\n"
        "Dies kann nicht rückgängig gemacht werden!"
    ),
    "Permanently deleted {count} old item(s).": "{count} alte(s) Element(e) endgültig gelöscht.",
    "Failed to load deleted items:\n{error}": "Gelöschte Elemente konnten nicht geladen werden:\n{error}",
    "Failed to count old items:\n{error}": "Alte Elemente konnten nicht gezählt werden:\n{error}",
    "Failed to cleanup:\n{error}": "Bereinigung fehlgeschlagen:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Excel importieren",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Erwartete Spalten: Language1, Language2, Word1, Word2 — benannt in einer Kopfzeile "
        "oder ohne Kopfzeile mit den ersten vier Spalten in genau dieser Reihenfolge. "
        "Eine fertige Vorlage ist im App-Menü verfügbar → Importvorlage speichern."
    ),
    "All ({n})": "Alle ({n})",
    "To add ({n})": "Hinzuzufügen ({n})",
    "To update ({n})": "Zu aktualisieren ({n})",
    "Skipped ({n})": "Übersprungen ({n})",
    "Unrecognized ({n})": "Nicht erkannt ({n})",
    " · {n} with unrecognized language": " · {n} mit nicht erkannter Sprache",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} Zeilen: {add} neu · {update} Aktualisierungen · {skip} übersprungen"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Überprüfen Sie die vorgeschlagenen Änderungen und importieren Sie dann die ausgewählten Zeilen."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Nichts zu importieren — keine neuen oder geänderten Einträge gefunden."
    ),
    "Analyzing file…": "Datei wird analysiert…",
    "Could not read the Excel file — see the activity log.": (
        "Excel-Datei konnte nicht gelesen werden — siehe Aktivitätsprotokoll."
    ),
    "Analysis failed — see the activity log.": "Analyse fehlgeschlagen — siehe Aktivitätsprotokoll.",
    "Import failed": "Import fehlgeschlagen",
    "Import failed — see the activity log.": "Import fehlgeschlagen — siehe Aktivitätsprotokoll.",
    "Importing…": "Importieren…",
    "Importing {count} item(s)…": "{count} Element(e) werden importiert…",
    "Import {count} Item(s)": "{count} Element(e) importieren",
    "Import finished:": "Import abgeschlossen:",
    "Backup failed — see the activity log.": "Sicherung fehlgeschlagen — siehe Aktivitätsprotokoll.",
    "{n} added": "{n} hinzugefügt",
    "{n} updated": "{n} aktualisiert",
    "{n} failed": "{n} fehlgeschlagen",
    "{n} failed.": "{n} fehlgeschlagen.",
    "Export Import Log": "Import-Protokoll exportieren",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Definition — {word}",
    "Failed to save definition:\n{error}": "Definition konnte nicht gespeichert werden:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Bearbeiten — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Wort konnte nicht gespeichert werden:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Die ausgewählten Tag(s) an jedes ausgewählte Wort anhängen"
    ),
    "Failed to add tag:\n{error}": "Tag konnte nicht hinzugefügt werden:\n{error}",
    "Failed to apply tags:\n{error}": "Tags konnten nicht angewendet werden:\n{error}",
    "Failed to remove tags:\n{error}": "Tags konnten nicht entfernt werden:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Generiert einen Text mit KI unter Verwendung der Felder Sprache, Niveau und Thema unten. "
        "Wählen Sie einen Themen-Chip oder geben Sie ein eigenes ein."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Ein {language} Text aus {count} Wort/Wörtern wird mit {ai} generiert:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Geben Sie einen Text in den Editor unten ein, vergeben Sie einen Titel, "
        "legen Sie die Sprache fest — dann speichern."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Extrahiert den lesbaren Artikeltext von einer beliebigen Webseite. "
        "Seiten hinter einem Login oder reine JavaScript-Seiten funktionieren möglicherweise nicht."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "Definition anzeigen (Doppelklick)",
    "Read selected words aloud": "Ausgewählte Wörter laut vorlesen",
    "Toggle favorite": "Favorit umschalten",
    "Add / remove tags": "Tags hinzufügen / entfernen",
    "Edit word": "Wort bearbeiten",
    "Copy words": "Wörter kopieren",
    "Generate text from selection": "Text aus Auswahl generieren",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "PDF-Dateien (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excel-Dateien (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV-Dateien (*.csv)",
    "Text files (*.txt)": "Textdateien (*.txt)",
    "MP3 files (*.mp3)": "MP3-Dateien (*.mp3)",
    "Open Excel Table": "Excel-Tabelle öffnen",
    "Save Import Template": "Importvorlage speichern",

    # Cloud sync status
    "Cloud sync": "Cloud-Synchronisierung",
    "Not connected. Check internet or credentials": "Nicht verbunden. Internet oder Anmeldedaten prüfen",
    "Syncing with cloud…": "Synchronisiere mit der Cloud…",
    "Sync completed successfully": "Synchronisierung erfolgreich abgeschlossen",
    "Sync enabled but not connected. Check settings.": "Synch aktiviert, aber nicht verbunden. Einstellungen prüfen.",
    "idle": "inaktiv",
    "syncing": "synchronisieren",
    "success": "erfolgreich",
    "error": "Fehler",

    # Chart empty states
    "No data yet": "Noch keine Daten vorhanden",
    "No activity yet": "Noch keine Aktivität vorhanden",
    "Not enough activity yet": "Noch nicht genügend Aktivität vorhanden",

    # Settings tabs
    "APIs": "APIs",
    "Audio (MP3)": "Audio (MP3)",
    "Sync": "Synch",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI API-Schlüssel (.env)",
    "Google API key (.env)": "Google API-Schlüssel (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Abrechnung nach Nutzung — Schlüssel anfordern unter <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modelle: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API-Nutzung — siehe <a href="https://platform.openai.com/usage">Dashboard</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Kostenloses Kontingent verfügbar — Schlüssel erhalten unter <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modelle: gemini-2.5-flash, gemini-2.5-flash-lite… API-Nutzung — siehe <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Schlüssel anfordern unter <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Nutzen Sie https://api-free.deepl.com/v2/translate für kostenlose API-Schlüssel.',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Bereiten Sie eine Excel-Datei mit den Spalten <b>Language1, Language2, Word1, Word2</b> vor — exakt so benannt in einer Kopfzeile (zusätzliche Spalten werden ignoriert), oder ohne Kopfzeile mit den ersten vier Spalten in genau dieser Reihenfolge.</li><li>Öffnen Sie das App-Menü → <i>Excel in Datenbank importieren…</i> und wählen Sie die Datei aus.</li><li>Überprüfen Sie die vorgeschlagenen Zeilen und klicken Sie auf <i>Importieren</i>.</li></ol>",

    # About dialog
    "created by": "erstellt von",
    "Version": "Version",
    "Build": "Build",
    "Your personal vocabulary companion": "Ihr persönlicher Wortschatz-Begleiter",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Bauen Sie Ihren Wortschatz über verschiedene Sprachen hinweg auf, lernen Sie ihn und behalten Sie ihn im Gedächtnis — mit Cloud-Synchronisierung, KI-gestützten Definitionen, Übersetzungen, Sprachausgabe und flexiblem Export.",
    "Source code": "Quellcode",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Ihr persönlicher Wortschatz-Begleiter mit Cloud-Synch, KI-Definitionen, Übersetzungen, Sprachausgabe und Exportoptionen.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Lizenziert unter der GNU Affero General Public License v3.0. Diese Namensnennung muss erhalten bleiben (AGPL §7).",
    "Found a bug or have an idea?": "Einen Fehler gefunden oder eine Idee?",
    "Report an issue": "Ein Problem melden",
    "What would you like to report?": "Was möchten Sie melden?",
    "A bug or technical problem": "Einen Fehler oder ein technisches Problem",
    "Creates a report with app diagnostics to send to the developers.":
        "Erstellt einen Bericht mit App-Diagnosedaten zum Senden an die Entwickler.",
    "Inappropriate AI-generated content": "Unangemessene KI-generierte Inhalte",
    "Report a definition, text, or translation the AI produced.":
        "Melden Sie eine Definition, einen Text oder eine Übersetzung, die von der KI generiert wurde.",
    "Report: inappropriate AI-generated content":
        "Melden: Unangemessene KI-generierte Inhalte",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Bitte beschreiben Sie den KI-generierten Inhalt, den Sie melden möchten.\n\n"
        "Wo er erschienen ist (Definition / generierter Text / Wortübersetzung):\n"
        "Das betreffende Wort bzw. der Text:\n"
        "Warum er unangemessen ist:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "Um unangemessene KI-generierte Inhalte zu melden, senden Sie bitte eine E-Mail an {email}.",

    # Support dialog
    "Support": "Unterstützen",
    "Support Lingueez": "Lingueez unterstützen",
    "Lingueez is free and open-source.": "Lingueez ist kostenlos und Open Source.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Wenn Ihnen Lingueez gefällt und Sie es nützlich finden, hilft ein einmaliger Beitrag, die Serverkosten für die optionale Cloud-Synchronisierung zu decken und die Weiterentwicklung zu unterstützen. Es gibt keine Paywall — jede Funktion bleibt in jedem Fall kostenlos.",
    "Support Lingueez's development": "Entwicklung von Lingueez unterstützen",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Die Stripe-Option ist einmalig — kein Abonnement. Zahlungen werden sicher über Stripe oder GitHub abgewickelt.",

    # Updates
    "Updates": "Updates",
    "Check for updates": "Auf Updates prüfen",
    "You're up to date.": "Sie sind auf dem neuesten Stand.",
    "Update available": "Update verfügbar",
    "Update available — v{version}": "Update verfügbar — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} ist verfügbar — Sie haben Version {current}.",
    "Skip this version": "Diese Version überspringen",
    "Later": "Später",
    "Download": "Herunterladen",
    "Check for updates on startup": "Beim Start auf Updates prüfen",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Prüft einmal täglich auf eine neuere Version und benachrichtigt Sie; "
        "es wird niemals etwas automatisch heruntergeladen oder installiert.",

    # Misc units
    "in": "Zoll",
    " s": " s",

    # Word statuses (stored in English; only the displayed label is localized)
    "New": "Neu",
    "To Learn": "Zu lernen",
    "Reviewing": "Wiederholen",
    "Ignored": "Ignoriert",

    # Table density (settings → Table size)
    "Compact": "Kompakt",
    "Normal": "Normal",
    "Comfortable": "Komfortabel",
    "Spacious": "Großzügig",

    # Language names
    "English": "Englisch",
    "German": "Deutsch",
    "Spanish": "Spanisch",
    "Ukrainian": "Ukrainisch",
    "French": "Französisch",
    "Italian": "Italienisch",
    "Portuguese": "Portugiesisch",
    "Russian": "Russisch",
    "Greek": "Griechisch",
    "Arabic": "Arabisch",
    "Bengali": "Bengali",
    "Cantonese": "Kantonessisch",
    "Hindi": "Hindi",
    "Japanese": "Japanisch",
    "Korean": "Koreanisch",
    "Mandarin": "Mandarin",
    "Polish": "Polnisch",
    "Turkish": "Türkisch",
    "Vietnamese": "Vietnamesisch",
    "Afrikaans": "Afrikaans",
    "Albanian": "Albanisch",
    "Amharic": "Amharisch",
    "Armenian": "Armenisch",
    "Azerbaijani": "Aserbaidschanisch",
    "Basque": "Baskisch",
    "Belarusian": "Weissrussisch",
    "Bosnian": "Bosnisch",
    "Bulgarian": "Bulgarisch",
    "Catalan": "Katalanisch",
    "Cebuano": "Cebuano",
    "Chichewa": "Chichewa",
    "Chinese": "Chinesisch",
    "Croatian": "Kroatisch",
    "Czech": "Tschechisch",
    "Danish": "Dänisch",
    "Dutch": "Niederländisch",
    "Estonian": "Estnisch",
    "Filipino": "Filipino",
    "Finnish": "Finnisch",
    "Galician": "Galicisch",
    "Georgian": "Georgisch",
    "Gujarati": "Gujarati",
    "Haitian Creole": "Haitianisches Kreol",
    "Hausa": "Hausa",
    "Hawaiian": "Hawaiianisch",
    "Hebrew": "Hebräisch",
    "Hmong": "Hmong",
    "Hungarian": "Ungarisch",
    "Icelandic": "Isländisch",
    "Igbo": "Igbo",
    "Indonesian": "Indonesisch",
    "Irish": "Irisch",
    "Javanese": "Javanisch",
    "Kannada": "Kannada",
    "Kazakh": "Kasachisch",
    "Khmer": "Khmer",
    "Kinyarwanda": "Kinyarwanda",
    "Kyrgyz": "Kirgisisch",
    "Lao": "Laotisch",
    "Latin": "Latein",
    "Latvian": "Lettisch",
    "Lithuanian": "Litauisch",
    "Luxembourgish": "Luxemburgisch",
    "Macedonian": "Mazedonisch",
    "Malagasy": "Madagassisch",
    "Malay": "Malaiisch",
    "Malayalam": "Malayalam",
    "Maltese": "Maltesisch",
    "Maori": "Maori",
    "Marathi": "Marathi",
    "Mongolian": "Mongolisch",
    "Myanmar (Burmese)": "Myanmar (Birmanisch)",
    "Nepali": "Nepalesisch",
    "Norwegian": "Norwegisch",
    "Odia": "Odia",
    "Pashto": "Paschtu",
    "Persian": "Persisch",
    "Punjabi": "Punjabi",
    "Romanian": "Rumänisch",
    "Samoan": "Samoanisch",
    "Scots Gaelic": "Schottisches Gälisch",
    "Serbian": "Serbisch",
    "Sesotho": "Sesotho",
    "Shona": "Shona",
    "Sindhi": "Sindhi",
    "Sinhala": "Singhalesisch",
    "Slovak": "Slowakisch",
    "Slovenian": "Slowenisch",
    "Somali": "Somali",
    "Sundanese": "Sundanesisch",
    "Swahili": "Suaheli",
    "Swedish": "Schwedisch",
    "Tajik": "Tadschikisch",
    "Tamil": "Tamil",
    "Tatar": "Tatarisch",
    "Telugu": "Telugu",
    "Thai": "Thailändisch",
    "Turkmen": "Turkmenisch",
    "Urdu": "Urdu",
    "Uyghur": "Uigurisch",
    "Uzbek": "Usbekisch",
    "Welsh": "Walisisch",
    "Xhosa": "Xhosa",
    "Yiddish": "Jiddisch",
    "Yoruba": "Yoruba",
    "Zulu": "Zulu",
    # --- Onboarding tour ---
    "Back": "Zurück",
    "Next": "Weiter",
    "Done": "Fertig",
    "Show Tour": "Tour anzeigen",
    "Step {n} of {total}": "Schritt {n} von {total}",
    "Your library": "Ihre Bibliothek",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Wechseln Sie über diese Seitenleiste zwischen Ihren Wörtern, Texten und Statistiken.",
    "Add a word": "Ein Wort hinzufügen",
    "Find anything": "Alles finden",
    "Search across your words, translations and tags as you type.":
        "Durchsuchen Sie Ihre Wörter, Übersetzungen und Tags direkt beim Tippen.",
    "Add a new word here — its translation can be fetched automatically.":
        "Fügen Sie hier ein neues Wort hinzu — seine Übersetzung kann automatisch abgerufen werden.",
    "Listen and learn": "Hören und lernen",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Wählen Sie Wörter aus und klicken Sie auf Vorlesen, um sie laut zu hören. Wiederholtes "
        "Anhören stuft jedes Wort von Neu zu Wiederholen, Lernen "
        "und schließlich Gemeistert hoch.",
    "Generate a text": "Einen Text generieren",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Verwandeln Sie ausgewählte Wörter in eine kurze, KI-generierte Geschichte — "
        "Ihr Wortschatz im Kontext.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Ihr Wortschatz bleibt auf allen Geräten synchron. Klicken Sie für den "
        "Status oder um jetzt zu synchronisieren.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Aktivieren Sie Cloud-Synch, wechseln Sie die Sprache, ändern Sie das Erscheinungsbild "
        "und mehr in den Einstellungen.",
    # --- Texts tour ---
    "Add texts": "Texte hinzufügen",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Schreiben oder fügen Sie einen Text ein, rufen Sie einen aus dem Internet ab "
        "(KI / Wikipedia / URL / RSS) oder importieren Sie .txt-Dateien.",
    "Your texts": "Ihre Texte",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Durchsuchen Sie Ihre gespeicherten Texte und filtern Sie sie nach Sprache, "
        "Niveau oder Thema.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Hören Sie sich jeden Text laut an — und klicken Sie beim Lesen auf ein Wort, "
        "um dessen Übersetzung zu sehen oder es zu Ihrem Wortschatz hinzuzufügen.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Zeigen Sie eine Parallelübersetzung nebeneinander an; wählen Sie die Sprache "
        "mit dem Pfeil daneben aus.",
    "Reading modes": "Lesemodi",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Der Fokusmodus blendet die Liste aus, der Papiermodus ändert den "
        "Hintergrund, und über Bearbeiten können Sie den Text anpassen.",
    # --- Flashcards tour ---
    "Choose your deck": "Deck auswählen",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Wählen Sie aus, was im Deck sein soll — fällige Karten zur Wiederholung, "
        "Wörter aus Ihrem aktuellen Filter, die neuesten Einträge "
        "oder eine manuelle Auswahl.",
    "Shape the session": "Sitzung gestalten",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Legen Sie fest, wie viele Karten wiederholt werden sollen, mischen Sie die Reihenfolge und "
        "lassen Sie jede Karte vorlesen, sobald sie erscheint und umgedreht wird.",
    "Preview the deck": "Vorschau des Decks",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Genau diese Karten werden in Ihrer Sitzung enthalten sein. Klicken Sie auf eine Kachel, "
        "um ihre Definition zu lesen oder zu bearbeiten, oder auf den Lautsprecher, um das "
        "Wort zu hören.",
    "Review and grade": "Wiederholen und bewerten",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Drehen Sie jede Karte um und bewerten Sie, wie gut Sie sie kannten — Schwer, "
        "Gut oder Einfach. Die zeitlich versetzte Wiederholung entscheidet, wann jede Karte "
        "wieder auftaucht: einfache Wörter warten länger, schwere kommen "
        "schneller zurück. Leertaste zum Umdrehen, 1–3 zum Bewerten.",
    "Or just listen": "Oder einfach zuhören",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "„Deck abspielen“ verwandelt die Sitzung in Audio — Karten wechseln "
        "und drehen sich synchron zur Stimme. Pausieren Sie jederzeit, um "
        "eine Karte selbst zu bewerten.",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Ihr Wortschatz auf einen Blick — Gesamtzahlen, gemeisterte Wörter, "
        "Sprachen und Ihre aktuelle Serie.",
    "See how your vocabulary has grown over time.":
        "Sehen Sie, wie Ihr Wortschatz im Laufe der Zeit gewachsen ist.",
    "Track how much you've reviewed over time.":
        "Verfolgen Sie, wie viel Sie im Laufe der Zeit wiederholt haben.",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Beispiel: Ein Spaziergang in der Stadt",
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
        "Der Morgen war hell und die Straßen waren ruhig. Eine junge Frau "
        "ging langsam die alte Straße entlang und betrachtete die hohen Häuser und die "
        "kleinen Geschäfte, die gerade öffneten. Sie hielt an, um frisches "
        "Brot und einen Kaffee zu kaufen, und überquerte dann den Platz in Richtung Park. "
        "Kinder spielten in der Nähe des Flusses, während sich ihre Eltern auf den "
        "Bänken in der Nähe unterhielten. Sie setzte sich unter einen großen Baum, öffnete ihr Buch und "
        "begann zu lesen. Die Geschichte handelte von einem Reisenden, der die "
        "Berge überquerte, auf der Suche nach einem alten Freund, den er seit vielen Jahren nicht gesehen hatte. "
        "Nach einer Weile blickte sie auf und beobachtete, wie die Boote langsam den "
        "Fluss hinabtrieben und die Vögel hoch über den Dächern kreisten. Ein Straßenmusiker "
        "begann irgendwo in der Nähe zu spielen, und die sanften Töne begleiteten ihre "
        "Gedanken. Es war ein ruhiger und glücklicher Morgen, so wie sie ihn am liebsten mochte.",
    "Demo": "Demo",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Ungültiger OpenAI API-Schlüssel. Prüfen Sie ihn unter Einstellungen → Übersetzung & KI → KI → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Ihr OpenAI-Konto hat kein Guthaben mehr. Laden Sie Guthaben auf unter "
        "platform.openai.com/account/billing oder wechseln Sie den KI-Anbieter "
        "zu Gemini unter Einstellungen → Übersetzung & KI → KI.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI-Ratenlimit erreicht. Warten Sie einen Moment und versuchen Sie es erneut.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Unbekanntes OpenAI-Modell. Prüfen Sie den Modellnamen unter Einstellungen → Übersetzung & KI → KI → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "OpenAI konnte nicht erreicht werden. Überprüfen Sie Ihre Internetverbindung.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Gemini-Kontingent erschöpft. Das kostenlose Kontingent wird täglich zurückgesetzt; warten Sie "
        "oder erstellen Sie einen neuen Schlüssel unter aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Ungültiger Google API-Schlüssel. Prüfen Sie ihn unter Einstellungen → Übersetzung & KI → KI → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Unbekanntes Gemini-Modell. Prüfen Sie den Modellnamen unter Einstellungen → Übersetzung & KI → KI → Gemini.",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "Ihre Wortschatz-Reise beginnt hier",
    "Add your first word — its translation can be fetched automatically.":
        "Fügen Sie Ihr erstes Wort hinzu — seine Übersetzung kann automatisch abgerufen werden.",
    "Add your first word": "Erstes Wort hinzufügen",
    "Take the tour": "Tour machen",
    "No matching words": "Keine passenden Wörter",
    "Try a different search or filter.": "Versuchen Sie eine andere Suche oder einen anderen Filter.",
    "Clear filters": "Filter zurücksetzen",
    # --- Texts empty state ---
    "Your reading library starts here": "Ihre Lese-Bibliothek beginnt hier",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Fügen Sie einen Text zum Lesen hinzu — schreiben oder fügen Sie einen eigenen ein, rufen Sie einen aus dem "
        "Internet ab oder importieren Sie eine .txt-Datei.",
    "Add a text": "Text hinzufügen",
    "Fetch from the Internet": "Aus dem Internet abrufen",
    "Import .txt": ".txt importieren",
    # demo text-list stub titles
    "My first story": "Meine erste Geschichte",
    "A news article": "Ein Zeitungsartikel",
    "A short poem": "Ein kurzes Gedicht",
    "Travel notes": "Reisenotizen",
    # demo text-list stub first sentences (shown as the list snippet)
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Es war einmal in einem kleinen Dorf am Meer, "
        "da lebte ein neugieriger junger Fuchs.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Forscher haben einen neuen Weg gefunden, um zu untersuchen, wie "
        "sich Sprachen im Laufe der Jahrhunderte verändern und entwickeln.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Der Wind weht sanft durch die herbstlichen Bäume "
        "und trägt alte, halb vergessene Lieder mit sich.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Tag eins: Wir kamen spät in der Nacht in der Stadt an, und die "
        "Straßen waren immer noch von warmem Licht erfüllt.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Auf einem anderen Gerät gelöschte Elemente",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Während dieses Gerät offline war, wurden {n} Element(e) hier auf Ihren "
        "anderen Geräten gelöscht. In der Cloud behalten oder von diesem Gerät entfernen?",
    "(untitled)": "(ohne Titel)",
    "[Text] {title}": "[Text] {title}",
    "Remove from this device": "Von diesem Gerät entfernen",
    "Decide later": "Später entscheiden",
    "Keep & upload": "Behalten & hochladen",
    "Not now": "Nicht jetzt",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Geben Sie einen Namen für das Offline-Profil ein.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Sie können bis zu {max} Offline-Profile behalten. Entfernen Sie eines, um ein neues hinzuzufügen.",
    "New offline profile": "Neues Offline-Profil",
    "Profile name:": "Profilname:",
    "Offline profile": "Offline-Profil",
    "Rename offline profile": "Offline-Profil umbenennen",
    "Offline profiles": "Offline-Profile",
    "Add offline profile…": "Offline-Profil hinzufügen…",
    "Profile actions": "Profilaktionen",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Separate, reine Geräte-Bibliotheken mit eigener Datenbank. Sie werden nie synchronisiert und benötigen keinen Login.",
    "Default (local)": "Standard (lokal)",
    "Rename": "Umbenennen",
    "Delete offline profile": "Offline-Profil löschen",
    "Enable cloud sync…": "Cloud-Synchronisierung aktivieren…",
    "Could not create the profile.": "Das Profil konnte nicht erstellt werden.",
    "Created and switched to “{name}”.": "Erstellt und zu „{name}“ gewechselt.",
    "Deleted “{name}”.": "„{name}“ gelöscht.",
    "Untitled profile": "Unbenanntes Profil",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Das Offline-Profil „{name}“ dauerhaft löschen? Seine Wörter und Texte existieren nur auf diesem Gerät — es gibt keine Cloud-Kopie. Die Datenbank wird zuerst im Sicherungsordner archiviert, aber dies kann in der App nicht rückgängig gemacht werden.",
    "this profile": "dieses Profil",
    "Connect to the internet to merge this profile into your account.": "Mit dem Internet verbinden, um dieses Profil mit Ihrem Konto zusammenzuführen.",
    "Enable cloud sync for this profile": "Cloud-Synchronisierung für dieses Profil aktivieren",
    "Continue": "Fortfahren",
    "Upload words": "Wörter hochladen",
    "Upload texts": "Texte hochladen",
    "Upload & sync": "Hochladen & synchronisieren",
    "Could not upload this profile. Your data is unchanged.": "Dieses Profil konnte nicht hochgeladen werden. Ihre Daten sind unverändert.",
    "“{name}” is now synced to your account.": "„{name}“ ist jetzt mit Ihrem Konto synchronisiert.",
    "Everything in this profile is already in your account.": "Alles in diesem Profil befindet sich bereits in Ihrem Konto.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Melden Sie sich an oder erstellen Sie ein Konto, um „{name}“ zu sichern und geräteübergreifend zu synchronisieren. Die Wörter und Texte dieses Profils werden hochgeladen und es wird zu Ihrem synchronisierten Konto auf diesem Gerät. Eine Kopie wird zuerst im Sicherungsordner archiviert.",
    "Upload “{name}” to your account": "„{name}“ in Ihr Konto hochladen",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Ihr Profil wird zum synchronisierten Konto „{who}“ auf diesem Gerät und lädt Daten in die Cloud hoch.",
    "Merge “{name}” into your account": "„{name}“ mit Ihrem Konto zusammenführen",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Dieses Konto enthält bereits Daten auf diesem Gerät. Wörter und Texte Ihres Profils, die dort noch nicht vorhanden sind, werden hinzugefügt — nichts wird überschrieben. „{name}“ wird anschließend im Sicherungsordner archiviert und entfernt.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Dieses Profil enthält {items}, die nur auf diesem Gerät gespeichert sind. Aktivieren Sie die Cloud-Synchronisierung, um sie zu sichern und auf allen Ihren Geräten zu lernen.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Wählen Sie die hinzuzufügenden Elemente aus. Sie werden in Ihr Konto kopiert und in die Cloud hochgeladen. „{name}“ wird anschließend im Sicherungsordner archiviert und entfernt.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Ich stimme den <a href=\"{terms}\">Nutzungsbedingungen</a> und der <a href=\"{privacy}\">Datenschutzerklärung</a> zu.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Bitte akzeptieren Sie die Nutzungsbedingungen und die Datenschutzerklärung, um fortzufahren.",
    "Updated Terms & Privacy": "Aktualisierte Bedingungen & Datenschutz",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Wir haben unsere Nutzungsbedingungen und Datenschutzerklärung aktualisiert. Bitte überprüfen und akzeptieren Sie diese, um Ihr Konto weiterhin zu nutzen.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Ich stimme den aktualisierten <a href=\"{terms}\">Nutzungsbedingungen</a> und der <a href=\"{privacy}\">Datenschutzerklärung</a> zu.",
    "Sign out": "Abmelden",
    "I agree": "Ich stimme zu",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Datenschutzerklärung</a> · <a href=\"{terms}\">Bedingungen</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Indem Sie fortfahren, stimmen Sie den <a href=\"{terms}\">Nutzungsbedingungen</a> und der <a href=\"{privacy}\">Datenschutzerklärung</a> zu.",
    "Privacy Policy": "Datenschutzerklärung",
    "Terms": "Nutzungsbedingungen",
    "Website": "Webseite",
    "Contact": "Kontakt",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Karteikarten",
    "Practice your vocabulary": "Üben Sie Ihren Wortschatz",
    "Due cards": "Fällige Karten",
    "Current filter": "Aktueller Filter",
    "Newest": "Neueste",
    "Selected words": "Ausgewählte Wörter",
    "Deck size": "Deckgröße",
    "Default deck size": "Standard-Deckgröße",
    "Shuffle": "Mischen",
    "Start session": "Sitzung starten",
    "Play deck": "Deck abspielen",
    "{n} cards ready to review": "{n} Karte(n) bereit zur Wiederholung",
    "No cards due — great job!": "Keine Karten fällig — gute Arbeit!",
    "{n} selected words": "{n} ausgewählte Wörter",
    "No words to practice.": "Keine Wörter zum Üben vorhanden.",
    "End session": "Sitzung beenden",
    "Listening — pause to review manually":
        "Zuhören — pausieren, um manuell zu wiederholen",
    "Show answer": "Antwort anzeigen",
    "Hard": "Schwer",
    "Good": "Gut",
    "Easy": "Einfach",
    "Space or click to flip": "Leertaste oder Klick zum Umdrehen",
    "Card {current} of {total}": "Karte {current} von {total}",
    "{n} correct": "{n} richtig",
    "Session complete!": "Sitzung abgeschlossen!",
    "You listened to {n} of {total} cards.": "Sie haben sich {n} von {total} Karten angehört.",
    "Correct: {n} of {total}": "Richtig: {n} von {total}",
    "New session": "Neue Sitzung",
    "Practice hard words": "Schwierige Wörter üben",
    "Hard words": "Schwierige Wörter",
    "Hard words cleared!": "Schwierige Wörter gemeistert!",
    "Open Flashcards when Read Aloud starts":
        "Karteikarten öffnen, wenn das Vorlesen startet",
    "Stop": "Stopp",
    "Auto-pronounce": "Automatisch aussprechen",
    "Speak each card as it appears and when it flips":
        "Jede Karte vorlesen, wenn sie erscheint und wenn sie umgedreht wird",
    "Deck preview": "Deck-Vorschau",
    "{n} cards": "{n} Karten",
    "Due": "Fällig",
    "In {n} d": "In {n} T.",
    "{n} d": "{n} T.",
    "{n} mo": "{n} Monat(e)",
    "{n} y": "{n} J.",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez für Android…",
    "Android app": "Android-App",
    "Lingueez on Android": "Lingueez auf Android",
    "Take your vocabulary with you": "Nehmen Sie Ihren Wortschatz mit",
    "Preview of Lingueez on a phone": "Vorschau von Lingueez auf einem Smartphone",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Melden Sie sich mit Ihrem Lingueez-Konto an und Ihr Wortschatz ist bereits da — "
        "nichts einzurichten, nichts zu übertragen.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Melden Sie sich auf beiden Geräten mit einem kostenlosen Lingueez-Konto an und Ihr Wortschatz "
        "synchronisiert sich mit dem Smartphone — keine Dateien zum manuellen Kopieren.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Melden Sie sich mit einem kostenlosen Lingueez-Konto an und Ihre Wörter werden mit Ihrem Smartphone synchronisiert.",
    "Synced both ways": "In beide Richtungen synchronisiert",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Wörter, die Sie auf dem Smartphone hinzufügen, warten auf dem Computer — und "
        "umgekehrt.",
    "Listen with the screen off": "Bei ausgeschaltetem Bildschirm zuhören",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Sperrbildschirm-Steuerung, damit die Wiederholung weiterläuft, während das Smartphone "
        "in Ihrer Tasche ist.",
    "Save a word from any app": "Ein Wort aus einer beliebigen App speichern",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Teilen Sie Text mit Lingueez und er landet in Ihrem Wortschatz, bereit, um "
        "später vervollständigt zu werden.",
    "Point your phone's camera at the code":
        "Richten Sie die Kamera Ihres Smartphones auf den Code",
    "Get it on Google Play": "Bei Google Play erhältlich",
    "Copy link": "Link kopieren",
    "Link copied": "Link kopiert",
    "Lingueez is now on Android": "Lingueez gibt es jetzt auch für Android",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Melden Sie sich mit Ihrem Lingueez-Konto an — Ihr Wortschatz ist bereits da.",
    "Dismiss": "Schließen",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Nutzen Sie Ihr Lingueez-Konto nahtlos auf Desktop- und Android-Geräten.",
    "Get the app…": "App herunterladen…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Quiz",
    "Quiz (recall practice)": "Quiz (Abfrage aus dem Gedächtnis)",
    "Recall your words, one question at a time":
        "Rufen Sie Ihre Wörter ab, Frage für Frage",
    "Questions": "Fragen",
    "Answer with": "Antworten mit",
    "Choices": "Auswahl",
    "Typing": "Eingabe",
    "Ask": "Abfragen",
    "Term": "Begriff",
    "Mixed": "Gemischt",
    "Auto-advance": "Automatisch weiter",
    "Move on by itself after a correct answer":
        "Nach einer richtigen Antwort von selbst weitergehen",
    "Speak the question, then the answer once it is revealed":
        "Die Frage vorlesen und die Antwort, sobald sie aufgedeckt ist",
    "Start quiz": "Quiz starten",
    "questions ready": "Fragen bereit",
    "Nothing to quiz": "Nichts zum Abfragen",
    "No words match this deck.": "Keine Wörter passen zu diesem Stapel.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Ein Quiz braucht mindestens zwei Wörter — die falschen Antworten stammen aus "
        "genau den Wörtern, nach denen gerade nicht gefragt wird.",
    "Not enough words": "Nicht genügend Wörter",
    "Add a few more words, or widen the deck.":
        "Fügen Sie ein paar Wörter hinzu oder erweitern Sie den Stapel.",
    "Question {n} of {total}": "Frage {n} von {total}",
    "Missed words": "Falsch beantwortet",
    "End quiz": "Quiz beenden",
    "Answer in {language}": "Antwort auf {language}",
    "Type the answer": "Antwort eingeben",
    "Check": "Prüfen",
    "Click to continue": "Zum Fortfahren klicken",
    "See results": "Ergebnisse",
    "Almost — it is \"{answer}\"": "Fast — es heißt „{answer}“",
    "It is \"{answer}\"": "Es heißt „{answer}“",
    "Now {status}": "Jetzt {status}",
    "Correct": "Richtig",
    "Missed": "Falsch",
    "Worth another look": "Noch einmal ansehen",
    "Again": "Nochmal",
    "Missed words cleared!": "Alle Fehler ausgeräumt!",
    "Perfect run": "Fehlerfreier Durchgang",
    "Quiz complete": "Quiz abgeschlossen",
    "Practice missed": "Fehler üben",
    "Default number of questions": "Standardanzahl der Fragen",
    "Move on after a correct answer": "Nach einer richtigen Antwort weitergehen",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Wählen Sie, wonach gefragt wird",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Dieselben Stapel wie bei den Karteikarten — fällige Wörter, Ihr aktueller "
        "Filter, die neuesten oder eine eigene Auswahl — und wie viele Fragen.",
    "Choices or typing": "Auswahl oder Eingabe",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "„Auswahl“ bietet vier Möglichkeiten an; „Eingabe“ verlangt, die Antwort zu "
        "schreiben — schwerer, aber die bessere Prüfung. Die Eingabe verzeiht Akzente "
        "und kleine Tippfehler. „Abfragen“ bestimmt, welche Seite Sie sehen: den "
        "Begriff, die Übersetzung oder gemischt.",
    "Start, and it counts": "Starten — und es zählt",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "Der Balken zeigt, woraus der Stapel nach Status besteht. Jede Antwort fließt "
        "in denselben Wiederholungsplan wie bei den Karteikarten: ein Wort, das Sie "
        "können, kommt später wieder — eines mit Fehler früher.",
}

# Date names, read by app.i18n. Months are in standard nominative/genitive German format.
# Weekdays start on Monday (datetime.weekday(): 0 = Monday).
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]
MONTHS_ABBR = ["Jan.", "Feb.", "März", "Apr.", "Mai", "Juni",
               "Juli", "Aug.", "Sept.", "Okt.", "Nov.", "Dez."]
WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
            "Freitag", "Samstag", "Sonntag"]
WEEKDAYS_ABBR = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]