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

"""Subprocess/ffmpeg helpers shared by the audio pipeline."""
import os
import re
import subprocess
import sys
from datetime import datetime


class NoConsolePopen(subprocess.Popen):
    """Popen that suppresses console windows on Windows."""

    def __init__(self, *args, **kwargs):
        if os.name == 'nt':
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
        super().__init__(*args, **kwargs)


_original_subprocess_run = subprocess.run
_original_subprocess_call = subprocess.call


def no_console_run(*args, **kwargs):
    if os.name == 'nt':
        kwargs.setdefault('creationflags', subprocess.CREATE_NO_WINDOW)
    return _original_subprocess_run(*args, **kwargs)


def no_console_call(*args, **kwargs):
    if os.name == 'nt':
        kwargs.setdefault('creationflags', subprocess.CREATE_NO_WINDOW)
    return _original_subprocess_call(*args, **kwargs)


def read_ffmpeg_path():
    """Point pydub at a bundled ./ffmpeg/bin if present, else rely on PATH."""
    from pydub import AudioSegment

    if sys.platform == 'win32':
        ffmpeg_bin = os.path.join("ffmpeg", "bin", "ffmpeg.exe")
        ffprobe_bin = os.path.join("ffmpeg", "bin", "ffprobe.exe")
    else:
        ffmpeg_bin = os.path.join("ffmpeg", "bin", "ffmpeg")
        ffprobe_bin = os.path.join("ffmpeg", "bin", "ffprobe")

    if os.path.isfile(ffmpeg_bin):
        AudioSegment.converter = ffmpeg_bin
        AudioSegment.ffprobe = ffprobe_bin
        os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_bin)


def suggest_filename(prefix, timestamp=True, word_count=None, lang1=None, lang2=None,
                     status=None, extension=".mp3"):
    """Build a descriptive default filename for exports."""
    parts = [prefix]
    if timestamp:
        parts.append(datetime.now().strftime("%Y%m%d_%H%M%S"))
    if word_count is not None:
        parts.append(f"{word_count}words")
    if lang1 and lang1 != "Language":
        parts.append(lang1)
    if lang2 and lang2 != "Translation":
        parts.append(f"to_{lang2}")
    if status and status != "Status":
        parts.append(status)
    name = re.sub(r'[^\w\s]', '', "_".join(parts))
    return f"{name}{extension}"
