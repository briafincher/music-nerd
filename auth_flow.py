import os
import spotipy
# from pprint import pformat
import spotipy.util as util

os.remove('.cache-haverchucks')

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

username = 'haverchucks'

token = util.prompt_for_user_token(username=username, redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

result = sp.search(q='genre:dance+pop', limit=10)

print result