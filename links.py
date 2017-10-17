from model2 import app, connect_to_db, db
from model2 import Genre, RelatedGenres, GenreAverages
import json


def add_nodes(relationships):
    """Given a list of relationships, parses nodes"""

    nodes = []

    for relationship in relationships:
        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        nodes.append({"id": genre1.name, "group": 1})
        nodes.append({"id": genre2.name, "group": 1})

    return [dict(genre) for genre in set([tuple(sorted(node.items())) for node in nodes])]


def add_links(relationships):
    """Given a list of relationships, parses links"""

    links = []

    for relationship in relationships:

        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        links.append({"source": genre1.name,
                      "target": genre2.name,
                      "value": relationship.shared_artists})

    return links


def find_genres(feature, limits):
    """Queries db for all genres that fit feature & limit criteria"""

    f = getattr(GenreAverages, feature)
    query = GenreAverages.query.filter(db.and_(f >= limits[0], f <= limits[1])).all()

    genres = set()
    for genre in query:
        genres.add(genre.genre)

    return genres


def find_relationships(genres, relationships):
    """Find all relationships for genres in given genre list"""

    results = []
    for relationship in relationships:

        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        if genre1.name in genres or genre2.name in genres:
            results.append(relationship)

    nodes = add_nodes(results)
    links = add_links(results)

    return {"nodes": nodes, "links": links}


def find_limits(feature, value):
    """Finds range for which to search genre averages table"""

    if feature == 'loudness':
        maximum = 0
        upper = -20
        lower = -40
        minimum = -60
    elif feature == 'tempo':
        maximum = 200
        upper = 150
        lower = 100
        minimum = 50
    else:
        maximum = 1
        upper = .66
        lower = .33
        minimum = 0

    if value >= upper:
        return (upper, maximum)
    if value < upper and value >= lower:
        return (lower, upper)
    if value < lower:
        return (minimum, lower)


def make_json(features):
    """Given a dictionary of features and parameters, creates a json file pulling
    from relationships in database that satisfy those parameters"""

    f = open('static/genre_maps/user_created.json', 'w')
    r = RelatedGenres.query.filter(RelatedGenres.shared_artists > 1).all()

    genres = set()

    for feature in features:
        limits = find_limits(feature, features[feature])
        result = find_genres(feature, limits)
        print len(result)
        genres = genres | result

    results = find_relationships(genres, r)

    json.dump(results, f)

    return results

if __name__ == '__main__':

    connect_to_db(app)

    r = RelatedGenres.query.filter(RelatedGenres.shared_artists > 1).all()
