#!/usr/bin/env bash
# Launch the Lingueez app with its virtual environment.
# The venv lives in ~/.venvs/dictionary-upgraded because this drive (exFAT)
# does not support the symlinks a venv needs.
set -e
cd "$(dirname "$0")"

VENV="$HOME/.venvs/dictionary-upgraded"
if [ ! -x "$VENV/bin/python" ]; then
    echo "Creating virtual environment at $VENV ..."
    python3 -m venv "$VENV"
    "$VENV/bin/pip" install --upgrade pip
    "$VENV/bin/pip" install -r requirements.txt
fi

exec "$VENV/bin/python" main.py "$@"
