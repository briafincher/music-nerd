from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Image, Artist, ArtistGenre, RelatedGenres

from related import top_related

from random import randint

from auth_flow import create_playlist
# import spotipy
# import spotipy.util as util
from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from spotipy import oauth2, Spotify

import os

# from auth_flow import create_playlist

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

oauth = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope='playlist-modify-public')


@app.route('/')
def index():
    """Landing page"""

    return render_template('homepage.html')


# @app.route('/login-form')
# def show_login_form():
#     """Allows user to login to connect their Spotify account."""

#     return render_template('login-form.html')

@app.route('/login')
def get_access_token():
    """Gets Spotify API access token for user"""

    code = request.args.get('code')
    token = oauth.get_access_token(code)['access_token']

    sp = Spotify(auth=token)
    user = sp.me()

    session['token'] = token
    session['user'] = user

    return redirect('/')


@app.route('/login-button')
def login():
    """Oauth for Spotify API"""

    oauth_url = oauth.get_authorize_url()

     # if session['username']:
     #     os.remove('.cache-{}'.format(session['username']))

#     username = request.args.get('username')
#     session['username'] = username

#     token = util.prompt_for_user_token(username=username,
#                                        redirect_uri=SPOTIPY_REDIRECT_URI,
#                                        client_id=SPOTIPY_CLIENT_ID,
#                                        client_secret=SPOTIPY_CLIENT_SECRET,
#                                        scope='playlist-modify-public')
#     sp = spotipy.Spotify(auth=token)
#     # session['token'] = token

    return redirect(oauth_url)


@app.route('/genres')
def show_genres():
    """Genre map"""

    genres = Genre.query.all()
    genre_list = []
    for genre in genres:
        genre_list.append(genre.name)

    genre_features = {}
    for genre in genre_list:
        features = GenreAverages.query.filter_by(genre=genre).first()
        genre_features[genre] = {'acousticness': features.acousticness,
                                 'danceability': features.danceability,
                                 'duration_ms': features.duration_ms,
                                 'energy': features.energy,
                                 'instrumentalness': features.instrumentalness,
                                 'key': features.key,
                                 'liveness': features.liveness,
                                 'loudness': features.loudness,
                                 'mode': features.mode,
                                 'speechiness': features.speechiness,
                                 'tempo': features.tempo,
                                 'time_signature': features.time_signature,
                                 'valence': features.valence
                                 }

    return render_template('genre-map.html', genres=genre_features)


def find_popular_artists(artists):

    most_popular = []

    for artist in artists:
        most_popular.append((artist.popularity, artist))

    most_popular.sort()

    return most_popular[::-1]


@app.route('/genres/<genre>')
def show_genre_info(genre):
    """Genre info page"""

    genre_object = Genre.query.filter_by(name=genre).first()
    genre_id = genre_object.genre_id

    related_genres_search = top_related(genre)
    related_genres = []
    for related in related_genres_search:
        for item in related:
            if item != genre and type(item) != int:
                related_genres.append(item)

    artists = {}

    popular_artists = find_popular_artists(genre_object.artists)

    while(len(artists) < 4):
        for popularity, artist in popular_artists:
            if len(artists) == 4:
                break
            name = artist.name
            if artist.images:
                url = artist.images[0].url
            else:
                url = None
            artists[name] = url

    description = None

    if session['user']:
        playlist_uri = create_playlist(genre, session['user'])

    f = GenreAverages.query.filter_by(genre=genre).first()
    features = {'acousticness': f.acousticness,
                'danceability': f.danceability,
                'duration_ms': f.duration_ms / 60000,  # duration in minutes
                'energy': f.energy,
                'instrumentalness': f.instrumentalness,
                'key': f.key,
                'liveness': f.liveness,
                'loudness': f.loudness,
                'mode': f.mode,
                'speechiness': f.speechiness,
                'tempo': f.tempo,
                'time_signature': f.time_signature,
                'valence': f.valence
                }

    return render_template('genre-info.html',
                           genre=genre,
                           artists=artists,
                           related=related_genres,
                           features=features,
                           playlist=playlist_uri)


@app.route('/random')
def find_random_genre():
    """Takes the user to a random genre page"""

    random = randint(1, 1520)

    genre = Genre.query.filter_by(genre_id=random).first()

    name = genre.name

    return redirect('/genres/{}'.format(name))

if __name__ == '__main__':
    app.debug = True

    connect_to_db(app)
    app.run()
