# Lingueez — Finnish (fi) translations.
# Keys are English UI strings; values are their Finnish equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Suomi"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Peruuta",
    "OK": "OK",
    "Close": "Sulje",
    "Save": "Tallenna",
    "Delete": "Poista",
    "Edit": "Muokkaa",
    "Remove": "Poista",
    "Add": "Lisää",
    "Refresh": "Päivitä",
    "Import": "Tuo",
    "Export": "Vie",
    "Search": "Hae",
    "Fetch": "Hae tiedot",
    "Browse…": "Selaa…",
    "Clear": "Tyhjennä",
    "Pause": "Tauko",
    "Resume": "Jatka",
    "Language": "Kieli",
    "Translation": "Käännös",
    "Word": "Sana",
    "Status": "Tila",
    "Error": "Virhe",
    "Title": "Otsikko",
    "Topic": "Aihe",
    "Level": "Taso",
    "Generate": "Luo",
    "Generating…": "Luodaan…",
    "Translating…": "Käännetään…",
    "Format": "Muoto",
    "Style": "Tyyli",
    "Model": "Malli",
    "Font": "Fontti",
    "Usage": "Käyttö",
    "Translation language": "Käännöskieli",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Valikko",
    "Open Excel Table…": "Avaa Excel-taulukko…",
    "Import Excel to Database…": "Tuo Excel tietokantaan…",
    "Save Import Template…": "Tallenna tuontimalli…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Ääni (MP3)…",
    "Backups…": "Varmuuskopiot…",
    "Show Source column": "Näytä Lähde-sarake",
    "Show Created At column": "Näytä Luontipäivämäärä-sarake",
    "Max words…": "Sanojen enimmäismäärä…",
    "View Log": "Näytä loki",
    "About": "Tietoa ohjelmasta",
    "Quit": "Lopeta",
    "Words": "Sanat",
    "Texts": "Tekstit",
    "Statistics": "Tilastot",
    "Bin (deleted items)": "Roskakori (poistetut kohteet)",
    "Settings": "Asetukset",
    "Vocabulary": "Sanasto",
    "Search words, translations or tags…": "Hae sanoja, käännöksiä tai tunnisteita…",
    "Search texts by title, content or words…": "Hae tekstejä otsikon, sisällön tai sanojen mukaan…",
    "Search scope": "Hakualue",
    "Search scope…": "Hakualue…",
    "Nothing to practice yet": "Ei vielä harjoiteltavaa",
    "Add words to your vocabulary and they show up here.":
        "Lisää sanoja sanastoosi, niin ne ilmestyvät tähän.",
    "Come back when cards are due, or practice the newest words now.":
        "Palaa, kun kortteja on kerrattavana, tai harjoittele nyt uusimpia sanoja.",
    "Practice newest words": "Harjoittele uusimpia sanoja",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Valitse yllä toinen pakka tai muuta suodattimia Sanat-sivulla.",
    "You're all caught up": "Olet ajan tasalla",
    "Add word": "Lisää sana",
    "Copy a word in any app, then press:":
        "Kopioi sana missä tahansa sovelluksessa ja paina:",
    "Set a shortcut": "Aseta pikanäppäin",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Kopioi sana missä tahansa sovelluksessa ja lisää se käännöksineen painamalla {keys}.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Aseta pikanäppäin Asetuksissa, niin voit lisätä kopioituja sanoja mistä tahansa sovelluksesta.",
    " Favorites": " Suosikit",
    " Filters": " Suodattimet",
    "Filters that don't fit the table": "Suodattimet, jotka eivät mahdu taulukkoon",
    "More actions": "Lisää toimintoja",
    "Filter by tag": "Suodata tunnisteella",
    "Close file and return to your vocabulary": "Sulje tiedosto ja palaa sanastoon",
    "Definition": "Määritelmä",
    "Read": "Lue",
    "Favorite": "Suosikki",
    "Tags": "Tunnisteet",
    "Copy": "Kopioi",
    "Text": "Teksti",
    "Delete selected (Del)": "Poista valitut (Del)",
    "No data": "Ei tietoja",
    "No texts yet": "Ei vielä tekstejä",
    "Words: {shown}/{total}": "Sanat: {shown}/{total}",
    "Texts: {total}": "Tekstit: {total}",
    "Texts: {shown}/{total}": "Tekstit: {shown}/{total}",
    "{count} selected": "{count} valittu",
    "No selection": "Ei valintaa",
    "Please select at least one word.": "Valitse vähintään yksi sana.",
    "Saved": "Tallennettu",
    "'{word}' updated.": "’{word}’ päivitetty.",
    "Database Error": "Tietokantavirhe",
    "Delete {count} word(s)?": "Poistetaanko {count} sana(a)?",
    "Deleted": "Poistettu",
    "{count} word(s) deleted.": "{count} sana(a) poistettu.",
    "Deleted with {n} error(s).": "Poistettu ({n} virhe(ttä)).",
    "Favorites": "Suosikit",
    "{count} word(s) added to favorites.": "{count} sana(a) lisätty suosikkeihin.",
    "{count} word(s) removed from favorites.": "{count} sana(a) poistettu suosikeista.",
    "Status set to '{status}' for {count} word(s).": "Tilaksi asetettu '{status}' {count} sanalle.",
    "Max Words": "Sanojen enimmäismäärä",
    "Show only the first N words (0 = show all):": "Näytä vain ensimmäiset N sanaa (0 = näytä kaikki):",
    "View Definition": "Näytä määritelmä",
    "Copy Word": "Kopioi sana",
    "Copy Translation": "Kopioi käännös",
    "Toggle Favorite": "Vaihda suosikkitilaa",
    "Change Status…": "Muuta tilaa…",
    "Add / Remove Tags…": "Lisää / poista tunnisteita…",
    "Read Aloud": "Lue ääneen",
    "Change Status": "Muuta tilaa",
    "New status:": "Uusi tila:",
    "Copied": "Kopioitu",
    "{count} row(s) copied to clipboard.": "{count} riviä kopioitu leikepöydälle.",
    "{count} item(s) copied to clipboard.": "{count} kohdetta kopioitu leikepöydälle.",
    "Copy Word(s)": "Kopioi sana(t)",
    "Copy Translation(s)": "Kopioi käännös (käännökset)",
    "Copy Both": "Kopioi molemmat",
    "Search in Word": "Hae sanasta",
    "Search in Translation": "Hae käännöksestä",
    "Search in Tags": "Hae tunnisteista",
    "Promoted": "Ylennetty",
    "Google Cloud TTS unavailable": "Google Cloud TTS ei ole käytettävissä",
    "Selection limit": "Valintaraja",
    "Only the first 200 selected words will be read.": "Vain ensimmäiset 200 valittua sanaa luetaan.",
    "Only the first 50 words will be used.": "Vain ensimmäisiä 50 sanaa käytetään.",
    "Select words to save as audio.": "Valitse sanat, jotka tallennetaan äänitiedostona.",
    "Nothing to export.": "Ei vietävää sisältöä.",
    "Export Error": "Vientivirhe",
    "Settings saved.": "Asetukset tallennettu.",
    "Generated text saved.": "Luotu teksti tallennettu.",
    "Show": "Näytä",
    "Add Word": "Lisää sana",
    "Stop reading": "Lopeta lukeminen",
    "Read — Read selected words aloud": "Lue — Lue valitut sanat ääneen",
    "Translation": "Käännös",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Ulkoasu",
    "Audio": "Ääni",
    "Learning": "Opitaan",
    "Listening": "Kuuntelu",
    "Backups": "Varmuuskopiot",
    "Sync your library?": "Synkronoidaanko kirjastosi?",
    "This will reconcile your device with the cloud:": "Tämä sovittaa laitteesi tiedot pilvipalvelun kanssa:",
    "Sync now": "Synkronoi nyt",
    "Upload": "Lataa palvelimelle",
    "Synced — ↑{up} ↓{down}": "Synkronoitu — ↑{up} ↓{down}",
    "Upload restored library?": "Ladataanko palautettu kirjasto palvelimelle?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Kirjasto palautettu. Sinua pyydetään lataamaan se palvelimelle, kun seuraavan kerran yhdistät synkronointipalvelimeen.",
    "Merging this restored backup with your cloud:": "Yhdistetään tämä palautettu varmuuskopio pilvipalveluusi:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Tässä varmuuskopiossa on {items}. Ladataanko ja yhdistetäänkö se pilveen nyt, vai pidetäänkö pilvi toistaiseksi ennallaan?",
    "General": "Yleiset",
    "Read-aloud": "Ääneenluku",
    "Translation & AI": "Käännös ja tekoäly",
    "Data": "Data",
    "Behavior": "Toiminta",
    "Progress": "Edistyminen",
    "DeepL request failed — using free Google Translate instead.": "DeepL-pyyntö epäonnistui — käytetään sen sijaan ilmaista Google Kääntäjää.",
    "DeepL key isn't set — using free Google Translate instead.": "DeepL-avainta ei ole asetettu — käytetään sen sijaan ilmaista Google Kääntäjää.",
    "System": "Järjestelmä",
    "Light": "Vaalea",
    "Dark": "Tummia",
    "Appearance mode": "Ulkoasutila",
    "Widget scaling": "Käyttöliittymän skaalaus",
    "Table size": "Taulukon koko",
    "Interface language": "Käyttöliittymän kieli",
    "Restart the app to apply the language change.": "Käynnistä sovellus uudelleen ottaaksesi kielimuutoksen käyttöön.",
    "The interface language has changed. Restart now to apply it?": "Käyttöliittymän kieli on muuttunut. Käynnistetäänkö uudelleen nyt?",
    "TTS provider": "TTS-tarjoaja",
    "Google Cloud credentials": "Google Cloud -tunnistetiedot",
    "Voice type": "Äänityyppi",
    "Voice name (optional)": "Äänen nimi (valinnainen)",
    "Read Aloud playback": "Ääneenluvun toisto",
    "Pause between words (s)": "Tauko sanojen välillä (s)",
    "Repeats per word": "Toistoja per sana",
    "Repeats per pair": "Toistoja per pari",
    "Promote status while listening": "Edistä tilaa kuunneltaessa",
    "Listens to reach {status}": "Kuuntelukertoja tilan '{status}' saavuttamiseen",
    "Excel import": "Excel-tuonti",
    "Placeholder values": "Asetteluarvot",
    "Skip placeholder rows": "Ohita asettelurivit",
    "Skip empty rows": "Ohita tyhjät rivit",
    "Normalize language pairs": "Normalisoi kieliparit",
    "How to import": "Kuinka tuoda",
    "Save import template…": "Tallenna tuontimalli…",
    "Active provider": "Aktiivinen tarjoaja",
    "API key": "API-avain",
    "API URL": "API URL",
    "Check usage": "Tarkista käyttö",
    "Enable cloud sync": "Ota pilvisynkronointi käyttöön",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase-avain (.env)",
    "Bin cleanup grace (days)": "Roskakorin säilytysaika (päivää)",
    "Test Connection": "Testaa yhteyttä",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "Pilvisynkronointi käyttää omaa Supabase-projektiasi. Luot tarvittavat taulukot kerran ja syötät sen jälkeen URL-osoitteen ja anon-avaimen yläpuolelle.",
    "Copy schema SQL": "Kopioi kaavion SQL",
    "Open SQL editor ↗": "Avaa SQL-editori ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "Kaavion SQL kopioitu leikepöydälle. Avaa Supabase-projektisi SQL-editori, liitä se ja paina Run luodaksesi taulukot.",
    "Server": "Palvelin",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Yhdistetty omaan Supabase-palvelimeesi — henkilökohtainen tila, tiliä ei tarvita.\n{host}",
    "Use your own Supabase server (personal)": "Käytä omaa Supabase-palvelintasi (henkilökohtainen)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Henkilökohtainen yhden käyttäjän synkronointi omaan Supabase-projektiisi. Ei tiliä tai kirjautumista — sovellus yhdistää projektin anon-avaimella. Suorita kaavion SQL projektissasi, liitä sen URL ja anon-avain alle ja valitse Testaa yhteyttä.\n\nHuomaa: kuka tahansa, jolla on tämä URL ja avain, voi lukea tiedot, joten pidä projekti yksityisenä äläkä jaa avainta.",
    "Disconnect — use the built-in server": "Katkaise yhteys — käytä sisäänrakennettua palvelinta",
    "Disconnect server": "Katkaise yhteys palvelimeen",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Lopetetaanko synkronointi oman Supabase-palvelimesi kanssa ja palataanko käyttämään sisäänrakennettua?\n\nSanasi pysyvät omassa projektissasi ja tällä laitteella. Olet vain paikallisessa tilassa, kunnes kirjaudut tilille.",
    "Disconnected — using the built-in server.": "Yhteys katkaistu — käytetään sisäänrakennettua palvelinta.",
    "{host} (personal)": "{host} (henkilökohtainen)",
    "Personal": "Henkilökohtainen",
    "your server": "palvelimesi",
    "Account actions": "Tilin toiminnot",
    "Add account…": "Lisää tili…",
    "Sync this device's data to my account…": "Synkronoi tämän laitteen tiedot tililleni…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Tili",
    "Accounts": "Tilit",
    "No accounts yet. Add one to sync your words across devices.": "Ei tilejä vielä. Lisää tili synkronoidaksesi sanasi laitteiden välillä.",
    "(active)": "(aktiivinen)",
    "Sign in": "Kirjaudu sisään",
    "(sign in again)": "(kirjaudu uudelleen)",
    "Switch": "Vaihda",
    "Remove account": "Poista tili",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Poistetaanko {email} tältä laitteelta? Voit lisätä sen uudelleen milloin tahansa — sanasi pysyvät pilvessä ja paikallinen kopio levyllä. Pilvitietojasi ei poisteta.",
    "Removed {email} from this device.": "Poistettu {email} tältä laitteelta.",
    "Your data was exported.": "Tietosi vietiin.",
    "Export failed.": "Vienti epäonnistui.",
    "Delete account": "Poista tili",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Tämä poistaa tilisi ja KAIKKI synkronoidut sanasi, tekstisi ja tunnisteesi pysyvästi pilvestä. Paikallinen kopio arkistoidaan varmuuskopiokansioon. Tätä ei voi peruuttaa.\n\nPoistetaanko tilisi?",
    "Account deleted.": "Tili poistettu.",
    "Could not delete the account.": "Tiliä ei voitu poistaa.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Nimi",
    "Enter your name.": "Syötä nimesi.",
    "Email": "Sähköposti",
    "Password": "Salasana",
    "New password": "Uusi salasana",
    "6-digit code": "6-numeroinen koodi",
    "or": "tai",
    "Sign in with Google": "Kirjaudu Google-tilillä",
    "Opening your browser to sign in with Google…": "Avataan selaintasi Google-kirjautumista varten…",
    "Forgot password?": "Unohtuiko salasana?",
    "Resend code": "Lähetä koodi uudelleen",
    "Confirm your email": "Vahvista sähköpostisi",
    "Verify code": "Vahvista koodi",
    "Use a different email": "Käytä toista sähköpostia",
    "Enter your email and password.": "Syötä sähköpostisi ja salasanasi.",
    "Enter the 6-digit code from the email.": "Syötä sähköpostissa saatu 6-numeroinen koodi.",
    "Enter the code and a new password.": "Syötä koodi ja uusi salasana.",
    "Enter your email above first.": "Syötä ensin sähköpostisi yläpuolelle.",
    "Enter the reset code we emailed you and a new password.": "Syötä sähköpostiisi lähetetty palautuskoodi ja uusi salasana.",
    "Enter the 6-digit code we emailed you.": "Syötä sähköpostiisi lähetetty 6-numeroinen koodi.",
    "Reset password": "Nollaa salasana",
    "Set new password": "Aseta uusi salasana",
    "Back to sign in": "Takaisin kirjautumiseen",
    "Sign-in failed.": "Kirjautuminen epäonnistui.",
    "Couldn't send the code.": "Koodia ei voitu lähettää.",
    "Done.": "Valmis.",
    "Failed.": "Epäonnistui.",
    "Create an account": "Luo tili",
    "Create account": "Luo tili",
    "I already have an account": "Minulla on jo tili",
    "Signed in as {email}": "Kirjautuneena käyttäjänä {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Synkronoi tämän laitteen tiedot tilillesi",
    "your account": "tilisi",
    "This device has {words} and {texts} not yet in {account}.": "Tällä laitteella on {words} ja {texts}, joita ei vielä ole tilillä {account}.",
    "This device has {words} not yet in {account}.": "Tällä laitteella on {words}, joita ei vielä ole tilillä {account}.",
    "This device has {texts} not yet in {account}.": "Tällä laitteella on {texts}, joita ei vielä ole tilillä {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Valitse lisättävät kohteet. Ne kopioidaan tilillesi ja ladataan pilveen, joten ne näkyvät muillakin laitteillasi. Kopio tällä laitteella säilytetään.",
    "Don't ask again for this account": "Älä kysy uudelleen tälle tilille",
    "{n} word": "{n} sana",
    "{n} words": "{n} sanaa",
    "{n} text": "{n} teksti",
    "{n} texts": "{n} tekstiä",
    "Add {n} item": "Lisää {n} kohde",
    "Add {n} items": "Lisää {n} kohdetta",
    # Finnish plural forms mapped to genitive slots
    "words (genitive)": "sanaa",
    "texts (genitive)": "tekstiä",
    "tags (genitive)": "tunnistetta",
    "changes (genitive)": "muutosta",
    "deletions (genitive)": "poistoa",
    "{n} words (genitive)": "{n} sanaa",
    "{n} texts (genitive)": "{n} tekstiä",
    "Add {n} items (genitive)": "Lisää {n} kohdetta",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "Lisätty {n} kohde tilillesi.",
    "Added {n} items to your account.": "Lisätty {n} kohdetta tilillesi.",
    "Added {n} items to your account. (genitive)": "Lisätty {n} kohdetta tilillesi.",
    "{n} couldn't be added.": "Kohdetta {n} ei voitu lisätä.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Istuntosi vanheni — kirjaudu uudelleen (Asetukset → Synkronointi)",
    "Sign in to sync (Settings → Sync)": "Kirjaudu sisään synkronoidaksesi (Asetukset → Synkronointi)",
    "Sign in again to sync": "Kirjaudu uudelleen synkronoidaksesi",
    "Sign in again to use this account.": "Kirjaudu uudelleen käyttääksesi tätä tiliä.",
    "Sync incomplete: {reason}": "Synkronointi keskeneräinen: {reason}",
    "Connect to the internet to add local items to your account.": "Yhdistä internetiin lisätäksesi paikallisia kohteita tilillesi.",
    "Everything on this device is already in your account.": "Kaikki tällä laitteella oleva on jo tililläsi.",
    "Upload local words?": "Ladataanko paikalliset sanat?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Ladataanko nykyiset paikalliset sanasi tälle tilille? Ne yhdistetään tilin pilvitietoihin ja synkronoidaan.\n\nValitse Ei säilyttääksesi tilin nykyiset tiedot ja siirtääksesi paikalliset sanat syrjään (arkistoidaan varmuuskopiokansioon).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Kirjautuminen epäonnistui. Tarkista sähköpostisi ja salasanasi.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Voit pitää enintään {max} tiliä tällä laitteella. Poista yksi lisätäksesi toisen.",
    "Wrong email or password.": "Väärä sähköposti tai salasana.",
    "That doesn't look like a valid email address.": "Sähköpostiosoite ei vaikuta kelvolliselta.",
    "Confirm password": "Vahvista salasana",
    "Passwords don't match.": "Salasanat eivät täsmää.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Sähköpostiasi ei ole vielä vahvistettu. Syötä lähetetty 6-numeroinen koodi.",
    "That email is already registered. Try signing in instead.": "Tämä sähköposti on jo rekisteröity. Yritä kirjautua sisään.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Lähetimme sinulle 6-numeroisen koodin. Syötä se viimeistelläksesi rekisteröinnin.",
    "That code didn't work. Check it and try again.": "Koodi ei toiminut. Tarkista koodi ja yritä uudelleen.",
    "If that account exists, a 6-digit reset code is on its way.": "Jos tili on olemassa, 6-numeroinen palautuskoodi on matkalla.",
    "Confirmation email re-sent.": "Vahvistussähköposti lähetetty uudelleen.",
    "Too many attempts. Please wait a minute and try again.": "Liian monta yritystä. Odota minuutti ja yritä uudelleen.",
    "Your password is too short — use at least 6 characters.": "Salasanasi on liian lyhyt — käytä vähintään 6 merkkiä.",
    "Sign-ups are disabled on this server.": "Rekisteröityminen on poistettu käytöstä tällä palvelimella.",
    "Can't reach the server. Check your internet connection.": "Palvelimeen ei saada yhteyttä. Tarkista internet-yhteytesi.",
    "Something went wrong.": "Jotain meni pieleen.",
    "Your saved sign-in for this account expired. Sign in again.": "Tallennettu kirjautumisesi vanheni. Kirjaudu uudelleen.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "Pilvisynkronointia ei ole vielä määritetty. Lisää Supabase URL ja -avain kohdassa Asetukset → Synkronointi.",
    "Could not start Google sign-in.": "Google-kirjautumista ei voitu käynnistää.",
    "Google sign-in was cancelled or timed out.": "Google-kirjautuminen peruutettiin tai se aikakatkaistiin.",
    "Google sign-in failed.": "Google-kirjautuminen epäonnistui.",
    "Google sign-in failed: {error}": "Google-kirjautuminen epäonnistui: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Paikallista kirjautumisapuria ei voitu käynnistää portissa {port} ({error}). Sulje sitä käyttävä sovellus ja yritä uudelleen.",
    "Export my data…": "Vie tietoni…",
    "Delete account…": "Poista tili…",
    "Cloud sync is on — your own server ({host})": "Pilvisynkronointi on käytössä — oma palvelin ({host})",
    "Cloud sync is on — signed in as {who}": "Pilvisynkronointi on käytössä — kirjautuneena käyttäjänä {who}",
    "Cloud sync is off — your words are saved on this device only": "Pilvisynkronointi ei ole käytössä — sanasi tallennetaan vain tälle laitteelle",
    "(checking…)": "(tarkistetaan…)",
    "(can't connect)": "(ei yhteyttä)",
    "Turn off cloud sync": "Ota pilvisynkronointi pois käytöstä",
    "Cloud sync turned off — this device only.": "Pilvisynkronointi poistettu käytöstä — vain tämä laite.",
    "Use this server": "Käytä tätä palvelinta",
    "Connecting…": "Yhdistetään…",
    "Testing…": "Testataan…",
    "Applying theme…": "Toteutetaan teemaa…",
    "Now syncing with your own server.": "Synkronoidaan nyt oman palvelimesi kanssa.",
    "Could not connect to this server:\n{error}": "Tähän palvelimeen ei saatu yhteyttä:\n{error}",
    "Could not connect to this server.": "Tähän palvelimeen ei saatu yhteyttä.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nTarkista URL ja anon-avain sekä se, että olet suorittanut kaavion SQL:n. Käytetäänkö näitä tietoja silti?",
    "Enter your server's URL and anon key first, then test.": "Syötä ensin palvelimesi URL ja anon-avain, ja testaa sitten.",
    "Enter your server's URL and anon key first.": "Syötä ensin palvelimesi URL ja anon-avain.",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase-avain (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Henkilökohtainen yhden käyttäjän synkronointi omaan Supabase-projektiisi. Ei tiliä tai kirjautumista — sovellus yhdistää projektin anon-avaimella. Suorita kaavion SQL projektissasi, liitä sen URL ja anon-avain alle, testaa ja paina sitten ”Käytä tätä palvelinta”.\n\nHuomaa: kuka tahansa, jolla on tämä URL ja avain, voi lukea tiedot, joten pidä projekti yksityisenä äläkä jaa avainta.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Lopetetaanko synkronointi oman Supabase-palvelimesi kanssa ja palataanko käyttämään sisäänrakennettua?\n\nSanasi pysyvät omassa projektissasi ja tällä laitteella. Palvelimen tiedot muistetaan, joten voit palata milloin tahansa. Olet paikallisessa tilassa, kunnes kirjaudut tilille.",
    "Start automatically on login (minimized to tray)": "Käynnistä automaattisesti kirjautuessa (pienennettynä ilmaisalueelle)",
    "Add Word hotkey (global)": "Lisää sana -pikanäppäin (globaali)",
    "Data format": "Datamuoto",
    "Columns to export": "Vietävät sarakkeet",
    "Sheet name": "Taulukon nimi",
    "Start row": "Aloitusrivi",
    "Start column": "Aloitussarake",
    "Shade alternate rows": "Raitoitettu taulukko",
    "Auto column width": "Automaattinen sarakkeen leveys",
    "Freeze header row": "Kiinnitä otsikkorivi",
    "Delimiter": "Erotin",
    "Delimiter (\\t = tab)": "Erotin (\\t = sarkain)",
    "Include header lines": "Sisällytä otsikkorivit",
    "Header lines": "Otsikkorivit",
    "Page size": "Sivukoko",
    "Font size": "Fonttikoko",
    "Line spacing (pt)": "Riviväli (pt)",
    "Text alignment": "Tekstin tasaus",
    "Margins L/R/T/B (pt)": "Reunukset V/O/Y/A (pt)",
    "Automatic widths (fit page)": "Automaattiset leveydet (sovita sivulle)",
    "Columns / width": "Sarakkeet / leveys",
    "Header background": "Otsikon tausta",
    "Header text": "Otsikon teksti",
    "Row background": "Rivin tausta",
    "Grid lines": "Ruudukkoviivat",
    "Background image": "Taustakuva",
    "Concurrent workers": "Rinnakkaiset prosessit",
    "Requests per second": "Pyyntöjä sekunnissa",
    "Add font…": "Lisää fontti…",
    "Page && text": "Sivu && teksti",
    "Columns": "Sarakkeet",
    "Max tokens": "Tokenien enimmäismäärä",
    "Temperature": "Lämpötila (Temperature)",
    "Prompt template": "Kehetepohja",
    "Definitions": "Määritelmät",
    "Generated Texts (from words)": "Luodut tekstit (sanoista)",
    "Generated Texts (by topic)": "Luodut tekstit (aiheen mukaan)",
    "Text Adaptation (to level)": "Tekstin mukauttaminen (tasoon)",
    "Thinking budget (0 = off, -1 = auto)": "Päättelybudjetti (0 = pois, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Tunnista kieli",
    "Type a word or phrase…": "Kirjoita sana tai fraasi…",
    "Translation…": "Käännös…",
    "Pronounce": "Lausu",
    "Swap word and translation": "Vaihda sanan ja käännöksen paikkaa",
    "Translate with DeepL (Enter)": "Käännä DeepL-palvelulla (Enter)",
    "Save Word": "Tallenna sana",
    "Enter a word to translate.": "Syötä käännettävä sana.",
    "Fill with AI (lemma + best translation)": "Täytä tekoälyllä (perusmuoto + paras käännös)",
    "Enter a word to fill with AI.": "Syötä sana täytettäväksi tekoälyllä.",
    "Source equals target — translated to {lang} instead.": "Lähdekieli on sama kuin kohdekieli — käännetty kielelle {lang}.",
    "Both word and translation are required.": "Sekä sana että käännös vaaditaan.",
    "Please select the source language before saving.": "Valitse lähdekieli ennen tallentamista.",
    "'{word}' already exists in your dictionary.": "’{word}’ on jo sanakirjassasi.",
    "'{word}' is already in your dictionary.": "’{word}’ on jo sanakirjassasi.",
    "Already in your dictionary": "Jo sanakirjassasi",
    "Show existing": "Näytä olemassa oleva",
    "The text was truncated to the first 100 words.": "Teksti katkaistiin ensimmäiseen 100 sanaan.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Luo tekoälyllä",
    "Regenerate with AI": "Luo uudelleen tekoälyllä",
    "Definition 2": "Määritelmä 2",
    "No definition yet": "Ei vielä määritelmää",
    "Generate one with AI, or write your own with Edit.": "Luo määritelmä tekoälyllä tai kirjoita oma Muokkaa-painikkeella.",
    "There is no word to define.": "Ei määriteltävää sanaa.",
    "Bold": "Lihavoitu",
    "Italic": "Kursivoitu",
    "Heading": "Otsikko",
    "List": "Luettelo",
    "API key missing": "API-avain puuttuu",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Aseta ensin palvelun {ai} API-avain kohdassa Asetukset → Käännös ja tekoäly → AI.",
    "Generating definition…": "Luodaan määritelmää…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Tunnisteet — {count} sana(a)",
    "New tag name…": "Uusi tunnisteen nimi…",
    "Add Tag": "Lisää tunniste",
    "Apply Selected to All": "Käytä valittuja kaikkiin",
    "Remove Selected": "Poista valitut",
    "(partial)": "(osittainen)",
    "use(s)": "käyttöä",
    "Tags marked ✓ apply to all selected words.": (
        "Merkin ✓ saaneet tunnisteet koskevat kaikkia valittuja sanoja."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (osittainen) tarkoittaa, että vain osalla sanoista on tämä tunniste."
    ),
    "Select tag(s) in the list first.": "Valitse ensin tunniste(et) luettelosta.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Roskakori — Poistetut kohteet",
    "Delete Permanently": "Poista Pysyvästi",
    "Cleanup Old Items…": "Puhdista vanhat kohteet…",
    "{n} selected": "{n} valittu",
    "The bin is empty. Deleted words will appear here.":
        "Roskakori on tyhjä. Poistetut sanat ilmestyvät tänne.",
    "The bin is empty. Deleted texts will appear here.":
        "Roskakori on tyhjä. Poistetut tekstit ilmestyvät tänne.",
    "deleted {when}": "poistettu {when}",
    "(empty)": "(tyhjä)",
    "Untitled": "Nimetön",
    "Auto-deletes soon": "Poistetaan automaattisesti pian",
    "Auto-deletes in {n} day": "Poistetaan automaattisesti {n} päivän kuluttua",
    "Auto-deletes in {n} days": "Poistetaan automaattisesti {n} päivän kuluttua",
    "Auto-deletes in {n} days (genitive)": "Poistetaan automaattisesti {n} päivän kuluttua",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Poistetaanko {count} kohdetta pysyvästi? Tätä ei voi peruuttaa.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Palauta aiempi versio",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Tietokannastasi otetaan automaattisesti varmuuskopio jokaisen muutoksen jälkeen. "
        "Valitse alta aiempi versio palautettavaksi."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Ei vielä tallennettuja versioita. "
        "Varmuuskopio luodaan automaattisesti jokaisen muutoksen jälkeen."
    ),
    "Restore this version": "Palauta tämä versio",
    "Today": "Tänään",
    "Yesterday": "Eilen",
    "Most recent": "Viimeisin",
    "Before your last restore": "Ennen viimeisintä palautusta",
    "today": "tänään",
    "yesterday": "eilen",
    "today {time}": "tänään {time}",
    "yesterday {time}": "eilen {time}",
    "the version from {date}": "versio päivämäärältä {date}",
    "the version from just before your last restore": "versio juuri ennen viimeisintä palautusta",
    "Restore Version": "Palauta versio",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Palautetaanko {phrase}?\n\nNykyiset tietosi tallennetaan ensin, joten voit peruuttaa tämän."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Tietokantasi on palautettu versioon {phrase}.\n\n"
        "Muutitko mieltäsi? Peruuta palauttamalla \"{before}\"."
    ),
    "Restore Error": "Palautusvirhe",
    "Sorry, that version could not be restored:\n{error}": "Tätä versiota ei voitu palauttaa:\n{error}",
    "Remove Version": "Poista versio",
    "Remove {phrase}?": "Poistetaanko {phrase}?",
    "Remove Error": "Poistovirhe",
    "Sorry, that version could not be removed:\n{error}": "Tätä versiota ei voitu poistaa:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Luo teksti",
    "Title…": "Otsikko…",
    "Generated text appears here…": "Luotu teksti ilmestyy tähän…",
    "Save to Texts": "Tallenna teksteihin",
    "Save failed": "Tallennus epäonnistui",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Tallenna äänitiedostona",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Luo yksi MP3-tiedosto {count} sana-/käännösparista."
    ),
    "Generating audio…": "Luodaan ääntä…",
    "Compiling final audio file…": "Kootaan lopullista äänitiedostoa…",
    "Processed: {word}": "Käsitelty: {word}",
    "Choose File && Start": "Valitse tiedosto && Aloita",
    "Cancelled.": "Peruutettu.",
    "Audio saved": "Ääni tallennettu",
    "Audio file saved to:\n{path}": "Äänitiedosto tallennettu kohteeseen:\n{path}",
    "Audio Error": "Äänivirhe",
    "Failed to save audio:\n{error}": "Äänen tallennus epäonnistui:\n{error}",
    "Cancelling…": "Peruutetaan…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Tuo Excelistä",
    "Row": "Rivi",
    "Word 1": "Sana 1",
    "Language 1": "Kieli 1",
    "Word 2": "Sana 2",
    "Language 2": "Kieli 2",
    "Action": "Toiminto",
    "Details": "Tiedot",
    "Add": "Lisää",
    "Update": "Päivitä",
    "Skip": "Ohita",
    "All": "Kaikki",
    "To add": "Lisättävät",
    "To update": "Päivitettävät",
    "Skipped": "Ohitetut",
    "Unrecognized": "Tunnistamattomat",
    "Only recognized languages": "Vain tunnistetut kielet",
    "Exclude rows whose language wasn't recognized.":
        "Jätä pois rivit, joiden kieltä ei tunnistettu.",
    "Unrecognized language — will be imported exactly as written.":
        "Tunnistamaton kieli — tuodaan täsmälleen kirjoitetussa muodossa.",
    "Select all": "Valitse kaikki",
    "Activity log": "Toimintaloki",
    "Export log…": "Vie loki…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Vie…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Lisää teksti",
    "Write": "Kirjoita",
    "AI Generate": "Luo tekoälyllä",
    "Wikipedia": "Wikipedia",
    "From URL": "URL-osoitteesta",
    "Language:": "Kieli:",
    "Level:": "Taso:",
    "Topic:": "Aihe:",
    "Topic…": "Aihe…",
    "Adapt to my level": "Mukauta tasolleni",
    "Load entries": "Lataa merkinnät",
    "Add feed…": "Lisää syöte…",
    "Ideas:": "Ideat:",
    "Short (~100 words)": "Lyhyt (~100 sanaa)",
    "Medium (~250 words)": "Keskipitkä (~250 sanaa)",
    "Long (~500 words)": "Pitkä (~500 sanaa)",
    "Travel": "Matkustus",
    "Food": "Ruoka",
    "Daily routine": "Päivittäiset rutiinit",
    "A short story": "Lyhyt tarina",
    "News": "Uutiset",
    "Dialogue at a café": "Keskustelu kahvilassa",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Kirjoita tai liitä tekstisi tähän, tai hae teksti yllä olevilla välilehdillä…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Uusimmat ensin",
    "Oldest first": "Vanhimmat ensin",
    "Title A–Z": "Otsikko A–Ö",
    "All languages": "Kaikki kielet",
    "All levels": "Kaikki tasot",
    "All topics": "Kaikki aihepiirit",
    "No matching texts": "Ei vastaavia tekstejä",
    "Try a different search or language filter.": "Kokeile toista hakua tai kielisuodatinta.",
    "New text (write or paste)": "Uusi teksti (kirjoita tai liitä)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Hae teksti internetistä (Tekoäly / Wikipedia / URL / RSS)"
    ),
    "Import .txt file(s)": "Tuo .txt-tiedosto(ja)",
    "Read aloud": "Lue ääneen",
    "Translate text": "Käännä teksti",
    "Hide translation": "Piilota käännös",
    "Focus mode": "Keskittymistila",
    "Exit focus mode": "Poistu keskittymistilasta",
    "Paper mode: off": "Paperitila: pois",
    "Paper: white (click for sepia)": "Paperi: valkoinen (napsauta vaihtaaksesi sepiaan)",
    "Paper: sepia (click to turn off)": "Paperi: sepia (napsauta poistaaksesi käytöstä)",
    "Save Changes": "Tallenna muutokset",
    "Previous text": "Edellinen teksti",
    "Next text": "Seuraava teksti",
    "From words: {words}": "Sanoista: {words}",
    "Created {date}": "Luotu {date}",
    "Unsaved changes": "Tallentamattomia muutoksia",
    "Save changes to '{title}'?": "Tallennetaanko muutokset tekstiin '{title}'?",
    "Changes saved.": "Muutokset tallennettu.",
    "'{title}' moved to bin.": "’{title}’ siirretty roskakoriin.",
    "Reader": "Lukija",
    'Pronounce "{word}"': 'Lausu "{word}"',
    'Add "{word}" to vocabulary': 'Lisää "{word}" sanastoon',
    "Read from here": "Lue tästä eteenpäin",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Lähde",
    "Added manually": "Lisätty käsin",
    "From reader": "Lukijasta",
    "Created at": "Luontiaika",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Lisää tekoälyllä (perusmuoto + paras käännös)",
    "Add to vocabulary as is": "Lisää sanastoon sellaisenaan",
    "Thinking…": "Mietitään…",
    "'{pair}' is already in your dictionary.": "’{pair}’ on jo sanakirjassasi.",
    "{label} — {translation} · added": "{label} — {translation} · lisätty",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Pilvisynkronointi",
    "Last sync": "Viimeisin synkronointi",
    "Pending": "Odottaa",
    "never": "ei koskaan",
    "just now": "juuri nyt",
    "{n} min ago": "{n} min sitten",
    "Connected": "Yhdistetty",
    "Not connected": "Ei yhteyttä",
    "change": "muutos",
    "changes": "muutosta",
    "deletion": "poisto",
    "deletions": "poistoa",
    "everything synced": "kaikki synkronoitu",
    "Initial sync has not completed yet.": "Ensisynkronointi ei ole vielä valmis.",
    "Sync Now": "Synkronoi nyt",
    "Syncing…": "Synkronoidaan…",
    # Local-only promo state
    "{words} and {texts}": "{words} ja {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Olet tallentanut tähän {items}. Kirjaudu sisään pitääksesi ne tallessa ja opiskellaksesi kaikilla laitteillasi.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Vain paikallinen — kirjaudu synkronoidaksesi sanasi laitteiden välillä",
    "Sign in to sync across devices": "Kirjaudu synkronoidaksesi laitteiden välillä",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Tervetuloa",
    "Welcome to {app}": "Tervetuloa sovellukseen {app}",
    "Sync across your devices": "Synkronoi laitteidesi välillä",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Kirjaudu sisään pitääksesi sanastosi tallessa ja opiskellaksesi sitä jokaisella laitteella.",
    "Automatic cloud backup": "Automaattinen pilvivarmuuskopiointi",
    "Your words follow you to every computer.":
        "Sanasi kulkevat mukanasi jokaiselle tietokoneelle.",
    "Never lose your progress.": "Älä koskaan menetä edistymistäsi.",
    "Study anywhere": "Opiskele missä vain",
    "Pick up right where you left off.":
        "Jatka täsmälleen siitä, mihin jäit.",
    "Your data is yours — sign in only to sync it.":
        "Tietosi ovat omiasi — kirjaudu sisään vain synkronoidaksesi ne.",
    "Sign in / Create account": "Kirjaudu sisään / Luo tili",
    "Continue on this device": "Jatka tällä laitteella",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Toistoasetukset",
    "Previous word": "Edellinen sana",
    "Next word": "Seuraava sana",
    "Stop playback": "Pysäytä toisto",
    "Pause between words": "Tauko sanojen välillä",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Ei mitään luettavaa.",
    "Previous sentence": "Edellinen lause",
    "Next sentence": "Seuraava lause",
    "Reading speed": "Lukunopeus",
    "Sentence {n} / {total}": "Lause {n} / {total}",
    "buffering…": "puskuroidaan…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Yleiskatsaus",
    "Learning status": "Oppimisen tila",
    "Activity": "Aktiivisuus",
    "Review activity": "Kertausaktiivisuus",
    "Breakdown": "Eritely",
    "Total words": "Sanoja yhteensä",
    "Mastered": "Hallitut",
    "In progress": "Kesken",
    "Languages": "Kielet",
    "Current streak": "Nykyinen putki",
    "Added this week": "Lisätty tällä viikolla",
    "Definitions written": "Kirjoitetut määritelmät",
    "Status distribution": "Tilojen jakautuma",
    "Words added over time": "Lisätyt sanat ajan myötä",
    "Activity calendar": "Aktiivisuuskalenteri",
    "Reviews over time": "Kertaukset ajan myötä",
    "Review calendar": "Kertauskalenteri",
    "Most reviewed words": "Eniten kertaatut sanat",
    "Top language pairs": "Suosituimmat kieliparit",
    "Top tags": "Suosituimmat tunnisteet",
    "Reviewed this week": "Kerrattu tällä viikolla",
    "Total reviews": "Kertauksia yhteensä",
    "Review streak": "Kertausputki",
    "{pct}% of all words": "{pct} % kaikista sanoista",
    "actively learning": "aktiivisessa opiskelussa",
    "{n} pairs": "{n} paria",
    "best {n}d": "paras {n} pv",
    "{n} today": "{n} tänään",
    "listens logged": "kuuntelukertaa kirjattu",
    "keep it going": "jatka samaan malliin!",
    "Day": "Päivä",
    "Week": "Viikko",
    "Month": "Kuukausi",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Tuo tekstitiedostoja",
    "Text files (*.txt);;All files (*)": "Tekstitiedostot (*.txt);;Kaikki tiedostot (*)",
    "Language of the imported text(s):": "Tuodun tekstin / tuotujen tekstien kieli:",
    "Imported {count} text(s).": "Tuotu {count} teksti(ä).",
    "Some files could not be imported:": "Joitakin tiedostoja ei voitu tuoda:",
    "Import failed:\n{error}": "Tuonti epäonnistui:\n{error}",
    "Failed to save text:\n{error}": "Tekstin tallennus epäonnistui:\n{error}",
    "Failed to delete text:\n{error}": "Tekstin poisto epäonnistui:\n{error}",
    "Delete Text": "Poista teksti",
    "Delete '{title}'?": "Poistetaanko '{title}'?",
    "Unsupported language: {language}": "Ei-tuettu kieli: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Ei-tuettu kieli: {lang}. Valitse kieli luettelosta.",
    "(empty)": "(tyhjä)",
    "unsupported language": "ei-tuettu kieli",
    "unreadable text": "lukukelvoton teksti",
    "Skipped {n} {noun} ({reasons}).": "Ohitettu {n} {noun} ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Jotain tekstiä ei voitu lukea ääneen — ei-tuettu kieli "
        "tai lukukelvottomia merkkejä.",
    "Edit text": "Muokkaa tekstiä",
    "Done editing": "Lopeta muokkaus",
    "Delete text": "Poista teksti",
    "Save Changes": "Tallenna muutokset",
    "Paper mode": "Paperitila",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Napsauta \"+\" kirjoittaaksesi tai liittääksesi tekstin, maapalloa hakeaksesi tekstin\n"
        "internetistä, tai valitse sanoja Sanat-näkymästä ja\n"
        "käytä \"Teksti\"-toimintoa opiskelutekstin luomiseen."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Hakee Wikipediasta valitulla kielellä. Napsauta tulosta ladataksesi artikkelin; käytä \"Mukauta tasolleni\" yksinkertaistaaksesi sitä."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Uutissyötteet valitulle kielelle. Lataa syöte ja kaksoisnapsauta merkintää hakeaksesi koko tekstin. Lisää omia syötteitä kohdasta \"Lisää syöte…\"."
    ),
    "Length:": "Pituus:",
    "Search Wikipedia (in the selected language)…": "Hae Wikipediasta (valitulla kielellä)…",
    "Double-click an entry to load its full text.": "Kaksoisnapsauta merkintää ladataksesi koko tekstin.",
    "Working…": "Käsitellään…",
    "Show the {count} result(s) again": "Näytä {count} tulos(ta) uudelleen",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "Palvelun {ai} API-avainta ei ole asetettu. Määritä se kohdassa Asetukset → Käännös ja tekoäly → AI."
    ),
    "Generating with {ai}…": "Luodaan tekoälyllä {ai}…",
    'Fetching "{title}"…': "Haetaan \"{title}\"…",
    "(yours)": "(sinun)",
    "Fetching the full text…": "Haetaan koko tekstiä…",
    "Add feed": "Lisää syöte",
    "Feed name:": "Syötteen nimi:",
    "Feed URL:": "Syötteen URL:",
    "Failed to save the text.": "Tekstin tallennus epäonnistui.",
    "Failed to save the text: {error}": "Tekstin tallennus epäonnistui: {error}",
    "'{title}' saved.": "’{title}’ tallennettu.",
    "(untitled)": "(nimetön)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Uudelleenkirjoita alla oleva teksti valitulle CEFR-tasolle tekoälyllä {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Vie loki",
    "Activity Log": "Toimintaloki",
    "Warnings & errors": "Varoitukset ja virheet",
    "Errors only": "Vain virheet",
    "Find…": "Etsi…",
    "Open log folder": "Avaa lokikansio",
    "Export diagnostics": "Vie diagnostiikka",
    "Clear the log file? This cannot be undone.":
        "Tyhjennetäänkö lokitiedosto? Tätä ei voi peruuttaa.",
    "Could not create the diagnostics file.":
        "Diagnostiikkatiedostoa ei voitu luoda.",
    "Diagnostics saved to:\n{path}": "Diagnostiikka tallennettu kohteeseen:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Kuvaile ongelma**\n\n\n**Toistovaiheet**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nLiitä diagnostiikkatiedosto:\n{path}\n",
    "Bug report: ": "Virheraportti: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Pienennä",
    "Maximize": "Suurenna",
    "Restore": "Palauta",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Näytä ohjaimet",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Ei väriä",
    "None": "Ei mitään",
    "Choose Color": "Valitse väri",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Pilvisynkronointi: toimeton",
    "Failed to open table:\n{error}": "Taulukon avaaminen epäonnistui:\n{error}",
    "Failed to save template:\n{error}": "Mallin tallentaminen epäonnistui:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Näytä / piilota",
    "Excel options": "Excel-asetukset",
    "CSV options": "CSV-asetukset",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Otsikkorivit kirjoitetaan tiedoston alkuun — tuontityökalut kuten "
        "Anki lukevat ne (esim. #separator:tab, #html:true). "
        "Itse sarakkeiden nimiä ei kirjoiteta."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Kopioi .ttf-tiedosto sovelluksen fonttikansioon ja käytä sitä"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Käytetään vain vietäessä sanoja MP3-tiedostoon. "
        "Itse ääni määritetään Ääni-välilehdellä."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "Ääni, jota käytetään kaikissa puheosioissa: sovelluksen ääneenluvussa "
        "ja MP3-viennissä. gTTS on ilmainen eikä vaadi määritystä. Google Cloud TTS "
        "tarvitsee palvelutilin JSON-avaimen (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) ja laskutuksen aktivoinnin projektille — "
        "käyttöä ilmaisen kuukausikiintiön puitteissa ei veloiteta."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Sanan kuunteleminen kokonaan ääneenluvussa edistää sitä tunnettuusasteikolla "
        "Uusi → Kerrattava → Opitaan → Hallittu. Kukin numero on vaadittujen kuuntelukertojen "
        "kokonaismäärä kyseisen tason saavuttamiseksi. Sanat, jotka asetat itse tilaan "
        "Hallittu tai Ohitettu, eivät koskaan muutu, eikä sanan tilaa lasketa alemmaksi."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Tallenna valmis .xlsx-tiedosto oikeilla otsikoilla ja esimerkkiriveillä"
    ),
    "Google Translate (free)": "Google Kääntäjä (ilmainen)",
    "Google Translate is free and needs no API key.": (
        "Google Kääntäjä on ilmainen eikä vaadi API-avainta."
    ),
    "Usage": "Käyttö",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Napsauta kenttää ja paina haluamaasi näppäinyhdistelmää — se avaa "
        "'Lisää sana' -ikkunan leikepöydän sisällöllä mistä tahansa. "
        "Jätä tyhjäksi poistaaksesi käytöstä."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Waylandissa tämä pikanäppäin rekisteröidään työpöytäympäristöösi "
        "ja se näkyy järjestelmän näppäimistöasetuksissa."
    ),
    "Add Word hotkey": "Lisää sana -pikanäppäin",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Globaali Lisää sana -pikanäppäin ei ole käytettävissä tässä "
        "ympäristössä. Katso vaihtoehdot kohdasta Asetukset ▸ Järjestelmä."
    ),
    "The global Add-Word hotkey isn't available in the "
    "Flatpak sandbox on Wayland.": (
        "Globaali Lisää sana -pikanäppäin ei ole käytettävissä "
        "Flatpak-hiekkalaatikossa Waylandissa."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Globaalia Lisää sana -pikanäppäintä ei tueta vielä tällä "
        "Wayland-työpöydällä."
    ),
    "To enable it, use any one of these:": "Ota se käyttöön käyttämällä jotakin näistä:",
    "Log in to an X11 session instead of Wayland":
        "kirjaudu X11-istuntoon Waylandin sijaan",
    "Use a GNOME session — the global hotkey works there":
        "käytä GNOME-istuntoa — globaali pikanäppäin toimii siellä",
    "Install the AppImage version — it runs outside the sandbox":
        "asenna AppImage-versio — se toimii hiekkalaatikon ulkopuolella",
    "Download the AppImage": "Lataa AppImage",
    "Add font…": "Lisää fontti…",
    "TrueType fonts (*.ttf)": "TrueType-fontit (*.ttf)",
    "Could not copy the font file:\n{error}": "Fonttitiedostoa ei voitu kopioida:\n{error}",
    "Save import template…": "Tallenna tuontimalli…",
    "Excel files (*.xlsx)": "Excel-tiedostot (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Malli tallennettu kohteeseen:\n{path}\n\n"
        "Täytä se sanoillasi (korvaa esimerkkirivit) "
        "ja tuo se sovellusvalikon kautta → Tuo Excel tietokantaan."
    ),
    "Could not save the template:\n{error}": "Mallia ei voitu tallentaa:\n{error}",
    "Background image": "Taustakuva",
    "Images (*.png *.jpg *.jpeg)": "Kuvat (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON-tiedostot (*.json)",
    "Connection successful! ✅": "Yhteys onnistui! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Yhteyttä ei voitu muodostaa. Tarkista URL/avain ja internet-yhteytesi."
    ),
    "Connection test failed:\n{error}": "Yhteystesti epäonnistui:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} merkkiä tällä jaksolla",
    "{count} characters used": "{count} merkkiä käytetty",
    "Autostart": "Automaattinen käynnistys",
    "Could not update autostart entry:\n{error}": "Automaattikäynnistyksen merkintää ei voitu päivittää:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS on valittu, mutta {problem}\n\n"
        "Ääni palautuu gTTS-palveluun, kunnes tämä korjataan."
    ),

    # ── Count nouns ───────────────────────────────────────────────────────
    "word": "sana",
    "words": "sanaa",
    "words (genitive)": "sanaa",
    "text": "teksti",
    "texts": "tekstiä",
    "texts (genitive)": "tekstiä",
    "tag": "tunniste",
    "tags": "tunnisteet",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Käännä",
    "AI": "AI",
    "Save As": "Tallenna nimellä",
    "Save Audio As": "Tallenna ääni nimellä",
    "Save PDF As": "Tallenna PDF nimellä",
    "Added": "Lisätty",
    "Updated": "Päivitetty",
    "Failed": "Epäonnistui",
    "Checking…": "Tarkistetaan…",
    "Cleanup": "Puhdistus",
    "Permanent Delete": "Pysyvä poisto",
    "No word": "Ei sanaa",
    "Category": "Luokka",
    "Bin": "Roskakori",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Kaikki tunnisteet",
    "Filter by tag — {tag}": "Suodata tunnisteella — {tag}",
    "(showing first {n})": "(näytetään ensimmäiset {n})",
    "Texts: {total}": "Tekstit: {total}",
    "Deleted with {n} error(s).": "Poistettu ({n} virhe(ttä)).",
    "Failed to update: {error}": "Päivitys epäonnistui: {error}",
    "Failed to export:\n{error}": "Vienti epäonnistui:\n{error}",
    "Failed to export PDF:\n{error}": "PDF-vienti epäonnistui:\n{error}",
    "Failed to export TXT:\n{error}": "TXT-vienti epäonnistui:\n{error}",
    "PDF saved to {path}": "PDF tallennettu kohteeseen {path}",
    "TXT file saved to {path}": "TXT-tiedosto tallennettu kohteeseen {path}",
    "Template saved to {path}": "Malli tallennettu kohteeseen {path}",
    "{format} file saved to {path}": "{format}-tiedosto tallennettu kohteeseen {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Käytetään sen sijaan gTTS-palvelua — {problem}\nKorjaa tämä kohdassa Asetukset → Ääneenluku → Ääni."
    ),
    "Failed to load the database:": "Tietokannan lataaminen epäonnistui:",
    "{selected} of {total} selected": "{selected} / {total} valittu",
    # Nav rail toggle tooltips
    "Collapse sidebar": "Pienennä sivupalkki",
    "Expand sidebar": "Laajenna sivupalkki",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Tallennettu {when} · {summary}",
    "the version from {date}": "versio päivämäärältä {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Sitä versiota ei valitettavasti voitu palauttaa:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Sitä versiota ei valitettavasti voitu poistaa:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Palautetaanko {count} kohdetta?",
    "Restored {count} item(s).": "{count} kohdetta palautettu.",
    "Select item(s) to restore.": "Valitse palautettavat kohteet.",
    "Permanently deleted {count} item(s).": "{count} kohdetta poistettu pysyvästi.",
    "Select item(s) to delete permanently.": "Valitse pysyvästi poistettavat kohteet.",
    "No items older than {n} days found.": "Yli {n} päivää vanhempia kohteita ei löytynyt.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Poistetaanko yli {days} päivää sitten poistetut kohteet pysyvästi?\n\n"
        "Tätä ei voi peruuttaa!"
    ),
    "Permanently deleted {count} old item(s).": "{count} vanhaa kohdetta poistettu pysyvästi.",
    "Failed to load deleted items:\n{error}": "Poistettujen kohteiden lataaminen epäonnistui:\n{error}",
    "Failed to count old items:\n{error}": "Vanhojen kohteiden laskeminen epäonnistui:\n{error}",
    "Failed to cleanup:\n{error}": "Puhdistus epäonnistui:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Tuo Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Odotetut sarakkeet: Language1, Language2, Word1, Word2 — nimettyinä otsikkorivillä "
        "tai ilman otsikoita, jolloin neljä ensimmäistä saraketta ovat tässä järjestyksessä. "
        "Valmis malli on saatavilla sovellusvalikosta → Tallenna tuontimalli."
    ),
    "All ({n})": "Kaikki ({n})",
    "To add ({n})": "Lisättävät ({n})",
    "To update ({n})": "Päivitettävät ({n})",
    "Skipped ({n})": "Ohitetut ({n})",
    "Unrecognized ({n})": "Tunnistamattomat ({n})",
    " · {n} with unrecognized language": " · {n} tunnistamattomalla kielellä",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} riviä: {add} uutta · {update} päivitystä · {skip} ohitettu"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Tarkista ehdotetut muutokset ja tuo sitten valitut rivit."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Ei tuotavaa — uusia tai muuttuneita merkintöjä ei löytynyt."
    ),
    "Analyzing file…": "Analysoidaan tiedostoa…",
    "Could not read the Excel file — see the activity log.": (
        "Excel-tiedostoa ei voitu lukea — katso toimintaloki."
    ),
    "Analysis failed — see the activity log.": "Analyysi epäonnistui — katso toimintaloki.",
    "Import failed": "Tuonti epäonnistui",
    "Import failed — see the activity log.": "Tuonti epäonnistui — katso toimintaloki.",
    "Importing…": "Tuodaan…",
    "Importing {count} item(s)…": "Tuodaan {count} kohdetta…",
    "Import {count} Item(s)": "Tuo {count} kohdetta",
    "Import finished:": "Tuonti valmis:",
    "Backup failed — see the activity log.": "Varmuuskopiointi epäonnistui — katso toimintaloki.",
    "{n} added": "{n} lisätty",
    "{n} updated": "{n} päivitetty",
    "{n} failed": "{n} epäonnistui",
    "{n} failed.": "{n} epäonnistui.",
    "Export Import Log": "Vie tuontiloki",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Määritelmä — {word}",
    "Failed to save definition:\n{error}": "Määritelmän tallennus epäonnistui:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Muokkaa — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Sanan tallennus epäonnistui:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Liitä valitut tunnisteet jokaiseen valittuun sanaan"
    ),
    "Failed to add tag:\n{error}": "Tunnisteen lisäys epäonnistui:\n{error}",
    "Failed to apply tags:\n{error}": "Tunnisteiden käyttö epäonnistui:\n{error}",
    "Failed to remove tags:\n{error}": "Tunnisteiden poisto epäonnistui:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Luo tekstin tekoälyllä käyttäen alla olevia Kieli-, Taso- ja Aihe-kenttiä. "
        "Valitse aihe-ehdotus tai kirjoita oma."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Luodaan kielen {language} tekstiä {count} sanasta palvelulla {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Kirjoita tai liitä teksti alla olevaan editoriin, anna sille otsikko, "
        "aseta kieli — ja tallenna."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Poimii luettavan artikkelitekstin miltä tahansa verkkosivulta. "
        "Kirjautumisen takana olevat tai pelkällä JavaScriptillä rakennetut sivut eivät välttämättä toimi."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    "View definition (double-click)": "Näytä määritelmä (kaksoisnapsautus)",
    "Read selected words aloud": "Lue valitut sanat ääneen",
    "Toggle favorite": "Vaihda suosikkitilaa",
    "Add / remove tags": "Lisää / poista tunnisteita",
    "Edit word": "Muokkaa sanaa",
    "Copy words": "Kopioi sanat",
    "Generate text from selection": "Luo teksti valinnasta",

    "PDF files (*.pdf)": "PDF-tiedostot (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excel-tiedostot (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV-tiedostot (*.csv)",
    "Text files (*.txt)": "Tekstitiedostot (*.txt)",
    "MP3 files (*.mp3)": "MP3-tiedostot (*.mp3)",
    "Open Excel Table": "Avaa Excel-taulukko",
    "Save Import Template": "Tallenna tuontimalli",

    "Cloud sync": "Pilvisynkronointi",
    "Not connected. Check internet or credentials": "Ei yhteyttä. Tarkista internet-yhteys tai tunnistetiedot",
    "Syncing with cloud…": "Synkronoidaan pilven kanssa…",
    "Sync completed successfully": "Synkronointi valmistui onnistuneesti",
    "Sync enabled but not connected. Check settings.": "Synkronointi on käytössä, mutta yhteyttä ei ole. Tarkista asetukset.",
    "idle": "toimeton",
    "syncing": "synkronoidaan",
    "success": "onnistui",
    "error": "virhe",

    "No data yet": "Ei vielä tietoja",
    "No activity yet": "Ei vielä aktiivisuutta",
    "Not enough activity yet": "Ei vielä riittävästi aktiivisuutta",

    "APIs": "Rajapinnat (API)",
    "Audio (MP3)": "Ääni (MP3)",
    "Sync": "Synkronointi",

    "OpenAI API key (.env)": "OpenAI API-avain (.env)",
    "Google API key (.env)": "Google API-avain (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Veloitetaan käytön mukaan — hanki avain osoitteesta <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Mallit: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API-käyttö — katso <a href="https://platform.openai.com/usage">hallintapaneeli</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Ilmainen käyttöluokka saatavilla — hanki avain osoitteesta <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Mallit: gemini-2.5-flash, gemini-2.5-flash-lite… API-käyttö — katso <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Hanki avain osoitteesta <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Käytä osoitetta https://api-free.deepl.com/v2/translate ilmaisille avaimille.',

    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Valmistele Excel-tiedosto sarakkeilla <b>Language1, Language2, Word1, Word2</b> — nimettyinä otsikkorivillä (ylimääräiset sarakkeet ohitetaan) tai ilman otsikoita, jolloin neljä ensimmäistä saraketta ovat juuri tässä järjestyksessä.</li><li>Avaa sovellusvalikko → <i>Tuo Excel tietokantaan…</i> ja valitse tiedosto.</li><li>Tarkista ehdotetut rivit ja napsauta <i>Tuo</i>.</li></ol>",

    "created by": "luonut",
    "Version": "Versio",
    "Build": "Käännösversio (Build)",
    "Your personal vocabulary companion": "Henkilökohtainen kumppanisi sanaston opiskeluun",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Rakenna, opiskele ja muista sanastoa eri kielillä — pilvisynkronoinnin, tekoälymääritelmien, käännösten, puhesynteesin ja joustavan viennin avulla.",
    "Source code": "Lähdekoodi",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Henkilökohtainen sanastokumppanisi pilvisynkronoinnilla, tekoälymääritelmillä, käännöksillä, puhesynteesillä ja vientivaihtoehdoilla.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Lisensoitu GNU Affero General Public License v3.0 -lisenssillä. Tämä tekijänoikeusmerkintä on säilytettävä (AGPL §7).",
    "Found a bug or have an idea?": "Löysitkö virheen tai onko sinulla idea?",
    "Report an issue": "Ilmoita ongelmasta",
    "What would you like to report?": "Mistä haluat ilmoittaa?",
    "A bug or technical problem": "Virheestä tai teknisestä ongelmasta",
    "Creates a report with app diagnostics to send to the developers.":
        "Luo raportin sovelluksen diagnostiikalla kehittäjille lähetettäväksi.",
    "Inappropriate AI-generated content": "Sopimattomasta tekoälyn luomasta sisällöstä",
    "Report a definition, text, or translation the AI produced.":
        "Ilmoita tekoälyn luomasta määritelmästä, tekstistä tai käännöksestä.",
    "Report: inappropriate AI-generated content":
        "Ilmoitus: sopimaton tekoälyn luoma sisältö",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Kuvaile ilmoittamaasi tekoälyn luomaa sisältöä.\n\n"
        "Missä se esiintyi (määritelmä / luotu teksti / sanan käännös):\n"
        "Kyseessä oleva sana tai teksti:\n"
        "Miksi se on sopimatonta:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "Ilmoittaaksesi sopimattomasta tekoälyn luomasta sisällöstä, lähetä sähköpostia osoitteeseen {email}.",

    "Support": "Tue",
    "Support Lingueez": "Tue Lingueez-sovellusta",
    "Lingueez is free and open-source.": "Lingueez on ilmainen ja avoimen lähdekoodin sovellus.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Jos pidät Lingueezistä ja pidät sitä hyödyllisenä, kertalahjoitus auttaa kattamaan valinnaisen pilvisynkronoinnin palvelinkuluja ja tukee jatkokehitystä. Maksumuureja ei ole — jokainen ominaisuus pysyy ilmaisena joka tapauksessa.",
    "Support Lingueez's development": "Tue Lingueezin kehitystä",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Stripe-vaihtoehto on kertamaksu — ei tilausta. Maksut käsitellään turvallisesti Stripen tai GitHubin kautta.",

    "Updates": "Päivitykset",
    "Check for updates": "Tarkista päivitykset",
    "You're up to date.": "Käytössäsi on uusin versio.",
    "Update available": "Päivitys saatavilla",
    "Update available — v{version}": "Päivitys saatavilla — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} on saatavilla — sinulla on {current}.",
    "Skip this version": "Ohita tämä versio",
    "Later": "Myöhemmin",
    "Download": "Lataa",
    "Check for updates on startup": "Tarkista päivitykset käynnistettäessä",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Tarkistaa kerran päivässä, onko uudempaa versiota saatavilla; "
        "mitään ei ladata tai asenneta automaattisesti.",

    "in": "in",
    " s": " s",

    # Word statuses
    "New": "Uusi",
    "To Learn": "Opittava",
    "Reviewing": "Kerrattava",
    "Ignored": "Ohitettu",

    # Table density
    "Compact": "Tiivis",
    "Normal": "Normaali",
    "Comfortable": "Mukava",
    "Spacious": "Avara",

    # Language names
    "English": "Englanti",
    "German": "Saksa",
    "Spanish": "Espanja",
    "Ukrainian": "Ukraina",
    "French": "Ranska",
    "Italian": "Italia",
    "Portuguese": "Portugali",
    "Russian": "Venäjä",
    "Greek": "Kreikka",
    "Arabic": "Arabia",
    "Bengali": "Bengali",
    "Cantonese": "Kantoninkiina",
    "Hindi": "Hindi",
    "Japanese": "Japani",
    "Korean": "Korea",
    "Mandarin": "Mandariinikiina",
    "Polish": "Puola",
    "Turkish": "Turkki",
    "Vietnamese": "Vietnam",
    "Afrikaans": "Afrikaans",
    "Albanian": "Albania",
    "Amharic": "Amhara",
    "Armenian": "Armenia",
    "Azerbaijani": "Azeri",
    "Basque": "Baski",
    "Belarusian": "Valkovenäjä",
    "Bosnian": "Bosnia",
    "Bulgarian": "Bulgaria",
    "Catalan": "Katalania",
    "Cebuano": "Cebuano",
    "Chichewa": "Tšitševa",
    "Chinese": "Kiina",
    "Croatian": "Kroatia",
    "Czech": "Tšekki",
    "Danish": "Tanska",
    "Dutch": "Hollanti",
    "Estonian": "Eesti",
    "Filipino": "Filipino",
    "Finnish": "Suomi",
    "Galician": "Galicia",
    "Georgian": "Georgia",
    "Gujarati": "Gudžarati",
    "Haitian Creole": "Haitinkreoli",
    "Hausa": "Hausa",
    "Hawaiian": "Havaiji",
    "Hebrew": "Heprea",
    "Hmong": "Hmong",
    "Hungarian": "Unkari",
    "Icelandic": "Islanti",
    "Igbo": "Igbo",
    "Indonesian": "Indonesia",
    "Irish": "Iiri",
    "Javanese": "Java",
    "Kannada": "Kannada",
    "Kazakh": "Kasakki",
    "Khmer": "Khmer",
    "Kinyarwanda": "Ruanda",
    "Kyrgyz": "Kirgiisi",
    "Lao": "Lao",
    "Latin": "Latina",
    "Latvian": "Latvia",
    "Lithuanian": "Liettua",
    "Luxembourgish": "Luksemburg",
    "Macedonian": "Makedonia",
    "Malagasy": "Malagassi",
    "Malay": "Malaiji",
    "Malayalam": "Malajalam",
    "Maltese": "Malta",
    "Maori": "Maori",
    "Marathi": "Marathi",
    "Mongolian": "Mongolia",
    "Myanmar (Burmese)": "Myanmar (byrma)",
    "Nepali": "Nepali",
    "Norwegian": "Norja",
    "Odia": "Orija",
    "Pashto": "Paštu",
    "Persian": "Persia",
    "Punjabi": "Pandžabi",
    "Romanian": "Romania",
    "Samoan": "Samoa",
    "Scots Gaelic": "Gaelit",
    "Serbian": "Serbia",
    "Sesotho": "Sotho",
    "Shona": "Shona",
    "Sindhi": "Sindhi",
    "Sinhala": "Sinhala",
    "Slovak": "Slovakia",
    "Slovenian": "Slovenia",
    "Somali": "Somali",
    "Sundanese": "Sunda",
    "Swahili": "Swahili",
    "Swedish": "Ruotsi",
    "Tajik": "Tadžikki",
    "Tamil": "Tamili",
    "Tatar": "Tataari",
    "Telugu": "Telugu",
    "Thai": "Thai",
    "Turkmen": "Turkmeeni",
    "Urdu": "Urdu",
    "Uyghur": "Uiguuri",
    "Uzbek": "Uzbekki",
    "Welsh": "Kymri",
    "Xhosa": "Xhosa",
    "Yiddish": "Jiddiš",
    "Yoruba": "Joruba",
    "Zulu": "Zulu",

    # --- Onboarding tour ---
    "Back": "Takaisin",
    "Next": "Seuraava",
    "Done": "Valmis",
    "Show Tour": "Näytä esittely",
    "Step {n} of {total}": "Vaihe {n} / {total}",
    "Your library": "Kirjastosi",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Vaihda Sanat-, Tekstit- ja Tilastot-näkymien välillä tästä sivupalkista.",
    "Add a word": "Lisää sana",
    "Find anything": "Etsi mitä tahansa",
    "Search across your words, translations and tags as you type.":
        "Hae sanoistasi, käännöksistäsi ja tunnisteistasi kirjoittaessasi.",
    "Add a new word here — its translation can be fetched automatically.":
        "Lisää uusi sana tähän — sen käännös voidaan hakea automaattisesti.",
    "Listen and learn": "Kuuntele ja opi",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Valitse sanat ja paina Lue kuullaksesi ne ääneen. Toistuva "
        "kuuntelu edistää sanaa tilasta Uusi tilaan Kerrattava, Opitaan "
        "ja lopulta Hallittu.",
    "Generate a text": "Luo teksti",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Muuta valitut sanat lyhyeksi tekoälyn kirjoittamaksi tarinaksi — "
        "näet sanastosi kontekstissa.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Sanastosi pysyy synkronoituna laitteidesi välillä. Napsauta nähdäksesi "
        "tilan tai synkronoidaksesi heti.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Ota pilvisynkronointi käyttöön, vaihda kieltä, muuta ulkoasua ja "
        "muuta Asetuksista.",

    # --- Texts tour ---
    "Add texts": "Lisää tekstejä",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Kirjoita tai liitä teksti, hae teksti internetistä "
        "(Tekoäly / Wikipedia / URL / RSS) tai tuo .txt-tiedostoja.",
    "Your texts": "Tekstisi",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Selaa tallennettuja tekstejäsi ja suodata niitä kielen, "
        "tason tai aihepiirin mukaan.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Kuuntele mikä tahansa teksti ääneen — ja napsauta sanaa lukemisen aikana "
        "nähdäksesi sen käännöksen tai lisätäksesi sen sanastöösi.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Näytä rinnakkain käännös vierekkäin; valitse kieli "
        "sen vieressä olevalla nuolella.",
    "Reading modes": "Lukutilat",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Keskittymistila piilottaa luettelon, paperitila muuttaa "
        "taustan ja Muokkaa-tila mahdollistaa tekstin muokkaamisen.",

    # --- Flashcards tour ---
    "Choose your deck": "Valitse pakka",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Valitse, mitä pakkaan tulee — kerrattavat kortit, "
        "sanat nykyisestä suodattimesta, uusimmat lisäykset "
        "tai käsin valittu joukko.",
    "Shape the session": "Muotoile istunto",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Määritä kerrattavien korttien määrä, sekoita järjestys ja "
        "aseta jokainen kortti lausuttavaksi, kun se ilmestyy ja kääntyy.",
    "Preview the deck": "Esikatsele pakka",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Täsmälliset kortit, jotka sisältyvät istuntoosi. Napsauta korttia "
        "lukeaksesi tai muokataksesi määritelmää, tai kaiutinta kuullaksesi "
        "sanan.",
    "Review and grade": "Kertaa ja arvioi",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Käännä kukin kortti ja arvioi kuinka hyvin tiesit sen — Vaikea, "
        "Hyvä tai Helppo. Jaksotettu kertaaminen päättää, milloin kortti "
        "palaa: helpot sanat odottavat pidempään, vaikeat palaavat "
        "nopeammin. Välilyönti kääntää, 1–3 arvioi.",
    "Or just listen": "Tai vain kuuntele",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "Toista pakka muuttaa istunnon ääneksi — kortit etenevät "
        "ja kääntyvät puheen tahdissa. Pysäytä milloin tahansa arvioidaksesi "
        "kortin itse.",

    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Sanastosi yhdellä silmäyksellä — kokonaismäärät, hallitut sanat, "
        "kielet ja nykyinen putkesi.",
    "See how your vocabulary has grown over time.":
        "Katso, miten sanastosi on kasvanut ajan myötä.",
    "Track how much you've reviewed over time.":
        "Seuraa, kuinka paljon olet kerrannut ajan myötä.",

    # --- Demo text ---
    "Sample: A walk in the city": "Esimerkki: Kävely kaupungilla",
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
        "Aamu oli kirkas ja kadut olivat hiljaisia. Nuori nainen "
        "käveli hitaasti vanhaa tietä pitkin katsellen korkeita taloja ja "
        "pieniä kauppoja, jotka olivat juuri avautumassa. Hän pysähtyi ostamaan tuoretta "
        "leipää ja kupillisen kahvia, ja ylitti sitten torin puistoa kohti. "
        "Lapset leikkivät joen lähellä vanhempien jutellessa "
        "läheisillä penkeillä. Hän istui suuren puun alle, avasi kirjansa ja "
        "alkoi lukea. Tarina kertoi matkailijasta, joka ylitti "
        "vuoret etsiessään vanhaa ystäväänsä, jota ei ollut nähnyt vuosiin. "
        "Hetken kuluttua hän katsoi ylös ja seurasi veneiden hitaata kulkua "
        "joella ja lintujen liitelyä korkealla kattojen yllä. Katu-uskotko "
        "alkoi soitonsa jossain lähistöllä, ja pehmeät sävelet seurasivat hänen "
        "ajatuksiaan. Se oli rauhallinen ja onnellinen aamu, sellainen josta hän piti eniten.",
    "Demo": "Demo",

    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Virheellinen OpenAI API-avain. Tarkista se kohdassa Asetukset → Käännös ja tekoäly → AI → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "OpenAI-tilisi saldo on lopussa. Lisää saldoa osoitteessa "
        "platform.openai.com/account/billing, tai vaihda tekoälyntarjoajaksi "
        "Gemini kohdassa Asetukset → Käännös ja tekoäly → AI.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI-pyyntöraja saavutettu. Odota hetki ja yritä uudelleen.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Tuntematon OpenAI-malli. Tarkista mallin nimi kohdassa Asetukset → Käännös ja tekoäly → AI → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "OpenAI-palveluun ei saada yhteyttä. Tarkista internet-yhteytesi.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Gemini-kiintiö käytetty. Ilmainen kiintiö nollautuu päivittäin; odota "
        "tai luo uusi avain osoitteessa aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Virheellinen Google API-avain. Tarkista se kohdassa Asetukset → Käännös ja tekoäly → AI → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Tuntematon Gemini-malli. Tarkista mallin nimi kohdassa Asetukset → Käännös ja tekoäly → AI → Gemini.",

    # --- Words empty state ---
    "Your vocabulary journey starts here": "Sanastomatkasi alkaa tästä",
    "Add your first word — its translation can be fetched automatically.":
        "Lisää ensimmäinen sanasi — sen käännös voidaan hakea automaattisesti.",
    "Add your first word": "Lisää ensimmäinen sana",
    "Take the tour": "Katso esittely",
    "No matching words": "Ei vastaavia sanoja",
    "Try a different search or filter.": "Kokeile toista hakua tai suodatinta.",
    "Clear filters": "Tyhjennä suodattimet",

    # --- Texts empty state ---
    "Your reading library starts here": "Lukukirjastosi alkaa tästä",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Lisää teksti luettavaksi — kirjoita tai liitä oma tekstisi, hae sellainen "
        "internetistä tai tuo .txt-tiedosto.",
    "Add a text": "Lisää teksti",
    "Fetch from the Internet": "Hae internetistä",
    "Import .txt": "Tuo .txt",

    # demo text-list stub titles
    "My first story": "Ensimmäinen tarinani",
    "A news article": "Uutisartikkeli",
    "A short poem": "Lyhyt runo",
    "Travel notes": "Matkamuistiinpanot",

    # demo text-list stub first sentences
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Olipa kerran pienessä merenrantakylässä utelias nuori kettu.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Tutkijat ovat löytäneet uuden tavan tutkia, miten "
        "kielet muuttuvat ja kehittyvät vuosisatojen kuluessa.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Tuuli kulkee hiljaa syksyisten puiden läpi "
        "kantaen vanhoja ja puoliksi unohdettuja lauluja.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Ensimmäinen päivä: saavuimme kaupunkiin myöhään yöllä, ja "
        "kadut olivat edelleen täynnä lämmintä valoa.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Toisella laitteella poistetut kohteet",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Kun tämä laite oli offline-tilassa, {n} kohdetta poistettiin muilla "
        "laitteillasi. Säilytetäänkö ne pilvessä vai poistetaanko ne tältä laitteelta?",
    "(untitled)": "(nimetön)",
    "[Text] {title}": "[Teksti] {title}",
    "Remove from this device": "Poista tältä laitteelta",
    "Decide later": "Päätä myöhemmin",
    "Keep & upload": "Säilytä & lataa",
    "Not now": "Ei nyt",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Syötä nimi offline-profiilille.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Voit pitää enintään {max} offline-profiilia. Poista yksi lisätäksesi toisen.",
    "New offline profile": "Uusi offline-profiili",
    "Profile name:": "Profiilin nimi:",
    "Offline profile": "Offline-profiili",
    "Rename offline profile": "Nimeä offline-profiili uudelleen",
    "Offline profiles": "Offline-profiilit",
    "Add offline profile…": "Lisää offline-profiili…",
    "Profile actions": "Profiilin toiminnot",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Erilliset, vain laitekohtaiset kirjastot omalla tietokannallaan. Ne eivät koskaan synkronoidu eivätkä vaadi kirjautumista.",
    "Default (local)": "Oletus (paikallinen)",
    "Rename": "Nimeä uudelleen",
    "Delete offline profile": "Poista offline-profiili",
    "Enable cloud sync…": "Ota pilvisynkronointi käyttöön…",
    "Could not create the profile.": "Profiilia ei voitu luoda.",
    "Created and switched to “{name}”.": "Luotu ja vaihdettu profiiliin “{name}”.",
    "Deleted “{name}”.": "Poistettu “{name}”.",
    "Untitled profile": "Nimetön profiili",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Poistetaanko offline-profiili “{name}” pysyvästi? Sen sanat ja tekstit ovat olemassa vain tällä laitteella — pilvikopiota ei ole. Tietokanta arkistoidaan ensin varmuuskopiokansioon, mutta tätä ei voi peruuttaa sovelluksessa.",
    "this profile": "tämä profiili",
    "Connect to the internet to merge this profile into your account.": "Yhdistä internetiin yhdistääksesi tämän profiilin tiliisi.",
    "Enable cloud sync for this profile": "Ota pilvisynkronointi käyttöön tälle profiilille",
    "Continue": "Jatka",
    "Upload words": "Lataa sanat",
    "Upload texts": "Lataa tekstit",
    "Upload & sync": "Lataa & synkronoi",
    "Could not upload this profile. Your data is unchanged.": "Tätä profiilia ei voitu ladata. Tietosi ovat ennallaan.",
    "“{name}” is now synced to your account.": "“{name}” on nyt synkronoitu tilillesi.",
    "Everything in this profile is already in your account.": "Kaikki tässä profiilissa oleva on jo tililläsi.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Kirjaudu sisään tai luo tili varmuuskopioidaksesi profiilin “{name}” ja synkronoidaksesi sen laitteidesi välillä. Profiilin sanat ja tekstit ladataan palvelimelle ja siitä tulee synkronoitu tilisi tällä laitteella. Kopio arkistoidaan ensin varmuuskopiokansioon.",
    "Upload “{name}” to your account": "Lataa “{name}” tilillesi",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Profiilistasi tulee synkronoitu tili “{who}” tällä laitteella ja se ladataan pilveen.",
    "Merge “{name}” into your account": "Yhdistä “{name}” tiliisi",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Tällä tilillä on jo tietoja tällä laitteella. Profiilisi sanat ja tekstit, joita ei vielä ole siellä, lisätään siihen — mitään ei korvata. “{name}” arkistoidaan sitten varmuuskopiokansioon ja poistetaan.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Tässä profiilissa on {items}, tallennettuna vain tälle laitteelle. Ota pilvisynkronointi käyttöön varmuuskopioidaksesi ne ja opiskellaksesi kaikilla laitteillasi.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Valitse lisättävät kohteet. Ne kopioidaan tilillesi ja ladataan pilveen. “{name}” arkistoidaan sen jälkeen varmuuskopiokansioon ja poistetaan.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Hyväksyn <a href=\"{terms}\">Käyttöehdot</a> ja <a href=\"{privacy}\">Tietosuojaselosteen</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Hyväksy käyttöehdot ja tietosuojaseloste jatkaaksesi.",
    "Updated Terms & Privacy": "Päivitetyt ehdot ja tietosuoja",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Olemme päivittäneet käyttöehtojamme ja tietosuojaselostettamme. Tarkista ja hyväksy ne jatkaaksesi tilisi käyttöä.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Hyväksyn päivitetyt <a href=\"{terms}\">Käyttöehdot</a> ja <a href=\"{privacy}\">Tietosuojaselosteen</a>.",
    "Sign out": "Kirjaudu ulos",
    "I agree": "Hyväksyn",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Tietosuojaseloste</a> · <a href=\"{terms}\">Käyttöehdot</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Jatkamalla hyväksyt <a href=\"{terms}\">Käyttöehdot</a> ja <a href=\"{privacy}\">Tietosuojaselosteen</a>.",
    "Privacy Policy": "Tietosuojaseloste",
    "Terms": "Käyttöehdot",
    "Website": "Verkkosivusto",
    "Contact": "Yhteystiedot",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Muistikortit",
    "Practice your vocabulary": "Harjoittele sanastoasi",
    "Due cards": "Kerrattavat kortit",
    "Current filter": "Nykyinen suodatin",
    "Newest": "Uusimmat",
    "Selected words": "Valitut sanat",
    "Deck size": "Pakan koko",
    "Default deck size": "Pakan oletuskoko",
    "Shuffle": "Sekoita",
    "Start session": "Aloita istunto",
    "Play deck": "Toista pakka",
    "{n} cards ready to review": "{n} korttia valmiina kerrattavaksi",
    "No cards due — great job!": "Ei kerrattavia kortteja — hienoa työtä!",
    "{n} selected words": "{n} valittua sanaa",
    "No words to practice.": "Ei sanoja harjoiteltavaksi.",
    "End session": "Lopeta istunto",
    "Listening — pause to review manually":
        "Kuuntelu — keskeytä kertaaksesi käsin",
    "Show answer": "Näytä vastaus",
    "Hard": "Vaikea",
    "Good": "Hyvä",
    "Easy": "Helppo",
    "Space or click to flip": "Välilyönti tai napsautus kääntääksesi",
    "Card {current} of {total}": "Kortti {current} / {total}",
    "{n} correct": "{n} oikein",
    "Session complete!": "Istunto valmis!",
    "You listened to {n} of {total} cards.": "Kuuntelit {n} / {total} korttia.",
    "Correct: {n} of {total}": "Oikein: {n} / {total}",
    "New session": "Uusi istunto",
    "Practice hard words": "Harjoittele vaikeita sanoja",
    "Hard words": "Vaikeat sanat",
    "Hard words cleared!": "Vaikeat sanat käyty läpi!",
    "Open Flashcards when Read Aloud starts":
        "Avaa Muistikortit, kun Ääneenluku alkaa",
    "Stop": "Pysäytä",
    "Auto-pronounce": "Automaattinen lausunta",
    "Speak each card as it appears and when it flips":
        "Lausu jokainen kortti sen ilmestyessä ja kääntyessä",
    "Deck preview": "Pakan esikatselu",
    "{n} cards": "{n} korttia",
    "Due": "Kerrattava",
    "In {n} d": "{n} pv kuluttua",
    "{n} d": "{n} pv",
    "{n} mo": "{n} kk",
    "{n} y": "{n} v",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez Androidille…",
    "Android app": "Android-sovellus",
    "Lingueez on Android": "Lingueez Androidilla",
    "Take your vocabulary with you": "Ota sanastosi mukaasi",
    "Preview of Lingueez on a phone": "Lingueezin esikatselu puhelimessa",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Kirjaudu Lingueez-tilillesi ja sanastosi on valmiina siellä — "
        "ei määritettävää, ei siirrettävää.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Kirjaudu ilmaiselle Lingueez-tilille molemmilla laitteilla ja sanastosi "
        "synkronoituu puhelimeesi — tiedostoja ei tarvitse kopioida.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Kirjaudu ilmaiselle Lingueez-tilille ja sanasi synkronoituvat puhelimeesi.",
    "Synced both ways": "Kaksisuuntainen synkronointi",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Puhelimella lisäämäsi sanat odottavat tietokoneella ja "
        "päinvastoin.",
    "Listen with the screen off": "Kuuntele näytön ollessa sammutettuna",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Lukitusnäytön ohjaimet, joten kertaus jatkuu puhelimen "
        "ollessa taskussasi.",
    "Save a word from any app": "Tallenna sana mistä tahansa sovelluksesta",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Jaa tekstiä Lingueez-sovellukseen ja se päätyy sanastöösi valmiina "
        "täytettäväksi myöhemmin.",
    "Point your phone's camera at the code":
        "Osoita puhelimen kameralla koodia",
    "Get it on Google Play": "Lataa Google Playsta",
    "Copy link": "Kopioi linkki",
    "Link copied": "Linkki kopioitu",
    "Lingueez is now on Android": "Lingueez on nyt saatavilla Androidille",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Kirjaudu sisään Lingueez-tilillesi — sanastosi on jo siellä.",
    "Dismiss": "Hylkää",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Käytä Lingueez-tiliäsi saumattomasti tietokoneella ja Android-laitteilla.",
    "Get the app…": "Hanki sovellus…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Tietovisa",
    "Quiz (recall practice)": "Tietovisa (muistista palauttaminen)",
    "Recall your words, one question at a time":
        "Palauta sanasi mieleen, kysymys kerrallaan",
    "Questions": "Kysymyksiä",
    "Answer with": "Vastaustapa",
    "Choices": "Valinta",
    "Typing": "Kirjoitus",
    "Ask": "Kysytään",
    "Term": "Termi",
    "Mixed": "Sekaisin",
    "Auto-advance": "Automaattinen siirtyminen",
    "Move on by itself after a correct answer":
        "Siirry eteenpäin itsestään oikean vastauksen jälkeen",
    "Speak the question, then the answer once it is revealed":
        "Lue kysymys ja sen jälkeen vastaus, kun se paljastuu",
    "Start quiz": "Aloita tietovisa",
    "questions ready": "kysymystä valmiina",
    "Nothing to quiz": "Ei kysyttävää",
    "No words match this deck.": "Mikään sana ei vastaa tätä pakkaa.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Tietovisa tarvitsee vähintään kaksi sanaa — väärät vaihtoehdot tulevat juuri "
        "niistä sanoista, joita ei kysytä.",
    "Not enough words": "Ei tarpeeksi sanoja",
    "Add a few more words, or widen the deck.":
        "Lisää muutama sana tai laajenna pakkaa.",
    "Question {n} of {total}": "Kysymys {n}/{total}",
    "Missed words": "Väärin menneet sanat",
    "End quiz": "Lopeta tietovisa",
    "Answer in {language}": "Vastaa kielellä {language}",
    "Type the answer": "Kirjoita vastaus",
    "Check": "Tarkista",
    "Click to continue": "Jatka napsauttamalla",
    "See results": "Näytä tulokset",
    "Almost — it is \"{answer}\"": "Melkein — oikea vastaus on ”{answer}”",
    "It is \"{answer}\"": "Oikea vastaus on ”{answer}”",
    "Now {status}": "Nyt {status}",
    "Correct": "Oikein",
    "Missed": "Väärin",
    "Worth another look": "Kannattaa kerrata",
    "Again": "Uudelleen",
    "Missed words cleared!": "Väärin menneet sanat hallussa!",
    "Perfect run": "Virheetön kierros",
    "Quiz complete": "Tietovisa valmis",
    "Practice missed": "Harjoittele virheitä",
    "Default number of questions": "Kysymysten oletusmäärä",
    "Move on after a correct answer": "Siirry eteenpäin oikean vastauksen jälkeen",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Valitse, mistä sinulta kysytään",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Samat pakat kuin korteissa — kertausta odottavat sanat, nykyinen "
        "suodattimesi, uusimmat tai itse valitut — ja montako kysymystä.",
    "Choices or typing": "Valinta vai kirjoitus",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "”Valinta” tarjoaa neljä vaihtoehtoa; ”Kirjoitus” pyytää kirjoittamaan "
        "vastauksen — vaikeampaa, mutta parempi koe. Kirjoitus antaa anteeksi tarkkeet "
        "ja pienet lyöntivirheet. ”Kysytään” määrää, kumman puolen näet: termin, "
        "käännöksen vai sekaisin.",
    "Start, and it counts": "Aloita — ja se lasketaan",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "Palkki näyttää pakan koostumuksen tiloittain. Jokainen vastaus syöttää samaa "
        "kertausaikataulua kuin kortit: muistamasi sana palaa myöhemmin, väärin mennyt "
        "aiemmin.",
}

# Date names, read by app.i18n. Months are in genitive / partitive form for date displays.
MONTHS = ["tammikuuta", "helmikuuta", "maaliskuuta", "huhtikuuta", "toukokuuta", "kesäkuuta",
          "heinäkuuta", "elokuuta", "syyskuuta", "lokakuuta", "marraskuuta", "joulukuuta"]
MONTHS_ABBR = ["tammi", "helmi", "maalis", "huhti", "touko", "kesä",
               "heinä", "elo", "syys", "loka", "marras", "joulu"]
WEEKDAYS = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai",
            "Perjantai", "Lauantai", "Sunnuntai"]
WEEKDAYS_ABBR = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]