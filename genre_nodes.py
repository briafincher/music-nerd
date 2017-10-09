nodes = []

links = []

for node in open('all_genre_nodes.txt'):
    node.rstrip()
    if node not in nodes:
        links.append(node)

for link in open('all_genre_links.txt'):
    link.rstrip()
    links.append(link)

