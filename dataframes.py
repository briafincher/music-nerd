import pandas as pd
from model2 import GenreAverages

danceability = pd.DataFrame()
energy = pd.DataFrame()
key = pd.DataFrame()
loudness = pd.DataFrame()
mode = pd.DataFrame()
speechiness = pd.DataFrame()
acousticness = pd.DataFrame()
instrumentalness = pd.DataFrame()
liveness = pd.DataFrame()
valence = pd.DataFrame()
tempo = pd.DataFrame()

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