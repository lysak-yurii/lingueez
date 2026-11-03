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

"""Account limits, mirrored from the server so the UI can explain them first."""

from app.core.errors import LimitError
from app.i18n import tr

WORD_LIMIT = 10_000
IMPORT_LIMIT = 500
TEXT_LIMIT = 100
TEXT_LENGTH_LIMIT = 50_000


def active() -> bool:
    from app.core.auth_manager import cloud_backend_active
    from app.core.supabase_client import is_custom_server
    return cloud_backend_active() and not is_custom_server()


def word_limit_error() -> LimitError:
    return LimitError(tr("Dictionary limit reached"),
                      tr("A dictionary can contain up to 10,000 words."))


def import_limit_error(selected: int) -> LimitError:
    return LimitError(tr("Import limit exceeded"),
                      tr("A single import can add up to 500 new words "
                         "(selected: {n}).").format(n=selected))


def import_room_error(current: int, selected: int) -> LimitError:
    return LimitError(tr("Dictionary limit reached"),
                      tr("A dictionary can contain up to 10,000 words "
                         "(in your dictionary: {current}, selected for import: {n}).")
                      .format(current=current, n=selected))


def text_count_error() -> LimitError:
    return LimitError(tr("Text limit reached"), tr("Up to 100 texts can be saved."))


def text_length_error(length: int) -> LimitError:
    return LimitError(tr("Text too long"),
                      tr("A text can contain up to 50,000 characters "
                         "(this text: {n}).").format(n=length))
