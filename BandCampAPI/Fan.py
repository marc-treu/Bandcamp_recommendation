

class Fan:

    def __init__(self, id, name, adr, location, bio, fav_genre, length_collection, length_wishlist):
        self.id = id
        self.name = name
        self.adr = adr
        self.location = location
        self.bio = bio
        self.fav_genre = fav_genre
        self.length_collection = length_collection
        self.length_wishlist = length_wishlist

    def get_collection(self):
        pass

    def __repr__(self):
        return str(self.__dict__)
