from model2 import RelatedGenres, Genre
from model2 import connect_to_db, app


def top_related(genre_name):

    genre = Genre.query.filter_by(name=genre_name).first()

    related = RelatedGenres.query.filter_by(genre1_id=genre.genre_id).all()
    other_related = RelatedGenres.query.filter_by(genre2_id=genre.genre_id).all()

    related.extend(other_related)

    top_related = []
    for relationship in related:
        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()
        top_related.append((relationship.shared_artists,
                            genre1.name,
                            genre2.name))
    top_related.sort()

    return top_related[-5:]

if __name__ == '__main__':
    connect_to_db(app)
