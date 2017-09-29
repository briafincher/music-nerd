from client_credentials_flow import genre_search
from model2 import app, db, connect_to_db
from model2 import Genre, Track, AudioFeatures
import pdb


def get_genre_features():

    genres = Genre.query.all()
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

if __name__ == '__main__':
    connect_to_db(app)
    results = get_genre_features()
    print results
