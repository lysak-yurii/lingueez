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
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Account limits as the server resolves them for the signed-in account.

The numbers live on the server (plans plus per-account overrides, read through
the ``my_limits()`` function), so they can change without a release. They are
cached on disk per account so the checks still hold offline; until the server
has answered once nothing is checked up front and the server's own triggers
decide. A server without the limits schema (a personal one) reports none.
"""

import json
import logging
from dataclasses import asdict, dataclass
from typing import Optional

from app.core.errors import LimitError
from app.i18n import fmt_int, tr

CACHE_FILE = "account_limits.json"

# PostgREST's "no such function": a server without the limits schema.
_MISSING_FUNCTION = "PGRST202"


@dataclass(frozen=True)
class AccountLimits:
    """None means no limit."""
    words: Optional[int] = None
    import_batch: Optional[int] = None
    word_length: Optional[int] = None
    definition_length: Optional[int] = None
    tags: Optional[int] = None
    tags_per_word: Optional[int] = None
    texts: Optional[int] = None
    text_length: Optional[int] = None

    @classmethod
    def from_row(cls, row: dict) -> "AccountLimits":
        def num(key):
            value = row.get(key)
            return int(value) if value is not None else None
        return cls(
            words=num("words_max"),
            import_batch=num("import_batch_max"),
            word_length=num("word_length_max"),
            definition_length=num("definition_length_max"),
            tags=num("tags_max"),
            tags_per_word=num("tags_per_word_max"),
            texts=num("texts_max"),
            text_length=num("text_length_max"),
        )


NONE = AccountLimits()

_owner: Optional[str] = None
_limits: AccountLimits = NONE


def active() -> bool:
    from app.core.auth_manager import cloud_backend_active
    return cloud_backend_active()


def _current_owner() -> Optional[str]:
    from app.core.auth_manager import get_auth_manager
    from app.core.supabase_client import custom_server_host, is_custom_server
    auth = get_auth_manager()
    if auth.is_local_active():
        return None
    if auth.is_logged_in() and auth.current_user_id():
        return auth.current_user_id()
    if is_custom_server():
        return f"custom:{custom_server_host() or 'server'}"
    return None


def _load(owner: str) -> AccountLimits:
    try:
        with open(CACHE_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
        if data.get("owner") == owner:
            return AccountLimits(**data.get("limits", {}))
    except (OSError, ValueError, TypeError):
        pass
    return NONE


def _save(owner: str, limits: AccountLimits) -> None:
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as fh:
            json.dump({"owner": owner, "limits": asdict(limits)}, fh)
    except OSError as exc:
        logging.warning(f"Could not cache account limits: {exc}")


def current() -> AccountLimits:
    """The limits of whoever the app is writing for now; none when local-only."""
    global _owner, _limits
    if not active():
        return NONE
    owner = _current_owner()
    if owner is None:
        return NONE
    if owner != _owner:
        _owner, _limits = owner, _load(owner)
    return _limits


def refresh(client) -> None:
    """Ask the server for the current account's limits; keeps the known ones when
    it can't be reached. *client* is the supabase-py client."""
    global _owner, _limits
    owner = _current_owner()
    if owner is None or client is None:
        return
    try:
        rows = client.rpc("my_limits").execute().data or []
        limits = AccountLimits.from_row(rows[0]) if rows else NONE
    except Exception as exc:
        if getattr(exc, "code", None) == _MISSING_FUNCTION or _MISSING_FUNCTION in str(exc):
            limits = NONE
        else:
            logging.info(f"Account limits not refreshed: {exc}")
            return
    _owner, _limits = owner, limits
    _save(owner, limits)


def word_limit_error(maximum: int) -> LimitError:
    return LimitError(tr("Dictionary limit reached"),
                      tr("A dictionary can contain up to {max} words.")
                      .format(max=fmt_int(maximum)))


def import_limit_error(maximum: int, selected: int) -> LimitError:
    return LimitError(tr("Import limit exceeded"),
                      tr("A single import can add up to {max} new words "
                         "(selected: {n}).").format(max=fmt_int(maximum), n=selected))


def import_room_error(maximum: int, current_count: int, selected: int) -> LimitError:
    return LimitError(tr("Dictionary limit reached"),
                      tr("A dictionary can contain up to {max} words "
                         "(in your dictionary: {current}, selected for import: {n}).")
                      .format(max=fmt_int(maximum), current=current_count, n=selected))


def text_count_error(maximum: int) -> LimitError:
    return LimitError(tr("Text limit reached"),
                      tr("Up to {max} texts can be saved.").format(max=fmt_int(maximum)))


def text_length_error(maximum: int, length: int) -> LimitError:
    return LimitError(tr("Text too long"),
                      tr("A text can contain up to {max} characters "
                         "(this text: {n}).").format(max=fmt_int(maximum), n=length))
