

class Album:

    def __init__(self, band_id, band_name, band_url, album_id, album_name, album_url, genre_id, collected_count):
        self.band_id = band_id
        self.band_name = band_name
        self.band_url = band_url
        self.album_id = album_id
        self.album_name = album_name
        self.album_url = album_url
        self.genre_id = genre_id
        self.collected_count = collected_count
        self.fans = False

    def is_fill(self):
        return self.fans is not False

    def get_band_id(self):
        return self.band_id

    def get_band_url(self):
        return self.band_url

    def get_album_id(self):
        return self.album_id

    def get_album_url(self):
        return self.album_url

    def __repr__(self):
        return str(self.__dict__)
