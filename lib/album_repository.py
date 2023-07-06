from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    
    #def create
    #self, title, release_year, artist_id
    #SQL: INSERT INTO (title, release_year, artist_id) VALUES (....)

    def create(self, title, release_year, artist_id):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [title, release_year, artist_id])
    
    #def delete
    # self, id
    # DELETE FROM albums WHERE id = id

    def delete(self, id):
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])