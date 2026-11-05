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

"""Messages from the Lingueez team (the built-in project's ``app_messages``).

They are always read from the built-in project, also when sync goes to a
personal server, so every install hears from the team. A request carries only
the platform, the version and the audience, plus the session when signed in
there. The last answer and the messages the user closed are kept on disk, so
they still show offline and a closed one stays closed.
"""

import json
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from urllib.parse import urlparse

CACHE_FILE = "announcements.json"
PLATFORM = "desktop"
SEVERITIES = ("info", "success", "warning", "critical")


@dataclass(frozen=True)
class Announcement:
    id: str
    severity: str
    dialog: bool
    body: Dict[str, str]
    title: Dict[str, str] = field(default_factory=dict)
    action_label: Dict[str, str] = field(default_factory=dict)
    action_url: Optional[str] = None
    dismissible: bool = True
    priority: int = 0

    @classmethod
    def from_row(cls, row: dict) -> "Announcement":
        def texts(value):
            if not isinstance(value, dict):
                return {}
            return {str(k): v.strip() for k, v in value.items()
                    if isinstance(v, str) and v.strip()}
        severity = row.get("severity")
        return cls(
            id=str(row.get("id")),
            severity=severity if severity in SEVERITIES else "info",
            dialog=row.get("placement") == "dialog",
            body=texts(row.get("body")),
            title=texts(row.get("title")),
            action_label=texts(row.get("action_label")),
            action_url=row.get("action_url"),
            dismissible=row.get("dismissible") is not False,
            priority=int(row.get("priority") or 0),
        )

    def to_row(self) -> dict:
        return {
            "id": self.id, "severity": self.severity,
            "placement": "dialog" if self.dialog else "banner",
            "body": self.body, "title": self.title, "action_label": self.action_label,
            "action_url": self.action_url, "dismissible": self.dismissible,
            "priority": self.priority,
        }

    @property
    def link(self) -> Optional[str]:
        """The link to open, or None when there is none or it isn't https."""
        url = self.action_url or ""
        parsed = urlparse(url)
        return url if parsed.scheme == "https" and parsed.netloc else None


def localized(texts: Dict[str, str], lang: str) -> Optional[str]:
    """*texts* in *lang* ("pt_BR"), else its language ("pt"), else English,
    else whatever there is; None when empty."""
    if not texts:
        return None
    tag = (lang or "en").replace("_", "-")
    return (texts.get(tag) or texts.get(lang) or texts.get(tag.split("-")[0])
            or texts.get("en") or next(iter(texts.values())))


def channel() -> str:
    """How this copy was installed (msix, snap, …), for messages aimed at one."""
    from app.system.package_env import channel as install_channel
    return install_channel()


def audience() -> str:
    from app.core.auth_manager import get_auth_manager
    from app.core.supabase_client import is_custom_server
    if is_custom_server():
        return "custom_server"
    auth = get_auth_manager()
    if auth.is_local_active():
        return "local_profile"
    return "signed_in" if auth.is_logged_in() else "signed_out"


_built_in_client = None


def _client():
    """The built-in project's client: the shared one (it carries the session)
    unless sync goes to a personal server, then a separate anonymous one."""
    global _built_in_client
    from app.core.supabase_client import (DEFAULT_SUPABASE_KEY, DEFAULT_SUPABASE_URL,
                                          _client_options, get_supabase, is_custom_server)
    if not is_custom_server():
        return get_supabase().client
    if _built_in_client is None:
        from supabase import create_client
        _built_in_client = create_client(DEFAULT_SUPABASE_URL, DEFAULT_SUPABASE_KEY,
                                         options=_client_options())
    return _built_in_client


def fetch(version: str, client=None) -> List[Announcement]:
    """The current messages for this app; raises when the server can't be reached."""
    client = client or _client()
    if client is None:
        raise ConnectionError("no Supabase client")
    rows = client.rpc("active_messages", {
        "p_platform": PLATFORM, "p_version": version, "p_audience": audience(),
        "p_channel": channel(),
    }).execute().data or []
    return [m for m in (Announcement.from_row(r) for r in rows) if m.body]


class Store:
    """The cached messages and the ids the user closed for good."""

    def __init__(self, path: str = CACHE_FILE):
        self.path = path
        self.messages: List[Announcement] = []
        self.dismissed: set = set()
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            self.messages = [Announcement.from_row(r) for r in data.get("messages", [])]
            self.dismissed = set(data.get("dismissed", []))
        except (OSError, ValueError, TypeError, AttributeError):
            pass

    def _save(self) -> None:
        try:
            with open(self.path, "w", encoding="utf-8") as fh:
                json.dump({"messages": [m.to_row() for m in self.messages],
                           "dismissed": sorted(self.dismissed)}, fh)
        except OSError as exc:
            logging.warning(f"Could not cache announcements: {exc}")

    def update(self, messages: List[Announcement]) -> None:
        """Take the server's answer. Closings of messages that are gone are
        forgotten, so the list can't grow forever."""
        self.messages = list(messages)
        self.dismissed &= {m.id for m in messages}
        self._save()

    def dismiss(self, message: Announcement) -> None:
        if message.dismissible:
            self.dismissed.add(message.id)
            self._save()

    def banners(self) -> List[Announcement]:
        return [m for m in self.messages if not m.dialog and m.id not in self.dismissed]

    def dialogs(self) -> List[Announcement]:
        return [m for m in self.messages if m.dialog and m.id not in self.dismissed]
