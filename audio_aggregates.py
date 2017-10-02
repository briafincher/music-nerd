from client_credentials_flow import genre_search, track_search, make_tracks, feature_search
from model2 import app, db, connect_to_db
from model2 import Genre, Track, AudioFeatures
import pdb
import pandas as pd
from seed2 import load_audio_features


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
            danceability.append('NaN')
        try:
            energy.append(af.energy)
        except AttributeError:
            energy.append('NaN')
        try:
            key.append(af.key)
        except AttributeError:
            key.append('NaN')
        try:
            loudness.append(af.loudness)
        except AttributeError:
            loudness.append('NaN')
        try:
            mode.append(af.mode)
        except AttributeError:
            mode.append('NaN')
        try:
            speechiness.append(af.speechiness)
        except AttributeError:
            speechiness.append('NaN')
        try:
            acousticness.append(af.acousticness)
        except AttributeError:
            acousticness.append('NaN')
        try:
            instrumentalness.append(af.instrumentalness)
        except AttributeError:
            instrumentalness.append('NaN')
        try:
            liveness.append(af.liveness)
        except AttributeError:
            liveness.append('NaN')
        try:
            valence.append(af.valence)
        except AttributeError:
            valence.append('NaN')
        try:
            tempo.append(af.tempo)
        except AttributeError:
            tempo.append('NaN')
        try:
            duration_ms.append(af.duration_ms)
        except AttributeError:
            duration_ms.append('NaN')
        try:
            time_signature.append(af.time_signature)
        except AttributeError:
            time_signature.append('NaN')

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

    # pdb.set_trace()
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
    # results = get_genre_features(10)
    dataframes = {}
    stats = {}
    offset = 0
    for i in range(151):
        results = get_genre_features(10, offset)
        offset += 10

        for genre, features in results.iteritems():
            dataframes[genre] = create_dataframe(features)

        for genre, df in dataframes.iteritems():
            stats[genre] = df.describe()
