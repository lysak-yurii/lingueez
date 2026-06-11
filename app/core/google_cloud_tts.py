"""
Google Cloud Text-to-Speech API integration module.

This module provides functions to convert text to speech using Google Cloud TTS API.
It supports both Standard and WaveNet voices and includes language code mapping
from the app's language format to Google Cloud TTS format.
"""

import os
import logging
import tempfile
from typing import Optional, Tuple
from google.cloud import texttospeech
from google.oauth2 import service_account
from google.api_core import exceptions as google_exceptions


# Language code mapping from app's lang_codes to Google Cloud TTS language codes
# Format: app_language_code -> (google_cloud_language_code, voice_name_prefix)
LANGUAGE_CODE_MAPPING = {
    'en': ('en-US', 'en-US'),
    'de': ('de-DE', 'de-DE'),
    'es': ('es-ES', 'es-ES'),
    'uk': ('uk-UA', 'uk-UA'),
    'fr': ('fr-FR', 'fr-FR'),
    'it': ('it-IT', 'it-IT'),
    'pt': ('pt-PT', 'pt-PT'),
    'ru': ('ru-RU', 'ru-RU'),
    'el': ('el-GR', 'el-GR'),
    'ar': ('ar-XA', 'ar-XA'),
    'bn': ('bn-IN', 'bn-IN'),
    'zh-HK': ('zh-HK', 'zh-HK'),
    'hi': ('hi-IN', 'hi-IN'),
    'ja': ('ja-JP', 'ja-JP'),
    'ko': ('ko-KR', 'ko-KR'),
    'zh-CN': ('zh-CN', 'zh-CN'),
    'pl': ('pl-PL', 'pl-PL'),
    'tr': ('tr-TR', 'tr-TR'),
    'vi': ('vi-VN', 'vi-VN'),
    'af': ('af-ZA', 'af-ZA'),
    'sq': ('sq-AL', 'sq-AL'),
    'am': ('am-ET', 'am-ET'),
    'hy': ('hy-AM', 'hy-AM'),
    'az': ('az-AZ', 'az-AZ'),
    'eu': ('eu-ES', 'eu-ES'),
    'be': ('be-BY', 'be-BY'),
    'bs': ('bs-BA', 'bs-BA'),
    'bg': ('bg-BG', 'bg-BG'),
    'ca': ('ca-ES', 'ca-ES'),
    'ceb': ('ceb-PH', 'ceb-PH'),
    'ny': ('ny-MW', 'ny-MW'),
    'hr': ('hr-HR', 'hr-HR'),
    'cs': ('cs-CZ', 'cs-CZ'),
    'da': ('da-DK', 'da-DK'),
    'nl': ('nl-NL', 'nl-NL'),
    'et': ('et-EE', 'et-EE'),
    'fil': ('fil-PH', 'fil-PH'),
    'fi': ('fi-FI', 'fi-FI'),
    'gl': ('gl-ES', 'gl-ES'),
    'ka': ('ka-GE', 'ka-GE'),
    'gu': ('gu-IN', 'gu-IN'),
    'ht': ('ht-HT', 'ht-HT'),
    'ha': ('ha-NG', 'ha-NG'),
    'haw': ('haw-US', 'haw-US'),
    'he': ('he-IL', 'he-IL'),
    'hmn': ('hmn-CN', 'hmn-CN'),
    'hu': ('hu-HU', 'hu-HU'),
    'is': ('is-IS', 'is-IS'),
    'ig': ('ig-NG', 'ig-NG'),
    'id': ('id-ID', 'id-ID'),
    'ga': ('ga-IE', 'ga-IE'),
    'jv': ('jv-ID', 'jv-ID'),
    'kn': ('kn-IN', 'kn-IN'),
    'kk': ('kk-KZ', 'kk-KZ'),
    'km': ('km-KH', 'km-KH'),
    'rw': ('rw-RW', 'rw-RW'),
    'ky': ('ky-KG', 'ky-KG'),
    'lo': ('lo-LA', 'lo-LA'),
    'la': ('la-LA', 'la-LA'),
    'lv': ('lv-LV', 'lv-LV'),
    'lt': ('lt-LT', 'lt-LT'),
    'lb': ('lb-LU', 'lb-LU'),
    'mk': ('mk-MK', 'mk-MK'),
    'mg': ('mg-MG', 'mg-MG'),
    'ms': ('ms-MY', 'ms-MY'),
    'ml': ('ml-IN', 'ml-IN'),
    'mt': ('mt-MT', 'mt-MT'),
    'mi': ('mi-NZ', 'mi-NZ'),
    'mr': ('mr-IN', 'mr-IN'),
    'mn': ('mn-MN', 'mn-MN'),
    'my': ('my-MM', 'my-MM'),
    'ne': ('ne-NP', 'ne-NP'),
    'no': ('no-NO', 'no-NO'),
    'or': ('or-IN', 'or-IN'),
    'ps': ('ps-AF', 'ps-AF'),
    'fa': ('fa-IR', 'fa-IR'),
    'pa': ('pa-IN', 'pa-IN'),
    'ro': ('ro-RO', 'ro-RO'),
    'sm': ('sm-WS', 'sm-WS'),
    'gd': ('gd-GB', 'gd-GB'),
    'sr': ('sr-RS', 'sr-RS'),
    'st': ('st-ZA', 'st-ZA'),
    'sn': ('sn-ZW', 'sn-ZW'),
    'sd': ('sd-PK', 'sd-PK'),
    'si': ('si-LK', 'si-LK'),
    'sk': ('sk-SK', 'sk-SK'),
    'sl': ('sl-SI', 'sl-SI'),
    'so': ('so-SO', 'so-SO'),
    'su': ('su-ID', 'su-ID'),
    'sw': ('sw-KE', 'sw-KE'),
    'sv': ('sv-SE', 'sv-SE'),
    'tg': ('tg-TJ', 'tg-TJ'),
    'ta': ('ta-IN', 'ta-IN'),
    'tt': ('tt-RU', 'tt-RU'),
    'te': ('te-IN', 'te-IN'),
    'th': ('th-TH', 'th-TH'),
    'tk': ('tk-TM', 'tk-TM'),
    'ur': ('ur-PK', 'ur-PK'),
    'ug': ('ug-CN', 'ug-CN'),
    'uz': ('uz-UZ', 'uz-UZ'),
    'cy': ('cy-GB', 'cy-GB'),
    'xh': ('xh-ZA', 'xh-ZA'),
    'yi': ('yi-IL', 'yi-IL'),
    'yo': ('yo-NG', 'yo-NG'),
    'zu': ('zu-ZA', 'zu-ZA'),
}

# Default voice names for common languages (Standard voices)
DEFAULT_VOICES = {
    'en-US': 'en-US-Standard-B',
    'de-DE': 'de-DE-Standard-B',
    'es-ES': 'es-ES-Standard-A',
    'fr-FR': 'fr-FR-Standard-A',
    'it-IT': 'it-IT-Standard-A',
    'pt-PT': 'pt-PT-Standard-A',
    'ru-RU': 'ru-RU-Standard-A',
    'ja-JP': 'ja-JP-Standard-A',
    'ko-KR': 'ko-KR-Standard-A',
    'zh-CN': 'zh-CN-Standard-A',
    'pl-PL': 'pl-PL-Standard-A',
    'tr-TR': 'tr-TR-Standard-A',
    'vi-VN': 'vi-VN-Standard-A',
}

# Default WaveNet voice names
DEFAULT_WAVENET_VOICES = {
    'en-US': 'en-US-Wavenet-D',
    'de-DE': 'de-DE-Wavenet-B',
    'es-ES': 'es-ES-Wavenet-B',
    'fr-FR': 'fr-FR-Wavenet-B',
    'it-IT': 'it-IT-Wavenet-A',
    'pt-PT': 'pt-PT-Wavenet-B',
    'ru-RU': 'ru-RU-Wavenet-D',
    'ja-JP': 'ja-JP-Wavenet-B',
    'ko-KR': 'ko-KR-Wavenet-A',
    'zh-CN': 'zh-CN-Wavenet-A',
    'pl-PL': 'pl-PL-Wavenet-A',
    'tr-TR': 'tr-TR-Wavenet-A',
    'vi-VN': 'vi-VN-Wavenet-A',
}


class GoogleCloudTTSClient:
    """Wrapper class for Google Cloud TTS client."""
    
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Google Cloud TTS client.
        
        Args:
            credentials_path: Path to Google Cloud service account JSON file.
                           If None, uses default credentials from environment.
        """
        self.client = None
        self.credentials_path = credentials_path
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Google Cloud TTS client."""
        try:
            if self.credentials_path and os.path.exists(self.credentials_path):
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path
                )
                self.client = texttospeech.TextToSpeechClient(credentials=credentials)
            else:
                # Try to use default credentials from environment
                self.client = texttospeech.TextToSpeechClient()
            logging.info("Google Cloud TTS client initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize Google Cloud TTS client: {e}")
            self.client = None
            raise
    
    def is_available(self) -> bool:
        """Check if the client is available and initialized."""
        return self.client is not None
    
    def synthesize_speech(
        self,
        text: str,
        language_code: str,
        voice_type: str = 'standard',
        voice_name: Optional[str] = None,
        output_file: Optional[str] = None
    ) -> Optional[str]:
        """
        Synthesize speech from text using Google Cloud TTS.
        
        Args:
            text: Text to convert to speech
            language_code: Language code in format 'lang-REGION' (e.g., 'en-US')
            voice_type: 'standard' or 'wavenet'
            voice_name: Optional specific voice name. If None, uses default for language.
            output_file: Optional output file path. If None, creates temporary file.
        
        Returns:
            Path to the generated audio file, or None if synthesis failed.
        """
        if not self.client:
            raise ValueError("Google Cloud TTS client is not initialized")
        
        try:
            # Prepare synthesis input
            synthesis_input = texttospeech.SynthesisInput(text=text)
            
            # Determine voice name
            if voice_name:
                selected_voice = voice_name
            else:
                if voice_type.lower() == 'wavenet':
                    selected_voice = DEFAULT_WAVENET_VOICES.get(
                        language_code,
                        f"{language_code}-Wavenet-A"
                    )
                else:
                    selected_voice = DEFAULT_VOICES.get(
                        language_code,
                        f"{language_code}-Standard-A"
                    )
            
            # Configure voice
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,
                name=selected_voice,
            )
            
            # Configure audio
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            
            # Perform synthesis
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            # Save to file
            if output_file:
                output_path = output_file
            else:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                    output_path = tmp_file.name
            
            with open(output_path, 'wb') as out:
                out.write(response.audio_content)
            
            logging.debug(f"Google Cloud TTS: Generated audio file: {output_path}")
            return output_path
            
        except google_exceptions.PermissionDenied as e:
            logging.error(f"Google Cloud TTS permission denied: {e}")
            raise ValueError(f"Permission denied. Please check your credentials: {e}")
        except google_exceptions.InvalidArgument as e:
            logging.error(f"Google Cloud TTS invalid argument: {e}")
            raise ValueError(f"Invalid language or voice configuration: {e}")
        except Exception as e:
            logging.error(f"Google Cloud TTS synthesis error: {e}")
            raise


def get_google_cloud_language_code(app_language_code: str) -> Optional[Tuple[str, str]]:
    """
    Convert app's language code to Google Cloud TTS language code.
    
    Args:
        app_language_code: Language code from app's lang_codes dictionary
    
    Returns:
        Tuple of (google_cloud_language_code, voice_prefix) or None if not supported
    """
    return LANGUAGE_CODE_MAPPING.get(app_language_code)


def create_tts_client(credentials_path: Optional[str] = None) -> Optional[GoogleCloudTTSClient]:
    """
    Create and return a Google Cloud TTS client instance.
    
    Args:
        credentials_path: Path to service account JSON file
    
    Returns:
        GoogleCloudTTSClient instance or None if initialization failed
    """
    try:
        return GoogleCloudTTSClient(credentials_path)
    except Exception as e:
        logging.error(f"Failed to create Google Cloud TTS client: {e}")
        return None


def synthesize_text_to_speech(
    text: str,
    app_language_code: str,
    credentials_path: Optional[str] = None,
    voice_type: str = 'standard',
    voice_name: Optional[str] = None,
    output_file: Optional[str] = None
) -> Optional[str]:
    """
    High-level function to synthesize speech from text.
    
    Args:
        text: Text to convert to speech
        app_language_code: Language code from app's lang_codes dictionary
        credentials_path: Path to Google Cloud service account JSON file
        voice_type: 'standard' or 'wavenet'
        voice_name: Optional specific voice name
        output_file: Optional output file path
    
    Returns:
        Path to generated audio file or None if synthesis failed
    """
    # Convert language code
    lang_mapping = get_google_cloud_language_code(app_language_code)
    if not lang_mapping:
        logging.warning(f"Language code {app_language_code} not supported by Google Cloud TTS")
        return None
    
    google_lang_code = lang_mapping[0]
    
    # Create client and synthesize
    try:
        client = create_tts_client(credentials_path)
        if not client or not client.is_available():
            return None
        
        return client.synthesize_speech(
            text=text,
            language_code=google_lang_code,
            voice_type=voice_type,
            voice_name=voice_name,
            output_file=output_file
        )
    except Exception as e:
        logging.error(f"Error synthesizing speech with Google Cloud TTS: {e}")
        return None

