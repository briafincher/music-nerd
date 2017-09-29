# import os
import spotipy
# from pprint import pformat
from spotipy.oauth2 import SpotifyClientCredentials

# SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
# SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

# SPOTIPY_CLIENT_ID = 'aae1d1323f2548b0a2c612e1e2ce516e'
# SPOTIPY_CLIENT_SECRET = '5270b54d98e7461ebb1ea950c9e5a8ca'
# SPOTIPY_REDIRECT_URI = 'http://localhost:5000/'

client_credentials_manager = SpotifyClientCredentials(client_id='aae1d1323f2548b0a2c612e1e2ce516e',
                                                      client_secret='5270b54d98e7461ebb1ea950c9e5a8ca')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def genre_search(genre):
    """Makes a search request to Spotify's API for the given genre.

    Returns list of top ten tracks for that genre.

    """

    genre_terms = genre.split(' ')
    query = '+'.join(genre_terms)

    search = sp.search(q='genre:{}'.format(query), limit=10)

    tracks_results = search['tracks']['items']  # list of Spotify track objects

    return tracks_results


def make_tracks(tracks):
    """Makes list of track objects"""
    tracks = []  # list of tracks

    for result in tracks:
        track = {
            'track_id': result['id'],
            'name': result['name'],
            'album_id': result['album']['id'],
            'popularity': result['popularity'],
            'href': result['href'],
            'uri': result['uri']
        }

        tracks.append(track)

    return tracks


def track_search(tracks):
    """Makes a request to Spotify's API for tracks' audio features given list
    of track ids."""

    features_results = sp.audio_features(tracks)

    features = []
    for result in features_results:
        feature = {
            'track_id': result['id'],
            'danceability': result['danceability'],
            'energy': result['energy'],
            'key': result['key'],
            'loudness': result['loudness'],
            'mode': result['mode'],
            'speechiness': result['speechiness'],
            'acousticness': result['acousticness'],
            'instrumentalness': result['instrumentalness'],
            'liveness': result['liveness'],
            'valence': result['valence'],
            'tempo': result['tempo'],
            'duration_ms': result['duration_ms'],
            'time_signature': result['time_signature'],
        }

        features.append(feature)

    return features
