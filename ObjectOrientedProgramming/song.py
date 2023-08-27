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


class Album():
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
        if artist = None:
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
        if position = None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)