from client_credentials_flow import genre_search, track_search, make_tracks, feature_search
from model2 import app, db, connect_to_db
from model2 import Genre, Track, AudioFeatures
import pdb
import pandas as pd
import numpy as np
from seed2 import load_audio_features, load_audio_aggregates


def get_genre_features(limit, offset=0):

    genres = Genre.query
    genres = genres.limit(limit).offset(offset)
    genre_names = []
    for genre in genres:
        genre_names.append(genre.name)

    genre_features = {}
    for i, name in enumerate(genre_names):
        # print i

        tracks = genre_search(name, 50)  # imperfect, because spotify's search results are dynamic. thus, a track might not be in the audio features table
        # pdb.set_trace()

        track_ids = []
        for track in tracks:
            track_ids.append(track['id'])
        # print track_ids
        # pdb.set_trace()

        features = {}
        for track_id in track_ids:
            features[track_id] = AudioFeatures.query.filter(AudioFeatures.track_id == track_id).first()

        genre_features[name] = features
        # print genre_features[name]
        # pdb.set_trace()

    return genre_features
    # need to find way to save these genre features


def create_dataframe(genre):

    track_id = []
    danceability = []
    energy = []
    key = []
    loudness = []
    modes = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []
    time_signature = []

    for track in genre:
        track_id.append(track)
        # if not AudioFeatures.query.filter_by(track_id=track).all():
        #     pdb.set_trace() # running into error with track_search function returning actual track object
        #     track = track_search(track)
        #     track = make_tracks(track)
        #     features = feature_search(track)
        #     af = load_audio_features(features)

        #     new_track = Track(track_id=track['track_id'],
        #                       name=track['name'],
        #                       album_id=track['album_id'],
        #                       popularity=track['popularity'],
        #                       href=track['href'],
        #                       uri=track['uri'])

        #     db.session.add(new_track)
        #     db.session.commit()
        # else:
        af = genre[track]

        #     track_id.append(track)
        #     danceability.append(af.danceability)
        #     energy.append(af.energy)
        #     key.append(af.key)
        #     loudness.append(af.loudness)
        #     mode.append(af.mode)
        #     speechiness.append(af.speechiness)
        #     acousticness.append(af.acousticness)
        #     instrumentalness.append(af.instrumentalness)
        #     liveness.append(af.liveness)
        #     valence.append(af.valence)
        #     tempo.append(af.tempo)
        #     duration_ms.append(af.duration_ms)
        #     time_signature.append(af.time_signature)

        # pdb.set_trace()
        try:
            danceability.append(af.danceability)
        except AttributeError:
            danceability.append(np.nan)
        try:
            energy.append(af.energy)
        except AttributeError:
            energy.append(np.nan)
        try:
            key.append(af.key)
        except AttributeError:
            key.append(np.nan)
        try:
            loudness.append(af.loudness)
        except AttributeError:
            loudness.append(np.nan)
        try:
            modes.append(af.mode)
        except AttributeError:
            modes.append(np.nan)
        try:
            speechiness.append(af.speechiness)
        except AttributeError:
            speechiness.append(np.nan)
        try:
            acousticness.append(af.acousticness)
        except AttributeError:
            acousticness.append(np.nan)
        try:
            instrumentalness.append(af.instrumentalness)
        except AttributeError:
            instrumentalness.append(np.nan)
        try:
            liveness.append(af.liveness)
        except AttributeError:
            liveness.append(np.nan)
        try:
            valence.append(af.valence)
        except AttributeError:
            valence.append(np.nan)
        try:
            tempo.append(af.tempo)
        except AttributeError:
            tempo.append(np.nan)
        try:
            duration_ms.append(af.duration_ms)
        except AttributeError:
            duration_ms.append(np.nan)
        try:
            time_signature.append(af.time_signature)
        except AttributeError:
            time_signature.append(np.nan)

    data = {'track_id': track_id,
            'danceability': danceability,
            'energy': energy,
            'key': key,
            'loudness': loudness,
            'modes': modes,
            'speechiness': speechiness,
            'acousticness': acousticness,
            'instrumentalness': instrumentalness,
            'liveness': liveness,
            'valence': valence,
            'tempo': tempo,
            'duration_ms': duration_ms,
            'time_signature': time_signature}

    # pdb.set_trace()
    df = pd.DataFrame(data, columns=['track_id',
                                     'danceability',
                                     'energy',
                                     'key',
                                     'loudness',
                                     'modes',
                                     'speechiness',
                                     'acousticness',
                                     'instrumentalness',
                                     'liveness',
                                     'valence',
                                     'tempo',
                                     'duration_ms',
                                     'time_signature'])

    return df

if __name__ == '__main__':
    connect_to_db(app)
    # results = get_genre_features(10)
    dataframes = {}

    offset = 0
    offset = 1510
    # for i in range(151):
    stats = {}
        # print i
        # pdb.set_trace()
    results = get_genre_features(10, offset)
        # offset += 10

    for genre, features in results.iteritems():
        dataframes[genre] = create_dataframe(features)

    for genre, df in dataframes.iteritems():
        mean = df.mean()
        std = df.std()
        stats[genre] = {'genre': genre,
                        'danceability': mean.danceability,
                        'energy': mean.energy,
                        'key': mean.key,
                        'loudness': mean.loudness,
                        'mode': mean.modes,
                        'speechiness': mean.speechiness,
                        'acousticness': mean.acousticness,
                        'instrumentalness': mean.instrumentalness,
                        'liveness': mean.liveness,
                        'valence': mean.valence,
                        'tempo': mean.tempo,
                        'duration_ms': mean.duration_ms,
                        'time_signature': mean.time_signature
                        }

    load_audio_aggregates(stats)


    # print stats
