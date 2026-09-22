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

"""Related words: which saved words belong together.

Pure data — no Qt imports. Two kinds of relation, both within one language:

    translation  words sharing a translation segment ("glücklich" and
                 "fröhlich" both → "happy")
    root         words sharing a stem ("Anstand", "Anstandsdame"), or the same
                 word saved under several language pairs; with snowballstemmer
                 installed, also a word and the phrases that use it
                 ("χαλαρά", "Δείξε χαλαρός")
"""
from __future__ import annotations

import os
import re
import unicodedata
from collections import defaultdict

try:
    import snowballstemmer
except ImportError:  # optional: without it only the prefix rule applies
    snowballstemmer = None

KINDS = ("translation", "root")

MAX_GROUP = 12       # a translation/stem shared by more words says nothing
ROOT_LEN = 6
ROOT_SHARE = 0.6
STEM_MIN = 4         # shorter tokens/stems are mostly function words

_SEGMENT_SPLIT = re.compile(r"[,;/|]")
_PARENS = re.compile(r"\([^)]*\)|\[[^\]]*\]")
_TOKEN = re.compile(r"\w+")
_LEADING_ARTICLES = (
    "to ", "the ", "a ", "an ",
    "der ", "die ", "das ", "ein ", "eine ", "sich ",
    "el ", "la ", "los ", "las ", "un ", "una ",
    "le ", "les ", "une ",
    "ο ", "η ", "το ", "οι ", "τα ",
)


def fold(text):
    """Casefold and drop diacritics, so "Funklöcher"/"funklocher" and
    "καλός"/"καλος" share a key."""
    text = unicodedata.normalize("NFD", (text or "").casefold())
    return "".join(ch for ch in text if not unicodedata.combining(ch)).strip()


def translation_keys(text):
    """The comparable segments of a translation: "бігом (поспішно), біг" →
    {"бігом", "біг"}."""
    keys = set()
    for seg in _SEGMENT_SPLIT.split(_PARENS.sub(" ", text or "")):
        seg = " ".join(fold(seg).split()).strip(" .!?…\"'«»")
        for article in _LEADING_ARTICLES:
            if seg.startswith(article) and len(seg) > len(article):
                seg = seg[len(article):]
                break
        if seg:
            keys.add(seg)
    return keys


def root_key(word):
    """Stem bucket for a single word; phrases have none. Short words only
    match their exact spelling."""
    w = fold(word)
    if not w or " " in w:
        return None
    return w[:ROOT_LEN] if len(w) >= ROOT_LEN else f"={w}"


def _stemmer(language, cache):
    """The snowball stemmer for an app language name ("Greek"), or None.

    ``cache`` is per build: stemmer objects keep state between calls, so two
    builds on worker threads must not share one."""
    if snowballstemmer is None or not language:
        return None
    if language not in cache:
        algorithm = language.strip().lower()
        cache[language] = (snowballstemmer.stemmer(algorithm)
                           if algorithm in snowballstemmer.algorithms() else None)
    return cache[language]


def is_headword(text):
    """A single word, or forms of one listed together ("τρέχω / έτρεξα",
    "run, ran") — anything but a phrase."""
    counts = [len(_TOKEN.findall(seg))
              for seg in _SEGMENT_SPLIT.split(_PARENS.sub(" ", text or ""))]
    counts = [n for n in counts if n]
    return bool(counts) and all(n == 1 for n in counts)


def _group_pairs(groups):
    for members in groups.values():
        members = sorted(set(members))
        if not 2 <= len(members) <= MAX_GROUP:
            continue
        for i, a in enumerate(members):
            for b in members[i + 1:]:
                yield a, b


def _translation_pairs(words):
    groups = defaultdict(list)
    for i, w in enumerate(words):
        lang = w.get("Language2") or ""
        for key in translation_keys(w.get("Word2")):
            groups[(lang, key)].append(i)
    return _group_pairs(groups)


def _root_pairs(words):
    groups = defaultdict(list)
    folded = [fold(w.get("Word1")) for w in words]
    for i, w in enumerate(words):
        key = root_key(w.get("Word1"))
        if key:
            groups[(w.get("Language1") or "", key)].append(i)
    for a, b in _group_pairs(groups):
        fa, fb = folded[a], folded[b]
        if len(os.path.commonprefix((fa, fb))) >= ROOT_SHARE * min(len(fa), len(fb)):
            yield a, b


def _stem_pairs(words):
    """Words whose (stemmed) tokens meet; one side must be a single word, as
    two phrases sharing one word are rarely related."""
    groups = defaultdict(set)
    stemmers = {}
    for i, w in enumerate(words):
        stemmer = _stemmer(w.get("Language1"), stemmers)
        if stemmer is None:
            continue
        text = (w.get("Word1") or "").casefold()
        tokens = _TOKEN.findall(_PARENS.sub(" ", text))
        single = is_headword(text)
        for token in tokens:
            if len(token) < STEM_MIN:
                continue
            stem = fold(stemmer.stemWord(token))
            if len(stem) >= STEM_MIN:
                groups[(w.get("Language1"), stem)].add((i, single))
    for members in groups.values():
        if not 2 <= len(members) <= MAX_GROUP:
            continue
        members = sorted(members)
        for n, (a, a_single) in enumerate(members):
            for b, b_single in members[n + 1:]:
                if a_single or b_single:
                    yield a, b


def build_related(words):
    """``{word_id: {"translation": [ids], "root": [ids]}}`` for every word
    that has at least one relation.

    ``words``: dicts with ID, Word1, Word2, Language1 and Language2. A word
    related both ways is listed under "translation" only.
    """
    seen = set()
    unique = []
    for w in words:
        wid = w.get("ID")
        if wid and wid not in seen:
            seen.add(wid)
            unique.append(w)

    related = defaultdict(lambda: {kind: [] for kind in KINDS})
    linked = set()
    for kind, pairs in (("translation", _translation_pairs(unique)),
                        ("root", _root_pairs(unique)),
                        ("root", _stem_pairs(unique))):
        for a, b in pairs:
            ida, idb = unique[a]["ID"], unique[b]["ID"]
            pair = frozenset((ida, idb))
            if pair in linked:
                continue
            linked.add(pair)
            related[ida][kind].append(idb)
            related[idb][kind].append(ida)
    return dict(related)
