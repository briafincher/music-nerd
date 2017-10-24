from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension

from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Image, Artist, ArtistGenre, RelatedGenres, Description

from related import top_related

from random import randint

from auth_flow import create_playlist

# from secrets import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from spotipy import oauth2, Spotify

import wikipedia

import os

from links import make_json

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

oauth = oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope='playlist-modify-public')


@app.route('/')
def index():
    """Landing page"""

    return render_template('homepage.html')


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

    return redirect('/genres')


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
def show_genre_map():
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
                                 'energy': features.energy,
                                 'instrumentalness': features.instrumentalness,
                                 'liveness': features.liveness,
                                 'loudness': features.loudness,
                                 # 'mode': features.mode,
                                 'speechiness': features.speechiness,
                                 'tempo': features.tempo,
                                 'valence': features.valence
                                 }

    return render_template('genre-map.html', genres=genre_features)


@app.route('/features')
def display_features():
    """Generates graph based on user-selected audio feature parameters"""

    parameters = {}

    a_level = float(request.args.get('a-level'))
    d_level = float(request.args.get('d-level'))
    e_level = float(request.args.get('e-level'))
    i_level = float(request.args.get('i-level'))
    l_level = float(request.args.get('l-level'))
    lo_level = float(request.args.get('lo-level'))
    # m_level = float(request.args.get('m-level'))
    s_level = float(request.args.get('s-level'))
    t_level = float(request.args.get('t-level'))
    v_level = float(request.args.get('v-level'))

    if a_level != .5:
        parameters['acousticness'] = a_level
    if d_level != .5:
        parameters['danceability'] = d_level
    if e_level != .5:
        parameters['energy'] = e_level
    if i_level != .5:
        parameters['instrumentalness'] = i_level
    if l_level != .5:
        parameters['liveness'] = l_level
    if lo_level != -30:
        parameters['loudness'] = lo_level
    # if m_level != .5:
    #     parameters['mode'] = m_level
    if s_level != .5:
        parameters['speechiness'] = s_level
    if t_level != 150:
        parameters['tempo'] = t_level
    if v_level != .5:
        parameters['valence'] = v_level

    print parameters

    path = make_json(parameters)

    return path


@app.route('/genres/<genre>')
def show_genre_info(genre):
    """Genre info page"""

    import string

    genre_object = Genre.query.filter_by(name=genre).first()
    genre_id = genre_object.genre_id

    # populate related genre data
    related_genre_search = top_related(genre)
    related_genres = []
    for related, shared in related_genre_search:
        r = Genre.query.filter_by(genre_id=related).first()
        related_genres.append({'genre': r.name,
                              'capitalized': string.capwords(r.name),
                              'shared': shared})
    # if len(related_genres) < 5:
    #     for i in range(5 - len(related_genres))

    # populate top artists data
    artists = {}
    popular_artists = genre_object.artists[-6:]
    for artist in popular_artists:
        name = artist.name
        if artist.images:
            url = artist.images[0].url
        else:
            url = None
        artists[name] = url

    # pull genre description with Wikipedia API
    genre_description = Description.query.filter_by(genre_id=genre_id).first()
    if genre_description.page_name:
        description = wikipedia.summary(genre_description.page_name)
    else:
        description = None

    # populate genre audio features data
    f = GenreAverages.query.filter_by(genre=genre).first()
    features = {'acousticness': f.acousticness,
                'danceability': f.danceability,
                # 'duration_ms': f.duration_ms / 60000,  # duration in minutes
                'energy': f.energy,
                'instrumentalness': f.instrumentalness,
                # 'key': f.key,
                'liveness': f.liveness,
                'loudness': f.loudness,
                # 'mode': f.mode,
                'speechiness': f.speechiness,
                'tempo': f.tempo,
                # 'time_signature': f.time_signature,
                'valence': f.valence
                }

    return render_template('genre-info.html',
                           genre=genre,
                           capitalized=string.capwords(genre),
                           upper=genre.upper(),
                           artists=artists,
                           related=related_genres,
                           features=features,
                           description=description)


@app.route('/playlist/<genre>')
def render_playlist(genre):
    """Renders a playlist of that genre's top songs"""

    print session
    playlist_uri = create_playlist(genre=genre,
                                   user=session['user']['id'],
                                   token=session['token'])
    print playlist_uri

    return 'https://open.spotify.com/embed?uri={}'.format(playlist_uri)


@app.route('/random')
def find_random_genre():
    """Takes the user to a random genre page"""

    random = randint(1, 1520)

    genre = Genre.query.filter_by(genre_id=random).first()

    name = genre.name
    print name

    return redirect('/genres/{}'.format(name))


@app.route('/search')
def search():
    """Searches for a genre page to go to"""

    genre = request.args.get('search')

    return redirect('/genres/{}'.format(genre))


if __name__ == '__main__':
    app.debug = True

    connect_to_db(app)
    app.run(host="0.0.0.0")
