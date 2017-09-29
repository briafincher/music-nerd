"""Models and database functions for music database"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()

###############################################################################


class Genre(db.Model):
    """Genre model"""

    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Genre name={}>'.format(self.name)


# class Album(db.Model):
#     """Album model"""

#     __tablename__ = 'albums'

#     album_id = db.Column(db.String(50), primary_key=True, db.ForeignKey('tracks.album_id'))
#     # artists = # Array of simplified artist objects
#     name = db.Column(db.String(250), nullable=False)

#     genres = db.relationship('Genre', secondary='albums_genres', backref='albums')


# class AlbumGenre(db.Model):
#     """Association table for albums and genres"""

#     __tablename__ = 'albums_genres'

#     album_genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     album_id = db.Column(db.String(50), db.ForeignKey('albums.album_id'), nullable=False)
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)


# class Artist(db.Model):
#     """Artist model"""

#     __tablename__ = 'artists'

#     artist_id = db.Column(db.String(50), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     images =
#     popularity = db.Column(db.Integer)
#     href =
#     uri =

#     genres = db.relationship('Genre', secondary='artists_genres', backref='artists')


# class ArtistGenre(db.Model):
#     """Association table for artists and genres"""

#     __tablename__ = 'artists_genres'

#     artist_genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     artist_id = db.Column(db.String(100), db.ForeignKey('artists.artist_id'), nullable=False)
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)


class Track(db.Model):
    """"Track model"""

    __tablename__ = 'tracks'

    track_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    album_id = db.Column(db.String(50), nullable=False)  # From simplified album object
    popularity = db.Column(db.Integer, nullable=False)
    href = db.Column(db.String(250), nullable=False)
    uri = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Track name={}>'.format(self.name)


class AudioFeatures(db.Model):
    """Audio features model"""

    __tablename__ = 'audio_features'

    audio_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_id = db.Column(db.String(50), db.ForeignKey('tracks.track_id'))
    danceability = db.Column(db.Float, nullable=True)
    energy = db.Column(db.Float, nullable=True)
    key = db.Column(db.Integer, nullable=True)
    loudness = db.Column(db.Float, nullable=True)
    mode = db.Column(db.Integer, nullable=True)
    speechiness = db.Column(db.Float, nullable=True)
    acousticness = db.Column(db.Float, nullable=True)
    instrumentalness = db.Column(db.Float, nullable=True)
    liveness = db.Column(db.Float, nullable=True)
    valence = db.Column(db.Float, nullable=True)
    tempo = db.Column(db.Float, nullable=True)
    duration_ms = db.Column(db.Integer, nullable=True)
    time_signature = db.Column(db.Integer, nullable=True)

    track = db.relationship('Track', backref='audio_features')


###############################################################################
# Helper functions

# def init_app():

#     app = Flask(__name__)

def connect_to_db(app):
    """Connect the database to a Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///music2'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False
    db.app = app
    db.init_app(app)
