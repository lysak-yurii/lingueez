# Lingueez — French (fr) translations.
# Keys are English UI strings; values are their French equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Français"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Annuler",
    "OK": "OK",
    "Close": "Fermer",
    "Save": "Enregistrer",
    "Delete": "Supprimer",
    "Edit": "Modifier",
    "Remove": "Retirer",
    "Add": "Ajouter",
    "Refresh": "Actualiser",
    "Import": "Importer",
    "Export": "Exporter",
    "Search": "Rechercher",
    "Fetch": "Récupérer",
    "Browse…": "Parcourir…",
    "Clear": "Effacer",
    "Pause": "Pause",
    "Resume": "Reprendre",
    "Language": "Langue",
    "Translation": "Traduction",
    "Word": "Mot",
    "Status": "Statut",
    "Error": "Erreur",
    "Title": "Titre",
    "Topic": "Sujet",
    "Level": "Niveau",
    "Generate": "Générer",
    "Generating…": "Génération en cours…",
    "Translating…": "Traduction en cours…",
    "Format": "Format",
    "Style": "Style",
    "Model": "Modèle",
    "Font": "Police",
    "Usage": "Utilisation",
    "Translation language": "Langue de traduction",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Menu",
    "Open Excel Table…": "Ouvrir un tableau Excel…",
    "Import Excel to Database…": "Importer Excel dans la base de données…",
    "Save Import Template…": "Enregistrer le modèle d'importation…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Audio (MP3)…",
    "Backups…": "Sauvegardes…",
    "Show Source column": "Afficher la colonne « Source »",
    "Show Created At column": "Afficher la colonne « Date de création »",
    "Max words…": "Nombre max de mots…",
    "View Log": "Afficher le journal",
    "About": "À propos",
    "Quit": "Quitter",
    "Words": "Mots",
    "Texts": "Textes",
    "Statistics": "Statistiques",
    "Bin (deleted items)": "Corbeille (éléments supprimés)",
    "Settings": "Paramètres",
    "Vocabulary": "Vocabulaire",
    "Search words, translations or tags…": "Rechercher des mots, traductions ou étiquettes…",
    "Search texts by title, content or words…": "Rechercher des textes par titre, contenu ou mots…",
    "Search scope": "Périmètre de recherche",
    "Search scope…": "Périmètre de recherche…",
    "Nothing to practice yet": "Rien à réviser pour l'instant",
    "Add words to your vocabulary and they show up here.":
        "Ajoutez des mots à votre vocabulaire et ils apparaîtront ici.",
    "Come back when cards are due, or practice the newest words now.":
        "Revenez quand des cartes seront à réviser, ou entraînez-vous dès maintenant sur les mots les plus récents.",
    "Practice newest words": "Réviser les mots récents",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Choisissez un autre paquet ci-dessus ou ajustez vos filtres sur la page Mots.",
    "You're all caught up": "Vous êtes à jour",
    "Add word": "Ajouter un mot",
    "Copy a word in any app, then press:":
        "Copiez un mot dans n'importe quelle app, puis appuyez sur :",
    "Set a shortcut": "Définir un raccourci",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Copiez un mot dans n'importe quelle app, puis appuyez sur {keys} pour l'ajouter avec sa traduction.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Définissez un raccourci dans les Paramètres pour ajouter des mots copiés depuis n'importe quelle app.",
    " Favorites": " Favoris",
    " Filters": " Filtres",
    "Filters that don't fit the table": "Filtres ne tenant pas dans le tableau",
    "More actions": "Plus d'actions",
    "Filter by tag": "Filtrer par étiquette",
    "Close file and return to your vocabulary": "Fermer le fichier et revenir à votre vocabulaire",
    "Definition": "Définition",
    "Read": "Lire",
    "Favorite": "Favori",
    "Tags": "Étiquettes",
    "Copy": "Copier",
    "Text": "Texte",
    "Delete selected (Del)": "Supprimer la sélection (Suppr)",
    "No data": "Aucune donnée",
    "No texts yet": "Aucun texte pour le moment",
    "Words: {shown}/{total}": "Mots : {shown}/{total}",
    "Texts: {total}": "Textes : {total}",
    "Texts: {shown}/{total}": "Textes : {shown}/{total}",
    "{count} selected": "{count} sélectionné(s)",
    "No selection": "Aucune sélection",
    "Please select at least one word.": "Veuillez sélectionner au moins un mot.",
    "Saved": "Enregistré",
    "'{word}' updated.": "« {word} » mis à jour.",
    "Database Error": "Erreur de la base de données",
    "Delete {count} word(s)?": "Supprimer {count} mot(s) ?",
    "Deleted": "Supprimé",
    "{count} word(s) deleted.": "{count} mot(s) supprimé(s).",
    "Deleted with {n} error(s).": "Supprimé avec {n} erreur(s).",
    "Favorites": "Favoris",
    "{count} word(s) added to favorites.": "{count} mot(s) ajouté(s) aux favoris.",
    "{count} word(s) removed from favorites.": "{count} mot(s) retiré(s) des favoris.",
    "Status set to '{status}' for {count} word(s).": "Statut défini sur « {status} » pour {count} mot(s).",
    "Max Words": "Mots maximum",
    "Show only the first N words (0 = show all):": "Afficher uniquement les N premiers mots (0 = tout afficher) :",
    "View Definition": "Voir la définition",
    "Copy Word": "Copier le mot",
    "Copy Translation": "Copier la traduction",
    "Toggle Favorite": "Basculer les favoris",
    "Add to favorites": "Ajouter aux favoris",
    "Remove from favorites": "Retirer des favoris",
    "Tag these words…": "Étiqueter ces mots…",
    "Show less": "Réduire",
    "Show all {count}": "Afficher les {count}",
    "Change Status…": "Changer le statut…",
    "Add / Remove Tags…": "Ajouter / Supprimer des étiquettes…",
    "Read Aloud": "Lecture à haute voix",
    "Change Status": "Changer le statut",
    "New status:": "Nouveau statut :",
    "Copied": "Copié",
    "{count} row(s) copied to clipboard.": "{count} ligne(s) copiée(s) dans le presse-papiers.",
    "{count} item(s) copied to clipboard.": "{count} élément(s) copié(s) dans le presse-papiers.",
    "Copy Word(s)": "Copier le(s) mot(s)",
    "Copy Translation(s)": "Copier la/les traduction(s)",
    "Copy Both": "Copier les deux",
    "Search in Word": "Rechercher dans le mot",
    "Search in Translation": "Rechercher dans la traduction",
    "Search in Tags": "Rechercher dans les étiquettes",
    "Promoted": "Promu",
    "Google Cloud TTS unavailable": "Google Cloud TTS indisponible",
    "Selection limit": "Limite de sélection",
    "Only the first 200 selected words will be read.": "Seuls les 200 premiers mots sélectionnés seront lus.",
    "Only the first 50 words will be used.": "Seuls les 50 premiers mots seront utilisés.",
    "Select words to save as audio.": "Sélectionnez des mots à enregistrer sous forme d'audio.",
    "Nothing to export.": "Rien à exporter.",
    "Export Error": "Erreur d'exportation",
    "Settings saved.": "Paramètres enregistrés.",
    "Generated text saved.": "Texte généré enregistré.",
    "Show": "Afficher",
    "Add Word": "Ajouter un mot",
    "Stop reading": "Arrêter la lecture",
    "Read — Read selected words aloud": "Lire — Lire les mots sélectionnés à haute voix",
    "Translation": "Traduction",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Apparence",
    "Audio": "Audio",
    "Learning": "Apprentissage",
    "Listening": "Écoute",
    "Backups": "Sauvegardes",
    "Sync your library?": "Synchroniser votre bibliothèque ?",
    "This will reconcile your device with the cloud:": "Cela synchronisera votre appareil avec le cloud :",
    "Sync now": "Synchroniser maintenant",
    "Upload": "Téléverser",
    "Synced — ↑{up} ↓{down}": "Synchronisé — ↑{up} ↓{down}",
    "Upload restored library?": "Téléverser la bibliothèque restaurée ?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Bibliothèque restaurée. Il vous sera demandé de la téléverser lors de votre prochaine connexion à un serveur de synchronisation.",
    "Merging this restored backup with your cloud:": "Fusion de cette sauvegarde restaurée avec votre cloud :",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Cette sauvegarde contient {items}. Voulez-vous la téléverser et la fusionner avec votre cloud maintenant, ou laisser votre cloud inchangé pour l'instant ?",
    "General": "Général",
    "Read-aloud": "Lecture à haute voix",
    "Translation & AI": "Traduction & IA",
    "Data": "Données",
    "Behavior": "Comportement",
    "Progress": "Progression",
    "DeepL request failed — using free Google Translate instead.": "La requête DeepL a échoué — utilisation de Google Traduction gratuit à la place.",
    "DeepL key isn't set — using free Google Translate instead.": "La clé DeepL n'est pas définie — utilisation de Google Traduction gratuit à la place.",
    "System": "Système",
    "Light": "Clair",
    "Dark": "Sombre",
    "Appearance mode": "Mode d'apparence",
    "Widget scaling": "Échelle des éléments",
    "Table size": "Taille du tableau",
    "Interface language": "Langue de l'interface",
    "Restart the app to apply the language change.": "Redémarrez l'application pour appliquer le changement de langue.",
    "The interface language has changed. Restart now to apply it?": "La langue de l'interface a changé. Redémarrer maintenant pour l'appliquer ?",
    "TTS provider": "Fournisseur TTS",
    "Google Cloud credentials": "Identifiants Google Cloud",
    "Voice type": "Type de voix",
    "Voice name (optional)": "Nom de la voix (optionnel)",
    "Read Aloud playback": "Paramètres de lecture à haute voix",
    "Pause between words (s)": "Pause entre les mots (s)",
    "Repeats per word": "Répétitions par mot",
    "Repeats per pair": "Répétitions par paire",
    "Promote status while listening": "Promouvoir le statut pendant l'écoute",
    "Listens to reach {status}": "Écoutes pour atteindre « {status} »",
    "Excel import": "Importation Excel",
    "Placeholder values": "Valeurs d'exemple",
    "Skip placeholder rows": "Ignorer les lignes d'exemple",
    "Skip empty rows": "Ignorer les lignes vides",
    "Normalize language pairs": "Normaliser les paires de langues",
    "How to import": "Comment importer",
    "Save import template…": "Enregistrer le modèle d'importation…",
    "Active provider": "Fournisseur actif",
    "API key": "Clé API",
    "API URL": "URL de l'API",
    "Check usage": "Vérifier l'utilisation",
    "Enable cloud sync": "Activer la synchronisation cloud",
    "Supabase URL (.env)": "URL Supabase (.env)",
    "Supabase key (.env)": "Clé Supabase (.env)",
    "Bin cleanup grace (days)": "Délai avant nettoyage de la corbeille (jours)",
    "Test Connection": "Tester la connexion",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "La synchronisation cloud utilise votre propre projet Supabase. Créez les tables requises une fois, puis entrez l'URL et la clé anonyme ci-dessus.",
    "Copy schema SQL": "Copier le schéma SQL",
    "Open SQL editor ↗": "Ouvrir l'éditeur SQL ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "Le schéma SQL a été copié dans le presse-papiers. Ouvrez l'éditeur SQL de votre projet Supabase, collez-le et appuyez sur Run pour créer les tables.",
    "Server": "Serveur",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Connecté à votre propre serveur Supabase — mode personnel, aucun compte requis.\n{host}",
    "Use your own Supabase server (personal)": "Utiliser votre propre serveur Supabase (personnel)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Synchronisation personnelle et mono-utilisateur vers un projet Supabase dont vous êtes propriétaire. Pas de compte ni de connexion — l'application se connecte avec la clé anonyme du projet. Exécutez le schéma SQL dans votre projet, collez son URL et sa clé anonyme ci-dessous, puis testez la connexion.\n\nRemarque : toute personne possédant cette URL et cette clé peut lire les données, gardez donc le projet privé et ne partagez pas la clé.",
    "Disconnect — use the built-in server": "Déconnecter — utiliser le serveur intégré",
    "Disconnect server": "Déconnecter le serveur",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "Arrêter la synchronisation avec votre propre serveur Supabase et réutiliser le serveur intégré ?\n\nVos mots restent dans votre projet et sur cet appareil. Vous serez en mode local uniquement jusqu'à ce que vous vous connectiez à un compte.",
    "Disconnected — using the built-in server.": "Déconnecté — utilisation du serveur intégré.",
    "{host} (personal)": "{host} (personnel)",
    "Personal": "Personnel",
    "your server": "votre serveur",
    "Account actions": "Actions du compte",
    "Add account…": "Ajouter un compte…",
    "Sync this device's data to my account…": "Synchroniser les données de cet appareil avec mon compte…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Compte",
    "Accounts": "Comptes",
    "No accounts yet. Add one to sync your words across devices.": "Aucun compte pour le moment. Ajoutez-en un pour synchroniser vos mots sur plusieurs appareils.",
    "(active)": "(actif)",
    "Sign in": "Se connecter",
    "(sign in again)": "(reconnectez-vous)",
    "Switch": "Changer",
    "Remove account": "Supprimer le compte",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "Supprimer {email} de cet appareil ? Vous pourrez le rajouter à tout moment — vos mots restent dans le cloud et la copie locale reste sur le disque. Vos données cloud ne sont pas supprimées.",
    "Removed {email} from this device.": "{email} retiré de cet appareil.",
    "Your data was exported.": "Vos données ont été exportées.",
    "Export failed.": "L'exportation a échoué.",
    "Delete account": "Supprimer le compte",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Ceci supprimera définitivement votre compte et TOUS vos mots, textes et étiquettes synchronisés du cloud. Votre copie locale sera archivée dans le dossier de sauvegarde. Cette action est irréversible.\n\nSupprimer votre compte ?",
    "Account deleted.": "Compte supprimé.",
    "Could not delete the account.": "Impossible de supprimer le compte.",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Nom",
    "Enter your name.": "Saisissez votre nom.",
    "Email": "E-mail",
    "Password": "Mot de passe",
    "New password": "Nouveau mot de passe",
    "6-digit code": "Code à 6 chiffres",
    "or": "ou",
    "Sign in with Google": "Se connecter avec Google",
    "Opening your browser to sign in with Google…": "Ouverture de votre navigateur pour vous connecter avec Google…",
    "Forgot password?": "Mot de passe oublié ?",
    "Resend code": "Renvoyer le code",
    "Confirm your email": "Confirmez votre e-mail",
    "Verify code": "Vérifier le code",
    "Use a different email": "Utiliser un autre e-mail",
    "Enter your email and password.": "Saisissez votre e-mail et votre mot de passe.",
    "Enter the 6-digit code from the email.": "Saisissez le code à 6 chiffres reçu par e-mail.",
    "Enter the code and a new password.": "Saisissez le code et un nouveau mot de passe.",
    "Enter your email above first.": "Saisissez d'abord votre e-mail ci-dessus.",
    "Enter the reset code we emailed you and a new password.": "Saisissez le code de réinitialisation envoyé par e-mail et un nouveau mot de passe.",
    "Enter the 6-digit code we emailed you.": "Saisissez le code à 6 chiffres que nous vous avons envoyé par e-mail.",
    "Reset password": "Réinitialiser le mot de passe",
    "Set new password": "Définir un nouveau mot de passe",
    "Back to sign in": "Retour à la connexion",
    "Sign-in failed.": "Échec de la connexion.",
    "Couldn't send the code.": "Impossible d'envoyer le code.",
    "Done.": "Terminé.",
    "Failed.": "Échec.",
    "Create an account": "Créer un compte",
    "Create account": "Créer un compte",
    "I already have an account": "J'ai déjà un compte",
    "Signed in as {email}": "Connecté en tant que {email}",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Synchroniser les données de cet appareil avec votre compte",
    "your account": "votre compte",
    "This device has {words} and {texts} not yet in {account}.": "Cet appareil contient {words} et {texts} qui ne sont pas encore dans {account}.",
    "This device has {words} not yet in {account}.": "Cet appareil contient {words} qui ne sont pas encore dans {account}.",
    "This device has {texts} not yet in {account}.": "Cet appareil contient {texts} qui ne sont pas encore dans {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Sélectionnez les éléments à ajouter. Ils seront copiés sur votre compte et téléversés dans le cloud afin d'apparaître sur vos autres appareils. La copie sur cet appareil sera conservée.",
    "Don't ask again for this account": "Ne plus demander pour ce compte",
    "{n} word": "{n} mot",
    "{n} words": "{n} mots",
    "{n} text": "{n} texte",
    "{n} texts": "{n} textes",
    "Add {n} item": "Ajouter {n} élément",
    "Add {n} items": "Ajouter {n} éléments",
    # Ukrainian "many" (genitive) plural forms — fallback mapping for consistency
    "words (genitive)": "mots",
    "texts (genitive)": "textes",
    "tags (genitive)": "étiquettes",
    "changes (genitive)": "modifications",
    "deletions (genitive)": "suppressions",
    "{n} words (genitive)": "{n} mots",
    "{n} texts (genitive)": "{n} textes",
    "Add {n} items (genitive)": "Ajouter {n} éléments",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "{n} élément ajouté à votre compte.",
    "Added {n} items to your account.": "{n} éléments ajoutés à votre compte.",
    "Added {n} items to your account. (genitive)": "{n} éléments ajoutés à votre compte.",
    "{n} couldn't be added.": "{n} n'a pas pu être ajouté.",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Votre session a expiré — reconnectez-vous (Paramètres → Synchronisation)",
    "Sign in to sync (Settings → Sync)": "Connectez-vous pour synchroniser (Paramètres → Synchronisation)",
    "Sign in again to sync": "Reconnectez-vous pour synchroniser",
    "Sign in again to use this account.": "Reconnectez-vous pour utiliser ce compte.",
    "Sync incomplete: {reason}": "Synchronisation incomplète : {reason}",
    "Connect to the internet to add local items to your account.": "Connectez-vous à Internet pour ajouter les éléments locaux à votre compte.",
    "Everything on this device is already in your account.": "Tout ce qui se trouve sur cet appareil est déjà sur votre compte.",
    "Upload local words?": "Téléverser les mots locaux ?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "Téléverser vos mots locaux actuels vers ce compte ? Ils seront fusionnés avec les données cloud de ce compte et synchronisés.\n\nChoisissez Non pour conserver les données existantes du compte et mettre de côté vos mots locaux (archivés dans le dossier de sauvegarde).",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Échec de la connexion. Vérifiez votre e-mail et votre mot de passe.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Vous pouvez conserver jusqu'à {max} comptes sur cet appareil. Retirez-en un pour en ajouter un autre.",
    "Wrong email or password.": "E-mail ou mot de passe incorrect.",
    "That doesn't look like a valid email address.": "L'adresse e-mail ne semble pas valide.",
    "Confirm password": "Confirmer le mot de passe",
    "Passwords don't match.": "Les mots de passe ne correspondent pas.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Votre e-mail n'est pas encore confirmé. Saisissez le code à 6 chiffres qui vous a été envoyé.",
    "That email is already registered. Try signing in instead.": "Cet e-mail est déjà enregistré. Essayez plutôt de vous connecter.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Nous vous avons envoyé un code à 6 chiffres par e-mail. Saisissez-le pour terminer votre inscription.",
    "That code didn't work. Check it and try again.": "Ce code n'a pas fonctionné. Vérifiez-le et réessayez.",
    "If that account exists, a 6-digit reset code is on its way.": "Si ce compte existe, un code de réinitialisation à 6 chiffres vient de vous être envoyé.",
    "Confirmation email re-sent.": "L'e-mail de confirmation a été renvoyé.",
    "Too many attempts. Please wait a minute and try again.": "Trop de tentatives. Veuillez patienter une minute et réessayer.",
    "Your password is too short — use at least 6 characters.": "Votre mot de passe est trop court — utilisez au moins 6 caractères.",
    "Sign-ups are disabled on this server.": "Les inscriptions sont désactivées sur ce serveur.",
    "Can't reach the server. Check your internet connection.": "Impossible de contacter le serveur. Vérifiez votre connexion Internet.",
    "Something went wrong.": "Un problème est survenu.",
    "Your saved sign-in for this account expired. Sign in again.": "Votre connexion enregistrée a expiré. Veuillez vous reconnecter.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "La synchronisation cloud n'est pas encore configurée. Ajoutez d'abord l'URL et la clé Supabase dans Paramètres → Synchronisation.",
    "Could not start Google sign-in.": "Impossible de démarrer la connexion avec Google.",
    "Google sign-in was cancelled or timed out.": "La connexion avec Google a été annulée ou a expiré.",
    "Google sign-in failed.": "La connexion avec Google a échoué.",
    "Google sign-in failed: {error}": "La connexion avec Google a échoué : {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "Impossible de démarrer l'assistant de connexion local sur le port {port} ({error}). Fermez l'application qui l'utilise et réessayez.",
    "Export my data…": "Exporter mes données…",
    "Delete account…": "Supprimer le compte…",
    "Cloud sync is on — your own server ({host})": "Synchronisation cloud activée — votre propre serveur ({host})",
    "Cloud sync is on — signed in as {who}": "Synchronisation cloud activée — connecté en tant que {who}",
    "Cloud sync is off — your words are saved on this device only": "Synchronisation cloud désactivée — vos mots sont enregistrés sur cet appareil uniquement",
    "(checking…)": "(vérification…)",
    "(can't connect)": "(impossible de se connecter)",
    "Turn off cloud sync": "Désactiver la synchronisation cloud",
    "Cloud sync turned off — this device only.": "Synchronisation cloud désactivée — cet appareil uniquement.",
    "Use this server": "Utiliser ce serveur",
    "Connecting…": "Connexion en cours…",
    "Testing…": "Test en cours…",
    "Applying theme…": "Application du thème…",
    "Now syncing with your own server.": "Synchronisation en cours avec votre propre serveur.",
    "Could not connect to this server:\n{error}": "Impossible de se connecter à ce serveur :\n{error}",
    "Could not connect to this server.": "Impossible de se connecter à ce serveur.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nVérifiez l'URL, la clé anonyme et assurez-vous d'avoir exécuté le schéma SQL. Utiliser ces informations quand même ?",
    "Enter your server's URL and anon key first, then test.": "Entrez d'abord l'URL et la clé anonyme de votre serveur, puis testez.",
    "Enter your server's URL and anon key first.": "Entrez d'abord l'URL et la clé anonyme de votre serveur.",
    "Supabase URL": "URL Supabase",
    "Supabase key (anon)": "Clé Supabase (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Synchronisation personnelle et mono-utilisateur vers un projet Supabase dont vous êtes propriétaire. Pas de compte ni de connexion — l'application se connecte avec la clé anonyme du projet. Exécutez le schéma SQL dans votre projet, collez son URL et sa clé anonyme ci-dessous, testez la connexion, puis appuyez sur « Utiliser ce serveur ».\n\nRemarque : toute personne possédant cette URL et cette clé peut lire les données, gardez donc le projet privé et ne partagez pas la clé.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "Arrêter la synchronisation avec votre propre serveur Supabase et réutiliser le serveur intégré ?\n\nVos mots restent dans votre projet et sur cet appareil. Les paramètres du serveur sont conservés afin que vous puissiez y revenir à tout moment. Vous serez en mode local uniquement jusqu'à ce que vous vous connectiez à un compte.",
    "Start automatically on login (minimized to tray)": "Lancer automatiquement au démarrage (réduit dans la zone de notification)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "Le lancement à l'ouverture de session est désactivé pour Lingueez dans les paramètres Windows ; il ne peut pas être activé ici.",
    "Open Windows startup settings": "Ouvrir les paramètres de démarrage de Windows",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows n'a pas appliqué cette modification. Vous pouvez activer ou désactiver Lingueez vous-même dans Paramètres > Applications > Démarrage.",
    "Add Word hotkey (global)": "Raccourci clavier « Ajouter un mot » (global)",
    "Data format": "Format des données",
    "Columns to export": "Colonnes à exporter",
    "Sheet name": "Nom de la feuille",
    "Start row": "Ligne de départ",
    "Start column": "Colonne de départ",
    "Shade alternate rows": "Alterner la couleur des lignes",
    "Auto column width": "Largeur de colonne automatique",
    "Freeze header row": "Figer la ligne d'en-tête",
    "Delimiter": "Séparateur",
    "Delimiter (\\t = tab)": "Séparateur (\\t = tabulation)",
    "Include header lines": "Inclure les lignes d'en-tête",
    "Header lines": "Lignes d'en-tête",
    "Page size": "Taille de la page",
    "Font size": "Taille de la police",
    "Line spacing (pt)": "Interligne (pt)",
    "Text alignment": "Alignement du texte",
    "Margins L/R/T/B (pt)": "Marges G/D/H/B (pt)",
    "Automatic widths (fit page)": "Largeurs automatiques (ajuster à la page)",
    "Columns / width": "Colonnes / largeur",
    "Header background": "Arrière-plan de l'en-tête",
    "Header text": "Texte de l'en-tête",
    "Row background": "Arrière-plan des lignes",
    "Grid lines": "Quadrillage",
    "Background image": "Image de fond",
    "Concurrent workers": "Processus simultanés",
    "Requests per second": "Requêtes par seconde",
    "Add font…": "Ajouter une police…",
    "Page && text": "Page && texte",
    "Columns": "Colonnes",
    "Max tokens": "Jétons max (tokens)",
    "Temperature": "Température",
    "Prompt template": "Modèle de consigne (prompt)",
    "Definitions": "Définitions",
    "Generated Texts (from words)": "Textes générés (à partir de mots)",
    "Generated Texts (by topic)": "Textes générés (par sujet)",
    "Text Adaptation (to level)": "Adaptation de texte (au niveau)",
    "Thinking budget (0 = off, -1 = auto)": "Budget de réflexion (0 = désactivé, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Détecter la langue",
    "Type a word or phrase…": "Saisissez un mot ou une phrase…",
    "Translation…": "Traduction…",
    "Pronounce": "Prononcer",
    "Swap word and translation": "Inverser le mot et la traduction",
    "Translate with DeepL (Enter)": "Traduire avec DeepL (Entrée)",
    "Save Word": "Enregistrer le mot",
    "Enter a word to translate.": "Saisissez un mot à traduire.",
    "Fill with AI (lemma + best translation)": "Remplir avec l'IA (lemme + meilleure traduction)",
    "Enter a word to fill with AI.": "Saisissez un mot à compléter avec l'IA.",
    "Source equals target — translated to {lang} instead.": "La langue source est identique à la cible — traduit en {lang} à la place.",
    "Both word and translation are required.": "Le mot et la traduction sont tous deux requis.",
    "Please select the source language before saving.": "Veuillez sélectionner la langue source avant d'enregistrer.",
    "'{word}' already exists in your dictionary.": "« {word} » existe déjà dans votre dictionnaire.",
    "'{word}' is already in your dictionary.": "« {word} » est déjà dans votre dictionnaire.",
    "Already in your dictionary": "Déjà dans votre dictionnaire",
    "Show existing": "Afficher l'existant",
    "The text was truncated to the first 100 words.": "Le texte a été tronqué aux 100 premiers mots.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Générer avec l'IA",
    "Regenerate with AI": "Régénérer avec l'IA",
    "Definition 2": "Définition 2",
    "No definition yet": "Pas encore de définition",
    "Generate one with AI, or write your own with Edit.": "Générez-en une avec l'IA ou rédigez la vôtre avec Modifier.",
    "There is no word to define.": "Il n'y a aucun mot à définir.",
    "Bold": "Gras",
    "Italic": "Italique",
    "Heading": "Titre",
    "List": "Liste",
    "API key missing": "Clé API manquante",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Définissez d'abord votre clé API {ai} dans Paramètres → Traduction & IA → IA.",
    "Generating definition…": "Génération de la définition…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Étiquettes — {count} mot(s)",
    "New tag name…": "Nom de la nouvelle étiquette…",
    "Add Tag": "Ajouter l'étiquette",
    "Apply Selected to All": "Appliquer la sélection à tous",
    "Remove Selected": "Retirer la sélection",
    "(partial)": "(partiel)",
    "use(s)": "utilisation(s)",
    "Tags marked ✓ apply to all selected words.": (
        "Les étiquettes cochées ✓ s'appliquent à tous les mots sélectionnés."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (partiel) signifie que seuls certains éléments possèdent l'étiquette."
    ),
    "Select tag(s) in the list first.": "Sélectionnez d'abord des étiquettes dans la liste.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Corbeille — Éléments supprimés",
    "Delete Permanently": "Supprimer définitivement",
    "Cleanup Old Items…": "Nettoyer les anciens éléments…",
    "{n} selected": "{n} sélectionné(s)",
    "The bin is empty. Deleted words will appear here.":
        "La corbeille est vide. Les mots supprimés apparaîtront ici.",
    "The bin is empty. Deleted texts will appear here.":
        "La corbeille est vide. Les textes supprimés apparaîtront ici.",
    "deleted {when}": "supprimé {when}",
    "(empty)": "(vide)",
    "Untitled": "Sans titre",
    "Auto-deletes soon": "Suppression automatique prochaine",
    "Auto-deletes in {n} day": "Suppression automatique dans {n} jour",
    "Auto-deletes in {n} days": "Suppression automatique dans {n} jours",
    "Auto-deletes in {n} days (genitive)": "Suppression automatique dans {n} jours",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "Supprimer définitivement {count} élément(s) ? Cette action est irréversible.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Restaurer une version antérieure",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Votre base de données est sauvegardée automatiquement après chaque modification. "
        "Choisissez une version antérieure ci-dessous pour la restaurer."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Aucune version enregistrée pour le moment. "
        "Une sauvegarde est créée automatiquement après chaque modification."
    ),
    "Restore this version": "Restaurer cette version",
    "Today": "Aujourd'hui",
    "Yesterday": "Hier",
    "Most recent": "La plus récente",
    "Before your last restore": "Avant votre dernière restauration",
    "today": "aujourd'hui",
    "yesterday": "hier",
    "today {time}": "aujourd'hui à {time}",
    "yesterday {time}": "hier à {time}",
    "the version from {date}": "la version du {date}",
    "the version from just before your last restore": "la version juste avant votre dernière restauration",
    "Restore Version": "Restaurer la version",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "Restaurer {phrase} ?\n\nVos données actuelles seront d'abord sauvegardées pour que vous puissiez annuler."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Votre base de données a été restaurée à {phrase}.\n\n"
        "Vous avez changé d'avis ? Restaurez « {before} » pour annuler."
    ),
    "Restore Error": "Erreur de restauration",
    "Sorry, that version could not be restored:\n{error}": "Désolé, cette version n'a pas pu être restaurée :\n{error}",
    "Remove Version": "Supprimer la version",
    "Remove {phrase}?": "Supprimer {phrase} ?",
    "Remove Error": "Erreur de suppression",
    "Sorry, that version could not be removed:\n{error}": "Désolé, cette version n'a pas pu être supprimée :\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Générer du texte",
    "Title…": "Titre…",
    "Generated text appears here…": "Le texte généré apparaîtra ici…",
    "Save to Texts": "Enregistrer dans les textes",
    "Save failed": "Échec de l'enregistrement",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Enregistrer sous forme d'audio",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Générer un fichier MP3 à partir de {count} paire(s) mot/traduction."
    ),
    "Generating audio…": "Génération de l'audio…",
    "Compiling final audio file…": "Compilation du fichier audio final…",
    "Processed: {word}": "Traité : {word}",
    "Choose File && Start": "Choisir le fichier && Démarrer",
    "Cancelled.": "Annulé.",
    "Audio saved": "Audio enregistré",
    "Audio file saved to:\n{path}": "Fichier audio enregistré sous :\n{path}",
    "Audio Error": "Erreur audio",
    "Failed to save audio:\n{error}": "Échec de l'enregistrement audio :\n{error}",
    "Cancelling…": "Annulation…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Importer depuis Excel",
    "Row": "Ligne",
    "Word 1": "Mot 1",
    "Language 1": "Langue 1",
    "Word 2": "Mot 2",
    "Language 2": "Langue 2",
    "Action": "Action",
    "Details": "Détails",
    "Add": "Ajouter",
    "Update": "Mettre à jour",
    "Skip": "Ignorer",
    "All": "Tout",
    "To add": "À ajouter",
    "To update": "À mettre à jour",
    "Skipped": "Ignorés",
    "Unrecognized": "Non reconnus",
    "Only recognized languages": "Uniquement les langues reconnues",
    "Exclude rows whose language wasn't recognized.":
        "Exclure les lignes dont la langue n'a pas été reconnue.",
    "Unrecognized language — will be imported exactly as written.":
        "Langue non reconnue — sera importée exactement comme écrite.",
    "Select all": "Tout sélectionner",
    "Activity log": "Journal d'activité",
    "Export log…": "Exporter le journal…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Exporter…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Ajouter un texte",
    "Write": "Rédiger",
    "AI Generate": "Générer par IA",
    "Wikipedia": "Wikipédia",
    "From URL": "Depuis une URL",
    "Language:": "Langue :",
    "Level:": "Niveau :",
    "Topic:": "Sujet :",
    "Topic…": "Sujet…",
    "Adapt to my level": "Adapter à mon niveau",
    "Load entries": "Charger les entrées",
    "Add feed…": "Ajouter un flux…",
    "Ideas:": "Idées :",
    "Short (~100 words)": "Court (~100 mots)",
    "Medium (~250 words)": "Moyen (~250 mots)",
    "Long (~500 words)": "Long (~500 mots)",
    "Travel": "Voyage",
    "Food": "Nourriture",
    "Daily routine": "Routine quotidienne",
    "A short story": "Une courte histoire",
    "News": "Actualités",
    "Dialogue at a café": "Dialogue au café",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Saisissez ou collez votre texte ici, ou récupérez-en un avec les onglets ci-dessus…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Plus récents en premier",
    "Oldest first": "Plus anciens en premier",
    "Title A–Z": "Titre A–Z",
    "All languages": "Toutes les langues",
    "All levels": "Tous les niveaux",
    "All topics": "Tous les sujets",
    "No matching texts": "Aucun texte correspondant",
    "Try a different search or language filter.": "Essayez une autre recherche ou un autre filtre de langue.",
    "New text (write or paste)": "Nouveau texte (rédiger ou coller)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Obtenir du texte depuis Internet (IA / Wikipédia / URL / RSS)"
    ),
    "Import .txt file(s)": "Importer des fichiers .txt",
    "Read aloud": "Lire à haute voix",
    "Translate text": "Traduire le texte",
    "Hide translation": "Masquer la traduction",
    "Focus mode": "Mode concentration",
    "Exit focus mode": "Quitter le mode concentration",
    "Paper mode: off": "Mode papier : désactivé",
    "Paper: white (click for sepia)": "Papier : blanc (cliquer pour sépia)",
    "Paper: sepia (click to turn off)": "Papier : sépia (cliquer pour désactiver)",
    "Save Changes": "Enregistrer les modifications",
    "Previous text": "Texte précédent",
    "Next text": "Texte suivant",
    "From words: {words}": "Issu des mots : {words}",
    "Created {date}": "Créé le {date}",
    "Unsaved changes": "Modifications non enregistrées",
    "Save changes to '{title}'?": "Enregistrer les modifications apportées à « {title} » ?",
    "Changes saved.": "Modifications enregistrées.",
    "'{title}' moved to bin.": "« {title} » déplacé vers la corbeille.",
    "Reader": "Lecteur",
    'Pronounce "{word}"': 'Prononcer « {word} »',
    'Add "{word}" to vocabulary': 'Ajouter « {word} » au vocabulaire',
    "Read from here": "Lire à partir d'ici",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Source",
    "Added manually": "Ajouté manuellement",
    "From reader": "Depuis le lecteur",
    "Created at": "Créé le",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Ajouter avec l'IA (lemme + meilleure traduction)",
    "Add to vocabulary as is": "Ajouter au vocabulaire tel quel",
    "Thinking…": "Réflexion en cours…",
    "'{pair}' is already in your dictionary.": "« {pair} » est déjà dans votre dictionnaire.",
    "{label} — {translation} · added": "{label} — {translation} · ajouté",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Synchronisation cloud",
    "Last sync": "Dernière synchronisation",
    "Pending": "En attente",
    "never": "jamais",
    "just now": "à l'instant",
    "{n} min ago": "il y a {n} min",
    "Connected": "Connecté",
    "Not connected": "Non connecté",
    "change": "modification",
    "changes": "modifications",
    "deletion": "suppression",
    "deletions": "suppressions",
    "everything synced": "tout est synchronisé",
    "Initial sync has not completed yet.": "La synchronisation initiale n'est pas encore terminée.",
    "Sync Now": "Synchroniser maintenant",
    "Syncing…": "Synchronisation…",
    # Local-only promo state
    "{words} and {texts}": "{words} et {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Vous avez enregistré {items} ici. Connectez-vous pour les sécuriser et étudier sur tous vos appareils.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Local uniquement — connectez-vous pour synchroniser vos mots entre vos appareils",
    "Sign in to sync across devices": "Se connecter pour synchroniser",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Bienvenue",
    "Welcome to {app}": "Bienvenue dans {app}",
    "Sync across your devices": "Synchronisez sur tous vos appareils",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Connectez-vous pour conserver votre vocabulaire en toute sécurité et l'étudier sur chaque appareil.",
    "Automatic cloud backup": "Sauvegarde automatique dans le cloud",
    "Your words follow you to every computer.":
        "Vos mots vous suivent sur tous vos ordinateurs.",
    "Never lose your progress.": "Ne perdez jamais votre progression.",
    "Study anywhere": "Étudiez n'importe où",
    "Pick up right where you left off.":
        "Reprenez exactement là où vous vous étiez arrêté.",
    "Your data is yours — sign in only to sync it.":
        "Vos données vous appartiennent — connectez-vous uniquement pour les synchroniser.",
    "Sign in / Create account": "Se connecter / Créer un compte",
    "Continue on this device": "Continuer sur cet appareil",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Paramètres de lecture",
    "Previous word": "Mot précédent",
    "Next word": "Mot suivant",
    "Stop playback": "Arrêter la lecture",
    "Pause between words": "Pause entre les mots",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Rien à lire.",
    "Previous sentence": "Phrase précédente",
    "Next sentence": "Phrase suivante",
    "Reading speed": "Vitesse de lecture",
    "Sentence {n} / {total}": "Phrase {n} / {total}",
    "buffering…": "mise en mémoire tampon…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Aperçu",
    "Learning status": "Statut d'apprentissage",
    "Activity": "Activité",
    "Review activity": "Activité de révision",
    "Breakdown": "Détails",
    "Total words": "Total de mots",
    "Mastered": "Maîtrisés",
    "In progress": "En cours",
    "Languages": "Langues",
    "Current streak": "Série actuelle",
    "Added this week": "Ajoutés cette semaine",
    "Definitions written": "Définitions rédigées",
    "Status distribution": "Répartition par statut",
    "Words added over time": "Évolution du nombre de mots",
    "Activity calendar": "Calendrier d'activité",
    "Reviews over time": "Révisions au fil du temps",
    "Review calendar": "Calendrier de révision",
    "Most reviewed words": "Mots les plus révisés",
    "Top language pairs": "Meilleures paires de langues",
    "Top tags": "Principales étiquettes",
    "Reviewed this week": "Révisés cette semaine",
    "Total reviews": "Total des révisions",
    "Review streak": "Série de révisions",
    "{pct}% of all words": "{pct}% de tous les mots",
    "actively learning": "en cours d'apprentissage actif",
    "{n} pairs": "{n} paire(s)",
    "best {n}d": "record {n} j.",
    "{n} today": "{n} aujourd'hui",
    "listens logged": "écoutes enregistrées",
    "keep it going": "continuez comme ça !",
    "Day": "Jour",
    "Week": "Semaine",
    "Month": "Mois",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Importer des fichiers texte",
    "Text files (*.txt);;All files (*)": "Fichiers texte (*.txt);;Tous les fichiers (*)",
    "Language of the imported text(s):": "Langue du/des texte(s) importé(s) :",
    "Imported {count} text(s).": "{count} texte(s) importé(s).",
    "Some files could not be imported:": "Certains fichiers n'ont pas pu être importés :",
    "Import failed:\n{error}": "L'importation a échoué :\n{error}",
    "Failed to save text:\n{error}": "Échec de l'enregistrement du texte :\n{error}",
    "Failed to delete text:\n{error}": "Échec de la suppression du texte :\n{error}",
    "Delete Text": "Supprimer le texte",
    "Delete '{title}'?": "Supprimer « {title} » ?",
    "Unsupported language: {language}": "Langue non prise en charge : {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Langue non prise en charge : {lang}. Choisissez-en une dans la liste.",
    "(empty)": "(vide)",
    "unsupported language": "langue non prise en charge",
    "unreadable text": "texte illisible",
    "Skipped {n} {noun} ({reasons}).": "{n} {noun} ignoré(s) ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Certains textes n'ont pas pu être lus à haute voix — langue non prise en charge "
        "ou caractères illisibles.",
    "Edit text": "Modifier le texte",
    "Done editing": "Modifier terminé",
    "Delete text": "Supprimer le texte",
    "Save Changes": "Enregistrer les modifications",
    "Paper mode": "Mode papier",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Cliquez sur « + » pour rédiger ou coller un texte, sur le globe pour en télécharger un\n"
        "depuis Internet, ou sélectionnez des mots dans la vue Mots et\n"
        "utilisez l'action « Texte » pour générer un texte d'étude."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Recherche sur Wikipédia dans la langue sélectionnée. Cliquez sur un résultat pour charger l'article ; utilisez « Adapter à mon niveau » pour le simplifier."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Flux d'actualités pour la langue sélectionnée. Chargez un flux, puis double-cliquez sur une entrée pour obtenir son texte intégral. Ajoutez vos propres flux avec « Ajouter un flux… »."
    ),
    "Length:": "Longueur :",
    "Search Wikipedia (in the selected language)…": "Rechercher sur Wikipédia (dans la langue sélectionnée)…",
    "Double-click an entry to load its full text.": "Double-cliquez sur une entrée pour charger son texte intégral.",
    "Working…": "Traitement en cours…",
    "Show the {count} result(s) again": "Afficher à nouveau le(s) {count} résultat(s)",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "La clé API {ai} n'est pas définie. Configurez-la dans Paramètres → Traduction & IA → IA."
    ),
    "Generating with {ai}…": "Génération avec {ai}…",
    'Fetching "{title}"…': "Récupération de « {title} »…",
    "(yours)": "(le vôtre)",
    "Fetching the full text…": "Récupération du texte intégral…",
    "Add feed": "Ajouter un flux",
    "Feed name:": "Nom du flux :",
    "Feed URL:": "URL du flux :",
    "Failed to save the text.": "Échec de l'enregistrement du texte.",
    "Failed to save the text: {error}": "Échec de l'enregistrement du texte : {error}",
    "'{title}' saved.": "« {title} » enregistré.",
    "(untitled)": "(sans titre)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Réécrire le texte ci-dessous pour le niveau CECRL sélectionné avec {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Exporter le journal",
    "Activity Log": "Journal d'activité",
    "Warnings & errors": "Avertissements & erreurs",
    "Errors only": "Erreurs uniquement",
    "Find…": "Rechercher…",
    "Open log folder": "Ouvrir le dossier des journaux",
    "Export diagnostics": "Exporter les diagnostics",
    "Clear the log file? This cannot be undone.":
        "Effacer le fichier journal ? Cette action est irréversible.",
    "Could not create the diagnostics file.":
        "Impossible de créer le fichier de diagnostic.",
    "Diagnostics saved to:\n{path}": "Diagnostics enregistrés dans :\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Décrivez le problème**\n\n\n**Étapes pour reproduire**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nVeuillez joindre le fichier de diagnostic :\n{path}\n",
    "Bug report: ": "Rapport de bogue : ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Réduire",
    "Maximize": "Agrandir",
    "Restore": "Restaurer",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Afficher les commandes",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Aucune couleur",
    "None": "Aucun",
    "Choose Color": "Choisir la couleur",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Synchronisation cloud : inactive",
    "Failed to open table:\n{error}": "Échec de l'ouverture du tableau :\n{error}",
    "Failed to save template:\n{error}": "Échec de l'enregistrement du modèle :\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Afficher / masquer",
    "Excel options": "Options Excel",
    "CSV options": "Options CSV",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Les lignes d'en-tête sont écrites en haut du fichier — les outils d'importation "
        "comme Anki les lisent (ex : #separator:tab, #html:true). "
        "Les noms de colonnes eux-mêmes ne sont pas écrits."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Copiez un fichier .ttf dans le dossier des polices de l'application et utilisez-le"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Utilisé uniquement lors de l'exportation de mots vers un fichier MP3. "
        "La voix elle-même se configure dans l'onglet Audio."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "La voix utilisée partout où les mots sont énoncés : lecture à haute voix "
        "dans l'application et exportation MP3. gTTS est gratuit et ne nécessite aucune configuration. Google Cloud TTS "
        "nécessite une clé JSON de compte de service (Cloud Console → IAM & Admin → "
        "Service Accounts → Keys) et l'activation de la facturation — "
        "l'utilisation dans la limite du quota mensuel gratuit n'est pas facturée."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "L'écoute complète d'un mot dans la fonction de lecture le fait progresser sur l'échelle "
        "de familiarité : Nouveau → En révision → En apprentissage → Maîtrisé. Chaque "
        "nombre représente le nombre total d'écoutes nécessaires pour atteindre ce niveau — "
        "l'exposition passive étant faible, des valeurs élevées sont normales. Les mots que vous avez "
        "définis vous-même sur Maîtrisé ou Ignoré ne sont jamais modifiés, et un mot "
        "n'est jamais rétrogradé."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Enregistrer un fichier .xlsx prêt à l'emploi avec les bons en-têtes et des exemples de lignes"
    ),
    "Google Translate (free)": "Google Traduction (gratuit)",
    "Google Translate is free and needs no API key.": (
        "Google Traduction est gratuit et ne nécessite aucune clé API."
    ),
    "Usage": "Utilisation",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Cliquez sur le champ et appuyez sur la combinaison de touches souhaitée — cela ouvre "
        "« Ajouter un mot » avec le contenu du presse-papiers depuis n'importe où. "
        "Laissez vide pour désactiver."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Sur Wayland, ce raccourci est enregistré auprès de votre "
        "environnement et apparaît dans les paramètres de clavier du système."
    ),
    "Add Word hotkey": "Raccourci « Ajouter un mot »",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "Le raccourci global « Ajouter un mot » n'est pas disponible dans cet "
        "environnement. Consultez Paramètres ▸ Système pour plus d'options."
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "Le raccourci global « Ajouter un mot » n'est pas disponible dans le bac à sable "
        "{sandbox} sous Wayland."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "Le raccourci global « Ajouter un mot » n'est pas encore pris en charge "
        "sur ce bureau Wayland."
    ),
    "To enable it, use any one of these:": "Pour l'activer, utilisez l'une de ces méthodes :",
    "Log in to an X11 session instead of Wayland":
        "connectez-vous à une session X11 au lieu de Wayland",
    "Use a GNOME session — the global hotkey works there":
        "utilisez une session GNOME — le raccourci global y fonctionne",
    "Install the AppImage version — it runs outside the sandbox":
        "installez la version AppImage — elle s'exécute en dehors du bac à sable",
    "Download the AppImage": "Télécharger l'AppImage",
    "Add font…": "Ajouter une police…",
    "TrueType fonts (*.ttf)": "Polices TrueType (*.ttf)",
    "Could not copy the font file:\n{error}": "Impossible de copier le fichier de police :\n{error}",
    "Save import template…": "Enregistrer le modèle d'importation…",
    "Excel files (*.xlsx)": "Fichiers Excel (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Modèle enregistré dans :\n{path}\n\n"
        "Remplissez-le avec vos mots (remplacez les lignes d'exemple) "
        "et importez-le via le menu de l'application → Importer Excel dans la base de données."
    ),
    "Could not save the template:\n{error}": "Impossible d'enregistrer le modèle :\n{error}",
    "Background image": "Image de fond",
    "Images (*.png *.jpg *.jpeg)": "Images (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "Fichiers JSON (*.json)",
    "Connection successful! ✅": "Connexion réussie ! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "Impossible de se connecter. Vérifiez l'URL/clé et votre connexion Internet."
    ),
    "Connection test failed:\n{error}": "Échec du test de connexion :\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} caractères cette période",
    "{count} characters used": "{count} caractères utilisés",
    "Autostart": "Démarrage automatique",
    "Could not update autostart entry:\n{error}": "Impossible de mettre à jour l'entrée de démarrage automatique :\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS est sélectionné mais {problem}\n\n"
        "L'audio basculera sur gTTS tant que ce problème n'est pas résolu."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "mot",
    "words": "mots",
    "words (genitive)": "mots",
    "text": "texte",
    "texts": "textes",
    "texts (genitive)": "textes",
    "tag": "étiquette",
    "tags": "étiquettes",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Traduire",
    "AI": "IA",
    "Save As": "Enregistrer sous",
    "Save Audio As": "Enregistrer l'audio sous",
    "Save PDF As": "Enregistrer le PDF sous",
    "Added": "Ajouté",
    "Updated": "Mis à jour",
    "Failed": "Échec",
    "Checking…": "Vérification…",
    "Cleanup": "Nettoyage",
    "Permanent Delete": "Suppression définitive",
    "No word": "Aucun mot",
    "Category": "Catégorie",
    "Bin": "Corbeille",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Toutes les étiquettes",
    "Filter by tag — {tag}": "Filtrer par étiquette — {tag}",
    "(showing first {n})": "(affichage des {n} premiers)",
    "Texts: {total}": "Textes : {total}",
    "Deleted with {n} error(s).": "Supprimé avec {n} erreur(s).",
    "Failed to update: {error}": "Échec de la mise à jour : {error}",
    "Failed to export:\n{error}": "Échec de l'exportation :\n{error}",
    "Failed to export PDF:\n{error}": "Échec de l'exportation du PDF :\n{error}",
    "Failed to export TXT:\n{error}": "Échec de l'exportation du TXT :\n{error}",
    "PDF saved to {path}": "PDF enregistré sous {path}",
    "TXT file saved to {path}": "Fichier TXT enregistré sous {path}",
    "Template saved to {path}": "Modèle enregistré sous {path}",
    "{format} file saved to {path}": "Fichier {format} enregistré sous {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Utilisation de gTTS à la place — {problem}\nCorrigez cela dans Paramètres → Lecture à haute voix → Audio."
    ),
    "Failed to load the database:": "Échec du chargement de la base de données :",
    "{selected} of {total} selected": "{selected} sur {total} sélectionné(s)",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "Réduire la barre latérale",
    "Expand sidebar": "Agrandir la barre latérale",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Enregistré {when} · {summary}",
    "the version from {date}": "la version du {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Désolé, cette version n'a pas pu être restaurée :\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Désolé, cette version n'a pas pu être supprimée :\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "Restaurer {count} élément(s) ?",
    "Restored {count} item(s).": "{count} élément(s) restauré(s).",
    "Select item(s) to restore.": "Sélectionnez le(s) élément(s) à restaurer.",
    "Permanently deleted {count} item(s).": "{count} élément(s) supprimé(s) définitivement.",
    "Select item(s) to delete permanently.": "Sélectionnez le(s) élément(s) à supprimer définitivement.",
    "No items older than {n} days found.": "Aucun élément de plus de {n} jours trouvé.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "Supprimer définitivement les éléments supprimés il y a plus de {days} jours ?\n\n"
        "Cette action est irréversible !"
    ),
    "Permanently deleted {count} old item(s).": "{count} ancien(s) élément(s) supprimé(s) définitivement.",
    "Failed to load deleted items:\n{error}": "Échec du chargement des éléments supprimés :\n{error}",
    "Failed to count old items:\n{error}": "Échec du comptage des anciens éléments :\n{error}",
    "Failed to cleanup:\n{error}": "Échec du nettoyage :\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Importer Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Colonnes attendues : Language1, Language2, Word1, Word2 — nommées dans la ligne d'en-tête, "
        "ou sans en-tête avec les quatre premières colonnes dans cet ordre. "
        "Un modèle prêt à l'emploi est disponible dans le menu → Enregistrer le modèle d'importation."
    ),
    "All ({n})": "Tous ({n})",
    "To add ({n})": "À ajouter ({n})",
    "To update ({n})": "À mettre à jour ({n})",
    "Skipped ({n})": "Ignorés ({n})",
    "Unrecognized ({n})": "Non reconnus ({n})",
    " · {n} with unrecognized language": " · {n} avec langue non reconnue",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} lignes : {add} nouvelles · {update} mises à jour · {skip} ignorées"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Vérifiez les modifications proposées, puis importez les lignes sélectionnées."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Rien à importer — aucune entrée nouvelle ou modifiée trouvée."
    ),
    "Analyzing file…": "Analyse du fichier…",
    "Could not read the Excel file — see the activity log.": (
        "Impossible de lire le fichier Excel — consultez le journal d'activité."
    ),
    "Analysis failed — see the activity log.": "L'analyse a échoué — consultez le journal d'activité.",
    "Import failed": "Échec de l'importation",
    "Import failed — see the activity log.": "L'importation a échoué — consultez le journal d'activité.",
    "Importing…": "Importation…",
    "Importing {count} item(s)…": "Importation de {count} élément(s)…",
    "Import {count} Item(s)": "Importer {count} élément(s)",
    "Import finished:": "Importation terminée :",
    "Backup failed — see the activity log.": "La sauvegarde a échoué — consultez le journal d'activité.",
    "{n} added": "{n} ajouté(s)",
    "{n} updated": "{n} mis à jour",
    "{n} failed": "{n} a/ont échoué",
    "{n} failed.": "{n} a/ont échoué.",
    "Export Import Log": "Exporter le journal d'importation",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Définition — {word}",
    "Failed to save definition:\n{error}": "Échec de l'enregistrement de la définition :\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Modifier — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Échec de l'enregistrement du mot :\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Associer la/les étiquette(s) sélectionnée(s) à chaque mot sélectionné"
    ),
    "Failed to add tag:\n{error}": "Échec de l'ajout de l'étiquette :\n{error}",
    "Failed to apply tags:\n{error}": "Échec de l'application des étiquettes :\n{error}",
    "Failed to remove tags:\n{error}": "Échec du retrait des étiquettes :\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Génère un texte avec l'IA en utilisant les champs Langue, Niveau et Sujet ci-dessous. "
        "Sélectionnez un sujet ou saisissez le vôtre."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Génération d'un texte en {language} à partir de {count} mot(s) avec {ai} :"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Saisissez ou collez un texte dans l'éditeur ci-dessous, donnez-lui un titre, "
        "définissez la langue — puis enregistrez."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Extrait le texte lisible de l'article à partir de n'importe quelle page web. "
        "Les pages nécessitant une connexion ou conçues uniquement en JavaScript peuvent ne pas fonctionner."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "Voir la définition (double-clic)",
    "Read selected words aloud": "Lire les mots sélectionnés à haute voix",
    "Toggle favorite": "Ajouter/retirer des favoris",
    "Add / remove tags": "Ajouter / supprimer des étiquettes",
    "Edit word": "Modifier le mot",
    "Copy words": "Copier les mots",
    "Generate text from selection": "Générer un texte à partir de la sélection",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "Fichiers PDF (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Fichiers Excel (*.xlsx *.xls)",
    "CSV files (*.csv)": "Fichiers CSV (*.csv)",
    "Text files (*.txt)": "Fichiers texte (*.txt)",
    "MP3 files (*.mp3)": "Fichiers MP3 (*.mp3)",
    "Open Excel Table": "Ouvrir le tableau Excel",
    "Save Import Template": "Enregistrer le modèle d'importation",

    # Cloud sync status
    "Cloud sync": "Synchronisation cloud",
    "Not connected. Check internet or credentials": "Non connecté. Vérifiez Internet ou vos identifiants",
    "Syncing with cloud…": "Synchronisation avec le cloud…",
    "Sync completed successfully": "Synchronisation terminée avec succès",
    "Sync enabled but not connected. Check settings.": "Synchronisation activée mais non connectée. Vérifiez les paramètres.",
    "idle": "inactive",
    "syncing": "synchronisation",
    "success": "succès",
    "error": "erreur",

    # Chart empty states
    "No data yet": "Pas encore de données",
    "No activity yet": "Pas encore d'activité",
    "Not enough activity yet": "Pas encore assez d'activité",

    # Settings tabs
    "APIs": "API",
    "Audio (MP3)": "Audio (MP3)",
    "Sync": "Synchronisation",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "Clé API OpenAI (.env)",
    "Google API key (.env)": "Clé API Google (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Facturé à l\'utilisation — obtenez une clé sur <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modèles : gpt-4o-mini, gpt-4o, gpt-4.1-mini… Utilisation de l\'API — voir le <a href="https://platform.openai.com/usage">tableau de bord</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Offre gratuite disponible — obtenez une clé sur <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modèles : gemini-2.5-flash, gemini-2.5-flash-lite… Utilisation de l\'API — voir <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Obtenez une clé sur <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Utilisez https://api-free.deepl.com/v2/translate pour les clés d\'accès gratuit.',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Préparez un fichier Excel avec les colonnes <b>Language1, Language2, Word1, Word2</b> — nommées ainsi dans une ligne d'en-tête (les colonnes supplémentaires sont ignorées), ou sans en-tête avec les quatre premières colonnes exactement dans cet ordre.</li><li>Ouvrez le menu de l'application → <i>Importer Excel dans la base de données…</i> et choisissez le fichier.</li><li>Vérifiez les lignes proposées et cliquez sur <i>Importer</i>.</li></ol>",

    # About dialog
    "created by": "créé par",
    "Version": "Version",
    "Build": "Version de build",
    "Your personal vocabulary companion": "Votre compagnon de vocabulaire personnel",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Enrichissez, étudiez et mémorisez du vocabulaire dans plusieurs langues — avec synchronisation cloud, définitions assistées par IA, traductions, synthèse vocale et exportation flexible.",
    "Source code": "Code source",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Votre compagnon de vocabulaire personnel avec synchronisation cloud, définitions IA, traductions, synthèse vocale et options d'exportation.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Sous licence GNU Affero General Public License v3.0. Cette attribution doit être conservée (AGPL §7).",
    "Found a bug or have an idea?": "Vous avez trouvé un bogue ou avez une idée ?",
    "Report an issue": "Signaler un problème",
    "What would you like to report?": "Que souhaitez-vous signaler ?",
    "A bug or technical problem": "Un bogue ou un problème technique",
    "Creates a report with app diagnostics to send to the developers.":
        "Crée un rapport de diagnostic de l'application à envoyer aux développeurs.",
    "Inappropriate AI-generated content": "Contenu inapproprié généré par l'IA",
    "Report a definition, text, or translation the AI produced.":
        "Signaler une définition, un texte ou une traduction produit par l'IA.",
    "Report: inappropriate AI-generated content":
        "Signalement : contenu inapproprié généré par l'IA",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Veuillez décrire le contenu généré par l'IA que vous signalez.\n\n"
        "Où il est apparu (définition / texte généré / traduction du mot) :\n"
        "Le mot ou le texte en question :\n"
        "Pourquoi il est inapproprié :\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "Pour signaler un contenu inapproprié généré par l'IA, envoyez-nous un e-mail à {email}.",

    # Support dialog
    "Support": "Soutenir",
    "Support Lingueez": "Soutenir Lingueez",
    "Lingueez is free and open-source.": "Lingueez est gratuit et open-source.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Si vous appréciez Lingueez et le trouvez utile, une contribution ponctuelle aide à couvrir les coûts des serveurs de synchronisation optionnels et soutient le développement. Il n'y a pas d'accès payant — chaque fonctionnalité reste gratuite dans tous les cas.",
    "Support Lingueez's development": "Soutenir le développement de Lingueez",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "L'option Stripe est ponctuelle — sans abonnement. Les paiements sont traités en toute sécurité par Stripe ou GitHub.",

    # Updates
    "Updates": "Mises à jour",
    "Check for updates": "Vérifier les mises à jour",
    "You're up to date.": "Votre application est à jour.",
    "Update available": "Mise à jour disponible",
    "Update available — v{version}": "Mise à jour disponible — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} est disponible — vous possédez la version {current}.",
    "Skip this version": "Ignorer cette version",
    "Later": "Plus tard",
    "Download": "Télécharger",
    "Check for updates on startup": "Vérifier les mises à jour au démarrage",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Vérifie une fois par jour la présence d'une nouvelle version et vous informe ; "
        "rien n'est jamais téléchargé ni installé automatiquement.",

    # Misc units
    "in": "po",
    " s": " s",

    # Word statuses
    "New": "Nouveau",
    "To Learn": "À apprendre",
    "Reviewing": "En révision",
    "Ignored": "Ignoré",
    "Undo": "Annuler",
    "Restored": "Restauré",
    "Ignore word": "Ignorer le mot",
    "Ignore this word": "Ignorer ce mot",
    "Already ignored.": "Déjà ignoré.",
    "{count} word(s) won't come up in practice.": "{count} mot(s) n'apparaîtra(ont) plus dans les exercices.",
    "'{word}' is back in rotation": "« {word} » revient dans les exercices",
    "'{word}' won't come up again": "« {word} » n'apparaîtra plus",
    "Mark for relearning": "Marquer à réapprendre",
    "Forgot this word — move it to To Learn": "Mot oublié — déplacer vers « À apprendre »",
    "'{word}' is queued to learn again": "« {word} » est à réapprendre",
    "{count} word(s) queued to learn again.": "{count} mot(s) à réapprendre.",
    "Nothing here to relearn yet.": "Rien à réapprendre pour l'instant.",

    # Table density
    "Compact": "Compact",
    "Normal": "Normal",
    "Comfortable": "Confortable",
    "Spacious": "Spacieux",

    # Language names
    "English": "Anglais",
    "German": "Allemand",
    "Spanish": "Espagnol",
    "Ukrainian": "Ukrainien",
    "French": "Français",
    "Italian": "Italien",
    "Portuguese": "Portugais",
    "Russian": "Russe",
    "Greek": "Grec",
    "Arabic": "Arabe",
    "Bengali": "Bengali",
    "Cantonese": "Cantonais",
    "Hindi": "Hindi",
    "Japanese": "Japonais",
    "Korean": "Coréen",
    "Mandarin": "Mandarin",
    "Polish": "Polonais",
    "Turkish": "Turc",
    "Vietnamese": "Vietnamien",
    "Afrikaans": "Afrikaans",
    "Albanian": "Albanais",
    "Amharic": "Amharique",
    "Armenian": "Arménien",
    "Azerbaijani": "Azéri",
    "Basque": "Basque",
    "Belarusian": "Biélorusse",
    "Bosnian": "Bosnien",
    "Bulgarian": "Bulgare",
    "Catalan": "Catalan",
    "Cebuano": "Cebuano",
    "Chichewa": "Chichewa",
    "Chinese": "Chinois",
    "Croatian": "Croate",
    "Czech": "Tchèque",
    "Danish": "Danois",
    "Dutch": "Néerlandais",
    "Estonian": "Estonien",
    "Filipino": "Filipino",
    "Finnish": "Finnois",
    "Galician": "Galicien",
    "Georgian": "Géorgien",
    "Gujarati": "Goudjarati",
    "Haitian Creole": "Créole haïtien",
    "Hausa": "Haoussa",
    "Hawaiian": "Hawaïen",
    "Hebrew": "Hébreu",
    "Hmong": "Hmong",
    "Hungarian": "Hongrois",
    "Icelandic": "Islandais",
    "Igbo": "Igbo",
    "Indonesian": "Indonésien",
    "Irish": "Irlandais",
    "Javanese": "Javanais",
    "Kannada": "Kannada",
    "Kazakh": "Kazakhe",
    "Khmer": "Khmer",
    "Kinyarwanda": "Kinyarwanda",
    "Kyrgyz": "Kirghize",
    "Lao": "Laotien",
    "Latin": "Latin",
    "Latvian": "Letton",
    "Lithuanian": "Lituanien",
    "Luxembourgish": "Luxembourgeois",
    "Macedonian": "Macédonien",
    "Malagasy": "Malgache",
    "Malay": "Malais",
    "Malayalam": "Malayalam",
    "Maltese": "Maltais",
    "Maori": "Maori",
    "Marathi": "Marathi",
    "Mongolian": "Mongol",
    "Myanmar (Burmese)": "Birman",
    "Nepali": "Népalais",
    "Norwegian": "Norvégien",
    "Odia": "Odia",
    "Pashto": "Pachto",
    "Persian": "Persan",
    "Punjabi": "Pendjabi",
    "Romanian": "Roumain",
    "Samoan": "Samoan",
    "Scots Gaelic": "Gaélique écossais",
    "Serbian": "Serbe",
    "Sesotho": "Sesotho",
    "Shona": "Shona",
    "Sindhi": "Sindhi",
    "Sinhala": "Cingalais",
    "Slovak": "Slovaque",
    "Slovenian": "Slovène",
    "Somali": "Somali",
    "Sundanese": "Sondanais",
    "Swahili": "Swahili",
    "Swedish": "Suédois",
    "Tajik": "Tadjik",
    "Tamil": "Tamoul",
    "Tatar": "Tatar",
    "Telugu": "Télougou",
    "Thai": "Thaï",
    "Turkmen": "Turkmène",
    "Urdu": "Ourdou",
    "Uyghur": "Ouïghour",
    "Uzbek": "Ouzbek",
    "Welsh": "Gallois",
    "Xhosa": "Xhosa",
    "Yiddish": "Yiddish",
    "Yoruba": "Yoruba",
    "Zulu": "Zoulou",
    # --- Onboarding tour ---
    "Back": "Retour",
    "Next": "Suivant",
    "Done": "Terminé",
    "Show Tour": "Afficher la visite",
    "Step {n} of {total}": "Étape {n} sur {total}",
    "Your library": "Votre bibliothèque",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Basculez entre vos Mots, Textes et Statistiques depuis cette barre latérale.",
    "Add a word": "Ajouter un mot",
    "Find anything": "Trouvez n'importe quoi",
    "Search across your words, translations and tags as you type.":
        "Recherchez parmi vos mots, traductions et étiquettes lors de la saisie.",
    "Add a new word here — its translation can be fetched automatically.":
        "Ajoutez un nouveau mot ici — sa traduction peut être récupérée automatiquement.",
    "Listen and learn": "Écoutez et apprenez",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Sélectionnez des mots et appuyez sur Lire pour les entendre à haute voix. L'écoute "
        "répétée fait passer chaque mot de Nouveau à En révision, En apprentissage "
        "puis Maîtrisé.",
    "Generate a text": "Générer un texte",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Transformez les mots sélectionnés en une courte histoire écrite par l'IA — "
        "votre vocabulaire en contexte.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Votre vocabulaire reste synchronisé sur tous vos appareils. Cliquez pour "
        "voir le statut ou synchroniser maintenant.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Activez la synchronisation cloud, changez de langue, d'apparence et "
        "plus encore dans les Paramètres.",
    # --- Texts tour ---
    "Add texts": "Ajoutez des textes",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Rédigez ou collez un texte, récupérez-en un sur Internet "
        "(IA / Wikipédia / URL / RSS) ou importez des fichiers .txt.",
    "Your texts": "Vos textes",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Parcourez vos textes enregistrés et filtrez-les par langue, "
        "niveau ou sujet.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Écoutez n'importe quel texte à haute voix — et cliquez sur un mot pendant la lecture "
        "pour voir sa traduction ou l'ajouter à votre vocabulaire.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Affichez une traduction parallèle côte à côte ; choisissez la langue "
        "avec la flèche à côté.",
    "Reading modes": "Modes de lecture",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "Le mode concentration masque la liste, le mode papier modifie "
        "l'arrière-plan et Modifier vous permet d'ajuster le texte.",
    # --- Flashcards tour ---
    "Choose your deck": "Choisissez votre paquet",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Choisissez le contenu du paquet — cartes à réviser, "
        "mots de votre filtre actuel, ajouts récents, "
        "ou une sélection personnalisée.",
    "Shape the session": "Configurez la session",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Définissez le nombre de cartes à réviser, mélangez l'ordre et "
        "faites prononcer chaque carte lorsqu'elle apparaît et se retourne.",
    "Preview the deck": "Aperçu du paquet",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Les cartes exactes contenues dans votre session. Cliquez sur une carte pour "
        "lire ou modifier sa définition, ou sur l'haut-parleur pour entendre "
        "le mot.",
    "Review and grade": "Révisez et évaluez",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Retournez chaque carte et évaluez votre maîtrise — Difficile, "
        "Bon ou Facile. La répétition espacée détermine le retour des cartes : "
        "les mots faciles attendent plus longtemps, les difficiles reviennent "
        "plus vite. Espace retourne la carte, 1 à 3 attribue la note.",
    "Or just listen": "Ou écoutez simplement",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "« Lire le paquet » transforme la session en audio — les cartes avancent "
        "et se retournent en rythme avec la voix. Mettez en pause à tout moment pour évaluer "
        "une carte vous-même.",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Votre vocabulaire en un coup d'œil — totaux, mots maîtrisés, "
        "langues et votre série actuelle.",
    "See how your vocabulary has grown over time.":
        "Observez comment votre vocabulaire s'est développé au fil du temps.",
    "Track how much you've reviewed over time.":
        "Suivez l'évolution de vos révisions au fil du temps.",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Exemple : Une promenade en ville",
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
        "Le matin était radieux et les rues étaient calmes. Une jeune femme "
        "marchait lentement le long de la vieille route, admirant les hautes maisons et les "
        "petits commerces qui ouvraient à peine. Elle s'arrêta pour acheter du pain "
        "frais et une tasse de café, puis traversa la place en direction du parc. "
        "Des enfants jouaient près de la rivière pendant que leurs parents discutaient sur les "
        "bancs à proximité. Elle s'assit sous un grand arbre, ouvrit son livre et "
        "commença à lire. L'histoire parlait d'un voyageur qui traversait les "
        "montagnes à la recherche d'un vieil ami qu'il n'avait pas vu depuis de nombreuses années. "
        "Au bout d'un moment, elle leva les yeux, observant les bateaux dériver lentement le long du "
        "fleuve et les oiseaux tournoyer haut au-dessus des toits. Un musicien de rue "
        "commença à jouer non loin de là, et les douces notes accompagnèrent ses "
        "pensées. C'était un matin calme et heureux, comme elle les aimait tant.",
    "Demo": "Démo",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Clé API OpenAI non valide. Vérifiez-la dans Paramètres → Traduction & IA → IA → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Votre compte OpenAI n'a plus de crédits. Ajoutez des crédits sur "
        "platform.openai.com/account/billing, ou changez de fournisseur "
        "pour Gemini dans Paramètres → Traduction & IA → IA.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "Limite de requêtes OpenAI atteinte. Patientez un instant et réessayez.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Modèle OpenAI inconnu. Vérifiez le nom du modèle dans Paramètres → Traduction & IA → IA → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "Impossible de contacter OpenAI. Vérifiez votre connexion Internet.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Quota Gemini épuisé. L'offre gratuite se réinitialise quotidiennement ; attendez, "
        "ou créez une nouvelle clé sur aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Clé API Google non valide. Vérifiez-la dans Paramètres → Traduction & IA → IA → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Modèle Gemini inconnu. Vérifiez le nom du modèle dans Paramètres → Traduction & IA → IA → Gemini.",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "Votre aventure linguistique commence ici",
    "Add your first word — its translation can be fetched automatically.":
        "Ajoutez votre premier mot — sa traduction peut être récupérée automatiquement.",
    "Add your first word": "Ajouter votre premier mot",
    "Take the tour": "Faire la visite guidée",
    "No matching words": "Aucun mot correspondant",
    "Try a different search or filter.": "Essayez une autre recherche ou un autre filtre.",
    "Clear filters": "Effacer les filtres",
    # --- Texts empty state ---
    "Your reading library starts here": "Votre bibliothèque de lecture commence ici",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Ajoutez un texte à lire — rédigez ou collez le vôtre, récupérez-en un sur "
        "Internet ou importez un fichier .txt.",
    "Add a text": "Ajouter un texte",
    "Fetch from the Internet": "Obtenir depuis Internet",
    "Import .txt": "Importer .txt",
    # demo text-list stub titles
    "My first story": "Ma première histoire",
    "A news article": "Un article de presse",
    "A short poem": "Un court poème",
    "Travel notes": "Carnet de voyage",
    # demo text-list stub first sentences
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Il était une fois, dans un petit village au bord de la mer, "
        "un jeune renard très curieux.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Des chercheurs ont découvert une nouvelle méthode pour étudier la façon dont "
        "les langues évoluent et se développent au fil des siècles.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "Le vent souffle doucement à travers les arbres d'automne, "
        "emportant de vieilles chansons à demi oubliées.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Premier jour : nous sommes arrivés en ville tard dans la nuit, et les "
        "rues étaient encore baignées d'une lumière chaleureuse.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Éléments supprimés sur un autre appareil",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Pendant que cet appareil était hors ligne, {n} élément(s) ont été supprimés sur vos "
        "autres appareils. Les conserver dans le cloud ou les retirer de cet appareil ?",
    "(untitled)": "(sans titre)",
    "[Text] {title}": "[Texte] {title}",
    "Remove from this device": "Retirer de cet appareil",
    "Decide later": "Décider plus tard",
    "Keep & upload": "Conserver & téléverser",
    "Not now": "Pas maintenant",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Saisissez un nom pour le profil hors ligne.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Vous pouvez conserver jusqu'à {max} profils hors ligne. Supprimez-en un pour en ajouter un autre.",
    "New offline profile": "Nouveau profil hors ligne",
    "Profile name:": "Nom du profil :",
    "Offline profile": "Profil hors ligne",
    "Rename offline profile": "Renommer le profil hors ligne",
    "Offline profiles": "Profils hors ligne",
    "Add offline profile…": "Ajouter un profil hors ligne…",
    "Profile actions": "Actions du profil",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Bibliothèques indépendantes réservées à cet appareil avec leur propre base de données. Elles ne se synchronisent jamais et ne nécessitent aucune connexion.",
    "Default (local)": "Par défaut (local)",
    "Rename": "Renommer",
    "Delete offline profile": "Supprimer le profil hors ligne",
    "Enable cloud sync…": "Activer la synchronisation cloud…",
    "Could not create the profile.": "Impossible de créer le profil.",
    "Created and switched to “{name}”.": "Profil « {name} » créé et activé.",
    "Deleted “{name}”.": "Profil « {name} » supprimé.",
    "Untitled profile": "Profil sans titre",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "Supprimer définitivement le profil hors ligne « {name} » ? Ses mots et textes n'existent que sur cet appareil — il n'y a pas de copie cloud. La base de données sera d'abord archivée dans le dossier de sauvegarde, mais cette action est irréversible dans l'application.",
    "this profile": "ce profil",
    "Connect to the internet to merge this profile into your account.": "Connectez-vous à Internet pour fusionner ce profil avec votre compte.",
    "Enable cloud sync for this profile": "Activer la synchronisation cloud pour ce profil",
    "Continue": "Continuer",
    "Upload words": "Téléverser les mots",
    "Upload texts": "Téléverser les textes",
    "Upload & sync": "Téléverser & synchroniser",
    "Could not upload this profile. Your data is unchanged.": "Impossible de téléverser ce profil. Vos données restent inchangées.",
    "“{name}” is now synced to your account.": "« {name} » est désormais synchronisé avec votre compte.",
    "Everything in this profile is already in your account.": "Tout ce qui se trouve dans ce profil est déjà présent sur votre compte.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Connectez-vous ou créez un compte pour sauvegarder « {name} » et le synchroniser sur tous vos appareils. Les mots et textes de ce profil seront téléversés et il deviendra votre compte synchronisé sur cet appareil. Une copie est d'abord archivée dans le dossier de sauvegarde.",
    "Upload “{name}” to your account": "Téléverser « {name} » sur votre compte",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Votre profil devient le compte synchronisé « {who} » sur cet appareil et est téléversé dans le cloud.",
    "Merge “{name}” into your account": "Fusionner « {name} » avec votre compte",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Ce compte possède déjà des données sur cet appareil. Les mots et textes de votre profil qui n'y figurent pas encore y seront ajoutés — rien n'est écrasé. « {name} » est ensuite archivé dans le dossier de sauvegarde puis supprimé.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Ce profil contient {items}, enregistrés uniquement sur cet appareil. Activez la synchronisation cloud pour les sauvegarder et étudier sur tous vos appareils.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Choisissez les éléments à ajouter. Ils seront copiés sur votre compte et téléversés dans le cloud. « {name} » sera ensuite archivé dans le dossier de sauvegarde puis supprimé.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "J'accepte les <a href=\"{terms}\">Conditions d'utilisation</a> et la <a href=\"{privacy}\">Politique de confidentialité</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Veuillez accepter les Conditions d'utilisation et la Politique de confidentialité pour continuer.",
    "Updated Terms & Privacy": "Conditions & Confidentialité mises à jour",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Nous avons mis à jour nos Conditions d'utilisation et notre Politique de confidentialité. Veuillez les consulter et les accepter pour continuer à utiliser votre compte.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "J'accepte les nouvelles <a href=\"{terms}\">Conditions d'utilisation</a> et la nouvelle <a href=\"{privacy}\">Politique de confidentialité</a>.",
    "Sign out": "Se déconnecter",
    "I agree": "J'accepte",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Politique de confidentialité</a> · <a href=\"{terms}\">Conditions</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "En continuant, vous acceptez les <a href=\"{terms}\">Conditions d'utilisation</a> et la <a href=\"{privacy}\">Politique de confidentialité</a>.",
    "Privacy Policy": "Politique de confidentialité",
    "Terms": "Conditions d'utilisation",
    "Website": "Site web",
    "Contact": "Contact",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Cartes mémoires",
    "Practice your vocabulary": "Pratiquez votre vocabulaire",
    "Due cards": "Cartes à réviser",
    "Current filter": "Filtre actuel",
    "Newest": "Plus récentes",
    "Selected words": "Mots sélectionnés",
    "Deck size": "Taille du paquet",
    "Default deck size": "Taille par défaut du paquet",
    "Shuffle": "Mélanger",
    "Start session": "Démarrer la session",
    "Play deck": "Lire le paquet",
    "{n} cards ready to review": "{n} carte(s) prête(s) à être révisée(s)",
    "No cards due — great job!": "Aucune carte à réviser — excellent travail !",
    "{n} selected words": "{n} mot(s) sélectionné(s)",
    "No words to practice.": "Aucun mot à pratiquer.",
    "End session": "Terminer la session",
    "Listening — pause to review manually":
        "Écoute en cours — mettez en pause pour réviser manuellement",
    "Show answer": "Afficher la réponse",
    "Hard": "Difficile",
    "Good": "Bon",
    "Easy": "Facile",
    "Space or click to flip": "Espace ou clic pour retourner",
    "Card {current} of {total}": "Carte {current} sur {total}",
    "{n} correct": "{n} correcte(s)",
    "Session complete!": "Session terminée !",
    "You listened to {n} of {total} cards.": "Vous avez écouté {n} cartes sur {total}.",
    "Correct: {n} of {total}": "Correctes : {n} sur {total}",
    "New session": "Nouvelle session",
    "Practice hard words": "Pratiquer les mots difficiles",
    "Hard words": "Mots difficiles",
    "Hard words cleared!": "Mots difficiles révisés !",
    "Open Flashcards when Read Aloud starts":
        "Ouvrir les cartes mémoires au démarrage de la lecture à haute voix",
    "Stop": "Arrêter",
    "Auto-pronounce": "Prononciation automatique",
    "Speak each card as it appears and when it flips":
        "Prononcer chaque carte lorsqu'elle apparaît et se retourne",
    "Deck preview": "Aperçu du paquet",
    "{n} cards": "{n} cartes",
    "Due": "À réviser",
    "In {n} d": "Dans {n} j",
    "{n} d": "{n} j",
    "{n} mo": "{n} mois",
    "{n} y": "{n} an(s)",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez pour Android…",
    "Android app": "Application Android",
    "Lingueez on Android": "Lingueez sur Android",
    "Take your vocabulary with you": "Emmenez votre vocabulaire partout avec vous",
    "Preview of Lingueez on a phone": "Aperçu de Lingueez sur un téléphone",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Connectez-vous à votre compte Lingueez et votre vocabulaire sera déjà là — "
        "rien à configurer, rien à transférer.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Connectez-vous avec un compte Lingueez gratuit sur les deux appareils et votre vocabulaire "
        "se synchronisera sur votre téléphone — aucun fichier à copier.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Connectez-vous avec un compte Lingueez gratuit et vos mots se synchroniseront sur votre téléphone.",
    "Synced both ways": "Synchronisation dans les deux sens",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Les mots ajoutés sur le téléphone vous attendent sur l'ordinateur, et "
        "inversement.",
    "Listen with the screen off": "Écoutez avec l'écran éteint",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Commandes sur l'écran de verrouillage pour continuer votre révision le téléphone "
        "dans la poche.",
    "Save a word from any app": "Enregistrez un mot depuis n'importe quelle application",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Partagez du texte vers Lingueez et il arrivera directement dans votre vocabulaire, prêt à "
        "être complété plus tard.",
    "Point your phone's camera at the code":
        "Pointez la caméra de votre téléphone vers le code",
    "Get it on Google Play": "Disponible sur Google Play",
    "Copy link": "Copier le lien",
    "Link copied": "Lien copié",
    "Lingueez is now on Android": "Lingueez est maintenant disponible sur Android",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Connectez-vous avec votre compte Lingueez — votre vocabulaire est déjà présent.",
    "Dismiss": "Ignorer",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Utilisez votre compte Lingueez en toute fluidité entre votre ordinateur et vos appareils Android.",
    "Get the app…": "Obtenir l'application…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Quiz",
    "Quiz (recall practice)": "Quiz (exercice de rappel)",
    "Recall your words, one question at a time":
        "Retrouvez vos mots, une question à la fois",
    "Questions": "Questions",
    "Answer with": "Répondre par",
    "Choices": "Choix",
    "Typing": "Saisie",
    "Ask": "Demander",
    "Term": "Terme",
    "Mixed": "Mixte",
    "Auto-advance": "Avance automatique",
    "Move on by itself after a correct answer":
        "Passer à la suite après une bonne réponse",
    "Speak the question, then the answer once it is revealed":
        "Prononcer la question, puis la réponse une fois révélée",
    "Start quiz": "Commencer le quiz",
    "questions ready": "questions prêtes",
    "Nothing to quiz": "Rien à réviser",
    "No words match this deck.": "Aucun mot ne correspond à ce paquet.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Un quiz demande au moins deux mots — les mauvaises réponses proviennent "
        "justement des mots sur lesquels vous n'êtes pas interrogé.",
    "Not enough words": "Pas assez de mots",
    "Add a few more words, or widen the deck.":
        "Ajoutez quelques mots ou élargissez le paquet.",
    "Question {n} of {total}": "Question {n} sur {total}",
    "Missed words": "Mots manqués",
    "End quiz": "Terminer le quiz",
    "Answer in {language}": "Répondre en {language}",
    "Type the answer": "Saisissez la réponse",
    "Check": "Vérifier",
    "Click to continue": "Cliquez pour continuer",
    "See results": "Voir les résultats",
    "Almost — it is \"{answer}\"": "Presque — c'est « {answer} »",
    "It is \"{answer}\"": "C'est « {answer} »",
    "Now {status}": "Maintenant {status}",
    "Correct": "Correct",
    "Missed": "Manqués",
    "Worth another look": "À revoir",
    "Again": "Encore",
    "Missed words cleared!": "Mots manqués maîtrisés !",
    "Perfect run": "Parcours parfait",
    "Quiz complete": "Quiz terminé",
    "Practice missed": "Revoir les erreurs",
    "Default number of questions": "Nombre de questions par défaut",
    "Move on after a correct answer": "Passer à la suite après une bonne réponse",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Choisissez ce qui sera demandé",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Les mêmes paquets que les cartes — mots à réviser, votre filtre actuel, les "
        "plus récents ou une sélection manuelle — et le nombre de questions.",
    "Choices or typing": "Choix ou saisie",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "« Choix » propose quatre réponses ; « Saisie » demande d'écrire la réponse : "
        "plus difficile, mais bien plus révélateur. La saisie pardonne les accents et "
        "les petites fautes de frappe. « Demander » décide du côté affiché : le terme, "
        "sa traduction, ou les deux en alternance.",
    "Start, and it counts": "Lancez — et ça compte",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "La barre montre la composition du paquet par statut. Chaque réponse alimente "
        "le même calendrier de répétition espacée que les cartes : un mot retrouvé "
        "revient plus tard, un mot manqué revient plus tôt.",
}

# Date names, read by app.i18n. Months are in lowercase standard French form.
WEEKDAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi",
            "Vendredi", "Samedi", "Dimanche"]
WEEKDAYS_ABBR = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin",
          "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MONTHS_ABBR = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
               "juil.", "août", "sept.", "oct.", "nov.", "déc."]