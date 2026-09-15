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

"""AI provider abstraction (definitions and generated texts).

Two interchangeable backends — OpenAI (ChatGPT) and Google Gemini — behind
one facade. The active backend is selected by the ``ai_provider`` setting;
each backend reads its own model/prompt settings (``chatgpt_*`` /
``gemini_*`` keys in settings.cfg) and its API key from .env.

All generation failures are raised as :class:`AIError` with a message fit
for showing to the user directly.
"""
import logging
import os
import threading

from dotenv import load_dotenv

from app.config import load_settings, get_float, get_int
from app.core.backup_management import backup_database
from app.core.database_adapter import DatabaseAdapter
from app.i18n import tr

DEFAULT_PROVIDER = "openai"


class AIError(Exception):
    """A generation failure with a user-presentable message."""


# --------------------------------------------------------------- providers

class _Provider:
    """Base class: API-key handling, client caching, error translation."""

    id = ""
    label = ""
    env_key = ""
    settings_prefix = ""

    def __init__(self):
        self._lock = threading.Lock()
        self._client = None
        self._client_key = None

    def api_key(self):
        load_dotenv()
        return (os.getenv(self.env_key) or "").strip()

    def has_api_key(self):
        return bool(self.api_key())

    def reset(self):
        """Drop the cached client (call after the API key changes)."""
        with self._lock:
            self._client = None
            self._client_key = None

    def _cached_client(self):
        key = self.api_key()
        if not key:
            raise AIError(f"{self.label} API key is not set. "
                          f"Configure it in Settings → Translation & AI → AI.")
        with self._lock:
            if self._client is None or self._client_key != key:
                self._client = self._make_client(key)
                self._client_key = key
            return self._client

    def complete(self, prompt, model, max_tokens, temperature, role="user"):
        """Run one prompt; returns non-empty text or raises AIError."""
        if not model:
            raise AIError(f"No {self.label} model configured. "
                          f"Set one in Settings → Translation & AI → AI.")
        try:
            text = self._complete(prompt, model, max_tokens, temperature, role)
        except AIError:
            raise
        except Exception as exc:
            logging.error(f"{self.label} request failed: {exc}")
            raise AIError(self._friendly_error(exc)) from exc
        text = (text or "").strip()
        if not text:
            raise AIError(f"{self.label} returned an empty response. "
                          f"Try again or raise 'Max tokens' in Settings.")
        return text

    # subclasses implement:
    def _make_client(self, api_key):
        raise NotImplementedError

    def _complete(self, prompt, model, max_tokens, temperature, role):
        raise NotImplementedError

    def _friendly_error(self, exc):
        raise NotImplementedError


class _OpenAIProvider(_Provider):
    id = "openai"
    label = "ChatGPT"
    env_key = "OPENAI_API_KEY"
    settings_prefix = "chatgpt"

    def _make_client(self, api_key):
        from openai import OpenAI
        return OpenAI(api_key=api_key)

    def _complete(self, prompt, model, max_tokens, temperature, role):
        response = self._cached_client().chat.completions.create(
            model=model,
            messages=[{"role": role, "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content

    def _friendly_error(self, exc):
        import openai
        if isinstance(exc, openai.AuthenticationError):
            return tr("Invalid OpenAI API key. "
                      "Check it in Settings → Translation & AI → AI → OpenAI.")
        if isinstance(exc, openai.RateLimitError):
            if "insufficient_quota" in str(exc):
                return tr("Your OpenAI account is out of credits. Add credits at "
                          "platform.openai.com/account/billing, or switch the AI "
                          "provider to Gemini in Settings → Translation & AI → AI.")
            return tr("OpenAI rate limit reached. Wait a moment and try again.")
        if isinstance(exc, openai.NotFoundError):
            return tr("Unknown OpenAI model. "
                      "Check the model name in Settings → Translation & AI → AI → OpenAI.")
        if isinstance(exc, openai.APIConnectionError):
            return tr("Could not reach OpenAI. Check your internet connection.")
        return f"OpenAI error: {exc}"


class _GeminiProvider(_Provider):
    id = "gemini"
    label = "Gemini"
    env_key = "GOOGLE_API_KEY"
    settings_prefix = "gemini"

    def _make_client(self, api_key):
        from google import genai
        return genai.Client(api_key=api_key)

    def _complete(self, prompt, model, max_tokens, temperature, role):
        from google.genai import types
        config = types.GenerateContentConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        )
        # Thinking models (gemini-2.5-flash…) spend reasoning tokens from the
        # same max_output_tokens budget; budget 0 disables that so small caps
        # still yield full answers. -1 = let the model decide (needed for pro).
        budget = get_int(load_settings(), "gemini_thinking_budget", 0)
        if budget >= 0:
            config.thinking_config = types.ThinkingConfig(thinking_budget=budget)
        response = self._cached_client().models.generate_content(
            model=model,
            contents=prompt,
            config=config,
        )
        return response.text

    def _friendly_error(self, exc):
        from google.genai import errors
        if isinstance(exc, errors.APIError):
            if exc.code == 429:
                return tr("Gemini quota exhausted. The free tier resets daily; wait, "
                          "or create a new key at aistudio.google.com/app/apikey.")
            if exc.code in (401, 403):
                return tr("Invalid Google API key. "
                          "Check it in Settings → Translation & AI → AI → Gemini.")
            if exc.code == 404:
                return tr("Unknown Gemini model. "
                          "Check the model name in Settings → Translation & AI → AI → Gemini.")
            return f"Gemini error {exc.code}: {exc.message}"
        return f"Gemini error: {exc}"


_PROVIDERS = {p.id: p for p in (_OpenAIProvider(), _GeminiProvider())}


# ------------------------------------------------------------------ facade

def get_provider(settings=None):
    """The active provider per the ``ai_provider`` setting."""
    settings = settings or load_settings()
    pid = str(settings.get("ai_provider", DEFAULT_PROVIDER)).strip().lower()
    return _PROVIDERS.get(pid, _PROVIDERS[DEFAULT_PROVIDER])


def provider_label():
    """Display name of the active provider ('ChatGPT' / 'Gemini')."""
    return get_provider().label


def has_api_key():
    return get_provider().has_api_key()


def reset_clients():
    """Drop all cached API clients (call after keys change in .env)."""
    for provider in _PROVIDERS.values():
        provider.reset()


def _task_params(settings, provider, task=""):
    """Model/prompt settings for one task, e.g. chatgpt_texts_* keys."""
    prefix = provider.settings_prefix + (f"_{task}" if task else "")
    return {
        "model": str(settings.get(f"{prefix}_model", "")).strip(),
        "max_tokens": get_int(settings, f"{prefix}_max_tokens", 400),
        "temperature": get_float(settings, f"{prefix}_temperature", 0.5),
        "role": str(settings.get(f"{prefix}_role", "user")).strip() or "user",
        "template": str(settings.get(f"{prefix}_content", "")),
    }


def _render(template, **values):
    if not template.strip():
        raise AIError("The prompt template is empty. "
                      "Fix it in Settings → Translation & AI → AI.")
    try:
        return template.format(**values)
    except (KeyError, IndexError, ValueError) as exc:
        raise AIError(f"Invalid prompt template ({exc}). "
                      f"Fix it in Settings → Translation & AI → AI.")


WORD_SIDES = ("Word1", "Word2")
LANGUAGE_SIDES = ("Language1", "Language2")


_PAIRED_COLUMNS = (('Word1', 'Word2'), ('Language1', 'Language2'),
                   ('Definition', 'Definition2'))


def definition_column(language_side):
    """The column a definition written in *language_side* is stored in."""
    return 'Definition' if language_side == 'Language1' else 'Definition2'


def is_mirrored(row, shown):
    """True when *shown* presents the stored *row* with its sides flipped — the
    words table does that for rows matching a language filter."""
    return (bool(shown) and bool(row)
            and shown.get('Language1') != row.get('Language1')
            and shown.get('Language1') == row.get('Language2'))


def oriented(row, mirrored):
    """*row* with Word/Language/Definition sides flipped when *mirrored*."""
    if not mirrored:
        return dict(row)
    out = dict(row)
    for first, second in _PAIRED_COLUMNS:
        out[first], out[second] = row.get(second), row.get(first)
    return out


def stored_column(column, mirrored):
    """Map a Definition column of an oriented row back to the stored one."""
    if not mirrored:
        return column
    return 'Definition2' if column == 'Definition' else 'Definition'


def definition_request(record, word_side, language_side):
    """``get_definition`` kwargs for defining *word_side* of a word row in
    *language_side*; the other side supplies the translation hint."""
    first = word_side != 'Word2'
    other_side = 'Word2' if first else 'Word1'
    return {
        "word": str(record.get(word_side) or "").strip(),
        "word_language": record.get('Language1' if first else 'Language2') or "English",
        "language": record.get(language_side) or "English",
        "translation": str(record.get(other_side) or "").strip(),
        "translation_language": record.get('Language2' if first else 'Language1') or "",
    }


def build_definition_prompt(template, word, word_language, language,
                            translation="", translation_language=""):
    """Render a definition prompt template; raises AIError on a broken one."""
    same = word_language.strip().lower() == language.strip().lower()
    sense_hint = ""
    if translation and translation_language:
        sense_hint = (f'The learner saved it with the {translation_language} '
                      f'translation "{translation}": start with that sense, but '
                      f"don't leave out the word's other common senses. ")
    if same:
        sections = "'Definition', 'Example Sentences' and 'Synonyms'"
        language_rules = f"Write the whole entry solely in {language}."
    else:
        sections = "'Definition', 'Translations', 'Example Sentences' and 'Synonyms'"
        language_rules = (
            f"Write the grammar line and the definition in {language}. Under "
            f"'Translations', give the word's possible {language} translations as "
            f"one list item per sense: the translations in bold, then a short "
            f"italic note on when they apply, most common first. Keep the example "
            f"sentences and synonyms in {word_language}, following each example "
            f"sentence with its {language} translation in parentheses, and let the "
            f"examples show the different senses.")
    return _render(template, word=word, word_language=word_language,
                   language=language, translation=translation,
                   translation_language=translation_language,
                   sense_hint=sense_hint, sections=sections,
                   language_rules=language_rules,
                   # legacy placeholders of hand-edited templates
                   language1=language,
                   language2=translation_language if same else word_language)


def get_definition(word, word_language, language, translation="",
                   translation_language=""):
    """Define *word* (in *word_language*) writing in *language*; raises AIError."""
    settings = load_settings()
    provider = get_provider(settings)
    params = _task_params(settings, provider)
    prompt = build_definition_prompt(params.pop("template"), word, word_language,
                                     language, translation, translation_language)
    # senses, translations and translated examples outgrow old 400-token configs
    params["max_tokens"] = max(params["max_tokens"], 1000)
    return provider.complete(prompt, **params)


def lemma_translate(word, sentence, source_language, target_language):
    """Lemma form of *word* (as used in *sentence*) + its best translation.

    Returns (lemma, translation); raises AIError. Uses the definition-task
    model settings of the active provider with a fixed prompt.
    """
    settings = load_settings()
    provider = get_provider(settings)
    params = _task_params(settings, provider)
    params.pop("template")
    context = f' in the sentence: "{sentence.strip()}"' if sentence.strip() else ""
    prompt = (
        f'The {source_language} word "{word}" is used{context}. '
        f"Give its dictionary (lemma) form in {source_language} — e.g. the "
        f"infinitive for verbs, nominative singular for nouns (with the "
        f"article if customary for dictionary entries in {source_language}) — "
        f"and its best {target_language} translation for this exact context. "
        f"Answer with ONE line in exactly this format and nothing else:\n"
        f"lemma|translation"
    )
    content = provider.complete(prompt, **params)
    # last non-empty line guards against models that prepend chatter
    line = [ln for ln in content.splitlines() if ln.strip()][-1].strip()
    lemma, sep, translation = line.partition("|")
    if not sep or not lemma.strip() or not translation.strip():
        # tolerate a malformed answer: keep the clicked word as the entry
        return word, line.strip().strip("|")
    return lemma.strip(), translation.strip()


def generate_combined_text(words, language):
    """Generate (title, text) from a word list; raises AIError."""
    settings = load_settings()
    provider = get_provider(settings)
    params = _task_params(settings, provider, task="texts")
    prompt = _render(params.pop("template"), words=words, language=language)
    content = provider.complete(prompt, **params)
    return _split_title_text(content)


def generate_topic_text(language, level, topic, length_words):
    """Generate (title, text) for a language/level/topic; raises AIError."""
    settings = load_settings()
    provider = get_provider(settings)
    params = _task_params(settings, provider, task="texts_topic")
    prompt = _render(params.pop("template"), language=language, level=level,
                     topic=topic, length=length_words)
    # the configured cap is a floor — long texts need room (~3 tokens/word)
    params["max_tokens"] = max(params["max_tokens"], int(length_words) * 3 + 200)
    content = provider.complete(prompt, **params)
    return _split_title_text(content)


def adapt_text_to_level(text, language, level):
    """Rewrite *text* for a CEFR level; returns (title, text), raises AIError."""
    settings = load_settings()
    provider = get_provider(settings)
    params = _task_params(settings, provider, task="texts_adapt")
    snippet = text.strip()[:6000]
    prompt = _render(params.pop("template"), text=snippet,
                     language=language, level=level)
    params["max_tokens"] = max(params["max_tokens"], len(snippet) // 2 + 300)
    content = provider.complete(prompt, **params)
    return _split_title_text(content)


def _split_title_text(content):
    """Split model output into (title, text), tolerating missing delimiters."""
    title, _, text = content.partition("\n\n")
    if not text.strip():
        title, _, text = content.partition("\n")
    if not text.strip():
        return "", content.strip()
    return title.strip().strip("#*").strip(), text.strip()


# ------------------------------------------------------------- db helpers

def _make_db_adapter():
    # Cloud writes follow the backend identity (account *or* personal server).
    from app.core.auth_manager import cloud_backend_active
    return DatabaseAdapter(use_cloud=cloud_backend_active())


def store_definition(word_id, column, text, db_adapter=None):
    """Save a definition into its stored *column* and snapshot the database."""
    db_adapter = db_adapter or _make_db_adapter()
    try:
        db_adapter.update_word(word_id, {column: text})
    finally:
        backup_database()


def generate_definitions(records, word_side, language_side, skip_existing=True,
                         db_adapter=None, is_cancelled=lambda: False,
                         progress_callback=None):
    """Generate and store definitions for many words, one request each.

    *records* are rows as the table shows them; the sides are read in that
    orientation. Returns ``{"generated", "skipped", "failed", "error",
    "cancelled"}``; ``error`` is the last AI error message. Stops early once the
    same error repeats, since quota, key and connection failures never recover
    mid-run.
    """
    db_adapter = db_adapter or _make_db_adapter()
    column = definition_column(language_side)
    stats = {"generated": 0, "skipped": 0, "failed": 0, "error": "", "cancelled": False}
    last_error = None
    try:
        for index, record in enumerate(records):
            if is_cancelled():
                stats["cancelled"] = True
                break
            if progress_callback:
                progress_callback(index, len(records))
            word_id = record["ID"]
            row = db_adapter.get_word(word_id)
            mirrored = is_mirrored(row, record)
            view = oriented(row or {}, mirrored)
            request = definition_request(view, word_side, language_side)
            if not row or not request["word"]:
                stats["failed"] += 1
                continue
            if skip_existing and str(view.get(column) or "").strip():
                stats["skipped"] += 1
                continue
            try:
                text = get_definition(**request)
                db_adapter.update_word(word_id, {stored_column(column, mirrored): text})
                stats["generated"] += 1
                last_error = None
            except AIError as exc:
                stats["failed"] += 1
                stats["error"] = str(exc)
                if str(exc) == last_error:
                    break
                last_error = str(exc)
            except Exception as exc:
                logging.error(f"Error generating definition for {word_id}: {exc}")
                stats["failed"] += 1
        if progress_callback:
            progress_callback(len(records), len(records))
    finally:
        if stats["generated"]:
            backup_database()
    return stats


def save_generated_text_to_db(row_number, title, text, words, language,
                              level=None, category=None):
    """Returns (ok, message)."""
    try:
        db_adapter = _make_db_adapter()
        result = db_adapter.insert_text({
            'RowNumber': row_number,
            'Title': title,
            'Text': text,
            'Words': words,
            'Language': language,
            'Level': level,
            'Category': category,
        })
        if result:
            backup_database()
            return True, "Text saved successfully."
        return False, "Failed to save text to database."
    except Exception as exc:
        logging.error(f"Error saving text to database: {exc}")
        return False, f"An error occurred: {exc}"
