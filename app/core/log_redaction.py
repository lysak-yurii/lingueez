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

"""Scrub PII / secrets from log records before they are persisted.

Applied to both the rotating file handler (so secrets never reach app.log and
therefore never reach an exported diagnostics bundle) and the live in-app log
viewer. Kept deliberately conservative — emails, JWTs, and obvious key=value
secrets only — so ordinary log lines are left untouched.
"""
import logging
import re

_PATTERNS = (
    (re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+'), '<email>'),
    (re.compile(r'eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'), '<jwt>'),
    (re.compile(r'(?i)\b(access[_-]?token|refresh[_-]?token|api[_-]?key|'
                r'password|secret|authorization|bearer)\b'
                r'(["\':=\s]+)\S+'), r'\1\2<redacted>'),
)


def redact(text):
    """Return *text* with emails / tokens / secrets masked."""
    for pattern, repl in _PATTERNS:
        text = pattern.sub(repl, text)
    return text


class RedactionFilter(logging.Filter):
    """Masks emails / tokens / secrets in a log record, in place."""

    def filter(self, record):
        try:
            record.msg = redact(record.getMessage())
            record.args = ()
        except Exception:
            pass
        return True
