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

    # artists = db.relationship('Artist', secondary='artists_genres', backref='genres', lazy='dynamic')
    artists = db.relationship('Artist', secondary='artists_genres', backref='genres', order_by='Artist.popularity')

    def __repr__(self):
        return '<Genre name={}>'.format(self.name)


class RelatedGenres(db.Model):
    """Related genres model"""

    __tablename__ = 'related_genres'

    related_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre1_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    genre2_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    shared_artists = db.Column(db.Integer)
    pearson = db.Column(db.Float)
    kendall = db.Column(db.Float)
    spearman = db.Column(db.Float)


class TopRelatedGenres(db.Model):
    """Related genres model"""

    __tablename__ = 'top_related_genres'

    related_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre1_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    genre2_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    shared_artists = db.Column(db.Integer)
    pearson = db.Column(db.Float)
    kendall = db.Column(db.Float)
    spearman = db.Column(db.Float)


class Artist(db.Model):
    """Artist model"""

    __tablename__ = 'artists'

    artist_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    popularity = db.Column(db.Integer)
    # popularity = db.Column(db.Integer, index=True) # Use upon re-creation
    href = db.Column(db.String(250))
    uri = db.Column(db.String(250))

    images = db.relationship('Image', backref='artist')

    def __repr__(self):
        name = self.name.encode('utf8')
        return '<Artist name={}>'.format(name)


class Image(db.Model):
    """Image model"""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(200))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    artist_id = db.Column(db.String(50), db.ForeignKey('artists.artist_id'))


class ArtistGenre(db.Model):
    """Association table for artists and genres"""

    __tablename__ = 'artists_genres'

    artist_genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.String(100), db.ForeignKey('artists.artist_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)


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

    def __repr__(self):
        return '<Audio Features for track_id {}'.format(self.track_id)


class GenreAverages(db.Model):
    """Model for genres' audio features averages"""

    __tablename__ = 'genre_averages'

    genre = db.Column(db.String(50), primary_key=True)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Float)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Float)
    speechiness = db.Column(db.Float)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Float)
    time_signature = db.Column(db.Float)

    def __repr__(self):
        return "<Audio features for genre '{}'>".format(self.genre)


class Description(db.Model):
    """Model for genre descriptions"""

    __tablename__ = 'descriptions'

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), primary_key=True)
    page_name = db.Column(db.String(100), nullable=True)


###############################################################################


def connect_to_db(app):
    """Connect the database to a Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///music2'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    connect_to_db(app)
