import os
import spotipy
# from pprint import pformat
import spotipy.util as util
from client_credentials_flow import genre_search

os.remove('.cache-haverchucks')

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

username = 'haverchucks'

token = util.prompt_for_user_token(username=username, redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

result = sp.search(q='genre:dance+pop', limit=10)


def find_playlist(name):
    pass


def create_playlist(genre):

    playlist = find_playlist(genre)

    if playlist:

        return playlist

    else:

        search_results = genre_search(genre, 20)

        tracks = []

        for track in search_results:
            tracks.append(track['id'])
    pass
