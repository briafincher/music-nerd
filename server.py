from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Image, Artist, ArtistGenre, RelatedGenres

from related import top_related

from random import randint

from auth_flow import create_playlist

from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from spotipy import oauth2, Spotify

import os

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

# SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
# SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

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

    flash('You have logged in with your Spotify account!')

    print session

    return redirect('/')


@app.route('/login-button')
def login():
    """Oauth for Spotify API"""

    oauth_url = oauth.get_authorize_url()

    return redirect(oauth_url)


@app.route('/logout')
def logout():
    """Removes access token for Spotify user"""

    flash('You have been logged out!')
    session.pop('token', None)
    session.pop('user', None)

    return redirect('/')


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
                                 # 'duration_ms': features.duration_ms,
                                 'energy': features.energy,
                                 'instrumentalness': features.instrumentalness,
                                 # 'key': features.key,
                                 'liveness': features.liveness,
                                 'loudness': features.loudness,
                                 'mode': features.mode,
                                 'speechiness': features.speechiness,
                                 'tempo': features.tempo,
                                 # 'time_signature': features.time_signature,
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
    import string

    """Genre info page"""

    genre_object = Genre.query.filter_by(name=genre).first()
    genre_id = genre_object.genre_id

    related_genres_search = top_related(genre)
    related_genres = []
    for related in related_genres_search:
        for item in related:
            if item != genre and type(item) != int:
                related_genres.append({'genre': item,
                                       'capitalized': string.capwords(item)})

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
                           capitalized=string.capwords(genre),
                           artists=artists,
                           related=related_genres,
                           features=features)


@app.route('/playlist/<genre>')
def render_playlist(genre):
    """Renders a playlist of that genre's top songs"""

    print session
    playlist_uri = create_playlist(genre=genre,
                                   user=session['user']['id'],
                                   token=session['token'])

    return 'https://open.spotify.com/embed?uri={}'.format(playlist_uri)


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
