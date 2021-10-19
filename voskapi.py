
import urllib.request
# from spotifyapi import get_episodes

# res = get_episodes('a', 1)
# url = res['audio_preview_url']
def test():
    test_url = 'https://p.scdn.co/mp3-preview/373e0c58efe56fd08cbb850d166c301a3bdd9be7.mp3'
    output_file = "test.mp3"
    urllib.request.urlretrieve(test_url, output_file)

test()