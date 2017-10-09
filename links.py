from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages, Artist, ArtistGenre, Image, RelatedGenres
from client_credentials_flow import genre_search, track_search, make_tracks, feature_search
import pdb
import pandas as pd
import numpy as np
from seed2 import load_audio_features, load_audio_aggregates


def add_nodes(relationships):

    nodes = []

    for relationship in relationships:
        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        nodes.append({'id': genre1.name, 'group': 1})
        nodes.append({'id': genre2.name, 'group': 1})

    for node in nodes:
        print node


def add_links(relationships):

    links = []

    for relationship in relationships:

        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        links.append({'source': genre1.name,
                      'target': genre2.name,
                      'value': relationship.shared_artists})

    for link in links:
        print link


if __name__ == '__main__':

    connect_to_db(app)

    relationships = RelatedGenres.query.filter(RelatedGenres.shared_artists > 0).all()

    # add_nodes(relationships)
    add_links(relationships)
