# import os
import spotipy
# from pprint import pformat
import spotipy.util as util
from client_credentials_flow import genre_search
from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

# os.remove('.cache-haverchucks')

# SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
# SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

SPOTIPY_CLIENT_ID = SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = SPOTIPY_REDIRECT_URI

username = 'haverchucks'

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username=username,
                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   scope=scope)

sp = spotipy.Spotify(auth=token)


def find_playlist(name, username):

    playlists = sp.user_playlists(username)

    for playlist in playlists['items']:
        if playlist['name'] == name:
            return {'uri': playlist['uri'],
                    'id': playlist['id']}

    return None


def create_playlist(genre, sp):

    playlist = find_playlist(genre, username)

    if playlist:
        return playlist['uri']

    else:
        sp.trace = False
        sp.user_playlist_create(user=username,
                                name=genre)

        playlist = find_playlist(genre, username)
        playlist_id = playlist['id']
        playlist_uri = playlist['uri']

        search_results = genre_search(genre, 20)

        tracks = []
        for track in search_results:
            tracks.append(track['id'])

        sp.user_playlist_add_tracks(user=username,
                                    playlist_id=playlist_id,
                                    tracks=tracks)
        return playlist_uri
