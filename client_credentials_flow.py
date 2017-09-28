import os
import spotipy
# from pprint import pformat
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

client_credentials_manager = SpotifyClientCredentials()

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def genre_search(genre):
    """Makes a search request to Spotify's API for the given genre.

    Returns list of top ten tracks for that genre.
    
    """

    genre_terms = genre.split(' ')
    query = '+'.join(genre_terms)

    search = sp.search(q='genre:{}'.format(query), limit=10)

    tracks_results = search['tracks']['items'] # list of Spotify track objects 
    tracks = [] # list of tracks

    for track in tracks_results:
        track_info = {
            'track_id': track['id'],
            'name': track['name'],
            'album_id': track['album']['id'],
            'popularity': track['popularity'],
            'href': track['href'],
            'uri': track['uri']
        }

        tracks.append(track_info)

    return tracks


