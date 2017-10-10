from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Image, Artist, ArtistGenre, RelatedGenres

from related import top_related

from random import randint

from client_credentials_flow import create_playlist

# from auth_flow import create_playlist

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Landing page"""

    return render_template('homepage.html')


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
    # return render_template('d3.html')


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
    print genre, type(genre)
    for related in related_genres_search:
        print related
        for item in related:
            print item, type(item)
            if type(item) == 'unicode':
                related_genres.append(item)
            # WHAT IS GOING ON HERE LOL

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

    playlist = create_playlist(genre)

    return render_template('genre-info.html',
                           genre=genre,
                           artists=artists,
                           related=related_genres)


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
