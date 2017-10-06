import pandas as pd
from model2 import GenreAverages
from model2 import connect_to_db, app


def create_dataframe(feature, genres):
    data = {'genre': [], feature: []}

    for genre in genres:
        data['genre'].append(genre.genre)
        data[feature].append(getattr(genre, feature))

    dataframe = pd.DataFrame(data, columns=['genre', feature])
    dataframe.to_csv('genre_features/{}.csv'.format(feature))

connect_to_db(app)

genres = GenreAverages.query.all()

features = ['danceability',
            'energy',
            'key',
            'loudness',
            'mode',
            'speechiness',
            'acousticness',
            'instrumentalness',
            'liveness',
            'valence',
            'tempo']

for feature in features:
    create_dataframe(feature, genres)
