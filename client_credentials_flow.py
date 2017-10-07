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


def genre_search(genre, limit):
    """Makes a search request to Spotify's API for the given genre.

    Returns list of top tracks for that genre.

    """

    genre_terms = genre.split(' ')
    query = '+'.join(genre_terms)

    search = sp.search(q='genre:{}'.format(query), limit=limit)

    tracks_results = search['tracks']['items']  # list of Spotify track objects

    return tracks_results


def make_tracks(tracks):
    """Makes list of track objects"""
    # import pdb

    tracks_list = []  # list of tracks

    for result in tracks:
        track = {
            'track_id': result['id'],
            'name': result['name'],
            'album_id': result['album']['id'],
            'popularity': result['popularity'],
            'href': result['href'],
            'uri': result['uri']
        }
        # pdb.set_trace()
        # print track
        tracks_list.append(track)

    return tracks_list


def track_search(track):
    """Makes a request to Spotify's API for a track object given its ID"""

    return sp.tracks(track)


# def artist_search(artists):
#     """Makes a search request to Spotify's API for the given artist"""

#     pass


def feature_search(tracks):
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


def artist_search(genre):
    """Finds artists based on a genre search"""

    # related = sp.artist_related_artists(uri)
    # artist_results = related['artists']

    tracks = genre_search(genre, 20)

    artist_list = []
    for track in tracks:
        artist_list.extend(track['artists'])

    artists = {}
    for artist_item in artist_list:
        artist = sp.artist(artist_item['uri'])
        artist_id = artist['id']
        artists[artist_id] = {'name': artist['name'],
                              'popularity': artist['popularity'],
                              'artist_id': artist_id,
                              'uri': artist['uri'],
                              'genres': artist['genres'],
                              'href': artist['href'],
                              'images': artist['images']}

    return artists


def create_playlist(genre):
    pass
