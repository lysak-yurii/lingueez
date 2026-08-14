# Lingueez — Japanese (ja) translations.
# Keys are English UI strings; values are their Japanese equivalents.

# Native name of this language, shown in the interface-language picker.
LANGUAGE_NAME = "日本語"

TRANSLATIONS: dict[str, str] = {
    # ── Common ─────────────────────────────────────────────────────────────
    "Cancel": "キャンセル",
    "OK": "OK",
    "Close": "閉じる",
    "Save": "保存",
    "Delete": "削除",
    "Edit": "編集",
    "Remove": "削除",
    "Add": "追加",
    "Refresh": "更新",
    "Import": "インポート",
    "Export": "エクスポート",
    "Search": "検索",
    "Fetch": "取得",
    "Browse…": "参照…",
    "Clear": "クリア",
    "Pause": "一時停止",
    "Resume": "再開",
    "Language": "言語",
    "Translation": "翻訳",
    "Word": "単語",
    "Status": "ステータス",
    "Error": "エラー",
    "Title": "タイトル",
    "Topic": "トピック",
    "Level": "レベル",
    "Generate": "生成",
    "Generating…": "生成中…",
    "Translating…": "翻訳中…",
    "Format": "フォーマット",
    "Style": "スタイル",
    "Model": "モデル",
    "Font": "フォント",
    "Usage": "使用量",
    "Translation language": "翻訳言語",

    # ── main_window.py ──────────────────────────────────────────────────────
    "Menu": "メニュー",
    "Open Excel Table…": "Excel表を開く…",
    "Import Excel to Database…": "Excelをデータベースにインポート…",
    "Save Import Template…": "インポートテンプレートを保存…",
    "PDF…": "PDF…",
    "Excel / CSV…": "Excel / CSV…",
    "TXT…": "TXT…",
    "Audio (MP3)…": "音声 (MP3)…",
    "Backups…": "バックアップ…",
    "Show Source column": "「ソース」列を表示",
    "Show Created At column": "「作成日時」列を表示",
    "Max words…": "最大単語数…",
    "View Log": "ログを表示",
    "About": "アプリについて",
    "Quit": "終了",
    "Words": "単語一覧",
    "Texts": "テキスト一覧",
    "Statistics": "統計",
    "Bin (deleted items)": "ゴミ箱 (削除済み項目)",
    "Settings": "設定",
    "Vocabulary": "語彙ノート",
    "Search words, translations or tags…": "単語、翻訳、タグを検索…",
    "Search texts by title, content or words…": "タイトル、内容、単語からテキストを検索…",
    "Search scope": "検索範囲",
    "Search scope…": "検索範囲…",
    "Nothing to practice yet": "まだ練習する単語がありません",
    "Add words to your vocabulary and they show up here.": "単語を追加すると、ここに表示されます。",
    "Come back when cards are due, or practice the newest words now.":
        "復習の時期になったら戻ってくるか、今すぐ最新の単語を練習しましょう。",
    "Practice newest words": "最新の単語を練習",
    "Pick another deck above, or adjust your filters on the Words page.":
        "上で別のデッキを選ぶか、単語ページでフィルターを調整してください。",
    "You're all caught up": "すべて完了しています",
    "Add word": "単語を追加",
    "Copy a word in any app, then press:":
        "どのアプリでも単語をコピーして押すだけ：",
    "Set a shortcut": "ショートカットを設定",
    "Copy a word in any app, then press {keys} to add it with its "
    "translation.":
        "どのアプリでも単語をコピーして {keys} を押すと、訳付きで追加されます。",
    "Set a shortcut in Settings to add copied words from any app.":
        "設定でショートカットを登録すると、どのアプリからでもコピーした単語を追加できます。",
    " Favorites": " お気に入り",
    " Filters": " フィルター",
    "Filters that don't fit the table": "テーブルに入り切らないフィルター",
    "More actions": "その他の操作",
    "Filter by tag": "タグでフィルター",
    "Close file and return to your vocabulary": "ファイルを閉じて語彙ノートに戻る",
    "Definition": "定義",
    "Read": "読み上げ",
    "Favorite": "お気に入り",
    "Tags": "タグ",
    "Copy": "コピー",
    "Text": "テキスト",
    "Delete selected (Del)": "選択項目を削除 (Del)",
    "No data": "データなし",
    "No texts yet": "テキストがまだありません",
    "Words: {shown}/{total}": "単語: {shown}/{total}",
    "Texts: {total}": "テキスト: {total}",
    "Texts: {shown}/{total}": "テキスト: {shown}/{total}",
    "{count} selected": "{count} 件選択中",
    "No selection": "選択されていません",
    "Please select at least one word.": "単語を少なくとも1つ選択してください。",
    "Saved": "保存しました",
    "'{word}' updated.": "「{word}」を更新しました。",
    "Database Error": "データベースエラー",
    "Delete {count} word(s)?": "{count} 件の単語を削除しますか？",
    "Deleted": "削除完了",
    "{count} word(s) deleted.": "{count} 件の単語を削除しました。",
    "Deleted with {n} error(s).": "{n} 件のエラーが発生して削除されました。",
    "Favorites": "お気に入り",
    "{count} word(s) added to favorites.": "{count} 件の単語をお気に入りに追加しました。",
    "{count} word(s) removed from favorites.": "{count} 件の単語をお気に入りから削除しました。",
    "Status set to '{status}' for {count} word(s).": "{count} 件の単語のステータスを「{status}」に設定しました。",
    "Max Words": "最大単語数",
    "Show only the first N words (0 = show all):": "最初の N 個の単語のみ表示 (0 = すべて表示):",
    "View Definition": "定義を表示",
    "Copy Word": "単語をコピー",
    "Copy Translation": "翻訳をコピー",
    "Toggle Favorite": "お気に入りを切り替え",
    "Change Status…": "ステータスを変更…",
    "Add / Remove Tags…": "タグを追加 / 削除…",
    "Read Aloud": "読み上げ",
    "Change Status": "ステータスを変更",
    "New status:": "新しいステータス:",
    "Copied": "コピーしました",
    "{count} row(s) copied to clipboard.": "{count} 行をクリップボードにコピーしました。",
    "{count} item(s) copied to clipboard.": "{count} 件の項目をクリップボードにコピーしました。",
    "Copy Word(s)": "単語をコピー",
    "Copy Translation(s)": "翻訳をコピー",
    "Copy Both": "両方をコピー",
    "Search in Word": "単語内を検索",
    "Search in Translation": "翻訳内を検索",
    "Search in Tags": "タグ内を検索",
    "Promoted": "昇格しました",
    "Google Cloud TTS unavailable": "Google Cloud TTS は利用できません",
    "Selection limit": "選択数の制限",
    "Only the first 200 selected words will be read.": "選択された最初の 200 単語のみが読み上げられます。",
    "Only the first 50 words will be used.": "最初の 50 単語のみが使用されます。",
    "Select words to save as audio.": "音声として保存する単語を選択してください。",
    "Nothing to export.": "エクスポートするデータがありません。",
    "Export Error": "エクスポートエラー",
    "Settings saved.": "設定を保存しました。",
    "Generated text saved.": "生成されたテキストを保存しました。",
    "Show": "表示",
    "Add Word": "単語を追加",
    "Stop reading": "読み上げを停止",
    "Read — Read selected words aloud": "読み上げ — 選択した単語を読み上げます",
    "Translation": "翻訳",

    # ── settings_dialog.py ─────────────────────────────────────────────────
    "Appearance": "外観",
    "Audio": "音声",
    "Learning": "学習",
    "Listening": "リスニング",
    "Backups": "バックアップ",
    "Sync your library?": "ライブラリを同期しますか？",
    "This will reconcile your device with the cloud:": "デバイスとクラウドの整合性を統合します:",
    "Sync now": "今すぐ同期",
    "Upload": "アップロード",
    "Synced — ↑{up} ↓{down}": "同期完了 — ↑{up} ↓{down}",
    "Upload restored library?": "復元されたライブラリをアップロードしますか？",
    "Library restored. You'll be asked to upload it the next time you connect a sync server.": "ライブラリが復元されました。次回同期サーバー接続時にアップロードの確認が表示されます。",
    "Merging this restored backup with your cloud:": "復元されたバックアップをクラウドと統合しています:",
    "This backup has {items}. Upload and merge it into your cloud now, or leave your cloud unchanged for now?": "このバックアップには {items} が含まれています。今すぐクラウドにアップロードして統合しますか？それともクラウドを変更せずに残しますか？",
    "General": "一般",
    "Read-aloud": "読み上げ機能",
    "Translation & AI": "翻訳 & AI",
    "Data": "データ",
    "Behavior": "動作設定",
    "Progress": "進捗状況",
    "DeepL request failed — using free Google Translate instead.": "DeepLのリクエストに失敗したため、無料のGoogle翻訳を使用します。",
    "DeepL key isn't set — using free Google Translate instead.": "DeepLキーが設定されていないため、無料のGoogle翻訳を使用します。",
    "System": "システム標準",
    "Light": "ライト",
    "Dark": "ダーク",
    "Appearance mode": "外観モード",
    "Widget scaling": "ウィジェットの縮小・拡大",
    "Table size": "テーブルサイズ",
    "Interface language": "UI言語",
    "Restart the app to apply the language change.": "言語の変更を適用するにはアプリを再起動してください。",
    "The interface language has changed. Restart now to apply it?": "UI言語が変更されました。今すぐ再起動して適用しますか？",
    "TTS provider": "TTSプロバイダー",
    "Google Cloud credentials": "Google Cloudの認証情報",
    "Voice type": "音声タイプ",
    "Voice name (optional)": "音声名 (オプション)",
    "Read Aloud playback": "読み上げ再生設定",
    "Pause between words (s)": "単語間のポーズ (秒)",
    "Repeats per word": "単語ごとの繰り返し回数",
    "Repeats per pair": "ペアごとの繰り返し回数",
    "Promote status while listening": "リスニング中にステータスを自動昇格",
    "Listens to reach {status}": "「{status}」到達に必要な試聴回数",
    "Excel import": "Excelインポート",
    "Placeholder values": "プレースホルダー値",
    "Skip placeholder rows": "プレースホルダー行をスキップ",
    "Skip empty rows": "空行をスキップ",
    "Normalize language pairs": "言語ペアを正規化",
    "How to import": "インポート方法",
    "Save import template…": "インポートテンプレートを保存…",
    "Active provider": "使用中のプロバイダー",
    "API key": "APIキー",
    "API URL": "API URL",
    "Check usage": "使用量を確認",
    "Enable cloud sync": "クラウド同期を有効化",
    "Supabase URL (.env)": "Supabase URL (.env)",
    "Supabase key (.env)": "Supabase キー (.env)",
    "Bin cleanup grace (days)": "ゴミ箱自動削除期間 (日)",
    "Test Connection": "接続テスト",
    "Cloud sync uses your own Supabase project. Create the required tables once, then enter the URL and anon key above.": "クラウド同期にはご自身のSupabaseプロジェクトを使用します。一度必要なテーブルを作成し、上にURLとanonキーを入力してください。",
    "Copy schema SQL": "スキーマSQLをコピー",
    "Open SQL editor ↗": "SQLエディタを開く ↗",
    "Schema SQL copied to the clipboard. Open your Supabase project's SQL editor, paste it, and press Run to create the tables.": "スキーマSQLをクリップボードにコピーしました。SupabaseプロジェクトのSQLエディタを開いて貼り付け、Runを押してテーブルを作成してください。",
    "Server": "サーバー",
    "Connected to your own Supabase server — personal mode, no account needed.\n{host}": "ご自身のSupabaseサーバーに接続中 — パーソナルモード (アカウント不要)\n{host}",
    "Use your own Supabase server (personal)": "自前のSupabaseサーバーを使用 (パーソナル)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, then Test Connection.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "所有しているSupabaseプロジェクトへのパーソナル単一ユーザー同期です。アカウントやサインインは不要で、プロジェクトのanonキーで接続します。プロジェクト内でスキーマSQLを実行し、URLとanonキーを貼り付けて「接続テスト」を行ってください。\n\n注意: URLとキーを知っている人なら誰でもデータを読み取れるため、プロジェクトは非公開にし、キーを共有しないでください。",
    "Disconnect — use the built-in server": "切断 — 内蔵サーバーを使用する",
    "Disconnect server": "サーバーを切断",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. You'll be local-only until you sign into an account.": "所有のSupabaseサーバーとの同期を停止し、再び内蔵サーバーを使用しますか？\n\n単語データはプロジェクトとこのデバイス上に保持されます。アカウントにサインインするまではローカルのみの動作となります。",
    "Disconnected — using the built-in server.": "切断されました — 内蔵サーバーを使用しています。",
    "{host} (personal)": "{host} (パーソナル)",
    "Personal": "パーソナル",
    "your server": "ご使用のサーバー",
    "Account actions": "アカウント操作",
    "Add account…": "アカウントを追加…",
    "Sync this device's data to my account…": "このデバイスのデータをアカウントに同期…",
    # ── Accounts (Sync tab) ──────────────────────────────────────────────
    "Account": "アカウント",
    "Accounts": "アカウント",
    "No accounts yet. Add one to sync your words across devices.": "アカウントがまだありません。追加すると複数のデバイス間で単語を同期できます。",
    "(active)": "(アクティブ)",
    "Sign in": "サインイン",
    "(sign in again)": "(再サインインが必要)",
    "Switch": "切り替え",
    "Remove account": "アカウントを端末から削除",
    "Remove {email} from this device? You can add it again anytime — your words stay in the cloud, and the local copy remains on disk. Your cloud data is not deleted.": "{email} をこのデバイスから削除しますか？いつでも再追加可能です。クラウド上の単語やディスク上のローカルコピーは削除されません。",
    "Removed {email} from this device.": "{email} をこのデバイスから削除しました。",
    "Your data was exported.": "データをエクスポートしました。",
    "Export failed.": "エクスポートに失敗しました。",
    "Delete account": "アカウントを完全に削除",
    "This permanently deletes your account and ALL of your synced words, texts and tags from the cloud. Your local copy is archived to the backups folder. This cannot be undone.\n\nDelete your account?": "これにより、アカウントとクラウド上のすべての同期データ（単語、テキスト、タグ）が永久に削除されます。ローカルコピーはバックアップフォルダにアーカイブされます。この操作は取り消せません。\n\n本当にアカウントを削除しますか？",
    "Account deleted.": "アカウントを削除しました。",
    "Could not delete the account.": "アカウントを削除できませんでした。",
    # ── Sign-in dialog ───────────────────────────────────────────────────
    "Name": "名前",
    "Enter your name.": "名前を入力してください。",
    "Email": "メールアドレス",
    "Password": "パスワード",
    "New password": "新しいパスワード",
    "6-digit code": "6桁のコード",
    "or": "または",
    "Sign in with Google": "Googleでサインイン",
    "Opening your browser to sign in with Google…": "Googleでサインインするためブラウザを開いています…",
    "Forgot password?": "パスワードをお忘れですか？",
    "Resend code": "コードを再送",
    "Confirm your email": "メールアドレスの確認",
    "Verify code": "コードを検証",
    "Use a different email": "別のメールアドレスを使用",
    "Enter your email and password.": "メールアドレスとパスワードを入力してください。",
    "Enter the 6-digit code from the email.": "メールに記載された6桁のコードを入力してください。",
    "Enter the code and a new password.": "コードと新しいパスワードを入力してください。",
    "Enter your email above first.": "まず上のメールアドレスを入力してください。",
    "Enter the reset code we emailed you and a new password.": "送信されたリセットコードと新しいパスワードを入力してください。",
    "Enter the 6-digit code we emailed you.": "送信された6桁のコードを入力してください。",
    "Reset password": "パスワードをリセット",
    "Set new password": "新しいパスワードを設定",
    "Back to sign in": "サインインに戻る",
    "Sign-in failed.": "サインインに失敗しました。",
    "Couldn't send the code.": "コードを送信できませんでした。",
    "Done.": "完了しました。",
    "Failed.": "失敗しました。",
    "Create an account": "アカウントを作成",
    "Create account": "アカウントを作成",
    "I already have an account": "すでにアカウントをお持ちの方",
    "Signed in as {email}": "{email} としてサインイン中",
    # ── Contribute local items dialog ────────────────────────────────────
    "Sync this device's data to your account": "このデバイスのデータをアカウントに同期する",
    "your account": "あなたのアカウント",
    "This device has {words} and {texts} not yet in {account}.": "このデバイスには {account} に未登録の {words} と {texts} があります。",
    "This device has {words} not yet in {account}.": "このデバイスには {account} に未登録の {words} があります。",
    "This device has {texts} not yet in {account}.": "このデバイスには {account} に未登録の {texts} があります。",
    "Select the items to add. They are copied to your account and uploaded to the cloud, so they appear on your other devices. The copy on this device is kept.": "追加する項目を選択してください。アカウントにコピーされてクラウドにアップロードされ、他のデバイスでも利用可能になります（このデバイスのコピーも保持されます）。",
    "Don't ask again for this account": "このアカウントで次回から表示しない",
    "{n} word": "{n} 個の単語",
    "{n} words": "{n} 個の単語",
    "{n} text": "{n} 個のテキスト",
    "{n} texts": "{n} 個のテキスト",
    "Add {n} item": "{n} 件の項目を追加",
    "Add {n} items": "{n} 件の項目を追加",
    # Ukrainian "many" (genitive) plural forms — 5-20, 25-30, etc.
    "words (genitive)": "単語",
    "texts (genitive)": "テキスト",
    "tags (genitive)": "タグ",
    "changes (genitive)": "変更",
    "deletions (genitive)": "削除",
    "{n} words (genitive)": "{n} 個の単語",
    "{n} texts (genitive)": "{n} 個のテキスト",
    "Add {n} items (genitive)": "{n} 件の項目を追加",
    # Contribution result toast (main window)
    "Added {n} item to your account.": "{n} 件の項目をアカウントに追加しました。",
    "Added {n} items to your account.": "{n} 件の項目をアカウントに追加しました。",
    "Added {n} items to your account. (genitive)": "{n} 件の項目をアカウントに追加しました。",
    "{n} couldn't be added.": "{n} 件を追加できませんでした。",
    # ── Sync flow messages (main window) ─────────────────────────────────
    "Your session expired — sign in again (Settings → Sync)": "セッションの期限が切れました — 再度サインインしてください (設定 → 同期)",
    "Sign in to sync (Settings → Sync)": "同期するにはサインインしてください (設定 → 同期)",
    "Sign in again to sync": "同期するために再度サインインしてください",
    "Sign in again to use this account.": "このアカウントを使用するには再度サインインしてください。",
    "Sync incomplete: {reason}": "同期未完了: {reason}",
    "Connect to the internet to add local items to your account.": "ローカル項目をアカウントに追加するにはインターネットに接続してください。",
    "Everything on this device is already in your account.": "このデバイス上のすべてのデータは既にアカウントに同期されています。",
    "Upload local words?": "ローカルの単語をアップロードしますか？",
    "Upload your current local words to this account? They merge with this account's cloud data and sync up.\n\nChoose No to keep this account's existing data and set your local words aside (archived to the backups folder).": "現在のローカル単語をこのアカウントにアップロードしますか？クラウドデータと統合されて同期されます。\n\n「いいえ」を選ぶと既存のクラウドデータを維持し、ローカル単語は別に退避（バックアップフォルダにアーカイブ）されます。",
    # ── Auth status & error messages (auth_manager) ──────────────────────
    "Sign-in failed. Check your email and password.": "サインインに失敗しました。メールアドレスとパスワードを確認してください。",
    "You can keep up to {max} accounts on this device. Remove one to add another.": "このデバイスには最大 {max} 個のアカウントを保存できます。別のアカウントを追加するには1つ削除してください。",
    "Wrong email or password.": "メールアドレスまたはパスワードが正しくありません。",
    "That doesn't look like a valid email address.": "有効なメールアドレスの形式ではありません。",
    "Confirm password": "パスワードの確認",
    "Passwords don't match.": "パスワードが一致しません。",
    "Your email isn't confirmed yet. Enter the 6-digit code we emailed you.": "メールアドレスがまだ確認されていません。送信された6桁のコードを入力してください。",
    "That email is already registered. Try signing in instead.": "そのメールアドレスは既に登録されています。サインインをお試しください。",
    "We emailed you a 6-digit code. Enter it to finish signing up.": "6桁のコードをメールで送信しました。入力して登録を完了してください。",
    "That code didn't work. Check it and try again.": "コードが無効です。確認してやり直してください。",
    "If that account exists, a 6-digit reset code is on its way.": "アカウントが存在する場合、6桁のリセットコードが送信されます。",
    "Confirmation email re-sent.": "確認メールを再送しました。",
    "Too many attempts. Please wait a minute and try again.": "試行回数が多すぎます。しばらく待ってからやり直してください。",
    "Your password is too short — use at least 6 characters.": "パスワードが短すぎます — 6文字以上使用してください。",
    "Sign-ups are disabled on this server.": "このサーバーでは新規登録が無効化されています。",
    "Can't reach the server. Check your internet connection.": "サーバーに接続できません。インターネット接続を確認してください。",
    "Something went wrong.": "問題が発生しました。",
    "Your saved sign-in for this account expired. Sign in again.": "保存されたサインイン情報の期限が切れました。再度サインインしてください。",
    "Cloud sync is not configured yet. Add the Supabase URL and key in Settings → Sync first.": "クラウド同期がまだ設定されていません。まず「設定 → 同期」でSupabase URLとキーを入力してください。",
    "Could not start Google sign-in.": "Google サインインを開始できませんでした。",
    "Google sign-in was cancelled or timed out.": "Google サインインがキャンセルされたかタイムアウトしました。",
    "Google sign-in failed.": "Google サインインに失敗しました。",
    "Google sign-in failed: {error}": "Google サインインに失敗しました: {error}",
    "Could not start the local sign-in helper on port {port} ({error}). Close whatever is using it and retry.": "ポート {port} でローカルサインインヘルパーを起動できませんでした ({error})。使用中のアプリを閉じて再試行してください。",
    "Export my data…": "データをエクスポート…",
    "Delete account…": "アカウントを削除…",
    "Cloud sync is on — your own server ({host})": "クラウド同期ON — 自前サーバー ({host})",
    "Cloud sync is on — signed in as {who}": "クラウド同期ON — {who} としてサインイン中",
    "Cloud sync is off — your words are saved on this device only": "クラウド同期OFF — 単語はこのデバイスにのみ保存されています",
    "(checking…)": "(確認中…)",
    "(can't connect)": "(接続不能)",
    "Turn off cloud sync": "クラウド同期をオフにする",
    "Cloud sync turned off — this device only.": "クラウド同期をオフにしました — このデバイスのみ。",
    "Use this server": "このサーバーを使用する",
    "Connecting…": "接続中…",
    "Testing…": "テスト中…",
    "Applying theme…": "テーマを適用中…",
    "Now syncing with your own server.": "独自のサーバーと同期しています。",
    "Could not connect to this server:\n{error}": "このサーバーに接続できませんでした:\n{error}",
    "Could not connect to this server.": "このサーバーに接続できませんでした。",
    "{detail}\n\nCheck the URL and anon key, and that you've run the schema SQL there. Use these details anyway?": "{detail}\n\nURL、anonキー、およびスキーマSQLが実行されているか確認してください。この設定をそのまま使用しますか？",
    "Enter your server's URL and anon key first, then test.": "まずサーバーのURLとanonキーを入力してからテストしてください。",
    "Enter your server's URL and anon key first.": "まずサーバーのURLとanonキーを入力してください。",
    "Supabase URL": "Supabase URL",
    "Supabase key (anon)": "Supabase キー (anon)",
    "Personal, single-user sync to a Supabase project you own. No account or sign-in — the app connects with the project's anon key. Run the schema SQL in your project, paste its URL and anon key below, test it, then press “Use this server”.\n\nNote: anyone with this URL and key can read the data, so keep the project private and don't share the key.": "所有しているSupabaseプロジェクトへのパーソナル単一ユーザー同期です。アカウントやサインインは不要で、プロジェクトのanonキーで接続します。プロジェクトでスキーマSQLを実行し、URLとanonキーを下に貼り付けてテストし、「このサーバーを使用する」を押してください。\n\n注意: URLとキーを知っている人なら誰でもデータを読み取れるため、プロジェクトは非公開にし、キーを共有しないでください。",
    "Stop syncing with your own Supabase server and use the built-in one again?\n\nYour words stay in your own project and on this device. The server details are remembered so you can switch back anytime. You'll be local-only until you sign into an account.": "自前のSupabaseサーバーとの同期を停止し、再び内蔵サーバーを使用しますか？\n\n単語データはプロジェクトとこのデバイス上に残ります。サーバー詳細は保存されるため、いつでも元に戻せます。アカウントにサインインするまではローカルのみの動作となります。",
    "Start automatically on login (minimized to tray)": "ログイン時に自動起動 (トレイに最小化)",
    "Add Word hotkey (global)": "「単語を追加」ショートカットキー (グローバル)",
    "Data format": "データフォーマット",
    "Columns to export": "エクスポートする列",
    "Sheet name": "シート名",
    "Start row": "開始行",
    "Start column": "開始列",
    "Shade alternate rows": "1行おきに背景色を変更",
    "Auto column width": "列幅の自動調整",
    "Freeze header row": "ヘッダー行を固定",
    "Delimiter": "区切り文字",
    "Delimiter (\\t = tab)": "区切り文字 (\\t = タブ)",
    "Include header lines": "ヘッダー行を含める",
    "Header lines": "ヘッダー行",
    "Page size": "ページサイズ",
    "Font size": "フォントサイズ",
    "Line spacing (pt)": "行間 (pt)",
    "Text alignment": "テキストの配置",
    "Margins L/R/T/B (pt)": "余白 左/右/上/下 (pt)",
    "Automatic widths (fit page)": "自動幅調整 (幅に合わせる)",
    "Columns / width": "列 / 幅",
    "Header background": "ヘッダー背景色",
    "Header text": "ヘッダーテキスト",
    "Row background": "行の背景色",
    "Grid lines": "グリッド線",
    "Background image": "背景画像",
    "Concurrent workers": "並列処理数",
    "Requests per second": "1秒あたりのリクエスト数",
    "Add font…": "フォントを追加…",
    "Page && text": "ページ & テキスト",
    "Columns": "列",
    "Max tokens": "最大トークン数",
    "Temperature": "Temperature (ランダム性)",
    "Prompt template": "プロンプトテンプレート",
    "Definitions": "定義",
    "Generated Texts (from words)": "生成テキスト (単語から)",
    "Generated Texts (by topic)": "生成テキスト (トピック別)",
    "Text Adaptation (to level)": "テキスト調整 (レベル別)",
    "Thinking budget (0 = off, -1 = auto)": "思考バジェット (0 = オフ, -1 = 自動)",

    # ── add_word.py ────────────────────────────────────────────────────────
    "Detect language": "言語を自動検出",
    "Type a word or phrase…": "単語やフレーズを入力…",
    "Translation…": "翻訳…",
    "Pronounce": "発音",
    "Swap word and translation": "単語と翻訳を入れ替える",
    "Translate with DeepL (Enter)": "DeepLで翻訳 (Enter)",
    "Save Word": "単語を保存",
    "Enter a word to translate.": "翻訳する単語を入力してください。",
    "Fill with AI (lemma + best translation)": "AIで自動補完 (原形 + 最適な翻訳)",
    "Enter a word to fill with AI.": "AIで補完する単語を入力してください。",
    "Source equals target — translated to {lang} instead.": "翻訳元と翻訳先が同じです — 代わりに {lang} に翻訳されました。",
    "Both word and translation are required.": "単語と翻訳の両方が必要です。",
    "Please select the source language before saving.": "保存する前に翻訳元の言語を選択してください。",
    "'{word}' already exists in your dictionary.": "「{word}」は既に辞書に存在します。",
    "'{word}' is already in your dictionary.": "「{word}」は既に辞書に存在します。",
    "Already in your dictionary": "既に辞書にあります",
    "Show existing": "既存のデータを表示",
    "The text was truncated to the first 100 words.": "テキストは最初の100単語に切り詰められました。",

    # ── definition.py ──────────────────────────────────────────────────────
    "Generate with AI": "AIで生成",
    "Regenerate with AI": "AIで再生成",
    "Definition 2": "定義 2",
    "No definition yet": "定義がまだありません",
    "Generate one with AI, or write your own with Edit.": "AIで生成するか、「編集」から自分で作成してください。",
    "There is no word to define.": "定義する単語がありません。",
    "Bold": "太字",
    "Italic": "斜体",
    "Heading": "見出し",
    "List": "リスト",
    "API key missing": "APIキーがありません",
    "Set your {ai} API key in Settings → Translation & AI → AI first.": "まず「設定 → 翻訳 & AI → AI」で {ai} のAPIキーを設定してください。",
    "Generating definition…": "定義を生成中…",

    # ── tags.py ────────────────────────────────────────────────────────────
    "Tags — {count} word(s)": "タグ — {count} 件の単語",
    "New tag name…": "新しいタグ名…",
    "Add Tag": "タグを追加",
    "Apply Selected to All": "選択項目をすべてに適用",
    "Remove Selected": "選択項目を削除",
    "(partial)": "(一部)",
    "use(s)": "件使用",
    "Tags marked ✓ apply to all selected words.": (
        "✓ がついたタグは選択中のすべての単語に適用されます。"
    ),
    "◐ (partial) means only some of them have the tag.": (
        "◐ (一部) は、選択中の単語の一部にのみタグがついていることを意味します。"
    ),
    "Select tag(s) in the list first.": "リストからタグを先に選択してください。",

    # ── bin_window.py ──────────────────────────────────────────────────────
    "Bin — Deleted Items": "ゴミ箱 — 削除済みの項目",
    "Delete Permanently": "完全に削除",
    "Cleanup Old Items…": "古い項目をクリーンアップ…",
    "{n} selected": "{n} 件選択中",
    "The bin is empty. Deleted words will appear here.":
        "ゴミ箱は空です。削除された単語はここに表示されます。",
    "The bin is empty. Deleted texts will appear here.":
        "ゴミ箱は空です。削除されたテキストはここに表示されます。",
    "deleted {when}": "{when} に削除済み",
    "(empty)": "(空)",
    "Untitled": "無題",
    "Auto-deletes soon": "まもなく自動削除されます",
    "Auto-deletes in {n} day": "{n} 日後に自動削除",
    "Auto-deletes in {n} days": "{n} 日後に自動削除",
    "Auto-deletes in {n} days (genitive)": "{n} 日後に自動削除",
    "Permanently delete {count} item(s)? This cannot be undone.":
        "{count} 件の項目を完全に削除しますか？この操作は取り消せません。",

    # ── backups.py ─────────────────────────────────────────────────────────
    "Restore an earlier version": "以前のバージョンを復元",
    "Your database is backed up automatically after every change. Pick an earlier version below to restore it.": (
        "変更のたびにデータベースが自動的にバックアップされます。"
        "復元するには以下の以前のバージョンを選択してください。"
    ),
    "No saved versions yet. A backup is made automatically after every change.": (
        "保存されたバージョンはまだありません。"
        "変更のたびにバックアップが自動的に作成されます。"
    ),
    "Restore this version": "このバージョンを復元",
    "Today": "今日",
    "Yesterday": "昨日",
    "Most recent": "最新",
    "Before your last restore": "前回の復元直前",
    "today": "今日",
    "yesterday": "昨日",
    "today {time}": "今日 {time}",
    "yesterday {time}": "昨日 {time}",
    "the version from {date}": "{date} のバージョン",
    "the version from just before your last restore": "前回の復元直前のバージョン",
    "Restore Version": "バージョンを復元",
    "Restore {phrase}?\n\nYour current data is saved first, so you can undo this.": (
        "{phrase} に復元しますか？\n\n現在のデータが先に保存されるため、後からやり直すことも可能です。"
    ),
    "Your database has been restored to {phrase}.\n\nChanged your mind? Restore \"{before}\" to undo.": (
        "データベースが {phrase} に復元されました。\n\n"
        "元に戻したい場合は「{before}」を復元してください。"
    ),
    "Restore Error": "復元エラー",
    "Sorry, that version could not be restored:\n{error}": "申し訳ありません、そのバージョンは復元できませんでした:\n{error}",
    "Remove Version": "バージョンを削除",
    "Remove {phrase}?": "{phrase} を削除しますか？",
    "Remove Error": "削除エラー",
    "Sorry, that version could not be removed:\n{error}": "申し訳ありません、そのバージョンは削除できませんでした:\n{error}",

    # ── generate_text.py ───────────────────────────────────────────────────
    "Generate Text": "テキストを生成",
    "Title…": "タイトル…",
    "Generated text appears here…": "生成されたテキストがここに表示されます…",
    "Save to Texts": "テキストに保存",
    "Save failed": "保存に失敗しました",

    # ── audio_saver.py ─────────────────────────────────────────────────────
    "Save to Audio": "音声として保存",
    "Generate one MP3 file from {count} word/translation pair(s).": (
        "{count} 組の単語/翻訳ペアから 1 つの MP3 ファイルを生成します。"
    ),
    "Generating audio…": "音声を生成中…",
    "Compiling final audio file…": "最終音声ファイルを構築中…",
    "Processed: {word}": "処理済み: {word}",
    "Choose File && Start": "ファイルを選択して開始",
    "Cancelled.": "キャンセルされました。",
    "Audio saved": "音声を保存しました",
    "Audio file saved to:\n{path}": "音声ファイルを保存しました:\n{path}",
    "Audio Error": "音声エラー",
    "Failed to save audio:\n{error}": "音声を保存できませんでした:\n{error}",
    "Cancelling…": "キャンセル中…",

    # ── import_excel.py ────────────────────────────────────────────────────
    "Import from Excel": "Excelからインポート",
    "Row": "行",
    "Word 1": "単語 1",
    "Language 1": "言語 1",
    "Word 2": "単語 2",
    "Language 2": "言語 2",
    "Action": "操作",
    "Details": "詳細",
    "Add": "追加",
    "Update": "更新",
    "Skip": "スキップ",
    "All": "すべて",
    "To add": "追加対象",
    "To update": "更新対象",
    "Skipped": "スキップ済み",
    "Unrecognized": "未認識",
    "Only recognized languages": "認識された言語のみ",
    "Exclude rows whose language wasn't recognized.":
        "言語が認識されなかった行を除外します。",
    "Unrecognized language — will be imported exactly as written.":
        "未認識の言語 — 書かれている通りにインポートされます。",
    "Select all": "すべて選択",
    "Activity log": "アクティビティログ",
    "Export log…": "ログをエクスポート…",

    # ── log_window.py ──────────────────────────────────────────────────────
    "Export…": "エクスポート…",

    # ── add_text.py ────────────────────────────────────────────────────────
    "Add Text": "テキストを追加",
    "Write": "作成",
    "AI Generate": "AI生成",
    "Wikipedia": "Wikipedia",
    "From URL": "URLから",
    "Language:": "言語:",
    "Level:": "レベル:",
    "Topic:": "トピック:",
    "Topic…": "トピック…",
    "Adapt to my level": "自分のレベルに調整",
    "Load entries": "エントリーを読み込む",
    "Add feed…": "フィードを追加…",
    "Ideas:": "アイデア:",
    "Short (~100 words)": "短め (~100語)",
    "Medium (~250 words)": "中くらい (~250語)",
    "Long (~500 words)": "長め (~500語)",
    "Travel": "旅行",
    "Food": "料理・食事",
    "Daily routine": "日常生活",
    "A short story": "ショートストーリー",
    "News": "ニュース",
    "Dialogue at a café": "カフェでの会話",
    "Type or paste your text here, or fetch one with the tabs above…": (
        "ここにテキストを入力または貼り付けるか、上のタブから取得してください…"
    ),

    # ── texts_page.py ──────────────────────────────────────────────────────
    "Newest first": "新しい順",
    "Oldest first": "古い順",
    "Title A–Z": "タイトル順 (A–Z / あーん)",
    "All languages": "すべての言語",
    "All levels": "すべてのレベル",
    "All topics": "すべてのトピック",
    "No matching texts": "該当するテキストがありません",
    "Try a different search or language filter.": "別の検索ワードや言語フィルターを試してください。",
    "New text (write or paste)": "新規テキスト (作成または貼り付け)",
    "Get text from the Internet (AI / Wikipedia / URL / RSS)": (
        "Webからテキストを取得 (AI / Wikipedia / URL / RSS)"
    ),
    "Import .txt file(s)": ".txt ファイルをインポート",
    "Read aloud": "読み上げる",
    "Translate text": "テキストを翻訳",
    "Hide translation": "翻訳を隠す",
    "Focus mode": "集中モード",
    "Exit focus mode": "集中モードを解除",
    "Paper mode: off": "ペーパーモード: オフ",
    "Paper: white (click for sepia)": "ペーパー: ホワイト (クリックでセピア)",
    "Paper: sepia (click to turn off)": "ペーパー: セピア (クリックでオフ)",
    "Save Changes": "変更を保存",
    "Previous text": "前のテキスト",
    "Next text": "次のテキスト",
    "From words: {words}": "対象単語: {words}",
    "Created {date}": "作成日 {date}",
    "Unsaved changes": "未保存の変更",
    "Save changes to '{title}'?": "「{title}」への変更を保存しますか？",
    "Changes saved.": "変更を保存しました。",
    "'{title}' moved to bin.": "「{title}」をゴミ箱に移動しました。",
    "Reader": "リーダー",
    'Pronounce "{word}"': '「{word}」を発音',
    'Add "{word}" to vocabulary': '「{word}」を単語帳に追加',
    "Read from here": "ここから読み上げる",

    # ── word_model.py ──────────────────────────────────────────────────────
    "Source": "ソース",
    "Added manually": "手動で追加",
    "From reader": "リーダーから追加",
    "Created at": "作成日時",

    # ── word_popup.py ──────────────────────────────────────────────────────
    "Add with AI (lemma + best translation)": "AIで追加 (原形 + 最適な翻訳)",
    "Add to vocabulary as is": "そのまま単語帳に追加",
    "Thinking…": "考え中…",
    "'{pair}' is already in your dictionary.": "「{pair}」は既に辞書に存在します。",
    "{label} — {translation} · added": "{label} — {translation} · 追加済み",

    # ── sync_popover.py ────────────────────────────────────────────────────
    "Cloud Sync": "クラウド同期",
    "Last sync": "最終同期",
    "Pending": "保留中",
    "never": "なし",
    "just now": "たった今",
    "{n} min ago": "{n} 分前",
    "Connected": "接続済み",
    "Not connected": "未接続",
    "change": "件の変更",
    "changes": "件の変更",
    "deletion": "件の削除",
    "deletions": "件の削除",
    "everything synced": "すべて同期済み",
    "Initial sync has not completed yet.": "初回同期がまだ完了していません。",
    "Sync Now": "今すぐ同期",
    "Syncing…": "同期中…",
    # Local-only promo state
    "{words} and {texts}": "{words} と {texts}",
    "You've saved {items} here. Sign in to keep them safe and study on all your devices.":
        "ここに {items} が保存されています。サインインすると、データを安全に保護し、すべてのデバイスで学習できます。",

    # ── Local-only sync nudges (main_window.py) ──────────────────────────
    "Local only — sign in to sync your words across devices":
        "ローカルのみ — サインインして複数端末で単語を同期",
    "Sign in to sync across devices": "サインインして端末間で同期",

    # ── welcome_dialog.py ────────────────────────────────────────────────
    "Welcome": "ようこそ",
    "Welcome to {app}": "{app} へようこそ",
    "Sync across your devices": "複数デバイス間で同期",
    "Sign in to keep your vocabulary safe and study it on every device.":
        "サインインして単語帳を安全に保存し、どの端末からでも学習できるようにしましょう。",
    "Automatic cloud backup": "自動クラウドバックアップ",
    "Your words follow you to every computer.":
        "あなたの単語帳はどのパソコンからでもアクセスできます。",
    "Never lose your progress.": "進捗が消える心配はありません。",
    "Study anywhere": "どこでも学習",
    "Pick up right where you left off.":
        "いつでも中断したところから再開できます。",
    "Your data is yours — sign in only to sync it.":
        "データはあなたのものです — 同期したい場合のみサインインしてください。",
    "Sign in / Create account": "サインイン / アカウント作成",
    "Continue on this device": "このデバイスで続ける",

    # ── player.py ──────────────────────────────────────────────────────────
    "Playback settings": "再生設定",
    "Previous word": "前の単語",
    "Next word": "次の単語",
    "Stop playback": "再生停止",
    "Pause between words": "単語間のポーズ",

    # ── reader.py ──────────────────────────────────────────────────────────
    "Nothing to read.": "読み上げるものがありません。",
    "Previous sentence": "前の文",
    "Next sentence": "次の文",
    "Reading speed": "読み上げ速度",
    "Sentence {n} / {total}": "文 {n} / {total}",
    "buffering…": "バッファリング中…",

    # ── stats_page.py ──────────────────────────────────────────────────────
    "Overview": "概要",
    "Learning status": "学習ステータス",
    "Activity": "アクティビティ",
    "Review activity": "復習アクティビティ",
    "Breakdown": "内訳",
    "Total words": "総単語数",
    "Mastered": "習得済み",
    "In progress": "学習中",
    "Languages": "言語",
    "Current streak": "現在の連続日誌",
    "Added this week": "今週追加した数",
    "Definitions written": "作成した定義数",
    "Status distribution": "ステータス分布",
    "Words added over time": "単語数の推移",
    "Activity calendar": "アクティビティカレンダー",
    "Reviews over time": "復習数の推移",
    "Review calendar": "復習カレンダー",
    "Most reviewed words": "最も復習した単語",
    "Top language pairs": "上位の言語ペア",
    "Top tags": "上位のタグ",
    "Reviewed this week": "今週復習した数",
    "Total reviews": "総復習回数",
    "Review streak": "連続復習日数",
    "{pct}% of all words": "全単語の {pct}%",
    "actively learning": "積極学習中",
    "{n} pairs": "{n} 組のペア",
    "best {n}d": "最高 {n} 日",
    "{n} today": "今日 {n} 件",
    "listens logged": "回読み上げ完了",
    "keep it going": "その調子で続けましょう！",
    "Day": "日",
    "Week": "週",
    "Month": "月",

    # ── texts_page.py (additions) ──────────────────────────────────────────
    "Import text files": "テキストファイルをインポート",
    "Text files (*.txt);;All files (*)": "テキストファイル (*.txt);;すべてのファイル (*)",
    "Language of the imported text(s):": "インポートするテキストの言語:",
    "Imported {count} text(s).": "{count} 件のテキストをインポートしました。",
    "Some files could not be imported:": "一部のファイルをインポートできませんでした:",
    "Import failed:\n{error}": "インポートに失敗しました:\n{error}",
    "Failed to save text:\n{error}": "テキストを保存できませんでした:\n{error}",
    "Failed to delete text:\n{error}": "テキストを削除できませんでした:\n{error}",
    "Delete Text": "テキストを削除",
    "Delete '{title}'?": "「{title}」を削除しますか？",
    "Unsupported language: {language}": "未対応の言語: {language}",
    "Unsupported language: {lang}. Pick one from the list.":
        "未対応の言語: {lang}。リストから選択してください。",
    "(empty)": "(空)",
    "unsupported language": "未対応の言語",
    "unreadable text": "読み取り不可能なテキスト",
    "Skipped {n} {noun} ({reasons}).": "{n} 件の {noun} をスキップしました ({reasons})。",
    "Some text couldn't be read aloud — unsupported language "
    "or unreadable characters.":
        "一部のテキストを読み上げられませんでした — 未対応の言語 "
        "または読み取れない文字が含まれています。",
    "Edit text": "テキストを編集",
    "Done editing": "編集完了",
    "Delete text": "テキストを削除",
    "Save Changes": "変更を保存",
    "Paper mode": "ペーパーモード",
    'Click "+" to write or paste a text, the globe to fetch one\nfrom the Internet, or select words in the Words view and\nuse the "Text" action to generate a study text.': (
        "「+」をクリックしてテキストを作成または貼り付けるか、「地球儀」でWebから取得、\n"
        "または単語一覧で単語を選択して「テキスト」操作を行うことで\n"
        "学習用テキストを生成できます。"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "RSS": "RSS",
    'Searches Wikipedia in the selected language. Click a result to load the article; use "Adapt to my level" to simplify it.': (
        "選択した言語でWikipediaを検索します。結果をクリックして記事を読み込み、「自分のレベルに調整」で内容を平易にできます。"
    ),
    'News feeds for the selected language. Load a feed, then double-click an entry to fetch its full text. Add your own feeds with "Add feed…".': (
        "選択した言語のニュースフィードです。フィードを読み込み、記事をダブルクリックして全文を取得します。「フィードを追加…」で独自のフィードを追加可能です。"
    ),
    "Length:": "長さ:",
    "Search Wikipedia (in the selected language)…": "Wikipediaを検索 (選択した言語で)…",
    "Double-click an entry to load its full text.": "記事をダブルクリックして全文を読み込みます。",
    "Working…": "処理中…",
    "Show the {count} result(s) again": "再び {count} 件の検索結果を表示",
    "{ai} API key is not set. Configure it in Settings → Translation & AI → AI.": (
        "{ai} のAPIキーが設定されていません。「設定 → 翻訳 & AI → AI」で設定してください。"
    ),
    "Generating with {ai}…": "{ai} で生成中…",
    'Fetching "{title}"…': "「{title}」を取得中…",
    "(yours)": "(ユーザー作成)",
    "Fetching the full text…": "全文を取得中…",
    "Add feed": "フィードを追加",
    "Feed name:": "フィード名:",
    "Feed URL:": "フィード URL:",
    "Failed to save the text.": "テキストの保存に失敗しました。",
    "Failed to save the text: {error}": "テキストの保存に失敗しました: {error}",
    "'{title}' saved.": "「{title}」を保存しました。",
    "(untitled)": "(無題)",
    "Rewrite the text below for the selected CEFR level with {ai}": (
        "{ai} を使用して以下のテキストを選択したCEFRレベル用に書き直す"
    ),

    # ── log_window.py (additions) ──────────────────────────────────────────
    "Export Log": "ログをエクスポート",
    "Activity Log": "アクティビティログ",
    "Warnings & errors": "警告とエラー",
    "Errors only": "エラーのみ",
    "Find…": "検索…",
    "Open log folder": "ログフォルダを開く",
    "Export diagnostics": "診断情報をエクスポート",
    "Clear the log file? This cannot be undone.":
        "ログファイルをクリアしますか？この操作は取り消せません。",
    "Could not create the diagnostics file.":
        "診断ファイルを作成できませんでした。",
    "Diagnostics saved to:\n{path}": "診断情報を以下に保存しました:\n{path}",
    "**Describe the problem**\n\n\n**Steps to reproduce**\n\n\n---\n":
        "**問題の概要**\n\n\n**再現手順**\n\n\n---\n",
    "\nPlease attach the diagnostics file:\n{path}\n":
        "\n以下の診断ファイルを添付してください:\n{path}\n",
    "Bug report: ": "バグ報告: ",

    # ── titlebar.py ────────────────────────────────────────────────────────
    "Minimize": "最小化",
    "Maximize": "最大化",
    "Restore": "元に戻す",

    # ── mini_player.py ─────────────────────────────────────────────────────
    "Show controls": "コントロールを表示",

    # ── widgets.py ─────────────────────────────────────────────────────────
    "No color": "色なし",
    "None": "なし",
    "Choose Color": "色を選択",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "Cloud sync: idle": "クラウド同期: 待機中",
    "Failed to open table:\n{error}": "表を開けませんでした:\n{error}",
    "Failed to save template:\n{error}": "テンプレートを保存できませんでした:\n{error}",

    # ── settings_dialog.py (additions) ─────────────────────────────────────
    "Show / hide": "表示 / 非表示",
    "Excel options": "Excelオプション",
    "CSV options": "CSVオプション",
    "Header lines are written at the top of the file — import tools like "
    "Anki read them (e.g. #separator:tab, #html:true). "
    "Column names themselves are not written.": (
        "ヘッダー行はファイルの一番上に書き込まれます。Ankiなどのインポートツールが"
        "これらを読み取ります (例: #separator:tab, #html:true)。"
        "列名自体は書き込まれません。"
    ),
    "Copy a .ttf file into the app's fonts folder and use it": (
        "アプリの fonts フォルダに .ttf ファイルをコピーして使用します"
    ),
    "Used only when exporting words to an MP3 file. "
    "The voice itself is configured in the Audio tab.": (
        "単語を MP3 ファイルにエクスポートする時のみ使用されます。"
        "音声自体は「音声」タブで設定します。"
    ),
    "The voice used everywhere words are spoken: in-app Read Aloud "
    "and MP3 export. gTTS is free and needs no setup. Google Cloud TTS "
    "needs a service-account JSON key (Cloud Console → IAM & Admin → "
    "Service Accounts → Keys) and billing enabled on the project — "
    "usage within the free monthly quota is not charged.": (
        "アプリ内の読み上げや MP3 エクスポートなど、音声が使われる全機能で使用されます。"
        "gTTS は無料で設定も不要です。Google Cloud TTS にはサービスアカウントの "
        "JSON キー (Cloud Console → IAM と管理 → サービス アカウント → キー) と"
        "プロジェクトの請求有効化が必要です (毎月の無料枠内での利用は課金されません)。"
    ),
    "Fully listening to a word in Read Aloud promotes it along the "
    "familiarity ladder New → Reviewing → Learning → Mastered. Each "
    "number is the total completed listens needed to reach that level — "
    "passive audio exposure is weak, so high values are normal. Words "
    "you set to Mastered or Ignored yourself are never changed, and a "
    "word is never demoted.": (
        "読み上げで単語を最後まで聴くと、習得段階が「新規 → 復習中 → 学習中 → 習得済み」へと"
        "昇格します。各数値はそのレベルに達するのに必要な累積完了回数です。"
        "聞き流し学習の効果は緩やかであるため、大きめの数値が標準となっています。"
        "自分で「習得済み」や「無視」に設定した単語は変更されず、降格することもありません。"
    ),
    "Save a ready-made .xlsx with the right headers and example rows": (
        "適切なヘッダーとサンプル行が入った作成済みの .xlsx を保存する"
    ),
    "Google Translate (free)": "Google 翻訳 (無料)",
    "Google Translate is free and needs no API key.": (
        "Google 翻訳は無料であり、APIキーは不要です。"
    ),
    "Usage": "使用量",
    "OpenAI (ChatGPT)": "OpenAI (ChatGPT)",
    "Google Gemini": "Google Gemini",
    "Click the field and press the desired key combination — it opens "
    "'Add Word' with the clipboard content from anywhere. "
    "Leave empty to disable.": (
        "フィールドをクリックして希望のショートカットキーを押してください。"
        "どの画面からでもクリップボードの内容を入れて「単語を追加」を開くことができます。"
        "無効にするには空にしてください。"
    ),
    "On Wayland this shortcut is registered with your "
    "desktop and appears in the system keyboard settings.": (
        "Wayland環境では、このショートカットはデスクトップに登録され、"
        "システムのキーボード設定に表示されます。"
    ),
    "Add Word hotkey": "「単語を追加」ショートカット",
    "The global Add-Word hotkey isn't available in this "
    "environment. See Settings ▸ System for options.": (
        "この環境ではグローバル「単語を追加」ショートカットが利用できません。"
        "「設定 ▸ システム」のオプションを参照してください。"
    ),
    "The global Add-Word hotkey isn't available in the "
    "Flatpak sandbox on Wayland.": (
        "WaylandのFlatpakサンドボックス内では、グローバル「単語を追加」ショートカットが利用できません。"
    ),
    "The global Add-Word hotkey isn't supported on this "
    "Wayland desktop yet.": (
        "このWaylandデスクトップ環境では、グローバル「単語を追加」ショートカットがまだサポートされていません。"
    ),
    "To enable it, use any one of these:": "有効にするには、以下のいずれかの方法を試してください:",
    "Log in to an X11 session instead of Wayland":
        "Waylandの代わりにX11セッションでログインする",
    "Use a GNOME session — the global hotkey works there":
        "グローバルショートカットが動作するGNOMEセッションを使用する",
    "Install the AppImage version — it runs outside the sandbox":
        "サンドボックス外で動作するAppImage版をインストールする",
    "Download the AppImage": "AppImageをダウンロード",
    "Add font…": "フォントを追加…",
    "TrueType fonts (*.ttf)": "TrueTypeフォント (*.ttf)",
    "Could not copy the font file:\n{error}": "フォントファイルをコピーできませんでした:\n{error}",
    "Save import template…": "インポートテンプレートを保存…",
    "Excel files (*.xlsx)": "Excelファイル (*.xlsx)",
    "Template saved to:\n{path}\n\n"
    "Fill it with your words (replace the example rows) "
    "and import it via the app menu → Import Excel to Database.": (
        "テンプレートを以下に保存しました:\n{path}\n\n"
        "サンプル行を自分の単語に置き換えて記入し、"
        "アプリメニューの「Excelをデータベースにインポート」からインポートしてください。"
    ),
    "Could not save the template:\n{error}": "テンプレートを保存できませんでした:\n{error}",
    "Background image": "背景画像",
    "Images (*.png *.jpg *.jpeg)": "画像ファイル (*.png *.jpg *.jpeg)",
    "JSON files (*.json)": "JSONファイル (*.json)",
    "Connection successful! ✅": "接続に成功しました！ ✅",
    "Could not connect. Check the URL/key and your internet connection.": (
        "接続できませんでした。URL、キー、およびインターネット接続を確認してください。"
    ),
    "Connection test failed:\n{error}": "接続テストに失敗しました:\n{error}",
    "{count} / {limit} characters this period": "今期間の使用量: {count} / {limit} 文字",
    "{count} characters used": "{count} 文字使用済み",
    "Autostart": "自動起動",
    "Could not update autostart entry:\n{error}": "自動起動のエントリを更新できませんでした:\n{error}",
    "Google Cloud TTS": "Google Cloud TTS",
    "Google Cloud TTS is selected but {problem}\n\n"
    "Audio will fall back to gTTS until this is fixed.": (
        "Google Cloud TTS が選択されていますが、{problem}\n\n"
        "解決されるまで、音声は gTTS にフォールバックします。"
    ),

    # ── Count nouns (for ntr() in backups.py / sync_popover.py) ───────────
    "word": "単語",
    "words": "単語",
    "words (genitive)": "単語",
    "text": "テキスト",
    "texts": "テキスト",
    "texts (genitive)": "テキスト",
    "tag": "タグ",
    "tags": "タグ",

    # ── Common (additions) ─────────────────────────────────────────────────
    "Translate": "翻訳",
    "AI": "AI",
    "Save As": "名前を付けて保存",
    "Save Audio As": "音声を名前を付けて保存",
    "Save PDF As": "PDFを名前を付けて保存",
    "Added": "追加完了",
    "Updated": "更新完了",
    "Failed": "失敗",
    "Checking…": "確認中…",
    "Cleanup": "クリーンアップ",
    "Permanent Delete": "完全削除",
    "No word": "単語なし",
    "Category": "カテゴリ",
    "Bin": "ゴミ箱",

    # ── main_window.py (additions 2) ───────────────────────────────────────
    "All tags": "すべてのタグ",
    "Filter by tag — {tag}": "タグでフィルター — {tag}",
    "(showing first {n})": "(最初の {n} 件を表示中)",
    "Texts: {total}": "テキスト: {total}",
    "Deleted with {n} error(s).": "{n} 件のエラーが発生して削除されました。",
    "Failed to update: {error}": "更新に失敗しました: {error}",
    "Failed to export:\n{error}": "エクスポートに失敗しました:\n{error}",
    "Failed to export PDF:\n{error}": "PDFのエクスポートに失敗しました:\n{error}",
    "Failed to export TXT:\n{error}": "TXTのエクスポートに失敗しました:\n{error}",
    "PDF saved to {path}": "PDFを保存しました: {path}",
    "TXT file saved to {path}": "TXTファイルを保存しました: {path}",
    "Template saved to {path}": "テンプレートを保存しました: {path}",
    "{format} file saved to {path}": "{format} ファイルを保存しました: {path}",
    "Using gTTS instead — {problem}\nFix it in Settings → Read-aloud → Audio.": (
        "代わりに gTTS を使用中 — {problem}\n「設定 → 読み上げ機能 → 音声」で修正してください。"
    ),
    "Failed to load the database:": "データベースの読み込みに失敗しました:",
    "{selected} of {total} selected": "{total} 件中 {selected} 件を選択中",
    # The nav rail's toggle tooltip, which swaps with the rail's own state.
    "Collapse sidebar": "サイドバーを折りたたむ",
    "Expand sidebar": "サイドバーを展開する",

    # ── backups.py (additions) ─────────────────────────────────────────────
    "Saved {when} · {summary}": "保存日時: {when} · {summary}",
    "the version from {date}": "{date} のバージョン",
    "Sorry, that version could not be restored:\n{error}": (
        "申し訳ありません、そのバージョンは復元できませんでした:\n{error}"
    ),
    "Sorry, that version could not be removed:\n{error}": (
        "申し訳ありません、そのバージョンは削除できませんでした:\n{error}"
    ),

    # ── bin_window.py (additions) ──────────────────────────────────────────
    "Restore {count} item(s)?": "{count} 件の項目を復元しますか？",
    "Restored {count} item(s).": "{count} 件の項目を復元しました。",
    "Select item(s) to restore.": "復元する項目を選択してください。",
    "Permanently deleted {count} item(s).": "{count} 件の項目を完全に削除しました。",
    "Select item(s) to delete permanently.": "完全に削除する項目を選択してください。",
    "No items older than {n} days found.": "{n} 日以上前の項目は見つかりませんでした。",
    "Permanently delete items deleted more than {days} days ago?\n\n"
    "This cannot be undone!": (
        "{days} 日以上前に削除された項目を完全に削除しますか？\n\n"
        "この操作は取り消せません！"
    ),
    "Permanently deleted {count} old item(s).": "{count} 件の古い項目を完全に削除しました。",
    "Failed to load deleted items:\n{error}": "削除された項目の読み込みに失敗しました:\n{error}",
    "Failed to count old items:\n{error}": "古い項目のカウントに失敗しました:\n{error}",
    "Failed to cleanup:\n{error}": "クリーンアップに失敗しました:\n{error}",

    # ── import_excel.py (additions) ────────────────────────────────────────
    "Import Excel": "Excelインポート",
    "Expected columns: Language1, Language2, Word1, Word2 — named in a header row, "
    "or headerless with the first four columns in that order. "
    "A ready-made template is available in the app menu → Save Import Template.": (
        "推測される列: Language1, Language2, Word1, Word2（ヘッダー行で命名されているか、"
        "またはヘッダーなしで最初の4列がこの順序になっている必要があります）。"
        "作成済みのテンプレートは「アプリメニュー → インポートテンプレートを保存」から入手できます。"
    ),
    "All ({n})": "すべて ({n})",
    "To add ({n})": "追加対象 ({n})",
    "To update ({n})": "更新対象 ({n})",
    "Skipped ({n})": "スキップ済み ({n})",
    "Unrecognized ({n})": "未認識 ({n})",
    " · {n} with unrecognized language": " · 言語が未認識のもの {n} 件",
    "{total} rows: {add} new · {update} updates · {skip} skipped": (
        "全 {total} 行: 新規 {add} 件 · 更新 {update} 件 · スキップ {skip} 件"
    ),
    "Review the proposed changes, then import the selected rows.": (
        "変更案を確認し、選択した行をインポートしてください。"
    ),
    "Nothing to import — no new or changed entries found.": (
        "インポートするものがありません — 新規または変更されたエントリが見つかりませんでした。"
    ),
    "Analyzing file…": "ファイルを解析中…",
    "Could not read the Excel file — see the activity log.": (
        "Excelファイルを読み込めませんでした — アクティビティログを確認してください。"
    ),
    "Analysis failed — see the activity log.": "解析に失敗しました — アクティビティログを確認してください。",
    "Import failed": "インポート失敗",
    "Import failed — see the activity log.": "インポートに失敗しました — アクティビティログを確認してください。",
    "Importing…": "インポート中…",
    "Importing {count} item(s)…": "{count} 件の項目をインポート中…",
    "Import {count} Item(s)": "{count} 件の項目をインポート",
    "Import finished:": "インポート完了:",
    "Backup failed — see the activity log.": "バックアップに失敗しました — アクティビティログを確認してください。",
    "{n} added": "{n} 件追加",
    "{n} updated": "{n} 件更新",
    "{n} failed": "{n} 件失敗",
    "{n} failed.": "{n} 件失敗しました。",
    "Export Import Log": "インポートログをエクスポート",

    # ── definition.py (additions) ──────────────────────────────────────────
    "Definition — {word}": "定義 — {word}",
    "Failed to save definition:\n{error}": "定義の保存に失敗しました:\n{error}",

    # ── edit_word.py (additions) ───────────────────────────────────────────
    "Edit — {word}": "編集 — {word}",

    # ── add_word.py (additions) ────────────────────────────────────────────
    "Failed to save word:\n{error}": "単語の保存に失敗しました:\n{error}",

    # ── tags.py (additions) ────────────────────────────────────────────────
    "Attach the selected tag(s) to every selected word": (
        "選択したすべての単語に指定したタグを付ける"
    ),
    "Failed to add tag:\n{error}": "タグの追加に失敗しました:\n{error}",
    "Failed to apply tags:\n{error}": "タグの適用に失敗しました:\n{error}",
    "Failed to remove tags:\n{error}": "タグの削除に失敗しました:\n{error}",

    # ── generate_text.py (additions) ───────────────────────────────────────
    "Generates a text with AI using the Language, Level and Topic fields below. "
    "Pick a topic chip or type your own.": (
        "以下の「言語」「レベル」「トピック」のフィールドを使用して、AIがテキストを生成します。"
        "トピックのチップを選択するか、直接入力してください。"
    ),
    "Generating a {language} text from {count} word(s) with {ai}:": (
        "{count} 個の単語から {ai} を使用して {language} のテキストを生成中:"
    ),

    # ── add_text.py (additions) ────────────────────────────────────────────
    "Type or paste a text into the editor below, give it a title, "
    "set the language — then save.": (
        "下のエディタにテキストを入力または貼り付け、タイトルを付け、"
        "言語を設定してから保存してください。"
    ),
    "Extracts the readable article text from any web page. "
    "Pages behind logins or built purely with JavaScript may not work.": (
        "任意のWebページから読み取り可能な記事テキストを抽出します。"
        "ログインが必要なページやJavaScriptのみで構築されたページでは動作しない場合があります。"
    ),

    # ── Strings missed by the initial pass ─────────────────────────────────
    # Toolbar action tooltips
    "View definition (double-click)": "定義を表示 (ダブルクリック)",
    "Read selected words aloud": "選択した単語を読み上げる",
    "Toggle favorite": "お気に入りを切り替え",
    "Add / remove tags": "タグを追加 / 削除",
    "Edit word": "単語を編集",
    "Copy words": "単語をコピー",
    "Generate text from selection": "選択範囲からテキストを生成",

    # File-dialog filters & titles
    "PDF files (*.pdf)": "PDFファイル (*.pdf)",
    "Excel files (*.xlsx *.xls)": "Excelファイル (*.xlsx *.xls)",
    "CSV files (*.csv)": "CSVファイル (*.csv)",
    "Text files (*.txt)": "テキストファイル (*.txt)",
    "MP3 files (*.mp3)": "MP3ファイル (*.mp3)",
    "Open Excel Table": "Excel表を開く",
    "Save Import Template": "インポートテンプレートを保存",

    # Cloud sync status
    "Cloud sync": "クラウド同期",
    "Not connected. Check internet or credentials": "未接続。通信状態または認証情報を確認してください",
    "Syncing with cloud…": "クラウドと同期中…",
    "Sync completed successfully": "同期が正常に完了しました",
    "Sync enabled but not connected. Check settings.": "同期は有効ですが接続されていません。設定を確認してください。",
    "idle": "待機中",
    "syncing": "同期中",
    "success": "成功",
    "error": "エラー",

    # Chart empty states
    "No data yet": "データがまだありません",
    "No activity yet": "アクティビティがまだありません",
    "Not enough activity yet": "十分なアクティビティがまだありません",

    # Settings tabs
    "APIs": "API",
    "Audio (MP3)": "音声 (MP3)",
    "Sync": "同期",

    # Settings — AI/translation provider labels & notes
    "OpenAI API key (.env)": "OpenAI APIキー (.env)",
    "Google API key (.env)": "Google APIキー (.env)",
    'Billed per use — get a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>. Models: gpt-4o-mini, gpt-4o, gpt-4.1-mini… API usage — see <a href="https://platform.openai.com/usage">dashboard</a>.':
        '従量課金制 — キーの取得先: <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a>。モデル: gpt-4o-mini, gpt-4o, gpt-4.1-mini… 使用量確認: <a href="https://platform.openai.com/usage">ダッシュボード</a>。',
    'Free tier available — get a key at <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>. Models: gemini-2.5-flash, gemini-2.5-flash-lite… API usage — see <a href="https://aistudio.google.com/usage">AI Studio</a>.':
        '無料枠あり — キーの取得先: <a href="https://aistudio.google.com/app/apikey">aistudio.google.com/app/apikey</a>。モデル: gemini-2.5-flash, gemini-2.5-flash-lite… 使用量確認: <a href="https://aistudio.google.com/usage">AI Studio</a>。',
    'Get a key at <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>. Use https://api-free.deepl.com/v2/translate for free-tier keys.':
        'キーの取得先: <a href="https://www.deepl.com/pro-api">deepl.com/pro-api</a>。無料アカウントのキーには https://api-free.deepl.com/v2/translate を使用してください。',

    # Excel import help (settings)
    "<ol style='margin:0'><li>Prepare an Excel file with the columns <b>Language1, Language2, Word1, Word2</b> — named like that in a header row (extra columns are ignored), or without headers, with the first four columns in exactly that order.</li><li>Open the app menu → <i>Import Excel to Database…</i> and choose the file.</li><li>Review the proposed rows and click <i>Import</i>.</li></ol>":
        "<ol style='margin:0'><li>ヘッダー行に <b>Language1, Language2, Word1, Word2</b> という名前の列を含めるか（余分な列は無視されます）、ヘッダーなしで最初の4列をまさにその順序で並べたExcelファイルを用意します。</li><li>アプリメニュー → <i>Excelをデータベースにインポート…</i> を開いてファイルを選択します。</li><li>提示された行を確認し、<i>インポート</i> をクリックします。</li></ol>",

    # About dialog
    "created by": "開発者",
    "Version": "バージョン",
    "Build": "ビルド",
    "Your personal vocabulary companion": "あなただけの語彙学習パートナー",
    "Build, study, and remember vocabulary across languages — with cloud sync, AI-assisted definitions, translations, text-to-speech, and flexible export.":
        "クラウド同期、AIサポートによる定義の生成、翻訳、音声読み上げ、柔軟なエクスポート機能を使って、多言語の語彙を構築・学習・記憶しましょう。",
    "Source code": "ソースコード",
    "Your personal vocabulary companion with cloud sync, AI definitions, translations, text-to-speech and export options.":
        "クラウド同期、AI定義生成、翻訳、音声読み上げ、エクスポート機能を備えた、あなただけの語彙学習パートナー。",
    "Licensed under the GNU Affero General Public License v3.0. This attribution must be preserved (AGPL §7).":
        "GNU Affero General Public License v3.0 に基づいてライセンスされています。この著作権表示は保持される必要があります (AGPL §7)。",
    "Found a bug or have an idea?": "バグの報告やアイデアのお持ちの方",
    "Report an issue": "問題を報告する",
    "What would you like to report?": "どのような内容を報告しますか？",
    "A bug or technical problem": "バグや技術的な問題",
    "Creates a report with app diagnostics to send to the developers.":
        "開発者に送信するためのアプリ診断情報を含むレポートを作成します。",
    "Inappropriate AI-generated content": "不適切なAI生成コンテンツ",
    "Report a definition, text, or translation the AI produced.":
        "AIが生成した定義、テキスト、または翻訳について報告します。",
    "Report: inappropriate AI-generated content":
        "報告: 不適切なAI生成コンテンツ",
    "Please describe the AI-generated content you're reporting.\n\n"
    "Where it appeared (definition / generated text / word translation):\n"
    "The word or text in question:\n"
    "Why it is inappropriate:\n\n"
    "---\n":
        "報告するAI生成コンテンツの詳細を記述してください。\n\n"
        "表示された場所 (定義 / 生成テキスト / 単語の翻訳):\n"
        "該当の単語またはテキスト:\n"
        "不適切である理由:\n\n"
        "---\n",
    "To report inappropriate AI-generated content, please email us at {email}.":
        "不適切なAI生成コンテンツを報告するには、{email} までメールでお問い合わせください。",

    # Support dialog
    "Support": "サポート・寄付",
    "Support Lingueez": "Lingueez をサポートする",
    "Lingueez is free and open-source.": "Lingueez は無料のオープンソースソフトウェアです。",
    "If you enjoy Lingueez and find it useful, a one-off contribution helps cover the servers behind optional cloud sync and supports continued development. There's no paywall — every feature stays free either way.":
        "Lingueez を気に入っていただけた場合、単発の寄付はオプションのクラウド同期サーバーの運用費用や今後の開発維持に役立ちます。有料の機能制限はなく、どちらの場合でもすべての機能は無料のままです。",
    "Support Lingueez's development": "Lingueez の開発を支援する",
    "The Stripe option is one-time — no subscription. Payments are handled securely by Stripe or GitHub.":
        "Stripeのオプションは1回限りの決済で、サブスクリプションではありません。お支払いはStripeまたはGitHubにより安全に処理されます。",

    # Updates
    "Updates": "アップデート",
    "Check for updates": "アップデートを確認",
    "You're up to date.": "最新バージョンを使用しています。",
    "Update available": "アップデートが利用可能です",
    "Update available — v{version}": "アップデートが利用可能です — v{version}",
    "Lingueez {version} is available — you have {current}.":
        "Lingueez {version} が利用可能です（現在のバージョン: {current}）。",
    "Skip this version": "このバージョンをスキップ",
    "Later": "後で",
    "Download": "ダウンロード",
    "Check for updates on startup": "起動時にアップデートを確認する",
    "Checks once a day for a newer version and lets you know; "
    "nothing is ever downloaded or installed automatically.":
        "1日に1回最新バージョンを確認してお知らせします。"
        "自動的にダウンロードやインストールが行われることはありません。",

    # Misc units
    "in": "インチ",
    " s": " 秒",

    # Word statuses (stored in English; only the displayed label is localized)
    "New": "新規",
    "To Learn": "未習得",
    "Reviewing": "復習中",
    "Ignored": "無視",
    "Undo": "元に戻す",
    "Restored": "復元しました",
    "Ignore word": "単語を無視",
    "Ignore this word": "この単語を無視",
    "Already ignored.": "すでに無視されています。",
    "{count} word(s) won't come up in practice.": "{count} 件の単語は練習に出てこなくなります。",
    "'{word}' is back in rotation": "「{word}」を練習に戻しました",
    "'{word}' won't come up again": "「{word}」はもう出てきません",
    # "Learning" and "Mastered" are translated above.

    # Table density (settings → Table size)
    "Compact": "コンパクト",
    "Normal": "標準",
    "Comfortable": "ゆったり",
    "Spacious": "広い",

    # Language names (stored in English as the canonical DeepL/gTTS key;
    # only the displayed label is localized — see app/i18n.py lang_label).
    "English": "英語",
    "German": "ドイツ語",
    "Spanish": "スペイン語",
    "Ukrainian": "ウクライナ語",
    "French": "フランス語",
    "Italian": "イタリア語",
    "Portuguese": "ポルトガル語",
    "Russian": "ロシア語",
    "Greek": "ギリシャ語",
    "Arabic": "アラビア語",
    "Bengali": "ベンガル語",
    "Cantonese": "広東語",
    "Hindi": "ヒンディー語",
    "Japanese": "日本語",
    "Korean": "韓国語",
    "Mandarin": "中国語 (標準語)",
    "Polish": "ポーランド語",
    "Turkish": "トルコ語",
    "Vietnamese": "ベトナム語",
    "Afrikaans": "アフリカーンス語",
    "Albanian": "アルバニア語",
    "Amharic": "アムハラ語",
    "Armenian": "アルメニア語",
    "Azerbaijani": "アゼルバイジャン語",
    "Basque": "バスク語",
    "Belarusian": "ベラルーシ語",
    "Bosnian": "ボスニア語",
    "Bulgarian": "ブルガリア語",
    "Catalan": "カタルーニャ語",
    "Cebuano": "セブアノ語",
    "Chichewa": "チェワ語",
    "Chinese": "中国語",
    "Croatian": "クロアチア語",
    "Czech": "チェコ語",
    "Danish": "デンマーク語",
    "Dutch": "オランダ語",
    "Estonian": "エストニア語",
    "Filipino": "フィリピノ語",
    "Finnish": "フィンランド語",
    "Galician": "ガリシア語",
    "Georgian": "ジョージア語",
    "Gujarati": "グジャラート語",
    "Haitian Creole": "ハイチ・クレオール語",
    "Hausa": "ハウサ語",
    "Hawaiian": "ハワイ語",
    "Hebrew": "ヘブライ語",
    "Hmong": "モン語",
    "Hungarian": "ハンガリー語",
    "Icelandic": "アイスランド語",
    "Igbo": "イボ語",
    "Indonesian": "インドネシア語",
    "Irish": "アイルランド語",
    "Javanese": "ジャワ語",
    "Kannada": "カンナダ語",
    "Kazakh": "カザフ語",
    "Khmer": "クメール語",
    "Kinyarwanda": "ルワンダ語",
    "Kyrgyz": "キルギス語",
    "Lao": "ラオ語",
    "Latin": "ラテン語",
    "Latvian": "ラトビア語",
    "Lithuanian": "リトアニア語",
    "Luxembourgish": "ルクセンブルク語",
    "Macedonian": "マケドニア語",
    "Malagasy": "マダガスカル語",
    "Malay": "マレー語",
    "Malayalam": "マラヤーラム語",
    "Maltese": "マルタ語",
    "Maori": "マオリ語",
    "Marathi": "マラーティー語",
    "Mongolian": "モンゴル語",
    "Myanmar (Burmese)": "ミャンマー語 (ビルマ語)",
    "Nepali": "ネパール語",
    "Norwegian": "ノルウェー語",
    "Odia": "オリヤー語",
    "Pashto": "パシュトー語",
    "Persian": "ペルシア語",
    "Punjabi": "パンジャブ語",
    "Romanian": "ルーマニア語",
    "Samoan": "サモア語",
    "Scots Gaelic": "スコットランド・ゲール語",
    "Serbian": "セルビア語",
    "Sesotho": "ソト語",
    "Shona": "ショナ語",
    "Sindhi": "シンド語",
    "Sinhala": "シンハラ語",
    "Slovak": "スロバキア語",
    "Slovenian": "スロベニア語",
    "Somali": "ソマリ語",
    "Sundanese": "スンダ語",
    "Swahili": "スワヒリ語",
    "Swedish": "スウェーデン語",
    "Tajik": "タジク語",
    "Tamil": "タミル語",
    "Tatar": "タタール語",
    "Telugu": "テルグ語",
    "Thai": "タイ語",
    "Turkmen": "トルクメン語",
    "Urdu": "ウルドゥー語",
    "Uyghur": "ウイグル語",
    "Uzbek": "ウズベク語",
    "Welsh": "ウェールズ語",
    "Xhosa": "コサ語",
    "Yiddish": "イディッシュ語",
    "Yoruba": "ヨルバ語",
    "Zulu": "ズールー語",
    # --- Onboarding tour ---
    "Back": "戻る",
    "Next": "次へ",
    "Done": "完了",
    "Show Tour": "ツアーを表示",
    "Step {n} of {total}": "ステップ {n} / {total}",
    "Your library": "ライブラリ",
    "Switch between your Words, Texts and Statistics from this sidebar.":
        "このサイドバーから単語一覧、テキスト一覧、統計を切り替えます。",
    "Add a word": "単語を追加",
    "Find anything": "何でも検索",
    "Search across your words, translations and tags as you type.":
        "入力しながら単語、翻訳、タグを横断検索します。",
    "Add a new word here — its translation can be fetched automatically.":
        "ここから新しい単語を追加します — 翻訳は自動的に取得可能です。",
    "Listen and learn": "聴いて学ぶ",
    "Select words and press Read to hear them aloud. Repeated "
    "listening promotes each word from New to Reviewing, Learning "
    "and finally Mastered.":
        "単語を選択して「読み上げ」を押すと発音を確認できます。"
        "繰り返し聴くことで、単語のステータスが「新規」から「復習中」、「学習中」、そして「習得済み」へと自動的に昇格します。",
    "Generate a text": "テキストを生成",
    "Turn selected words into a short AI-written story — "
    "your vocabulary in context.":
        "選択した単語を元に、AIが短編ストーリーを生成します — "
        "文脈の中で単語を学びましょう。",
    "Your vocabulary stays in sync across devices. Click for "
    "status or to sync right now.":
        "単語帳は複数のデバイス間で同期されます。クリックして "
        "ステータスを確認するか、今すぐ同期します。",
    "Enable cloud sync, switch language, change appearance and "
    "more from Settings.":
        "設定からクラウド同期の有効化、言語の切り替え、外観の変更などが "
        "行えます。",
    # --- Texts tour ---
    "Add texts": "テキストを追加",
    "Write or paste a text, fetch one from the Internet "
    "(AI / Wikipedia / URL / RSS), or import .txt files.":
        "テキストを作成・貼り付けるか、Web (AI / Wikipedia / URL / RSS) から "
        "取得、または .txt ファイルをインポートします。",
    "Your texts": "保存したテキスト",
    "Browse your saved texts and filter them by language, "
    "level or topic.":
        "保存されたテキストを閲覧し、言語、レベル、"
        "トピックでフィルターできます。",
    "Listen to any text aloud — and click a word while reading "
    "to see its translation or add it to your vocabulary.":
        "任意のテキストを朗読で聴くことができます — 読み上げ中に単語をクリックして "
        "翻訳を表示したり、単語帳に追加したりできます。",
    "Show a parallel translation side-by-side; pick the language "
    "with the arrow beside it.":
        "対訳を並べて表示します。横の矢印で "
        "言語を選択できます。",
    "Reading modes": "閲覧モード",
    "Focus mode hides the list, Paper mode changes the "
    "background, and Edit lets you tweak the text.":
        "集中モードはリストを非表示にし、ペーパーモードは背景を変更、"
        "編集機能でテキストを修正できます。",
    # --- Flashcards tour ---
    "Choose your deck": "デッキを選択",
    "Pick what goes into the deck — cards due for review, "
    "words from your current filter, the newest additions, "
    "or a hand-picked selection.":
        "デッキに含めるカードを選択します — 復習期限のカード、"
        "現在のフィルター内の単語、最新の追加項目、"
        "または手動で選択した単語から選べます。",
    "Shape the session": "セッションの設定",
    "Set how many cards to review, shuffle their order, and "
    "have each card pronounced as it appears and flips.":
        "復習するカードの枚数を設定し、順序をシャッフル。カードが表示された時や"
        "めくられた時に自動で発音させることができます。",
    "Preview the deck": "デッキのプレビュー",
    "The exact cards your session will hold. Click a tile to "
    "read or edit its definition, or the speaker to hear the "
    "word.":
        "セッションに含まれるカードの一覧です。タイルをクリックして"
        "定義の確認や編集を行ったり、スピーカーアイコンで単語の発音を"
        "聴くことができます。",
    "Review and grade": "復習と評価",
    "Flip each card and grade how well you knew it — Hard, "
    "Good or Easy. Spaced repetition decides when each card "
    "returns: easy words wait longer, hard ones come back "
    "sooner. Space flips, 1–3 grade.":
        "カードをめくって記憶度を評価します — 「難しい」「普通」「簡単」。"
        "分散学習システムが各カードの再表示時期を決定します。簡単な単語は間隔が長く、"
        "難しい単語はすぐに再表示されます。スペースキーでめくり、1〜3キーで評価します。",
    "Or just listen": "あるいは聴くだけ",
    "Play deck turns the session into audio — cards advance "
    "and flip in sync with the voice. Pause anytime to grade "
    "a card yourself.":
        "「デッキを再生」を使うとセッションが音声モードになります — 音声に合わせて"
        "カードが自動的にめくられて進みます。いつでも一時停止して"
        "自分で評価を付けることができます。",
    # --- Statistics tour ---
    "Your vocabulary at a glance — totals, mastered words, "
    "languages and your current streak.":
        "語彙データの概要 — 総数、習得済み単語数、言語数、連続学習日数など。",
    "See how your vocabulary has grown over time.":
        "時間の経過に伴う語彙の増加グラフを確認できます。",
    "Track how much you've reviewed over time.":
        "時間の経過に伴う復習実績をトラッキングできます。",
    # --- Demo text shown during the Texts tour on an empty library ---
    "Sample: A walk in the city": "サンプル: 街の散歩",
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
        "朝の光は明るく、通りは静かでした。若い女性が古い通りをゆっくりと歩き、"
        "立ち並ぶ高い家々や開店準備を始めたばかりの小さな店を眺めていました。"
        "彼女は立ち止まって焼きたてのパンとコーヒーを買い、広場を横切って公園へと向かいました。"
        "親たちが近くのベンチでおしゃべりをしている間、子供たちは川の近くで遊んでいました。"
        "彼女は大きな木の下に座り、本を開いて読み始めました。"
        "その物語は、何年も会っていない旧友を探して山を越えた旅人の話でした。"
        "しばらくして彼女は顔を上げ、船が川をゆっくりと流れていく様子や、鳥たちが屋根の遥か上を旋回するのを眺めました。"
        "どこか近くでストリートミュージシャンが演奏を始め、穏やかな音色が彼女の思考に寄り添いました。"
        "それは穏やかで幸せな朝であり、彼女が最も好きな種類の朝でした。",
    "Demo": "デモ",
    # --- AI provider error messages ---
    "Invalid OpenAI API key. Check it in Settings → Translation & AI → AI → OpenAI.":
        "無効な OpenAI API キーです。「設定 → 翻訳 & AI → AI → OpenAI」で確認してください。",
    "Your OpenAI account is out of credits. Add credits at "
    "platform.openai.com/account/billing, or switch the AI "
    "provider to Gemini in Settings → Translation & AI → AI.":
        "OpenAI アカウントのクレジットが不足しています。platform.openai.com/account/billing で"
        "クレジットを追加するか、「設定 → 翻訳 & AI → AI」でプロバイダーを Gemini に変更してください。",
    "OpenAI rate limit reached. Wait a moment and try again.":
        "OpenAI のレート制限に達しました。しばらく待ってからやり直してください。",
    "Unknown OpenAI model. Check the model name in Settings → Translation & AI → AI → OpenAI.":
        "不明な OpenAI モデルです。「設定 → 翻訳 & AI → AI → OpenAI」でモデル名を確認してください。",
    "Could not reach OpenAI. Check your internet connection.":
        "OpenAI に接続できませんでした。インターネット接続を確認してください。",
    "Gemini quota exhausted. The free tier resets daily; wait, "
    "or create a new key at aistudio.google.com/app/apikey.":
        "Gemini のクォータを使い果たしました。無料枠は毎日リセットされます。時間をおくか、"
        "aistudio.google.com/app/apikey で新しいキーを作成してください。",
    "Invalid Google API key. Check it in Settings → Translation & AI → AI → Gemini.":
        "無効な Google API キーです。「設定 → 翻訳 & AI → AI → Gemini」で確認してください。",
    "Unknown Gemini model. Check the model name in Settings → Translation & AI → AI → Gemini.":
        "不明な Gemini モデルです。「設定 → 翻訳 & AI → AI → Gemini」でモデル名を確認してください。",
    # --- Words empty state ---
    "Your vocabulary journey starts here": "ここから語彙学習の旅が始まります",
    "Add your first word — its translation can be fetched automatically.":
        "最初の単語を追加してみましょう — 翻訳は自動で取得できます。",
    "Add your first word": "最初の単語を追加",
    "Take the tour": "ツアーを見る",
    "No matching words": "該当する単語がありません",
    "Try a different search or filter.": "別の検索ワードやフィルターをお試しください。",
    "Clear filters": "フィルターをクリア",
    # --- Texts empty state ---
    "Your reading library starts here": "ここから読書ライブラリが始まります",
    "Add a text to read — write or paste your own, fetch one from the "
    "Internet, or import a .txt file.":
        "読むテキストを追加しましょう — 自分で作成・貼り付けたり、"
        "Webから取得、または .txt ファイルをインポートできます。",
    "Add a text": "テキストを追加",
    "Fetch from the Internet": "Webから取得",
    "Import .txt": ".txt をインポート",
    # demo text-list stub titles
    "My first story": "はじめてのストーリー",
    "A news article": "ニュース記事",
    "A short poem": "短い詩",
    "Travel notes": "旅行記",
    # demo text-list stub first sentences (shown as the list snippet)
    "Once upon a time, in a small village by the sea, "
    "there lived a curious young fox.":
        "昔々、海の近くの小さな村に、好奇心旺盛な若いキツネが住んでいました。",
    "Researchers have found a new way to study how "
    "languages change and grow over the centuries.":
        "研究者たちは、何世紀にもわたって言語がどのように変化し成長するかを研究する新しい方法を発見しました。",
    "The wind walks softly through the autumn trees, "
    "carrying old and half-forgotten songs.":
        "風は秋の木々の間を静かに吹き抜け、古く忘れかけられた歌を運んできます。",
    "Day one: we arrived in the city late at night, and the "
    "streets were still full of warm light.":
        "1日目: 私たちは夜遅くに街に到着しましたが、通りはまだ温かい光に満ちていました。",

    # ── Stale-reconnect deletion review ────────────────────────────────────
    "Items deleted on another device": "他のデバイスで削除された項目",
    "While this device was offline, {n} item(s) here were deleted on your "
    "other devices. Keep them in the cloud, or remove them from this device?":
        "このデバイスがオフラインの間、ここにある {n} 件の項目が他のデバイスで削除されました。"
        "クラウド上に保持しますか？それともこのデバイスからも削除しますか？",
    "(untitled)": "(無題)",
    "[Text] {title}": "[テキスト] {title}",
    "Remove from this device": "このデバイスから削除",
    "Decide later": "後で決める",
    "Keep & upload": "保持してアップロード",
    "Not now": "今はしない",

    # ── Offline profiles + upgrade-to-synced-account ───────────────────────
    "Enter a name for the offline profile.": "オフラインプロファイルの名前を入力してください。",
    "You can keep up to {max} offline profiles. Remove one to add another.": "最大 {max} 個のオフラインプロファイルを保持できます。新しいものを追加するには1つ削除してください。",
    "New offline profile": "新しいオフラインプロファイル",
    "Profile name:": "プロファイル名:",
    "Offline profile": "オフラインプロファイル",
    "Rename offline profile": "オフラインプロファイルの名前を変更",
    "Offline profiles": "オフラインプロファイル",
    "Add offline profile…": "オフラインプロファイルを追加…",
    "Profile actions": "プロファイル操作",
    "Separate, device-only libraries with their own database. They never sync and need no sign-in.": "このデバイス専用の独立したライブラリ（独自のデータベース）です。同期は行われず、サインインも不要です。",
    "Default (local)": "デフォルト (ローカル)",
    "Rename": "名前を変更",
    "Delete offline profile": "オフラインプロファイルを削除",
    "Enable cloud sync…": "クラウド同期を有効化…",
    "Could not create the profile.": "プロファイルを作成できませんでした。",
    "Created and switched to “{name}”.": "作成し、「{name}」に切り替えました。",
    "Deleted “{name}”.": "「{name}」を削除しました。",
    "Untitled profile": "無題のプロファイル",
    "Permanently delete the offline profile “{name}”? Its words and texts exist only on this device — there is no cloud copy. The database is archived to the backups folder first, but this cannot be undone in the app.": "オフラインプロファイル「{name}」を永久に削除しますか？そこに含まれる単語やテキストはこのデバイスにのみ存在し、クラウド上にコピーはありません。データベースはまずバックアップフォルダにアーカイブされますが、アプリ内で元に戻すことはできません。",
    "this profile": "このプロファイル",
    "Connect to the internet to merge this profile into your account.": "このプロファイルをアカウントに統合するには、インターネットに接続してください。",
    "Enable cloud sync for this profile": "このプロファイルのクラウド同期を有効にする",
    "Continue": "続行",
    "Upload words": "単語をアップロード",
    "Upload texts": "テキストをアップロード",
    "Upload & sync": "アップロードして同期",
    "Could not upload this profile. Your data is unchanged.": "このプロファイルをアップロードできませんでした。データは変更されていません。",
    "“{name}” is now synced to your account.": "「{name}」がアカウントに同期されました。",
    "Everything in this profile is already in your account.": "このプロファイル内のすべては既にアカウントに存在します。",
    "Sign in or create an account to back up “{name}” and sync it across your devices. This profile's words and texts are uploaded and it becomes your synced account on this device. A copy is archived to the backups folder first.": "サインインまたはアカウントを作成して「{name}」をバックアップし、複数のデバイス間で同期できるようにします。プロファイルの単語とテキストがアップロードされ、このデバイス上の同期アカウントになります。先にバックアップフォルダにコピーがアーカイブされます。",
    "Upload “{name}” to your account": "「{name}」をアカウントにアップロード",
    "Your profile becomes the synced account “{who}” on this device and uploads to the cloud.": "あなたのプロファイルはこのデバイス上で同期アカウント「{who}」となり、クラウドにアップロードされます。",
    "Merge “{name}” into your account": "「{name}」をアカウントに統合",
    "This account already has data on this device. Your profile's words and texts that aren't already there will be added to it — nothing is overwritten. “{name}” is then archived to the backups folder and removed.": "このアカウントには既にこのデバイス上にデータが存在します。まだ存在していないプロファイルの単語やテキストがそこに追加されます（既存データは上書きされません）。その後「{name}」はバックアップフォルダにアーカイブされ、削除されます。",
    "This profile has {items}, saved only on this device. Enable cloud sync to back them up and study on all your devices.": "このプロファイルにはこのデバイスにのみ保存されている {items} があります。クラウド同期を有効にしてバックアップし、すべてのデバイスで学習できるようにしましょう。",
    "Choose the items to add. They're copied into your account and uploaded to the cloud. “{name}” is then archived to the backups folder and removed.": "追加する項目を選択してください。アカウントにコピーされ、クラウドにアップロードされます。その後「{name}」はバックアップフォルダにアーカイブされ、削除されます。",

    # ── Legal / consent ─────────────────────────────────────────────────────
    "I agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "<a href=\"{terms}\">利用規約</a> および <a href=\"{privacy}\">プライバシーポリシー</a> に同意します。",
    "Please accept the Terms of Service and Privacy Policy to continue.":
        "続行するには利用規約とプライバシーポリシーに同意してください。",
    "Updated Terms & Privacy": "利用規約とプライバシーポリシーの改定",
    "We've updated our Terms of Service and Privacy Policy. Please review and accept them to keep using your account.":
        "利用規約とプライバシーポリシーを改定いたしました。アカウントの利用を続けるには、内容を確認して同意してください。",
    "I agree to the updated <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "改定された <a href=\"{terms}\">利用規約</a> および <a href=\"{privacy}\">プライバシーポリシー</a> に同意します。",
    "Sign out": "サインアウト",
    "I agree": "同意する",
    "<a href=\"{privacy}\">Privacy Policy</a> · <a href=\"{terms}\">Terms</a>":
        "<a href=\"{privacy}\">プライバシーポリシー</a> · <a href=\"{terms}\">利用規約</a>",
    "By continuing, you agree to the <a href=\"{terms}\">Terms of Service</a> and <a href=\"{privacy}\">Privacy Policy</a>.":
        "続行することで、<a href=\"{terms}\">利用規約</a> および <a href=\"{privacy}\">プライバシーポリシー</a> に同意したものとみなされます。",
    "Privacy Policy": "プライバシーポリシー",
    "Terms": "利用規約",
    "Website": "ウェブサイト",
    "Contact": "お問い合わせ",

    # ── Flashcards ──────────────────────────────────────────────────────────
    "Flashcards": "単語カード",
    "Practice your vocabulary": "単語を練習する",
    "Due cards": "復習対象のカード",
    "Current filter": "現在のフィルター",
    "Newest": "最新順",
    "Selected words": "選択した単語",
    "Deck size": "デッキのサイズ",
    "Default deck size": "デフォルトのデッキサイズ",
    "Shuffle": "シャッフル",
    "Start session": "セッションを開始",
    "Play deck": "デッキを再生",
    "{n} cards ready to review": "復習可能なカード: {n} 枚",
    "No cards due — great job!": "復習対象のカードはありません — 素晴らしい！",
    "{n} selected words": "選択した単語: {n} 個",
    "No words to practice.": "練習する単語がありません。",
    "End session": "セッションを終了",
    "Listening — pause to review manually":
        "リスニング中 — 手動で復習するには一時停止してください",
    "Show answer": "答えを表示",
    "Hard": "難しい",
    "Good": "普通",
    "Easy": "簡単",
    "Space or click to flip": "スペースキーまたはクリックでめくる",
    "Card {current} of {total}": "カード {current} / {total}",
    "{n} correct": "正解: {n}",
    "Session complete!": "セッション完了！",
    "You listened to {n} of {total} cards.": "{total} 枚中 {n} 枚のカードを試聴しました。",
    "Correct: {n} of {total}": "正解数: {total} 枚中 {n} 枚",
    "New session": "新しいセッション",
    "Practice hard words": "苦手な単語を練習",
    "Hard words": "苦手な単語",
    "Hard words cleared!": "苦手な単語をすべてクリアしました！",
    "Open Flashcards when Read Aloud starts":
        "読み上げ開始時に単語カードを開く",
    "Stop": "停止",
    "Auto-pronounce": "自動発音",
    "Speak each card as it appears and when it flips":
        "カードの表示時とめくった時に自動で発音する",
    "Deck preview": "デッキのプレビュー",
    "{n} cards": "{n} 枚のカード",
    "Due": "要復習",
    "In {n} d": "{n} 日後",
    "{n} d": "{n} 日",
    "{n} mo": "{n} ヶ月",
    "{n} y": "{n} 年",

    # ── Android companion app (android_promo.py) ────────────────────────────
    "Lingueez for Android…": "Android版 Lingueez…",
    "Android app": "Android アプリ",
    "Lingueez on Android": "Android版 Lingueez",
    "Take your vocabulary with you": "語彙ノートをどこへでも持ち歩こう",
    "Preview of Lingueez on a phone": "スマートフォンでの Lingueez プレビュー",
    "Sign in with your Lingueez account and your vocabulary is already there — "
    "nothing to set up, nothing to move across.":
        "Lingueez アカウントでサインインするだけで、単語帳がすぐに利用可能 — "
        "面倒な設定やデータ移行は一切不要です。",
    "Sign in with a free Lingueez account on both and your vocabulary "
    "syncs to the phone — no files to copy across.":
        "両方の端末で無料の Lingueez アカウントにサインインすれば、語彙データが "
        "スマホに自動同期 — ファイルを手動でコピーする必要はありません。",
    "Sign in with a free Lingueez account and your words sync to your phone.":
        "無料の Lingueez アカウントにサインインすると、単語がスマートフォンに同期されます。",
    "Synced both ways": "双方向同期",
    "Words you add on the phone are waiting on the computer, and the "
    "other way round.":
        "スマホで追加した単語はパソコンで確認でき、その逆も同様です。",
    "Listen with the screen off": "画面オフで聴く",
    "Lock-screen controls, so a review keeps running with the phone "
    "in your pocket.":
        "ロック画面で操作できるため、スマホをポケットに入れたまま復習を続けられます。",
    "Save a word from any app": "あらゆるアプリから単語を保存",
    "Share text to Lingueez and it lands in your vocabulary, ready to "
    "fill in later.":
        "テキストを Lingueez に共有すれば単語帳に自動登録され、後からいつでも詳細を入力できます。",
    "Point your phone's camera at the code":
        "スマホのカメラをコードに向けてください",
    "Get it on Google Play": "Google Play で手に入れよう",
    "Copy link": "リンクをコピー",
    "Link copied": "リンクをコピーしました",
    "Lingueez is now on Android": "Lingueez が Android に登場",
    "Sign in with your Lingueez account — your vocabulary is already there.":
        "Lingueez アカウントでサインインすれば、すぐにあなたの単語帳が使えます。",
    "Dismiss": "閉じる",
    "Use your Lingueez account seamlessly across desktop and Android devices.":
        "PCとAndroid端末で Lingueez アカウントをシームレスに活用できます。",
    "Get the app…": "アプリを入手…",
    # ── Quiz (quiz_page.py) ───────────────────────────────────────────
    "Quiz": "クイズ",
    "Quiz (recall practice)": "クイズ（思い出す練習）",
    "Recall your words, one question at a time": "1問ずつ、覚えた単語を思い出しましょう",
    "Questions": "問題数",
    "Answer with": "回答方法",
    "Choices": "選択",
    "Typing": "入力",
    "Ask": "出題",
    "Term": "単語",
    "Mixed": "混合",
    "Auto-advance": "自動で次へ",
    "Move on by itself after a correct answer": "正解したら自動で次に進む",
    "Speak the question, then the answer once it is revealed":
        "問題を読み上げ、答えが表示されたら答えも読み上げる",
    "Start quiz": "クイズを開始",
    "questions ready": "問が準備できました",
    "Nothing to quiz": "出題できる単語がありません",
    "No words match this deck.": "この一組に該当する単語はありません。",
    "A quiz needs at least two words — the ones you are not being asked about are "
    "where the wrong answers come from.":
        "クイズには少なくとも2つの単語が必要です。出題されない単語が、誤答の選択肢になります。",
    "Not enough words": "単語が足りません",
    "Add a few more words, or widen the deck.": "単語をいくつか追加するか、対象を広げてください。",
    "Question {n} of {total}": "問題 {n} / {total}",
    "Missed words": "間違えた単語",
    "End quiz": "クイズを終了",
    "Answer in {language}": "{language}で回答",
    "Type the answer": "答えを入力",
    "Check": "確認",
    "Click to continue": "クリックして続ける",
    "See results": "結果を見る",
    "Almost — it is \"{answer}\"": "惜しい — 正解は「{answer}」",
    "It is \"{answer}\"": "正解は「{answer}」",
    "Now {status}": "現在 {status}",
    "Correct": "正解",
    "Missed": "不正解",
    "Worth another look": "もう一度見ておきたい単語",
    "Again": "もう一度",
    "Missed words cleared!": "間違えた単語を克服しました！",
    "Perfect run": "全問正解",
    "Quiz complete": "クイズ終了",
    "Practice missed": "間違えた単語を練習",
    "Default number of questions": "既定の問題数",
    "Move on after a correct answer": "正解したら次に進む",
    # ── Quiz tour (tour.py) ───────────────────────────────────────────
    "Pick what you'll be asked": "何を出題するか選ぶ",
    "The same deck choices as Flashcards — words due for review, your current filter, "
    "the newest ones, or a hand-picked selection — and how many questions to ask.":
        "カードと同じ出題範囲 — 復習時期の単語、現在の絞り込み、新しい順、手動で選んだもの — と、出題数を決めます。",
    "Choices or typing": "選択か入力か",
    "Choices offers four options to pick from; Typing asks you to write the answer, "
    "which is harder but the better test. Typing forgives accents and small typos. Ask "
    "decides which side you see — the term, its translation, or a mix.":
        "「選択」は4つの選択肢から選びます。「入力」は答えを書くので難しくなりますが、力試しには向いています。入力ではアクセント記号や軽い打ち間違いは許容されます。「出題」は表示される側を決めます "
        "— 単語、訳語、またはその混合です。",
    "Start, and it counts": "始めましょう — 記録されます",
    "The bar shows what the deck is made of by status. Every answer feeds the same "
    "spaced-repetition schedule as Flashcards, so a word you recall here comes back "
    "later — and one you miss comes back sooner.":
        "バーは出題範囲の状態別の内訳です。どの回答もカードと同じ間隔反復の予定に反映されるので、思い出せた単語は次に出るまで長くなり、間違えた単語は早く戻ってきます。",
}

# Date names, read by app.i18n. Months use standard Japanese calendar names.
# Weekdays start on Monday (datetime.weekday(): 0 = Monday).
MONTHS = ["1月", "2月", "3月", "4月", "5月", "6月",
          "7月", "8月", "9月", "10月", "11月", "12月"]
MONTHS_ABBR = ["1月", "2月", "3月", "4月", "5月", "6月",
               "7月", "8月", "9月", "10月", "11月", "12月"]
WEEKDAYS = ["月曜日", "火曜日", "水曜日", "木曜日",
            "金曜日", "土曜日", "日曜日"]
WEEKDAYS_ABBR = ["月", "火", "水", "木", "金", "土", "日"]