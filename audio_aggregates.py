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
        print i
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
        danceability.append(af.danceability)
        energy.append(af.energy)
        key.append(af.key)
        loudness.append(af.loudness)
        mode.append(af.mode)
        speechiness.append(af.speechiness)
        acousticness.append(af.acousticness)
        instrumentalness.append(af.instrumentalness)
        liveness.append(af.liveness)
        valence.append(af.valence)
        tempo.append(af.tempo)
        duration_ms.append(af.duration_ms)
        time_signature.append(af.time_signature)

    data = {'track_id': pd.Series(track_id),
            'danceability': pd.Series(danceability),
            'energy': pd.Series(energy),
            'key': pd.Series(key),
            'loudness': pd.Series(loudness),
            'mode': pd.Series(mode),
            'speechiness': pd.Series(speechiness),
            'acousticness': pd.Series(acousticness),
            'instrumentalness': pd.Series(instrumentalness),
            'liveness': pd.Series(liveness),
            'valence': pd.Series(valence),
            'tempo': pd.Series(tempo),
            'duration_ms': pd.Series(duration_ms),
            'time_signature': pd.Series(time_signature)}

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

# if __name__ == '__main__':
    connect_to_db(app)
    results = get_genre_features()

    for genre, features in results.iteritems():
        print genre
        df = create_dataframe(features)
