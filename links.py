from model2 import app, connect_to_db
from model2 import Genre, RelatedGenres, GenreAverages
import json
import pdb


def add_nodes(relationships):

    nodes = []

    for relationship in relationships:
        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        nodes.append({"id": genre1.name, "group": 1})
        nodes.append({"id": genre2.name, "group": 1})

    return [dict(genre) for genre in set([tuple(sorted(node.items())) for node in nodes])]


def add_links(relationships):

    links = []

    for relationship in relationships:

        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        links.append({"source": genre1.name,
                      "target": genre2.name,
                      "value": relationship.shared_artists})

    # for link in links:
    #     print link

    return links


def find_genres(feature, limit):
    """Queries db for all genres that fit feature & limit criteria"""

    f = getattr(GenreAverages, feature)

    genres = set()
    for genre in GenreAverages.query.filter(f >= limit).all():
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


def find_filename(feature):
    """Returns the corresponding filename for an audio feature"""

    if feature == 'acousticness':
        return 'static/genre_maps/acoustic.json'
    elif feature == 'danceability':
        return 'static/genre_maps/dancey.json'
    elif feature == 'energy':
        return 'static/genre_maps/energetic.json'
    elif feature == 'instrumentalness':
        return 'static/genre_maps/instrumental.json'
    elif feature == 'liveness':
        return 'static/genre_maps/live.json'
    elif feature == 'loudness':
        return 'static/genre_maps/loud.json'
    elif feature == 'mode':
        return 'static/genre_maps/mode.json'
    elif feature == 'speechiness':
        return 'static/genre_maps/speechy.json'
    elif feature == 'tempo':
        return 'static/genre_maps/tempo.json'
    elif feature == 'valence':
        return 'static/genre_maps/valence.json'


def make_json(feature, limit, relationships):
    """Given a dictionary of nodes and links, converts to json file"""

    filename = find_filename(feature)

    genres = find_genres(feature, limit)

    results = find_relationships(genres, relationships)

    f = open(filename, 'w')

    json.dump(results, f)

if __name__ == '__main__':

    connect_to_db(app)

    r = RelatedGenres.query.filter(RelatedGenres.shared_artists > 0).all()

    # nodes = add_nodes(relationships)
    # links = add_links(relationships)

    # genres = json.dumps({"nodes": nodes,
    #                      "links": links})

    # print genres

    make_json('acousticness', 0.5, r, 'static/genre_maps/acoustic.json')
    make_json('danceability', 0.5, r, 'static/genre_maps/dancey.json')
    make_json('energy', 0.5, r, 'static/genre_maps/energetic.json')
    make_json('instrumentalness', 0.5, r, 'static/genre_maps/instrumental.json')
    make_json('liveness', 0.5, r, 'static/genre_maps/live.json')
    make_json('loudness', 0.5, r, 'static/genre_maps/loud.json')
    make_json('mode', 0.5, r, 'static/genre_maps/mode.json')
    make_json('speechiness', 0.5, r, 'static/genre_maps/speechy.json')
    make_json('tempo', 0.5, r, 'static/genre_maps/tempo.json')
    make_json('valence', 0.5, r, 'static/genre_maps/valence.json')

    # feature = 'acousticness'
    # limit = 0.5
    # genres = find_genres(feature, limit)
    # results = find_relationships(genres, relationships)
    # f = open('static/genre_maps/acoustic.json', 'w')
    # json.dump(results, f)
