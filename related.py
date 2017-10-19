from model2 import RelatedGenres, Genre
from model2 import connect_to_db, app, db

# def top_related(genre_name):

#     genre = Genre.query.filter_by(name=genre_name).first()

#     related = RelatedGenres.query.filter_by(genre1_id=genre.genre_id).all()
#     other_related = RelatedGenres.query.filter_by(genre2_id=genre.genre_id).all()

#     related.extend(other_related)

#     top_related = []
#     for relationship in related:
#         genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
#         genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()
#         top_related.append((relationship.shared_artists,
#                             genre1.name,
#                             genre2.name))
#     top_related.sort()

#     return top_related[-5:]


def top_related(genre_name):

    genre = Genre.query.filter_by(name=genre_name).first()
    related = RelatedGenres.query.filter(db.or_(RelatedGenres.genre1_id == genre.genre_id, RelatedGenres.genre2_id == genre.genre_id)).order_by(db.desc(RelatedGenres.shared_artists)).limit(5).all()

    genres = []
    for r in related:
        if r.genre1_id == genre.genre_id:
            genres.append((r.genre2_id, r.shared_artists))
        elif r.genre2_id == genre.genre_id:
            genres.append((r.genre1_id, r.shared_artists))

    return genres

if __name__ == '__main__':
    connect_to_db(app)
