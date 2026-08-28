# Lingueez — Spanish (es) translations.
# Keys are English UI strings; values are their Spanish equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "Español"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "Cancelar",
    "OK": "Aceptar",
    "Close": "Cerrar",
    "Save": "Guardar",
    "Delete": "Eliminar",
    "Edit": "Editar",
    "Remove": "Quitar",
    "Add": "Añadir",
    "Refresh": "Actualizar",
    "Import": "Importar",
    "Export": "Exportar",
    "Search": "Buscar",
    "Fetch": "Obtener",
    "Browse…": "Examinar…",
    "Clear": "Limpiar",
    "Pause": "Pausar",
    "Resume": "Reanudar",
    "Language": "Idioma",
    "Translation": "Traducción",
    "Word": "Palabra",
    "Status": "Estado",
    "Error": "Error",
    "Title": "Título",
    "Topic": "Tema",
    "Level": "Nivel",
    "Generate": "Generar",
    "Generating…": "Generando…",
    "Translating…": "Traduciendo…",
    "Format": "Formato",
    "Style": "Estilo",
    "Model": "Modelo",
    "Font": "Fuente",
    "Usage": "Uso",
    "Translation language": "Idioma de traducción",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "Menú",
    "Open Excel Table…": "Abrir tabla de Excel…",
    "Import Excel to Database…": "Importar Excel a la base de datos…",
    "Save Import Template…": "Guardar plantilla de importación…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "Audio (MP3)…",
    "Backups…": "Copias de seguridad…",
    "Show Source column": "Mostrar columna «Origen»",
    "Show Created At column": "Mostrar columna «Fecha de creación»",
    "Max words…": "Límite de palabras…",
    "View Log": "Ver registro",
    "About": "Acerca de",
    "Quit": "Salir",
    "Words": "Palabras",
    "Texts": "Textos",
    "Statistics": "Estadísticas",
    "Bin (deleted items)": "Papelera (elementos eliminados)",
    "Settings": "Ajustes",
    "Vocabulary": "Vocabulario",
    "Search words, translations or tags…": "Buscar palabras, traducciones o etiquetas…",
    "Search texts by title, content or words…": "Buscar textos por título, contenido o palabras…",
    "Search scope": "Alcance de búsqueda",
    "Search scope…": "Alcance de búsqueda…",
    "Nothing to practice yet": "Aún no hay nada que practicar",
    "Add words to your vocabulary and they show up here.":
        "Añade palabras a tu vocabulario y aparecerán aquí.",
    "Come back when cards are due, or practice the newest words now.":
        "Vuelve cuando haya tarjetas pendientes o practica ahora las palabras más recientes.",
    "Practice newest words": "Practicar las más recientes",
    "Pick another deck above, or adjust your filters on the Words page.":
        "Elige otro mazo arriba o ajusta los filtros en la página Palabras.",
    "You're all caught up": "Estás al día",
    "Add word": "Añadir palabra",
    "Copy a word in any app, then press:":
        "Copia una palabra en cualquier app y pulsa:",
    "Set a shortcut": "Definir un atajo",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "Copia una palabra en cualquier app y pulsa {keys} para añadirla con su traducción.",
    "Set a shortcut in Settings to add copied words from any app.":
        "Define un atajo en Ajustes para añadir palabras copiadas desde cualquier app.",
    " Favorites": " Favoritos",
    " Filters": " Filtros",
    "Filters that don't fit the table": "Filtros que no caben en la tabla",
    "More actions": "Más acciones",
    "Filter by tag": "Filtrar por etiqueta",
    "Close file and return to your vocabulary": "Cerrar archivo y volver a tu vocabulario",
    "Definition": "Definición",
    "Read": "Leer",
    "Favorite": "Favorito",
    "Tags": "Etiquetas",
    "Copy": "Copiar",
    "Text": "Texto",
    "Delete selected (Del)": "Eliminar seleccionados (Supr)",
    "No data": "Sin datos",
    "No texts yet": "Aún no hay textos",
    "Words: {shown}/{total}": "Palabras: {shown}/{total}",
    "Texts: {total}": "Textos: {total}",
    "Texts: {shown}/{total}": "Textos: {shown}/{total}",
    "{count} selected": "{count} seleccionado(s)",
    "No selection": "Ninguna selección",
    "Please select at least one word.": "Por favor, selecciona al menos una palabra.",
    "Saved": "Guardado",
    "'{word}' updated.": "«{word}» actualizada.",
    "Database Error": "Error de la base de datos",
    "Delete {count} word(s)?": "¿Eliminar {count} palabra(s)?",
    "Deleted": "Eliminado",
    "{count} word(s) deleted.": "{count} palabra(s) eliminada(s).",
    "Deleted with {n} error(s).": "Eliminado con {n} error(es).",
    "Favorites": "Favoritos",
    "{count} word(s) added to favorites.": "{count} palabra(s) añadida(s) a favoritos.",
    "{count} word(s) removed from favorites.": "{count} palabra(s) quitada(s) de favoritos.",
    "Status set to '{status}' for {count} word(s).": "Estado establecido a «{status}» para {count} palabra(s).",
    "Max Words": "Máximo de palabras",
    "Show only the first N words (0 = show all):": "Mostrar solo las primeras N palabras (0 = mostrar todas):",
    "View Definition": "Ver definición",
    "Copy Word": "Copiar palabra",
    "Copy Translation": "Copiar traducción",
    "Toggle Favorite": "Alternar favorito",
    "Change Status…": "Cambiar estado…",
    "Add / Remove Tags…": "Añadir / quitar etiquetas…",
    "Read Aloud": "Leer en voz alta",
    "Change Status": "Cambiar estado",
    "New status:": "Nuevo estado:",
    "Copied": "Copiado",
    "{count} row(s) copied to clipboard.": "{count} fila(s) copiada(s) al portapapeles.",
    "{count} item(s) copied to clipboard.": "{count} elemento(s) copiado(s) al portapapeles.",
    "Copy Word(s)": "Copiar palabra(s)",
    "Copy Translation(s)": "Copiar traducción(es)",
    "Copy Both": "Copiar ambos",
    "Search in Word": "Buscar en palabra",
    "Search in Translation": "Buscar en traducción",
    "Search in Tags": "Buscar en etiquetas",
    "Promoted": "Ascendido",
    "Google Cloud TTS unavailable": "Google Cloud TTS no está disponible",
    "Selection limit": "Límite de selección",
    "Only the first 200 selected words will be read.": "Solo se leerán las primeras 200 palabras seleccionadas.",
    "Only the first 50 words will be used.": "Solo se utilizarán las primeras 50 palabras.",
    "Select words to save as audio.": "Selecciona palabras para guardarlas como audio.",
    "Nothing to export.": "Nada que exportar.",
    "Export Error": "Error de exportación",
    "Settings saved.": "Ajustes guardados.",
    "Generated text saved.": "Texto generado guardado.",
    "Show": "Mostrar",
    "Add Word": "Añadir palabra",
    "Stop reading": "Detener lectura",
    "Read — Read selected words aloud": "Leer — Leer palabras seleccionadas en voz alta",
    "Translation": "Traducción",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "Apariencia",
    "Audio": "Audio",
    "Learning": "Aprendiendo",
    "Listening": "Escuchando",
    "Backups": "Copias de seguridad",
    "Sync your library?": "¿Sincronizar tu biblioteca?",
    "This will reconcile your device with the cloud:": "Esto reconciliará tu dispositivo con la nube:",
    "Sync now": "Sincronizar ahora",
    "Upload": "Subir",
    "Synced — ↑{up} ↓{down}": "Sincronizado — ↑{up} ↓{down}",
    "Upload restored library?": "¿Subir biblioteca restaurada?",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "Biblioteca restaurada. Se te pedirá subirla la próxima vez que te conectes a un servidor de sincronización.",
    "Merging this restored backup with your cloud:": "Combinando esta copia de seguridad restaurada con tu nube:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "Esta copia de seguridad tiene {items}. ¿Subirla y combinarla con tu nube ahora, o dejar tu nube sin cambios por el momento?",
    "General": "General",
    "Read-aloud": "Lectura en voz alta",
    "Translation & AI": "Traducción e IA",
    "Data": "Datos",
    "Behavior": "Comportamiento",
    "Progress": "Progreso",
    "DeepL request failed — using free Google Translate instead.": "La solicitud de DeepL falló; usando Google Translate gratuito en su lugar.",
    "DeepL key isn't set — using free Google Translate instead.": "La clave de DeepL no está configurada; usando Google Translate gratuito en su lugar.",
    "System": "Sistema",
    "Light": "Claro",
    "Dark": "Oscuro",
    "Appearance mode": "Modo de apariencia",
    "Widget scaling": "Escalado de elementos",
    "Table size": "Tamaño de tabla",
    "Interface language": "Idioma de la interfaz",
    "Restart the app to apply the language change.": "Reinicia la aplicación para aplicar el cambio de idioma.",
    "The interface language has changed. Restart now to apply it?": "El idioma de la interfaz ha cambiado. ¿Reiniciar ahora para aplicarlo?",
    "TTS provider": "Proveedor TTS",
    "Google Cloud credentials": "Credenciales de Google Cloud",
    "Voice type": "Tipo de voz",
    "Voice name (optional)": "Nombre de voz (opcional)",
    "Read Aloud playback": "Reproducción de lectura en voz alta",
    "Pause between words (s)": "Pausa entre palabras (s)",
    "Repeats per word": "Repeticiones por palabra",
    "Repeats per pair": "Repeticiones por par",
    "Promote status while listening": "Ascender estado al escuchar",
    "Listens to reach {status}": "Escuchas para alcanzar «{status}»",
    "Excel import": "Importación de Excel",
    "Placeholder values": "Valores de sustitución",
    "Skip placeholder rows": "Omitir filas de sustitución",
    "Skip empty rows": "Omitir filas vacías",
    "Normalize language pairs": "Normalizar pares de idiomas",
    "How to import": "Cómo importar",
    "Save import template…": "Guardar plantilla de importación…",
    "Active provider": "Proveedor activo",
    "API key": "Clave API",
    "API URL": "URL de la API",
    "Check usage": "Comprobar uso",
    "Enable cloud sync": "Activar sincronización en la nube",
    "Supabase URL (.env)": "URL de Supabase (.env)",
    "Supabase key (.env)": "Clave de Supabase (.env)",
    "Bin cleanup grace (days)": "Días de gracia para la papelera",
    "Test Connection": "Probar conexión",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "La sincronización en la nube usa tu propio proyecto de Supabase. Crea las tablas requeridas una vez, luego ingresa la URL y la clave anónima arriba.",
    "Copy schema SQL": "Copiar SQL de esquema",
    "Open SQL editor ↗": "Abrir editor SQL ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "SQL de esquema copiado al portapapeles. Abre el editor SQL de tu proyecto Supabase, pégalo y presiona Run para crear las tablas.",
    "Server": "Servidor",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "Conectado a tu propio servidor Supabase — modo personal, sin necesidad de cuenta.\n{host}",
    "Use your own Supabase server (personal)": "Usar tu propio servidor Supabase (personal)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Sincronización personal e individual a un proyecto de Supabase propio. Sin cuenta ni inicio de sesión: la app se conecta con la clave anónima del proyecto. Ejecuta el SQL de esquema en tu proyecto, pega su URL y clave anónima a continuación, luego prueba la conexión.\n\nNota: cualquiera con esta URL y clave puede leer los datos, así que mantén el proyecto privado y no compartas la clave.",
    "Disconnect — use the built-in server": "Desconectar — usar el servidor integrado",
    "Disconnect server": "Desconectar servidor",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "¿Dejar de sincronizar con tu propio servidor Supabase y usar de nuevo el integrado?\n\nTus palabras permanecerán en tu proyecto y en este dispositivo. Estarás en modo local hasta que inicies sesión en una cuenta.",
    "Disconnected — using the built-in server.": "Desconectado — usando el servidor integrado.",
    "{host} (personal)": "{host} (personal)",
    "Personal": "Personal",
    "your server": "tu servidor",
    "Account actions": "Acciones de cuenta",
    "Add account…": "Añadir cuenta…",
    "Sync this device's data to my account…": "Sincronizar datos de este dispositivo a mi cuenta…",

    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "Cuenta",
    "Accounts": "Cuentas",
    "No accounts yet. Add one to sync your words across devices.": "Aún no hay cuentas. Añade una para sincronizar tus palabras entre dispositivos.",
    "(active)": "(activa)",
    "Sign in": "Iniciar sesión",
    "(sign in again)": "(iniciar sesión de nuevo)",
    "Switch": "Cambiar",
    "Remove account": "Quitar cuenta",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "¿Quitar {email} de este dispositivo? Puedes volver a añadirla en cualquier momento: tus palabras permanecen en la nube y la copia local sigue en el disco. Tus datos en la nube no se eliminarán.",
    "Removed {email} from this device.": "Se quitó {email} de este dispositivo.",
    "Your data was exported.": "Tus datos han sido exportados.",
    "Export failed.": "Error al exportar.",
    "Delete account": "Eliminar cuenta",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "Esto eliminará permanentemente tu cuenta y TODAS tus palabras, textos y etiquetas sincronizadas de la nube. Tu copia local se archivará en la carpeta de copias de seguridad. Esto no se puede deshacer.\n\n¿Eliminar tu cuenta?",
    "Account deleted.": "Cuenta eliminada.",
    "Could not delete the account.": "No se pudo eliminar la cuenta.",

    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "Nombre",
    "Enter your name.": "Ingresa tu nombre.",
    "Email": "Correo electrónico",
    "Password": "Contraseña",
    "New password": "Nueva contraseña",
    "6-digit code": "Código de 6 dígitos",
    "or": "o",
    "Sign in with Google": "Iniciar sesión con Google",
    "Opening your browser to sign in with Google…": "Abriendo tu navegador para iniciar sesión con Google…",
    "Forgot password?": "¿Olvidaste tu contraseña?",
    "Resend code": "Reenviar código",
    "Confirm your email": "Confirma tu correo electrónico",
    "Verify code": "Verificar código",
    "Use a different email": "Usar otro correo electrónico",
    "Enter your email and password.": "Ingresa tu correo electrónico y contraseña.",
    "Enter the 6-digit code from the email.": "Ingresa el código de 6 dígitos enviado a tu correo.",
    "Enter the code and a new password.": "Ingresa el código y una nueva contraseña.",
    "Enter your email above first.": "Ingresa tu correo electrónico arriba primero.",
    "Enter the reset code we emailed you and a new password.": "Ingresa el código de restablecimiento enviado a tu correo y una nueva contraseña.",
    "Enter the 6-digit code we emailed you.": "Ingresa el código de 6 dígitos que te enviamos por correo.",
    "Reset password": "Restablecer contraseña",
    "Set new password": "Establecer nueva contraseña",
    "Back to sign in": "Volver a iniciar sesión",
    "Sign-in failed.": "Error al iniciar sesión.",
    "Couldn't send the code.": "No se pudo enviar el código.",
    "Done.": "Hecho.",
    "Failed.": "Falló.",
    "Create an account": "Crear una cuenta",
    "Create account": "Crear cuenta",
    "I already have an account": "Ya tengo una cuenta",
    "Signed in as {email}": "Sesión iniciada como {email}",

    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "Sincronizar datos de este dispositivo a tu cuenta",
    "your account": "tu cuenta",
    "This device has {words} and {texts} not yet in {account}.": "Este dispositivo tiene {words} y {texts} que aún no están en {account}.",
    "This device has {words} not yet in {account}.": "Este dispositivo tiene {words} que aún no están en {account}.",
    "This device has {texts} not yet in {account}.": "Este dispositivo tiene {texts} que aún no están en {account}.",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "Selecciona los elementos a añadir. Se copiarán a tu cuenta y se subirán a la nube para que aparezcan en tus otros dispositivos. La copia en este dispositivo se mantendrá.",
    "Don't ask again for this account": "No volver a preguntar para esta cuenta",
    "{n} word": "{n} palabra",
    "{n} words": "{n} palabras",
    "{n} text": "{n} texto",
    "{n} texts": "{n} textos",
    "Add {n} item": "Añadir {n} elemento",
    "Add {n} items": "Añadir {n} elementos",
    "words (genitive)": "palabras",
    "texts (genitive)": "textos",
    "tags (genitive)": "etiquetas",
    "changes (genitive)": "cambios",
    "deletions (genitive)": "eliminaciones",
    "{n} words (genitive)": "{n} palabras",
    "{n} texts (genitive)": "{n} textos",
    "Add {n} items (genitive)": "Añadir {n} elementos",
    "Added {n} item to your account.": "Se añadió {n} elemento a tu cuenta.",
    "Added {n} items to your account.": "Se añadieron {n} elementos a tu cuenta.",
    "Added {n} items to your account. (genitive)": "Se añadieron {n} elementos a tu cuenta.",
    "{n} couldn't be added.": "No se pudieron añadir {n} elementos.",

    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "Tu sesión ha expirado: inicia sesión de nuevo (Ajustes → Sincronización)",
    "Sign in to sync (Settings → Sync)": "Inicia sesión para sincronizar (Ajustes → Sincronización)",
    "Sign in again to sync": "Inicia sesión de nuevo para sincronizar",
    "Sign in again to use this account.": "Inicia sesión de nuevo para usar esta cuenta.",
    "Sync incomplete: {reason}": "Sincronización incompleta: {reason}",
    "Connect to the internet to add local items to your account.": "Conéctate a internet para añadir elementos locales a tu cuenta.",
    "Everything on this device is already in your account.": "Todo en este dispositivo ya está en tu cuenta.",
    "Upload local words?": "¿Subir palabras locales?",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "¿Subir tus palabras locales actuales a esta cuenta? Se combinarán con los datos en la nube de esta cuenta y se sincronizarán.\n\nElige No para mantener los datos existentes de esta cuenta y apartar tus palabras locales (archivadas en la carpeta de copias de seguridad).",

    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "Error al iniciar sesión. Comprueba tu correo y contraseña.",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "Puedes mantener hasta {max} cuentas en este dispositivo. Quita una para añadir otra.",
    "Wrong email or password.": "Correo electrónico o contraseña incorrectos.",
    "That doesn't look like a valid email address.": "No parece una dirección de correo válida.",
    "Confirm password": "Confirmar contraseña",
    "Passwords don't match.": "Las contraseñas no coinciden.",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "Tu correo aún no está confirmado. Ingresa el código de 6 dígitos que te enviamos.",
    "That email is already registered. Try signing in instead.": "Ese correo ya está registrado. Intenta iniciar sesión en su lugar.",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "Te enviamos un código de 6 dígitos al correo. Ingrésalo para finalizar el registro.",
    "That code didn't work. Check it and try again.": "Ese código no funcionó. Compruébalo e inténtalo de nuevo.",
    "If that account exists, a 6-digit reset code is on its way.": "Si esa cuenta existe, un código de restablecimiento de 6 dígitos está en camino.",
    "Confirmation email re-sent.": "Correo de confirmación reenviado.",
    "Too many attempts. Please wait a minute and try again.": "Demasiados intentos. Por favor, espera un minuto e inténtalo de nuevo.",
    "Your password is too short — use at least 6 characters.": "Tu contraseña es demasiado corta: usa al menos 6 caracteres.",
    "Sign-ups are disabled on this server.": "Los registros están desactivados en este servidor.",
    "Can't reach the server. Check your internet connection.": "No se puede alcanzar el servidor. Comprueba tu conexión a internet.",
    "Something went wrong.": "Algo salió mal.",
    "Your saved sign-in for this account expired. Sign in again.": "Tu inicio de sesión guardado para esta cuenta ha expirado. Inicia sesión de nuevo.",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "La sincronización en la nube aún no está configurada. Añade la URL y la clave de Supabase en Ajustes → Sincronización primero.",
    "Could not start Google sign-in.": "No se pudo iniciar el inicio de sesión con Google.",
    "Google sign-in was cancelled or timed out.": "El inicio de sesión con Google fue cancelado o expiró.",
    "Google sign-in failed.": "El inicio de sesión con Google falló.",
    "Google sign-in failed: {error}": "El inicio de sesión con Google falló: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "No se pudo iniciar el asistente de inicio de sesión local en el puerto {port} ({error}). Cierra la aplicación que lo esté usando e inténtalo de nuevo.",
    "Export my data…": "Exportar mis datos…",
    "Delete account…": "Eliminar cuenta…",
    "Cloud sync is on — your own server ({host})": "Sincronización activada — tu propio servidor ({host})",
    "Cloud sync is on — signed in as {who}": "Sincronización activada — sesión iniciada como {who}",
    "Cloud sync is off — your words are saved on this device only": "Sincronización desactivada — tus palabras se guardan solo en este dispositivo",
    "(checking…)": "(comprobando…)",
    "(can't connect)": "(sin conexión)",
    "Turn off cloud sync": "Desactivar sincronización en la nube",
    "Cloud sync turned off — this device only.": "Sincronización desactivada — solo en este dispositivo.",
    "Use this server": "Usar este servidor",
    "Connecting…": "Conectando…",
    "Testing…": "Comprobando…",
    "Applying theme…": "Aplicando tema…",
    "Now syncing with your own server.": "Sincronizando ahora con tu propio servidor.",
    "Could not connect to this server:\n{error}": "No se pudo conectar a este servidor:\n{error}",
    "Could not connect to this server.": "No se pudo conectar a este servidor.",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nComprueba la URL y la clave anónima, y asegúrate de haber ejecutado el SQL del esquema allí. ¿Usar estos datos de todos modos?",
    "Enter your server's URL and anon key first, then test.": "Ingresa primero la URL del servidor y la clave anónima, luego prueba.",
    "Enter your server's URL and anon key first.": "Ingresa primero la URL del servidor y la clave anónima.",
    "Supabase URL": "URL de Supabase",
    "Supabase key (anon)": "Clave de Supabase (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "Sincronización personal e individual a un proyecto de Supabase propio. Sin cuenta ni inicio de sesión: la app se conecta con la clave anónima del proyecto. Ejecuta el SQL de esquema en tu proyecto, pega su URL y clave anónima a continuación, pruébalo y presiona “Usar este servidor”.\n\nNota: cualquiera con esta URL y clave puede leer los datos, así que mantén el proyecto privado y no compartas la clave.",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "¿Dejar de sincronizar con tu propio servidor Supabase y usar de nuevo el integrado?\n\nTus palabras permanecerán en tu proyecto y en este dispositivo. Se recordarán los detalles del servidor para que puedas volver en cualquier momento. Estarás en modo local hasta que inicies sesión en una cuenta.",
    "Start automatically on login (minimized to tray)": "Iniciar automáticamente al iniciar sesión (minimizado en la bandeja)",
    "Starting on login is turned off for Lingueez in Windows Settings, so it can't be switched on here.": "El inicio al iniciar sesión está desactivado para Lingueez en la configuración de Windows, así que no se puede activar aquí.",
    "Open Windows startup settings": "Abrir la configuración de inicio de Windows",
    "Windows did not apply this change. You can turn Lingueez on or off yourself under Settings > Apps > Startup.": "Windows no aplicó este cambio. Puedes activar o desactivar Lingueez tú mismo en Configuración > Aplicaciones > Inicio.",
    "Add Word hotkey (global)": "Atajo de teclado «Añadir palabra» (global)",
    "Data format": "Formato de datos",
    "Columns to export": "Columnas a exportar",
    "Sheet name": "Nombre de la hoja",
    "Start row": "Fila inicial",
    "Start column": "Columna inicial",
    "Shade alternate rows": "Sombrear filas alternas",
    "Auto column width": "Ancho automático de columnas",
    "Freeze header row": "Inmovilizar fila de encabezado",
    "Delimiter": "Delimitador",
    "Delimiter (\\t = tab)": "Delimitador (\\t = tabulación)",
    "Include header lines": "Incluir líneas de encabezado",
    "Header lines": "Líneas de encabezado",
    "Page size": "Tamaño de página",
    "Font size": "Tamaño de fuente",
    "Line spacing (pt)": "Interlineado (pt)",
    "Text alignment": "Alineación del texto",
    "Margins L/R/T/B (pt)": "Márgenes I/D/A/A (pt)",
    "Automatic widths (fit page)": "Anchos automáticos (ajustar a la página)",
    "Columns / width": "Columnas / ancho",
    "Header background": "Fondo del encabezado",
    "Header text": "Texto del encabezado",
    "Row background": "Fondo de fila",
    "Grid lines": "Líneas de cuadrícula",
    "Background image": "Imagen de fondo",
    "Concurrent workers": "Procesos concurrentes",
    "Requests per second": "Solicitudes por segundo",
    "Add font…": "Añadir fuente…",
    "Page && text": "Página y texto",
    "Columns": "Columnas",
    "Max tokens": "Máximo de tokens",
    "Temperature": "Temperatura",
    "Prompt template": "Plantilla de prompt",
    "Definitions": "Definiciones",
    "Generated Texts (from words)": "Textos generados (a partir de palabras)",
    "Generated Texts (by topic)": "Textos generados (por tema)",
    "Text Adaptation (to level)": "Adaptación de texto (al nivel)",
    "Thinking budget (0 = off, -1 = auto)": "Presupuesto de pensamiento (0 = deshabilitado, -1 = auto)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "Detectar idioma",
    "Type a word or phrase…": "Escribe una palabra o frase…",
    "Translation…": "Traducción…",
    "Pronounce": "Pronunciar",
    "Swap word and translation": "Intercambiar palabra y traducción",
    "Translate with DeepL (Enter)": "Traducir con DeepL (Intro)",
    "Save Word": "Guardar palabra",
    "Enter a word to translate.": "Ingresa una palabra para traducir.",
    "Fill with AI (lemma + best translation)": "Rellenar con IA (lema + mejor traducción)",
    "Enter a word to fill with AI.": "Ingresa una palabra para rellenar con IA.",
    "Source equals target — translated to {lang} instead.": "El idioma de origen es igual al de destino; traducido a {lang} en su lugar.",
    "Both word and translation are required.": "Se requieren tanto la palabra como la traducción.",
    "Please select the source language before saving.": "Por favor, selecciona el idioma de origen antes de guardar.",
    "'{word}' already exists in your dictionary.": "«{word}» ya existe en tu diccionario.",
    "'{word}' is already in your dictionary.": "«{word}» ya está en tu diccionario.",
    "Already in your dictionary": "Ya está en tu diccionario",
    "Show existing": "Mostrar existente",
    "The text was truncated to the first 100 words.": "El texto se truncó a las primeras 100 palabras.",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "Generar con IA",
    "Regenerate with AI": "Regenerar con IA",
    "Definition 2": "Definición 2",
    "No definition yet": "Aún no hay definición",
    "Generate one with AI, or write your own with Edit.": "Genera una con IA o escribe la tuya propia en Editar.",
    "There is no word to define.": "No hay palabra para definir.",
    "Bold": "Negrita",
    "Italic": "Cursiva",
    "Heading": "Encabezado",
    "List": "Lista",
    "API key missing": "Falta la clave API",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "Configura primero tu clave API de {ai} en Ajustes → Traducción e IA → IA.",
    "Generating definition…": "Generando definición…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "Etiquetas — {count} palabra(s)",
    "New tag name…": "Nuevo nombre de etiqueta…",
    "Add Tag": "Añadir etiqueta",
    "Apply Selected to All": "Aplicar seleccionadas a todo",
    "Remove Selected": "Quitar seleccionadas",
    "(partial)": "(parcial)",
    "use(s)": "uso(s)",
    "Tags marked ✓ apply to all selected words.": (
        "Las etiquetas marcadas con ✓ se aplican a todas las palabras seleccionadas."
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (parcial) significa que solo algunas de ellas tienen la etiqueta."
    ),
    "Select tag(s) in the list first.": "Selecciona primero la(s) etiqueta(s) en la lista.",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "Papelera — Elementos eliminados",
    "Delete Permanently": "Eliminar permanentemente",
    "Cleanup Old Items…": "Limpiar elementos antiguos…",
    "{n} selected": "{n} seleccionado(s)",
    "The bin is empty. Deleted words will appear here.":
        "La papelera está vacía. Las palabras eliminadas aparecerán aquí.",
    "The bin is empty. Deleted texts will appear here.":
        "La papelera está vacía. Los textos eliminados aparecerán aquí.",
    "deleted {when}": "eliminado {when}",
    "(empty)": "(vacío)",
    "Untitled": "Sin título",
    "Auto-deletes soon": "Se eliminará automáticamente pronto",
    "Auto-deletes in {n} day": "Se elimina automáticamente en {n} día",
    "Auto-deletes in {n} days": "Se elimina automáticamente en {n} días",
    "Auto-deletes in {n} days (genitive)": "Se elimina automáticamente en {n} días",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "¿Eliminar permanentemente {count} elemento(s)? Esto no se puede deshacer.",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "Restaurar una versión anterior",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "Se realiza una copia de seguridad automática de tu base de datos tras cada cambio. "
        "Elige una versión anterior a continuación para restaurarla."
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "Aún no hay versiones guardadas. "
        "Se crea una copia de seguridad automáticamente después de cada cambio."
    ),
    "Restore this version": "Restaurar esta versión",
    "Today": "Hoy",
    "Yesterday": "Ayer",
    "Most recent": "Más reciente",
    "Before your last restore": "Antes de tu última restauración",
    "today": "hoy",
    "yesterday": "ayer",
    "today {time}": "hoy {time}",
    "yesterday {time}": "ayer {time}",
    "the version from {date}": "la versión del {date}",
    "the version from just before your last restore": "la versión de justo antes de tu última restauración",
    "Restore Version": "Restaurar versión",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "¿Restaurar {phrase}?\n\nTus datos actuales se guardarán primero para que puedas deshacer esto."
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "Tu base de datos ha sido restaurada a {phrase}.\n\n"
        "¿Cambiaste de opinión? Restaura «{before}» para deshacer."
    ),
    "Restore Error": "Error al restaurar",
    "Sorry, that version could not be restored:\n{error}": "Lo sentimos, esa versión no pudo ser restaurada:\n{error}",
    "Remove Version": "Eliminar versión",
    "Remove {phrase}?": "¿Eliminar {phrase}?",
    "Remove Error": "Error al eliminar",
    "Sorry, that version could not be removed:\n{error}": "Lo sentimos, esa versión no pudo ser eliminada:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "Generar texto",
    "Title…": "Título…",
    "Generated text appears here…": "El texto generado aparecerá aquí…",
    "Save to Texts": "Guardar en Textos",
    "Save failed": "Error al guardar",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "Guardar como audio",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "Generar un archivo MP3 a partir de {count} par(es) de palabra/traducción."
    ),
    "Generating audio…": "Generando audio…",
    "Compiling final audio file…": "Compilando archivo de audio final…",
    "Processed: {word}": "Procesado: {word}",
    "Choose File && Start": "Elegir archivo e iniciar",
    "Cancelled.": "Cancelado.",
    "Audio saved": "Audio guardado",
    "Audio file saved to:\n{path}": "Archivo de audio guardado en:\n{path}",
    "Audio Error": "Error de audio",
    "Failed to save audio:\n{error}": "Error al guardar el audio:\n{error}",
    "Cancelling…": "Cancelando…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Importar desde Excel",
    "Row": "Fila",
    "Word 1": "Palabra 1",
    "Language 1": "Idioma 1",
    "Word 2": "Palabra 2",
    "Language 2": "Idioma 2",
    "Action": "Acción",
    "Details": "Detalles",
    "Add": "Añadir",
    "Update": "Actualizar",
    "Skip": "Omitir",
    "All": "Todos",
    "To add": "Para añadir",
    "To update": "Para actualizar",
    "Skipped": "Omitidos",
    "Unrecognized": "No reconocidos",
    "Only recognized languages": "Solo idiomas reconocidos",
    "Exclude rows whose language wasn't recognized.":
        "Excluir filas cuyo idioma no fue reconocido.",
    "Unrecognized language — will be imported exactly as written.":
        "Idioma no reconocido: se importará exactamente como está escrito.",
    "Select all": "Seleccionar todo",
    "Activity log": "Registro de actividad",
    "Export log…": "Exportar registro…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "Exportar…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "Añadir texto",
    "Write": "Escribir",
    "AI Generate": "Generar con IA",
    "Wikipedia": "Wikipedia",
    "From URL": "Desde URL",
    "Language:": "Idioma:",
    "Level:": "Nivel:",
    "Topic:": "Tema:",
    "Topic…": "Tema…",
    "Adapt to my level": "Adaptar a mi nivel",
    "Load entries": "Cargar entradas",
    "Add feed…": "Añadir fuente…",
    "Ideas:": "Ideas:",
    "Short (~100 words)": "Corto (~100 palabras)",
    "Medium (~250 words)": "Medio (~250 palabras)",
    "Long (~500 words)": "Largo (~500 palabras)",
    "Travel": "Viajes",
    "Food": "Comida",
    "Daily routine": "Rutina diaria",
    "A short story": "Una historia corta",
    "News": "Noticias",
    "Dialogue at a café": "Diálogo en un café",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "Escribe o pega tu texto aquí, o consigue uno mediante las pestañas superiores…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "Más recientes primero",
    "Oldest first": "Más antiguos primero",
    "Title A–Z": "Título A–Z",
    "All languages": "Todos los idiomas",
    "All levels": "Todos los niveles",
    "All topics": "Todos los temas",
    "No matching texts": "No hay textos coincidentes",
    "Try a different search or language filter.": "Prueba una búsqueda o filtro de idioma diferente.",
    "New text (write or paste)": "Nuevo texto (escribir o pegar)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Obtener texto de Internet (IA / Wikipedia / URL / RSS)"
    ),
    "Import .txt file(s)": "Importar archivo(s) .txt",
    "Read aloud": "Leer en voz alta",
    "Translate text": "Traducir texto",
    "Hide translation": "Ocultar traducción",
    "Focus mode": "Modo de enfoque",
    "Exit focus mode": "Salir del modo de enfoque",
    "Paper mode: off": "Modo papel: desactivado",
    "Paper: white (click for sepia)": "Papel: blanco (clic para sepia)",
    "Paper: sepia (click to turn off)": "Papel: sepia (clic para desactivar)",
    "Save Changes": "Guardar cambios",
    "Previous text": "Texto anterior",
    "Next text": "Texto siguiente",
    "From words: {words}": "A partir de palabras: {words}",
    "Created {date}": "Creado el {date}",
    "Unsaved changes": "Cambios no guardados",
    "Save changes to '{title}'?": "¿Guardar cambios en «{title}»?",
    "Changes saved.": "Cambios guardados.",
    "'{title}' moved to bin.": "«{title}» movido a la papelera.",
    "Reader": "Lector",
    'Pronounce "{word}"': 'Pronunciar «{word}»',
    'Add "{word}" to vocabulary': 'Añadir «{word}» al vocabulario',
    "Read from here": "Leer desde aquí",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "Origen",
    "Added manually": "Añadido manualmente",
    "From reader": "Desde el lector",
    "Created at": "Creado el",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "Añadir con IA (lema + mejor traducción)",
    "Add to vocabulary as is": "Añadir al vocabulario tal cual",
    "Thinking…": "Pensando…",
    "'{pair}' is already in your dictionary.": "«{pair}» ya está en tu diccionario.",
    "{label} — {translation} · added": "{label} — {translation} · añadido",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "Sincronización en la nube",
    "Last sync": "Última sincronización",
    "Pending": "Pendiente",
    "never": "nunca",
    "just now": "ahora mismo",
    "{n} min ago": "hace {n} min",
    "Connected": "Conectado",
    "Not connected": "No conectado",
    "change": "cambio",
    "changes": "cambios",
    "deletion": "eliminación",
    "deletions": "eliminaciones",
    "everything synced": "todo sincronizado",
    "Initial sync has not completed yet.": "La sincronización inicial aún no ha finalizado.",
    "Sync Now": "Sincronizar ahora",
    "Syncing…": "Sincronizando…",
    "{words} and {texts}": "{words} y {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "Has guardado {items} aquí. Inicia sesión para mantenerlos a salvo y estudiar en todos tus dispositivos.",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "Solo local: inicia sesión para sincronizar tus palabras entre dispositivos",
    "Sign in to sync across devices": "Iniciar sesión para sincronizar",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "Bienvenido",
    "Welcome to {app}": "Bienvenido a {app}",
    "Sync across your devices": "Sincroniza en todos tus dispositivos",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "Inicia sesión para proteger tu vocabulario y estudiarlo en cualquier dispositivo.",
    "Automatic cloud backup": "Copia de seguridad automática en la nube",
    "Your words follow you to every computer.":
        "Tus palabras te acompañan a cualquier ordenador.",
    "Never lose your progress.": "Nunca pierdas tu progreso.",
    "Study anywhere": "Estudia en cualquier lugar",
    "Pick up right where you left off.":
        "Retómalo justo donde lo dejaste.",
    "Your data is yours — sign in only to sync it.":
        "Tus datos son tuyos: inicia sesión únicamente para sincronizarlos.",
    "Sign in / Create account": "Iniciar sesión / Crear cuenta",
    "Continue on this device": "Continuar en este dispositivo",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "Ajustes de reproducción",
    "Previous word": "Palabra anterior",
    "Next word": "Palabra siguiente",
    "Stop playback": "Detener reproducción",
    "Pause between words": "Pausa entre palabras",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "Nada que leer.",
    "Previous sentence": "Frase anterior",
    "Next sentence": "Frase siguiente",
    "Reading speed": "Velocidad de lectura",
    "Sentence {n} / {total}": "Frase {n} / {total}",
    "buffering…": "almacenando en búfer…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "Resumen",
    "Learning status": "Estado del aprendizaje",
    "Activity": "Actividad",
    "Review activity": "Actividad de repasos",
    "Breakdown": "Desglose",
    "Total words": "Total de palabras",
    "Mastered": "Dominadas",
    "In progress": "En progreso",
    "Languages": "Idiomas",
    "Current streak": "Racha actual",
    "Added this week": "Añadidas esta semana",
    "Definitions written": "Definiciones escritas",
    "Status distribution": "Distribución por estado",
    "Words added over time": "Palabras añadidas con el tiempo",
    "Activity calendar": "Calendario de actividad",
    "Reviews over time": "Repasos a lo largo del tiempo",
    "Review calendar": "Calendario de repasos",
    "Most reviewed words": "Palabras más repasadas",
    "Top language pairs": "Pares de idiomas principales",
    "Top tags": "Etiquetas principales",
    "Reviewed this week": "Repasado esta semana",
    "Total reviews": "Total de repasos",
    "Review streak": "Racha de repasos",
    "{pct}% of all words": "{pct}% de todas las palabras",
    "actively learning": "aprendiendo activamente",
    "{n} pairs": "{n} par(es)",
    "best {n}d": "récord {n} días",
    "{n} today": "{n} hoy",
    "listens logged": "escuchas registradas",
    "keep it going": "¡continúa así!",
    "Day": "Día",
    "Week": "Semana",
    "Month": "Mes",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "Importar archivos de texto",
    "Text files (*.txt);;All files (*)": "Archivos de texto (*.txt);;Todos los archivos (*)",
    "Language of the imported text(s):": "Idioma del texto(s) importado(s):",
    "Imported {count} text(s).": "Se importó/aron {count} texto(s).",
    "Some files could not be imported:": "No se pudieron importar algunos archivos:",
    "Import failed:\n{error}": "Error al importar:\n{error}",
    "Failed to save text:\n{error}": "Error al guardar el texto:\n{error}",
    "Failed to delete text:\n{error}": "Error al eliminar el texto:\n{error}",
    "Delete Text": "Eliminar texto",
    "Delete '{title}'?": "¿Eliminar «{title}»?",
    "Unsupported language: {language}": "Idioma no compatible: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "Idioma no compatible: {lang}. Elige uno de la lista.",
    "(empty)": "(vacío)",
    "unsupported language": "idioma no compatible",
    "unreadable text": "texto no legible",
    "Skipped {n} {noun} ({reasons}).": "Se omitieron {n} {noun} ({reasons}).",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "Algunos textos no se pudieron leer en voz alta: idioma no compatible "
        "o caracteres no legibles.",
    "Edit text": "Editar texto",
    "Done editing": "Terminar edición",
    "Delete text": "Eliminar texto",
    "Save Changes": "Guardar cambios",
    "Paper mode": "Modo papel",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "Haz clic en «+» para escribir o pegar un texto, en el globo terráqueo para obtener uno\n"
        "de Internet, o selecciona palabras en la vista Palabras y\n"
        "usa la acción «Texto» para generar un texto de estudio."
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "Busca en Wikipedia en el idioma seleccionado. Haz clic en un resultado para cargar el artículo; usa «Adaptar a mi nivel» para simplificarlo."
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "Fuentes de noticias para el idioma seleccionado. Carga una fuente y luego haz doble clic en una entrada para obtener el texto completo. Añade tus propias fuentes con «Añadir fuente…»."
    ),
    "Length:": "Longitud:",
    "Search Wikipedia (in the selected language)…": "Buscar en Wikipedia (en el idioma seleccionado)…",
    "Double-click an entry to load its full text.": "Haz doble clic en una entrada para cargar su texto completo.",
    "Working…": "Procesando…",
    "Show the {count} result(s) again": "Mostrar los {count} resultado(s) de nuevo",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "La clave API de {ai} no está configurada. Configúrala en Ajustes → Traducción e IA → IA."
    ),
    "Generating with {ai}…": "Generando con {ai}…",
    'Fetching "{title}"…': 'Obteniendo «{title}»…',
    "(yours)": "(tuya)",
    "Fetching the full text…": "Obteniendo el texto completo…",
    "Add feed": "Añadir fuente",
    "Feed name:": "Nombre de la fuente:",
    "Feed URL:": "URL de la fuente:",
    "Failed to save the text.": "Error al guardar el texto.",
    "Failed to save the text: {error}": "Error al guardar el texto: {error}",
    "'{title}' saved.": "«{title}» guardado.",
    "(untitled)": "(sin título)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "Reescribir el texto a continuación para el nivel MCER seleccionado con {ai}"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "Exportar registro",
    "Activity Log": "Registro de actividad",
    "Warnings & errors": "Advertencias y errores",
    "Errors only": "Solo errores",
    "Find…": "Buscar…",
    "Open log folder": "Abrir carpeta de registros",
    "Export diagnostics": "Exportar diagnóstico",
    "Clear the log file? This cannot be undone.":
        "¿Vaciar el archivo de registro? Esto no se puede deshacer.",
    "Could not create the diagnostics file.":
        "No se pudo crear el archivo de diagnóstico.",
    "Diagnostics saved to:\n{path}": "Diagnóstico guardado en:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**Describe el problema**\n\n\n**Pasos para reproducirlo**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\nPor favor, adjunta el archivo de diagnóstico:\n{path}\n",
    "Bug report: ": "Informe de error: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "Minimizar",
    "Maximize": "Maximizar",
    "Restore": "Restaurar",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "Mostrar controles",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "Sin color",
    "None": "Ninguno",
    "Choose Color": "Elegir color",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "Sincronización en la nube: inactiva",
    "Failed to open table:\n{error}": "Error al abrir la tabla:\n{error}",
    "Failed to save template:\n{error}": "Error al guardar la plantilla:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "Mostrar / ocultar",
    "Excel options": "Opciones de Excel",
    "CSV options": "Opciones de CSV",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "Las líneas de encabezado se escriben en la parte superior del archivo; herramientas de importación "
        "como Anki las leen (ej. #separator:tab, #html:true). "
        "Los nombres de las columnas en sí no se escriben."
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "Copia un archivo .ttf en la carpeta de fuentes de la app y úsalo"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "Se usa únicamente al exportar palabras a un archivo MP3. "
        "La voz se configura en la pestaña Audio."
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "La voz utilizada en cualquier lugar donde se pronuncien palabras: Lectura en voz alta e "
        "importación a MP3. gTTS es gratuito y no requiere configuración. Google Cloud TTS "
        "requiere una clave JSON de cuenta de servicio (Cloud Console → IAM & Admin → "
        "Cuentas de servicio → Claves) y facturación activada en el proyecto "
        "(el uso dentro de la cuota mensual gratuita no se cobra)."
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "Escuchar completamente una palabra en Lectura en voz alta la promueve en la "
        "escala de familiaridad: Nueva → Repasando → Aprendiendo → Dominada. Cada "
        "número es el total de escuchas completas necesarias para alcanzar ese nivel. "
        "Las palabras que establezcas tú mismo como Dominada u Omitida nunca se cambian, y una "
        "palabra nunca es degradada de estado."
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "Guardar un .xlsx listo con los encabezados correctos y filas de ejemplo"
    ),
    "Google Translate (free)": "Google Translate (gratuito)",
    "Google Translate is free and needs no API key.": (
        "Google Translate es gratuito y no requiere clave API."
    ),
    "Usage": "Uso",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "Haz clic en el campo y presiona la combinación de teclas deseada: abrirá "
        "«Añadir palabra» con el contenido del portapapeles desde cualquier lugar. "
        "Déjalo vacío para desactivar."
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "En Wayland, este atajo se registra en tu entorno de escritorio "
        "y aparece en la configuración de teclado del sistema."
    ),
    "Add Word hotkey": "Atajo de teclado «Añadir palabra»",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "El atajo global «Añadir palabra» no está disponible en este "
        "entorno. Consulta Ajustes ▸ Sistema para más opciones."
    ),
    "The global Add-Word hotkey isn't available in the "
    "{sandbox} sandbox on Wayland.": (
        "El atajo global «Añadir palabra» no está disponible en el "
        "aislamiento (sandbox) de {sandbox} en Wayland."
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "El atajo global «Añadir palabra» aún no es compatible "
        "en este escritorio Wayland."
    ),
    "To enable it, use any one of these:": "Para activarlo, usa cualquiera de estas opciones:",
    "Log in to an X11 session instead of Wayland":
        "Inicia sesión en una sesión X11 en lugar de Wayland",
    "Use a GNOME session — the global hotkey works there":
        "Usa una sesión de GNOME: el atajo global funciona allí",
    "Install the AppImage version — it runs outside the sandbox":
        "Instala la versión AppImage: funciona fuera del aislamiento (sandbox)",
    "Download the AppImage": "Descargar AppImage",
    "Add font…": "Añadir fuente…",
    "TrueType fonts (*.ttf)": "Fuentes TrueType (*.ttf)",
    "Could not copy the font file:\n{error}": "No se pudo copiar el archivo de fuente:\n{error}",
    "Save import template…": "Guardar plantilla de importación…",
    "Excel files (*.xlsx)": "Archivos de Excel (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "Plantilla guardada en:\n{path}\n\n"
        "Rellénala con tus palabras (reemplaza las filas de ejemplo) "
        "e impórtala a través del menú de la app → Importar Excel a la base de datos."
    ),
    "Could not save the template:\n{error}": "No se pudo guardar la plantilla:\n{error}",
    "Background image": "Imagen de fondo",
    "Images (*.png *.jpg *.jpeg)": "Imágenes (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "Archivos JSON (*.json)",
    "Connection successful! ✅": "¡Conexión exitosa! ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "No se pudo conectar. Comprueba la URL, la clave y tu conexión a internet."
    ),
    "Connection test failed:\n{error}": "La prueba de conexión falló:\n{error}",
    "{count} / {limit} characters this period": "{count} / {limit} caracteres en este período",
    "{count} characters used": "{count} caracteres utilizados",
    "Autostart": "Inicio automático",
    "Could not update autostart entry:\n{error}": "No se pudo actualizar la entrada de inicio automático:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS está seleccionado pero {problem}\n\n"
        "El audio recurrirá a gTTS hasta que esto se solucione."
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "palabra",
    "words": "palabras",
    "words (genitive)": "palabras",
    "text": "texto",
    "texts": "textos",
    "texts (genitive)": "textos",
    "tag": "etiqueta",
    "tags": "etiquetas",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "Traducir",
    "AI": "IA",
    "Save As": "Guardar como",
    "Save Audio As": "Guardar audio como",
    "Save PDF As": "Guardar PDF como",
    "Added": "Añadido",
    "Updated": "Actualizado",
    "Failed": "Falló",
    "Checking…": "Comprobando…",
    "Cleanup": "Limpieza",
    "Permanent Delete": "Eliminación permanente",
    "No word": "Sin palabra",
    "Category": "Categoría",
    "Bin": "Papelera",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "Todas las etiquetas",
    "Filter by tag — {tag}": "Filtrar por etiqueta — {tag}",
    "(showing first {n})": "(mostrando las primeras {n})",
    "Texts: {total}": "Textos: {total}",
    "Deleted with {n} error(s).": "Eliminado con {n} error(es).",
    "Failed to update: {error}": "Error al actualizar: {error}",
    "Failed to export:\n{error}": "Error al exportar:\n{error}",
    "Failed to export PDF:\n{error}": "Error al exportar PDF:\n{error}",
    "Failed to export TXT:\n{error}": "Error al exportar TXT:\n{error}",
    "PDF saved to {path}": "PDF guardado en: {path}",
    "TXT file saved to {path}": "Archivo TXT guardado en: {path}",
    "Template saved to {path}": "Plantilla guardada en: {path}",
    "{format} file saved to {path}": "Archivo {format} guardado en: {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "Usando gTTS en su lugar — {problem}\nSoluciónalo en Ajustes → Lectura en voz alta → Audio."
    ),
    "Failed to load the database:": "Error al cargar la base de datos:",
    "{selected} of {total} selected": "{selected} de {total} seleccionado(s)",
    "Collapse sidebar": "Contraer barra lateral",
    "Expand sidebar": "Expandir barra lateral",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "Guardado {when} · {summary}",
    "the version from {date}": "la versión del {date}",
    "Sorry, that version could not be restored:\n{error}": (
        "Lo sentimos, esa versión no pudo ser restaurada:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "Lo sentimos, esa versión no pudo ser eliminada:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "¿Restaurar {count} elemento(s)?",
    "Restored {count} item(s).": "Se restauró/aron {count} elemento(s).",
    "Select item(s) to restore.": "Selecciona elemento(s) para restaurar.",
    "Permanently deleted {count} item(s).": "Se eliminó/aron permanentemente {count} elemento(s).",
    "Select item(s) to delete permanently.": "Selecciona elemento(s) para eliminar permanentemente.",
    "No items older than {n} days found.": "No se encontraron elementos más antiguos de {n} días.",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "¿Eliminar permanentemente elementos eliminados hace más de {days} días?\n\n"
        "¡Esto no se puede deshacer!"
    ),
    "Permanently deleted {count} old item(s).": "Se eliminaron permanentemente {count} elementos antiguos.",
    "Failed to load deleted items:\n{error}": "Error al cargar los elementos eliminados:\n{error}",
    "Failed to count old items:\n{error}": "Error al contar elementos antiguos:\n{error}",
    "Failed to cleanup:\n{error}": "Error en la limpieza:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Importar Excel",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "Columnas esperadas: Language1, Language2, Word1, Word2 (nombradas en una fila de encabezado "
        "o sin encabezados con las primeras cuatro columnas en ese orden). "
        "Hay una plantilla lista disponible en el menú de la app → Guardar plantilla de importación."
    ),
    "All ({n})": "Todos ({n})",
    "To add ({n})": "Para añadir ({n})",
    "To update ({n})": "Para actualizar ({n})",
    "Skipped ({n})": "Omitidos ({n})",
    "Unrecognized ({n})": "No reconocidos ({n})",
    " · {n} with unrecognized language": " · {n} con idioma no reconocido",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "{total} filas: {add} nuevas · {update} actualizaciones · {skip} omitidas"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "Revisa los cambios propuestos y luego importa las filas seleccionadas."
    ),
    "Nothing to import — no new or changed entries found.": (
        "Nada que importar: no se encontraron entradas nuevas o modificadas."
    ),
    "Analyzing file…": "Analizando archivo…",
    "Could not read the Excel file — see the activity log.": (
        "No se pudo leer el archivo Excel: consulta el registro de actividad."
    ),
    "Analysis failed — see the activity log.": "El análisis falló: consulta el registro de actividad.",
    "Import failed": "Error de importación",
    "Import failed — see the activity log.": "La importación falló: consulta el registro de actividad.",
    "Importing…": "Importando…",
    "Importing {count} item(s)…": "Importando {count} elemento(s)…",
    "Import {count} Item(s)": "Importar {count} elemento(s)",
    "Import finished:": "Importación finalizada:",
    "Backup failed — see the activity log.": "Error en la copia de seguridad: consulta el registro de actividad.",
    "{n} added": "{n} añadido(s)",
    "{n} updated": "{n} actualizado(s)",
    "{n} failed": "{n} fallido(s)",
    "{n} failed.": "{n} fallido(s).",
    "Export Import Log": "Exportar registro de importación",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "Definición — {word}",
    "Failed to save definition:\n{error}": "Error al guardar la definición:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "Editar — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "Error al guardar la palabra:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "Adjuntar la(s) etiqueta(s) seleccionada(s) a cada palabra seleccionada"
    ),
    "Failed to add tag:\n{error}": "Error al añadir la etiqueta:\n{error}",
    "Failed to apply tags:\n{error}": "Error al aplicar las etiquetas:\n{error}",
    "Failed to remove tags:\n{error}": "Error al quitar las etiquetas:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "Genera un texto con IA utilizando los campos Idioma, Nivel y Tema a continuación. "
        "Elige una opción de tema o escribe el tuyo propio."
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "Generando un texto en {language} a partir de {count} palabra(s) con {ai}:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "Escribe o pega un texto en el editor a continuación, dale un título, "
        "establece el idioma y luego guárdalo."
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "Extrae el texto legible de un artículo desde cualquier página web. "
        "Las páginas tras un inicio de sesión o creadas puramente con JavaScript pueden no funcionar."
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    "View definition (double-click)": "Ver definición (doble clic)",
    "Read selected words aloud": "Leer palabras seleccionadas en voz alta",
    "Toggle favorite": "Alternar favorito",
    "Add / remove tags": "Añadir / quitar etiquetas",
    "Edit word": "Editar palabra",
    "Copy words": "Copiar palabras",
    "Generate text from selection": "Generar texto a partir de la selección",

    "PDF files (*.pdf)": "Archivos PDF (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Archivos de Excel (*.xlsx *.xls)",
    "CSV files (*.csv)": "Archivos CSV (*.csv)",
    "Text files (*.txt)": "Archivos de texto (*.txt)",
    "MP3 files (*.mp3)": "Archivos MP3 (*.mp3)",
    "Open Excel Table": "Abrir tabla de Excel",
    "Save Import Template": "Guardar plantilla de importación",

    "Cloud sync": "Sincronización en la nube",
    "Not connected. Check internet or credentials": "Sin conexión. Comprueba internet o tus credenciales",
    "Syncing with cloud…": "Sincronizando con la nube…",
    "Sync completed successfully": "Sincronización completada con éxito",
    "Sync enabled but not connected. Check settings.": "Sincronización activada pero no conectada. Revisa los ajustes.",
    "idle": "inactiva",
    "syncing": "sincronizando",
    "success": "éxito",
    "error": "error",

    "No data yet": "Aún no hay datos",
    "No activity yet": "Aún no hay actividad",
    "Not enough activity yet": "Aún no hay suficiente actividad",

    "APIs": "APIs",
    "Audio (MP3)": "Audio (MP3)",
    "Sync": "Sincronización",

    "OpenAI API key (.env)": "Clave API de OpenAI (.env)",
    "Google API key (.env)": "Clave API de Google (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        'Facturado por uso: obtén una clave en <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Modelos: gpt-4o-mini, gpt-4o, gpt-4.1-mini… Uso de la API: consulta el <a href="https://platform.openai.com/usage">panel de control</a>.',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        'Nivel gratuito disponible: obtén una clave en <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Modelos: gemini-2.5-flash, gemini-2.5-flash-lite… Uso de la API: consulta <a href="https://aistudio.google.com/usage">AI Studio</a>.',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'Obtén una clave en <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Usa https://api-free.deepl.com/v2/translate para claves del plan gratuito.',

    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>Prepara un archivo de Excel con las columnas <b>Language1, Language2, Word1, Word2</b> (nombradas así en una fila de encabezado; las columnas adicionales se ignorarán) o sin encabezados, con las cuatro primeras columnas exactamente en ese orden.</li><li>Abre el menú de la app → <i>Importar Excel a la base de datos…</i> y elige el archivo.</li><li>Revisa las filas propuestas y haz clic en <i>Importar</i>.</li></ol>",

    "created by": "creado por",
    "Version": "Versión",
    "Build": "Compilación",
    "Your personal vocabulary companion": "Tu compañero personal de vocabulario",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "Crea, estudia y recuerda vocabulario en múltiples idiomas: con sincronización en la nube, definiciones asistidas por IA, traducciones, síntesis de voz y exportación flexible.",
    "Source code": "Código fuente",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "Tu compañero personal de vocabulario con sincronización en la nube, definiciones con IA, traducciones, síntesis de voz y opciones de exportación.",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "Licenciado bajo la Licencia Pública General Affero de GNU v3.0. Esta atribución debe conservarse (AGPL §7).",
    "Found a bug or have an idea?": "¿Encontraste un error o tienes una idea?",
    "Report an issue": "Notificar un problema",
    "What would you like to report?": "¿Qué te gustaría notificar?",
    "A bug or technical problem": "Un error o problema técnico",
    "Creates a report with app diagnostics to send to the developers.":
        "Crea un informe con diagnósticos de la aplicación para enviar a los desarrolladores.",
    "Inappropriate AI-generated content": "Contenido generado por IA inapropiado",
    "Report a definition, text, or translation the AI produced.":
        "Notificar sobre una definición, texto o traducción que haya producido la IA.",
    "Report: inappropriate AI-generated content":
        "Informe: contenido generado por IA inapropiado",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "Por favor, describe el contenido generado por IA que estás notificando.\n\n"
        "Dónde apareció (definición / texto generado / traducción de palabra):\n"
        "La palabra o texto en cuestión:\n"
        "Por qué es inapropiado:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "Para notificar contenido generado por IA inapropiado, envíanos un correo a {email}.",

    "Support": "Apoyar",
    "Support Lingueez": "Apoyar a Lingueez",
    "Lingueez is free and open-source.": "Lingueez es gratuito y de código abierto.",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Si disfrutas de Lingueez y lo encuentras útil, una contribución puntual ayuda a cubrir los servidores tras la sincronización opcional en la nube y apoya el desarrollo continuo. No hay muros de pago: todas las funciones siguen siendo gratuitas de todos modos.",
    "Support Lingueez's development": "Apoyar el desarrollo de Lingueez",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "La opción de Stripe es de un solo pago, sin suscripción. Los pagos se procesan de forma segura a través de Stripe o GitHub.",

    "Updates": "Actualizaciones",
    "Check for updates": "Buscar actualizaciones",
    "You're up to date.": "Estás actualizado.",
    "Update available": "Actualización disponible",
    "Update available — v{version}": "Actualización disponible — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} está disponible (tienes la versión {current}).",
    "Skip this version": "Omitir esta versión",
    "Later": "Más tarde",
    "Download": "Descargar",
    "Check for updates on startup": "Buscar actualizaciones al iniciar",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "Busca una vez al día si hay una versión más nueva y te lo notifica; "
        "nunca se descarga ni se instala nada automáticamente.",

    "in": "pulg",
    " s": " s",

    "New": "Nueva",
    "To Learn": "Por aprender",
    "Reviewing": "Repasando",
    "Ignored": "Omitida",
    "Undo": "Deshacer",
    "Restored": "Restaurado",
    "Ignore word": "Ignorar palabra",
    "Ignore this word": "Ignorar esta palabra",
    "Already ignored.": "Ya está ignorada.",
    "{count} word(s) won't come up in practice.": "{count} palabra(s) no aparecerá(n) en la práctica.",
    "'{word}' is back in rotation": "«{word}» vuelve a la rotación",
    "'{word}' won't come up again": "«{word}» no volverá a aparecer",
    "Mark for relearning": "Marcar para volver a aprender",
    "Forgot this word — move it to To Learn": "Olvidé esta palabra — mover a «Por aprender»",
    "'{word}' is queued to learn again": "«{word}» está en la cola para volver a aprender",
    "{count} word(s) queued to learn again.": "{count} palabra(s) en la cola para volver a aprender.",
    "Nothing here to relearn yet.": "Aquí todavía no hay nada que volver a aprender.",

    "Compact": "Compacto",
    "Normal": "Normal",
    "Comfortable": "Cómodo",
    "Spacious": "Espacioso",

    "English": "Inglés",
    "German": "Alemán",
    "Spanish": "Español",
    "Ukrainian": "Ucraniano",
    "French": "Francés",
    "Italian": "Italiano",
    "Portuguese": "Portugués",
    "Russian": "Ruso",
    "Greek": "Griego",
    "Arabic": "Árabe",
    "Bengali": "Bengalí",
    "Cantonese": "Cantonés",
    "Hindi": "Hindi",
    "Japanese": "Japonés",
    "Korean": "Coreano",
    "Mandarin": "Mandarín",
    "Polish": "Polaco",
    "Turkish": "Turco",
    "Vietnamese": "Vietnamita",
    "Afrikaans": "Afrikáans",
    "Albanian": "Albanés",
    "Amharic": "Amhárico",
    "Armenian": "Armenio",
    "Azerbaijani": "Azerbaiyano",
    "Basque": "Euskera",
    "Belarusian": "Bielorruso",
    "Bosnian": "Bosnio",
    "Bulgarian": "Búlgaro",
    "Catalan": "Catalán",
    "Cebuano": "Cebuano",
    "Chichewa": "Chichewa",
    "Chinese": "Chino",
    "Croatian": "Croata",
    "Czech": "Checo",
    "Danish": "Danés",
    "Dutch": "Holandés",
    "Estonian": "Estonio",
    "Filipino": "Filipino",
    "Finnish": "Finlandés",
    "Galician": "Gallego",
    "Georgian": "Georgiano",
    "Gujarati": "Guyarati",
    "Haitian Creole": "Criollo haitiano",
    "Hausa": "Hausa",
    "Hawaiian": "Hawaiano",
    "Hebrew": "Hebreo",
    "Hmong": "Hmong",
    "Hungarian": "Húngaro",
    "Icelandic": "Islandés",
    "Igbo": "Igbo",
    "Indonesian": "Indonesio",
    "Irish": "Irlandés",
    "Javanese": "Javanés",
    "Kannada": "Canarés",
    "Kazakh": "Cazajo",
    "Khmer": "Jemer",
    "Kinyarwanda": "Kinyarwanda",
    "Kyrgyz": "Kirguís",
    "Lao": "Lao",
    "Latin": "Latín",
    "Latvian": "Letón",
    "Lithuanian": "Lituano",
    "Luxembourgish": "Luxemburgués",
    "Macedonian": "Macedonio",
    "Malagasy": "Malgache",
    "Malay": "Malayo",
    "Malayalam": "Malayalam",
    "Maltese": "Maltés",
    "Maori": "Maorí",
    "Marathi": "Maratí",
    "Mongolian": "Mongol",
    "Myanmar (Burmese)": "Birmano",
    "Nepali": "Nepalí",
    "Norwegian": "Noruego",
    "Odia": "Odia",
    "Pashto": "Pastún",
    "Persian": "Persa",
    "Punjabi": "Punyabí",
    "Romanian": "Rumano",
    "Samoan": "Samoano",
    "Scots Gaelic": "Gaélico escocés",
    "Serbian": "Serbio",
    "Sesotho": "Sesotho",
    "Shona": "Shona",
    "Sindhi": "Sindhi",
    "Sinhala": "Cingalés",
    "Slovak": "Eslovaco",
    "Slovenian": "Esloveno",
    "Somali": "Somalí",
    "Sundanese": "Sundanés",
    "Swahili": "Suajili",
    "Swedish": "Sueco",
    "Tajik": "Tayiko",
    "Tamil": "Tamil",
    "Tatar": "Tártaro",
    "Telugu": "Telugu",
    "Thai": "Tailandés",
    "Turkmen": "Turcomano",
    "Urdu": "Urdu",
    "Uyghur": "Uigur",
    "Uzbek": "Uzbeco",
    "Welsh": "Galés",
    "Xhosa": "Xhosa",
    "Yiddish": "Yidis",
    "Yoruba": "Yoruba",
    "Zulu": "Zulú",

    # --- Onboarding tour ---
    "Back": "Atrás",
    "Next": "Siguiente",
    "Done": "Hecho",
    "Show Tour": "Mostrar recorrido",
    "Step {n} of {total}": "Paso {n} de {total}",
    "Your library": "Tu biblioteca",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "Cambia entre tus Palabras, Textos y Estadísticas desde esta barra lateral.",
    "Add a word": "Añade una palabra",
    "Find anything": "Encuentra lo que sea",
    "Search across your words, translations and tags as you type.":
        "Busca en tus palabras, traducciones y etiquetas mientras escribes.",
    "Add a new word here — its translation can be fetched automatically.":
        "Añade una nueva palabra aquí: su traducción se puede obtener automáticamente.",
    "Listen and learn": "Escucha y aprende",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "Selecciona palabras y presiona Leer para escucharlas en voz alta. "
        "La escucha repetida promueve cada palabra de Nueva a Repasando, Aprendiendo "
        "y finalmente Dominada.",
    "Generate a text": "Genera un texto",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "Convierte las palabras seleccionadas en una corta historia escrita por IA: "
        "tu vocabulario en contexto.",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "Tu vocabulario se mantiene sincronizado entre dispositivos. Haz clic para "
        "ver el estado o para sincronizar ahora mismo.",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "Activa la sincronización en la nube, cambia de idioma, modifica la apariencia y "
        "más desde Ajustes.",

    # --- Texts tour ---
    "Add texts": "Añade textos",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "Escribe o pega un texto, consigue uno de Internet "
        "(IA / Wikipedia / URL / RSS) o importa archivos .txt.",
    "Your texts": "Tus textos",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "Explora tus textos guardados y fíltralos por idioma, "
        "nivel o tema.",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "Escucha cualquier texto en voz alta y haz clic en una palabra mientras lees "
        "para ver su traducción o añadirla a tu vocabulario.",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "Muestra una traducción paralela lado a lado; elige el idioma "
        "con la flecha contigua.",
    "Reading modes": "Modos de lectura",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "El modo enfoque oculta la lista, el modo papel cambia el "
        "fondo y Editar te permite retocar el texto.",

    # --- Flashcards tour ---
    "Choose your deck": "Elige tu mazo",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "Elige qué entra en el mazo: tarjetas pendientes de repaso, "
        "palabras de tu filtro actual, las últimas añadidas "
        "o una selección manual.",
    "Shape the session": "Personaliza la sesión",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "Define cuántas tarjetas repasar, mezcla su orden y "
        "activa la pronunciación de cada tarjeta conforme aparece y se gira.",
    "Preview the deck": "Vista previa del mazo",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "Las tarjetas exactas que contendrá tu sesión. Haz clic en un mosaico para "
        "leer o editar su definición, o en el altavoz para escuchar la "
        "palabra.",
    "Review and grade": "Repasa y califica",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "Gira cada tarjeta y califica qué tan bien la sabías: Difícil, "
        "Bien o Fácil. La repetición espaciada decide cuándo reaparece "
        "cada tarjeta: las palabras fáciles esperan más, las difíciles vuelven "
        "antes. La barra espaciadora gira, las teclas 1–3 califican.",
    "Or just listen": "O simplemente escucha",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "«Reproducir mazo» convierte la sesión en audio: las tarjetas avanzan "
        "y se giran en sincronía con la voz. Pausa en cualquier momento para calificar "
        "una tarjeta manualmente.",

    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "Tu vocabulario de un vistazo: totales, palabras dominadas, "
        "idiomas y tu racha actual.",
    "See how your vocabulary has grown over time.":
        "Observa cómo ha crecido tu vocabulario con el tiempo.",
    "Track how much you've reviewed over time.":
        "Haz un seguimiento de cuánto has repasado a lo largo del tiempo.",

    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "Ejemplo: Un paseo por la ciudad",
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
        "La mañana era luminosa y las calles estaban tranquilas. Una joven "
        "caminaba despacio por el viejo camino, mirando las casas altas y las "
        "pequeñas tiendas que acababan de abrir. Se detuvo a comprar pan fresco "
        "y un café, y luego cruzó la plaza hacia el parque. Los niños jugaban "
        "cerca del río mientras sus padres conversaban en los bancos cercanos. "
        "Ella se sentó bajo un gran árbol, abrió su libro y empezó a leer. "
        "La historia trataba sobre un viajero que cruzó las montañas en busca "
        "de un viejo amigo al que no había visto en muchos años. Después de un "
        "tiempo levantó la vista, observando los barcos flotar lentamente río "
        "abajo y las aves circular en lo alto sobre los tejados. Un músico callejero "
        "comenzó a tocar cerca de allí, y las suaves notas acompañaron sus "
        "pensamientos. Era una mañana tranquila y feliz, del tipo que a ella más le gustaba.",
    "Demo": "Demostración",

    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "Clave API de OpenAI no válida. Compruébala en Ajustes → Traducción e IA → IA → OpenAI.",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "Tu cuenta de OpenAI se ha quedado sin créditos. Añade créditos en "
        "platform.openai.com/account/billing, o cambia el proveedor "
        "de IA a Gemini en Ajustes → Traducción e IA → IA.",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "Límite de frecuencia de OpenAI alcanzado. Espera un momento e inténtalo de nuevo.",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "Modelo de OpenAI desconocido. Comprueba el nombre del modelo en Ajustes → Traducción e IA → IA → OpenAI.",
    "Could not reach OpenAI. Check your internet connection.":
        "No se pudo conectar con OpenAI. Comprueba tu conexión a internet.",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Cuota de Gemini agotada. El nivel gratuito se restablece diariamente; espera "
        "o crea una nueva clave en aistudio.google.com/app/apikey.",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "Clave API de Google no válida. Compruébala en Ajustes → Traducción e IA → IA → Gemini.",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "Modelo de Gemini desconocido. Comprueba el nombre del modelo en Ajustes → Traducción e IA → IA → Gemini.",

    # --- Words empty state ---
    "Your vocabulary journey starts here": "Tu viaje de vocabulario comienza aquí",
    "Add your first word — its translation can be fetched automatically.":
        "Añade tu primera palabra: su traducción se puede obtener automáticamente.",
    "Add your first word": "Añadir tu primera palabra",
    "Take the tour": "Ver el recorrido",
    "No matching words": "No hay palabras coincidentes",
    "Try a different search or filter.": "Prueba una búsqueda o filtro diferente.",
    "Clear filters": "Limpiar filtros",

    # --- Texts empty state ---
    "Your reading library starts here": "Tu biblioteca de lectura comienza aquí",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "Añade un texto para leer: escribe o pega el tuyo propio, consigue uno "
        "de Internet o importa un archivo .txt.",
    "Add a text": "Añadir un texto",
    "Fetch from the Internet": "Obtener de Internet",
    "Import .txt": "Importar .txt",

    # demo text-list stub titles
    "My first story": "Mi primera historia",
    "A news article": "Un artículo de noticias",
    "A short poem": "Un poema corto",
    "Travel notes": "Notas de viaje",

    # demo text-list stub first sentences
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "Había una vez, en un pequeño pueblo junto al mar, "
        "un joven y curioso zorro.",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "Investigadores han encontrado una nueva forma de estudiar cómo "
        "los idiomas cambian y crecen a lo largo de los siglos.",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "El viento camina suavemente entre los árboles de otoño, "
        "llevando viejas canciones medio olvidadas.",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "Día uno: llegamos a la ciudad muy de noche, y las "
        "calles aún estaban llenas de una luz cálida.",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "Elementos eliminados en otro dispositivo",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "Mientras este dispositivo estaba desconectado, {n} elemento(s) de aquí fueron eliminados en tus "
        "otros dispositivos. ¿Mantenerlos en la nube o quitarlos de este dispositivo?",
    "(untitled)": "(sin título)",
    "[Text] {title}": "[Texto] {title}",
    "Remove from this device": "Quitar de este dispositivo",
    "Decide later": "Decidir más tarde",
    "Keep & upload": "Mantener y subir",
    "Not now": "Ahora no",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "Ingresa un nombre para el perfil sin conexión.",
    "You can keep up to {max} offline profiles. Remove one to add another.": "Puedes tener hasta {max} perfiles sin conexión. Quita uno para añadir otro.",
    "New offline profile": "Nuevo perfil sin conexión",
    "Profile name:": "Nombre del perfil:",
    "Offline profile": "Perfil sin conexión",
    "Rename offline profile": "Renombrar perfil sin conexión",
    "Offline profiles": "Perfiles sin conexión",
    "Add offline profile…": "Añadir perfil sin conexión…",
    "Profile actions": "Acciones del perfil",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "Bibliotecas independientes y exclusivas para este dispositivo con su propia base de datos. Nunca se sincronizan y no requieren inicio de sesión.",
    "Default (local)": "Predeterminado (local)",
    "Rename": "Renombrar",
    "Delete offline profile": "Eliminar perfil sin conexión",
    "Enable cloud sync…": "Activar sincronización en la nube…",
    "Could not create the profile.": "No se pudo crear el perfil.",
    "Created and switched to “{name}”.": "Creado y cambiado a «{name}».",
    "Deleted “{name}”.": "Se eliminó «{name}».",
    "Untitled profile": "Perfil sin título",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "¿Eliminar permanentemente el perfil sin conexión «{name}»? Sus palabras y textos solo existen en este dispositivo: no hay copia en la nube. La base de datos se archivará primero en la carpeta de copias de seguridad, pero esto no se podrá deshacer en la app.",
    "this profile": "este perfil",
    "Connect to the internet to merge this profile into your account.": "Conéctate a internet para combinar este perfil con tu cuenta.",
    "Enable cloud sync for this profile": "Activar sincronización en la nube para este perfil",
    "Continue": "Continuar",
    "Upload words": "Subir palabras",
    "Upload texts": "Subir textos",
    "Upload & sync": "Subir y sincronizar",
    "Could not upload this profile. Your data is unchanged.": "No se pudo subir este perfil. Tus datos permanecen sin cambios.",
    "“{name}” is now synced to your account.": "«{name}» ahora está sincronizado con tu cuenta.",
    "Everything in this profile is already in your account.": "Todo en este perfil ya está en tu cuenta.",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "Inicia sesión o crea una cuenta para hacer una copia de seguridad de «{name}» y sincronizarlo en tus dispositivos. Las palabras y textos de este perfil se subirán y se convertirá en tu cuenta sincronizada en este dispositivo. Primero se archivará una copia en la carpeta de copias de seguridad.",
    "Upload “{name}” to your account": "Subir «{name}» a tu cuenta",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "Tu perfil se convierte en la cuenta sincronizada «{who}» en este dispositivo y se sube a la nube.",
    "Merge “{name}” into your account": "Combinar «{name}» con tu cuenta",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "Esta cuenta ya tiene datos en este dispositivo. Las palabras y textos de tu perfil que no estén allí se añadirán, sin sobrescribir nada. Luego, «{name}» se archivará en la carpeta de copias de seguridad y se eliminará.",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "Este perfil tiene {items}, guardados únicamente en este dispositivo. Activa la sincronización en la nube para hacer una copia de seguridad y estudiar en todos tus dispositivos.",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "Elige los elementos a añadir. Se copiarán en tu cuenta y se subirán a la nube. Luego, «{name}» se archivará en la carpeta de copias de seguridad y se eliminará.",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Acepto los <a href=\"{terms}\">Términos del Servicio</a> y la <a href=\"{privacy}\">Política de Privacidad</a>.",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "Por favor, acepta los Términos del Servicio y la Política de Privacidad para continuar.",
    "Updated Terms & Privacy": "Términos y Privacidad actualizados",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "Hemos actualizado nuestros Términos del Servicio y la Política de Privacidad. Por favor, revísalos y acéptalos para seguir usando tu cuenta.",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Acepto los <a href=\"{terms}\">Términos del Servicio</a> y la <a href=\"{privacy}\">Política de Privacidad</a> actualizados.",
    "Sign out": "Cerrar sesión",
    "I agree": "Acepto",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">Política de Privacidad</a> · <a href=\"{terms}\">Términos</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "Al continuar, aceptas los <a href=\"{terms}\">Términos del Servicio</a> y la <a href=\"{privacy}\">Política de Privacidad</a>.",
    "Privacy Policy": "Política de Privacidad",
    "Terms": "Términos",
    "Website": "Sitio web",
    "Contact": "Contacto",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "Tarjetas",
    "Practice your vocabulary": "Practica tu vocabulario",
    "Due cards": "Tarjetas pendientes",
    "Current filter": "Filtro actual",
    "Newest": "Más recientes",
    "Selected words": "Palabras seleccionadas",
    "Deck size": "Tamaño del mazo",
    "Default deck size": "Tamaño predeterminado del mazo",
    "Shuffle": "Mezclar",
    "Start session": "Iniciar sesión",
    "Play deck": "Reproducir mazo",
    "{n} cards ready to review": "{n} tarjetas listas para repasar",
    "No cards due — great job!": "No hay tarjetas pendientes. ¡Buen trabajo!",
    "{n} selected words": "{n} palabras seleccionadas",
    "No words to practice.": "No hay palabras para practicar.",
    "End session": "Finalizar sesión",
    "Listening — pause to review manually":
        "Escuchando: pausa para repasar manualmente",
    "Show answer": "Mostrar respuesta",
    "Hard": "Difícil",
    "Good": "Bien",
    "Easy": "Fácil",
    "Space or click to flip": "Espacio o clic para girar",
    "Card {current} of {total}": "Tarjeta {current} de {total}",
    "{n} correct": "{n} correctas",
    "Session complete!": "¡Sesión completada!",
    "You listened to {n} of {total} cards.": "Escuchaste {n} de {total} tarjetas.",
    "Correct: {n} of {total}": "Correctas: {n} de {total}",
    "New session": "Nueva sesión",
    "Practice hard words": "Practicar palabras difíciles",
    "Hard words": "Palabras difíciles",
    "Hard words cleared!": "¡Palabras difíciles completadas!",
    "Open Flashcards when Read Aloud starts":
        "Abrir Tarjetas al iniciar Lectura en voz alta",
    "Stop": "Detener",
    "Auto-pronounce": "Pronunciación automática",
    "Speak each card as it appears and when it flips":
        "Pronunciar cada tarjeta cuando aparece y al girarse",
    "Deck preview": "Vista previa del mazo",
    "{n} cards": "{n} tarjetas",
    "Due": "Pendiente",
    "In {n} d": "En {n} d",
    "{n} d": "{n} d",
    "{n} mo": "{n} m",
    "{n} y": "{n} a",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Lingueez para Android…",
    "Android app": "Aplicación para Android",
    "Lingueez on Android": "Lingueez en Android",
    "Take your vocabulary with you": "Lleva tu vocabulario contigo",
    "Preview of Lingueez on a phone": "Vista previa de Lingueez en un teléfono",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Inicia sesión con tu cuenta de Lingueez y tu vocabulario ya estará allí: "
        "nada que configurar, nada que transferir.",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "Inicia sesión con una cuenta gratuita de Lingueez en ambos y tu vocabulario "
        "se sincronizará con el teléfono: sin archivos que copiar.",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "Inicia sesión con una cuenta gratuita de Lingueez y tus palabras se sincronizarán con tu teléfono.",
    "Synced both ways": "Sincronizado en ambas direcciones",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "Las palabras que añades en el teléfono te esperan en el ordenador, y "
        "viceversa.",
    "Listen with the screen off": "Escucha con la pantalla apagada",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "Controles en la pantalla de bloqueo para que el repaso continúe con el teléfono "
        "en tu bolsillo.",
    "Save a word from any app": "Guarda una palabra desde cualquier app",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "Comparte texto hacia Lingueez y llegará a tu vocabulario, listo para "
        "completarse más tarde.",
    "Point your phone's camera at the code":
        "Apunta la cámara de tu teléfono al código",
    "Get it on Google Play": "Consíguelo en Google Play",
    "Copy link": "Copiar enlace",
    "Link copied": "Enlace copiado",
    "Lingueez is now on Android": "Lingueez ya está en Android",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Inicia sesión con tu cuenta de Lingueez: tu vocabulario ya está allí.",
    "Dismiss": "Descartar",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "Usa tu cuenta de Lingueez sin problemas entre tu ordenador y dispositivos Android.",
    "Get the app…": "Obtener la app…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "Cuestionario",
    "Quiz (recall practice)": "Cuestionario (práctica de recuerdo)",
    "Recall your words, one question at a time":
        "Recuerda tus palabras, una pregunta a la vez",
    "Questions": "Preguntas",
    "Answer with": "Responder con",
    "Choices": "Opciones",
    "Typing": "Escritura",
    "Ask": "Preguntar",
    "Term": "Término",
    "Mixed": "Mixto",
    "Auto-advance": "Avance automático",
    "Move on by itself after a correct answer":
        "Continuar solo tras una respuesta correcta",
    "Speak the question, then the answer once it is revealed":
        "Pronunciar la pregunta y luego la respuesta al revelarla",
    "Start quiz": "Empezar cuestionario",
    "questions ready": "preguntas listas",
    "Nothing to quiz": "Nada que preguntar",
    "No words match this deck.": "Ninguna palabra coincide con este mazo.",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "Un cuestionario necesita al menos dos palabras: las respuestas incorrectas "
        "salen precisamente de las que no se te preguntan.",
    "Not enough words": "No hay palabras suficientes",
    "Add a few more words, or widen the deck.":
        "Añade algunas palabras más o amplía el mazo.",
    "Question {n} of {total}": "Pregunta {n} de {total}",
    "Missed words": "Palabras falladas",
    "End quiz": "Terminar cuestionario",
    "Answer in {language}": "Responde en {language}",
    "Type the answer": "Escribe la respuesta",
    "Check": "Comprobar",
    "Click to continue": "Haz clic para continuar",
    "See results": "Ver resultados",
    "Almost — it is \"{answer}\"": "Casi — es «{answer}»",
    "It is \"{answer}\"": "Es «{answer}»",
    "Now {status}": "Ahora {status}",
    "Correct": "Correctas",
    "Missed": "Falladas",
    "Worth another look": "Merece otro repaso",
    "Again": "Otra vez",
    "Missed words cleared!": "¡Palabras falladas superadas!",
    "Perfect run": "Ronda perfecta",
    "Quiz complete": "Cuestionario completado",
    "Practice missed": "Repasar falladas",
    "Default number of questions": "Número de preguntas predeterminado",
    "Move on after a correct answer": "Continuar tras una respuesta correcta",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "Elige sobre qué te preguntarán",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "Los mismos mazos que en las tarjetas: palabras pendientes, tu filtro actual, "
        "las más recientes o una selección manual, y cuántas preguntas.",
    "Choices or typing": "Opciones o escritura",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "«Opciones» ofrece cuatro respuestas para elegir; «Escritura» te pide "
        "escribirla: más difícil, pero mejor prueba. La escritura perdona acentos y "
        "erratas pequeñas. «Preguntar» decide qué lado ves: el término, su traducción "
        "o una mezcla.",
    "Start, and it counts": "Empieza, y cuenta",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "La barra muestra de qué se compone el mazo por estado. Cada respuesta "
        "alimenta el mismo calendario de repetición espaciada que las tarjetas: la "
        "palabra que recuerdas vuelve más tarde y la que fallas, antes.",
}

# Date names, read by app.i18n. Months are in lowercase as standard in Spanish dates.
# Weekdays start on Monday (datetime.weekday(): 0 = Monday).
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
          "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS_ABBR = ["ene", "feb", "mar", "abr", "may", "jun",
               "jul", "ago", "sep", "oct", "nov", "dic"]
WEEKDAYS = ["Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"]
WEEKDAYS_ABBR = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"]