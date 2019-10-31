

class Album:

    def __init__(self, band_id, band_name, album_id, album_name, url, genre_id, collected_count):
        self.band_id = band_id
        self.band_name = band_name
        self.album_id = album_id
        self.album_name = album_name
        self.url = url
        self.genre_id = genre_id
        self.collected_count = collected_count

    def get_collection(self):
        pass

    def get_band_id(self):
        return self.band_id

    def get_album_id(self):
        return self.album_id

    def get_url(self):
        return self.url

    def __repr__(self):
        return str(self.__dict__)
