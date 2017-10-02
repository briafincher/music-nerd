from client_credentials_flow import genre_search
from model2 import app, db, connect_to_db
from model2 import Genre, Track, AudioFeatures
import pdb
import pandas as pd


def get_genre_features(limit, offset=0):

    genres = Genre.query
    genres = genres.limit(limit).offset(offset)
    genre_names = []
    for genre in genres:
        genre_names.append(genre.name)

    genre_features = {}
    for i, name in enumerate(genre_names):
        # print i
        tracks = genre_search(name, 50)
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
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []
    time_signature = []

    for track in genre:
        af = genre[track]

        track_id.append(track)
        # pdb.set_trace()
        try:
            danceability.append(af.danceability)
        except AttributeError:
            danceability.append(None)
        try:
            energy.append(af.energy)
        except AttributeError:
            energy.append(None)
        try:
            key.append(af.key)
        except AttributeError:
            key.append(None)
        try:
            loudness.append(af.loudness)
        except AttributeError:
            loudness.append(None)
        try:
            mode.append(af.mode)
        except AttributeError:
            mode.append(None)
        try:
            speechiness.append(af.speechiness)
        except AttributeError:
            speechiness.append(None)
        try:
            acousticness.append(af.acousticness)
        except AttributeError:
            acousticness.append(None)
        try:
            instrumentalness.append(af.instrumentalness)
        except AttributeError:
            instrumentalness.append(None)
        try:
            liveness.append(af.liveness)
        except AttributeError:
            liveness.append(None)
        try:
            valence.append(af.valence)
        except AttributeError:
            valence.append(None)
        try:
            tempo.append(af.tempo)
        except AttributeError:
            tempo.append(None)
        try:
            duration_ms.append(af.duration_ms)
        except AttributeError:
            duration_ms.append(None)
        try:
            time_signature.append(af.time_signature)
        except AttributeError:
            time_signature.append(None)

    data = {'track_id': track_id,
            'danceability': danceability,
            'energy': energy,
            'key': key,
            'loudness': loudness,
            'mode': mode,
            'speechiness': speechiness,
            'acousticness': acousticness,
            'instrumentalness': instrumentalness,
            'liveness': liveness,
            'valence': valence,
            'tempo': tempo,
            'duration_ms': duration_ms,
            'time_signature': time_signature}

    df = pd.DataFrame(data, columns=['track_id',
                                     'danceability',
                                     'energy',
                                     'key',
                                     'loudness',
                                     'mode',
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
    results = get_genre_features(10)

    dataframes = {}
    for genre, features in results.iteritems():
        dataframes[genre] = create_dataframe(features)
