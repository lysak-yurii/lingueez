"""OpenAI ChatGPT integration (definitions and generated texts).

GUI-free port of the original gpt.py: no tkinter prompts at import time;
the API key is read lazily from .env / the environment and errors are
raised to the caller.
"""
import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.config import load_settings, get_float, get_int
from app.core.backup_management import backup_database
from app.core.database_adapter import DatabaseAdapter

_client = None


def create_env_file(api_key=""):
    with open('.env', 'w', encoding='utf-8') as env_file:
        env_file.write(f'OPENAI_API_KEY={api_key}\n')


def set_api_key(api_key):
    """Persist the key to .env and reset the cached client."""
    global _client
    create_env_file(api_key)
    os.environ['OPENAI_API_KEY'] = api_key
    _client = None


def get_client():
    """Return a cached OpenAI client, or None when no key is configured."""
    global _client
    if _client is not None:
        return _client
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return None
    _client = OpenAI(api_key=api_key)
    return _client


def has_api_key():
    load_dotenv()
    return bool(os.getenv('OPENAI_API_KEY'))


def _make_db_adapter():
    settings = load_settings()
    enable_sync = settings.get("enable_sync", "false").lower() == "true"
    return DatabaseAdapter(use_cloud=enable_sync)


def get_definition_from_gpt(word, language1, language2):
    """Fetch a definition; raises on missing key or API failure."""
    client = get_client()
    if client is None:
        raise ValueError("ChatGPT API key is not set. Configure it in Settings → APIs → OpenAI.")

    settings = load_settings()
    model = settings.get("chatgpt_model", "gpt-4o-mini")
    role = settings.get("chatgpt_role", "assistant")
    content = settings.get(
        "chatgpt_content",
        "Define the word: {word} in {language1} and in {language2}. "
        "Also provide example sentences (in different contexts) with that word, "
        "and synonyms solely in {language1}. Markups: '***' for 'Definition', "
        "'Example Sentences' and 'Synonyms'; other possible markups: '**' and '*'.",
    )
    max_tokens = get_int(settings, "chatgpt_max_tokens", 400)
    temperature = get_float(settings, "chatgpt_temperature", 0.3)

    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role": role,
            "content": content.format(word=word, language1=language1, language2=language2),
        }],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def update_definition_in_db(word, language1, language2, word_field, word_id):
    """Fetch a GPT definition and store it. Returns (ok, message)."""
    try:
        definition = get_definition_from_gpt(word, language1, language2)
        if not definition:
            return False, "Failed to fetch the definition."

        db_adapter = _make_db_adapter()
        word_data = db_adapter.get_word(word_id)
        if not word_data:
            return False, f"Word with ID {word_id} not found."

        definition_column = 'Definition' if word_field == 'Word1' else 'Definition2'
        db_adapter.update_word(word_id, {definition_column: definition})
        return True, f"Definition for '{word}' was successfully updated."

    except Exception as exc:
        logging.error(f"Error updating definition: {exc}")
        return False, f"An error occurred: {exc}"
    finally:
        backup_database()


def generate_combined_text_from_gpt(words, language):
    """Generate (title, text) from a word list; raises on missing key."""
    client = get_client()
    if client is None:
        raise ValueError("ChatGPT API key is not set. Configure it in Settings → APIs → OpenAI.")

    settings = load_settings()
    model = settings.get("chatgpt_texts_model", "gpt-4o-mini")
    role = settings.get("chatgpt_texts_role", "assistant")
    content_template = settings.get(
        "chatgpt_texts_content",
        'Generate a title and a comprehensive text using the following words: {words} '
        'in the following language: {language}.Separate the title and text with a '
        'delimiter like "\\n\\n". And do not use any markups(\'**\' etc.)',
    )
    max_tokens = get_int(settings, "chatgpt_texts_max_tokens", 300)
    temperature = get_float(settings, "chatgpt_texts_temperature", 0.7)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": role, "content": content_template.format(words=words, language=language)}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    content = response.choices[0].message.content.strip()
    title, text = content.split("\n\n", 1)
    return title, text


def save_generated_text_to_db(row_number, title, text, words, language):
    """Returns (ok, message)."""
    try:
        db_adapter = _make_db_adapter()
        result = db_adapter.insert_text({
            'RowNumber': row_number,
            'Title': title,
            'Text': text,
            'Words': words,
            'Language': language,
        })
        if result:
            backup_database()
            return True, "Text saved successfully."
        return False, "Failed to save text to database."
    except Exception as exc:
        logging.error(f"Error saving text to database: {exc}")
        return False, f"An error occurred: {exc}"
