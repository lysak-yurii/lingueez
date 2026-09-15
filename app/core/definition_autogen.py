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

"""When Quick Save generates a definition for the word it just saved.

Pure policy over the settings dict (Qt-free, testable): the dialog and the main
window load and save the settings around these calls.
"""
from __future__ import annotations

from app.config import get_bool, get_int
from app.core import ai

ENABLED_KEY = "addword_generate_definition"
FAILURES_KEY = "addword_definition_failures"
MAX_FAILURES = 3


def enabled(settings) -> bool:
    """On, and able to run: a switched-on setting with no API key is off."""
    return get_bool(settings, ENABLED_KEY) and ai.has_api_key()


def disable_if_unavailable(settings) -> bool:
    """Switch the setting off when there is no API key; returns whether it changed."""
    if get_bool(settings, ENABLED_KEY) and not ai.has_api_key():
        set_enabled(settings, False)
        return True
    return False


def set_enabled(settings, on: bool) -> None:
    """Set the switch by hand, which also forgives past failures."""
    settings[ENABLED_KEY] = str(bool(on))
    settings[FAILURES_KEY] = "0"


def record_outcome(settings, ok: bool) -> str:
    """Count one background generation: ``"ok"``, ``"failed"`` or ``"turned_off"``."""
    if ok:
        settings[FAILURES_KEY] = "0"
        return "ok"
    failures = get_int(settings, FAILURES_KEY) + 1
    if failures >= MAX_FAILURES:
        set_enabled(settings, False)
        return "turned_off"
    settings[FAILURES_KEY] = str(failures)
    return "failed"
