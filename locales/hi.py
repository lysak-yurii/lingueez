# Lingueez — Hindi (hi) translations.
# Keys are English UI strings; values are their Hindi equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "हिन्दी"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "रद्द करें",
    "OK": "ठीक है",
    "Close": "बंद करें",
    "Save": "सहेजें",
    "Delete": "हटाएं",
    "Edit": "संपादित करें",
    "Remove": "हटाएं",
    "Add": "जौड़ें",
    "Refresh": "रिफ्रेश करें",
    "Import": "आयात करें",
    "Export": "निर्यात करें",
    "Search": "खोजें",
    "Fetch": "प्राप्त करें",
    "Browse…": "ब्राउज़ करें…",
    "Clear": "साफ़ करें",
    "Pause": "रोकें",
    "Resume": "पुनः प्रारंभ करें",
    "Language": "भाषा",
    "Translation": "अनुवाद",
    "Word": "शब्द",
    "Status": "स्थिति",
    "Error": "त्रुटि",
    "Title": "शीर्षक",
    "Topic": "विषय",
    "Level": "स्तर",
    "Generate": "जनरेट करें",
    "Generating…": "जनरेट हो रहा है…",
    "Translating…": "अनुवाद हो रहा है…",
    "Format": "प्रारूप",
    "Style": "शैली",
    "Model": "मॉडल",
    "Font": "फ़ॉन्ट",
    "Usage": "उपयोग",
    "Translation language": "अनुवाद की भाषा",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "मेनू",
    "Open Excel Table…": "एक्सेल तालिका खोलें…",
    "Import Excel to Database…": "डेटाबेस में एक्सेल आयात करें…",
    "Save Import Template…": "आयात टेम्पलेट सहेजें…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "ऑडियो (MP3)…",
    "Backups…": "बैकअप…",
    "Show Source column": "'स्रोतः' कॉलम दिखाएं",
    "Show Created At column": "'निर्मित तिथि' कॉलम दिखाएं",
    "Max words…": "अधिकतम शब्द…",
    "View Log": "लॉग देखें",
    "About": "के बारे में",
    "Quit": "बाहर निकलें",
    "Words": "शब्द",
    "Texts": "पाठ",
    "Statistics": "आंकड़े",
    "Bin (deleted items)": "रीसायकल बिन (हटाए गए आइटम)",
    "Settings": "सेटिंग्स",
    "Vocabulary": "शब्दावली",
    "Search words, translations or tags…": "शब्द, अनुवाद या टैग खोजें…",
    "Search texts by title, content or words…": "शीर्षक, सामग्री या शब्दों द्वारा पाठ खोजें…",
    "Search scope": "खोज का दायरा",
    "Search scope…": "खोज का दायरा…",
    "Nothing to practice yet": "अभी अभ्यास के लिए कुछ नहीं है",
    "Add words to your vocabulary and they show up here.":
        "अपनी शब्दावली में शब्द जोड़ें, वे यहाँ दिखाई देंगे।",
    "Come back when cards are due, or practice the newest words now.":
        "जब कार्ड दोहराने का समय हो तब लौटें, या अभी नवीनतम शब्दों का अभ्यास करें।",
    "Practice newest words": "नवीनतम शब्दों का अभ्यास करें",
    "Pick another deck above, or adjust your filters on the Words page.":
        "ऊपर दूसरा डेक चुनें, या शब्द पृष्ठ पर अपने फ़िल्टर बदलें।",
    "You're all caught up": "सब पूरा हो गया",
    "Add word": "शब्द जोड़ें",
    "Copy a word in any app, then press:":
        "किसी भी ऐप में शब्द कॉपी करें, फिर दबाएँ:",
    "Set a shortcut": "शॉर्टकट सेट करें",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "किसी भी ऐप में शब्द कॉपी करें और {keys} दबाएँ — वह अनुवाद सहित जुड़ जाएगा।",
    "Set a shortcut in Settings to add copied words from any app.":
        "किसी भी ऐप से कॉपी किए शब्द जोड़ने के लिए सेटिंग्स में शॉर्टकट सेट करें।",
    " Favorites": " पसंदीदा",
    " Filters": " फ़िल्टर",
    "Filters that don't fit the table": "फ़िल्टर जो तालिका में फ़िट नहीं होते",
    "More actions": "अधिक कार्रवाइयां",
    "Filter by tag": "टैग द्वारा फ़िल्टर करें",
    "Close file and return to your vocabulary": "फ़ाइल बंद करें और अपनी शब्दावली पर लौटें",
    "Definition": "परिभाषा",
    "Read": "पढ़ें",
    "Favorite": "पसंदीदा",
    "Tags": "टैग",
    "Copy": "कॉपी करें",
    "Text": "पाठ",
    "Delete selected (Del)": "चयनित को हटाएं (Del)",
    "No data": "कोई डेटा नहीं",
    "No texts yet": "अभी तक कोई पाठ नहीं है",
    "Words: {shown}/{total}": "शब्द: {shown}/{total}",
    "Texts: {total}": "पाठ: {total}",
    "Texts: {shown}/{total}": "पाठ: {shown}/{total}",
    "{count} selected": "{count} चयनित",
    "No selection": "कोई चयन नहीं",
    "Please select at least one word.": "कृपया कम से कम एक शब्द चुनें।",
    "Saved": "सहेजा गया",
    "'{word}' updated.": "'{word}' अद्यतन किया गया।",
    "Database Error": "डेटाबेस त्रुटि",
    "Delete {count} word(s)?": "क्या आप {count} शब्द हटाना चाहते हैं?",
    "Deleted": "हटा दिया गया",
    "{count} word(s) deleted.": "{count} शब्द हटा दिए गए।",
    "Deleted with {n} error(s).": "{n} त्रुटियों के साथ हटाया गया।",
    "Favorites": "पसंदीदा",
    "{count} word(s) added to favorites.": "{count} शब्द पसंदीदा में जोड़े गए।",
    "{count} word(s) removed from favorites.": "{count} शब्द पसंदीदा से हटा दिए गए।",
    "Status set to '{status}' for {count} word(s).": "{count} शब्दों के लिए स्थिति '{status}' पर सेट की गई।",
    "Max Words": "अधिकतम शब्द",
    "Show only the first N words (0 = show all):": "केवल पहले N शब्द दिखाएं (0 = सभी दिखाएं):",
    "View Definition": "परिभाषा देखें",
    "Copy Word": "शब्द कॉपी करें",
    "Copy Translation": "अनुवाद कॉपी करें",
    "Toggle Favorite": "पसंदीदा चालू/बंद करें",
    "Change Status…": "स्थिति बदलें…",
    "Add / Remove Tags…": "टैग जोड़ें / हटाएं…",
    "Read Aloud": "ज़ोर से पढ़ें",
    "Change Status": "स्थिति बदलें",
    "New status:": "नई स्थिति:",
    "Copied": "कॉपी किया गया",
    "{count} row(s) copied to clipboard.": "{count} पंक्तियां क्लिपबोर्ड पर कॉपी की गईं।",
    "{count} item(s) copied to clipboard.": "{count} आइटम क्लिपबोर्ड पर कॉपी किए गए।",
    "Copy Word(s)": "शब्द कॉपी करें",
    "Copy Translation(s)": "अनुवाद कॉपी करें",
    "Copy Both": "दोनों कॉपी करें",
    "Search in Word": "शब्द में खोजें",
    "Search in Translation": "अनुवाद में खोजें",
    "Search in Tags": "टैग में खोजें",
    "Promoted": "प्रन्नत किया गया",
    "Google Cloud TTS unavailable": "Google Cloud TTS उपलब्ध नहीं है",
    "Selection limit": "चयन सीमा",
    "Only the first 200 selected words will be read.": "केवल पहले 200 चयनित शब्द ही पढ़े जाएंगे।",
    "Only the first 50 words will be used.": "केवल पहले 50 शब्दों का उपयोग किया जाएगा।",
    "Select words to save as audio.": "ऑडियो के रूप में सहेजने के लिए शब्द चुनें।",
    "Nothing to export.": "निर्यात करने के लिए कुछ नहीं है।",
    "Export Error": "निर्यात त्रुटि",
    "Settings saved.": "सेटिंग्स सहेजी गईं।",
    "Generated text saved.": "जनरेट किया गया पाठ सहेजा गया।",
    "Show": "दिखाएं",
    "Add Word": "शब्द जोड़ें",
    "Stop reading": "पढ़ना बंद करें",
    "Read — Read selected words aloud": "पढ़ें — चयनित शब्दों को ज़ोर से पढ़ें",
    "Translation": "अनुवाद",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "रुप-रंग",
    "Audio": "ऑडियो",
    "Learning": "सीखना",
    "Listening": "सुनना",
    "Backups": "बैकअप",
    "Sync your library?": "क्या आप अपनी लाइब्रेरी सिंक करना चाहते हैं?",
    "This will reconcile your device with the cloud:": "यह आपके डिवाइस को क्लाउड के साथ सिंक कर देगा:",
    "Sync now": "अभी सिंक करें",
    "Upload": "अपलोड करें",
    "Synced — ↑{up} ↓{down}": "सिंक किया गया — ↑{up} ↓{down}",
    "Upload restored library?": "पुनर्प्राप्त लाइब्रेरी अपलोड करें?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "लाइब्रेरी पुनर्प्राप्त कर ली गई है। अगली बार सिंक सर्वर से कनेक्ट होने पर आपको इसे अपलोड करने के लिए कहा जाएगा।",
    "Merging this restored backup with your cloud:": "इस पुनर्प्राप्त बैकअप को अपने क्लाउड के साथ मिलाना:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "इस बैकअप में {items} हैं। क्या आप इसे अभी अपने क्लाउड में अपलोड और विलय करना चाहते हैं, या अभी के लिए क्लाउड को अपरिवर्तित रखना चाहते हैं?",
    "General": "सामान्य",
    "Read-aloud": "सस्वर वाचन (Read-aloud)",
    "Translation & AI": "अनुवाद और AI",
    "Data": "डेटा",
    "Behavior": "व्यवहार",
    "Progress": "प्रगति",
    "DeepL request failed — using free Google Translate instead.": "DeepL अनुरोध विफल रहा — इसके बजाय मुफ़्त Google Translate का उपयोग किया जा रहा है।",
    "DeepL key isn't set — using free Google Translate instead.": "DeepL की (key) सेट नहीं है — इसके बजाय मुफ़्त Google Translate का उपयोग किया जा रहा है।",
    "System": "सिस्टम",
    "Light": "लाइट",
    "Dark": "डार्क",
    "Appearance mode": "उपस्थिति मोड",
    "Widget scaling": "विजेट स्केलिंग",
    "Table size": "तालिका का आकार",
    "Interface language": "इंटरफ़ेस की भाषा",
    "Restart the app to apply the language change.": "भाषा परिवर्तन लागू करने के लिए ऐप को पुनः प्रारंभ करें।",
    "The interface language has changed. Restart now to apply it?": "इंटरफ़ेस की भाषा बदल गई है। लागू करने के लिए अभी पुनरारंभ करें?",
    "TTS provider": "TTS प्रदाता",
    "Google Cloud credentials": "Google Cloud क्रेडेंशियल",
    "Voice type": "आवाज़ का प्रकार",
    "Voice name (optional)": "आवाज़ का नाम (वैकल्पिक)",
    "Read Aloud playback": "ज़ोर से पढ़ने का प्लेबैक",
    "Pause between words (s)": "शब्दों के बीच विराम (सेकंड)",
    "Repeats per word": "प्रति शब्द दोहराव",
    "Repeats per pair": "प्रति जोड़ी दोहराव",
    "Promote status while listening": "सुनते समय स्थिति को प्रन्नत करें",
    "Listens to reach {status}": "'{status}' तक पहुंचने के लिए सुनें",
    "Excel import": "एक्सेल आयात",
    "Placeholder values": "प्लेसहोल्डर मान",
    "Skip placeholder rows": "प्लेसहोल्डर पंक्तियों को छोड़ें",
    "Skip empty rows": "खाली पंक्तियों को छोड़ें",
    "Normalize language pairs": "भाषा जोड़ों को सामान्य करें",
    "How to import": "आयात कैसे करें",
    "Save import template…": "आयात टेम्पलेट सहेजें…",
    "Active provider": "सक्रिय प्रदाता",
    "API key": "API की (Key)",
    "API URL": "API URL",
    "Check usage": "उपयोग जांचें",
    "Enable cloud sync": "क्लाउड सिंक सक्षम करें",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase की (.env)",
    "Bin cleanup grace (days)": "बिन सफ़ाई की समय-सीमा (दिन)",
    "Test Connection": "कनेक्शन का परीक्षण करें",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "क्लाउड सिंक आपके खुद के Supabase प्रोजेक्ट का उपयोग करता है। एक बार आवश्यक तालिकाएं बनाएं, फिर ऊपर URL और anon key दर्ज करें।",
    "Copy schema SQL": "स्कीमा SQL कॉपी करें",
    "Open SQL editor ↗": "SQL एडिटर खोलें ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "स्कीमा SQL क्लिपबोर्ड पर कॉपी हो गया है। अपने Supabase प्रोजेक्ट का SQL एडिटर खोलें, इसे पेस्ट करें और तालिकाएं बनाने के लिए Run दबाएं।",
    "Server": "सर्वर",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "आपके अपने Supabase सर्वर से कनेक्टेड — व्यक्तिगत मोड, किसी खाते की आवश्यकता नहीं है।\n{host}",
    "Use your own Supabase server (personal)": "अपने स्वयं के Supabase सर्वर का उपयोग करें (व्यक्तिगत)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "आपके स्वामित्व वाले Supabase प्रोजेक्ट के लिए व्यक्तिगत, एकल-उपयोगकर्ता सिंक। कोई खाता या साइन-इन नहीं — ऐप प्रोजेक्ट की anon key से जुड़ता है। अपने प्रोजेक्ट में स्कीमा SQL चलाएं, उसका URL और anon key नीचे पेस्ट करें, फिर परीक्षण करें।\n\nनोट: इस URL और key वाला कोई भी व्यक्ति डेटा पढ़ सकता है, इसलिए प्रोजेक्ट को निजी रखें और key साझा न करें।",
    "Disconnect — use the built-in server": "डिस्कनेक्ट करें — अंतर्निहित (built-in) सर्वर का उपयोग करें",
    "Disconnect server": "सर्वर डिस्कनेक्ट करें",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "क्या आप अपने खुद के Supabase सर्वर के साथ सिंक करना बंद करके पुनः अंतर्निहित सर्वर का उपयोग करना चाहते हैं?\n\nआपके शब्द आपके अपने प्रोजेक्ट और इस डिवाइस में रहेंगे। जब तक आप किसी खाते में साइन इन नहीं करते, आप केवल स्थानीय मोड में रहेंगे।",
    "Disconnected — using the built-in server.": "डिस्कनेक्ट हो गया — अंतर्निहित सर्वर का उपयोग किया जा रहा है।",
    "{host} (personal)": "{host} (व्यक्तिगत)",
    "Personal": "व्यक्तिगत",
    "your server": "आपका सर्वर",
    "Account actions": "खाता कार्रवाइयां",
    "Add account…": "खाता जोड़ें…",
    "Sync this device's data to my account…": "इस डिवाइस का डेटा मेरे खाते में सिंक करें…",

    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "खाता",
    "Accounts": "खाते",
    "No accounts yet. Add one to sync your words across devices.": "अभी तक कोई खाता नहीं है। अपने शब्दों को डिवाइसों में सिंक करने के लिए एक खाता जोड़ें।",
    "(active)": "(सक्रिय)",
    "Sign in": "साइन इन करें",
    "(sign in again)": "(पुनः साइन इन करें)",
    "Switch": "बदलें",
    "Remove account": "खाता हटाएं",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "इस डिवाइस से {email} को हटाएं? आप इसे किसी भी समय फिर से जोड़ सकते हैं — आपके शब्द क्लाउड में सुरक्षित रहेंगे, और स्थानीय प्रति डिस्क पर रहेगी। आपका क्लाउड डेटा नहीं हटाया जाता है।",
    "Removed {email} from this device.": "इस डिवाइस से {email} को हटा दिया गया।",
    "Your data was exported.": "आपका डेटा निर्यात किया गया था।",
    "Export failed.": "निर्यात विफल रहा।",
    "Delete account": "खाता हटाएं",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "यह आपके खाते को और क्लाउड से आपके सभी सिंक किए गए शब्दों, पाठों और टैगों को स्थायी रूप से हटा देता है। आपकी स्थानीय प्रति बैकअप फ़ोल्डर में संग्रहीत की जाएगी। इसे पूर्ववत नहीं किया जा सकता।\n\nक्या अपना खाता हटाना चाहते हैं?",
    "Account deleted.": "खाता हटा दिया गया।",
    "Could not delete the account.": "खाता नहीं हटाया जा सका।",

    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "नाम",
    "Enter your name.": "अपना नाम दर्ज करें।",
    "Email": "ईमेल",
    "Password": "पासवर्ड",
    "New password": "नया पासवर्ड",
    "6-digit code": "6-अंकों का कोड",
    "or": "या",
    "Sign in with Google": "Google के साथ साइन इन करें",
    "Opening your browser to sign in with Google…": "Google से साइन इन करने के लिए आपका ब्राउज़र खोला जा रहा है…",
    "Forgot password?": "पासवर्ड भूल गए?",
    "Resend code": "कोड पुनः भेजें",
    "Confirm your email": "अपने ईमेल की पुष्टि करें",
    "Verify code": "कोड सत्यापित करें",
    "Use a different email": "किसी अन्य ईमेल का उपयोग करें",
    "Enter your email and password.": "अपना ईमेल और पासवर्ड दर्ज करें।",
    "Enter the 6-digit code from the email.": "ईमेल से 6 अंकों का कोड दर्ज करें।",
    "Enter the code and a new password.": "कोड और नया पासवर्ड दर्ज करें।",
    "Enter your email above first.": "पहले ऊपर अपना ईमेल दर्ज करें।",
    "Enter the reset code we emailed you and a new password.": "हमने जो रीसेट कोड आपको ईमेल किया है वह और नया पासवर्ड दर्ज करें।",
    "Enter the 6-digit code we emailed you.": "हमने जो 6 अंकों का कोड ईमेल किया है उसे दर्ज करें।",
    "Reset password": "पासवर्ड रीसेट करें",
    "Set new password": "नया पासवर्ड सेट करें",
    "Back to sign in": "साइन इन पर वापस जाएं",
    "Sign-in failed.": "साइन इन विफल रहा।",
    "Couldn't send the code.": "कोड नहीं भेजा जा सका।",
    "Done.": "हो गया।",
    "Failed.": "विफल।",
    "Create an account": "एक खाता बनाएं",
    "Create account": "खाता बनाएं",
    "I already have an account": "मेरा पहले से एक खाता है",
    "Signed in as {email}": "{email} के रूप में साइन इन हैं",

    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "इस डिवाइस के डेटा को अपने खाते से सिंक करें",
    "your account": "आपका खाता",
    "This device has {words} and {texts} not yet in {account}.": "इस डिवाइस में {words} और {texts} हैं जो अभी {account} में नहीं हैं।",
    "This device has {words} not yet in {account}.": "इस डिवाइस में {words} हैं जो अभी {account} में नहीं हैं।",
    "This device has {texts} not yet in {account}.": "इस डिवाइस में {texts} हैं जो अभी {account} में नहीं हैं।",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "जोड़ने के लिए आइटम चुनें। वे आपके खाते में कॉपी हो जाते हैं और क्लाउड पर अपलोड हो जाते हैं, ताकि वे आपके अन्य डिवाइसों पर दिखाई दें। इस डिवाइस पर कॉपी बनी रहती है।",
    "Don't ask again for this account": "इस खाते के लिए दोबारा न पूछें",
    "{n} word": "{n} शब्द",
    "{n} words": "{n} शब्द",
    "{n} text": "{n} पाठ",
    "{n} texts": "{n} पाठ",
    "Add {n} item": "{n} आइटम जोड़ें",
    "Add {n} items": "{n} आइटम जोड़ें",
    "words (genitive)": "शब्द",
    "texts (genitive)": "पाठ",
    "tags (genitive)": "टैग",
    "changes (genitive)": "परिवर्तन",
    "deletions (genitive)": "हटाए गए",
    "{n} words (genitive)": "{n} शब्द",
    "{n} texts (genitive)": "{n} पाठ",
    "Add {n} items (genitive)": "{n} आइटम जोड़ें",
    "Added {n} item to your account.": "आपके खाते में {n} आइटम जोड़ा गया।",
    "Added {n} items to your account.": "आपके खाते में {n} आइटम जोड़े गए।",
    "Added {n} items to your account. (genitive)": "आपके खाते में {n} आइटम जोड़े गए।",
    "{n} couldn't be added.": "{n} नहीं जोड़ा जा सका।",

    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "आपका सत्र समाप्त हो गया — पुनः साइन इन करें (सेटिंग्स → सिंक)",
    "Sign in to sync (Settings → Sync)": "सिंक करने के लिए साइन इन करें (सेटिंग्स → सिंक)",
    "Sign in again to sync": "सिंक करने के लिए पुनः साइन इन करें",
    "Sign in again to use this account.": "इस खाते का उपयोग करने के लिए पुनः साइन इन करें।",
    "Sync incomplete: {reason}": "सिंक अधूरा: {reason}",
    "Connect to the internet to add local items to your account.": "अपने खाते में स्थानीय आइटम जोड़ने के लिए इंटरनेट से कनेक्ट करें।",
    "Everything on this device is already in your account.": "इस डिवाइस की हर चीज़ पहले से ही आपके खाते में है।",
    "Upload local words?": "स्थानीय शब्द अपलोड करें?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "अपने वर्तमान स्थानीय शब्दों को इस खाते में अपलोड करें? वे इस खाते के क्लाउड डेटा के साथ मिल जाएंगे और सिंक हो जाएंगे।\n\nइस खाते के मौजूदा डेटा को रखने के लिए 'नहीं' चुनें (स्थानीय शब्दों को बैकअप फ़ोल्डर में सहेजा जाएगा)।",

    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "साइन-इन विफल रहा। अपना ईमेल और पासवर्ड जांचें।",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "आप इस डिवाइस पर {max} खाते तक रख सकते हैं। दूसरा जोड़ने के लिए एक हटाएं।",
    "Wrong email or password.": "गलत ईमेल या पासवर्ड।",
    "That doesn't look like a valid email address.": "यह एक मान्य ईमेल पता नहीं लग रहा है।",
    "Confirm password": "पासवर्ड की पुष्टि करें",
    "Passwords don't match.": "पासवर्ड मेल नहीं खाते।",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "आपका ईमेल अभी तक पुष्ट नहीं हुआ है। हमने जो 6 अंकों का कोड ईमेल किया है उसे दर्ज करें।",
    "That email is already registered. Try signing in instead.": "वह ईमेल पहले से पंजीकृत है। इसके बजाय साइन इन करने का प्रयास करें।",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "हमने आपको 6 अंकों का कोड ईमेल किया है। साइन अप पूरा करने के लिए इसे दर्ज करें।",
    "That code didn't work. Check it and try again.": "वह कोड काम नहीं किया। इसे जांचें और पुनः प्रयास करें।",
    "If that account exists, a 6-digit reset code is on its way.": "यदि वह खाता मौजूद है, तो 6 अंकों का रीसेट कोड भेजा जा चुका है।",
    "Confirmation email re-sent.": "पुष्टि ईमेल पुनः भेजा गया।",
    "Too many attempts. Please wait a minute and try again.": "बहुत सारे प्रयास। कृपया एक मिनट प्रतीक्षा करें और पुनः प्रयास करें।",
    "Your password is too short — use at least 6 characters.": "आपका पासवर्ड बहुत छोटा है — कम से कम 6 अक्षरों का उपयोग करें।",
    "Sign-ups are disabled on this server.": "इस सर्वर पर साइन-अप अक्षम हैं।",
    "Can't reach the server. Check your internet connection.": "सर्वर तक नहीं पहुंचा जा सका। अपना इंटरनेट कनेक्शन जांचें।",
    "Something went wrong.": "कुछ गलत हो गया।",
    "Your saved sign-in for this account expired. Sign in again.": "इस खाते के लिए आपका सहेजा गया साइन-इन समाप्त हो गया है। फिर से साइन इन करें।",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "क्लाउड सिंक अभी कॉन्फ़िगर नहीं किया गया है। पहले सेटिंग्स → सिंक में Supabase URL और Key जोड़ें।",
    "Could not start Google sign-in.": "Google साइन-इन प्रारंभ नहीं किया जा सका।",
    "Google sign-in was cancelled or timed out.": "Google साइन-इन रद्द कर दिया गया था या समय समाप्त हो गया था।",
    "Google sign-in failed.": "Google साइन-इन विफल रहा।",
    "Google sign-in failed: {error}": "Google साइन-इन विफल: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "पोर्ट {port} पर स्थानीय साइन-इन सहायक प्रारंभ नहीं किया जा सका ({error})। जो भी इसका उपयोग कर रहा है उसे बंद करें और पुनः प्रयास करें।",
    "Export my data…": "मेरा डेटा निर्यात करें…",
    "Delete account…": "खाता हटाएं…",
    "Cloud sync is on — your own server ({host})": "क्लाउड सिंक चालू है — आपका अपना सर्वर ({host})",
    "Cloud sync is on — signed in as {who}": "क्लाउड सिंक चालू है — {who} के रूप में साइन इन हैं",
    "Cloud sync is off — your words are saved on this device only": "क्लाउड सिंक बंद है — आपके शब्द केवल इस डिवाइस पर सहेजे गए हैं",
    "(checking…)": "(जांच हो रही है…)",
    "(can't connect)": "(कनेक्ट नहीं हो सकता)",
    "Turn off cloud sync": "क्लाउड सिंक बंद करें",
    "Cloud sync turned off — this device only.": "क्लाउड सिंक बंद कर दिया गया — केवल यह डिवाइस।",
    "Use this server": "इस सर्वर का उपयोग करें",
    "Connecting…": "कनेक्ट हो रहा है…",
    "Testing…": "परीक्षण जारी है…",
    "Applying theme…": "थीम लागू हो रही है…",
    "Now syncing with your own server.": "अब आपके अपने सर्वर के साथ सिंक हो रहा है।",
    "Could not connect to this server:\n{error}": "इस सर्वर से कनेक्ट नहीं हो सका:\n{error}",
    "Could not connect to this server.": "इस सर्वर से कनेक्ट नहीं हो सका।",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nURL और anon key की जांच करें, और देखें कि आपने वहां स्कीमा SQL चलाया है या नहीं। फिर भी इन विवरणों का उपयोग करें?",
    "Enter your server's URL and anon key first, then test.": "पहले अपने सर्वर का URL और anon key दर्ज करें, फिर परीक्षण करें।",
    "Enter your server's URL and anon key first.": "पहले अपने सर्वर का URL और anon key दर्ज करें।",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase key (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "आपके स्वामित्व वाले Supabase प्रोजेक्ट के लिए व्यक्तिगत सिंक। कोई खाता नहीं — ऐप प्रोजेक्ट की anon key से जुड़ता है। अपने प्रोजेक्ट में स्कीमा SQL चलाएं, उसका URL और anon key नीचे पेस्ट करें, परीक्षण करें, फिर “इस सर्वर का उपयोग करें” दबाएं।\n\nनोट: इस URL और key वाला कोई भी व्यक्ति डेटा पढ़ सकता है, इसलिए प्रोजेक्ट को निजी रखें।",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "क्या अपने स्वयं के Supabase सर्वर के साथ सिंक करना बंद करके पुनः अंतर्निहित सर्वर का उपयोग करना चाहते हैं?\n\nआपके शब्द आपके प्रोजेक्ट और डिवाइस पर रहेंगे। जब तक आप किसी खाते में साइन इन नहीं करते, आप केवल स्थानीय मोड में रहेंगे।",
    "Start automatically on login (minimized to tray)": "लॉगिन पर स्वचालित रूप से प्रारंभ करें (ट्रे में छोटा करके)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "Windows सेटिंग्स में Lingueez के लिए लॉगिन पर शुरू होना बंद है, इसलिए इसे यहाँ चालू नहीं किया जा सकता।",
    "Open Windows startup settings": "Windows स्टार्टअप सेटिंग्स खोलें",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows ने यह बदलाव लागू नहीं किया। आप Lingueez को स्वयं सेटिंग्स > ऐप्स > स्टार्टअप में चालू या बंद कर सकते हैं।",
    "Add Word hotkey (global)": "'शब्द जोड़ें' हॉटकी (ग्लोबल)",
    "Data format": "डेटा प्रारूप",
    "Columns to export": "निर्यात करने के लिए कॉलम",
    "Sheet name": "शीट का नाम",
    "Start row": "शुरुआती पंक्ति",
    "Start column": "शुरुआती कॉलम",
    "Shade alternate rows": "एकांतर पंक्तियों को छायांकित करें",
    "Auto column width": "ऑटो कॉलम चौड़ाई",
    "Freeze header row": "शीर्षलेख पंक्ति फ़्रीज़ करें",
    "Delimiter": "डेलीमीटर",
    "Delimiter (\\t = tab)": "डेलीमीटर (\\t = टैब)",
    "Include header lines": "शीर्षलेख पंक्तियां शामिल करें",
    "Header lines": "शीर्षलेख पंक्तियां",
    "Page size": "पेज का आकार",
    "Font size": "फ़ॉन्ट का आकार",
    "Line spacing (pt)": "पंक्ति रिक्ति (pt)",
    "Text alignment": "पाठ संरेखण",
    "Margins L/R/T/B (pt)": "मार्जिन बायां/दायां/ऊपर/नीचे (pt)",
    "Automatic widths (fit page)": "स्वचालित चौड़ाई (पेज में फिट)",
    "Columns / width": "कॉलम / चौड़ाई",
    "Header background": "शीर्षलेख पृष्ठभूमि",
    "Header text": "शीर्षलेख पाठ",
    "Row background": "पंक्ति पृष्ठभूमि",
    "Grid lines": "ग्रिड लाइनें",
    "Background image": "पृष्ठभूमि छवि",
    "Concurrent workers": "समवर्ती वर्कर",
    "Requests per second": "प्रति सेकंड अनुरोध",
    "Add font…": "फ़ॉन्ट जोड़ें…",
    "Page && text": "पेज और पाठ",
    "Columns": "कॉलम",
    "Max tokens": "अधिकतम टोकन",
    "Temperature": "तापमान (Temperature)",
    "Prompt template": "प्रॉम्प्ट टेम्पलेट",
    "Definitions": "परिभाषाएं",
    "Generated Texts (from words)": "जनरेट किए गए पाठ (शब्दों से)",
    "Generated Texts (by topic)": "जनरेट किए गए पाठ (विषय के अनुसार)",
    "Text Adaptation (to level)": "पाठ अनुकूलन (स्तर के अनुसार)",
    "Thinking budget (0 = off, -1 = auto)": "थिंकिंग बजट (0 = बंद, -1 = ऑटो)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "भाषा पहचानें",
    "Type a word or phrase…": "एक शब्द या वाक्यांश टाइप करें…",
    "Translation…": "अनुवाद…",
    "Pronounce": "उच्चारण करें",
    "Swap word and translation": "शब्द और अनुवाद को आपस में बदलें",
    "Translate with DeepL (Enter)": "DeepL से अनुवाद करें (Enter)",
    "Save Word": "शब्द सहेजें",
    "Enter a word to translate.": "अनुवाद करने के लिए एक शब्द दर्ज करें।",
    "Fill with AI (lemma + best translation)": "AI से भरें (मूल शब्द + सर्वोत्तम अनुवाद)",
    "Enter a word to fill with AI.": "AI से भरने के लिए एक शब्द दर्ज करें।",
    "Source equals target — translated to {lang} instead.": "स्रोत और लक्ष्य समान हैं — इसके बजाय {lang} में अनुवादित किया गया।",
    "Both word and translation are required.": "शब्द और अनुवाद दोनों आवश्यक हैं।",
    "Please select the source language before saving.": "कृपया सहेजने से पहले स्रोत भाषा चुनें।",
    "'{word}' already exists in your dictionary.": "'{word}' आपकी शब्दावली में पहले से मौजूद है।",
    "'{word}' is already in your dictionary.": "'{word}' आपकी शब्दावली में पहले से मौजूद है।",
    "Already in your dictionary": "आपकी शब्दावली में पहले से मौजूद है",
    "Show existing": "मौजूदा दिखाएं",
    "The text was truncated to the first 100 words.": "पाठ को पहले 100 शब्दों तक छोटा कर दिया गया था।",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "AI से जनरेट करें",
    "Regenerate with AI": "AI से पुनः जनरेट करें",
    "Definition 2": "परिभाषा 2",
    "No definition yet": "अभी कोई परिभाषा नहीं है",
    "Generate one with AI, or write your own with Edit.": "AI से एक जनरेट करें, या 'संपादित करें' से अपनी खुद की लिखें।",
    "There is no word to define.": "परिभाषित करने के लिए कोई शब्द नहीं है।",
    "Bold": "बोल्ड",
    "Italic": "इटैलिक",
    "Heading": "शीर्षक",
    "List": "सूची",
    "API key missing": "API की (key) गायब है",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "पहले सेटिंग्स → अनुवाद और AI → AI में अपनी {ai} API key सेट करें।",
    "Generating definition…": "परिभाषा जनरेट हो रही है…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "टैग — {count} शब्द",
    "New tag name…": "नया टैग नाम…",
    "Add Tag": "टैग जोड़ें",
    "Apply Selected to All": "चयनित को सभी पर लागू करें",
    "Remove Selected": "चयनित को हटाएं",
    "(partial)": "(आंशिक)",
    "use(s)": "उपयोग",
    "Tags marked ✓ apply to all selected words.": (
        "✓ से चिह्नित टैग सभी चयनित शब्दों पर लागू होते हैं।"
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (आंशिक) का अर्थ है कि केवल कुछ शब्दों में यह टैग है।"
    ),
    "Select tag(s) in the list first.": "पहले सूची में टैग चुनें।",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "रीसायकल बिन — हटाए गए आइटम",
    "Delete Permanently": "स्थायी रूप से हटाएं",
    "Cleanup Old Items…": "पुराने आइटम साफ़ करें…",
    "{n} selected": "{n} चयनित",
    "The bin is empty. Deleted words will appear here.":
        "बिन खाली है। हटाए गए शब्द यहां दिखाई देंगे।",
    "The bin is empty. Deleted texts will appear here.":
        "बिन खाली है। हटाए गए पाठ यहां दिखाई देंगे।",
    "deleted {when}": "{when} हटाया गया",
    "(empty)": "(खाली)",
    "Untitled": "बिना शीर्षक का",
    "Auto-deletes soon": "शीघ्र ही स्वचालित रूप से हट जाएगा",
    "Auto-deletes in {n} day": "{n} दिन में स्वचालित रूप से हट जाएगा",
    "Auto-deletes in {n} days": "{n} दिनों में स्वचालित रूप से हट जाएगा",
    "Auto-deletes in {n} days (genitive)": "{n} दिनों में स्वचालित रूप से हट जाएगा",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "क्या {count} आइटम स्थायी रूप से हटाना चाहते हैं? इसे पूर्ववत नहीं किया जा सकता।",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "पुराना संस्करण पुनर्प्राप्त करें",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "प्रत्येक परिवर्तन के बाद आपके डेटाबेस का स्वचालित रूप से बैकअप लिया जाता है। "
        "इसे पुनर्प्राप्त करने के लिए नीचे एक पुराना संस्करण चुनें।"
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "अभी तक कोई सहेजे गए संस्करण नहीं हैं। "
        "हर बदलाव के बाद अपने आप बैकअप बन जाता है।"
    ),
    "Restore this version": "इस संस्करण को पुनर्प्राप्त करें",
    "Today": "आज",
    "Yesterday": "कल",
    "Most recent": "नवीनतम",
    "Before your last restore": "आपके अंतिम पुनर्प्राप्ति से पहले",
    "today": "आज",
    "yesterday": "कल",
    "today {time}": "आज {time}",
    "yesterday {time}": "कल {time}",
    "the version from {date}": "{date} का संस्करण",
    "the version from just before your last restore": "आपकी अंतिम पुनर्प्राप्ति से ठीक पहले का संस्करण",
    "Restore Version": "संस्करण पुनर्प्राप्त करें",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "क्या {phrase} पुनर्प्राप्त करना चाहते हैं?\n\nआपका वर्तमान डेटा पहले सहेजा जाता है, ताकि आप इसे पूर्ववत कर सकें।"
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "आपका डेटाबेस {phrase} में पुनर्प्राप्त कर दिया गया है।\n\n"
        "क्या मन बदल गया? पूर्ववत करने के लिए \"{before}\" पुनर्प्राप्त करें।"
    ),
    "Restore Error": "पुनर्प्राप्ति त्रुटि",
    "Sorry, that version could not be restored:\n{error}": "क्षमा करें, वह संस्करण पुनर्प्राप्त नहीं किया जा सका:\n{error}",
    "Remove Version": "संस्करण हटाएं",
    "Remove {phrase}?": "{phrase} हटाएं?",
    "Remove Error": "हटाने में त्रुटि",
    "Sorry, that version could not be removed:\n{error}": "क्षमा करें, वह संस्करण हटाया नहीं जा सका:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "पाठ जनरेट करें",
    "Title…": "शीर्षक…",
    "Generated text appears here…": "जनरेट किया गया पाठ यहां दिखाई देगा…",
    "Save to Texts": "पाठ में सहेजें",
    "Save failed": "सहेजना विफल रहा",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "ऑडियो में सहेजें",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "{count} शब्द/अनुवाद जोड़ों से एक MP3 फ़ाइल जनरेट करें।"
    ),
    "Generating audio…": "ऑडियो जनरेट हो रहा है…",
    "Compiling final audio file…": "अंतिम ऑडियो फ़ाइल संकलित की जा रही है…",
    "Processed: {word}": "संसाधित: {word}",
    "Choose File && Start": "फ़ाइल चुनें और शुरू करें",
    "Cancelled.": "रद्द कर दिया गया।",
    "Audio saved": "ऑडियो सहेजा गया",
    "Audio file saved to:\n{path}": "ऑडियो फ़ाइल यहां सहेजी गई:\n{path}",
    "Audio Error": "ऑडियो त्रुटि",
    "Failed to save audio:\n{error}": "ऑडियो सहेजने में विफल:\n{error}",
    "Cancelling…": "रद्द किया जा रहा है…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "एक्सेल से आयात करें",
    "Row": "पंक्ति",
    "Word 1": "शब्द 1",
    "Language 1": "भाषा 1",
    "Word 2": "शब्द 2",
    "Language 2": "भाषा 2",
    "Action": "कार्रवाई",
    "Details": "विवरण",
    "Add": "जोड़ें",
    "Update": "अद्यतन करें",
    "Skip": "छोड़ें",
    "All": "सभी",
    "To add": "जोड़ने के लिए",
    "To update": "अद्यतन करने के लिए",
    "Skipped": "छोड़े गए",
    "Unrecognized": "अपरिचित",
    "Only recognized languages": "केवल पहचानी गई भाषाएं",
    "Exclude rows whose language wasn't recognized.":
        "उन पंक्तियों को बाहर रखें जिनकी भाषा पहचानी नहीं गई थी।",
    "Unrecognized language — will be imported exactly as written.":
        "अपरिचित भाषा — ठीक वैसे ही आयात की जाएगी जैसी लिखी गई है।",
    "Select all": "सभी चुनें",
    "Activity log": "गतिविधि लॉग",
    "Export log…": "लॉग निर्यात करें…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "निर्यात करें…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "पाठ जोड़ें",
    "Write": "लिखें",
    "AI Generate": "AI जनरेट",
    "Wikipedia": "विकिपीडिया",
    "From URL": "URL से",
    "Language:": "भाषा:",
    "Level:": "स्तर:",
    "Topic:": "विषय:",
    "Topic…": "विषय…",
    "Adapt to my level": "मेरे स्तर के अनुसार ढालें",
    "Load entries": "प्रविष्टियां लोड करें",
    "Add feed…": "फ़ीड जोड़ें…",
    "Ideas:": "विचार:",
    "Short (~100 words)": "छोटा (~100 शब्द)",
    "Medium (~250 words)": "मध्यम (~250 शब्द)",
    "Long (~500 words)": "लंबा (~500 शब्द)",
    "Travel": "यात्रा",
    "Food": "भोजन",
    "Daily routine": "दिनचर्या",
    "A short story": "एक छोटी कहानी",
    "News": "समाचार",
    "Dialogue at a café": "कैफे में बातचीत",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "अपना पाठ यहां टाइप करें या पेस्ट करें, या ऊपर दिए गए टैब से प्राप्त करें…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "नवीनतम पहले",
    "Oldest first": "पुराने पहले",
    "Title A–Z": "शीर्षक A–Z",
    "All languages": "सभी भाषाएं",
    "All levels": "सभी स्तर",
    "All topics": "सभी विषय",
    "No matching texts": "कोई मेल खाते पाठ नहीं हैं",
    "Try a different search or language filter.": "अलग खोज या भाषा फ़िल्टर का प्रयास करें।",
    "New text (write or paste)": "नया पाठ (लिखें या पेस्ट करें)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "इंटरनेट से पाठ प्राप्त करें (AI / विकिपीडिया / URL / RSS)"
    ),
    "Import .txt file(s)": ".txt फ़ाइल(एं) आयात करें",
    "Read aloud": "ज़ोर से पढ़ें",
    "Translate text": "पाठ का अनुवाद करें",
    "Hide translation": "अनुवाद छिपाएं",
    "Focus mode": "फ़ोकस मोड",
    "Exit focus mode": "फ़ोकस मोड से बाहर निकलें",
    "Paper mode: off": "पेपर मोड: बंद",
    "Paper: white (click for sepia)": "पेपर: सफ़ेद (सेपिया के लिए क्लिक करें)",
    "Paper: sepia (click to turn off)": "पेपर: सेपिया (बंद करने के लिए क्लिक करें)",
    "Save Changes": "परिवर्तन सहेजें",
    "Previous text": "पिछला पाठ",
    "Next text": "अगला पाठ",
    "From words: {words}": "शब्दों से: {words}",
    "Created {date}": "निर्मित {date}",
    "Unsaved changes": "असहेजे गए परिवर्तन",
    "Save changes to '{title}'?": "क्या '{title}' में परिवर्तन सहेजना चाहते हैं?",
    "Changes saved.": "परिवर्तन सहेजे गए।",
    "'{title}' moved to bin.": "'{title}' को बिन में ले जाया गया।",
    "Reader": "रीडर",
    'Pronounce "{word}"': '"{word}" का उच्चारण करें',
    'Add "{word}" to vocabulary': '"{word}" को शब्दावली में जोड़ें',
    "Read from here": "यहाँ से पढ़ें",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "स्रोत",
    "Added manually": "मैन्युअल रूप से जोड़ा गया",
    "From reader": "रीडर से",
    "Created at": "निर्मित तिथि",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "AI के साथ जोड़ें (मूल शब्द + सर्वोत्तम अनुवाद)",
    "Add to vocabulary as is": "शब्दावली में जैसा है वैसा ही जोड़ें",
    "Thinking…": "सोच रहा है…",
    "'{pair}' is already in your dictionary.": "'{pair}' आपकी शब्दावली में पहले से मौजूद है।",
    "{label} — {translation} · added": "{label} — {translation} · जोड़ा गया",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "क्लाउड सिंक",
    "Last sync": "अंतिम सिंक",
    "Pending": "लंबित",
    "never": "कभी नहीं",
    "just now": "अभी-अभी",
    "{n} min ago": "{n} मिनट पहले",
    "Connected": "कनेक्टेड",
    "Not connected": "कनेक्ट नहीं है",
    "change": "परिवर्तन",
    "changes": "परिवर्तन",
    "deletion": "हटाया गया",
    "deletions": "हटाए गए",
    "everything synced": "सब कुछ सिंक हो गया",
    "Initial sync has not completed yet.": "प्रारंभिक सिंक अभी पूरा नहीं हुआ है।",
    "Sync Now": "अभी सिंक करें",
    "Syncing…": "सिंक हो रहा है…",

    # Local-only promo state
    "{words} and {texts}": "{words} और {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "आपने यहां {items} सहेजे हैं। उन्हें सुरक्षित रखने और अपने सभी डिवाइसों पर अध्ययन करने के लिए साइन इन करें।",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "केवल स्थानीय — डिवाइसों में अपने शब्दों को सिंक करने के लिए साइन इन करें",
    "Sign in to sync across devices": "डिवाइसों में सिंक करने के लिए साइन इन करें",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "स्वागत हे",
    "Welcome to {app}": "{app} में आपका स्वागत है",
    "Sync across your devices": "अपने डिवाइसों में सिंक करें",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "अपनी शब्दावली को सुरक्षित रखने और हर डिवाइस पर इसका अध्ययन करने के लिए साइन इन करें।",
    "Automatic cloud backup": "स्वचालित क्लाउड बैकअप",
    "Your words follow you to every computer.":
        "आपके शब्द हर कंप्यूटर पर आपके साथ रहेंगे।",
    "Never lose your progress.": "अपनी प्रगति कभी न खोएं।",
    "Study anywhere": "कहीं भी अध्ययन करें",
    "Pick up right where you left off.":
        "ठीक वहीं से शुरू करें जहां आपने छोड़ा था।",
    "Your data is yours — sign in only to sync it.":
        "आपका डेटा आपका है — इसे केवल सिंक करने के लिए साइन इन करें।",
    "Sign in / Create account": "साइन इन करें / खाता बनाएं",
    "Continue on this device": "इस डिवाइस पर जारी रखें",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "प्लेबैक सेटिंग्स",
    "Previous word": "पिछला शब्द",
    "Next word": "अगला शब्द",
    "Stop playback": "प्लेबैक रोकें",
    "Pause between words": "शब्दों के बीच विराम",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "पढ़ने के लिए कुछ नहीं है।",
    "Previous sentence": "पिछला वाक्य",
    "Next sentence": "अगला वाक्य",
    "Reading speed": "पढ़ने की गति",
    "Sentence {n} / {total}": "वाक्य {n} / {total}",
    "buffering…": "बफरिंग जारी है…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "अवलोकन",
    "Learning status": "सीखने की स्थिति",
    "Activity": "गतिविधि",
    "Review activity": "समीक्षा गतिविधि",
    "Breakdown": "विवरण",
    "Total words": "कुल शब्द",
    "Mastered": "महारत हासिल",
    "In progress": "प्रगति पर है",
    "Languages": "भाषाएं",
    "Current streak": "वर्तमान स्ट्रिक",
    "Added this week": "इस सप्ताह जोड़े गए",
    "Definitions written": "लिखी गई परिभाषाएं",
    "Status distribution": "स्थिति विवरण",
    "Words added over time": "समय के साथ जोड़े गए शब्द",
    "Activity calendar": "गतिविधि कैलेंडर",
    "Reviews over time": "समय के साथ समीक्षाएं",
    "Review calendar": "समीक्षा कैलेंडर",
    "Most reviewed words": "सर्वाधिक समीक्षा किए गए शब्द",
    "Top language pairs": "शीर्ष भाषा जोड़ें",
    "Top tags": "शीर्ष टैग",
    "Reviewed this week": "इस सप्ताह समीक्षा की गई",
    "Total reviews": "कुल समीक्षाएं",
    "Review streak": "समीक्षा स्ट्रिक",
    "{pct}% of all words": "सभी शब्दों का {pct}%",
    "actively learning": "सक्रिय रूप से सीख रहे हैं",
    "{n} pairs": "{n} जोड़े",
    "best {n}d": "सर्वश्रेष्ठ {n} दिन",
    "{n} today": "आज {n}",
    "listens logged": "सुनना दर्ज किया गया",
    "keep it going": "इसे जारी रखें!",
    "Day": "दिन",
    "Week": "सप्ताह",
    "Month": "महीना",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "पाठ फ़ाइलें आयात करें",
    "Text files (*.txt);;All files (*)": "पाठ फ़ाइलें (*.txt);;सभी फ़ाइलें (*)",
    "Language of the imported text(s):": "आयातित पाठ की भाषा:",
    "Imported {count} text(s).": "{count} पाठ आयात किए गए।",
    "Some files could not be imported:": "कुछ फ़ाइलें आयात नहीं की जा सकीं:",
    "Import failed:\n{error}": "आयात विफल रहा:\n{error}",
    "Failed to save text:\n{error}": "पाठ सहेजने में विफल:\n{error}",
    "Failed to delete text:\n{error}": "पाठ हटाने में विफल:\n{error}",
    "Delete Text": "पाठ हटाएं",
    "Delete '{title}'?": "क्या '{title}' हटाना चाहते हैं?",
    "Unsupported language: {language}": "असमर्थित भाषा: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "असमर्थित भाषा: {lang}। सूची में से एक चुनें।",
    "(empty)": "(खाली)",
    "unsupported language": "असमर्थित भाषा",
    "unreadable text": "अपठनीय पाठ",
    "Skipped {n} {noun} ({reasons}).": "{n} {noun} छोड़े गए ({reasons})।",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "कुछ पाठ ज़ोर से नहीं पढ़ा जा सका — असमर्थित भाषा "
        "या अपठनीय अक्षर।",
    "Edit text": "पाठ संपादित करें",
    "Done editing": "संपादन पूर्ण",
    "Delete text": "पाठ हटाएं",
    "Save Changes": "परिवर्तन सहेजें",
    "Paper mode": "पेपर मोड",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "पाठ लिखने या पेस्ट करने के लिए '+' पर क्लिक करें, इंटरनेट से प्राप्त करने के लिए 'ग्लोब' पर,\n"
        "या 'शब्द' व्यू में शब्दों का चयन करें और अध्ययन पाठ जनरेट करने के लिए\n"
        "'पाठ' कार्रवाई का उपयोग करें।"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "चयनित भाषा में विकिपीडिया खोजता है। लेख लोड करने के लिए परिणाम पर क्लिक करें; इसे सरल बनाने के लिए 'मेरे स्तर के अनुसार ढालें' का उपयोग करें।"
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "चयनित भाषा के लिए समाचार फ़ीड। फ़ीड लोड करें, फिर उसका पूरा पाठ प्राप्त करने के लिए प्रविष्टि पर डबल-क्लिक करें। 'फ़ीड जोड़ें…' के साथ अपनी खुद की फ़ीड जोड़ें।"
    ),
    "Length:": "लंबाई:",
    "Search Wikipedia (in the selected language)…": "विकिपीडिया खोजें (चयनित भाषा में)…",
    "Double-click an entry to load its full text.": "इसका पूरा पाठ लोड करने के लिए किसी प्रविष्टि पर डबल-क्लिक करें।",
    "Working…": "काम जारी है…",
    "Show the {count} result(s) again": "{count} परिणाम फिर से दिखाएं",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "{ai} API key सेट नहीं है। इसे सेटिंग्स → अनुवाद और AI → AI में कॉन्फ़िगर करें।"
    ),
    "Generating with {ai}…": "{ai} के साथ जनरेट हो रहा है…",
    'Fetching "{title}"…': '"{title}" प्राप्त किया जा रहा है…',
    "(yours)": "(आपका)",
    "Fetching the full text…": "पूरा पाठ प्राप्त किया जा रहा है…",
    "Add feed": "फ़ीड जोड़ें",
    "Feed name:": "फ़ीड का नाम:",
    "Feed URL:": "फ़ीड URL:",
    "Failed to save the text.": "पाठ सहेजने में विफल।",
    "Failed to save the text: {error}": "पाठ सहेजने में विफल: {error}",
    "'{title}' saved.": "'{title}' सहेजा गया।",
    "(untitled)": "(बिना शीर्षक का)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "{ai} के साथ चयनित CEFR स्तर के लिए नीचे दिए गए पाठ को फिर से लिखें"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "लॉग निर्यात करें",
    "Activity Log": "गतिविधि लॉग",
    "Warnings & errors": "चेतावनी और त्रुटियां",
    "Errors only": "केवल त्रुटियां",
    "Find…": "खोजें…",
    "Open log folder": "लॉग फ़ोल्डर खोलें",
    "Export diagnostics": "निदान (Diagnostics) निर्यात करें",
    "Clear the log file? This cannot be undone.":
        "क्या लॉग फ़ाइल साफ़ करना चाहते हैं? इसे पूर्ववत नहीं किया जा सकता।",
    "Could not create the diagnostics file.":
        "निदान फ़ाइल नहीं बनाई जा सकी।",
    "Diagnostics saved to:\n{path}": "निदान फ़ाइल यहां सहेजी गई:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**समस्या का वर्णन करें**\n\n\n**पुनरावृत्ति के चरण**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nकृपया निदान फ़ाइल संलग्न करें:\n{path}\n",
    "Bug report: ": "बग रिपोर्ट: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "छोटा करें (Minimize)",
    "Maximize": "बड़ा करें (Maximize)",
    "Restore": "पुनर्स्थापित करें",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "नियंत्रण दिखाएं",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "कोई रंग नहीं",
    "None": "कोई नहीं",
    "Choose Color": "रंग चुनें",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "क्लाउड सिंक: निष्क्रिय",
    "Failed to open table:\n{error}": "तालिका खोलने में विफल:\n{error}",
    "Failed to save template:\n{error}": "टेम्पलेट सहेजने में विफल:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "दिखाएं / छिपाएं",
    "Excel options": "एक्सेल विकल्प",
    "CSV options": "CSV विकल्प",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "शीर्षलेख पंक्तियां फ़ाइल के शीर्ष पर लिखी जाती हैं — Anki जैसे आयात उपकरण "
        "उन्हें पढ़ते हैं (उदा. #separator:tab, #html:true)। "
        "स्वयं कॉलम के नाम नहीं लिखे जाते हैं।"
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "ऐप के फ़ॉन्ट फ़ोल्डर में एक .ttf फ़ाइल कॉपी करें और इसका उपयोग करें"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "केवल शब्दों को MP3 फ़ाइल में निर्यात करते समय उपयोग किया जाता है। "
        "आवाज़ को ऑडियो टैब में कॉन्फ़िगर किया गया है।"
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "वह आवाज़ जिसका उपयोग उन सभी जगहों पर किया जाता है जहाँ शब्द बोले जाते हैं: इन-ऐप 'ज़ोर से पढ़ें' "
        "और MP3 निर्यात। gTTS मुफ़्त है और इसे किसी सेट-अप की आवश्यकता नहीं है। Google Cloud TTS "
        "को एक सेवा-खाता JSON key की आवश्यकता होती है और प्रोजेक्ट पर बिलिंग सक्षम होना आवश्यक है।"
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "'ज़ोर से पढ़ें' में किसी शब्द को पूरी तरह से सुनना उसे न्यू → समीक्षा → सीखना → मास्टर के स्तर पर प्रन्नत करता है।"
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "सही हेडर और उदाहरण पंक्तियों के साथ एक तैयार .xlsx सहेजें"
    ),
    "Google Translate (free)": "Google Translate (मुफ़्त)",
    "Google Translate is free and needs no API key.": (
        "Google Translate मुफ़्त है और इसके लिए किसी API key की आवश्यकता नहीं है।"
    ),
    "Usage": "उपयोग",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "फ़ील्ड पर क्लिक करें और वांछित कुंजी संयोजन दबाएं — यह कहीं से भी क्लिपबोर्ड "
        "सामग्री के साथ 'शब्द जोड़ें' खोलता है। "
        "अक्षम करने के लिए खाली छोड़ें।"
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Wayland पर यह शॉर्टकट आपके डेस्कटॉप के साथ पंजीकृत है "
        "और सिस्टम कीबोर्ड सेटिंग्स में दिखाई देता है।"
    ),
    "Add Word hotkey": "शब्द जोड़ें हॉटकी",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "ग्लोबल ऐड-वर्ड हॉटकी इस वातावरण में उपलब्ध नहीं है। "
        "विकल्पों के लिए सेटिंग्स ▸ सिस्टम देखें।"
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "Wayland पर {sandbox} सैंडबॉक्स में ग्लोबल ऐड-वर्ड हॉटकी उपलब्ध नहीं है।"
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "इस Wayland डेस्कटॉप पर अभी तक ग्लोबल ऐड-वर्ड हॉटकी समर्थित नहीं है।"
    ),
    "To enable it, use any one of these:": "इसे सक्षम करने के लिए, इनमें से किसी एक का उपयोग करें:",
    "Log in to an X11 session instead of Wayland":
        "Wayland के बजाय X11 सत्र में लॉग इन करें",
    "Use a GNOME session — the global hotkey works there":
        "GNOME सत्र का उपयोग करें — ग्लोबल हॉटकी वहां काम करती है",
    "Install the AppImage version — it runs outside the sandbox":
        "AppImage संस्करण इंस्टॉल करें — यह सैंडबॉक्स के बाहर चलता है",
    "Download the AppImage": "AppImage डाउनलोड करें",
    "Add font…": "फ़ॉन्ट जोड़ें…",
    "TrueType fonts (*.ttf)": "TrueType फ़ॉन्ट (*.ttf)",
    "Could not copy the font file:\n{error}": "फ़ॉन्ट फ़ाइल कॉपी नहीं की जा सकी:\n{error}",
    "Save import template…": "आयात टेम्पलेट सहेजें…",
    "Excel files (*.xlsx)": "एक्सेल फ़ाइलें (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "टेम्पलेट यहां सहेजा गया:\n{path}\n\n"
        "इसे अपने शब्दों से भरें (उदाहरण पंक्तियों को बदलें) "
        "और ऐप मेनू → डेटाबेस में एक्सेल आयात करें के माध्यम से इसे आयात करें।"
    ),
    "Could not save the template:\n{error}": "टेम्पलेट सहेजा नहीं जा सका:\n{error}",
    "Background image": "पृष्ठभूमि छवि",
    "Images (*.png *.jpg *.jpeg)": "छवियां (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSON फ़ाइलें (*.json)",
    "Connection successful! ✅": "कनेक्शन सफल! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "कनेक्ट नहीं हो सका। URL/key और अपना इंटरनेट कनेक्शन जांचें।"
    ),
    "Connection test failed:\n{error}": "कनेक्शन परीक्षण विफल रहा:\n{error}",
    "{count} / {limit} characters this period": "इस अवधि में {count} / {limit} अक्षर",
    "{count} characters used": "{count} अक्षर उपयोग किए गए",
    "Autostart": "ऑटोस्टार्ट",
    "Could not update autostart entry:\n{error}": "ऑटोस्टार्ट प्रविष्टि को अद्यतन नहीं किया जा सका:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS चुना गया है लेकिन {problem}\n\n"
        "जब तक इसे ठीक नहीं किया जाता, ऑडियो gTTS पर वापस चला जाएगा।"
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "शब्द",
    "words": "शब्द",
    "words (genitive)": "शब्द",
    "text": "पाठ",
    "texts": "पाठ",
    "texts (genitive)": "पाठ",
    "tag": "टैग",
    "tags": "टैग",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "अनुवाद करें",
    "AI": "AI",
    "Save As": "रूप में सहेजें (Save As)",
    "Save Audio As": "ऑडियो इस रूप में सहेजें",
    "Save PDF As": "PDF इस रूप में सहेजें",
    "Added": "जोड़ा गया",
    "Updated": "अद्यतन किया गया",
    "Failed": "विफल",
    "Checking…": "जांच हो रही है…",
    "Cleanup": "सफ़ाई",
    "Permanent Delete": "स्थायी रूप से हटाएं",
    "No word": "कोई शब्द नहीं",
    "Category": "श्रेणी",
    "Bin": "रीसायकल बिन",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "सभी टैग",
    "Filter by tag — {tag}": "टैग द्वारा फ़िल्टर करें — {tag}",
    "(showing first {n})": "(पहले {n} दिखा रहा है)",
    "Texts: {total}": "पाठ: {total}",
    "Deleted with {n} error(s).": "{n} त्रुटि(यों) के साथ हटाया गया।",
    "Failed to update: {error}": "अद्यतन करने में विफल: {error}",
    "Failed to export:\n{error}": "निर्यात करने में विफल:\n{error}",
    "Failed to export PDF:\n{error}": "PDF निर्यात करने में विफल:\n{error}",
    "Failed to export TXT:\n{error}": "TXT निर्यात करने में विफल:\n{error}",
    "PDF saved to {path}": "PDF {path} पर सहेजा गया",
    "TXT file saved to {path}": "TXT फ़ाइल {path} पर सहेजी गई",
    "Template saved to {path}": "टेम्पलेट {path} पर सहेजा गया",
    "{format} file saved to {path}": "{format} फ़ाइल {path} पर सहेजी गई",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "इसके बजाय gTTS का उपयोग किया जा रहा है — {problem}\nइसे सेटिंग्स → सस्वर वाचन → ऑडियो में ठीक करें।"
    ),
    "Failed to load the database:": "डेटाबेस लोड करने में विफल:",
    "{selected} of {total} selected": "{total} में से {selected} चयनित",
    "Collapse sidebar": "साइडबार समेटें",
    "Expand sidebar": "साइडबार विस्तार करें",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "{when} सहेजा गया · {summary}",
    "the version from {date}": "{date} का संस्करण",
    "Sorry, that version could not be restored:\n{error}": (
        "क्षमा करें, वह संस्करण पुनर्प्राप्त नहीं किया जा सका:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "क्षमा करें, वह संस्करण हटाया नहीं जा सका:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "क्या {count} आइटम पुनर्प्राप्त करना चाहते हैं?",
    "Restored {count} item(s).": "{count} आइटम पुनर्प्राप्त किए गए।",
    "Select item(s) to restore.": "पुनर्प्राप्त करने के लिए आइटम चुनें।",
    "Permanently deleted {count} item(s).": "{count} आइटम स्थायी रूप से हटा दिए गए।",
    "Select item(s) to delete permanently.": "स्थायी रूप से हटाने के लिए आइटम चुनें।",
    "No items older than {n} days found.": "{n} दिनों से पुराने कोई आइटम नहीं मिले।",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "क्या {days} दिनों से अधिक समय पहले हटाए गए आइटमों को स्थायी रूप से हटाना चाहते हैं?\n\n"
        "इसे पूर्ववत नहीं किया जा सकता!"
    ),
    "Permanently deleted {count} old item(s).": "{count} पुराने आइटम स्थायी रूप से हटा दिए गए।",
    "Failed to load deleted items:\n{error}": "हटाए गए आइटमों को लोड करने में विफल:\n{error}",
    "Failed to count old items:\n{error}": "पुराने आइटमों की गिनती करने में विफल:\n{error}",
    "Failed to cleanup:\n{error}": "सफ़ाई करने में विफल:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "एक्सेल आयात करें",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "अपेक्षित कॉलम: Language1, Language2, Word1, Word2 — हेडर पंक्ति में इस नाम से, "
        "या बिना हेडर के उसी क्रम में पहले चार कॉलम। "
        "एक तैयार टेम्पलेट ऐप मेनू → आयात टेम्पलेट सहेजें में उपलब्ध है।"
    ),
    "All ({n})": "सभी ({n})",
    "To add ({n})": "जोड़ने के लिए ({n})",
    "To update ({n})": "अद्यतन करने के लिए ({n})",
    "Skipped ({n})": "छोड़े गए ({n})",
    "Unrecognized ({n})": "अपरिचित ({n})",
    " · {n} with unrecognized language": " · {n} अपरिचित भाषा के साथ",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} पंक्तियां: {add} नई · {update} अद्यतन · {skip} छोड़े गए"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "प्रस्तावित परिवर्तनों की समीक्षा करें, फिर चयनित पंक्तियों को आयात करें।"
    ),
    "Nothing to import — no new or changed entries found.": (
        "आयात करने के लिए कुछ नहीं है — कोई नई या परिवर्तित प्रविष्टियां नहीं मिलीं।"
    ),
    "Analyzing file…": "फ़ाइल का विश्लेषण किया जा रहा है…",
    "Could not read the Excel file — see the activity log.": (
        "एक्सेल फ़ाइल नहीं पढ़ी जा सकी — गतिविधि लॉग देखें।"
    ),
    "Analysis failed — see the activity log.": "विश्लेषण विफल रहा — गतिविधि लॉग देखें।",
    "Import failed": "आयात विफल रहा",
    "Import failed — see the activity log.": "आयात विफल रहा — गतिविधि लॉग देखें।",
    "Importing…": "आयात हो रहा है…",
    "Importing {count} item(s)…": "{count} आइटम आयात हो रहे हैं…",
    "Import {count} Item(s)": "{count} आइटम आयात करें",
    "Import finished:": "आयात समाप्त:",
    "Backup failed — see the activity log.": "बैकअप विफल रहा — गतिविधि लॉग देखें।",
    "{n} added": "{n} जोड़े गए",
    "{n} updated": "{n} अद्यतन किए गए",
    "{n} failed": "{n} विफल",
    "{n} failed.": "{n} विफल।",
    "Export Import Log": "आयात लॉग निर्यात करें",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "परिभाषा — {word}",
    "Failed to save definition:\n{error}": "परिभाषा सहेजने में विफल:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "संपादित करें — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "शब्द सहेजने में विफल:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "प्रत्येक चयनित शब्द के साथ चयनित टैग संलग्न करें"
    ),
    "Failed to add tag:\n{error}": "टैग जोड़ने में विफल:\n{error}",
    "Failed to apply tags:\n{error}": "टैग लागू करने में विफल:\n{error}",
    "Failed to remove tags:\n{error}": "टैग हटाने में विफल:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "नीचे दिए गए भाषा, स्तर और विषय फ़ील्ड का उपयोग करके AI के साथ एक पाठ जनरेट करता है। "
        "एक विषय चिप चुनें या अपना खुद का टाइप करें।"
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "{ai} के साथ {count} शब्द(शब्दों) से एक {language} पाठ जनरेट किया जा रहा है:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "नीचे दिए गए संपादक में एक पाठ टाइप करें या पेस्ट करें, इसे एक शीर्षक दें, "
        "भाषा सेट करें — फिर सहेजें।"
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "किसी भी वेब पेज से पढ़ने योग्य लेख पाठ निकालता है। "
        "लॉगिन के पीछे वाले पेज या पूरी तरह से जावास्क्रिप्ट के साथ बने पेज काम नहीं कर सकते हैं।"
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    "View definition (double-click)": "परिभाषा देखें (डबल-क्लिक करें)",
    "Read selected words aloud": "चयनित शब्दों को ज़ोर से पढ़ें",
    "Toggle favorite": "पसंदीदा चालू/बंद करें",
    "Add / remove tags": "टैग जोड़ें / हटाएं",
    "Edit word": "शब्द संपादित करें",
    "Copy words": "शब्द कॉपी करें",
    "Generate text from selection": "चयन से पाठ जनरेट करें",

    "PDF files (*.pdf)": "PDF फ़ाइलें (*.pdf)",
    "Excel files (*.xlsx *.xls)": "एक्सेल फ़ाइलें (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSV फ़ाइलें (*.csv)",
    "Text files (*.txt)": "पाठ फ़ाइलें (*.txt)",
    "MP3 files (*.mp3)": "MP3 फ़ाइलें (*.mp3)",
    "Open Excel Table": "एक्सेल तालिका खोलें",
    "Save Import Template": "आयात टेम्पलेट सहेजें",

    "Cloud sync": "क्लाउड सिंक",
    "Not connected. Check internet or credentials": "कनेक्ट नहीं है। इंटरनेट या क्रेडेंशियल जांचें",
    "Syncing with cloud…": "क्लाउड के साथ सिंक हो रहा है…",
    "Sync completed successfully": "सिंक सफलतापूर्वक पूरा हुआ",
    "Sync enabled but not connected. Check settings.": "सिंक सक्षम है लेकिन कनेक्ट नहीं है। सेटिंग्स जांचें।",
    "idle": "निष्क्रिय",
    "syncing": "सिंक हो रहा है",
    "success": "सफल",
    "error": "त्रुटि",

    "No data yet": "अभी कोई डेटा नहीं है",
    "No activity yet": "अभी कोई गतिविधि नहीं है",
    "Not enough activity yet": "अभी पर्याप्त गतिविधि नहीं है",

    "APIs": "APIs",
    "Audio (MP3)": "ऑडियो (MP3)",
    "Sync": "सिंक",

    "OpenAI API key (.env)": "OpenAI API key (.env)",
    "Google API key (.env)": "Google API key (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'प्रति उपयोग बिल — <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a> पर एक key प्राप्त करें। मॉडल: gpt-4o-mini, gpt-4o… API उपयोग — देखें <a href="https://platform.openai.com/usage">डैशबोर्ड</a>।',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'मुफ़्त स्तर उपलब्ध है — <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a> पर एक key प्राप्त करें। मॉडल: gemini-2.5-flash… API उपयोग — देखें <a href="https://aistudio.google.com/usage">AI Studio</a>।',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        '<a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a> पर एक key प्राप्त करें।',

    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li><b>Language1, Language2, Word1, Word2</b> कॉलम के साथ एक एक्सेल फ़ाइल तैयार करें।</li><li>ऐप मेनू खोलें → <i>डेटाबेस में एक्सेल आयात करें…</i> और फ़ाइल चुनें।</li><li>समीक्षा करें और <i>आयात करें</i> पर क्लिक करें।</li></ol>",

    "created by": "द्वारा निर्मित",
    "Version": "संस्करण",
    "Build": "बिल्ड",
    "Your personal vocabulary companion": "आपका व्यक्तिगत शब्दावली साथी",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "भाषाओं में शब्दावली बनाएं, अध्ययन करें और याद रखें — क्लाउड सिंक, AI-सहायता प्राप्त परिभाषाओं, अनुवादों, टेक्स्ट-टू-स्पीच और लचीले निर्यात के साथ।",
    "Source code": "स्रोत कोड",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "क्लाउड सिंक, AI परिभाषाओं, अनुवादों, टेक्स्ट-टू-स्पीच और निर्यात विकल्पों के साथ आपका व्यक्तिगत शब्दावली साथी।",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "GNU एफ़रो जनरल पब्लिक लाइसेंस v3.0 के तहत लाइसेंस प्राप्त।",
    "Found a bug or have an idea?": "कोई बग मिला या कोई विचार है?",
    "Report an issue": "समस्या की रिपोर्ट करें",
    "What would you like to report?": "आप किस चीज़ की रिपोर्ट करना चाहेंगे?",
    "A bug or technical problem": "एक बग या तकनीकी समस्या",
    "Creates a report with app diagnostics to send to the developers.":
        "डेवलपर्स को भेजने के लिए ऐप निदान के साथ एक रिपोर्ट बनाता है।",
    "Inappropriate AI-generated content": "अनुचित AI-जनरेट की गई सामग्री",
    "Report a definition, text, or translation the AI produced.":
        "AI द्वारा निर्मित परिभाषा, पाठ या अनुवाद की रिपोर्ट करें।",
    "Report: inappropriate AI-generated content":
        "रिपोर्ट: अनुचित AI-जनरेट की गई सामग्री",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "कृपया उस AI-जनरेट की गई सामग्री का वर्णन करें जिसकी आप रिपोर्ट कर रहे हैं।\n\n"
        "यह कहां दिखाई दिया (परिभाषा / जनरेट किया गया पाठ / शब्द अनुवाद):\n"
        "संबंधित शब्द या पाठ:\n"
        "यह अनुचित क्यों है:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "अनुचित AI-जनरेट की गई सामग्री की रिपोर्ट करने के लिए, कृपया हमें {email} पर ईमेल करें।",

    "Support": "समर्थन करें",
    "Support Lingueez": "Lingueez का समर्थन करें",
    "Lingueez is free and open-source.": "Lingueez मुफ़्त और ओपन-सोर्स है।",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "यदि आप Lingueez का आनंद लेते हैं, तो एक बार का योगदान क्लाउड सिंक सर्वर के खर्चों को कवर करने में मदद करता है। हर सुविधा मुफ़्त रहती है।",
    "Support Lingueez's development": "Lingueez के विकास का समर्थन करें",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Stripe विकल्प एक बार के लिए है — कोई सदस्यता नहीं। भुगतानों को Stripe या GitHub द्वारा सुरक्षित रूप से संभाला जाता है।",

    "Updates": "अपडेट",
    "Check for updates": "अपडेट के लिए जांचें",
    "You're up to date.": "आपका ऐप अप-टू-डेट है।",
    "Update available": "अपडेट उपलब्ध है",
    "Update available — v{version}": "अपडेट उपलब्ध है — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} उपलब्ध है — आपके पास {current} है।",
    "Skip this version": "इस संस्करण को छोड़ें",
    "Later": "बाद में",
    "Download": "डाउनलोड करें",
    "Check for updates on startup": "स्टार्टअप पर अपडेट के लिए जांचें",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "नए संस्करण के लिए दिन में एक बार जांच करता है और आपको सूचित करता है; "
        "कुछ भी स्वचालित रूप से डाउनलोड या इंस्टॉल नहीं होता है।",

    "in": "इंच",
    " s": " सेकंड",

    "New": "नया",
    "To Learn": "सीखना है",
    "Reviewing": "समीक्षा जारी",
    "Ignored": "अनदेखा किया गया",
    "Undo": "पूर्ववत करें",
    "Restored": "पुनर्स्थापित",
    "Ignore word": "शब्द अनदेखा करें",
    "Ignore this word": "इस शब्द को अनदेखा करें",
    "Already ignored.": "पहले से अनदेखा किया गया है।",
    "{count} word(s) won't come up in practice.": "{count} शब्द अब अभ्यास में नहीं आएंगे।",
    "'{word}' is back in rotation": "'{word}' फिर से अभ्यास में है",
    "'{word}' won't come up again": "'{word}' अब नहीं आएगा",
    "Mark for relearning": "फिर से सीखने के लिए चिह्नित करें",
    "Forgot this word — move it to To Learn": "भूला हुआ शब्द — 'सीखना है' में ले जाएँ",
    "'{word}' is queued to learn again": "'{word}' फिर से सीखने की सूची में है",
    "{count} word(s) queued to learn again.": "{count} शब्द फिर से सीखने की सूची में हैं।",
    "Nothing here to relearn yet.": "यहाँ अभी फिर से सीखने के लिए कुछ नहीं है।",

    "Compact": "संक्षिप्त",
    "Normal": "सामान्य",
    "Comfortable": "आरामदायक",
    "Spacious": "विस्तृत",

    "English": "अंग्रेज़ी",
    "German": "जर्मन",
    "Spanish": "स्पैनिश",
    "Ukrainian": "यूक्रेनी",
    "French": "फ्रेंच",
    "Italian": "इतालवी",
    "Portuguese": "पुर्तगाली",
    "Russian": "रूसी",
    "Greek": "ग्रीक",
    "Arabic": "अरबी",
    "Bengali": "बंगाली",
    "Cantonese": "कैंटोनीज़",
    "Hindi": "हिन्दी",
    "Japanese": "जापानी",
    "Korean": "कोरियाई",
    "Mandarin": "मंदारिन",
    "Polish": "पोलिश",
    "Turkish": "तुर्की",
    "Vietnamese": "वियतनामी",
    "Afrikaans": "अफ़्रीकी",
    "Albanian": "अल्बानियाई",
    "Amharic": "अम्हारिरक",
    "Armenian": "आर्मीनियाई",
    "Azerbaijani": "अज़रबैजानी",
    "Basque": "बास्क",
    "Belarusian": "बेलारूसी",
    "Bosnian": "बोस्नियाई",
    "Bulgarian": "बुल्गारियाई",
    "Catalan": "कातालान",
    "Cebuano": "सिबुआनो",
    "Chichewa": "चिचेवा",
    "Chinese": "चीनी",
    "Croatian": "क्रोएशियाई",
    "Czech": "चेक",
    "Danish": "डेविश",
    "Dutch": "डच",
    "Estonian": "एस्टोनियाई",
    "Filipino": "फिलीपिनो",
    "Finnish": "फिनिश",
    "Galician": "गैलिशियन",
    "Georgian": "जॉर्जियाई",
    "Gujarati": "गुजराती",
    "Haitian Creole": "हैतीयाई क्रियोल",
    "Hausa": "होउसा",
    "Hawaiian": "हवाईयन",
    "Hebrew": "हिब्रू",
    "Hmong": "ह्मोंग",
    "Hungarian": "हंगेरियन",
    "Icelandic": "आइसलैंडिक",
    "Igbo": "इग्बो",
    "Indonesian": "इंडोनेशियाई",
    "Irish": "आइरिश",
    "Javanese": "जावानीस",
    "Kannada": "कन्नड़",
    "Kazakh": "कज़ाख",
    "Khmer": "खमेर",
    "Kinyarwanda": "किन्यारवांडा",
    "Kyrgyz": "किर्गीज़",
    "Lao": "लाओ",
    "Latin": "लैटिन",
    "Latvian": "लातवियाई",
    "Lithuanian": "लिथुआनियाई",
    "Luxembourgish": "लक्ज़मबर्गिश",
    "Macedonian": "मैसिडोनियाई",
    "Malagasy": "मालागासी",
    "Malay": "मलय",
    "Malayalam": "मलयलम",
    "Maltese": "माल्टीज़",
    "Maori": "माओरी",
    "Marathi": "मराठी",
    "Mongolian": "मंगोलियाई",
    "Myanmar (Burmese)": "म्यांमार (बर्मी)",
    "Nepali": "नेपाली",
    "Norwegian": "नार्वेजियन",
    "Odia": "ओडिया",
    "Pashto": "पश्तो",
    "Persian": "फारसी",
    "Punjabi": "पंजाबी",
    "Romanian": "रोमानियाई",
    "Samoan": "समोअन",
    "Scots Gaelic": "स्कॉट्स गेलिक",
    "Serbian": "सर्बियाई",
    "Sesotho": "सेसोथो",
    "Shona": "शोना",
    "Sindhi": "सिंधी",
    "Sinhala": "सिंहल",
    "Slovak": "स्लोवाक",
    "Slovenian": "स्लोवेनियाई",
    "Somali": "सोमाली",
    "Sundanese": "सुंदानी",
    "Swahili": "स्वाहिली",
    "Swedish": "स्वीडिश",
    "Tajik": "ताजिक",
    "Tamil": "तमिल",
    "Tatar": "तातार",
    "Telugu": "तेलुगु",
    "Thai": "थाई",
    "Turkmen": "तुर्कमेन",
    "Urdu": "उर्दू",
    "Uyghur": "उईघुर",
    "Uzbek": "उज़्बेक",
    "Welsh": "वेल्श",
    "Xhosa": "होसा",
    "Yiddish": "यिडिश",
    "Yoruba": "योरूबा",
    "Zulu": "ज़ुलु",

    # --- Onboarding tour ---
    "Back": "पीछे",
    "Next": "आगे",
    "Done": "पूर्ण",
    "Show Tour": "टूर दिखाएं",
    "Step {n} of {total}": "चरण {total} में से {n}",
    "Your library": "आपकी लाइब्रेरी",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "इस साइडबार से अपने शब्दों, पाठों और आंकड़ों के बीच स्विच करें।",
    "Add a word": "एक शब्द जोड़ें",
    "Find anything": "कुछ भी खोजें",
    "Search across your words, translations and tags as you type.":
        "जैसे ही आप टाइप करते हैं, अपने शब्दों, अनुवादों और टैग में खोजें।",
    "Add a new word here — its translation can be fetched automatically.":
        "यहां एक नया शब्द जोड़ें — इसका अनुवाद स्वचालित रूप से प्राप्त किया जा सकता है।",
    "Listen and learn": "सुनें और सीखें",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "शब्दों का चयन करें और उन्हें ज़ोर से सुनने के लिए 'पढ़ें' दबाएं। बार-बार सुनने "
        "से प्रत्येक शब्द नया से समीक्षा, सीखना और अंततः मास्टर में पदोन्नत होता है।",
    "Generate a text": "एक पाठ जनरेट करें",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "चयनित शब्दों को एक छोटी AI-लिखित कहानी में बदलें — "
        "संदर्भ में आपकी शब्दावली।",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "आपकी शब्दावली डिवाइसों में सिंक रहती है। स्थिति देखने या "
        "अभी सिंक करने के लिए क्लिक करें।",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "सेटिंग्स से क्लाउड सिंक सक्षम करें, भाषा बदलें, रूप-रंग बदलें और बहुत कुछ।",

    # --- Texts tour ---
    "Add texts": "पाठ जोड़ें",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "एक पाठ लिखें या पेस्ट करें, इंटरनेट से एक प्राप्त करें "
        "(AI / विकिपीडिया / URL / RSS), या .txt फ़ाइलें आयात करें।",
    "Your texts": "आपके पाठ",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "अपने सहेजे गए पाठ ब्राउज़ करें और उन्हें भाषा, स्तर या विषय के आधार पर फ़िल्टर करें।",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "किसी भी पाठ को ज़ोर से सुनें — और पढ़ते समय उसका अनुवाद देखने या अपनी शब्दावली में जोड़ने के लिए "
        "किसी शब्द पर क्लिक करें।",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "साथ-साथ एक समानांतर अनुवाद दिखाएं; इसके बगल में दिए गए तीर से "
        "भाषा चुनें।",
    "Reading modes": "पढ़ने के मोड",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "फ़ोकस मोड सूची को छिपाता है, पेपर मोड पृष्ठभूमि बदलता है, "
        "और संपादन आपको पाठ में बदलाव करने देता है।",

    # --- Flashcards tour ---
    "Choose your deck": "अपनी डेक चुनें",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "चुनें कि डेक में क्या जाता है — समीक्षा के लिए देय कार्ड, "
        "आपके वर्तमान फ़िल्टर के शब्द, नवीनतम जोड़, "
        "या एक हाथ से चुनी गई पसंद।",
    "Shape the session": "सत्र को आकार दें",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "समीक्षा करने के लिए कार्डों की संख्या सेट करें, उनके क्रम को फेरबदल (shuffle) करें, "
        "और प्रत्येक कार्ड के दिखाई देने और पलटने पर उसका उच्चारण करवाएं।",
    "Preview the deck": "डेक का पूर्वावलोकन करें",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "सटीक कार्ड जो आपके सत्र में होंगे। इसकी परिभाषा पढ़ने या "
        "संपादित करने के लिए किसी टाइल पर क्लिक करें, या शब्द सुनने के लिए स्पीकर पर क्लिक करें।",
    "Review and grade": "समीक्षा करें और ग्रेड दें",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "प्रत्येक कार्ड को पलटें और ग्रेड दें कि आप इसे कितना जानते हैं — कठिन, "
        "अच्छा या आसान। स्पेस-की पलटने के लिए, 1-3 ग्रेड देने के लिए।",
    "Or just listen": "या बस सुनें",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "प्ले डेक सत्र को ऑडियो में बदल देता है — आवाज़ के साथ तालमेल बिठाकर कार्ड आगे बढ़ते "
        "और पलटते हैं। स्वयं कार्ड ग्रेड करने के लिए किसी भी समय रोकें।",

    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "आपकी शब्दावली एक नज़र में — कुल, महारत हासिल शब्द, "
        "भाषाएं और आपकी वर्तमान स्ट्रिक।",
    "See how your vocabulary has grown over time.":
        "देखें कि समय के साथ आपकी शब्दावली कैसे बढ़ी है।",
    "Track how much you've reviewed over time.":
        "ट्रैक करें कि आपने समय के साथ कितना समीक्षा किया है।",

    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "नमूना: शहर में एक सैर",
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
        "सुबह उज्ज्वल थी और सड़कें शांत थीं। एक युवती पुरानी सड़क पर धीरे-धीरे चल रही थी, "
        "ऊंचे मकानों और अभी-अभी खुल रही छोटी दुकानों को देख रही थी। वह कुछ ताज़ी "
        "ब्रेड और एक कप कॉफ़ी खरीदने के लिए रुकी, फिर पार्क की ओर वर्ग को पार किया। "
        "नदी के पास बच्चे खेल रहे थे जबकि उनके माता-पिता पास के बेंचों पर बात कर रहे थे। "
        "वह एक बड़े पेड़ के नीचे बैठ गई, अपनी किताब खोली और पढ़ने लगी। कहानी एक ऐसे यात्री के बारे में थी "
        "जो एक पुराने दोस्त की तलाश में पहाड़ों को पार कर गया था जिसे उसने कई वर्षों से नहीं देखा था। "
        "कुछ देर बाद उसने ऊपर देखा, नावों को धीरे-धीरे नदी में बहते देखा और पक्षियों को छत के ऊपर "
        "ऊंचे गोल चक्कर काटते देखा। पास में कहीं एक गली का संगीतकार बजाने लगा, और कोमल स्वर "
        "उसके विचारों का पीछा करने लगे। यह एक शांत और खुशहाल सुबह थी, जिस तरह की वह सबसे ज्यादा पसंद करती थी।",
    "Demo": "डेमो",

    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "अमान्य OpenAI API key। इसे सेटिंग्स → अनुवाद और AI → AI → OpenAI में जांचें।",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "आपके OpenAI खाते में क्रेडिट समाप्त हो गया है। platform.openai.com/account/billing पर क्रेडिट जोड़ें, "
        "या AI प्रदाता को सेटिंग्स → अनुवाद और AI → AI में Gemini पर स्विच करें।",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI दर सीमा समाप्त हो गई। कुछ देर प्रतीक्षा करें और पुनः प्रयास करें।",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "अज्ञात OpenAI मॉडल। सेटिंग्स → अनुवाद और AI → AI → OpenAI में मॉडल का नाम जांचें।",
    "Could not reach OpenAI. Check your internet connection.":
        "OpenAI तक नहीं पहुंचा जा सका। अपना इंटरनेट कनेक्शन जांचें।",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Gemini कोटा समाप्त हो गया। मुफ़्त स्तर दैनिक रूप से रीसेट होता है; प्रतीक्षा करें, "
        "या aistudio.google.com/app/apikey पर एक नई key बनाएं।",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "अमान्य Google API key। इसे सेटिंग्स → अनुवाद और AI → AI → Gemini में जांचें।",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "अज्ञात Gemini मॉडल। सेटिंग्स → अनुवाद और AI → AI → Gemini में मॉडल नाम जांचें।",

    # --- Words empty state ---
    "Your vocabulary journey starts here": "आपकी शब्दावली यात्रा यहां से शुरू होती है",
    "Add your first word — its translation can be fetched automatically.":
        "अपना पहला शब्द जोड़ें — इसका अनुवाद स्वचालित रूप से प्राप्त किया जा सकता है।",
    "Add your first word": "अपना पहला शब्द जोड़ें",
    "Take the tour": "टूर लें",
    "No matching words": "कोई मेल खाते शब्द नहीं हैं",
    "Try a different search or filter.": "अलग खोज या फ़िल्टर का प्रयास करें।",
    "Clear filters": "फ़िल्टर साफ़ करें",

    # --- Texts empty state ---
    "Your reading library starts here": "आपकी पठन लाइब्रेरी यहां से शुरू होती है",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "पढ़ने के लिए एक पाठ जोड़ें — अपना खुद का लिखें या पेस्ट करें, इंटरनेट से एक प्राप्त करें, "
        "या एक .txt फ़ाइल आयात करें।",
    "Add a text": "एक पाठ जोड़ें",
    "Fetch from the Internet": "इंटरनेट से प्राप्त करें",
    "Import .txt": ".txt आयात करें",

    # demo text-list stub titles
    "My first story": "मेरी पहली कहानी",
    "A news article": "एक समाचार लेख",
    "A short poem": "एक छोटी कविता",
    "Travel notes": "यात्रा नोट्स",

    # demo text-list stub first sentences (shown as the list snippet)
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "एक समय की बात है, समुद्र के किनारे एक छोटे से गाँव में, "
        "एक जिज्ञासु युवा लोमड़ी रहती थी।",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "शोधकर्ताओं ने यह अध्ययन करने का एक नया तरीका खोजा है कि "
        "सदियों से भाषाएं कैसे बदलती और बढ़ती हैं।",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "हवा पतझड़ के पेड़ों के माध्यम से धीरे-धीरे चलती है, "
        "पुराने और आधे-भूल गए गानों को साथ ले जाती है।",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "पहला दिन: हम देर रात शहर पहुंचे, और "
        "सड़कें अभी भी गर्म रोशनी से भरी थीं।",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "किसी अन्य डिवाइस पर हटाए गए आइटम",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "जब यह डिवाइस ऑफ़लाइन था, तो आपके अन्य डिवाइसों पर यहाँ के {n} आइटम हटा दिए गए थे। "
        "उन्हें क्लाउड में रखें, या इस डिवाइस से हटा दें?",
    "(untitled)": "(बिना शीर्षक का)",
    "[Text] {title}": "[पाठ] {title}",
    "Remove from this device": "इस डिवाइस से हटाएं",
    "Decide later": "बाद में निर्णय लें",
    "Keep & upload": "रखें और अपलोड करें",
    "Not now": "अभी नहीं",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "ऑफ़लाइन प्रोफ़ाइल के लिए एक नाम दर्ज करें।",
    "You can keep up to {max} offline profiles. Remove one to add another.": "आप {max} ऑफ़लाइन प्रोफ़ाइल तक रख सकते हैं। दूसरा जोड़ने के लिए एक को हटाएं।",
    "New offline profile": "नई ऑफ़लाइन प्रोफ़ाइल",
    "Profile name:": "प्रोफ़ाइल का नाम:",
    "Offline profile": "ऑफ़लाइन प्रोफ़ाइल",
    "Rename offline profile": "ऑफ़लाइन प्रोफ़ाइल का नाम बदलें",
    "Offline profiles": "ऑफ़लाइन प्रोफ़ाइल",
    "Add offline profile…": "ऑफ़लाइन प्रोफ़ाइल जोड़ें…",
    "Profile actions": "प्रोफ़ाइल कार्रवाइयां",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "उनके अपने डेटाबेस के साथ अलग, केवल-डिवाइस लाइब्रेरी। वे कभी सिंक नहीं होते और किसी साइन-इन की आवश्यकता नहीं होती है।",
    "Default (local)": "डिफ़ॉल्ट (स्थानीय)",
    "Rename": "नाम बदलें",
    "Delete offline profile": "ऑफ़लाइन प्रोफ़ाइल हटाएं",
    "Enable cloud sync…": "क्लाउड सिंक सक्षम करें…",
    "Could not create the profile.": "प्रोफ़ाइल नहीं बनाई जा सकी।",
    "Created and switched to “{name}”.": "बनाया गया और “{name}” पर स्विच किया गया।",
    "Deleted “{name}”.": "“{name}” हटा दिया गया।",
    "Untitled profile": "बिना शीर्षक वाली प्रोफ़ाइल",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "क्या ऑफ़लाइन प्रोफ़ाइल “{name}” को स्थायी रूप से हटाना चाहते हैं? इसके शब्द और पाठ केवल इस डिवाइस पर मौजूद हैं — कोई क्लाउड कॉपी नहीं है। डेटाबेस को पहले बैकअप फ़ोल्डर में संग्रहीत किया जाता है, लेकिन इसे ऐप में पूर्ववत नहीं किया जा सकता है।",
    "this profile": "यह प्रोफ़ाइल",
    "Connect to the internet to merge this profile into your account.": "इस प्रोफ़ाइल को अपने खाते में मिलाने के लिए इंटरनेट से कनेक्ट करें।",
    "Enable cloud sync for this profile": "इस प्रोफ़ाइल के लिए क्लाउड सिंक सक्षम करें",
    "Continue": "जारी रखें",
    "Upload words": "शब्द अपलोड करें",
    "Upload texts": "पाठ अपलोड करें",
    "Upload & sync": "अपलोड करें और सिंक करें",
    "Could not upload this profile. Your data is unchanged.": "इस प्रोफ़ाइल को अपलोड नहीं किया जा सका। आपका डेटा अपरिवर्तित है।",
    "“{name}” is now synced to your account.": "“{name}” अब आपके खाते में सिंक हो गया है।",
    "Everything in this profile is already in your account.": "इस प्रोफ़ाइल की हर चीज़ पहले से ही आपके खाते में है।",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "“{name}” का बैकअप लेने और इसे अपने सभी डिवाइसों पर सिंक करने के लिए साइन इन करें या एक खाता बनाएं। इस प्रोफ़ाइल के शब्द और पाठ अपलोड किए जाते हैं और यह इस डिवाइस पर आपका सिंक किया गया खाता बन जाता है।",
    "Upload “{name}” to your account": "अपने खाते में “{name}” अपलोड करें",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "आपकी प्रोफ़ाइल इस डिवाइस पर सिंक किया गया खाता “{who}” बन जाती है और क्लाउड पर अपलोड हो जाती है।",
    "Merge “{name}” into your account": "अपने खाते में “{name}” को मिलाएं",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "इस खाते का इस डिवाइस पर पहले से ही डेटा है। आपकी प्रोफ़ाइल के वे शब्द और पाठ जो पहले से मौजूद नहीं हैं, इसमें जोड़ दिए जाएंगे — कुछ भी ओवरराइट नहीं किया जाएगा। “{name}” को फिर बैकअप फ़ोल्डर में संग्रहीत करके हटा दिया जाता है।",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "इस प्रोफ़ाइल में {items} हैं, जो केवल इस डिवाइस पर सहेजे गए हैं। उनका बैकअप लेने और अपने सभी डिवाइसों पर अध्ययन करने के लिए क्लाउड सिंक सक्षम करें।",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "जोड़ने के लिए आइटम चुनें। वे आपके खाते में कॉपी हो जाते हैं और क्लाउड पर अपलोड हो जाते हैं। “{name}” को फिर बैकअप फ़ोल्डर में संग्रहीत करके हटा दिया जाता है।",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "मैं <a href=\"{terms}\">सेवा की शर्तों</a> और <a href=\"{privacy}\">गोपनीयता नीति</a> से सहमत हूं।",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "जारी रखने के लिए कृपया सेवा की शर्तों और गोपनीयता नीति को स्वीकार करें।",
    "Updated Terms & Privacy": "अद्यतन शर्तें और गोपनीयता",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "हमने अपनी सेवा की शर्तों और गोपनीयता नीति को अद्यतन किया है। अपने खाते का उपयोग जारी रखने के लिए कृपया उनकी समीक्षा करें और उन्हें स्वीकार करें।",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "मैं अद्यतन <a href=\"{terms}\">सेवा की शर्तों</a> और <a href=\"{privacy}\">गोपनीयता नीति</a> से सहमत हूं।",
    "Sign out": "साइन आउट करें",
    "I agree": "मैं सहमत हूं",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">गोपनीयता नीति</a> · <a href=\"{terms}\">शर्तें</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "जारी रखकर, आप <a href=\"{terms}\">सेवा की शर्तों</a> और <a href=\"{privacy}\">गोपनीयता नीति</a> से सहमत होते हैं।",
    "Privacy Policy": "गोपनीयता नीति",
    "Terms": "शर्तें",
    "Website": "वेबसाइट",
    "Contact": "संपर्क करें",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "फ्लैशकार्ड",
    "Practice your vocabulary": "अपनी शब्दावली का अभ्यास करें",
    "Due cards": "समीक्षा के लिए देय कार्ड",
    "Current filter": "वर्तमान फ़िल्टर",
    "Newest": "नवीनतम",
    "Selected words": "चयनित शब्द",
    "Deck size": "डेक का आकार",
    "Default deck size": "डिफ़ॉल्ट डेक आकार",
    "Shuffle": "फेरबदल (Shuffle)",
    "Start session": "सत्र शुरू करें",
    "Play deck": "डेक चलाएं",
    "{n} cards ready to review": "समीक्षा के लिए {n} कार्ड तैयार हैं",
    "No cards due — great job!": "कोई कार्ड देय नहीं है — बहुत बढ़िया काम!",
    "{n} selected words": "{n} चयनित शब्द",
    "No words to practice.": "अभ्यास के लिए कोई शब्द नहीं है।",
    "End session": "सत्र समाप्त करें",
    "Listening — pause to review manually":
        "सुनना — मैन्युअल रूप से समीक्षा करने के लिए रोकें",
    "Show answer": "उत्तर दिखाएं",
    "Hard": "कठिन",
    "Good": "अच्छा",
    "Easy": "आसान",
    "Space or click to flip": "पलटने के लिए स्पेस दबाएं या क्लिक करें",
    "Card {current} of {total}": "{total} में से कार्ड {current}",
    "{n} correct": "{n} सही",
    "Session complete!": "सत्र पूरा हुआ!",
    "You listened to {n} of {total} cards.": "आपने {total} में से {n} कार्ड सुने।",
    "Correct: {n} of {total}": "सही: {total} में से {n}",
    "New session": "नया सत्र",
    "Practice hard words": "कठिन शब्दों का अभ्यास करें",
    "Hard words": "कठिन शब्द",
    "Hard words cleared!": "कठिन शब्द साफ़ हो गए!",
    "Open Flashcards when Read Aloud starts":
        "सस्वर वाचन (Read Aloud) शुरू होने पर फ्लैशकार्ड खोलें",
    "Stop": "रोकें",
    "Auto-pronounce": "ऑटो-उच्चारण",
    "Speak each card as it appears and when it flips":
        "प्रत्येक कार्ड के दिखाई देने और पलटने पर उसे बोलें",
    "Deck preview": "डेक पूर्वावलोकन",
    "{n} cards": "{n} कार्ड",
    "Due": "देय (Due)",
    "In {n} d": "{n} दिनों में",
    "{n} d": "{n} दिन",
    "{n} mo": "{n} महीने",
    "{n} y": "{n} वर्ष",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Android के लिए Lingueez…",
    "Android app": "Android ऐप",
    "Lingueez on Android": "Android पर Lingueez",
    "Take your vocabulary with you": "अपनी शब्दावली को अपने साथ ले जाएं",
    "Preview of Lingueez on a phone": "फ़ोन पर Lingueez का पूर्वावलोकन",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "अपने Lingueez खाते से साइन इन करें और आपकी शब्दावली पहले से मौजूद है — "
        "कुछ भी सेट अप नहीं करना है, कुछ भी स्थानांतरित नहीं करना है।",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "दोनों पर एक मुफ़्त Lingueez खाते से साइन इन करें और आपकी शब्दावली "
        "फ़ोन से सिंक हो जाएगी — कोई फ़ाइल कॉपी करने की आवश्यकता नहीं है।",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "एक मुफ़्त Lingueez खाते से साइन इन करें और आपके शब्द आपके फ़ोन से सिंक हो जाएंगे।",
    "Synced both ways": "दोनों तरफ सिंक किया गया",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "फ़ोन पर आपके द्वारा जोड़े गए शब्द कंप्यूटर पर प्रतीक्षा कर रहे हैं, और "
        "ठीक इसका उल्टा।",
    "Listen with the screen off": "स्क्रीन बंद करके सुनें",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "लॉक-स्क्रीन नियंत्रण, ताकि जेब में फ़ोन होने पर भी समीक्षा चलती रहे।",
    "Save a word from any app": "किसी भी ऐप से एक शब्द सहेजें",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Lingueez पर पाठ साझा करें और यह आपकी शब्दावली में आ जाएगा, बाद में भरने के लिए तैयार।",
    "Point your phone's camera at the code":
        "अपने फ़ोन का कैमरा कोड की ओर करें",
    "Get it on Google Play": "Google Play पर इसे प्राप्त करें",
    "Copy link": "लिंक कॉपी करें",
    "Link copied": "लिंक कॉपी हो गया",
    "Lingueez is now on Android": "Lingueez अब Android पर है",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "अपने Lingueez खाते से साइन इन करें — आपकी शब्दावली पहले से मौजूद है।",
    "Dismiss": "खारिज करें",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "डेस्कटॉप और एंड्रॉइड डिवाइसों पर अपने Lingueez खाते का निर्बाध उपयोग करें।",
    "Get the app…": "ऐप प्राप्त करें…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "प्रश्नोत्तरी",
    "Quiz (recall practice)": "प्रश्नोत्तरी (याद करने का अभ्यास)",
    "Recall your words, one question at a time":
        "एक-एक प्रश्न करके अपने शब्द याद कीजिए",
    "Questions": "प्रश्न",
    "Answer with": "उत्तर का तरीका",
    "Choices": "विकल्प",
    "Typing": "टाइपिंग",
    "Ask": "पूछें",
    "Term": "शब्द",
    "Mixed": "मिश्रित",
    "Auto-advance": "स्वतः आगे बढ़ें",
    "Move on by itself after a correct answer": "सही उत्तर के बाद अपने आप आगे बढ़ें",
    "Speak the question, then the answer once it is revealed":
        "प्रश्न बोलें, और उत्तर दिखते ही उत्तर भी बोलें",
    "Start quiz": "प्रश्नोत्तरी शुरू करें",
    "questions ready": "प्रश्न तैयार",
    "Nothing to quiz": "पूछने के लिए कुछ नहीं",
    "No words match this deck.": "इस सेट से कोई शब्द मेल नहीं खाता।",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "प्रश्नोत्तरी के लिए कम से कम दो शब्द चाहिए — गलत विकल्प उन्हीं शब्दों से आते "
        "हैं जिनके बारे में आपसे नहीं पूछा जा रहा।",
    "Not enough words": "पर्याप्त शब्द नहीं",
    "Add a few more words, or widen the deck.": "कुछ और शब्द जोड़ें, या सेट बड़ा करें।",
    "Question {n} of {total}": "प्रश्न {n} / {total}",
    "Missed words": "गलत हुए शब्द",
    "End quiz": "प्रश्नोत्तरी समाप्त करें",
    "Answer in {language}": "{language} में उत्तर दें",
    "Type the answer": "उत्तर लिखें",
    "Check": "जाँचें",
    "Click to continue": "जारी रखने के लिए क्लिक करें",
    "See results": "परिणाम देखें",
    "Almost — it is \"{answer}\"": "लगभग — सही उत्तर है “{answer}”",
    "It is \"{answer}\"": "सही उत्तर है “{answer}”",
    "Now {status}": "अब {status}",
    "Correct": "सही",
    "Missed": "गलत",
    "Worth another look": "एक बार और देखने लायक",
    "Again": "फिर से",
    "Missed words cleared!": "गलत हुए शब्द सध गए!",
    "Perfect run": "पूरी तरह सही",
    "Quiz complete": "प्रश्नोत्तरी पूरी हुई",
    "Practice missed": "गलतियों का अभ्यास",
    "Default number of questions": "प्रश्नों की डिफ़ॉल्ट संख्या",
    "Move on after a correct answer": "सही उत्तर के बाद आगे बढ़ें",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "चुनें कि किस बारे में पूछा जाए",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "वही सेट जो फ़्लैशकार्ड में हैं — दोहराने योग्य शब्द, आपका मौजूदा फ़िल्टर, "
        "सबसे नए, या हाथ से चुने हुए — और कितने प्रश्न पूछे जाएँ।",
    "Choices or typing": "विकल्प या टाइपिंग",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "“विकल्प” चार उत्तर देता है जिनमें से चुनना होता है; “टाइपिंग” उत्तर लिखवाता "
        "है — कठिन है, पर यही असली परख है। टाइपिंग में मात्राएँ और छोटी टाइपिंग "
        "गलतियाँ माफ़ रहती हैं। “पूछें” तय करता है कि आप कौन-सा पक्ष देखेंगे — शब्द, "
        "उसका अनुवाद, या दोनों मिलाकर।",
    "Start, and it counts": "शुरू करें — यह गिना जाता है",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "पट्टी दिखाती है कि सेट में किस स्थिति के कितने शब्द हैं। हर उत्तर वही "
        "अंतराल-पुनरावृत्ति कार्यक्रम भरता है जो फ़्लैशकार्ड का है: याद आया शब्द बाद "
        "में लौटता है, और चूका हुआ जल्दी।",
}

# Date names, read by app.i18n.
MONTHS = ["जनवरी", "फ़रवरी", "मार्च", "अप्रैल", "मई", "जून",
          "जुलाई", "अगस्त", "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"]
MONTHS_ABBR = ["जन", "फ़र", "मार्च", "अप्रै", "मई", "जून",
               "जुलाई", "अगस्त", "सितं", "अक्तू", "नवं", "दिसं"]
WEEKDAYS = ["सोमवार", "मंगलवार", "बुधवार", "गुरुवार",
            "शुक्रवार", "शनिवार", "रविवार"]
WEEKDAYS_ABBR = ["सोम", "मंगल", "बुध", "गुरु", "शुक्र", "शनि", "रवि"]