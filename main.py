import whisper
import pydub
from googletrans import Translator, LANGUAGES
from pydub import AudioSegment
import os

# Path to FFmpeg executables
pydub.AudioSegment.converter = r"D:\ffmpeg-7.1-full_build\bin\ffmpeg.exe"
pydub.AudioSegment.ffprobe = r"D:\ffmpeg-7.1-full_build\bin\ffprobe.exe"

def convert_audio_to_wav(file_path):
    """Convert mp3 or mp4 to wav format for Whisper model compatibility."""
    try:
        audio = AudioSegment.from_file(file_path)
        wav_path = "converted_audio.wav"
        audio.export(wav_path, format="wav")
        print("Audio successfully converted to WAV.")
        return wav_path
    except Exception as e:
        print(f"Error in audio conversion: {e}")
        raise

def transcribe_audio(file_path):
    """Use Whisper model to automatically detect and transcribe audio language."""
    try:
        model = whisper.load_model("base")  # Use "base" model; can use "large" for higher accuracy.
        result = model.transcribe(file_path)
        detected_language = result["language"]
        print(f"Detected Language: {detected_language}")
        print("Audio successfully transcribed.")
        return result["text"], detected_language
    except Exception as e:
        print(f"Error in transcription: {e}")
        raise

def translate_text(text, source_language, target_language):
    """Translate the transcribed text to the target language specified by the user."""
    try:
        translator = Translator()
        translated = translator.translate(text, src=source_language, dest=target_language)
        print(f"Text successfully translated to {target_language}.")
        return translated.text
    except Exception as e:
        print(f"Error in translation: {e}")
        raise

def audio_to_translated_text(file_path, target_language="en"):
    """Main function to convert audio to translated text in the user-specified language."""
    try:
        print("Converting audio...")
        wav_path = convert_audio_to_wav(file_path)

        print("Transcribing audio...")
        original_text, detected_language = transcribe_audio(wav_path)
        print(f"Transcribed Text:\n{original_text}")

        print(f"Translating text to {target_language}...")
        translated_text = translate_text(original_text, source_language=detected_language, target_language=target_language)
        print(f"Translated Text:\n{translated_text}")

        # Clean up temporary wav file
        if os.path.exists(wav_path):
            os.remove(wav_path)
            print("Temporary WAV file removed.")

        return translated_text

    except Exception as e:
        print(f"Error during processing: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = r"D:\project\PYTHON_PROJECT\Audio_Translator\flas-films-sp.mp3"
    user_target_language = input("Enter target language code (e.g., 'en' for English, 'fr' for French): ").strip().lower()

    if os.path.exists(file_path):
        translated_text = audio_to_translated_text(file_path, target_language=user_target_language)
        print("\nFinal Translated Text:\n", translated_text)
    else:
        print(f"File not found: {file_path}")




# import whisper
# import pydub
# from googletrans import Translator, LANGUAGES
# from pydub import AudioSegment
# import os

# # Path to FFmpeg executables
# pydub.AudioSegment.converter = r"D:\ffmpeg-7.1-full_build\bin\ffmpeg.exe"
# pydub.AudioSegment.ffprobe = r"D:\ffmpeg-7.1-full_build\bin\ffprobe.exe"

# def convert_audio_to_wav(file_path):
#     """Convert mp3 or mp4 to wav format for Whisper model compatibility."""
#     try:
#         audio = AudioSegment.from_file(file_path)
#         wav_path = "converted_audio.wav"
#         audio.export(wav_path, format="wav")
#         print("Audio successfully converted to WAV.")
#         return wav_path
#     except Exception as e:
#         print(f"Error in audio conversion: {e}")
#         raise

# def transcribe_audio(file_path):
#     """Use Whisper model to automatically detect and transcribe audio language."""
#     try:
#         model = whisper.load_model("large")  # Use "base" model; can use "large" for higher accuracy.
#         result = model.transcribe(file_path)
#         detected_language = result["language"]
#         print(f"Detected Language: {detected_language}")
#         print("Audio successfully transcribed.")
#         return result["text"], detected_language
#     except Exception as e:
#         print(f"Error in transcription: {e}")
#         raise

# def translate_text(text, source_language, target_language="en"):
#     """Translate the transcribed text to the target language."""
#     try:
#         translator = Translator()
#         translated = translator.translate(text, src=source_language, dest=target_language)
#         print("Text successfully translated.")
#         return translated.text
#     except Exception as e:
#         print(f"Error in translation: {e}")
#         raise

# def audio_to_translated_text(file_path):
#     """Main function to convert audio to English-translated text."""
#     try:
#         print("Converting audio...")
#         wav_path = convert_audio_to_wav(file_path)

#         print("Transcribing audio...")
#         original_text, detected_language = transcribe_audio(wav_path)
#         print(f"Transcribed Text:\n{original_text}")

#         print("Translating text to English...")
#         translated_text = translate_text(original_text, source_language=detected_language, target_language="en")
#         print(f"Translated Text:\n{translated_text}")

#         # Clean up temporary wav file
#         if os.path.exists(wav_path):
#             os.remove(wav_path)
#             print("Temporary WAV file removed.")

#         return translated_text

#     except Exception as e:
#         print(f"Error during processing: {e}")
#         return None

# # Example usage
# if __name__ == "__main__":
#     file_path = r"D:\project\PYTHON_PROJECT\Audio_Translator\Hindi_Female_3.mp3"

#     if os.path.exists(file_path):
#         translated_text = audio_to_translated_text(file_path)
#         print("\nFinal Translated Text:\n", translated_text)
#     else:
#         print(f"File not found: {file_path}")
