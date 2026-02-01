## ============================================================
## VOICE.PY - Text-to-Speech engine using ElevenLabs
## ============================================================
## Converts text to speech and plays it.
##
## FEATURES:
## - ElevenLabs API integration
## - Structured error handling (401/429/422/timeout)
## - Rate limit retry logic
## - Text filtering (removes code blocks, markdown)
## - Skip functionality (kill playback mid-speech)
## - Subprocess-based playback (non-blocking)
##
## REQUIRES:
## - mpg123 installed (apt install mpg123)
## - Valid ELEVENLABS_API_KEY
## ============================================================

import os
import re
import time
import tempfile
import subprocess
import requests
from pathlib import Path


class VoiceEngine:
    """
    Text-to-Speech engine using ElevenLabs API.

    Example:
        voice = VoiceEngine(api_key="sk_...", voice_id="abc123")
        voice.speak("Hello you absolute drongo!")
        voice.skip()  # Kill playback
    """

    def __init__(self, config):
        """
        Initialize voice engine.

        Args:
            config: Dict with keys:
                - elevenlabs_api_key: API key
                - voice_id: Voice ID from ElevenLabs
                - voice_stability: Stability setting (0-1)
                - voice_similarity: Similarity boost (0-1)
        """
        self.api_key = config.get("elevenlabs_api_key", "")
        self.voice_id = config.get("voice_id", "twLPF55UcxNYRmxaWLAn")
        self.stability = config.get("voice_stability", 0.4)
        self.similarity = config.get("voice_similarity", 0.3)

        ## Track playing process for skip functionality
        self.process = None
        self.temp_file = None

        ## API endpoint
        self.api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

    def speak(self, text):
        """
        Convert text to speech and play it.

        Args:
            text: Text to speak

        Returns:
            bool: True if successful, False otherwise
        """
        if not text or not text.strip():
            return False

        if not self.api_key:
            print("[Voice disabled - no API key]")
            return False

        ## Filter text (remove code blocks, markdown, etc)
        clean_text = self._filter_text(text)
        # TEMP DEBUG: show what gets sent to TTS
        #print("[DEBUG TTS] Raw input text (first 200 chars):", repr(text[:200]))
        #print("[DEBUG TTS] Cleaned text (first 200 chars):", repr(clean_text[:200]))
        #print("[DEBUG TTS] Cleaned length:", len(clean_text))
        if not clean_text:
            return False

        ## Get audio from API
        audio_data = self._tts_request(clean_text)

        if not audio_data:
            return False

        ## Play audio
        return self._play_audio(audio_data)

    def skip(self):
        """
        Kill audio playback immediately.

        Called when user presses Ctrl+C to skip voice.
        """
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=1)
            except Exception:
                try:
                    self.process.kill()
                except Exception:
                    pass
            self.process = None

        ## Clean up temp file
        if self.temp_file and os.path.exists(self.temp_file):
            try:
                os.unlink(self.temp_file)
            except Exception:
                pass
            self.temp_file = None

    def is_playing(self):
        """
        Check if audio is currently playing.

        Returns:
            bool: True if playing
        """
        if self.process:
            return self.process.poll() is None
        return False

    def _filter_text(self, text):
        """
        Filter text for speech - remove code blocks, markdown, etc.

        Args:
            text: Raw text

        Returns:
            str: Cleaned text suitable for TTS
        """
        ## Remove code blocks (```...```)
        text = re.sub(r'```[\s\S]*?```', '', text)

        ## Remove inline code (`...`)
        text = re.sub(r'`[^`]*`', '', text)

        ## Remove bold/italic markers
        text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)  ## **bold**
        text = re.sub(r'\*([^*]*)\*', r'\1', text)      ## *italic*
        text = re.sub(r'__([^_]*)__', r'\1', text)      ## __bold__
        text = re.sub(r'_([^_]*)_', r'\1', text)        ## _italic_

        ## Remove lines that look like code
        lines = text.split('\n')
        filtered_lines = []
        for line in lines:
            ## Skip lines with code-like patterns
            if re.search(r'^\s*(def |class |import |from |print\(|if |for |while |return )', line):
                continue
            if re.search(r'[{};\[\]]=', line):  ## Brackets and assignment
                continue
            if line.strip().startswith('#') and not line.strip().startswith('# '):
                continue  ## Code comments (but keep markdown headers)
            filtered_lines.append(line)

        text = '\n'.join(filtered_lines)

        ## Clean up whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)  ## Max 2 newlines
        text = text.strip()

        return text

    def _tts_request(self, text, retry_count=0):
        """
        Make TTS request to ElevenLabs API.

        Args:
            text: Text to convert
            retry_count: Number of retries (for rate limiting)

        Returns:
            bytes: Audio data, or None on error
        """
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "model_id": "eleven_flash_v2_5",
            "voice_settings": {
                "stability": 0.3,
                "similarity_boost": 0.9,
                "style": 1.0,
                "use_speaker_boost": True
            }
        }
                # TEMP DEBUG: confirm what is actually sent
        #print("[DEBUG PAYLOAD] Full payload sent to ElevenLabs:")
        #print(payload)
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.content

        except requests.HTTPError as e:
            status = e.response.status_code if e.response else 0

            if status == 401:
                ## Invalid API key
                print("[Voice error: Invalid ELEVENLABS_API_KEY]")
                return None

            elif status == 429:
                ## Rate limited - retry once after wait
                if retry_count < 1:
                    print("[Voice: Rate limited - waiting 10s...]")
                    time.sleep(10)
                    return self._tts_request(text, retry_count + 1)
                else:
                    print("[Voice error: Rate limit exceeded]")
                    return None

            elif status == 422:
                ## Invalid text - try cleaning further
                print("[Voice: Text contains unsupported characters - cleaning...]")
                ## Remove all non-ASCII
                clean = ''.join(c for c in text if ord(c) < 128)
                if clean and retry_count < 1:
                    return self._tts_request(clean, retry_count + 1)
                return None

            else:
                print(f"[Voice error: HTTP {status}]")
                return None

        except requests.Timeout:
            print("[Voice error: Request timed out]")
            return None

        except requests.RequestException as e:
            print(f"[Voice error: {e}]")
            return None

    def _play_audio(self, audio_data):
        """
        Play audio data using mpg123.

        Args:
            audio_data: MP3 audio bytes

        Returns:
            bool: True if playback started
        """
        try:
            ## Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
                f.write(audio_data)
                self.temp_file = f.name

            ## Play with mpg123 (quiet mode, suppress debug output)
            ## CRITICAL: stdin=DEVNULL prevents mpg123 from stealing keyboard input
            self.process = subprocess.Popen(
                ["mpg123", "-q", self.temp_file],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            return True

        except FileNotFoundError:
            print("[Voice error: mpg123 not installed. Run: apt install mpg123]")
            return False

        except Exception as e:
            print(f"[Voice error: {e}]")
            return False

    def wait(self):
        """
        Wait for current playback to finish.
        """
        if self.process:
            try:
                self.process.wait()
            except Exception:
                pass

        ## Clean up temp file
        if self.temp_file and os.path.exists(self.temp_file):
            try:
                os.unlink(self.temp_file)
            except Exception:
                pass
            self.temp_file = None


## ============================================================
## QUICK TEST - Run this file directly to test voice
## ============================================================
if __name__ == "__main__":
    import sys

    print("Testing voice engine...")
    print("=" * 50)

    ## Load config to get API key
    from digger.config import load_config
    config = load_config()

    voice = VoiceEngine(config)

    ## Test text
    test_text = sys.argv[1] if len(sys.argv) > 1 else "G'day cunt, testing voice output."

    print(f"Speaking: {test_text}")
    print("-" * 50)

    success = voice.speak(test_text)

    if success:
        print("Waiting for playback...")
        voice.wait()
        print("Done!")
    else:
        print("Voice failed.")

    print("=" * 50)
