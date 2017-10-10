from model2 import app, connect_to_db
from model2 import Genre, RelatedGenres
import json


def add_nodes(relationships):

    nodes = []

    for relationship in relationships:
        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        if genre1.name not in nodes:
            nodes.append({'id': genre1.name, 'group': 1})
        if genre2.name not in nodes:
            nodes.append({'id': genre2.name, 'group': 1})

    # for node in nodes:
    #     print node

    return nodes


def add_links(relationships):

    links = []

    for relationship in relationships:

        genre1 = Genre.query.filter_by(genre_id=relationship.genre1_id).first()
        genre2 = Genre.query.filter_by(genre_id=relationship.genre2_id).first()

        links.append({'source': genre1.name,
                      'target': genre2.name,
                      'value': relationship.shared_artists})

    # for link in links:
    #     print link

    return links


if __name__ == '__main__':

    connect_to_db(app)

    relationships = RelatedGenres.query.filter(RelatedGenres.shared_artists > 0).all()

    nodes = add_nodes(relationships)
    links = add_links(relationships)

    genres = json.dumps({"nodes": nodes,
                         "links": links})

    print genres
