from client_credentials_flow import genre_search, sp

def find_artists(genre, limit):

# Search the genre for ten artists
# Do an artist search on those ten artists
# Make artist info
# Sort artists by popularity
# Return name & image for top 4

    results = genre_search(genre, limit)

    artists = []
    for track in results:
        artist = track['artists'][0]

        new_artist = {
            'artist_id': artist['id'],
            'name': artist['name'],
            'images': artist.get('images'),
            'popularity': artist.get('popularity'),
            'href': artist['href'],
            'uri': artist['uri']

        }
