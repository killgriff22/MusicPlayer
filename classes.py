from modules import *

class Song:
    def __init__(self, title, artist, album, track_number, year, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        self.year = str(year)
        self.length = length
    def __str__(self):
        return f'{self.title} by {self.artist} on {self.album}'

class Library:
    def __init__(self):
        self.database = None
    def load_library_from_disk(self):
        self.database = json.load(open('database.json'))
    def save_library_to_disk(self):
        json.dump(self.database, open('database.json', 'w'))
    def add_song(self, song: str):
        path = song[:]
        song = eyed3.load(song)
        song = Song(song.tag.title, song.tag.artist, song.tag.album, song.tag.track_num[0], song.tag.getBestDate(), song.info.time_secs)
        self.database['songs'].append({
                'title': song.title,
                'album': song.album,
                'track_number': song.track_number,
                'year': song.year,
                'length': song.length,
                'path': path
            })
    def discover_songs_from_source(self, source):
        for root, dirs, files in os.walk(source):
            for file in files:
                if file.endswith('.mp3'):
                    self.add_song(os.path.join(root, file))
                    sleep(0.001)
                    self.save_library_to_disk()

