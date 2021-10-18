import configparser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

episode = sp.search(q='data',
                    type='episode',
                    market='US',
                    limit=1,
                    offset=0)

print(json.dumps(episode, indent=2))

def get_episodes(queries, total):
    name = []
    # description = []
    duration = []
    explicit = []
    language = []
    release_date = []
    url = []
    audio_preview_url = []

    if total <= 50:
        limit = total
    else:
        limit = 50

    for q in queries:
        for i in range(0, total, limit):
            results = sp.search(q=q,
                                type='episode',
                                market='US',
                                limit=limit,
                                offset=i)
            for i, t in enumerate(results['episodes']['items']):
                name.append(t['name'])
                # description.append(t['description'])
                duration.append(t['duration_ms'])
                explicit.append(t['explicit'])
                language.append(t['language'])
                audio_preview_url.append(t['audio_preview_url'])
                release_date.append(t['release_date'])
                url.append(t['external_urls']['spotify'])

    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.expand_frame_repr', False)

    dataframe = pd.DataFrame({'Name' : name,
                              'Duration': duration,
                              'Language': language,
                              'Explicit': explicit,
                              'Release Date': release_date,
                              'audio_preview_url' : audio_preview_url,
                              'URL' : url,
                              }).drop_duplicates().reset_index(drop = True)

    return dataframe
    # json.dumps(results)
    # print('-------------------------------------------------------------------------------------------')
    # print(json.dumps(results))
    # for r in results:
    #     # print(r['episodes']['items'][9]["name"])
    #     print(json.dumps(r['episodes']['items'][0]['audio_preview_url'], indent=2))

print(get_episodes(['sad'], 2))



def get_top_10_tracks():
    api_url = 'spotify:artist:1kfWoWgCugPkyxQP8lkRlY'
    results = sp.artist_top_tracks(api_url)
    # albums = results['items']
    print('results ', results)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()

get_top_10_tracks()