from client_credentials_flow import genre_search
from model import app, db, connect_to_db
# from model import connect_to_db, app
from model import Genre, Track 
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


def load_tracks(query):
    """Loads tracks from each genre query"""

    tracks = [] # list of all tracks returned from searches of all genres
    for genre in query:
        search_results = genre_search(genre)
        tracks.extend(search_results)
        

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


def batch_genre_queries():
    """Batches genre queries in groups of ten"""

    # import pdb

    genres = Genre.query.all()
    genre_names = [] # list of genre names
    for genre in genres: 
        genre_names.append(genre.name)

    start = 0
    end = 0
    for i in range(len(genre_names)/10):
        # print i
        # pdb.set_trace()

        end += 10
        genre_query = genre_names[start:end]
        load_tracks(genre_query)
        start = end


if __name__ == '__main__':
    # init_app()
    connect_to_db(app)
    db.create_all()

    load_genres()
    batch_genre_queries()








