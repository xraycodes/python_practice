class Song:
    """Class to represent song
    
    Attributes:
        title(str): The title of song
        artist(str): An artist object representing song creator
        duration(int): The duration of song in seconds. May be zero    
    """

def __init__(self, title, artist, duration=0):
    self.title = title
    self.artist = artist
    self.duration = duration


class Album:
    """Class to represent album,using its track list
    
    Attributes:
        album_name (str): The name of album
        year (int): The year album was released
        artist (Artist): The artist responsible for album
            If not specified, default will be 'various artist'
        tracks (list[song]): A list of songs in the album

    Methods:
        add_song: Used to add new song to album's track list 
    """
    
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist == None:
            self.artist = Artist("Various artist")
        else:
            self.artist = artist 

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds song to the track list

        Args:
            song (Song): A song to add
            position (Optional[int]): If specified, song added to that position
                in that track list- inserting between songs if necessary.
                Otherwise song will be added to end of list.
        """
        if position == None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes: 
        name (str):  Name of artist
        albums (list[album]: List of album by artist.
            List includes only those albums in collection, it is
            not an exhaustive list of artists published albums

    Methods:
        add_album: use to add new album to artists albums list
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add new album to the list.
        
        Args:
            album (Album): Album object to add to list. 
                If album already present, not added again.
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            #data row consist of artist, album, year, song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

if __name__ == '__main__':
    load_data()