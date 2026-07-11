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

"""Distribution-package detection.

The Windows `.exe` installer and the Microsoft Store MSIX ship the *same*
PyInstaller binary, so "am I the Store build?" can't be a compile-time constant —
it must be answered at runtime. A packaged (MSIX) process has *package identity*;
an unpackaged one does not. :func:`is_msix` asks the OS via
``GetCurrentPackageFullName``: it returns ``APPMODEL_ERROR_NO_PACKAGE`` for the
plain `.exe` and success for the MSIX.

The Store manages updates itself and its certification dislikes apps steering
users to off-Store downloads, so the UI uses this to hide the (GitHub-based)
update affordances when running from the Store. Mirrors the style of
``hotkey_env.is_flatpak()``.
"""
import sys

# Win32 AppModel error returned by GetCurrentPackageFullName when the calling
# process has no package identity (i.e. the plain .exe, not the MSIX).
_APPMODEL_ERROR_NO_PACKAGE = 15700

_msix_cache = None


def is_msix():
    """True when running as a packaged (MSIX / Microsoft Store) app.

    Cached — package identity can't change within a process. Always False off
    Windows, and False (never raises) if the API is unavailable, so callers can
    use it unconditionally.
    """
    global _msix_cache
    if _msix_cache is not None:
        return _msix_cache

    packaged = False
    if sys.platform == "win32":
        try:
            import ctypes
            from ctypes import wintypes

            # Passing a zero-length buffer makes the call return the required
            # length; we only care about the return code, not the name itself.
            length = wintypes.UINT(0)
            rc = ctypes.windll.kernel32.GetCurrentPackageFullName(
                ctypes.byref(length), None)
            packaged = rc != _APPMODEL_ERROR_NO_PACKAGE
        except (AttributeError, OSError):
            # GetCurrentPackageFullName is absent on very old Windows; treat any
            # failure as "unpackaged" rather than crash the app at startup.
            packaged = False

    _msix_cache = packaged
    return packaged
