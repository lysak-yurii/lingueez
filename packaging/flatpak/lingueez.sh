#!/bin/sh
# Flatpak entry point. The app's source tree is installed read-only under
# /app/lingueez; main.py detects the read-only install and runs from a writable
# per-user data dir (see _setup_paths in main.py).
exec python3 /app/lingueez/main.py "$@"
