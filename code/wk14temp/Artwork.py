import Artist

class Artwork:
    def __init__(self, title = 'None', year = 0, artist = Artist.Artist):
        self.title = title
        self.year = year
        self.artist = artist
    def print_info(new_artist):
        if new_artist.artist.death != -1:
            print(f'Artist: {new_artist.artist.name} ({new_artist.artist.birth}-{new_artist.artist.death})')
            print(f'Title: {new_artist.title}, {new_artist.year}')
        else:
            print(f'Artist: {new_artist.arist.name}, born {new_artist.arist.birth}')
            print(f'Title: {new_artist.title}, {new_artist.year}')

