from model2 import db, connect_to_db, app
from model2 import Genre, RelatedGenres, GenreAverages, TopRelatedGenres, ArtistGenre
import pdb


def locate_in_db(genre):

    one = TopRelatedGenres.query.filter_by(genre1_id=genre.genre_id).all()
    two = TopRelatedGenres.query.filter_by(genre2_id=genre.genre_id).all()

    one.extend(two)

    return one


def create_links(links, data):

    for relationship in data:

        genre1_id = relationship.genre1_id
        genre1 = Genre.query.filter_by(genre_id=genre1_id).first().name

        genre2_id = relationship.genre2_id
        genre2 = Genre.query.filter_by(genre_id=genre2_id).first().name

        shared_artists = relationship.shared_artists

        links.append({'source': '{}'.format(genre1),
                      'target': '{}'.format(genre2),
                      'value': shared_artists
                      })

if __name__ == '__main__':
    connect_to_db(app)

    genre_names = []
    for line in open('extra.txt'):
        name = line.rstrip()
        genre_names.append(name)

    genres = []
    for name in genre_names[:500]:
        genre = Genre.query.filter_by(name=name).first()
        genres.append(genre)

    genre_data = {}
    for genre in genres:
        genre_data[genre.name] = locate_in_db(genre)

    print genre_data

    # links = []
    # for i, genre in enumerate(genre_data):
    #     pdb.set_trace()
    #     print i
    #     create_links(links, genre_data[genre])

    # print links
