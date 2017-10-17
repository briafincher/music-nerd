from model2 import app, connect_to_db
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

    genres = set()
    for genre in GenreAverages.query.filter(f >= limits[1] and f <= limits[0]).all():
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

    genres = []

    for feature in features:
        limits = find_limits(feature, features[feature])
        genres.extend(find_genres(feature, limits))

    results = find_relationships(set(genres), r)

    json.dump(results, f)

    return f

# def find_filename(feature):
#     """Returns the corresponding filename for an audio feature"""

#     if feature == 'acousticness':
#         return 'static/genre_maps/acoustic.json'
#     elif feature == 'danceability':
#         return 'static/genre_maps/dancey.json'
#     elif feature == 'energy':
#         return 'static/genre_maps/energetic.json'
#     elif feature == 'instrumentalness':
#         return 'static/genre_maps/instrumental.json'
#     elif feature == 'liveness':
#         return 'static/genre_maps/live.json'
#     elif feature == 'loudness':
#         return 'static/genre_maps/loud.json'
#     elif feature == 'mode':
#         return 'static/genre_maps/mode.json'
#     elif feature == 'speechiness':
#         return 'static/genre_maps/speechy.json'
#     elif feature == 'tempo':
#         return 'static/genre_maps/tempo.json'
#     elif feature == 'valence':
#         return 'static/genre_maps/valence.json'


# def make_json(feature, limit, relationships):
#     """Given a dictionary of nodes and links, converts to json file"""

#     filename = find_filename(feature)

#     genres = find_genres(feature, limit)

#     results = find_relationships(genres, relationships)

#     f = open(filename, 'w')

#     json.dump(results, f)

if __name__ == '__main__':

    connect_to_db(app)

    r = RelatedGenres.query.filter(RelatedGenres.shared_artists > 1).all()

    # make_json('acousticness', 0.5, r)
    # make_json('danceability', 0.5, r)
    # make_json('energy', 0.5, r)
    # make_json('instrumentalness', 0.5, r)
    # make_json('liveness', 0.5, r)
    # make_json('loudness', -30, r)  # dB measured from -60 to 0
    # make_json('mode', 0.5, r)
    # make_json('speechiness', 0.66, r)
    # make_json('tempo', 115, r)
    # make_json('valence', 0.5, r)
