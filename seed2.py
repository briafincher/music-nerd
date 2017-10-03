from client_credentials_flow import genre_search, make_tracks, feature_search
from model2 import app, db, connect_to_db
# from model import connect_to_db, app
from model2 import Genre, Track, AudioFeatures, GenreAverages
import pandas
#Album, AlbumGenre, Artist, ArtistGenre, Track, AudioFeatures

# tracks = c.search['tracks']['items'] # list of track dictionaries

# for track in tracks:


def load_genres():
    """Loads genres from genre list file"""

    for row in open('genre-list.txt'):
        row = row.rstrip()
        new_genre = Genre(name=row)

        db.session.add(new_genre)

    db.session.commit()


def batch_genre_queries():
    """Batches genre queries in groups of ten"""

    import pdb

    genres = Genre.query.all()
    genre_names = []  # list of genre names
    for genre in genres:
        genre_names.append(genre.name)

    # pdb.set_trace()
    # print genre_names

    start = 0
    end = 0
    for i in range(len(genre_names)/10):
        print i
        pdb.set_trace()

        end += 10
        genre_query = genre_names[start:end]
        # print genre_query
        # pdb.set_trace()
        load_tracks(genre_query)
        start = end


def load_tracks(query):
    """Loads tracks from each genre query"""
    # import pdb
    tracks = []  # list of all tracks returned from searches of all genres
    for genre in query:
        search_results = genre_search(genre, 50)
        # pdb.set_trace()
        # print search_results
        results = make_tracks(search_results)
        # pdb.set_trace()
        # print results
        tracks.extend(results)

    # print tracks
    # pdb.set_trace()
    for track in tracks:
        track_id = track['track_id']
        name = track['name']
        album_id = track['album_id']
        popularity = track['popularity']
        href = track['href']
        uri = track['uri']

        if not Track.query.filter(Track.track_id == track_id).first():
            new_track = Track(track_id=track_id,
                              name=name,
                              album_id=album_id,
                              popularity=popularity,
                              href=href,
                              uri=uri)

            db.session.add(new_track)

    db.session.commit()


def load_audio_features(tracks):
    """Loads audio features for each track"""

    features = feature_search(tracks)

    for feature in features:
        track_id = feature['track_id']
        danceability = feature['danceability']
        energy = feature['energy']
        key = feature['key']
        loudness = feature['loudness']
        mode = feature['mode']
        speechiness = feature['speechiness']
        acousticness = feature['acousticness']
        instrumentalness = feature['instrumentalness']
        liveness = feature['liveness']
        valence = feature['valence']
        tempo = feature['tempo']
        duration_ms = feature['duration_ms']
        time_signature = feature['time_signature']

        if not AudioFeatures.query.filter(AudioFeatures.track_id == track_id).first():
            new_feature = AudioFeatures(track_id=track_id,
                                        danceability=danceability,
                                        energy=energy,
                                        key=key,
                                        loudness=loudness,
                                        mode=mode,
                                        speechiness=speechiness,
                                        acousticness=acousticness,
                                        instrumentalness=instrumentalness,
                                        liveness=liveness,
                                        valence=valence,
                                        tempo=tempo,
                                        duration_ms=duration_ms,
                                        time_signature=time_signature)

            db.session.add(new_feature)

    db.session.commit()


def batch_track_queries():
    """Batches track audio feature queries in groups of 100"""

    import pdb

    tracks = Track.query.all()
    track_ids = []  # list of track ids
    for track in tracks:
        track_ids.append(track.track_id)

    # print track_ids

    repeats = len(track_ids) / 100 + 1
    print repeats

    start = 0
    end = 0
    for i in range(repeats):
        print i
        pdb.set_trace()

        end += 100
        tracks_to_query = track_ids[start:end]
        load_audio_features(tracks_to_query)
        start = end


def load_audio_aggregates(stats):
    """Adds aggregate genre info"""

    for genre in stats:
        # mean_df = stats[genre]['mean']
        if not GenreAverages.query.filter(GenreAverages.genre == genre).first():
            genre_info = GenreAverages(genre=genre,
                                       danceability=stats[genre]['danceability'],
                                       energy=stats[genre]['energy'],
                                       key=stats[genre]['key'],
                                       loudness=stats[genre]['loudness'],
                                       mode=stats[genre]['mode'],
                                       speechiness=stats[genre]['speechiness'],
                                       acousticness=stats[genre]['acousticness'],
                                       instrumentalness=stats[genre]['instrumentalness'],
                                       liveness=stats[genre]['liveness'],
                                       valence=stats[genre]['valence'],
                                       tempo=stats[genre]['tempo'],
                                       duration_ms=stats[genre]['duration_ms'],
                                       time_signature=stats[genre]['time_signature'])
            db.session.add(genre_info)

    db.session.commit()


if __name__ == '__main__':
    # init_app()
    connect_to_db(app)
    db.create_all()

    # load_genres()
    # batch_genre_queries()
    # batch_track_queries()
    # load_audio_aggregates()
