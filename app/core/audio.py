"""Text-to-speech playback and audio-file generation.

Port of the original dictionary/audio.py with the tkinter message boxes
removed: errors are reported through logging / the optional ``logger``
callback so the module is GUI-framework independent.
"""
import concurrent.futures
import logging
import os
import queue
import random
import subprocess
import tempfile
import threading
import time
from queue import Queue

import pygame
from gtts import gTTS

from app.config import load_settings, get_int
from app.core.shell_utils import (
    NoConsolePopen, no_console_call, no_console_run, read_ffmpeg_path,
)

try:
    from app.core.google_cloud_tts import (
        get_google_cloud_language_code, synthesize_text_to_speech,
    )
    GOOGLE_CLOUD_TTS_AVAILABLE = True
except ImportError:
    GOOGLE_CLOUD_TTS_AVAILABLE = False
    logging.warning("Google Cloud TTS not available. Install google-cloud-texttospeech to use it.")

# Patch subprocess before pydub imports it so no console windows pop up on Windows
subprocess.Popen = NoConsolePopen
subprocess.run = no_console_run
subprocess.call = no_console_call

from pydub import AudioSegment  # noqa: E402

read_ffmpeg_path()

try:
    pygame.mixer.init()
except pygame.error as exc:  # no audio device (e.g. headless CI)
    logging.warning(f"pygame mixer init failed: {exc}")

# Language name -> gTTS code
lang_codes = {
    'Detect language': 'en', 'English': 'en', 'German': 'de', 'Spanish': 'es',
    'Ukrainian': 'uk', 'French': 'fr', 'Italian': 'it', 'Portuguese': 'pt',
    'Russian': 'ru', 'Greek': 'el', 'Arabic': 'ar', 'Bengali': 'bn',
    'Cantonese': 'zh-HK', 'Hindi': 'hi', 'Japanese': 'ja', 'Korean': 'ko',
    'Mandarin': 'zh-CN', 'Polish': 'pl', 'Turkish': 'tr', 'Vietnamese': 'vi',
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Armenian': 'hy',
    'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bosnian': 'bs',
    'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny',
    'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl',
    'Estonian': 'et', 'Filipino': 'fil', 'Finnish': 'fi', 'Galician': 'gl',
    'Georgian': 'ka', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha',
    'Hawaiian': 'haw', 'Hebrew': 'he', 'Hmong': 'hmn', 'Hungarian': 'hu',
    'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga',
    'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km',
    'Kinyarwanda': 'rw', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la',
    'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
    'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml',
    'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn',
    'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or',
    'Pashto': 'ps', 'Persian': 'fa', 'Punjabi': 'pa', 'Romanian': 'ro',
    'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st',
    'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk',
    'Slovenian': 'sl', 'Somali': 'so', 'Sundanese': 'su', 'Swahili': 'sw',
    'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt',
    'Telugu': 'te', 'Thai': 'th', 'Turkmen': 'tk', 'Urdu': 'ur',
    'Uyghur': 'ug', 'Uzbek': 'uz', 'Welsh': 'cy', 'Xhosa': 'xh',
    'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu',
}

stop_event = threading.Event()
playback_queue = Queue()
playback_lock = threading.Lock()
is_playing = threading.Event()
current_files = set()
all_temp_files = set()
temp_files_lock = threading.Lock()


def get_tts_settings():
    """Return (provider, credentials_path, voice_type, voice_name)."""
    settings = load_settings()
    provider = settings.get("tts_provider", "gTTS").lower()
    if "google" in provider and "cloud" in provider:
        provider = "google_cloud_tts"
    else:
        provider = "gtts"

    credentials_path = settings.get("google_cloud_tts_credentials_path", "")
    voice_type = settings.get("google_cloud_tts_voice_type", "standard").lower()
    voice_name = settings.get("google_cloud_tts_voice_name", "")

    if provider == "google_cloud_tts" and not GOOGLE_CLOUD_TTS_AVAILABLE:
        logging.warning("Google Cloud TTS selected but not available. Falling back to gTTS.")
        provider = "gtts"

    return provider, credentials_path, voice_type, voice_name


def synthesize_speech(text, language_code, cancellation_event=None):
    """Generate an mp3 for *text*; returns the temp-file path or None."""
    provider, credentials_path, voice_type, voice_name = get_tts_settings()

    if cancellation_event and cancellation_event.is_set():
        return None

    if provider == "google_cloud_tts" and GOOGLE_CLOUD_TTS_AVAILABLE:
        try:
            if get_google_cloud_language_code(language_code):
                result = synthesize_text_to_speech(
                    text=text,
                    app_language_code=language_code,
                    credentials_path=credentials_path or None,
                    voice_type=voice_type,
                    voice_name=voice_name or None,
                )
                if result:
                    return result
                logging.warning(f"Google Cloud TTS failed for '{text}', falling back to gTTS")
            else:
                logging.warning(f"Language '{language_code}' not supported by Google Cloud TTS, using gTTS")
        except Exception as exc:
            logging.error(f"Google Cloud TTS error: {exc}, falling back to gTTS")

    try:
        if cancellation_event and cancellation_event.is_set():
            return None
        tts = gTTS(text=text, lang=language_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tts.save(tmp_file.name)
            return tmp_file.name
    except Exception as exc:
        logging.error(f"gTTS error: {exc}")
        return None


def stop_playback():
    """Stop current playback, drain the queue and delete temp files."""
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    is_playing.clear()
    stop_event.set()

    with playback_lock:
        while not playback_queue.empty():
            try:
                item = playback_queue.get_nowait()
                playback_queue.task_done()
                filename = item[0]
                if filename not in ("STOP", ""):
                    _remove_temp_file(filename)
            except queue.Empty:
                break

    playback_queue.put(("STOP", None))

    with temp_files_lock:
        for filename in list(all_temp_files):
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                    all_temp_files.discard(filename)
                except Exception as exc:
                    logging.error(f"Error removing file: {exc}")
            else:
                all_temp_files.discard(filename)


def _remove_temp_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except Exception as exc:
            logging.error(f"Error removing file: {exc}")
            return
    with temp_files_lock:
        all_temp_files.discard(filename)


def cleanup_temp_files():
    temp_dir = tempfile.gettempdir()
    for filename in os.listdir(temp_dir):
        if filename.startswith('tmp') and filename.endswith('.mp3'):
            try:
                os.remove(os.path.join(temp_dir, filename))
            except Exception as exc:
                logging.error(f"Error removing file: {exc}")


def playback_worker():
    while True:
        filename, callback = playback_queue.get()

        if stop_event.is_set() or filename == "STOP":
            playback_queue.task_done()
            break

        try:
            with playback_lock:
                if filename in current_files:
                    pygame.mixer.music.load(filename)
                    pygame.mixer.music.play()
                    is_playing.set()

            while pygame.mixer.music.get_busy() and not stop_event.is_set():
                pygame.time.Clock().tick(10)

            if not stop_event.is_set() and is_playing.is_set():
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                is_playing.clear()

            if callback and not stop_event.is_set():
                callback()

        except Exception as exc:
            logging.error(f"Error during playback: {exc}")
        finally:
            pygame.time.wait(200)
            _remove_temp_file(filename)
            current_files.discard(filename)
            playback_queue.task_done()


def start_playback_worker():
    if not stop_event.is_set():
        threading.Thread(target=playback_worker, daemon=True).start()


def retry_request(func, *args, cancellation_event=None, logger=None, **kwargs):
    """Retry *func* with exponential backoff."""
    max_retries = 5
    for attempt in range(max_retries):
        if cancellation_event and cancellation_event.is_set():
            break
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                message = f"Error: {exc}. Retrying in {wait_time:.2f} seconds..."
                if logger:
                    logger(message, level='warning')
                else:
                    logging.error(message)
                time.sleep(wait_time)
            else:
                message = f"Max retries exceeded. Error: {exc}"
                if logger:
                    logger(message, level='error')
                else:
                    logging.error(message)
                raise


def play_next_file(file_list, callback):
    if not file_list or stop_event.is_set():
        if stop_event.is_set():
            for filename in file_list:
                _remove_temp_file(filename)
        if callback and not stop_event.is_set():
            callback()
        return

    filename = file_list.pop(0)
    current_files.add(filename)
    playback_queue.put((filename, lambda: play_next_file(file_list, callback)))
    if not is_playing.is_set():
        start_playback_worker()


def read_words_list(words, languages, callback=None, error_callback=None):
    """Synthesize and queue word/translation pairs for playback."""
    try:
        stop_event.clear()
        results = {}

        def process_word_pair(index, word_pair):
            (word, translation), (lang_word, lang_translation) = word_pair
            temp_files = []
            try:
                if stop_event.is_set():
                    return index, temp_files
                for text, lang in [(word, lang_word), (translation, lang_translation)]:
                    if stop_event.is_set():
                        return index, temp_files
                    if lang not in lang_codes:
                        logging.error(f"Unsupported language: {lang}")
                        continue
                    filename = synthesize_speech(text, lang_codes[lang], cancellation_event=stop_event)
                    if filename:
                        temp_files.append(filename)
                        with temp_files_lock:
                            all_temp_files.add(filename)
                return index, temp_files
            except Exception as exc:
                logging.error(f"Error processing word '{word}': {exc}")
                if error_callback:
                    error_callback(f"Error processing word '{word}': {exc}")
                return index, temp_files

        word_pairs_with_indices = list(enumerate(zip(words, languages)))

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(process_word_pair, idx, wp)
                       for idx, wp in word_pairs_with_indices]
            for future in concurrent.futures.as_completed(futures):
                if stop_event.is_set():
                    break
                index, temp_files_pair = future.result()
                results[index] = temp_files_pair

        temp_files_in_order = []
        for idx in sorted(results.keys()):
            temp_files_in_order.extend(results[idx])

        if not stop_event.is_set():
            play_next_file(temp_files_in_order, callback)
        else:
            with temp_files_lock:
                pending = list(all_temp_files)
            for filename in pending:
                _remove_temp_file(filename)

    except Exception as exc:
        logging.error(f"Error preparing sound: {exc}")
        if callback:
            callback()


def save_audio_file(words, file_path, languages, progress_callback=None, is_cancelled=None,
                    all_temp_files=None, logger=None, pause_duration=1000, number_of_repeats=1):
    """Render word/translation pairs into a single mp3 at *file_path*."""
    try:
        progress_lock = threading.Lock()
        rate_limit_lock = threading.Lock()
        next_available_time = [time.time()]
        results = {}
        current = 0

        settings = load_settings()
        max_concurrent_workers = get_int(settings, "max_concurrent_workers", 2)
        requests_per_sec = 1 / max(get_int(settings, "requests_per_sec", 5), 1)

        def process_word_pair(index, word_pair):
            nonlocal current
            (word, translation), (lang_word, lang_translation) = word_pair
            temp_files = []
            try:
                if is_cancelled and is_cancelled.is_set():
                    return index, temp_files

                for text, lang in [(word, lang_word), (translation, lang_translation)]:
                    if is_cancelled and is_cancelled.is_set():
                        return index, temp_files
                    if lang not in lang_codes:
                        message = f"Unsupported language: {lang} for {word_pair}"
                        if logger:
                            logger(message, level='warning')
                        logging.warning(message)
                        continue

                    provider, _, _, _ = get_tts_settings()
                    if provider == "gtts":
                        with rate_limit_lock:
                            now = time.time()
                            if now < next_available_time[0]:
                                time.sleep(next_available_time[0] - now)
                                now = time.time()
                            next_available_time[0] = now + requests_per_sec

                    filename = synthesize_speech(text, lang_codes[lang], cancellation_event=is_cancelled)
                    if is_cancelled and is_cancelled.is_set():
                        return index, temp_files
                    if filename:
                        temp_files.append(filename)
                        if all_temp_files is not None:
                            all_temp_files.add(filename)

                silent_segment = AudioSegment.silent(duration=pause_duration)
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                    silent_segment.export(tmp_file.name, format='mp3')
                    temp_files.append(tmp_file.name)
                    if all_temp_files is not None:
                        all_temp_files.add(tmp_file.name)

                with progress_lock:
                    current += 1
                    if progress_callback:
                        progress_callback(current, word)

            except Exception as exc:
                if logger:
                    logger(f"Error processing word '{word}': {exc}", level='error')
                logging.error(f"Error processing word '{word}': {exc}")
            return index, temp_files

        word_pairs_with_indices = list(enumerate(zip(words, languages)))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent_workers) as executor:
            futures = [executor.submit(process_word_pair, idx, wp)
                       for idx, wp in word_pairs_with_indices]
            for future in concurrent.futures.as_completed(futures):
                if is_cancelled and is_cancelled.is_set():
                    break
                index, temp_files = future.result()
                results[index] = temp_files

        text_segments_in_order = []
        for idx in sorted(results.keys()):
            for _ in range(number_of_repeats):
                text_segments_in_order.extend(results[idx])

        if text_segments_in_order and not (is_cancelled and is_cancelled.is_set()):
            if progress_callback:
                progress_callback('compiling_audio', None)
            combined = AudioSegment.empty()
            for segment in text_segments_in_order:
                combined += AudioSegment.from_file(segment, format="mp3")
            combined.export(file_path, format="mp3")

        for segment in text_segments_in_order:
            if os.path.exists(segment):
                try:
                    os.remove(segment)
                    if all_temp_files is not None:
                        all_temp_files.discard(segment)
                except Exception as exc:
                    if logger:
                        logger(f"Error removing file: {exc}", level='error')
            elif all_temp_files is not None:
                all_temp_files.discard(segment)

    except Exception as exc:
        if logger:
            logger(f"Error saving audio file: {exc}", level='error')
        raise


_speak_lock = threading.Lock()


def speak_word(word, language):
    """Speak a single word synchronously. Raises ValueError on bad input.

    Serialized with a lock: concurrent pygame.mixer.music access from
    multiple threads can crash SDL.
    """
    if not word.strip():
        raise ValueError("Please enter a word to speak.")
    if language not in lang_codes:
        raise ValueError(f"Unsupported language: {language}")

    filename = synthesize_speech(word, lang_codes[language])
    if not filename:
        raise RuntimeError("Failed to generate speech. Check your TTS provider settings.")

    all_temp_files.add(filename)
    with _speak_lock:
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() and not stop_event.is_set():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
        finally:
            _remove_temp_file(filename)
