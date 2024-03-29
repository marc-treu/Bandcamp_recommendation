

class Fan:

    def __init__(self, fan_id, name, url, location, bio, fav_genre, length_collection, length_wishlist):
        self.fan_id = fan_id
        self.name = name
        self.url = url
        self.location = location
        self.bio = bio
        self.fav_genre = fav_genre
        self.length_collection = length_collection
        self.length_wishlist = length_wishlist
        self.collection = False

    def is_fill(self):
        return self.collection is not False

    def fill(self, list_album):
        self.collection = set()
        for album in list_album:
            self.collection.add(album.get_album_id())

    def get_collection(self):
        pass

    def get_id(self):
        return self.fan_id

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_length_collection(self):
        return self.length_collection

    def get_length_wishlist(self):
        return self.length_wishlist

    def __repr__(self):
        return str(self.__dict__)
