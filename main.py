import ssl
import urllib.request
from voicetotextAPI import transcribe_voice_to_text
from spotifyapi import get_episodes

# Example request
# audio_url = 'https://p.scdn.co/mp3-preview/373e0c58efe56fd08cbb850d166c301a3bdd9be7'
context = ssl._create_unverified_context()
# output_file = "test.wav"
# urllib.urlopen(audio_url, context=context)
# urllib.request.urlretrieve(audio_url, output_file)

podcasts = get_episodes(['Obama'], 2)
print('audio file urls ', list(podcasts.audio_preview_url))

def get_response():
    for idx, u in enumerate(list(podcasts.audio_preview_url)):
        try:
            output_file = 'test'+str(idx)+'.wav'
            urllib.request.urlretrieve(u, output_file)
            transcribe_voice_to_text(output_file)
        except Exception:
            print('url', u, 'at index', idx, 'does not have a speech in it')
            continue

get_response()