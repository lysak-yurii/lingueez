# Lingueez — a desktop app for studying vocabulary across languages.
# Copyright (C) 2024-2026 Yurii Lysak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Additional terms under AGPL-3.0 section 7 apply to this program; see the
# NOTICE file distributed with this source for details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Standalone global-hotkey listener process.

pynput's X11 record-extension thread is known to segfault occasionally;
running it in this separate process keeps the main app alive. Prints a
line to stdout whenever the hotkey fires; the app restarts the agent if
it dies.

Usage: hotkey_agent.py [<pynput-hotkey>]   e.g. '<ctrl>+<shift>+v'
"""
import sys

DEFAULT_HOTKEY = '<ctrl>+<shift>+v'


def main():
    from pynput import keyboard

    hotkey = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_HOTKEY

    def on_hotkey():
        print("HOTKEY", flush=True)

    try:
        hotkeys = keyboard.GlobalHotKeys({hotkey: on_hotkey})
    except ValueError:
        # invalid combo from settings — stay alive on the default instead
        # of dying and being restarted in a loop
        print(f"Invalid hotkey {hotkey!r}, using {DEFAULT_HOTKEY}",
              file=sys.stderr, flush=True)
        hotkeys = keyboard.GlobalHotKeys({DEFAULT_HOTKEY: on_hotkey})

    with hotkeys as listener:
        listener.join()


if __name__ == "__main__":
    sys.exit(main())
