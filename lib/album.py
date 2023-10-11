class Album:
    def __init__(self, id, title, release_year, artist_name):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_name = artist_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # def __repr__(self):
    #     return f"{self.id} - title: {self.title}, release year: {self.release_year}, artist name: {self.artist_name}"
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_name})"
    
    def __dict__(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_year': self.release_year,
        'artist_name': self.artist_name
    }