import os
from google.cloud import speech

# Set the credential path
credential_path = "/Users/jyt/Downloads/service-account-key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
speech_client = speech.SpeechClient()

# Transcribe Local Media File
podcast_demo_wav = 'podcast-demo.wav'

with open(podcast_demo_wav, 'rb') as f2:
    byte_data_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

# Configure Media Files Output
config_wav = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US',
    audio_channel_count=2
)

# Transcribing the RecognitionAudio objects
response_standard_wav = speech_client.recognize(
    config=config_wav,
    audio=audio_wav
)

print(response_standard_wav)