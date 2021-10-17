import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='ccf3be6f194a4ad39f642e580cbd6119', client_secret='5041921bd96341cab9ea9b53aa8ea0d8')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

api_uri = 'spotify:artist:1kfWoWgCugPkyxQP8lkRlY'
# results = sp.artist_albums(api_url, album_type='album')
# albums = results['items']
results = sp.artist_top_tracks(api_uri)
print('results ', results)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()



# import configparser
# import spotipy
# import spotipy.oauth2 as oauth2
# from spotipy.oauth2 import SpotifyClientCredentials
#
#
# config = configparser.ConfigParser()
# config.read('config.cfg')
# client_id = config.get('SPOTIFY', 'CLIENT_ID')
# client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
#
# auth = oauth2.SpotifyClientCredentials(
#     client_id=client_id,
#     client_secret=client_secret
# )
#
