from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Image, Artist, ArtistGenre

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

if __name__ == '__main__':
    app.debug = True

    connect_to_db(app)
    app.run()
