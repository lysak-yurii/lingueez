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


def word_length_error(maximum: int, length: int) -> LimitError:
    return LimitError(tr("Word too long"),
                      tr("A word can contain up to {max} characters "
                         "(this word: {n}).").format(max=fmt_int(maximum), n=length))


def definition_length_error(maximum: int, length: int) -> LimitError:
    return LimitError(tr("Definition too long"),
                      tr("A definition can contain up to {max} characters "
                         "(this definition: {n}).").format(max=fmt_int(maximum), n=length))


WORD_FIELDS = ("Word1", "Word2")
DEFINITION_FIELDS = ("Definition", "Definition2")


def check_word_fields(word_data: dict, stored: Optional[dict] = None) -> None:
    """Raise LimitError for a word or definition longer than the account allows.
    With *stored*, values equal to it pass, as they do on the server."""
    lim = current()
    for fields, cap, error in ((WORD_FIELDS, lim.word_length, word_length_error),
                               (DEFINITION_FIELDS, lim.definition_length,
                                definition_length_error)):
        if cap is None:
            continue
        for field in fields:
            value = word_data.get(field)
            if (isinstance(value, str) and len(value) > cap
                    and (stored is None or value != stored.get(field))):
                raise error(cap, len(value))


def shorten(text: Optional[str], maximum: Optional[int]) -> Optional[str]:
    """*text* cut to *maximum* characters, at the last paragraph or sentence end
    when one falls in the last third, else at a word break."""
    if not isinstance(text, str) or maximum is None or len(text) <= maximum:
        return text
    cut = text[:maximum]
    floor = maximum * 2 // 3
    for marks in (("\n",), (". ", "! ", "? ", "。", "！", "？")):
        end = max(cut.rfind(m) + len(m.rstrip()) for m in marks)
        if end >= floor:
            return cut[:end].rstrip()
    space = cut.rfind(" ")
    return (cut[:space] if space >= floor else cut).rstrip()


def fit_definition(text: Optional[str]) -> Optional[str]:
    return shorten(text, current().definition_length)


def fit_text(title: str, text: str) -> tuple:
    return shorten(title, TITLE_MAX), shorten(text, current().text_length)


def fit_word(word_data: dict) -> dict:
    """*word_data* with its words and definitions shortened to the limits."""
    lim = current()
    fitted = dict(word_data)
    for fields, cap in ((WORD_FIELDS, lim.word_length),
                        (DEFINITION_FIELDS, lim.definition_length)):
        for field in fields:
            if field in fitted:
                fitted[field] = shorten(fitted[field], cap)
    return fitted


# Fixed caps the server applies to every account (see supabase_schema.py).
TITLE_MAX = 200
WORD_LIST_MAX = 10000
TAG_NAME_MAX = 50

# Server rejection code -> the cloud columns it is about and where their cap comes from:
# an AccountLimits attribute (the server also sends it as the error's detail) or fixed caps.
_REJECTIONS = {
    "word_too_long": (("word1", "word2"), "word_length"),
    "definition_too_long": (("definition", "definition2"), "definition_length"),
    "text_too_long": (("text",), "text_length"),
    "text_field_too_long": {"title": TITLE_MAX, "words": WORD_LIST_MAX},
    "tags_length_check": {"tag_name": TAG_NAME_MAX},
}


def cap_rejected(payload: dict, exc: Exception) -> Optional[dict]:
    """The cloud *payload* cut to fit, when *exc* is the server refusing it for a
    field's length; None when it is any other error or nothing could be cut."""
    hint = getattr(exc, "hint", None)
    code = hint if hint in _REJECTIONS else next(
        (c for c in _REJECTIONS if c in str(exc)), None)
    if code is None:
        return None
    rule = _REJECTIONS[code]
    if isinstance(rule, dict):
        caps = rule
    else:
        fields, attr = rule
        detail = str(getattr(exc, "details", None) or "").replace(",", "")
        cap = int(detail) if detail.isdigit() else getattr(current(), attr)
        if cap is None:
            return None
        caps = dict.fromkeys(fields, cap)
    capped, changed = dict(payload), False
    for field, cap in caps.items():
        value = capped.get(field)
        if isinstance(value, str) and len(value) > cap:
            capped[field] = value[:cap]
            changed = True
    return capped if changed else None
