from lib.album import Album
import json

class Albums_Repository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums_list = []
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_name'] )
            # print(json.dumps(album))
            albums_list.append(album.__dict__())
            print(albums_list)
            print("_______")
            print(type(albums_list))
        return albums_list
    
    def get_artists(self):
        artists = self._connection.execute('SELECT artist_name FROM albums')
        print (type(artists))
        return artists
    
    def add_artist(self, new_album_artist_name):
        self._connection.execute('INSERT INTO albums (title, artist_name,release_year) VALUES (%s, %s, %s)', ["NA", new_album_artist_name, 9999])
        return None


    def find(self, album_id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row['id'], row['title'], row['artist_name'], row['release_year'])
    
    def create(self, new_album_title, new_album_release_year, new_album_artist_name):
        self._connection.execute('INSERT INTO albums (title, artist_name,release_year) VALUES (%s, %s, %s)', [new_album_title, new_album_release_year, new_album_artist_name])
        return None
    
    def delete(self, album_title):
        self._connection.execute('DELETE FROM albums WHERE title = %s', [album_title])
        return None
    
    def update_release_year(self, album_title, new_release_year):
        self._connection.execute('UPDATE albums SET release_year = %s WHERE title = %s', [new_release_year, album_title])
        return None