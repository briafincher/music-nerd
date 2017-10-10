import json
from pprint import pprint


nodes = []

links = []

for node in open('all_genre_nodes.txt'):
    node.strip()
    if node not in nodes:
        nodes.append(node)

for link in open('all_genre_links.txt'):
    link.strip()
    links.append(link)

genres = json.dumps({'nodes': nodes,
                     'links': links})

pprint(genres)

# print "{"
# print "'nodes': {},".format(nodes)
# print "'links': {}".format(links)
# print "}"
