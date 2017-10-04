from model2 import app, connect_to_db, db
from model2 import Genre, Track, AudioFeatures, GenreAverages
from client_credentials_flow import genre_search, track_search, make_tracks, feature_search
import pdb
import pandas as pd
import numpy as np
from seed2 import load_audio_features, load_audio_aggregates


    # genres = Genre.query.all()
    # genre_list = []
    # for genre in genres:
    #     genre_list.append(genre.name)

    # genre_features = {}
    # for genre in genre_list:
    #     features = GenreAverages.query.filter_by(genre=genre).first()
    #     genre_features[genre] = {'acousticness': features.acousticness,
    #                              'danceability': features.danceability,
    #                              'duration_ms': features.duration_ms,
    #                              'energy': features.energy,
    #                              'instrumentalness': features.instrumentalness,
    #                              'key': features.key,
    #                              'liveness': features.liveness,
    #                              'loudness': features.loudness,
    #                              'mode': features.mode,
    #                              'speechiness': features.speechiness,
    #                              'tempo': features.tempo,
    #                              'time_signature': features.time_signature,
    #                              'valence': features.valence
    #                              }
connect_to_db(app)


def create_dict(ranks, feature):
    feature_dict = {}
    for i, genre in enumerate(ranks):
        feature_dict[genre.genre] = {'rank': i,
                                     feature: genre.feature}

    return feature_dict

genres = GenreAverages.query.all()
# for genre in genres:
#     name = genre.genre

acousticness = GenreAverages.query.order_by(GenreAverages.acousticness).all()
acousticness_dict = create_dict(acousticness, 'acousticness')
# for i, genre in enumerate(acousticness):
#     acousticness_dict[genre.genre] = {'rank': i, 'acousticness': genre.acousticness}

danceability = GenreAverages.query.order_by(GenreAverages.danceability).all()

duration_ms = GenreAverages.query.order_by(GenreAverages.duration_ms).all()

energy = GenreAverages.query.order_by(GenreAverages.energy).all()

instrumentalness = GenreAverages.query.order_by(GenreAverages.instrumentalness).all()

key = GenreAverages.query.order_by(GenreAverages.key).all()

liveness = GenreAverages.query.order_by(GenreAverages.liveness).all()

loudness = GenreAverages.query.order_by(GenreAverages.loudness).all()

mode = GenreAverages.query.order_by(GenreAverages.mode).all()

speechiness = GenreAverages.query.order_by(GenreAverages.speechiness).all()

tempo = GenreAverages.query.order_by(GenreAverages.tempo).all()

time_signature = GenreAverages.query.order_by(GenreAverages.time_signature).all()

valence = GenreAverages.query.order_by(GenreAverages.valence).all()




# if __name__ == '__main__':

#     connect_to_db(app)
