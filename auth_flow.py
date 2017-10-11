import os
import spotipy
# from pprint import pformat
import spotipy.util as util
from client_credentials_flow import genre_search
from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

os.remove('.cache-haverchucks')

# SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
# SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

SPOTIPY_CLIENT_ID = SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = SPOTIPY_REDIRECT_URI

username = 'haverchucks'

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username=username, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)

sp = spotipy.Spotify(auth=token)

# result = sp.search(q='genre:dance+pop', limit=10)


def find_playlist(name, username):

    playlists = sp.user_playlists(username)

    for playlist in playlists['items']:
        if playlist['name'] == name:
            return playlist['id']

    return None


def create_playlist(genre, username):

    playlist = find_playlist(genre, username)

    if playlist:
        return playlist

    else:
        playlist = sp.user_playlist_create(username=username,
                                           playlist_name=genre,
                                           playlist_description=genre)

        playlist_id = find_playlist(genre, username)

        search_results = genre_search(genre, 20)

        tracks = []
        for track in search_results:
            tracks.append(track['id'])

        sp.user_playlist_add_tracks(username=username,
                                    playlist_id=playlist_id,
                                    track_ids=tracks)
