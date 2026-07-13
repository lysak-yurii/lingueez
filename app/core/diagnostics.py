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

"""Build a support-friendly diagnostics bundle (logs + environment info).

Shared by the "Report an issue" flow in About (visible to everyone) and the
advanced Log viewer's "Export diagnostics" button. Log files are already
redacted on write (see log_redaction.py), so the bundle is safe to share.
"""
import glob
import os
import platform
import tempfile
import zipfile
from datetime import datetime

from app.version import APP_NAME, APP_VERSION, BUILD_NUMBER

# Log files resolve relative to the chdir'd working dir (see main._setup_paths).
_LOG_GLOB = "app.log*"  # current + rotated backups (app.log.1 ..)
_CRASH_LOG = "crash.log"


def system_info():
    """Human-readable environment summary — also reused in the issue body."""
    return (
        f"{APP_NAME} {APP_VERSION} (build {BUILD_NUMBER})\n"
        f"OS: {platform.platform()}\n"
        f"Python: {platform.python_version()}"
    )


def build_ai_report_mailto():
    """Build a ``mailto:`` URL for reporting inappropriate AI-generated content.

    Kept Qt-free (returns a plain string) so it's unit-testable; the UI just hands
    the result to ``QDesktopServices.openUrl``. Pre-fills a short template plus the
    ``system_info()`` environment block, addressed to the report inbox.
    """
    from urllib.parse import urlencode

    from app.i18n import tr
    from app.version import REPORT_EMAIL

    subject = tr("Report: inappropriate AI-generated content")
    body = tr(
        "Please describe the AI-generated content you're reporting.\n\n"
        "Where it appeared (definition / generated text / word translation):\n"
        "The word or text in question:\n"
        "Why it is inappropriate:\n\n"
        "---\n"
    ) + system_info() + "\n"
    query = urlencode({"subject": subject, "body": body})
    return f"mailto:{REPORT_EMAIL}?{query}"


def build_diagnostics_zip(dest_dir=None):
    """Zip the logs + environment info and return the path to the archive.

    ``dest_dir`` defaults to the OS temp directory.
    """
    dest_dir = dest_dir or tempfile.gettempdir()
    os.makedirs(dest_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    zip_path = os.path.join(dest_dir, f"lingueez-diagnostics-{stamp}.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("system-info.txt", system_info())
        for name in sorted(glob.glob(_LOG_GLOB)) + [_CRASH_LOG]:
            if os.path.isfile(name):
                try:
                    zf.write(name, os.path.basename(name))
                except OSError:
                    pass  # a locked/rotating file shouldn't abort the bundle
    return zip_path
