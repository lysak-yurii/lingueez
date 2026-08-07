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

"""The languages the app knows, and each service's code for them.

One vocabulary of English language names — the values stored in the DB and the
keys locale files translate — with a separate code map per service. The maps are
deliberately *not* derived from one another: the services disagree both on which
languages they handle and on what to call them, and collapsing that into one
table is what previously made 44 of the 106 offered languages silently
unspeakable.

Concretely, Google Translate and gTTS are both Google and still differ:

    Hebrew      translate "he"      speak "iw"
    Filipino    translate "fil"     speak "tl"
    Javanese    translate "jv"      speak "jw"
    Cantonese   translate "zh-HK"   speak "yue"

and gTTS has no voice at all for 40 languages Google Translate handles fine
(Slovenian, Persian, Georgian, Macedonian, Irish, Maltese, …). So a language
being translatable says nothing about it being speakable; ask the right map.

Kept free of heavy imports (no pygame, no requests) so both app.core.translator
and app.core.audio can read it without dragging the other's dependencies in.
"""

# Language name -> Google Translate code. The vocabulary every language combo
# offers, and the widest set: anything the app can translate at all is here.
# Codes verified against the endpoint in app.core.translator.translate_with_google.
TRANSLATION_CODES = {
     "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy",
     "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs",
     "Bulgarian": "bg", "Cantonese": "zh-HK", "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny",
     "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en",
     "Estonian": "et", "Filipino": "fil", "Finnish": "fi", "French": "fr", "Galician": "gl",
     "Georgian": "ka", "German": "de", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht",
     "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he", "Hindi": "hi", "Hmong": "hmn",
     "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Irish": "ga",
     "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", "Kazakh": "kk",
     "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kyrgyz": "ky", "Lao": "lo",
     "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk",
     "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Mandarin": "zh-CN",
     "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne",
     "Norwegian": "no", "Odia": "or", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
     "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru", "Samoan": "sm",
     "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
     "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es",
     "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tajik": "tg", "Tamil": "ta",
     "Tatar": "tt", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Turkmen": "tk",
     "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz", "Vietnamese": "vi",
     "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu",
}

# Language name -> gTTS code, for the subset gTTS can actually synthesize.
# Sourced from gtts.lang.tts_langs(); tests/test_languages.py fails if this
# drifts from what the installed gTTS supports. A name missing here is
# translatable but has no voice — callers must check, not assume.
SPEECH_CODES = {
     "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Basque": "eu",
     "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Cantonese": "yue", "Catalan": "ca",
     "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en",
     "Estonian": "et", "Filipino": "tl", "Finnish": "fi", "French": "fr", "Galician": "gl",
     "German": "de", "Greek": "el", "Gujarati": "gu", "Hausa": "ha", "Hebrew": "iw", "Hindi": "hi",
     "Hungarian": "hu", "Icelandic": "is", "Indonesian": "id", "Italian": "it", "Japanese": "ja",
     "Javanese": "jw", "Kannada": "kn", "Khmer": "km", "Korean": "ko", "Latin": "la",
     "Latvian": "lv", "Lithuanian": "lt", "Malay": "ms", "Malayalam": "ml", "Mandarin": "zh-CN",
     "Marathi": "mr", "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Polish": "pl",
     "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru", "Serbian": "sr",
     "Sinhala": "si", "Slovak": "sk", "Spanish": "es", "Sundanese": "su", "Swahili": "sw",
     "Swedish": "sv", "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr",
     "Ukrainian": "uk", "Urdu": "ur", "Vietnamese": "vi", "Welsh": "cy",
}

# Language name -> DeepL code, for the subset DeepL's /v2/translate accepts as
# target_lang. Routing only: translate() sends these to DeepL when the user has
# it configured, and everything else straight to Google. Deliberately narrower
# than DeepL's v3/next-gen language list, which /v2 does not accept.
DEEPL_CODES = {
     "Arabic": "AR", "Bulgarian": "BG", "Cantonese": "ZH-HANT", "Czech": "CS", "Danish": "DA",
     "Dutch": "NL", "English": "EN", "Estonian": "ET", "Finnish": "FI", "French": "FR",
     "German": "DE", "Greek": "EL", "Hebrew": "HE", "Hungarian": "HU", "Indonesian": "ID",
     "Italian": "IT", "Japanese": "JA", "Korean": "KO", "Latvian": "LV", "Lithuanian": "LT",
     "Mandarin": "ZH-HANS", "Norwegian": "NB", "Polish": "PL", "Portuguese": "PT",
     "Romanian": "RO", "Russian": "RU", "Slovak": "SK", "Slovenian": "SL", "Spanish": "ES",
     "Swedish": "SV", "Thai": "TH", "Turkish": "TR", "Ukrainian": "UK", "Vietnamese": "VI",
}

# Names once stored in the DB that are no longer offered, mapped to their
# current equivalent. "Chinese" predates splitting Mandarin from Cantonese; it
# had no gTTS entry at all, so those words could never be pronounced.
ALIASES = {
    "Chinese": "Mandarin",
}


def canonical(name):
    """Resolve a stored language name to the one the code maps are keyed on."""
    return ALIASES.get(name, name)


def is_known(name):
    """True if *name* is a language the app can translate."""
    return canonical(name) in TRANSLATION_CODES


def can_speak(name):
    """True if *name* has a text-to-speech voice (a subset of is_known)."""
    return canonical(name) in SPEECH_CODES
